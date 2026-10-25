# Primitive polynomial solutions in the exceptional quadratic-form family

## Finding

For every integer \(n\ne0\) and every integer \(c\), define
\[
F_c(X,Y,Z)=X^2+Y^2+2XY+cYZ=(X+Y)^2+cYZ.
\]
There are explicit nonhomogeneous polynomials \(x,y,z,t\in\mathbb Z[u,v]\) such that
\[
\gcd_{\mathbb Z[u,v]}(x,y,z)=1,
\qquad t^2=nxyzF_c(x,y,z).
\]
This proves the polynomial-coprimality assertion for the exceptional coefficient family \(a=d=0,\ b=2\) singled out in Conjecture 2.4(a) of Gawron and Ulas.

Put
\[
U=u+1,\qquad A=2Uv,\qquad B=U^2-2nv^2,\qquad C=U^2+2nv^2.
\]
The identity
\[
C^2=2nA^2+B^2
\]
holds in \(\mathbb Z[u,v]\).

If \(c\ne0\), take
\[
x=-cnA^2,\qquad y=-cB^2,\qquad z=C^2,
\qquad t=c^2n^2A^3BC.
\]
If \(c=0\), take instead
\[
x=nA^2,\qquad y=B^2,\qquad z=C^2,
\qquad t=nABC(nA^2+B^2).
\]

## Assumptions and scope

Here \(n\) is any nonzero integer, \(c\) is any integer, and the polynomial variables are \(u,v\). The gcd is taken in \(\mathbb Z[u,v]\), so it excludes both nonconstant common polynomial factors and a common integer content greater than one. The result concerns only the exceptional family \(F_c=(X+Y)^2+cYZ\); it does not assert that the remaining cases of Conjecture 2.4(a) are resolved.

## Proof

First,
\[
C^2-B^2=(U^2+2nv^2)^2-(U^2-2nv^2)^2
=8nU^2v^2=2nA^2,
\]
which proves \(C^2=2nA^2+B^2\).

Suppose \(c\ne0\). Substitution gives
\[
\begin{aligned}
F_c(x,y,z)
&=c^2(nA^2+B^2)^2-c^2B^2C^2\\
&=c^2\big((nA^2+B^2)^2-B^2(2nA^2+B^2)\big)\\
&=c^2n^2A^4.
\end{aligned}
\]
Also \(xyz=c^2nA^2B^2C^2\). Consequently
\[
nxyzF_c(x,y,z)=c^4n^4A^6B^2C^2=(c^2n^2A^3BC)^2=t^2.
\]

If \(c=0\), then \(F_0(x,y,z)=(x+y)^2=(nA^2+B^2)^2\) and \(xyz=nA^2B^2C^2\). Hence
\[
nxyzF_0(x,y,z)=n^2A^2B^2C^2(nA^2+B^2)^2
=\big(nABC(nA^2+B^2)\big)^2=t^2.
\]

It remains to verify coprimality. Since \(n\ne0\), neither \(U=u+1\) nor \(v\) divides \(B=U^2-2nv^2\). As \(A=2Uv\), this gives \(\gcd_{\mathbb Q[u,v]}(A,B)=1\). In both branches, \(x\) and \(y\) are constant multiples of \(A^2\) and \(B^2\), respectively, so they have no common nonconstant polynomial factor. Finally, \(z=C^2\) has coefficient \(1\) on \(u^4\), hence content one. Thus no integer greater than one divides all coefficients of \(x,y,z\), and \(\gcd_{\mathbb Z[u,v]}(x,y,z)=1\).

## Verification

The standalone script `verify.py` uses exact sparse multivariate polynomial arithmetic with integer coefficients to check the conic identity and both branches of \(t^2=nxyzF_c(x,y,z)\) symbolically in \(n,c,u,v\). It prints `VERIFY_OK`. The coprimality claim is proved algebraically above; the script does not purport to certify that gcd argument.

## Relationship to prior work

Gawron and Ulas, Theorem 2.1, treat the nonexceptional coefficient cases and give polynomial solutions whose gcd over \(\mathbb Q[u,v]\) is one. For the exceptional case \(a=d=0,\ b=2\), they instead prove the existence of infinitely many primitive integer solutions. In Remark 2.3 they state that they were unable to obtain polynomial solutions with gcd one in \(\mathbb Z[u,v]\), and Conjecture 2.4(a) asks for such a solution. The formulas above supply that polynomial solution for every value of the remaining coefficient \(c\) and every nonzero integer \(n\). This does not settle the conjecture for the other coefficient cases or add a new claim about its integer-solution part.

## Limitations

The theorem is confined to \(F_c=(X+Y)^2+cYZ\). No independent audit has been performed. The symbolic checker verifies identities, while the proof—not finite testing—establishes them for all allowed integers \(n,c\).

## References

1. M. Gawron and M. Ulas, “On primitive integer solutions of the Diophantine equation \(t^2=G(x,y,z)\) and related results,” arXiv:1502.07307v1, first posted 25 February 2015; published in *Journal of Number Theory* 159 (2016), 101–122. https://arxiv.org/abs/1502.07307. DOI: https://doi.org/10.1016/j.jnt.2015.07.012. See Theorem 2.1, Remark 2.3, and Conjecture 2.4.
