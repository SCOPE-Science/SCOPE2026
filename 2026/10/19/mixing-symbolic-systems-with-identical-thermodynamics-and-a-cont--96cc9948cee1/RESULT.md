# Mixing symbolic systems with identical thermodynamics and a continuum of subleading complexity exponents

## Finding
For each real parameter \(0<\beta<1\), let
\[
H_\beta=\left\{b\in\{0,1\}^{\mathbb Z}:\ \sum_{j=i}^{i+m-1}b_j\le 3m^\beta\ \text{for every }i\in\mathbb Z,\ m\ge1\right\},
\qquad X_\beta=\{0,1\}^{\mathbb Z}\times H_\beta,
\]
with the two-sided coordinate shift \(\sigma\). The following statements hold simultaneously.

1. Every \(X_\beta\) is a topologically mixing, expansive symbolic system with the **prescribed-position approximate product property** of Zhang and Ren (Definition 2.8 of [1]), but without specification.
2. Every invariant Borel probability on \(X_\beta\) is concentrated on the common full-shift slice \(\{0,1\}^{\mathbb Z}\times\{0^{\mathbb Z}\}\). Restriction and embedding identify all the invariant-measure simplices and preserve each measure's entropy. Consequently every \(X_\beta\) has entropy \(\log2\), exactly \(2^n\) points fixed by \(\sigma^n\) for every \(n\ge1\), and zeta function \((1-2z)^{-1}\). For any continuous potential \(\varphi\) on \(X_\beta\), its variational topological pressure and equilibrium measures equal those of the restricted potential on that common full-shift slice.
3. Write \(P_\beta(n)\) for the number of length-\(n\) words in \(X_\beta\). There are constants \(c_\beta,C_\beta>0\) and \(n_\beta\) such that, for every integer \(n\ge n_\beta\),
\[
c_\beta n^\beta\log n\le \log P_\beta(n)-n\log2\le C_\beta n^\beta\log n.
\]
In particular, the **subleading complexity exponent** is exactly
\[
\lim_{n\to\infty}\frac{\log\!\left(\log P_\beta(n)-n\log2\right)}{\log n}=\beta.
\]
Thus \(X_\beta\) and \(X_\gamma\) are not topologically conjugate whenever \(\beta\ne\gamma\), giving continuum many mixing systems with identical invariant-measure statistics, periodic counts, and pressure after restriction.

## Assumptions and scope
The parameter is any real \(\beta\in(0,1)\). Both coordinates are bilateral sequences; every interval count in the definition of \(H_\beta\) is over a finite, nonempty interval of integers. The constant \(3\) is a fixed convenient normalization: the mathematically varying quantity is the sublinear marker-budget exponent. A length-\(n\) binary word is admitted by \(H_\beta\) precisely when each of its subwords obeys that interval-count bound, since appending zeros on both sides preserves it. The mixing and approximate-product properties refer to the two-sided shift, not to a one-sided factor.

The prescribed-position approximate product property here is the one from [1]: for each \(\delta,\varepsilon\in(0,1)\), there are a finite \(K\subset\mathbb Z\) containing \(0\) and \(\eta>0\) such that any countable family of pairwise disjoint finite \((K,\eta)\)-invariant observation sets and any prescribed orbit points can be simultaneously traced with at most \(\delta\) of the sites mistaken in **each** observation set. This is stronger than a property allowing shifts of the prescribed locations.

## Proof
**I. Compactness, invariant measures, and periodic points.** The inequalities defining \(H_\beta\) prohibit unions of finitely many cylinder sets, so \(H_\beta\) is closed, nonempty, and shift invariant. Every \(b\in H_\beta\) contains at most \(3n^\beta\) ones in any interval of length \(n\). If \(\nu\) is shift invariant on \(H_\beta\), then
\[
n\nu\{b:b_0=1\}=\int\sum_{j=0}^{n-1}b_j\,d\nu\le3n^\beta.
\]
Letting \(n\to\infty\) gives \(\nu\{b:b_0=1\}=0\). By shift invariance and countable subadditivity, \(\nu=\delta_{0^{\mathbb Z}}\). This also applies to the second-coordinate marginal of any invariant measure on \(X_\beta\). The first-coordinate projection is therefore an affine homeomorphism from the invariant-measure simplex of \(X_\beta\) onto that of the binary full shift, inverse to embedding at zero marker coordinate. Both maps are measure-theoretic isomorphisms on the supports, preserving entropy. The variational principle yields the assertion for all continuous potentials and their equilibrium states. A nonzero periodic marker configuration would have positive asymptotic marker frequency, contradicting the preceding interval bound. Thus all periodic marker coordinates are zero, and \(\#\operatorname{Fix}(\sigma^n)=2^n\); summing the periodic-point series gives the zeta function.

**II. Topological mixing.** Given finite admissible marker words \(u,v\), choose an integer gap \(D\) so large that \(3D^\beta\ge |u|+|v|\). For every gap length at least \(D\), the word \(u0^Dv\) obeys every interval bound: intervals containing markers from only one input word inherit its admissibility, while intervals containing markers from both have length at least \(D\) and have at most \(|u|+|v|\) markers. Any such finite word extends to a point in \(H_\beta\) by zeros. The binary full-shift coordinate can be joined across arbitrary gaps. Hence the product shift is topologically mixing.

**III. Prescribed-position approximate product property.** Use a compatible symbolic metric whose coordinate-zero disagreement has positive weight and whose weight outside any growing finite window tends to zero; one concrete choice is
\[
d(x,y)=\sum_{j\in\mathbb Z}2^{-|j|-2}\,\mathbf1_{x_j\ne y_j}
\]
for the four-symbol product alphabet. Given \(\delta,\varepsilon\in(0,1)\), choose a finite interval \(W=[-R,R]\) with metric tail outside \(W\) below \(\varepsilon\). Put \(K=W\cup\{-1,0,1\}\), and choose \(0<\eta<1\) so that
\[
\eta+3|W|\eta^{1-\beta}<\delta.
\]
Consider any countable family of pairwise disjoint finite \((K,\eta)\)-invariant sets \(F_i\subset\mathbb Z\), and target points \(x_i=(a_i,b_i)\in X_\beta\). Define a global point \(z=(a,0^{\mathbb Z})\) by setting \(a|_{F_i}=a_i|_{F_i}\), and assigning arbitrary binary symbols elsewhere. This is a valid point because its marker coordinate is identically zero.

For each \(F=F_i\), split \(F\) into its \(c\) maximal nonempty consecutive-integer components of lengths \(\ell_1,\ldots,\ell_c\). Each component contributes a distinct endpoint to the \(K\)-boundary, since \(1\in K\). Hence \(c\le|\partial_KF|<\eta|F|\). By the marker interval constraint and concavity,
\[
\#\{j\in F:b_i(j)=1\}\le3\sum_{r=1}^c\ell_r^\beta
\le3c^{1-\beta}|F|^\beta
<3\eta^{1-\beta}|F|.
\]
At most \(|\partial_KF|<\eta|F|\) observation sites are discarded at the boundary. At an interior site, the base coordinate matches the target throughout \(W\), while each marker in \(F\) can cause mismatch at at most \(|W|\) sites. The total number of mistaken observation sites is therefore less than
\[
(\eta+3|W|\eta^{1-\beta})|F|<\delta|F|.
\]
The estimate holds separately for each \(F_i\), proving precisely the prescribed-position property for countably many target blocks.

**IV. Failure of specification.** Choose tracing accuracy smaller than the weight of coordinate zero in the symbolic metric. For any proposed finite separation set, fix an integer spacing \(D\) larger than its diameter. Take arbitrarily many singleton observation blocks at positions \(0,D,2D,\ldots,(N-1)D\), and let the target marker in the corresponding block have a unique one at that block's position. Any orbit that traces all blocks must contain at least \(N\) marker ones in an interval of length \((N-1)D+1\). For fixed \(D\), the inequality \(N\le3((N-1)D+1)^\beta\) fails as \(N\to\infty\). Thus no uniform separation set realizes specification.

**V. Subleading word complexity.** Let \(p_\beta(n)\) count admitted binary marker words of length \(n\). The independent full-shift first coordinate gives the exact factorization \(P_\beta(n)=2^np_\beta(n)\). As any marker word contains at most \(3n^\beta\) ones,
\[
p_\beta(n)\le\sum_{j=0}^{\lfloor3n^\beta\rfloor}\binom nj,
\]
so \(\log p_\beta(n)\le C_\beta n^\beta\log n\) for all sufficiently large \(n\).

For the lower bound, take \(s=\lceil4n^{1-\beta}\rceil\) and \(L=\lfloor n/s\rfloor\). For sufficiently large \(n\), partition the initial \(Ls\) coordinates into \(L\) consecutive blocks of size \(s\), place exactly one marker in the middle third of each block, and put zeros elsewhere. Distinct markers are separated by at least \(s/2\). Therefore an interval of length \(m\le n\) contains at most \(1+2m/s\le1+\frac12m^\beta\le3m^\beta\) markers. An interval longer than \(n\) contains at most \(L\le n/s\le n^\beta/4<3m^\beta\) markers. Every constructed marker word is admitted even after zero-extension. There are at least \(\lfloor s/4\rfloor^L\) such words for large \(n\); since \(L\asymp n^\beta\) and \(\log s\asymp(1-\beta)\log n\), this gives \(\log p_\beta(n)\ge c_\beta n^\beta\log n\). The stated exponent follows.

**VI. Conjugacy obstruction.** By the Curtis–Hedlund–Lyndon local-rule theorem, a conjugacy between two bilateral finite-alphabet subshifts and its inverse use finite coding radii. If \(X_\beta\) and \(X_\gamma\) were conjugate, there would be fixed integers \(R,S\) with
\[
P_\beta(n)\le P_\gamma(n+2R),\qquad
P_\gamma(n)\le P_\beta(n+2S).
\]
After removing the common main exponential factor \(2^n\), their entropy excesses \(E_\beta(n)=\log P_\beta(n)-n\log2\) would satisfy
\[
E_\beta(n)\le E_\gamma(n+2R)+2R\log2,
\quad E_\gamma(n)\le E_\beta(n+2S)+2S\log2.
\]
The proven asymptotic bounds force \(\beta\le\gamma\) and \(\gamma\le\beta\), respectively. Hence a conjugacy requires \(\beta=\gamma\).

## Verification
A standalone Python 3 checker (`verify.py`) tests admissible finite words for the rational exponents \(1/2\) and \(2/3\) using exact integer-power inequalities rather than floating-point cutoffs. It also checks the necessary binomial pattern-count upper bound, zero-extension closure for small words, finite-gap mixing witnesses, and violations of the density bound by periodic markers at long finite horizons. It passed 1208 assertions. These finite checks are consistency tests only; the proofs in sections I–VI establish the infinite and all-real-parameter claims.

## Relationship to prior work
Zhang and Ren [1, Example 2.12 and Remark 2.13] introduce a product of the binary full shift with a marker subshift permitting **at most one marker in total**, prove their prescribed-position approximate product property, and observe that all invariant measures concentrate on the full-shift slice. Their example is not topologically transitive: two marker-one cylinders cannot both occur in a single orbit. Here the marker count is unbounded but uniformly sublinear on every interval; the resulting systems are **topologically mixing**, their approximate-product proof must handle arbitrary disconnected observation sets, and their subleading complexity exponents distinguish a continuum of systems whose invariant measures and periodic data agree. The finite-marker case and the abstract approximate-product framework are not claimed as new.

García-Ramos, Pavlov and Reyes [2, Section 2.4] study bounded-density shifts and record that zero limiting gradient implies zero entropy; their broader questions concern maximal-entropy measures and surjunctivity. The marker systems here are specific zero-gradient bounded-density shifts. The elementary density estimate and classical coding-radius argument are background tools; the combined mixing/prescribed-position-APP/thermodynamic-equivalence continuum with a quantitative conjugacy separator is the assessed assertion.

## Limitations
The construction is restricted to the bilateral integer shift, a binary marker coordinate, and a power-law sublinear density budget with \(0<\beta<1\). It establishes order-sharp entropy-excess growth, not its exact leading coefficient. The pressure comparison is for potentials **identified by their restriction to the common invariant full-shift slice**; unrelated potentials on different ambient spaces need not have equal pressure. No classification of all mixing approximate-product systems, all bounded-density shifts, or other amenable groups is claimed. A broader theorem in the bounded-density or symbolic-conjugacy literature may imply part of this explicit construction, so the literature comparison is subject to the stated residual risk.

## References
[1] W. Zhang and X. Ren, *Ergodic measures of intermediate entropies for amenable group actions with an approximate product property*, arXiv:2610.09949v1 (publicly posted 2026-10-07), Definition 2.8, Example 2.12, Remark 2.13. https://arxiv.org/html/2610.09949v1

[2] F. García-Ramos, R. Pavlov and C. Reyes, *Measures of maximal entropy of bounded density shifts*, arXiv:2302.07307v2 (2023), in particular Sections 1 and 2.4. https://arxiv.org/pdf/2302.07307

[3] B. Stanley, *Bounded density shifts*, Ergodic Theory and Dynamical Systems 33 (2013), 1891–1928 (foundational reference cited in [2]).

[4] D. Lind and B. Marcus, *An Introduction to Symbolic Dynamics and Coding*, Cambridge University Press, 1995 (standard sliding-block-code principle).
