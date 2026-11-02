"""Independent exact finite-field checks for shifted quartic squarefreeness."""
from itertools import product

class F:
    def __init__(self, p, mod=None):
        self.p=p
        self.mod=mod
        self.d=len(mod)-1 if mod is not None else 1
        self.q=p**self.d
        self.coeff=[tuple((i//(p**j))%p for j in range(self.d)) for i in range(self.q)]
        index={v:i for i,v in enumerate(self.coeff)}
        self.add=[[index[tuple((a[j]+b[j])%p for j in range(self.d))] for b in self.coeff] for a in self.coeff]
        self.neg=[index[tuple(-v[j]%p for j in range(self.d))] for v in self.coeff]
        self.mul=[]
        for a in self.coeff:
            row=[]
            for b in self.coeff:
                c=[0]*(2*self.d-1)
                for j in range(self.d):
                    for k in range(self.d):
                        c[j+k]=(c[j+k]+a[j]*b[k])%p
                if mod is not None:
                    for t in range(len(c)-1,self.d-1,-1):
                        for k in range(self.d):
                            c[t-self.d+k]=(c[t-self.d+k]-c[t]*mod[k])%p
                row.append(index[tuple(c[:self.d])])
            self.mul.append(row)
        self.one=1
        self.inv=[0]*self.q
        for a in range(1,self.q):
            self.inv[a]=next(b for b in range(1,self.q) if self.mul[a][b]==1)
        self.squares={self.mul[a][a] for a in range(1,self.q)}
        self.chi=[0 if a==0 else (1 if a in self.squares else -1) for a in range(self.q)]

    def squarefree(self, f):
        a,m,inv=self.add,self.mul,self.inv
        der=[m[i%self.p][f[i]] for i in range(1,len(f))]
        def strip(x):
            while x and x[-1]==0: x.pop()
            return x
        x=strip(f[:]); y=strip(der)
        while y:
            x,y=y,x
            if not y: break
            d=inv[y[-1]]
            while len(x)>=len(y):
                c=m[x[-1]][d]
                off=len(x)-len(y)
                for j in range(len(y)):
                    x[off+j]=a[x[off+j]][self.neg[m[c][y[j]]]]
                strip(x)
        return len(x)==1

def predict(F,u):
    q=F.q
    add,mul=F.add,F.mul
    sixteen=16%F.p
    uu=mul[u][u]
    S=0
    for s in range(1,q):
        s3=mul[mul[s][s]][s]
        v=add[uu][F.neg[mul[sixteen][s3]]]
        S+=F.chi[v]
    return q**4-2*q**3+q*(q-1)-2*S

def run():
    fields=[F(3), F(5), F(7),F(11),F(13), F(3,[1,0,1]),F(5,[2,0,1]),F(3,[2,2,0,1])]
    settings={3:None,5:None,7:None,11:[1,2,3,4,5,6,7,8,9,10],13:[1,2,3,4,5,6,7,8,9,10,11,12],9:None,25:[],27:[]}
    tested=0; counts=0; shifts=0; ext=0; mv=0
    for field in fields:
        q=field.q
        us=list(range(1,q)) if settings[q] is None else settings[q]
        vals=[]
        for u in range(1,q):
            vals.append(predict(field,u))
        avg=q**4-2*q**3+q*(q-1)+2
        assert sum(vals)==(q-1)*avg, (q,vals,avg)
        variance=sum((v-avg)**2 for v in vals)//(q-1)
        assert variance==(8*q if q%3==1 else 0),(q, variance)
        mv+=q-1
        for u in us:
            for v in ([0,1] if q<=9 else [0]):
                if v>=q: continue
                total=0
                for b,c,d,e in product(range(q),repeat=4):
                    f=[e,d,c,b,1]
                    g=[field.add[e][v],field.add[d][u],c,b,1]
                    if field.squarefree(f) and field.squarefree(g): total+=1
                pred=predict(field,u)
                assert total==pred, (q,u,v,total,pred)
                tested+=1; counts+=q**4
        print('FIELD_OK',q,'shifts',len(us)*(2 if q<=9 else 1),'prediction_values',sorted(set(vals)),'variance',variance)
    print('VERIFY_OK field_orders=',[f.q for f in fields],'direct_shifts=',tested,'quartic_tests=',counts,'slope_moment_terms=',mv)
if __name__=='__main__':run()
