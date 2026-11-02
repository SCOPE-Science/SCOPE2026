# A factor-free univariate discriminant for the logarithmic determinants of \(2\times(m+1)\) matrices

## Finding
For every integer \(m\ge3\), the logarithmic \(A\)-discriminant of the Segre embedding \(\mathbb P^1\times\mathbb P^m\) is, up to a nonzero rational constant, **exactly** the ordinary discriminant of the explicitly defined degree-\(m+1\) polynomial \(P_m(U)\) below. No coefficient-only, resonance, boundary, or other extraneous polynomial factor occurs. This provides a single univariate discriminant representation for every rectangular \(2\times(m+1)\) format, not just a formula for its bidegree.

## Assumptions and scope
Work over \(\mathbb C\) with independent indeterminates \(a_0,\dots,a_m,b_0,\dots,b_m,s,v,\nu_1,\dots,\nu_m\). Let
\[
f(t_1,\ldots,t_m,U)=a_0+\sum_{i=1}^{m}a_it_i+U\left(b_0+\sum_{i=1}^{m}b_it_i\right).
\]
This is the general polynomial supported on \(\Delta_m\times\Delta_1\). Its associated projective toric variety is the Segre variety \(X=\mathbb P^m\times\mathbb P^1\) embedded by \(\mathcal O(1,1)\). Let \(\Lambda_m\) denote the primitive irreducible logarithmic \(A\)-discriminant in the sense of Goertz–Sturmfels–Telen: it is the equation of the closure of parameters at which the critical scheme of \(f^sU^v\prod_i t_i^{\nu_i}\) on \((\mathbb C^*)^{m+1}\setminus V(f)\) has a degenerate point, with \(s\ne0\).

Set \(S=s+\sum_{i=1}^m\nu_i\), \(A(U)=a_0+b_0U\), \(L_i(U)=a_i+b_iU\), \(G(U)=\prod_{i=1}^mL_i(U)\), and \(G_i(U)=\prod_{j\ne i}L_j(U)\). Define
\[
P_m(U)=\bigl(Sb_0U+vA(U)\bigr)G(U)
-UA(U)\sum_{i=1}^m\nu_ib_iG_i(U).
\]
The claim is the polynomial identity, up to multiplication by a nonzero element of \(\mathbb Q\),
\[
\boxed{\Lambda_m=\operatorname{Disc}_U(P_m).}
\]
The discriminant is the standard discriminant of the binary homogenization of a polynomial of generic degree \(m+1\); the equality concerns polynomials in **all** the coefficient and exponent variables. For a primitive-integral normalization, divide by the content and choose either sign. The two indicated polynomials have bidegree \(\bigl(2m(m+1),2m\bigr)\) in \((a,b)\) and \((s,v,\nu)\), respectively. The leading and constant coefficients of \(P_m\) are
\[
[U^{m+1}]P_m=b_0\left(\prod_{i=1}^mb_i\right)(s+v),\qquad
P_m(0)=v a_0\prod_{i=1}^ma_i.
\]
These endpoint formulas are included for reproducibility; their individual derivations are not a separate novelty claim.

## Proof
The cleared critical equations are
\[
\nu_i f+s t_i L_i(U)=0\quad(1\le i\le m),\qquad
v f+sU\left(b_0+\sum_i b_it_i\right)=0.
\]
Put \(N=\sum_i\nu_i\). Since \(f=A(U)+\sum_it_iL_i(U)\), summing the first \(m\) equations gives \(Sf=sA(U)\). On the dense open locus where \(s,S,A(U),U,\nu_i,L_i(U)\) are nonzero, the first equations solve uniquely as
\[
f=\frac{sA(U)}S,\qquad
t_i=-\frac{\nu_i A(U)}{S L_i(U)}.
\]
Substituting into the final critical equation and clearing \(G(U)\) yields \(P_m(U)=0\), and conversely each root satisfying the open conditions gives exactly one critical point. This is an isomorphism of the corresponding finite critical schemes on the open locus, not merely a bijection of their reduced supports: all eliminations divide by units, and the eliminated variables have linear equations with unit coefficients. Therefore a nonreduced critical point in that locus gives a multiple root of \(P_m\).

The toric exponent configuration affinely spans its full lattice, and its affine column matroid is connected. The hypersurface \(\Lambda_m\) is irreducible by [1, Theorem 1.1]. It has a dense subset disjoint from the coefficient-boundary and resonance divisors, because [1, Theorem 1.3] distinguishes its mixed coefficient/exponent factor from these one-sided factors. In particular, the preceding open-locus argument applies at a general point of \(\Lambda_m\). Hence the irreducible polynomial \(\Lambda_m\) divides \(\operatorname{Disc}_U(P_m)\) in the polynomial ring over \(\mathbb Q\).

We now rule out **every** extra factor using degrees, not a special-case factorization. The smooth Segre \(X\) has dimension \(d=m+1\) and degree \(\deg X=m+1\), since \((H_1+H_2)^{m+1}=(m+1)H_1H_2^m\). Its sectional curve has genus zero: adjunction with \(m\) general hyperplanes gives \(2g-2=-2\). Thus its Hurwitz degree is \(h=2\deg X+2g-2=2m\). By [1, Theorem 5.2 and Corollary 5.6], \(\Lambda_m\) has bidegree \((dh,h)=\bigl(2m(m+1),2m\bigr)\).

Every coefficient of \(P_m\), regarded as a polynomial in \(U\), is bihomogeneous of bidegree \((m+1,1)\); its generic \(U\)-degree is \(m+1\), as is seen from its leading coefficient above. The univariate polynomial discriminant is homogeneous of degree \(2m\) in those coefficients. It therefore has bidegree \(\bigl(2m(m+1),2m\bigr)\) provided it is not identically zero. To check nonvanishing for each \(m\), specialize \(\nu_1=\cdots=\nu_m=0\): then \(P_m=(sb_0U+vA(U))\prod_i L_i(U)\), which has \(m+1\) distinct linear factors for generic choices of \(a,b,s,v\). Thus its discriminant is nonzero. Since the nonzero polynomial \(\operatorname{Disc}_U(P_m)\) has the same bidegree as its irreducible factor \(\Lambda_m\), their quotient is a nonzero constant. This proves the identity for every \(m\ge3\).

## Verification
The standalone `verify_segre_logdiscriminant.py` reconstructs the eliminant in exact SymPy arithmetic. It checks: (i) the \(m=1\) specialization is precisely [1, equation (5)] after relabeling; (ii) for explicit integral coefficient/exponent choices in each \(1\le m\le8\), the polynomial has degree \(m+1\), nonzero discriminant and the specified endpoints; and (iii) the reconstructed critical equations give an exact rational-function identity \(\tfrac{SG}{s}\cdot E_U=P_m\). It returns `VERIFY_OK`. These finite checks are additional safeguards; the all-\(m\) statement is proved above by elimination and bidegree comparison, not by the finite test set.

## Relationship to prior work
Goertz, Sturmfels and Telen [1] introduce \(\Lambda_A\), prove irreducibility and bidegrees, and calculate the \(2\times3\) logarithmic determinant as a 441-term polynomial (Example 2.6). They also identify its eliminated coordinate's leading and trailing coefficients (Example 6.9) and remark that an elimination-polynomial discriminant **usually has \(\Lambda_A\) as its largest factor** (§8). The formula here uses those general theorems as premises but establishes the stronger factor-free identity uniformly for all \(2\times(m+1)\), \(m\ge3\), by an explicit \(m+1\)-degree eliminant and a sharp bidegree argument. The earlier \(2\times2\) and \(2\times3\) cases are calibration, not new results. Kayser, Kretschmer and Telen [2] study logarithmic discriminants for hyperplane arrangements with fixed coefficient arrangements; their reported statements do not cover this coefficient/exponent Segre family as formulated here.

## Limitations
The equality is up to nonzero rational scalar, and it is an equality of parameter polynomials—not a claim that every specialization has no spurious projective roots. The critical-point coordinate recovery applies only off the explicitly excluded divisors. No analogue for a general \(p\times q\) Segre format with \(p,q\ge3\), or for singular toric configurations, is proved. Historical priority is qualified: the identity may be implicit in a less obvious classical hyperdeterminant or likelihood-elimination result, despite the statement-level searches described in the review. Independent mathematical validation has not been performed.

## References
[1] M. Goertz, B. Sturmfels, S. Telen, *The Logarithmic A-Discriminant*, arXiv:2610.29204v1, first posted 2026-10-21; https://arxiv.org/html/2610.29204v1 . Theorems 1.1, 1.3, 5.2, Corollary 5.6, Examples 1.2, 2.6, 6.9, and §8.

[2] L. Kayser, A. Kretschmer, S. Telen, *Logarithmic discriminants of hyperplane arrangements*, arXiv:2410.11675; https://arxiv.org/abs/2410.11675 .
