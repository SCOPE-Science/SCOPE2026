# The genus-six boundary curve over \(\mathbb F_3\) has a squared Frobenius polynomial

## Finding

Let \(X/\mathbb F_3\) be the smooth projective curve with function field
\[
\mathbb F_3(x,y),\qquad y^3-y=x+\frac{1}{x^3-x}.
\]
The complete numerator of its Hasse–Weil zeta function, with convention
\(Z(X,T)=L_X(T)/((1-T)(1-3T))\), is
\[
\boxed{L_X(T)=1+16T^3+118T^6+432T^9+729T^{12}}
=\big[(1-T+3T^2)(1+T-2T^2+3T^3+9T^4)\big]^2.
\]
In particular \(\#\operatorname{Jac}(X)(\mathbb F_3)=L_X(1)=1296\).
Let \(E/\mathbb F_3\) denote the smooth elliptic curve \(v^2=u^3+u^2+2\). Let \(A/\mathbb F_3\) denote the unique isogeny class of simple ordinary abelian surfaces with Frobenius characteristic polynomial
\[
P_A(U)=U^4+U^3-2U^2+3U+9.
\]
Then
\[
\boxed{\operatorname{Jac}(X)\sim_{\mathbb F_3}(E\times A)^2.}
\]
For every integer \(n\ge1\) with \(3\nmid n\), the rational point count satisfies the exact identity
\(\#X(\mathbb F_{3^n})=3^n+1\).

## Assumptions and scope

The base field is exactly \(\mathbb F_3\); no assertion is made for arbitrary coefficients in the parameter family or for all arithmetic twists. The characteristic-three curve is the parameter \(c=1\) instance of Tafazolian's ordinary genus-six boundary family [1, Proposition 8.7]. The four poles of the rational function, \(0,1,-1,\infty\), are rational and simple. The separable degree-three Artin–Schreier cover therefore has exactly one rational, totally ramified place above each pole in every finite extension. Its genus, calculated from the four conductor-two contributions by Riemann–Hurwitz, is \(g=(3-1)(4(1+1)-2)/2=6\). These facts also independently recover the genus stated in [1].

## Proof

**1. Infinite nonmultiples-of-three point-count identity.** Write \(f(x)=x+1/(x^3-x)\). In characteristic three,
\(f(x+1)=f(x)+1\); the denominator is invariant under translation by one. For \(K=\mathbb F_{3^n}\), the absolute trace therefore obeys
\[
\operatorname{Tr}_{K/\mathbb F_3}(f(x+1))
=\operatorname{Tr}_{K/\mathbb F_3}(f(x))+n\pmod3.
\]
The three excluded finite poles form one translation orbit. Each other orbit of size three has exactly one zero-trace value when \(3\nmid n\). The Artin–Schreier equation has precisely three solutions in \(K\) when the absolute trace is zero, and none otherwise. Together with the four totally ramified rational places, this gives
\[
\#X(K)=4+3\frac{3^n-3}{3}=3^n+1\quad(3\nmid n).
\]
This proves the count for all such degrees, not merely the six verified numerically.

**2. The remaining counts through genus.** For each \(1\le n\le6\), construct \(K=\mathbb F_3[t]/(h_n(t))\) using the irreducible polynomials in the table below, whose coefficients are displayed low degree first:

| \(n\) | \(h_n\), low-to-high coefficient vector | \(\#X(\mathbb F_{3^n})\) |
|---:|---|---:|
|1|`[0,1]`|4|
|2|`[1,0,1]`|10|
|3|`[1,0,2,1]`|76|
|4|`[1,0,1,1,1]`|82|
|5|`[1,0,0,0,2,1]`|244|
|6|`[1,0,0,0,1,1,1]`|670|

Every polynomial is proved irreducible by exhaustive division by all monic polynomials of degree at most half its degree. For each nonpole \(x\in K\), two independent finite computations count the fibre: direct enumeration of the image multiset of \(y\mapsto y^3-y\), and the absolute-trace-zero test. Both computations include the four distinct rational ramification points separately and agree for each field. The complete standalone certificate is `verify.py`. In particular, the only counts not already forced by step 1 among \(n\le6\) are \(N_3=76\) and \(N_6=670\).

**3. Exact Weil numerator reconstruction.** Put \(N_n=\#X(\mathbb F_{3^n})\) and \(L_X(T)=\sum_{j=0}^{12}a_jT^j\), \(a_0=1\). The formal exponential identity for the zeta function gives the exact Newton recurrence
\[
na_n=\sum_{k=1}^n a_{n-k}(N_k-3^k-1).
\]
The six counts give
\((a_0,a_1,\dots,a_6)=(1,0,0,16,0,0,118)\).
The genus-six functional equation \(a_{12-j}=3^{6-j}a_j\) for \(0\le j\le6\) determines the full coefficient vector
\[
(1,0,0,16,0,0,118,0,0,432,0,0,729).
\]
Direct integer convolution verifies its exact square factorization stated above.

**4. Isogeny factors.** The curve \(E:v^2=u^3+u^2+2\) is nonsingular: in characteristic three the derivative of the cubic is \(-u\), which has no common root with the cubic because the latter is nonzero at zero. Direct enumeration gives \(\#E(\mathbb F_3)=3\), so its trace is \(1\) and its numerator is \(1-T+3T^2\). The quartic inverse Frobenius polynomial is \(P_A(U)=U^4+U^3-2U^2+3U+9\). It is irreducible over \(\mathbb Q\): no rational linear factor is possible since all its roots have complex absolute value \(\sqrt3\); any rational quadratic factor, being monic integral, would have constant term \(+3\) or \(-3\). The \(+3,+3\) case would require two integers with sum \(1\) and product \(-8\), excluded by discriminant \(33\); the \(-3,-3\) case contradicts the coefficient of \(U\). The quartic is an integral Weil factor of the actual Jacobian, so standard finite-field isogeny theory produces a simple abelian surface \(A\). It is ordinary because the middle coefficient \(-2\) is prime to \(3\). Tate's isogeny theorem and the squared factorization therefore yield \(\operatorname{Jac}(X)\sim_{\mathbb F_3}(E\times A)^2\).

## Verification

Execute `python3 verify.py` with Python 3.10 or later; no third-party packages or auxiliary data are needed. It independently verifies polynomial irreducibility over \(\mathbb F_3\), exhaustively enumerates the degree-one through degree-six extension fields, compares direct fibre and absolute-trace criteria at each nonpole, reconstructs the exact Weil numerator with divisibility checks, verifies the factorization by integer convolution, and counts the points on the displayed elliptic curve. It outputs `ALL EXACT CHECKS PASSED`. The infinite arithmetic identity for \(3\nmid n\), completeness of the zeta numerator, and the finite-field isogeny conclusion rely on the mathematical arguments above, not on experiments beyond the genus-six cutoff.

## Relationship to prior work

Tafazolian [1, Theorem 1.1(4), Propositions 8.7–8.8] determines this genus-six family, its automorphisms, and its parameter equivalence. Those geometric statements are inputs, not claimed as new. The accessible text of [1] does not give the displayed zeta numerator, the parameter-one arithmetic point-count identity, or the Jacobian's finite-field isogeny factors. Giulietti–Korchmáros [2, Proposition 2.1, Remarks 2.2–2.3] study a different genus-two Artin–Schreier family with two simple poles; their exceptional group \(\operatorname{GL}(2,3)\) is not the genus-six family here. General Weil-polynomial tables such as [3] classify possible finite-field abelian isogeny classes, but a table entry for a polynomial does not identify the Jacobian of the particular curve above. Literature and mathematical-database searches did not identify a pre-existing determination of this curve's complete numerator. This is a bounded originality assessment, not a claim of exhaustive uniqueness across unindexed work.

## Limitations

Only the specified \(\mathbb F_3\)-model is considered; the formula is not extended to all nonzero parameters or twists. The isogeny is over \(\mathbb F_3\) and is not asserted to preserve principal polarizations. No explicit isogeny morphism or kernel is constructed. The point-count certificate performs finite-field exhaustion through extension degree six, sufficient because genus six and the functional equation are proved separately. An unindexed equivalent arithmetic computation remains a possible literature overlap.

## References

[1] Saeed Tafazolian, *Sharp bounds and gap phenomena for large \(p\)-subgroups of automorphism groups of curves*, arXiv:2610.05539v1 (first public 2026-10-04), Theorem 1.1(4), Propositions 8.7–8.8, https://arxiv.org/html/2610.05539v1 .

[2] Massimo Giulietti and Gábor Korchmáros, *Large \(p\)-groups of automorphisms of algebraic curves in characteristic \(p\)*, arXiv:1507.03737 (2015), Proposition 2.1 and Remarks 2.2–2.3, https://arxiv.org/abs/1507.03737 .

[3] Taylor Dupuy, Kiran Kedlaya, David Roe, and Christelle Vincent, *Isogeny Classes of Abelian Varieties over Finite Fields in the LMFDB*, arXiv:2003.05380 (2020), https://arxiv.org/abs/2003.05380 .
