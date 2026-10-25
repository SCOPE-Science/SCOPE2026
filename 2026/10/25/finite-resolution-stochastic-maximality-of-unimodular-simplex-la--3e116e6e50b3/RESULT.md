# Finite-resolution stochastic maximality of unimodular-simplex lattice homothets

## Finding

For every full-dimensional lattice polytope \(P\subset\mathbb R^d\), every integer \(d\ge1\), and every integer grid resolution \(t\ge1\), consider the finite family
\[
\mathcal M_t(P)=\{(iP+a)/t:\ 0\le i\le t,\ a\in\mathbb Z^d,\ iP+a\subseteq tP\},
\]
where \(i=0\) includes the distinct single-point copies. Choose one member uniformly and let \(I_P\in\{0,\ldots,t\}\) be its numerator of scale. Set \(\Delta_d=\operatorname{conv}(0,e_1,\ldots,e_d)\). Then
\[
\frac{\Pr(I_P=i)}{\Pr(I_{\Delta_d}=i)}
\quad\text{is nonincreasing in }i=0,\ldots,t.
\]
In particular \(I_P\) is dominated by \(I_{\Delta_d}\) in monotone likelihood-ratio order and hence in stochastic order: for every \(1\le k\le t\),
\[
\Pr(I_P\ge k)\le\Pr(I_{\Delta_d}\ge k).
\]
If some positive-degree Ehrhart numerator coefficient \(h_j^*(P)\), with \(1\le j\le\min(d,t)\), is nonzero, all \(t\) tail inequalities are strict. If no such coefficient is nonzero, the two laws coincide. Consequently, whenever \(t\ge d\), equality of even one interior tail holds if and only if \(P\) is a unimodular simplex.

More precisely, define \(h_P^*(z)=\sum_{j=0}^d h_j^*z^j\), with \(h_j^*\ge0\) and \(h_0^*=1\), and
\[
W_j(t)=h_j^*\binom{t+d+1-j}{d+1},\qquad Z_t=\sum_{j=0}^d W_j(t),
\]
with binomial coefficients zero when the upper index is smaller than the lower index. For an auxiliary \(J\) having probabilities \(\Pr(J=j)=W_j(t)/Z_t\), the exact scale law is
\[
I_P\mid J=j\ \sim\ \operatorname{BetaBinomial}(t-j,1,d+1).
\]
The unimodular-simplex law is \(\operatorname{BetaBinomial}(t,1,d+1)\). Both laws can be coupled so that \(I_P\le I_{\Delta_d}\) almost surely.

For every integer \(1\le r\le t\), their binomial factorial moments satisfy the sharp inequality
\[
\mathbb E\binom{I_P}{r}
=\frac{\mathbb E\binom{t-J}{r}}{\binom{d+r+1}{r}}
\le\frac{\binom{t}{r}}{\binom{d+r+1}{r}},
\]
and the exact mean scale is
\[
\mathbb E\frac{I_P}{t}
=\frac{1}{d+2}-\frac{\mathbb E J}{t(d+2)}
\le\frac1{d+2}.
\]
Thus the unimodular simplex simultaneously maximizes *every* nondecreasing functional of the resolution-\(t\) scale, notably every positive scale moment and the mean relative \(d\)-volume. For fixed \(P\) the first finite-grid correction is
\[
\mathbb E\frac{I_P}{t}
=\frac1{d+2}-\frac{\mu_P}{(d+2)t}+O_P(t^{-2}),
\quad \mu_P=\frac{\sum_j jh_j^*}{\sum_j h_j^*}.
\]

## Assumptions and scope

The ambient lattice is \(\mathbb Z^d\) and \(P\) has affine dimension \(d\). The integer \(i\) is part of the explicitly defined family: this does not assert that every rational homothet with vertices on the grid has an integer scale numerator (a nonprimitive polytope can have additional rational scales). The degenerate single-point copies at \(i=0\) are included. Copies are counted as distinct subsets of \(\mathbb R^d\), not by duplicate representations. All normalizations use the lattice Ehrhart series and the actual resolution \(t\); no volume normalization is required.

The Beta-binomial distribution \(\operatorname{BetaBinomial}(N,1,d+1)\) means that first \(U\sim\operatorname{Beta}(1,d+1)\) is drawn, then \(N\) independent Bernoulli trials of success probability \(U\) are taken. The count of successes is the output.

## Proof

**1. Exact counts.** Write \(L_P(s)=\#(sP\cap\mathbb Z^d)\) for \(s\ge0\). For any \(0\le i\le t\), the support-function inequality for convex \(P\) gives
\[
iP+a\subseteq tP\iff a\in(t-i)P.
\]
Thus precisely \(L_P(t-i)\) distinct members have scale numerator \(i\). The supports at different positive \(i\) are disjoint as geometric copies because their scale factors differ; the \(i=0\) members are distinct lattice-grid points. Hence
\[
\Pr(I_P=i)=\frac{L_P(t-i)}{\sum_{s=0}^t L_P(s)}.
\]

**2. Ehrhart positive decomposition.** The standard Ehrhart-series identity and Stanley's nonnegativity theorem give, for every integer \(s\ge0\),
\[
L_P(s)=\sum_{j=0}^d h_j^*\binom{s+d-j}{d},\qquad h_j^*\in\mathbb Z_{\ge0},\quad h_0^*=1.
\]
For a fixed \(j\le t\), the hockey-stick identity gives
\[
\sum_{i=0}^t\binom{t-i+d-j}{d}=\binom{t+d+1-j}{d+1}.
\]
This proves that the scale law is the indicated mixture. Conditional on \(J=j\), writing \(N=t-j\), its point probability is
\[
\frac{\binom{N-i+d}{d}}{\binom{N+d+1}{d+1}}
=\binom Ni(d+1)\int_0^1u^i(1-u)^{N-i+d}\,du,
\]
which is \(\operatorname{BetaBinomial}(N,1,d+1)\). For \(\Delta_d\), the only nonzero Ehrhart numerator coefficient is \(h_0^*=1\); the claimed reference law follows.

**3. Likelihood-ratio and strictness.** For every \(s\ge0\) define
\[
R(s)=\frac{L_P(s)}{\binom{s+d}{d}}
=1+\sum_{j=1}^d h_j^*r_j(s),
\qquad
r_j(s)=\begin{cases}
0,&s<j,\\
\displaystyle\prod_{a=0}^{j-1}\frac{s-a}{s+d-a},&s\ge j.
\end{cases}
\]
Each \(r_j(s)\) is nondecreasing in \(s\), strictly increasing after its first positive term because each factor is increasing for \(d\ge1\). Therefore \(R(s)\) is nondecreasing. Up to a positive normalizing constant, the probability ratio in the finding is \(R(t-i)\), hence nonincreasing in \(i\). Since a decreasing likelihood ratio between two probability mass functions entails first-order stochastic domination (sum the signed differences across the unique possible crossing), every asserted tail inequality follows.

If a \(j\le t\) with \(h_j^*>0\) exists, the mixture has positive weight on a shorter \(N=t-j\) and yields strict domination at every integer tail. To see this without a general strictness theorem, use one shared \(U\sim\operatorname{Beta}(1,d+1)\) and an infinite conditionally independent Bernoulli sequence. Draw \(J\) independently, set \(I_P=\sum_{a=1}^{t-J}X_a\), and \(I_{\Delta_d}=\sum_{a=1}^{t}X_a\). For every threshold \(1\le k\le t\), conditional on any positive-weight \(j>0\), the event that the first \(t-j\) successes number \(\min(k-1,t-j)\) and the remaining \(j\) trials lift the total to at least \(k\) has positive probability (when \(k>t-j\), all of the last \(j\) can be successes). Thus each tail is strictly smaller. If no accessible positive-degree coefficient exists, \(J=0\) almost surely and the laws agree.

When \(t\ge d\), this condition is equivalent to \(h_P^*(z)=1\). Since \(\sum_jh_j^*=d!\operatorname{vol}_d(P)\), the normalized volume is then one. Any \(d+1\) affinely independent lattice vertices span a simplex of normalized volume at least one, so \(P\) must equal that simplex and it is unimodular.

**4. Moments and limits.** Given \(U\), the conditional factorial moment of order \(r\) of \(\operatorname{Binomial}(N,U)\) is \(\binom Nr U^r\). The beta moment is \(\mathbb E U^r=1/\binom{d+r+1}{r}\), yielding the displayed identity and sharp bound. At \(r=1\), \(\mathbb E U=1/(d+2)\), giving the exact mean scale. At fixed \(P\), \(W_j(t)/\sum_a W_a(t)\to h_j^*/\sum_a h_a^*\) as \(t\to\infty\), and the ratio differs by \(O_P(t^{-1})\); substituting into the exact mean identity yields the final expansion.

## Verification

The included exact-rational checker `miniature_law_checker.py` validates the point masses, the \(h^*\)-mixture, the monotone likelihood ratio, all discrete tails, the rigidity criterion, and the exact mean identity for 3,366 parameter cases. It also checks six explicit lattice polygons against independently calculated Pick-theorem Ehrhart counts. Successful output: `MINIATURE_LAW_EXACT_OK cases= 3366`. These finite checks are evidence against algebraic or indexing mistakes, not a substitute for the all-\(d\), all-\(t\) argument above.

For a tangible example, take \(P=[0,1]^2\), with \(h_P^*(z)=1+z\), and \(t=2\). The scale-numerator weights for \(I_P=0,1,2\) are \((9,4,1)\); for the unimodular triangle they are \((6,3,1)\). Thus \(\mathbb E_P(I/2)=3/14\), strictly below \(\mathbb E_{\Delta_2}(I/2)=1/4\). The exact sharp finite-grid bound holds for every increasing scale statistic, not only this mean.

## Relationship to prior work

Hirotsu's work (arXiv:2605.20905, earliest public version 20 May 2026) counts the integral-scale horizontal homothets using Ehrhart polynomials and proves a universal *limiting* mean-volume fraction. The present finding uses that count but establishes an exact finite-resolution law, a distributional likelihood-ratio extremum, a rigid equality criterion, and the first finite-grid mean-scale correction. Hirotsu's preceding work (arXiv:2501.00459) treats limiting averages and the simplex case. Braun, Hlavacek, Meza, Morales and Vindas-Meléndez (arXiv:2607.15886) study the normalized \(h^*\)-coefficient distribution, not the distribution of selected homothet scales. Their viewpoint provides a natural interpretation of \(\mu_P\); neither inspected paper states the finite-resolution Beta-binomial mixture or simplex likelihood-ratio extremal law. The proof necessarily uses Stanley's established nonnegativity of \(h^*\); it does not claim that ingredient as new.

## Limitations

The theorem applies only to integer-numerator homothets in the explicitly stated family, including degenerate copies. It does not compare arbitrary rotated, non-homothetic, or continuously sampled inscribed copies, nor arbitrary grid-scaled homothets with noninteger \(t\)-scale numerator. The value is a sharp finite-grid refinement of known asymptotic enumeration, not a new Ehrhart nonnegativity theorem. Historical priority remains provisional because an equivalent finite-grid stochastic statement may exist under alternative terminology; no independent mathematical audit has been performed.

## References

1. Takashi Hirotsu, *Horizontal miniatures and normal-sized miniatures of convex lattice polytopes*, arXiv:2605.20905 (first submitted 20 May 2026), Sections 1–3, especially Theorem 7.
2. Takashi Hirotsu, *Average-sized miniatures and normal-sized miniatures of lattice polytopes*, arXiv:2501.00459 (first publicly submitted 31 December 2024), Section 4.
3. Benjamin Braun, Max Hlavacek, Cesar J. Meza, Santiago Morales and Andrés R. Vindas-Meléndez, *Ehrhart \(h^*\)-distributions*, arXiv:2607.15886 (17 July 2026), Sections 2 and 3.
4. Richard P. Stanley, classical nonnegativity theorem for Ehrhart \(h^*\)-coefficients, as stated and referenced in arXiv:2607.15886, Section 2.1.
