# An isolated degree-eight rank jump with constant Prym invariants in a genus-seven trigonal pencil

## Finding

Let \(k\) be an algebraically closed field of characteristic \(5\), and consider the smooth projective model \(C_a\) of
\[
 y^3=x^8+a x^6+1,\qquad a\in k,\quad a^4\ne3.
\]
The genus is \(7\). Write \(f_5\) for the Jacobian \(5\)-rank and \(a(-)\) for its \(a\)-number. Then
\[
 a(C_a)=3,\qquad f_5(C_a)=\begin{cases}2,&a^8=2,\\4,&a^8\ne2.\end{cases}
\]
The exceptional equation defines one *reduced closed point of degree eight* over \(\mathbb F_5\), hence eight distinct geometric parameter values forming one Frobenius orbit. All eight are smooth, and the rank-two locus does not meet the singular boundary.

The involution \((x,y)\mapsto(-x,y)\) has a smooth genus-three quotient
\[
 D_a:\quad y^3=t^4+a t^3+1,\qquad t=x^2.
\]
Let \(P_a\) be the connected Prym of \(C_a\to D_a\), of dimension four. For every smooth parameter,
\[
 a(D_a)=1,\qquad f_5(D_a)=\begin{cases}0,&a^8=2,\\2,&a^8\ne2,\end{cases}
\qquad a(P_a)=2,\quad f_5(P_a)=2.
\]
Thus the entire \(5\)-rank jump lies in the genus-three quotient, while the Prym fourfold has constant \(5\)-rank and constant \(a\)-number.

For \(q=5^m\), the number of smooth *marked coefficients* in \(\mathbb F_q\) with \(f_5=2\) equals \(8\) if \(8\mid m\), and \(0\) otherwise. The number with \(f_5=4\) equals
\[
 q-4\,\mathbf 1_{4\mid m}-8\,\mathbf 1_{8\mid m}.
\]
The counts are not asserted to classify isomorphism classes.

## Assumptions and scope

The characteristic is exactly five; all geometric classifications are over an algebraic closure. The coefficient \(a\) is a marked parameter, not a moduli-coordinate assertion. A curve means the smooth, geometrically integral projective curve with the specified function field. The parameter restriction \(a^4\ne3\) is necessary and sufficient for smoothness. Neither the Newton polygons nor the full Ekedahl–Oort types are determined here.

## Proof

**Smoothness and genus.** Set \(F=x^8+a x^6+1\). In characteristic five,
\[
 F'=x^5(3x^2+a).
\]
At \(x=0\) one has \(F=1\). At every other zero of \(F'\), \(x^2=3a\) and \(F=1+3a^4\). Thus \(F\) is squarefree exactly when \(a^4\ne3\). Since \(\gcd(3,8)=1\), Riemann–Hurwitz for the cyclic triple cover gives \(g(C_a)=(3-1)(8-1)/2=7\). The polynomial \(t^4+a t^3+1\) has the same squarefreeness condition; its triple cover has genus three.

**Cartier coefficients.** The following seven regular differentials form a basis:
\[
 U=\langle dx/y,\ x\,dx/y\rangle,\qquad
 V=\langle x^j dx/y^2:0\le j\le4\rangle.
\]
Regularity follows from the valuations at the unique point above infinity: \(v(x)=-3\), \(v(y)=-8\), \(v(dx)=-4\). The Cartier operator \(\mathcal C\) interchanges \(U\) and \(V\). In characteristic five, its coefficient matrices *before extracting fifth roots* are
\[
 A=\begin{pmatrix}
 0&0\\0&3\\a&0\\0&a^3\\1&0
 \end{pmatrix}:U\longrightarrow V,\qquad
 B=\begin{pmatrix}0&0&0&0&1\\0&1&0&a&0\end{pmatrix}:V\longrightarrow U.
\]
Here the \((r,i)\) entry of \(A\) is \([x^{5r+4-i}]F^3\), and the \((s,j)\) entry of \(B\) is \([x^{5s+4-j}]F\). Indeed, \(y^{-1}=F^3/y^{10}\) and \(y^{-2}=F/y^5\), so the usual coefficient-extraction formula for \(\mathcal C\) gives exactly these blocks. Matrices \(A\) and \(B\) both have rank two for every \(a\) (the nonzero constant minors involve their second and fifth rows/columns). Thus \(\operatorname{rank}\mathcal C=4\), and \(a(C_a)=7-4=3\).

**Stable semilinear rank.** Denote entrywise fifth power by \([5]\). For \(\mathcal C^2\) on \(U\), raising the coefficient matrix to the twenty-fifth power yields
\[
 B^{[5]}A=\begin{pmatrix}1&0\\0&3+a^8\end{pmatrix}.
\]
Since all Frobenius twists of the first diagonal entry are invertible, and the second is invertible exactly when \(a^8\ne2\), the stable Cartier dimension on \(U\) is respectively one or two. As \(\mathcal C:U\to V\) is injective and \(\mathcal C:V\to U\) surjective, the nonnilpotent part comes in pairs across these spaces. Thus the total stable Cartier dimension, equal to \(f_5(C_a)\), is twice this dimension. This proves the stated dichotomy and rules out all other \(5\)-ranks for this pencil.

**Quotient and Prym.** With \(t=x^2\), the quotient \(D_a\) has differential basis \(dt/y\), \(dt/y^2\), \(t\,dt/y^2\). Its coefficient blocks are
\[
 A_D=\begin{pmatrix}3\\a^3\end{pmatrix},\qquad
 B_D=\begin{pmatrix}1&a\end{pmatrix},\qquad
 B_D^{[5]}A_D=(3+a^8).
\]
Their ranks are one each for all parameters. Hence \(a(D_a)=3-2=1\) and \(f_5(D_a)=0\) at the exceptional parameters, two otherwise. The involution has four geometric fixed points (three above \(t=0\), one above \(t=\infty\)); the quotient map is separable of degree two and the Prym has dimension \(7-3=4\). The natural isogeny \(\operatorname{Jac}(D_a)\times P_a\to\operatorname{Jac}(C_a)\) has \(2\)-power degree, prime to the characteristic. Consequently the \(5\)-divisible and \(5\)-torsion invariants add: \(f_5(P_a)=f_5(C_a)-f_5(D_a)=2\) and \(a(P_a)=a(C_a)-a(D_a)=2\).

**Exceptional arithmetic.** Over \(\mathbb F_5\) the binomials \(T^8-2\) and \(T^4-3\) are irreducible: both \(2\) and \(3\) have multiplicative order four in \(\mathbb F_5^\times\), and satisfy the standard binomial irreducibility criterion for these powers of two (or direct finite-field gcd tests). The former is separable since \(8\not\equiv0\pmod5\); likewise for the latter. Their gcd is one, since \(a^4=3\) implies \(a^8=4\), not \(2\). Therefore the rank-jump locus is one degree-eight closed point, whereas the singular boundary is one degree-four closed point. A root of an irreducible polynomial of degree \(d\) belongs to \(\mathbb F_{5^m}\) exactly when \(d\mid m\), which gives the stated coefficient counts.

## Verification

The included `verify_symbolic.py` reconstructs the two Cartier blocks from coefficient extraction, checks all displayed matrix identities and nonzero minors, verifies the smoothness polynomial and both irreducibility statements, and confirms disjointness of the exceptional and singular loci. It prints `SYMBOLIC_GENUS7_PRYM_OK`.

The separate, standard-library-only `verify_field.py` uses \(\mathbb F_{5^8}=\mathbb F_5[z]/(z^8-2)\), reconstructs the raw matrices via independent polynomial convolution, computes inverse-Frobenius semilinear iterates and exact matrix ranks, and checks the smooth special value \(a=z\), nonspecial values \(a=0,1,z+1\), and the quotient in every case. It prints `INDEPENDENT_FINITE_FIELD_OK`. The finite calculations are checks of the symbolic proof, not extrapolations to infinitely many parameters.

Run using `python verify_symbolic.py` (requires SymPy), and `python verify_field.py` (Python standard library). No imported data files or third-party code are required.

## Relationship to prior work

Ozman–Pries–Weir (first preprint 2019) establish existence and geometric bounds for \(p\)-rank strata of cyclic covers, including the characteristic-five trielliptic setting. Their genus/signature existence statements do not determine the exact jumping parameters in this pencil or its Prym decomposition. Sutherland (first preprint 2020) gives general superelliptic Cartier–Manin algorithms; the coefficient-extraction technique is therefore not claimed as new. Asif–Fité–Pentland (first preprint 2020) analyze Cartier matrices and Frobenius invariants of Picard curves, but not this marked genus-seven pencil. Nourozi–Rahmati (first preprint 2023) discuss \(a\)-numbers of Picard curves, providing context for the quotient's constant \(a\)-number. Kazemifard–Tafazolian (2015) classify Newton polygons for the special fixed Picard models \(y^3=x^4-x\) and \(y^3=x^4-1\), not for all quartic coefficient pencils.

The distinguishing content here is the *joint* exact genus-seven and quotient rank-jump locus, its irreducible degree-eight arithmetic, and the constancy of Prym invariants. These statements are stronger than an existence theorem, but do not claim a new general Cartier algorithm, a generic moduli stratification, or a classification up to isomorphism.

## Limitations

This is a one-parameter, coefficient-marked subfamily. It is not a classification of all genus-seven curves, all trigonal curves, all Prym fourfolds, or their Newton polygons. An inaccessible or unindexed prior special-family computation could overlap; no global novelty guarantee is implied. The results have undergone mathematical review but not independent external validation.

## References

- E. Ozman, R. Pries and C. Weir, *The boundary of the p-rank 0 stratum of the moduli space of cyclic covers of the projective line*, arXiv:1907.05684, first posted 2019-07-12, Sections 1 and 5; https://arxiv.org/abs/1907.05684.
- A. V. Sutherland, *Counting points on superelliptic curves in average polynomial time*, arXiv:2004.10189, first posted 2020-04-21, Section 2; https://arxiv.org/abs/2004.10189.
- S. Asif, F. Fité and D. Pentland, *Computing L-polynomials of Picard curves from Cartier–Manin matrices*, arXiv:2010.07247, first posted 2020-10-14, Section 2; https://arxiv.org/abs/2010.07247.
- V. Nourozi and F. Rahmati, *The Rank of the Cartier operator on Picard Curves*, arXiv:2306.07823, first posted 2023-06-13, Section 3; https://arxiv.org/abs/2306.07823.
- A. Kazemifard and S. Tafazolian, *A note on some Picard curves over finite fields*, Finite Fields Appl. 34 (2015), 107–122; doi:10.1016/j.ffa.2014.12.002.
