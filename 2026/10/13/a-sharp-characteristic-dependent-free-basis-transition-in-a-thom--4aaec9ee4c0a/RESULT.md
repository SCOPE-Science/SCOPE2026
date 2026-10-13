# A sharp characteristic-dependent free-basis transition in a Thom–Sebastiani line–curve arrangement

## Finding

Let \(k\) be an algebraically closed field, let \(m\geq 2\), and let \(\ell_1,\ldots,\ell_m\in k[x,y]\) be nonzero, pairwise nonproportional linear forms. Fix positive integers \(k_1,\ldots,k_m\), set \(d=\sum_{j=1}^m k_j\), and write
\[
G=\prod_{j=1}^m\ell_j,\qquad P=\prod_{j=1}^m\ell_j^{k_j},\qquad H=P-z^d,\qquad F=GH.
\]
Let \(D(F)=\{\delta\in\operatorname{Der}_k(k[x,y,z]):\delta(F)\in(F)\}\). The degree of a homogeneous derivation means its homogeneous polynomial coefficient degree.

**Theorem.** In characteristic zero or positive characteristic \(p\nmid d\), \(F\) is reduced and \(D(F)\) has a homogeneous free basis of coefficient degrees \((1,m-1,d)\). In positive characteristic \(p\mid d\), \(F\) is reduced precisely when at least one \(k_j\) is not divisible by \(p\); in that reduced case \(D(F)\) has a homogeneous free basis of coefficient degrees \((0,1,d+m-1)\). When \(p\mid d\) and all \(k_j\) are divisible by \(p\), \(H\) is a nontrivial \(p\)-th power and this reduced-divisor statement does not apply.

In every reduced \(p\mid d\) case, \(F_z=0\). The polar map of the original reduced equation has image contained in the line \(Z=0\) of the dual projective plane. Every tangent line to \(H=0\) at a smooth geometric point passes through the fixed exterior point \([0:0:1]\). For \(p\nmid d\), the latter universal tangent-concurrency property fails on a dense open subset of the smooth locus of \(H=0\). These assertions hold for every admissible choice of coefficients and weights, not merely for generic forms.

## Assumptions and scope

The forms \(\ell_j\) are pairwise nonproportional **over the working field**, including after any desired reduction. There is no choice of integral model or assertion of good reduction of a fixed characteristic-zero model in this statement. The parameter \(d\) is a positive integer and is interpreted as a scalar in \(k\) when divided or tested for vanishing. The freeness assertion concerns the full logarithmic derivation module \(D(F)\), not merely Jacobian syzygies or a splitting by an Euler field. In positive characteristic, coefficient degrees \((0,1,d+m-1)\) are **not** identified with the usual characteristic-zero pair of exponents.

## Proof

**1. Reducedness.** Since \(H\) is monic up to sign in \(z\), with leading coefficient \(-1\), no nonconstant polynomial in \(k[x,y]\) divides \(H\); in particular \(\gcd(G,H)=1\). The binary form \(G\) is squarefree. If \(\operatorname{char}k=0\), or if \(p\nmid d\), then \(H_z=-dz^{d-1}\) and \(\gcd(H,H_z)=1\), so \(H\) is squarefree.

If \(p\mid d\), \(H_z=0\). Over the perfect field \(k\), both derivatives of the binary form \(P\) vanish if and only if \(P\) is a \(p\)-th power, equivalently if and only if each \(k_j\) is divisible by \(p\). In that case \(H=(P_0-z^{d/p})^p\) for \(P=P_0^p\). Otherwise, at least one of \(P_x,P_y\) is nonzero. Since it belongs to \(k[x,y]\), its gcd with \(H\) is one; hence \(H\) is squarefree. This establishes the exact reducedness boundary.

**2. A binary logarithmic frame.** Write \(\ell_1=ax+by\) and put
\[
L=\prod_{j=2}^m\ell_j,\quad U=x\partial_x+y\partial_y,\quad
A=L(-b\partial_x+a\partial_y),\quad Z=\partial_z.
\]
The derivation \(A\) annihilates \(\ell_1\), while \(\ell_j\mid A(\ell_j)\) for each \(j>1\). Consequently there are homogeneous forms \(\alpha,\beta\in k[x,y]\) of coefficient degree \(m-2\) such that
\[
A(G)=\alpha G,\qquad A(P)=\beta P.
\]
A direct two-by-two determinant computation gives
\[
\det(U,A,Z)=L(ax+by)=G.
\]
These identities remain true in every characteristic, even when several integer weights become zero in \(k\).

**3. A basis when \(d\ne0\) in \(k\).** Let
\[
E=U+zZ,\qquad B=A+\frac{z\beta}{d}Z,\qquad
T=z^{d-1}U+PZ.
\]
The homogeneous coefficient degrees are respectively \(1,m-1,d\). Using the homogeneity of \(P\) and \(G\), one obtains
\[
E(F)=(d+m)F,\quad B(F)=(\alpha+\beta)F,\quad
T(F)=mz^{d-1}F.
\]
For example, \(T(H)=dz^{d-1}P-dz^{d-1}P=0\); also \(B(H)=\beta P-(z\beta/d)dz^{d-1}=\beta H\). Subtracting suitable column multiples of \(Z\) in the determinant gives the exact identity
\[
\det(E,B,T)=(P-z^d)\det(U,A,Z)=GH=F.
\]
There is **no hidden nonunit multiplier**, so the determinant works for every admissible coefficient specialization with \(d\) invertible.

**4. A basis when \(p\mid d\).** In this case \(H_z=0\) and \(U(H)=dP=0\). Define
\[
W=HA.
\]
Then \(Z(F)=0\), \(U(F)=mF\), and
\[
W(F)=H\,A(GH)=\bigl(\alpha H+\beta P\bigr)F.
\]
The coefficient degrees of \(Z,U,W\) are \(0,1,d+m-1\), and their determinant is again **exactly** the reduced equation:
\[
\det(Z,U,W)=H\det(U,A,Z)=F.
\]
The same identity holds formally for a nonreduced \(F\), but the theorem carefully restricts logarithmic freeness to the reduced regime of Step 1.

**5. Why either determinant proves an entire basis.** Let \(f\) be any reduced homogeneous polynomial over \(k\), and let three homogeneous logarithmic derivations have coefficient determinant \(u f\), with \(u\in k^\times\). They are independent over the fraction field. Given any logarithmic derivation \(\delta\), Cramer's rule expresses \(\delta\) in this frame with coefficients whose denominator is \(uf\). For each irreducible factor \(g\) of \(f\), reducing modulo \(g\) at its smooth generic point makes all logarithmic derivation vectors tangent to \(g=0\); the corresponding three-column determinants with \(\delta\) replacing one column therefore vanish modulo \(g\). Since the factors of \(f\) are distinct, their product divides every Cramer numerator. Thus the coefficients are polynomials. This proves freeness in arbitrary characteristic without using the characteristic-zero Euler splitting or Jacobian-length formulas.

**6. Polar geometry.** The equality \(F_z=0\) in the wild case is immediate from \(G_z=P_z=0\) and \(p\mid d\); hence every defined polar image has last coordinate zero. At any smooth point of \(H=0\), the tangent line is \(H_xx'+H_yy'+H_zz'=0\), where the primed coordinates are variables and \(H_z=0\), so it contains \([0:0:1]\). This point does not belong to \(H=0\), because \(H(0,0,1)=-1\). In the tame case \(H_z=-dz^{d-1}\) is nonzero wherever \(z\ne0\); that open set intersects the smooth locus densely, and its tangents do not contain \([0:0:1]\). This proves the asserted geometric distinction.

## Verification

The companion file `verify.py` is a dependency-free Python 3 exact polynomial-ring checker. From the extracted files, execute `python3 verify.py`. It constructs polynomial coefficients over rational numbers and representative prime fields, checks all displayed logarithmic identities, verifies \(\det=F\) exactly in thirteen nontrivial examples, and separately checks the tame versus wild \(z\)-gradient behavior. Its final line is `VERIFY_OK: exact coefficient-ring logarithmic identities and unit determinants in 13 cases`. The parameter-uniform proof is Steps 1–6; finite checks are supplemental only. The freeness result is not based on numerical sampling.

For a concrete infinite family, in each prime characteristic \(p\), take \(m=2\), \(\ell_1=x\), \(\ell_2=y\), \(k_1=1\), \(k_2=p-1\). Then \(F=xy(xy^{p-1}-z^p)\) is reduced and has the explicitly certified free basis degrees \((0,1,p+1)\), whereas the characteristic-zero version of that same exponent pattern has coefficient degrees \((1,1,p)\). At \(p=2\) its nonlinear component is the smooth conic \(xy-z^2\).

## Relationship to prior work

Dimca, Ilardi, Pokora and Sticlaru proved characteristic-zero freeness, with the two standard exponents \((m-1,d)\), for precisely this line–curve construction (their Theorem 1.5). Their proof uses characteristic-zero Tjurina-number and Jacobian-syzygy arguments, and does not state the present complete positive-characteristic reducedness classification, exact wild basis \((0,1,d+m-1)\), or the wild tangent-concurrency transition. The characteristic-zero part of the theorem above merely supplies an elementary determinant-basis perspective on their established result and is not claimed as novel by itself. General Saito-type determinant criteria, including more recent positive-characteristic perspectives on Jacobian-kernel sheaves, supply methodology rather than the present specific parameter-uniform classification. No priority or independent verification claim is made.

## Limitations

Only the specified reduced homogeneous plane divisors over algebraically closed fields are covered. When \(p\mid d\) and all weights are divisible by \(p\), the displayed polynomial is nonreduced; no freeness assertion for its reduced support is made. No statement is made about flat liftings, arbitrary coordinate changes preserving a chosen integral model, all modular reductions of published coefficient choices, freeness of the *Jacobian syzygy module*, or a classification of singularity types. The universal concurrency statement concerns the component \(H=0\), not tangents to the union of the line components. No independent mathematical audit has been performed.

## References

1. A. Dimca, G. Ilardi, P. Pokora, G. Sticlaru, *Construction of free curves by adding lines to a given curve*, arXiv:2301.01117 (first public version 2023-01-03), Theorem 1.5 and its proof in §4.2; https://arxiv.org/html/2301.01117v4 .
2. D. Faenzi, M. Jardim, J. Vallès, *A generalized Saito freeness criterion*, arXiv:2407.14082 (2024); https://arxiv.org/abs/2407.14082 .
3. D. Faenzi, M. Jardim, J. Vallès, *Saito criterion and its avatars*, arXiv:2402.08305 (2024); https://arxiv.org/abs/2402.08305 .
