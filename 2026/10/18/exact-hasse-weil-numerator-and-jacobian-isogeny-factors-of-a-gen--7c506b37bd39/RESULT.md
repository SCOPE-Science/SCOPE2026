# Exact Hasse–Weil numerator and Jacobian isogeny factors of a genus-nine Artin–Schreier curve

## Finding
Let \(X\) be the smooth projective normalization over \(\mathbb F_2\) of the plane equation
\[
(x^7+x)(z^4+z)=x^8+x^6+x^4+x^2+1.
\]
This is the ordinary genus-nine curve of Tafazolian, Proposition 7.2. Define the Hasse–Weil numerator \(L_X(T)\) by
\[
Z(X,T)=\exp\!\left(\sum_{n\ge1}\#X(\mathbb F_{2^n})\frac{T^n}{n}\right)
=\frac{L_X(T)}{(1-T)(1-2T)}.
\]
Then its **complete** numerator is
\[
\boxed{L_X(T)=(1-T+2T^2)(1+T+2T^2)^2(1-T^2+4T^4)
(1-2T^2+T^4-8T^6+16T^8).}
\]
In particular, \(\#\operatorname{Jac}(X)(\mathbb F_2)=L_X(1)=1024\). By the finite-field isogeny decomposition theorem, \(\operatorname{Jac}(X)\) is \(\mathbb F_2\)-isogenous to \(E_{+}\times E_{-}^{2}\times A_2\times A_4\), where the elliptic curves have Frobenius traces \(1\) and \(-1\), and the abelian factors of dimensions \(2\) and \(4\) have numerators \(1-T^2+4T^4\) and \(1-2T^2+T^4-8T^6+16T^8\), respectively.

## Assumptions and scope
Everything is over \(\mathbb F_2\) and its finite extensions; this is **one specified curve**, not a uniform formula for all members of Tafazolian's family. We use the published proof that the plane model defines the smooth projective curve and that its Artin–Schreier presentation above the ordinary elliptic curve
\[
E:\ y^2+xy=x^3+1
\]
has simple ramification at eight geometric points (Proposition 7.2 of the cited paper). The point at infinity on \(E\), the point \((0,1)\), and the pairs \((a,0)\) with \(a^3=1\) comprise the ramification points. Each has exactly one point of \(X\) above it because the Artin–Schreier poles are simple. All eight are rational over \(\mathbb F_4\), and four are rational over \(\mathbb F_2\).

## Proof
Put \(A(x)=x^7+x\) and \(B(x)=x^8+x^6+x^4+x^2+1\). The affine plane curve has equation \(A(x)(z^4+z)=B(x)\). At every point with \(A(x)\ne0\), its partial derivative with respect to \(z\) equals \(A(x)\), so the affine model is nonsingular there and the normalization gives a bijection on geometric points over that open set. At \(A(x)=0\), one has either \(x=0\) or \(x^3=1\). If \(x=0\), then \(B(x)=1\). If \(x^3=1\), then \(B(x)=x\ne0\). Thus no affine solution occurs there, and all points omitted by that open model are precisely the eight points above the known ramification divisor on \(E\).

Write \(N_n=\#X(\mathbb F_{2^n})\), and let \(q_n=2^n\). In \(\mathbb F_{q_n}\), the number of omitted rational points is
\[
b_n=2+2\gcd(3,q_n-1)=\begin{cases}4,&n\text{ odd},\\8,&n\text{ even}.\end{cases}
\]
Consequently, for every integer \(n\ge1\), the **exact** formula is
\[
N_n=b_n+\sum_{x,z\in\mathbb F_{q_n}}
\mathbf1\bigl(A(x)\ne0\ \text{and}\ A(x)(z^4+z)=B(x)\bigr).
\]
The supplied standalone, standard-library-only checker performs exhaustive field enumeration for \(n=1,\ldots,9\), with explicit binary irreducible defining polynomials, and independently enumerates the Artin–Schreier double-cover points on \(E\) using the absolute-trace criterion. The two computations agree term for term:
\[
(N_1,N_2,N_3,N_4,N_5,N_6,N_7,N_8,N_9)
=(4,8,4,24,44,8,116,312,508).
\]
Set \(s_n=q_n+1-N_n\), the \(n\)-th power sum of the reciprocal roots of \(L_X\). The first nine sums are
\[
(s_1,\ldots,s_9)=(-1,-3,5,-7,-11,57,13,-55,5).
\]
Newton's identity for \(L_X(T)=\sum_{i=0}^{18}c_iT^i\), with \(c_0=1\), gives
\[
 ic_i=-\sum_{k=1}^{i}c_{i-k}s_k\qquad(1\le i\le9).
\]
Thus \((c_0,\ldots,c_9)=(1,1,2,0,2,2,-4,-8,-11,5)\). Since the published genus is nine, the Weil functional equation supplies the remaining nine coefficients as \(c_{18-i}=2^{9-i}c_i\) for \(0\le i\le8\). Hence
\[
L_X(T)=1+T+2T^2+2T^4+2T^5-4T^6-8T^7-11T^8+5T^9
-22T^{10}-32T^{11}-32T^{12}+32T^{13}+64T^{14}
+256T^{16}+256T^{17}+512T^{18}.
\]
Integer-polynomial multiplication of the four displayed factors yields these same coefficients exactly, proving the factorization. Their pairwise coprime rational factors define a corresponding isogeny splitting over \(\mathbb F_2\), by the standard semisimplicity and Tate isogeny theorem for abelian varieties over finite fields. Evaluating at \(T=1\) gives \(L_X(1)=1024\).

## Verification
Run `python3 verify_zeta.py` in the same directory. The standalone script prints all nine exact counts, separately computed smooth-affine and ramification counts, nine Frobenius power sums, all nineteen numerator coefficients, factor-product equality and the Jacobian cardinality. Binary-polynomial irreducibility is checked using exact Euclidean polynomial gcds and Frobenius powering. No randomized computation, external tables, floating-point approximations, or third-party packages are needed. The script took two independently formulated enumerations from the published affine model and the elliptic Artin–Schreier model; it is a complete finite calculation up to the genus-nine functional-equation cutoff rather than a heuristic extrapolation.

## Relationship to prior work
Tafazolian's arXiv:2609.14830, Proposition 7.2, provides the equation, genus, ordinarity, automorphism group and branch description. These inputs are **not new**. Giulietti–Korchmáros (2015) investigate related automorphism groups and exhibit a distinct genus-nine example over \(\mathbb F_{16}\), discussed in Tafazolian's Proposition 5.8. The original source's inspected results do not give the displayed finite-field point sequence, its Hasse–Weil numerator, or its \(\mathbb F_2\)-Jacobian decomposition. Standard Artin–Schreier trace criteria, the Weil functional equation, and finite-field isogeny theory supply the methods; the explicit arithmetic classification of this particular newly displayed curve is the contribution.

## Limitations
The conclusion concerns this fixed \(\mathbb F_2\)-model and an **isogeny**, not an isomorphism or polarization-preserving decomposition of its Jacobian. The point sequence is explicitly checked only through degree nine; higher degrees follow from the proved genus-nine Weil identity, not separate brute-force counts. The large automorphism group and genus come from the cited source, not an independent reproof. An equivalent zeta computation could appear in unindexed or inaccessible older work; the searched sources do not establish exhaustive worldwide novelty.

## References
1. S. Tafazolian, *Nakajima-extremal Artin–Schreier covers of ordinary elliptic curves in characteristic 2*, arXiv:2609.14830 (first public version 2026-09-13), especially Sections 5 and 7, Proposition 7.2. https://arxiv.org/abs/2609.14830
2. M. Giulietti and G. Korchmáros, *Large 2-groups of automorphisms of algebraic curves over a field of characteristic 2*, Journal of Algebra 437 (2015), 262–302, https://doi.org/10.1016/j.jalgebra.2014.12.019 (related automorphism classifications; complete article not available for direct text inspection here).
3. M. Giulietti and G. Korchmáros, *Large 2-groups of automorphisms of algebraic curves over a field of characteristic 2*, related open preprint arXiv:1104.5159 (older group-theoretic examples).
