# Parity-dependent leading Fourier support of integral cross-polytopes in all dimensions

## Finding
For each integer \(d\ge3\), define the unit cross-polytope \(B_d=\{x\in\mathbb R^d:\sum_{j=1}^d|x_j|\le1\}\) and its Fourier coefficient
\[
F_d(k)=\int_{B_d}\exp(-2\pi i\langle k,x\rangle)\,dx,\qquad k\in\mathbb Z^d.
\]
Let \(S_d(N)=\#\{k\in\{-N,\ldots,N\}^d:F_d(k)\ne0\}\), for integer \(N\ge1\). The following distinct parity laws hold, with implied constants depending only on the fixed dimension:
\[
S_d(N)=\begin{cases}
2^d\binom d2 N^{d-1}+O_d(N^{d-2}),&d\ge3\ \text{odd},\\
2^d\binom d3 N^{d-2}+O_d(N^{d-3}),&d\ge4\ \text{even}.
\end{cases}
\]
In odd dimension, frequencies with pairwise distinct absolute coordinate values have zero Fourier coefficient. In even dimension, frequencies in which every absolute coordinate value occurs at most twice have zero Fourier coefficient, including the possibility of zero coordinates.

These leading orders are attained on explicit configurations. If \(d\) is odd, all coordinates are nonzero and exactly one absolute frequency \(a>0\) occurs twice while the remaining absolute frequencies \(b_3,\ldots,b_d>0\) are mutually distinct and different from \(a\), then
\[
F_d(k)=\frac{2^{d-1}a^{d-3}}{(2\pi i)^{d-1}\prod_{j=3}^d(a^2-b_j^2)}\ne0.
\]
If \(d\) is even, all coordinates are nonzero and exactly one absolute frequency \(a>0\) occurs three times while the other absolute frequencies \(b_4,\ldots,b_d>0\) are distinct and different from \(a\), then
\[
F_d(k)=\frac{2^{d-3}a^{d-4}}{(2\pi i)^{d-2}\prod_{j=4}^d(a^2-b_j^2)}\ne0.
\]
All equalities are exact, for every integer frequency of the specified forms. In particular, the Fourier support in integer cubes grows in codimension one for odd dimensions but in codimension two for even dimensions.

## Assumptions and scope
All dimensions are integers \(d\ge3\); radii are fixed at one; the Fourier convention is \(\exp(-2\pi i\langle k,x\rangle)\); frequency vectors are integral, and \(N\) is a positive integer. The result concerns nonvanishing and its leading cardinality, not an exact count for arbitrary \(N\) and dimension. The displayed coefficient formulas apply only to their stated generic collision patterns.

## Proof
For \(r\ge0\), let \(F_{d,r}(k)\) be the integral of the same plane wave over the radius-\(r\) cross-polytope. Write \(q=2\pi i\). Integration over the independent positive and negative half-lines gives, initially for sufficiently large real \(s>0\),
\[
\int_0^\infty e^{-sr}F_{d,r}(k)\,dr
=\frac1s\prod_{j=1}^d\int_{\mathbb R}e^{-s|x|-qk_jx}\,dx
=\frac{2^d s^{d-1}}{\prod_{j=1}^d(s^2-q^2k_j^2)}.
\]
The inverse Laplace transform is a finite sum over the poles, so evaluating at \(r=1\), after \(s=qz\), yields
\[
F_d(k)=\frac{2^d}{q^d}\sum_{a\in\mathcal A(k)}\operatorname{Res}_{z=a}\left[e^{qz}R_k(z)\right],\quad
R_k(z)=\frac{z^{d-1}}{\prod_{j=1}^d(z^2-k_j^2)},
\]
where \(\mathcal A(k)\) is the set of poles after cancellations (and may include zero). Each pole is an integer, hence \(e^{qa}=1\). At a pole of order \(m\) write the Laurent principal part \(\sum_{j=1}^m c_{-j}(z-a)^{-j}\). Its contribution to the last sum equals
\[
c_{-1}+qc_{-2}+\frac{q^2}{2}c_{-3}+\cdots+\frac{q^{m-1}}{(m-1)!}c_{-m}.
\]
Because \(R_k(z)=O(z^{-d-1})\) at infinity, the sum of the ordinary residues \(c_{-1}\) over all poles is zero. Thus only terms involving a pole of order at least two can contribute.

If \(d\) is odd and the \(|k_j|\) are distinct, every nonzero pole is simple and a possible zero coordinate does not create a pole: the numerator has a zero of degree \(d-1\) and the denominator contributes only \(z^2\). This proves the odd-dimensional vanishing statement. If \(d\) is even and no absolute frequency occurs more than twice, every nonzero pole has order at most two. The rational function is odd, \(R_k(-z)=-R_k(z)\), so the coefficients \(c_{-2}\) at the paired poles \(a\) and \(-a\) cancel. At zero there can be only a simple pole: with at most two zero coordinates its order is \(2t-(d-1)\le5-d\le1\). Hence the entire residue sum is zero, proving even-dimensional vanishing.

In the odd generic double-collision case, the coefficient \(c_{-2}\) at each of \(\pm a\) is \(a^{d-3}/[4\prod_j(a^2-b_j^2)]\). There are no other higher poles. Multiplication by \(2^dq/q^d\) gives the first exact formula. In the even generic triple-collision case, \(c_{-3}\) at each of \(\pm a\) is \(a^{d-4}/[8\prod_j(a^2-b_j^2)]\); the terms linear in \(q\) cancel by oddness and those quadratic in \(q\) add. Multiplication by \(2^dq^2/(2q^d)\) gives the second exact formula.

For odd \(d\), frequencies with exactly one pair of equal positive absolute values and \(d-2\) other distinct positive values number exactly \(2^d\binom d2N(N-1)_{d-2}\), where \((N-1)_{d-2}\) is the falling factorial (and is zero when \(N<d-1\)). This yields the displayed leading term. Every remaining possibly nonzero pattern has at most \(d-2\) freely chosen **positive** absolute values: either a second collision reduces the number of positive choices, or the repeated value is zero (which itself has only one choice), or further coincidences occur. Hence there are \(O_d(N^{d-2})\) such frequencies. For even \(d\), every possibly nonzero pattern has an absolute value appearing at least three times, hence at most \(d-2\) distinct absolute values. The generic pattern with a unique triple and all other values nonzero and distinct has exactly \(2^d\binom d3N(N-1)_{d-3}\) members. Every other possibly nonzero pattern has at most \(d-3\) freely chosen **positive** absolute values: another collision costs a parameter, and a triple collision at zero has the repeated value fixed. This yields \(O_d(N^{d-3})\) members. This proves both asymptotic statements. The estimates on the exceptional patterns remain valid when zero is among the absolute values because each coordinate-sign choice only contributes a dimension-dependent bounded factor.

## Verification
The standalone arithmetic checker `CHECK.py` constructs the residue polynomial \(\sum_a\operatorname{Res}(e^{qz}R_k)\) exactly over the rationals using Taylor-series arithmetic around every pole and confirms the generic closed coefficient identities and the parity vanishing mechanisms. It passes 1,095 exact tests, including an exhaustive box \(k\in\{0,1,2\}^d\) for \(d=3,4,5,6\). These finite calculations corroborate, but do not replace, the above proof for all dimensions and frequencies. Run with `python CHECK.py` using Python's standard library.

## Relationship to prior work
Borda's 2016 cross-polytope lattice-discrepancy analysis gives a general polytope Fourier contour representation and discusses repeated poles. Diaz–Le–Robins (2016) give general polytope Fourier-transform machinery. Neither inspected treatment states the parity-dependent leading integer-frequency support count here; the all-dimension count and explicit generic coefficients are the specialized results being asserted. These general transform formulas can be used as alternative starting points, so the underlying residue method is not claimed as new. Lower-dimensional integer-frequency formulas in dimensions three and four are special cases; the claim here is the uniform odd/even dichotomy across all dimensions with its sharp leading support constants.

## Limitations
The theorem does not classify every nongeneric frequency collision or provide the lower-order coefficients of \(S_d(N)\). The originality comparison was bounded by the accessible literature and mathematical search index; a prior equivalent all-dimensional specialization remains possible. The proof has received self-review, not independent mathematical audit.

## References
1. Bence Borda, *Lattice points in algebraic cross-polytopes and simplices*, arXiv:1608.02417, first public 2016-08-08, especially Section 2.3 and Theorem 3.
2. Ricardo Diaz, Quang-Nhat Le, Sinai Robins, *Fourier transforms of polytopes, solid angle sums, and discrete volume*, arXiv:1602.08593, first public 2016-02-27.
