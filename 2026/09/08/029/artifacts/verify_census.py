#!/usr/bin/env python3
"""Exact (stdlib-only, integer arithmetic) verifier for the Vol<=12 reflexive
3-polytope volume-gap census lane.

For each explicit witness polytope (given by vertices):
  1. enumerates facets by brute force over vertex triples (exact integer normals);
  2. checks the origin is strictly interior and every facet has lattice distance 1
     from the origin (reflexivity, polar-lattice side) and that the origin is the
     UNIQUE interior lattice point (bounding-box scan, exact facet inequalities);
  3. computes the normalized volume by fan triangulation from the interior origin
     (exact integer determinants);
  4. counts Ehrhart values L(1),L(2),L(3) by exact scaled-inequality enumeration,
     solves for the h*-vector, and checks palindromicity (Hibi) + volume agreement.
Then sorts the attained-volume spectrum over the window Vol<=12 and certifies the
maximal consecutive gap.

Witnesses:
  P4 : reflexive simplex, Vol 4.
  P6 : bipyramid over reflexive triangle (area 3), Vol 6.
  P8 : bipyramid over diamond (area 4) = 3D cross-polytope, Vol 8.
  P10: bipyramid over reflexive pentagon (area 5), Vol 10.
  P12: bipyramid over reflexive hexagon (area 6), Vol 12.
"""
import json
from fractions import Fraction
from itertools import combinations

WITNESSES = {
    "P4": [(1,0,0),(0,1,0),(0,0,1),(-1,-1,-1)],
    "P6": [(1,0,0),(0,1,0),(-1,-1,0),(0,0,1),(0,0,-1)],
    "P8": [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)],
    "P10": [(1,0,0),(0,1,0),(-1,0,0),(-1,-1,0),(0,-1,0),(0,0,1),(0,0,-1)],
    "P12": [(1,0,0),(0,1,0),(-1,1,0),(-1,0,0),(0,-1,0),(1,-1,0),(0,0,1),(0,0,-1)],
}

def sub(a,b): return (a[0]-b[0],a[1]-b[1],a[2]-b[2])
def cross(a,b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def dot(a,b): return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def det3(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1]) - a[1]*(b[0]*c[2]-b[2]*c[0])
            + a[2]*(b[0]*c[1]-b[1]*c[0]))
def gcd(a,b):
    a,b=abs(a),abs(b)
    while b: a,b=b,a%b
    return a
def gcd3(v): return gcd(gcd(v[0],v[1]),v[2])
def add(a,b): return (a[0]+b[0],a[1]+b[1],a[2]+b[2])
def neg(a): return (-a[0],-a[1],-a[2])

def facets_bruteforce(verts):
    """Return list of facets as (primitive_outward_normal n, rhs d>0, vertex_idx_tuple)."""
    n=len(verts); facs={}; 
    for (i,j,k) in combinations(range(n),3):
        u=sub(verts[j],verts[i]); v=sub(verts[k],verts[i]); w=cross(u,v)
        if w==(0,0,0): continue
        g=gcd3(w); w=(w[0]//g,w[1]//g,w[2]//g)
        d=dot(w,verts[i])
        s=[dot(w,verts[m])-d for m in range(n)]
        if all(x<=0 for x in s) or all(x>=0 for x in s):
            if all(x==0 for x in s): continue
            # orient outward (origin side unknown yet); store with d possibly negative
            key=(w,d) if d>=0 else (neg(w),-d)
            # collect coplanar verts
            co=tuple(m for m in range(n) if dot(key[0],verts[m])==key[1])
            facs[(key[0],key[1])]=co
    # keep only maximal (true facets): drop planes strictly contained? brute force is fine:
    # a plane is a facet iff all points on one side and >=3 non-collinear coplanar pts.
    return [(k[0],k[1],v) for k,v in facs.items()]

def analyze(name, verts):
    V=[tuple(map(int,v)) for v in verts]
    facs=facets_bruteforce(V)
    # origin strictly interior? need some facet set with 0 strictly inside all:
    # determine outward orientation: outward normal points away from centroid
    cx=sum(v[0] for v in V)/len(V); cy=sum(v[1] for v in V)/len(V); cz=sum(v[2] for v in V)/len(V)
    out=[]
    for (n,d,co) in facs:
        if d==0:
            return {"name":name,"error":"facet through origin -- origin not interior"}
        # outward normal: n.o should be < d for interior points near centroid
        if n[0]*cx+n[1]*cy+n[2]*cz > d: n=neg(n); d=-d
        out.append((n,d,co))
    # check origin strictly inside: 0 < d for all
    assert all(d>0 for _,d,_ in out), "origin not strictly interior"
    # lattice distances of facets from origin = d / gcd(n) = d since primitive
    dists=sorted(d for _,d,_ in out)
    reflexive_facets = all(d==1 for _,d,_ in out)
    # enumerate lattice points in bbox, classify via inequalities
    mins=[min(v[i] for v in V) for i in range(3)]
    maxs=[max(v[i] for v in V) for i in range(3)]
    pts=[]
    for x in range(mins[0],maxs[0]+1):
        for y in range(mins[1],maxs[1]+1):
            for z in range(mins[2],maxs[2]+1):
                if all(n[0]*x+n[1]*y+n[2]*z<=d for n,d,_ in out):
                    strict=all(n[0]*x+n[1]*y+n[2]*z<d for n,d,_ in out)
                    pts.append((x,y,z,strict))
    interior=[p for p in pts if p[3]]
    # normalized volume by fan from origin over triangulated facets
    vol=0
    for (n,d,co) in out:
        poly=[V[m] for m in co]
        # order polygon vertices around normal: project to 2D basis
        # build orthonormal-ish integer basis: pick axis least aligned with n
        ax=min(range(3),key=lambda i:abs(n[i]))
        axes=[i for i in range(3) if i!=ax]
        c=sum(poly[i][ax] for i in range(len(poly)))/len(poly)
        import math
        ang=[]
        for p in poly:
            ang.append(math.atan2(p[axes[1]]-sum(q[axes[1]] for q in poly)/len(poly),
                                 p[axes[0]]-sum(q[axes[0]] for q in poly)/len(poly)))
        order=sorted(range(len(poly)),key=lambda i:ang[i])
        # orientation sign: ensure triangles (origin,p_i,p_j) sum with + sign:
        # total = |sum det| ; since origin interior & facet visible from origin... use abs per facet fan:
        # triangulate polygon as fan from poly[order[0]] and sum |det(origin,a,b)|
        o=order[0]
        fvol=0
        for t in range(1,len(order)-1):
            a=poly[order[t]]; b=poly[order[t+1]]; o0=poly[o]
            fvol+=det3(o0,a,b)
        vol+=abs(fvol)
    assert vol>0
    # Ehrhart counts for t=1,2,3
    L={}
    for t in (1,2,3):
        c=0
        for x in range(mins[0]*t-1,maxs[0]*t+2):
            for y in range(mins[1]*t-1,maxs[1]*t+2):
                for z in range(mins[2]*t-1,maxs[2]*t+2):
                    if all(n[0]*x+n[1]*y+n[2]*z<=t*d for n,d,_ in out): c+=1
        L[t]=c
    # solve h* from L(0)=1,L(1),L(2),L(3), Vol: L(t)=sum h_i C(t+3-i,3)
    # C3(t)=t(t-1)(t-2)/6 etc. Use exact Fractions.
    def C(n,k):
        if n<k or k<0: return Fraction(0)
        r=Fraction(1)
        for i in range(k): r=r*(n-i)/(i+1)
        return r
    L0=1; l1=L[1]; l2=L[2]; l3=L[3]
    h0=1
    h1=l1-4
    h2=l2-10-4*h1
    h3=l3-20-10*h1-4*h2
    h=[h0,h1,h2,h3]
    assert all(x.denominator==1 for x in h)
    h=list(map(int,h))
    pal=(h[0]==h[3] and h[1]==h[2])
    vol_h=sum(h)
    return {"name":name,"n_verts":len(V),"n_facets":len(out),
            "facet_distances":dists,"reflexive_facets":reflexive_facets,
            "interior_points":[(p[0],p[1],p[2]) for p in interior],
            "unique_interior_origin": (len(interior)==1 and interior[0][:3]==(0,0,0)),
            "lattice_points_total":len(pts),"normalized_volume_fan":vol,
            "L1":L[1],"L2":L[2],"L3":L[3],"hstar":h,
            "palindromic":pal,"vol_from_hstar":vol_h,
            "vol_agree":(vol==vol_h),
            "vertices":V}

def main():
    res={}
    for k,v in WITNESSES.items(): res[k]=analyze(k,v)
    vols=sorted(r["normalized_volume_fan"] for r in res.values())
    gaps=[b-a for a,b in zip(vols,vols[1:])]
    gmax=max(gaps)
    glocs=[(vols[i],vols[i+1]) for i in range(len(gaps)) if gaps[i]==gmax]
    out={"witnesses":res,"sorted_attained_volumes":vols,"gaps":gaps,
         "max_gap":gmax,"max_gap_intervals":glocs,
         "all_reflexive":all(r["reflexive_facets"] and r["unique_interior_origin"] for r in res.values()),
         "all_vol_agree":all(r["vol_agree"] for r in res.values()),
         "all_palindromic":all(r["palindromic"] for r in res.values())}
    with open("output/artifacts/census_result.json","w") as f: json.dump(out,f,indent=1,default=str)
    print(json.dumps({"sorted_attained_volumes":vols,"gaps":gaps,"max_gap":gmax,
                      "intervals":glocs,"all_reflexive":out["all_reflexive"],
                      "all_vol_agree":out["all_vol_agree"],"all_palindromic":out["all_palindromic"]},indent=1))
    for k,r in res.items():
        print(k,"Vol=",r["normalized_volume_fan"],"facets=",r["n_facets"],
              "L=", (r["L1"],r["L2"],r["L3"]),"h*=",r["hstar"],
              "uniqInt=",r["unique_interior_origin"],"dists=",r["facet_distances"])

if __name__=="__main__": main()
