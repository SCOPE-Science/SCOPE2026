---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The claim is symbolic. The following checks were carried out.

1. The exact source presentation was used: \(g^3=1\), \(p^3=0\), \(gp=\lambda pg\), \(\Delta(p)=p\otimes1+g\otimes p\), together with the displayed action on \(x,y,z\).
2. The induced cross-relations \(gx=\lambda^2xg\), \(gy=\lambda yg\), \(gz=zg\), \(px=\lambda^2xp\), \(py=x+\lambda yp\), and \(pz=y+zp\) all survive the assignment \(x,y,p\mapsto0\), \(g\mapsto1\), \(z\mapsto z\).
3. The left integral \(t=3^{-1}(1+g+g^2)p^2\) maps to zero, hence the two-sided trace ideal \(T\) lies in the kernel.
4. On \(C=k[X,Y,Z]\) with \(X=x^3\), \(Y=y^3\), \(Z=z^3\), kernel membership implies \(F(0,0,z^3)=0\). Injectivity of \(k[Z]\to k[z]\) then gives \(F\in(X,Y)\).
5. The motivating source proves \(X^2=x^6\in T\) and \(Y^6=y^{18}\in T\), so \((X,Y)\subseteq\sqrt{T\cap C}\). Since \((X,Y)\) is prime and contains \(T\cap C\), equality follows.
6. The quotient map \(B/T\twoheadrightarrow k[z]\) gives \(\operatorname{GKdim}(B/T)\ge1\); the source proves the opposite inequality.

No finite enumeration, floating-point computation, or unproved extrapolation is used. The verification does not determine the nonreduced ideal \(T\cap C\) or the full algebra structure of \(B/T\).
