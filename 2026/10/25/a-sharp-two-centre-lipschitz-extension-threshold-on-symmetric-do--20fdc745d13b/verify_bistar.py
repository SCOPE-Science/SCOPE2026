from fractions import Fraction as F
from itertools import product
from scipy.optimize import linprog

def test(m,t):
    t=F(t); D=t*t+(F(2)+F(2,m))*t+4
    z=(t+2)*(t+1)/D
    alpha=min(F(1),z)
    norm=max(F(1), 2+t-(t+F(2,m))*alpha, (2+t)*abs(2*alpha-1)/t)
    predicted=(2+t)*(t+4-F(2,m))/D if (m==2 or t<=F(2*m,m-2)) else 2-F(2,m)
    assert norm==predicted,(m,t,alpha,norm,predicted)
    # All leaf-supported signed coefficients: tree earthmover norm=sum |leaf masses| + t |left-cluster sum|.
    # Linear program in arbitrary 2*(2m) coefficients, with 2 hubs and constant constraints.
    n=2*m; from scipy.optimize import linprog
    # exhaustive sign choices for the formula |v|_1+t |sum left|; maximize over 2^(n+1) choices
    import numpy as np
    rows=[]; rhs=[]
    # variables 2n hub coeffs and lambda
    for hub in (0,1):
       for leaf in (range(m) if hub==0 else range(m,n)):
          for signs in product((-1,1),repeat=n+1):
             r=np.zeros(2*n+1)
             for j in range(n):r[hub*n+j]= signs[j]+(t*signs[n] if j<m else 0)
             r[-1]=-1
             rows.append(r);rhs.append(signs[leaf]+(t*signs[n] if leaf<m else 0))
    for signs in product((-1,1),repeat=n+1):
       r=np.zeros(2*n+1)
       for j in range(n):
          c= signs[j]+(t*signs[n] if j<m else 0)
          r[j]+=c/t;r[n+j]-=c/t
       r[-1]=-1;rows.append(r);rhs.append(0)
    eq=np.zeros((2,2*n+1));eq[0,:n]=1;eq[1,n:2*n]=1
    res=linprog(np.r_[np.zeros(2*n),1.],A_ub=np.asarray(rows),b_ub=np.asarray(rhs),A_eq=eq,b_eq=np.ones(2),bounds=[(None,None)]*(2*n)+[(1,None)],method='highs')
    assert res.success,(m,t,res.message)
    assert abs(res.fun-float(norm))<1e-8,(m,t,res.fun,norm)
    return m,str(t),str(norm)

if __name__=='__main__':
  count=0
  for m in (2,3,4):
   for t in (F(1,3),F(1),F(3),F(12)):
    print(test(m,t),flush=True);count+=1
  print('BISTAR_EXACT_FORMULA_LP_OK',count)
