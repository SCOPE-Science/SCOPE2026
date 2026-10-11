# Exposed-face saturation criterion for the \(T_G\) constant
## Finding
Let \(X\) be a finite-dimensional real Banach space with \(\dim X\ge2\). For the Ahmad--Xie--Li constant
\[
T_G(X)=\sup\left\{\sqrt{\|x+y\|\,\|2x-y\|}:x,y\in S_X,\ \|x-y\|=1}\right\},
\]
one has \(T_G(X)=2\) exactly when there are \(u,v,w\in S_X\) and \(f,g\in S_{X^*}\) satisfying
\[
u=v+w,\qquad f(u)=f(v)=1,\qquad g(u)=g(w)=1.
\]
Thus upper-bound saturation is an exposed-face phenomenon: \(u,v\) occupy one exposed face and \(u,w\) another.

For the Day--James plane \(X_D=(\mathbb R^2,N)\),
\[
N(s,t)=\max\{|s|,|t|,|s-t|\},
\]
the criterion gives \(T_G(X_D)=2\). Since the classical James constant is \(J(X_D)=3/2\), this plane is uniformly non-square. Hence the published implication \(T_G(X)<2\Rightarrow X\) uniformly non-square has no converse, already in dimension two.

## Assumptions and scope
All spaces are real and finite-dimensional, with dimension at least two. The characterization concerns exact attainment of the universal upper bound \(2\). Finite dimensionality is used only to ensure that the supremum defining \(T_G\) is attained on the compact admissible set. No assertion is made for an infinite-dimensional space in which the supremum may fail to be attained.

For the Day--James corollary, \(N(s,t)=\max\{|s|,|t|,|s-t|\}\), equivalently the norm is \(\ell_\infty\) on the same-sign quadrants and \(\ell_1\) on the opposite-sign quadrants.

## Proof
The defining paper proves the universal bound \(T_G(X)\le2\). Suppose first that \(T_G(X)=2\). By finite-dimensional compactness there is an admissible pair \(x,y\in S_X\), \(\|x-y\|=1\), at which the supremum is attained. Each factor is at most \(2\):
\[
\|x+y\|\le2,
\qquad
\|2x-y\|=\|x+(x-y)\|\le2.
\]
Their product is \(4\), so both inequalities are equalities. Put \(u=x\), \(v=y\), and \(w=x-y\). Then \(u,v,w\in S_X\) and \(u=v+w\).

Choose a norm-one functional \(f\in X^*\) supporting \(x+y\), so \(f(x+y)=\|x+y\|=2\). Since \(f(x)\le1\) and \(f(y)\le1\), equality forces \(f(u)=f(v)=1\). Likewise \(2x-y=x+(x-y)=u+w\) has norm \(2\); a norm-one supporting functional \(g\) satisfies \(g(u)=g(w)=1\). This proves necessity.

Conversely, suppose \(u,v,w\in S_X\) and \(f,g\in S_{X^*}\) satisfy the stated relations. Set \(x=u\) and \(y=v\). Then \(x-y=w\), hence \(\|x-y\|=1\). Moreover
\[
2\ge\|u+v\|\ge f(u+v)=2
\]
and, because \(2u-v=u+w\),
\[
2\ge\|2u-v\|=\|u+w\|\ge g(u+w)=2.
\]
Thus this admissible pair gives \(\sqrt{\|x+y\|\,\|2x-y\|}=2\), and the universal upper bound yields \(T_G(X)=2\).

For \(X_D\), take
\[
u=(1,1),\qquad v=(1,0),\qquad w=(0,1).
\]
All three vectors have Day--James norm \(1\), and \(u=v+w\). The coordinate functionals \(f(s,t)=s\) and \(g(s,t)=t\) have dual norm \(1\) because \(|s|\le N(s,t)\) and \(|t|\le N(s,t)\), with equality on \(v\) and \(w\). They satisfy the criterion, so \(T_G(X_D)=2\). Kato, Maligranda, and Takahashi computed \(J(X_D)=3/2\). From the definition of the James constant, \(J(X)<2\) is equivalent to uniform non-squareness, so \(X_D\) is uniformly non-square.

## Verification
The critical equalities are exact and require no numerical approximation. The forward direction uses only compact attainment, the two triangle inequalities, and supporting functionals. The reverse direction checks the defining constraints directly. In the Day--James example,
\[
N(1,1)=N(1,0)=N(0,1)=1,
\]
while
\[
N(2,1)=N(1,2)=2.
\]
Thus the witness itself also verifies \(T_G(X_D)\ge2\), independently of the exposed-face reformulation; the published universal bound supplies the reverse inequality.

## Relationship to prior work
Ahmad, Xie, and Li introduced \(T_G\), proved \(1\le T_G(X)\le2\), showed that finite-dimensional rotund spaces satisfy \(T_G(X)<2\), and proved the one-way implication \(T_G(X)<2\Rightarrow X\) uniformly non-square. Their proof of the rotund result detects one equality segment when \(T_G=2\), but it does not state the two-supporting-face equivalence above or the failure of the converse to uniform non-squareness. Their conclusion explicitly leaves values on further specific spaces for future investigation.

Kato, Maligranda, and Takahashi computed \(J(X_D)=3/2\) for the Day--James \(\ell_\infty-\ell_1\) plane. That known value supplies the uniform-non-squareness premise; it does not determine \(T_G\). The new face criterion supplies the missing implication and produces a canonical endpoint-saturation counterexample.

## Limitations
The equivalence is stated only in finite dimension because compactness guarantees an extremizing pair. For infinite-dimensional spaces, the same argument gives the face criterion whenever the supremum \(T_G(X)=2\) is attained, but no general attainment claim is made. The literature comparison cannot exclude an unindexed computation of the same Day--James value; the closest inspected sources and semantic searches did not reveal one.

## References
1. A. Ahmad, H. Xie, and Y. Li, *Some new geometric constants in Banach spaces*, Advances in Fixed Point Theory 12 (2022), Article 9, DOI 10.28919/afpt/7588. Published 2022-08-25; primary 2010 AMS classification 46B20.
2. M. Kato, L. Maligranda, and Y. Takahashi, *On James and Jordan--von Neumann constants and the normal structure coefficient of Banach spaces*, Studia Mathematica 144 (2001), 275--295, DOI 10.4064/sm144-3-5.
