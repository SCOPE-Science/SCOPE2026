"""Exact finite-field checks for primitive-idempotent products in spin-factor Jordan algebras.

This is an independent finite enumerator, not a substitute for the general proof.
Run: python3 verify.py
"""
from itertools import product


class F:
    def __init__(self, p, extension=1, mu=None):
        self.p=p; self.k=extension; self.q=p**extension
        assert self.k in (1,2)
        if self.k==2:
            assert mu is not None and pow(mu,(p-1)//2,p)==p-1
            # z^2=mu, irreducible over the prime subfield
            self.mu=mu
        else: self.mu=None
        self.add=[[self._add(a,b) for b in range(self.q)] for a in range(self.q)]
        self.mul=[[self._mul(a,b) for b in range(self.q)] for a in range(self.q)]
        self.neg=[next(b for b in range(self.q) if self.add[a][b]==0) for a in range(self.q)]
        self.inv=[None]+[next(b for b in range(1,self.q) if self.mul[a][b]==1) for a in range(1,self.q)]
        self.quad=[self.mul[a][a] for a in range(self.q)]
        self.character=[0 if a==0 else (1 if self.power(a,(self.q-1)//2)==1 else -1) for a in range(self.q)]
    def _add(self,a,b):
        if self.k==1: return (a+b)%self.p
        p=self.p; return ((a%p+b%p)%p)+p*((a//p+b//p)%p)
    def _mul(self,a,b):
        if self.k==1: return a*b%self.p
        p=self.p; x,y=a%p,a//p; u,v=b%p,b//p
        return (x*u+self.mu*y*v)%p+p*((x*v+y*u)%p)
    def power(self,a,n):
        r=1
        while n:
            if n&1:r=self.mul[r][a]
            a=self.mul[a][a];n//=2
        return r
    def dot(self, xs,ys):
        z=0
        for x,y in zip(xs,ys): z=self.add[z][self.mul[x][y]]
        return z
    def Q(self, xs, diag):
        z=0
        for x,d in zip(xs,diag):z=self.add[z][self.mul[d][self.quad[x]]]
        return z
    def nondegenerate_count(self,r,delta,t):
        assert r>=1 and delta!=0
        q=self.q;chi=self.character
        if r%2==0:
            eps=chi[self.mul[(-1 if ((r//2)%2) else 1)%self.p][delta]]
            return q**(r-1)+(q-1)*eps*q**(r//2-1) if t==0 else q**(r-1)-eps*q**(r//2-1)
        if t==0:return q**(r-1)
        sign=(-1 if ((r-1)//2)%2 else 1)%self.p
        return q**(r-1)+chi[self.mul[self.mul[sign][delta]][t]]*q**((r-1)//2)
    def check(self,diag,verbose=False):
        d=len(diag);assert d>=3
        det=1
        for a in diag:det=self.mul[det][a]
        assert det!=0
        quarter=self.inv[(4%self.p)]
        elems=list(product(range(self.q),repeat=d))
        idempotents=[u for u in elems if self.Q(u,diag)==quarter]
        inv2=self.inv[2%self.p]
        pair_fibers={v:0 for v in elems}
        for u in idempotents:
            for v in idempotents:
                w=tuple(self.mul[inv2][self.add[a][b]] for a,b in zip(u,v))
                pair_fibers[w]+=1
        minus_det=self.neg[det]
        n_obstructions=0
        for w,fiber in pair_fibers.items():
            a=self.Q(w,diag)
            if not any(w):
                pred=self.nondegenerate_count(d,det,quarter)
            elif a:
                deltaperp=self.mul[det][self.inv[a]]
                pred=self.nondegenerate_count(d-1,deltaperp,self.add[quarter][self.neg[a]])
            else:
                pred=self.q*self.nondegenerate_count(d-2,minus_det,quarter)
            assert pred==fiber,(self.q,d,diag,w,pred,fiber)
            if fiber==0:n_obstructions+=1
        exp_obs=0 if d>=4 or self.character[minus_det]==1 else self.q*self.q-1
        assert n_obstructions==exp_obs,(self.q,d,diag,n_obstructions,exp_obs)
        assert sum(pair_fibers.values())==len(idempotents)**2
        print('PASS', 'field=',self.q, 'dimension=',d,'diag=',diag,'primitive_idempotents=',len(idempotents),
              'ordered_pairs=',len(idempotents)**2,'two_factor_values=',len(elems)-n_obstructions,
              'excluded=',n_obstructions)


def main():
    tested=0
    for p in (3,5,7,11):
        Fp=F(p)
        non_square=next(x for x in range(1,p) if Fp.character[x]==-1)
        for d in (3,4):
            for last in (1,non_square):
                Fp.check((1,)*(d-1)+(last,));tested+=1
    for p,mu in ((3,2),(5,2)):
        Fq=F(p,2,mu)
        non_square=next(a for a in range(1,Fq.q) if Fq.character[a]==-1)
        for last in (1,non_square):
            Fq.check((1,1,last));tested+=1
    print('VERIFY_OK',tested,'complete configurations')

if __name__=='__main__':main()
