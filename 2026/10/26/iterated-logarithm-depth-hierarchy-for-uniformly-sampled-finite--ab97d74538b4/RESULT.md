# Iterated-logarithm depth hierarchy for uniformly sampled finite unary forests

## Finding
For every fixed integer \(h\ge3\), let \(F_n\) be uniformly chosen among all functions on \([n]\) satisfying the identity \(F_n^{h+1}=F_n^h\). For \(0\le j\le h\), let \(X_{j,n}\) be the number of vertices with forward distance exactly \(j\) to a fixed point. These are all the vertices, and every component is a directed rooted tree of height at most \(h\).

Define \(t_0(z)=z\) and recursively \(t_{k+1}(z)=z\exp(t_k(z))\). There is a unique positive \(r_n\) with \(n=r_nt_h'(r_n)\). Put
\[
\mu_{0,n}=t_h(r_n),\qquad
\mu_{j,n}=t_h(r_n)\prod_{i=h-j}^{h-1}t_i(r_n)\quad(1\le j\le h).
\]
The mean parameters satisfy \(\sum_{j=0}^h\mu_{j,n}=n\), and for each fixed \(\varepsilon\in(0,1)\) and \(h\ge3\) there are constants \(c>0\) and \(n_0\) such that
\[
\Pr\left(\max_{0\le j\le h}\left|\frac{X_{j,n}}{\mu_{j,n}}-1\right|>\varepsilon\right)\le \exp(-c\mu_{0,n})\quad(n\ge n_0).
\]
Thus each level is relatively concentrated on a distinct scale. For \(1\le k<h\),
\[
t_{h-k}(r_n)\sim\log^{(k)}n,\qquad
r_n\sim W(\log^{(h-1)}n).
\]
Here \(\log^{(k)}\) denotes \(k\)-fold iteration of the natural logarithm and \(W\) is the positive Lambert function. In particular,
\[
X_{j,n}\sim_{\mathsf P}\frac{n}{\prod_{i=0}^{h-j-1}t_i(r_n)}\quad(0\le j<h),\qquad
\frac{X_{h,n}}n\longrightarrow1\quad\text{in probability}.
\]
For \(h=3\), the first three levels respectively have scales
\[
\frac{n}{\log n\,\log\log n\,W(\log\log n)},\quad
\frac{n}{\log\log n\,W(\log\log n)},\quad
\frac{n}{W(\log\log n)},
\]
while the last level contains \(n(1+o_{\mathsf P}(1))\) vertices.

## Assumptions and scope
The height \(h\) is fixed as \(n\to\infty\). The labels are distinguishable, every permitted unary operation receives equal probability, and the only operation symbol is \(f\). The identity uses the conventional functional iterate. The distance is the least \(j\ge0\) such that \(F_n^j(x)\) is fixed. The theorem does not allow \(h\) to grow with \(n\).

## Proof
**1. Exact finite enumeration.** For integers \(a_0,\dots,a_h\ge0\) summing to \(n\), the number of permitted functions having \(a_j\) vertices at depth \(j\) is
\[
\frac{n!}{\prod_{j=0}^h a_j!}\prod_{j=1}^h a_{j-1}^{a_j},
\]
where \(0^0=1\) and the expression vanishes if a positive level follows an empty level. Indeed, first choose and label the disjoint levels; every vertex in level \(j\ge1\) chooses one parent in level \(j-1\), while level-zero vertices are fixed.

**2. Exact conditioned Poisson cascade.** The exponential generating function for rooted labelled trees of height at most \(k\) is \(t_k(z)\), so the EGF for their sets (forests) is \(\exp(t_h(z))\). Fix \(r>0\). Draw \(Z_0\sim\mathrm{Pois}(t_h(r))\), and, conditionally on all preceding populations, draw independently
\[
Z_j\mid Z_{j-1}\sim\mathrm{Pois}(Z_{j-1}t_{h-j}(r)),\quad 1\le j\le h.
\]
This is precisely the unconditioned Boltzmann distribution on forests: every root begins a recursive Poisson offspring tree, with remaining maximum height reduced by one at each level. Consequently, conditional on \(S=\sum_{j=0}^h Z_j=n\), the vector \((Z_0,\ldots,Z_h)\) has the same distribution as \((X_{0,n},\ldots,X_{h,n})\). Equivalently, the product of Poisson probabilities, after conditioning, agrees with the exact level-count coefficient above. This is an equality for every \(n\) and every \(r>0\), not an asymptotic approximation.

**3. Choice of parameter and concentration before conditioning.** Direct differentiation gives
\[
r t_h'(r)=t_h(r)\left(1+t_{h-1}(r)+t_{h-1}(r)t_{h-2}(r)+\cdots+\prod_{i=0}^{h-1}t_i(r)\right).
\]
This strictly increases continuously from zero to infinity because it is the sum of positive terms of a power series with positive coefficients. Hence its value equals \(n\) for exactly one \(r_n\). At this parameter the cascade expectations are exactly the displayed \(\mu_{j,n}\).

Since \(r_n\to\infty\), all \(t_i(r_n)\to\infty\), and \(\mu_{j,n}\ge\mu_{0,n}\). Apply the standard Poisson Chernoff inequality \(\Pr(|Y/\lambda-1|>\delta)\le2\exp(-\delta^2\lambda/3)\) for \(0<\delta<1\) to the initial root count and inductively to each conditional offspring count. On the event that all relative one-step errors are at most \(\delta\), each \(Z_j/\mu_{j,n}\) lies between \((1-\delta)^{j+1}\) and \((1+\delta)^{j+1}\). Choosing \(\delta\) sufficiently small in terms of \(h,\varepsilon\) gives
\[
\Pr\left(\max_j|Z_j/\mu_{j,n}-1|>\varepsilon\right)\le 2(h+1)\exp(-c_0\mu_{0,n})
\]
for some \(c_0=c_0(h,\varepsilon)>0\) and all sufficiently large \(n\).

**4. Conditioning costs only a polynomial factor.** Put \(a_j\) equal to the nearest integer to \(\mu_{j,n}\) for \(j<h\), and set \(a_h=n-\sum_{j<h}a_j\). Then all entries are positive for large \(n\), and each differs from its mean by at most \(h\). The conditional Poisson mean at level \(j\ge1\), with the previous count fixed to \(a_{j-1}\), differs from \(\mu_{j,n}\) by at most \(h\max_i t_i(r_n)\). The latter is \(O_h(\log n)\), while \(\min_j\sqrt{\mu_{j,n}}\gg_h\log n\), as established in step 5 below. Thus every Poisson mass in the path \((a_0,\ldots,a_h)\) is \((1+o(1))/\sqrt{2\pi\mu_{j,n}}\) by Stirling's formula, uniformly over these finitely many levels. Since \(\mu_{j,n}\le n\), their product bounds
\[
\Pr(S=n)\ge n^{-(h+2)}
\]
for all sufficiently large \(n\). Dividing the bound of step 3 by this probability yields \(2(h+1)n^{h+2}\exp(-c_0\mu_{0,n})\). Because \(\mu_{0,n}/\log n\to\infty\), it is bounded by \(\exp(-c\mu_{0,n})\) for some smaller \(c>0\).

**5. Hierarchy and estimates used above.** The last summand in \(rt_h'(r)\) dominates as \(r\to\infty\), so
\[
n\sim t_h(r_n)\prod_{i=0}^{h-1}t_i(r_n).
\]
Taking logarithms and recalling \(t_h(r)=r\exp(t_{h-1}(r))\), one obtains \(t_{h-1}(r_n)\sim\log n\). Descending through the equations \(t_{i}(r)=r\exp(t_{i-1}(r))\) yields \(t_{h-k}(r_n)\sim\log^{(k)}n\) for \(1\le k<h\), and the final equation \(t_1=r e^r\) gives \(r_n=W(t_1(r_n))\sim W(\log^{(h-1)}n)\). Consequently
\[
\mu_{0,n}\sim\frac{n}{\prod_{i=0}^{h-1}t_i(r_n)}\gg\frac{n}{(\log n)^h}\gg(\log n)^2.
\]
(The first \(\gg\) may use an \(h\)-dependent constant.) This justifies the square-root and conditioning estimates of step 4. The ratios \(\mu_{j+1,n}/\mu_{j,n}=t_{h-j-1}(r_n)\to\infty\) yield strict scale separation and the final-layer conclusion.

## Verification
The standalone `checker.py` enumerates every function on labelled sets of size at most six, for heights three and four, and compares the complete observed level-vector histogram with the exact counting formula. It checked 100138 raw functions and 118 nonzero profile entries, with no discrepancy. These finite checks do not establish any of the asymptotic inequalities; the proof above does. To reproduce, run `python checker.py` with Python 3 and its standard library.

## Relationship to prior work
The exponential generating-function recurrence for bounded-height labelled trees is classical and is not claimed here as new; see Moon's treatment of height-bounded trees. Koponen and Tousinejad study random relational expansions of previously specified bounded-height trees, whereas the present probability space samples the unary forest itself uniformly. Koponen's later finite-model-property work provides related model-theoretic motivation, but does not state these uniform-forest layer laws. Earlier height-two unary-forest calculations provide a lower-height comparison; the claimed contribution here is the **all-fixed-heights** simultaneous exponential profile law, its exact conditional cascade, and its iterated-logarithm scales rather than the EGF recurrence or any single extra layer.

## Limitations
The parameter \(h\) must be fixed. This is a concentration theorem, not a central limit theorem, not an enumeration asymptotic for the total number of structures, and not a first-order zero–one law. General preexisting conditioned-tree methods could imply parts of the result; full historical priority is not certified, particularly older analytic enumeration and random-tree level literature. Numerical checking is finite and does not replace the proof.

## References
1. Vera Koponen, *A characterization of the finite model property for ω-categorical theories*, arXiv:2610.16163v1, first public 12 October 2026.
2. Vera Koponen and Yasmin Tousinejad, *Random expansions of trees with bounded height*, arXiv:2410.11775, first public 15 October 2024.
3. John W. Moon, *Counting Labelled Trees*, section 7.4 on restricted-height trees (classical recurrence; publication era 1970).
4. V. E. Stepanov, *On the Distribution of the Number of Vertices in Strata of a Random Tree* (1969), residual comparison risk regarding older level-profile problems.
