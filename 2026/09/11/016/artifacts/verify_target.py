# Exact closed-loop replay with sympy rational functions in x1,x2,x3,y1,y2,y3.
import json
import sympy as sp

x1,x2,x3,y1,y2,y3 = sp.symbols("x1 x2 x3 y1 y2 y3")
xs=[x1,x2,x3]; ys=[y1,y2,y3]
B0=[[0,3,-2],[-3,0,2],[2,-2,0]]
I3=[[1 if i==j else 0 for j in range(3)] for i in range(3)]
W=[2,0,1,0,1,0,2]

def mut_ext(B,C,k):
    n=len(B); E=[r[:] for r in B]+[r[:] for r in C]
    N=2*n; Ep=[r[:] for r in E]
    for i in range(N):
        for j in range(n):
            if i==k or j==k: Ep[i][j]=-E[i][j]
            else: Ep[i][j]=E[i][j]+max(0,E[i][k])*max(0,E[k][j])-max(0,-E[i][k])*max(0,-E[k][j])
    return [r[:] for r in Ep[:n]],[r[:] for r in Ep[n:]]

X=[xs[i] for i in range(3)]
B=[r[:] for r in B0]; C=[r[:] for r in I3]
log=[]
for step,k in enumerate(W):
    col=[C[i][k] for i in range(3)]
    assert all(v>=0 for v in col) or all(v<=0 for v in col), f"sign-incoherent at step {step}"
    cpos=[max(v,0) for v in col]; cneg=[max(-v,0) for v in col]
    Mp=sp.Integer(1); Mm=sp.Integer(1)
    for i in range(3):
        if B[i][k]>0: Mp=Mp*X[i]**B[i][k]
        elif B[i][k]<0: Mm=Mm*X[i]**(-B[i][k])
    yp=ys[0]**cpos[0]*ys[1]**cpos[1]*ys[2]**cpos[2]
    yn=ys[0]**cneg[0]*ys[1]**cneg[1]*ys[2]**cneg[2]
    # correct principal-coeff exchange: x_k x_k' = y^[c]+ * M+ + y^[-c]+ * M-
    N=sp.simplify(yp*Mp+yn*Mm)
    Xnew=sp.simplify(N/X[k])
    # verify identity x_k * Xnew - N == 0
    chk=sp.simplify(X[k]*Xnew-N)
    assert chk==0, f"exchange identity fails step {step}: {chk}"
    X[k]=Xnew
    B,C=mut_ext(B,C,k)
    log.append({"step":step+1,"k":k+1,"B":[r[:] for r in B],"C":[r[:] for r in C],
                "num_terms":[len(sp.Poly(sp.together(X[i]).as_numer_denom()[0],xs+ys).terms()) if X[i]!=0 else 0 for i in range(3)]})
    print(f"step {step+1} k={k+1} terms={log[-1]['num_terms']} C={C}",flush=True)

print("final B:",B); print("final C:",C)
okC=all(v in (0,1) for row in C for v in row) and all(sum(r)==1 for r in C) and all(sum(C[i][j] for i in range(3))==1 for j in range(3))
sig=None
if okC:
    sig=[]
    for j in range(3):
        for i in range(3):
            if C[i][j]==1: sig.append(i)
print("sig:",sig)
PB=[[B0[sig[i]][sig[j]] for j in range(3)] for i in range(3)]
print("B==perm(B0):",B==PB)
for j in range(3):
    d=sp.simplify(X[j]-xs[sig[j]])
    print(f"x{j+1}-x0_{sig[j]+1}==0:",d==0)
    num,den=sp.together(X[j]).as_numer_denom()
    print("  expr:",X[j])
json.dump(log,open("output/artifacts/closed_loop_log.json","w"),indent=1)
json.dump([str(X[i]) for i in range(3)],open("output/artifacts/final_X.txt","w"),indent=1)
# F-polynomials at y-substitution x_i=1
Fs=[]
for i in range(3):
    Fi=sp.expand(X[i].subs({x1:1,x2:1,x3:1}))
    # check Laurent: denominator in y/x should be monomial
    num,den=sp.together(X[i]).as_numer_denom()
    print(f"F{j if False else i}: terms via Poly:",len(sp.Poly(Fi,ys).terms()),"den:",den)
    Fs.append(str(Fi))
json.dump(Fs,open("output/artifacts/Fpolys.txt","w"),indent=1)
print("saved")
