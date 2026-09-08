import json
L=[(2,2),(2,3),(3,3),(3,4),(4,4),(2,4)]
def eul(a,b,c,d): return a*c+b*d-3*a*d
def q(a,b): return a*a+b*b-3*a*b
def weyl_root(a,b):
    # reduce by reflections to fundamental or real; return path
    path=[(a,b)]
    for _ in range(20):
        c1=2*a-3*b; c2=2*b-3*a
        if c1<=0 and c2<=0: return 'imag-fund',path
        if q(a,b)==1: return 'real',path
        if q(a,b)>1: return 'notroot',path
        if c1>0: a=3*b-a
        else: b=3*a-b
        path.append((a,b))
    return 'unknown',path
out={}
for d in L:
    a,b=d
    subs=[(e1,e2) for e1 in range(a+1) for e2 in range(b+1) if (0,0)<(e1,e2)<(a,b)]
    worst=[]; ok=True
    for e in subs:
        f=(a-e[0],b-e[1])
        x=eul(*e,*f); y=eul(*f,*e)
        # canonical split needs ext both ways =0; Euler<0 forces ext>0
        if not (x<0 and y<0): ok=False; worst.append((e,f,x,y))
    typ,path=weyl_root(a,b)
    out[str(d)]={'q':q(a,b),'type':typ,'path':path,'nsub':len(subs),'allEulerNeg':ok,'exceptions':worst}
print(json.dumps(out,indent=1))
json.dump(out,open('output/artifacts/s1_euler.json','w'),indent=1)
