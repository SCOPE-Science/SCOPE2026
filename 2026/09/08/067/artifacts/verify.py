from fractions import Fraction
from math import gcd
import itertools

def det3(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1]) - a[1]*(b[0]*c[2]-b[2]*c[0]) + a[2]*(b[0]*c[1]-b[1]*c[0]))

def sub(a,b): return (a[0]-b[0],a[1]-b[1],a[2]-b[2])
def add(a,b): return (a[0]+b[0],a[1]+b[1],a[2]+b[2])

def facets_bruteforce(verts):
    # verts: list of tuples
    n=len(verts)
    uniq=list(dict.fromkeys(verts))
    verts=uniq; n=len(verts)
    planes={}  # (nx,ny,nz,d) normalized primitive outward? collect
    for i,j,k in itertools.combinations(range(n),3):
        a,b,c=verts[i],verts[j],verts[k]
        ab=sub(b,a); ac=sub(c,a)
        nx=ab[1]*ac[2]-ab[2]*ac[1]
        ny=ab[2]*ac[0]-ab[0]*ac[2]
        nz=ab[0]*ac[1]-ab[1]*ac[0]
        if (nx,ny,nz)==(0,0,0): continue
        d=nx*a[0]+ny*a[1]+nz*a[2]
        # check coplanarity set + sidedness
        vals=[nx*v[0]+ny*v[1]+nz*v[2]-d for v in verts]
        if all(v<=0 for v in vals) or all(v>=0 for v in vals):
            # supporting plane; find all verts on plane
            on=tuple(sorted([t for t in range(n) if vals[t]==0]))
            # only keep maximal (facets); use plane normalized
            # normalize (n,d) by gcd and sign canonical later
            g=gcd(gcd(abs(nx),abs(ny)),gcd(abs(nz),abs(d)))
            if g==0: g=1
            key=None
            # canonical sign: first nonzero among (nx,ny,nz,d) positive? but keep both orientations merged
            # store with both signs merged: normalize so that d>0, or d==0 then first nonzero n positive
            sx,sy,sz,sdd=nx//g,ny//g,nz//g,d//g
            if sdd<0 or (sdd==0 and (sx,sy,sz)<(0,0,0)):
                sx,sy,sz,sdd=-sx,-sy,-sz,-sdd
            key=(sx,sy,sz,sdd)
            if key not in planes:
                planes[key]=on
            else:
                # merge coplanar: union
                planes[key]=tuple(sorted(set(planes[key])|set(on)))
    # filter maximal: remove planes whose vertex set is subset of another with same geometry? bruteforce triples of same facet give same key so merged already.
    # Remove non-facet (edge) planes: a true facet must have at least 3 non-collinear points and be maximal; edges would also be supporting? In 3D, edge supporting planes are not unique; our enumeration from triples: edge-only planes arise only if third point collinear? Actually any plane containing an edge and with all points on one side - for a 3-polytope there are infinitely many such planes rotating around edge, but our discrete triples only give planes through 3 vertices, which for edge + third vertex off the edge-facet gives facet plane. A plane through edge + vertex not in adjacent facet would cut through. So all keys found should be facets. But filter dimension: need >=3 non-collinear (by construction) and polygon area>0.
    return planes

def outward_facets(verts, planes):
    # orient so interior (centroid) satisfies <n,x> < d with d>0? compute centroid
    cx=sum(v[0] for v in verts)/len(verts); cy=sum(v[1] for v in verts)/len(verts); cz=sum(v[2] for v in verts)/len(verts)
    out=[]
    for (nx,ny,nz,d),on in planes.items():
        # canonical key has d>=0; interior should satisfy n.c < d (strict) if d>0
        cval=nx*cx+ny*cy+nz*cz-d
        if cval>0:
            nx,ny,nz,d=-nx,-ny,-nz,-d
        out.append(((nx,ny,nz,d),on))
    return out

def point_in_poly(pt, facets):
    # facets outward: <n,x> <= d, strict < for interior
    for (nx,ny,nz,d),on in facets:
        if nx*pt[0]+ny*pt[1]+nz*pt[2]>d: return False
    return True
def point_interior(pt, facets):
    for (nx,ny,nz,d),on in facets:
        if nx*pt[0]+ny*pt[1]+nz*pt[2]>=d: return False
    return True

def lattice_points(verts, facets, bound=6):
    xs=[v[0] for v in verts]; ys=[v[1] for v in verts]; zs=[v[2] for v in verts]
    pts=[]
    for x in range(min(xs),max(xs)+1):
        for y in range(min(ys),max(ys)+1):
            for z in range(min(zs),max(zs)+1):
                if point_in_poly((x,y,z),facets): pts.append((x,y,z))
    return pts

def fan_volume_from_origin(verts, facets):
    total=0
    detail=[]
    for (nx,ny,nz,d),on in facets:
        poly=[verts[i] for i in on]
        # order polygon vertices cyclically: project onto plane basis
        # triangulate fan from poly[0]: need correct ordering? fan from one vertex of convex polygon works regardless of order? No - need polygon order. Instead triangulate by: for all triples containing poly[0]? Simpler: compute facet pyramid volume via 2D? Alternative robust: 3D volume fan from origin = sum over triangulated facet with consistent orientation: use polygon centroid method: pick pivot = poly[0], and sum |det| over (pivot, pj, pj+1) after ordering cyclically.
        # Order cyclically: compute facet centroid, basis e1,e2 in plane, sort by angle (exact via quadrant+cross sign, no floats? use floats for ordering only, volume exact)
        cx=sum(p[0] for p in poly)/len(poly); cy=sum(p[1] for p in poly)/len(poly); cz=sum(p[2] for p in poly)/len(poly)
        # normal
        import math
        # build orthonormal-ish basis via floats
        nn=(float(nx),float(ny),float(nz))
        # pick arbitrary vector not parallel
        av=(1.0,0.0,0.0) if abs(nn[0])<0.9*math.sqrt(nn[0]**2+nn[1]**2+nn[2]**2) else (0.0,1.0,0.0)
        # e1 = av x n, e2 = n x e1
        def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
        e1=cross(av,nn); e2=cross(nn,e1)
        angs=[]
        for p in poly:
            dx,dy,dz=p[0]-cx,p[1]-cy,p[2]-cz
            angs.append(math.atan2(dx*e2[0]+dy*e2[1]+dz*e2[2], dx*e1[0]+dy*e1[1]+dz*e1[2]))
        order=sorted(range(len(poly)),key=lambda i: angs[i])
        # fan from order[0]
        v0=poly[order[0]]
        for t in range(1,len(order)-1):
            v1=poly[order[t]]; v2=poly[order[t+1]]
            vol=abs(det3(v0,v1,v2))
            total+=vol
            detail.append((v0,v1,v2,vol))
    return total, detail

def volume_from_vertex(verts, facets):
    # second triangulation: fan from verts[0]: tetrahedralize polytope by triangulating each facet not containing v0, forming tetras (v0, tri). Sum |det(vi-v0,...)|.
    v0=verts[0]
    # need facet triangulations as above (cyclic order)
    import math
    def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
    total=0
    for (nx,ny,nz,d),on in facets:
        if 0 in on: continue
        poly=[verts[i] for i in on]
        cx=sum(p[0] for p in poly)/len(poly); cy=sum(p[1] for p in poly)/len(poly); cz=sum(p[2] for p in poly)/len(poly)
        nn=(float(nx),float(ny),float(nz))
        av=(1.0,0.0,0.0) if abs(nn[0])<0.9*math.sqrt(nn[0]**2+nn[1]**2+nn[2]**2) else (0.0,1.0,0.0)
        e1=cross(av,nn); e2=cross(nn,e1)
        angs=[]
        for p in poly:
            dx,dy,dz=p[0]-cx,p[1]-cy,p[2]-cz
            angs.append(math.atan2(dx*e2[0]+dy*e2[1]+dz*e2[2], dx*e1[0]+dy*e1[1]+dz*e1[2]))
        order=sorted(range(len(poly)),key=lambda i: angs[i])
        p0=poly[order[0]]
        for t in range(1,len(order)-1):
            p1=poly[order[t]]; p2=poly[order[t+1]]
            vol=abs(det3(sub(p0,v0),sub(p1,v0),sub(p2,v0)))
            # tetra (v0,p0,p1,p2) volume*6 = |det|
            total+=vol
    # Note: this sums only facets opposite v0? For convex polytope, fan from vertex v0 over opposite facets gives full volume. Facets containing v0 give degenerate (det 0)? We skip them. Correct.
    return total

def analyze(name, verts):
    planes=facets_bruteforce(verts)
    of=outward_facets(verts, planes)
    # reflexivity: all d==1?
    ds=sorted([f[0][3] for f in of])
    origin_inside = point_interior((0,0,0), of)
    reflexive = origin_inside and all(d==1 for d in ds)
    pts=lattice_points(verts, of)
    interior=[p for p in pts if point_interior(p, of)]
    v1,_=fan_volume_from_origin(verts, of)
    v2=volume_from_vertex(verts, of)
    # dual verts = facet normals (since d=1)
    dual=None; dv1=None; dv2=None; din=None
    if reflexive:
        dual=list(dict.fromkeys([(f[0][0],f[0][1],f[0][2]) for f in of]))
        dplanes=facets_bruteforce(dual)
        dof=outward_facets(dual, dplanes)
        dds=sorted([f[0][3] for f in dof])
        din = point_interior((0,0,0), dof) and all(d==1 for d in dds)
        dv1,_=fan_volume_from_origin(dual, dof)
        dv2=volume_from_vertex(dual, dof)
    return {"name":name,"verts":verts,"facets":of,"ds":ds,"reflexive":reflexive,"npts":len(pts),"interior":interior,"vol_origin":v1,"vol_vertex":v2,"dual":dual,"dual_vol_origin":dv1,"dual_vol_vertex":dv2,"dual_reflexive":din}

def show(r):
    print("="*70)
    print(r["name"], "verts=",r["verts"])
    print(" facet ds:",r["ds"],"reflexive:",r["reflexive"],"npts:",r["npts"],"interior:",r["interior"])
    print(" vol(origin-fan)=",r["vol_origin"],"vol(vertex-fan)=",r["vol_vertex"])
    if r["dual"] is not None:
        print(" dual verts:",r["dual"])
        print(" dual vol(origin)=",r["dual_vol_origin"],"dual vol(vertex)=",r["dual_vol_vertex"],"dual refl:",r["dual_reflexive"])
        print(" Mahler (normalized) =",r["vol_origin"]*r["dual_vol_origin"])

# Candidates
P4=[(1,0,0),(0,1,0),(0,0,1),(-1,-1,-1)]
# bipyramid bases in z=0
T=[(1,0,0),(0,1,0),(-1,-1,0)]  # triangle area 3
D=[(1,0,0),(0,1,0),(-1,0,0),(0,-1,0)]  # diamond area 4
P5=[(1,0,0),(0,1,0),(-1,0,0),(-1,-1,0),(0,-1,0)]  # pentagon?
H=[(1,0,0),(1,1,0),(0,1,0),(-1,0,0),(-1,-1,0),(0,-1,0)]  # hexagon?
def bipy(base):
    v=[(x,y,0) for (x,y,_) in base]+[(0,0,1),(0,0,-1)]
    return v

for name,verts in [("P4-simplex",P4),("P6-bipyr-tri",bipy(T)),("P8-bipyr-dia",bipy(D)),("P10-bipyr-pent",bipy(P5)),("P12-bipyr-hex",bipy(H))]:
    show(analyze(name,verts))
