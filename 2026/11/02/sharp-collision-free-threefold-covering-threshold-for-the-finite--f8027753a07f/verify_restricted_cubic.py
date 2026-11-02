#!/usr/bin/env python3
"""Independent finite-field check of collision-free cubic moment representations.

Run: python verify_restricted_cubic.py
Only uses the Python standard library. In quadratic field cases x=a+p*b
with u*u=non-square D in F_p. This is a finite check, not an infinite proof.
"""

class Field:
    def __init__(self,p,D=None):
        self.p=p; self.D=D; self.q=p if D is None else p*p
        self.zero=0; self.one=1
        self.vals=range(self.q)
        self.adds=[[self.add(a,b) for b in self.vals] for a in self.vals]
        self.muls=[[self.mul(a,b) for b in self.vals] for a in self.vals]
        self.squares={self.muls[a][a] for a in self.vals}
        self.chi=[0 if a==0 else (1 if a in self.squares else -1) for a in self.vals]
        self.cubes=[self.mul(self.mul(a,a),a) for a in self.vals]

    def add(self,a,b):
        p=self.p
        if self.D is None:return (a+b)%p
        return (a%p+b%p)%p+p*((a//p+b//p)%p)
    def neg(self,a):
        p=self.p
        if self.D is None:return (-a)%p
        return (-a%p)+p*((-(a//p))%p)
    def mul(self,a,b):
        p=self.p
        if self.D is None:return (a*b)%p
        a0,a1=a%p,a//p;b0,b1=b%p,b//p
        return (a0*b0+self.D*a1*b1)%p+p*((a0*b1+a1*b0)%p)
    def pow(self,a,k):
        z=1
        while k:
            if k&1:z=self.muls[z][a]
            a=self.muls[a][a]; k//=2
        return z
    def const(self,k):return k%self.p
    def inv(self,a):
        assert a; return self.pow(a,self.q-2)

SMALL={
  5:([1,2,3,4],[0,3,4]),
  7:([1,2,5,6],[2,3,4]),
  11:([],[3,10]),
  13:([4,6,7,9],[2]),
  17:([],[14]),
  19:([4,6,9,10,13,15],[]),
}

def check(p,D=None):
    F=Field(p,D);q=F.q; M=F.muls; A=F.adds;neg=F.neg
    c2,c3,c4,c6,c9=(F.const(t) for t in (2,3,4,6,9))
    inv3=F.inv(c3);inv6=F.inv(c6);inv9=F.inv(c9)
    # Independent direct enumeration of ordered triples.
    all_count=[[0]*q for _ in range(q)]
    dist_count=[[0]*q for _ in range(q)]
    for x in F.vals:
      for y in F.vals:
        xy=A[x][y]; zcube0=A[F.cubes[x]][F.cubes[y]]
        for z in F.vals:
          s=A[xy][z]; w=A[zcube0][F.cubes[z]]
          all_count[s][w]+=1
          if len({x,y,z})==3:dist_count[s][w]+=1
    # Formula from polarization, quadratic-character sums, and collision subtraction.
    for s in F.vals:
      s3=F.cubes[s]
      s3by9=M[s3][inv9]
      for w in F.vals:
        z=M[c4][M[A[w][neg(s3)]][inv3]]
        base=q if w==s3 else 0
        R=base+q-1
        for u in range(1,q):
          uminus2s=A[u][neg(M[c2][s])]
          term=M[M[u][u]][M[uminus2s][uminus2s]]
          P=A[term][M[z][u]]
          R+=F.chi[P]
        h=0
        for t in F.vals:
          tm1=A[t][neg(s)]
          RHS=A[s3][neg(M[c6][M[t][M[tm1][tm1]]])]
          if RHS==w:h+=1
        Rd=R-3*h+2*(w==s3by9)
        assert R==all_count[s][w],('all',p,D,s,w,R,all_count[s][w])
        assert Rd==dist_count[s][w],('distinct',p,D,s,w,Rd,dist_count[s][w])
    missing={(s,w) for s in F.vals for w in F.vals if dist_count[s][w]==0}
    if q in SMALL:
        zeros, ratios = SMALL[q]
        expect={(0,w) for w in zeros}
        for s in range(1,q):
           for a in ratios:expect.add((s,M[F.cubes[s]][a]))
        assert missing==expect,(q,missing^expect)
    else:
        assert q>=23 and not missing,(q,list(missing)[:8])
    print('PASS', 'q='+str(q), 'field='+ ('prime' if D is None else 'quadratic'),
          'targets='+str(q*q), 'missing='+str(len(missing)))
    return q*q

if __name__=='__main__':
    fibers=0
    for p in (5,7,11,13,17,19,23,29,31):fibers+=check(p)
    fibers+=check(5,2)
    fibers+=check(7,3)
    print('VERIFY_OK distinct_and_unrestricted_fibers=',fibers,'fields=11')
