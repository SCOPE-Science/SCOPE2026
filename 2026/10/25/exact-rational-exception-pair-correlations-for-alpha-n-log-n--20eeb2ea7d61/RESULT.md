# Exact rational-exception pair correlations for \(\alpha(n+\log n)\)

## Finding
Let \(\alpha\in\mathbb Q\setminus\{0\}\), and write \(\alpha=\pm a/b\) in lowest terms, with integers \(a,b\ge1\). Set \(x_n=\{\alpha(n+\log n)\}\), with the natural logarithm and fractional part in \([0,1)\). For \(s\ge0\), count **ordered** pairs of distinct indices by
\[
R_N(s;\alpha)=\frac1N\#\left\{1\le m\ne n\le N:\|x_n-x_m\|_{\mathbb R/\mathbb Z}\le\frac{s}{N}\right\}.
\]
For each fixed \(s\ge0\), the limit exists. It depends **only on the positive numerator \(a\)** and not on the denominator \(b\) or the sign of \(\alpha\):
\[
\lim_{N\to\infty}R_N(s;\alpha)=F_a(s),\qquad F_a(0)=0,
\]
\[
\boxed{F_a(s)=\frac{2s}{a(e^{1/a}-1)}+2\sum_{h\ge1}\left(1-\frac{ah}{s}\right)_+\quad(s>0),}
\]
where \((u)_+=\max\{u,0\}\). The sum is finite at each fixed \(s\). In particular, for \(0<s\le a\),
\[
F_a(s)=\frac{2s}{a(e^{1/a}-1)}<2s.
\]
Thus no nonzero rational multiplier has Poissonian pair correlations for this sequence, although the motivating 2026 theorem proves that almost every real multiplier does. The positive nonsmooth thresholds of \(F_a\) occur exactly at \(s=a,2a,3a,\ldots\); at \(s=ah\), the right derivative exceeds the left derivative by \(2/(ah)\). One equivalent expression, with \(\vartheta=\{s/a\}\), is
\[
F_a(s)=\frac{s}{a}\coth\!\left(\frac1{2a}\right)-1+\frac{a}{s}\vartheta(1-\vartheta),\qquad s>0.
\]

## Assumptions and scope
The multiplier \(\alpha\) is fixed and rational, nonzero; \(a,b\) are its uniquely determined positive coprime numerator and denominator. The scale \(s\) is any fixed nonnegative real number, and \(N\to\infty\) through positive integers. The norm \(\|u\|_{\mathbb R/\mathbb Z}=\min_{k\in\mathbb Z}|u-k|\). No uniform error estimate as \(a,b,s\) vary is claimed. All logarithms are natural. The theorem makes no assertion for irrational multipliers.

## Proof
By symmetry of the circle norm we may take \(\alpha=a/b>0\). Fix \(s>0\), put \(\delta_N=bs/(aN)\), and count pairs \(1\le m<n\le N\); ordered pairs contribute twice their number. For sufficiently large \(N\), \(\delta_N<1/(2a)\). Let \(r\in\{0,\ldots,b-1\}\) be the residue of \(n-m\) modulo \(b\). The pair condition is exactly equivalent to the existence of an integer \(k\) such that
\[
\left|\log\frac nm-\frac{bk-ar}{a}\right|\le\delta_N.
\]
Write \(j=bk-ar\). Since \(n>m\) and the possible centers \(j/a\) are separated by \(1/a\), the relevant branch \(j\ge0\) is unique for all sufficiently large \(N\). Coprimality gives, for each integer \(j\ge0\), a unique residue \(r_j\in\{0,\ldots,b-1\}\) satisfying \(ar_j\equiv-j\pmod b\). Thus the branch \(j\) is the simultaneous condition
\[
n-m\equiv r_j\pmod b,\qquad
\rho_j e^{-\delta_N}m\le n\le\rho_j e^{\delta_N}m,
\quad\rho_j=e^{j/a}.
\]

**The diagonal branch \(j=0\).** Here \(r_0=0\), so \(n=m+bh\), \(h\ge1\). The condition becomes
\[
m\ge\frac{bh}{e^{\delta_N}-1},\qquad m\le N-bh.
\]
The number of such pairs for fixed \(h\), divided by \(N\), tends to \((1-ah/s)_+\), because \(N(e^{\delta_N}-1)\to bs/a\). Only boundedly many values of \(h\) occur: the inequality \(m\le N\) forces \(h\le N(e^{\delta_N}-1)/b\to s/a\). Therefore the total normalized unordered contribution is
\[
\sum_{h\ge1}(1-ah/s)_+.
\]

**An equidistribution counting lemma.** Fix an irrational \(c>1\), a positive integer \(b\), a residue \(r\pmod b\), and a fixed \(s>0\). Let \(\delta_N=bs/(aN)\). The number of integers \(m,n\) obeying \(1\le m<n\le N\), \(n-m\equiv r\pmod b\), and \(ce^{-\delta_N}m\le n\le ce^{\delta_N}m\) is
\[
\frac{s}{ac}N+o(N).
\]
Indeed, outside \(O(1)\) boundary values of \(m\), the permitted range is \(1\le m\le N/c\). For such \(m\), admissible \(n\) occupy an interval of length \(c(e^{\delta_N}-e^{-\delta_N})m\) in the lattice \(m+r+b\mathbb Z\). Along each residue class of \(m\pmod b\), the fractional lattice-center position advances by an irrational amount \(c-1\). Weyl equidistribution therefore implies that the average number of lattice points in an interval is its length divided by \(b\), including when the interval length varies continuously with \(m/N\): partition \([0,1/c]\) into finitely many short subintervals, sandwich the moving interval lengths by their endpoint values, use equidistribution on each subinterval, and then refine the partition. Consequently the count is
\[
\frac{c(e^{\delta_N}-e^{-\delta_N})}{b}\sum_{m\le N/c}m+o(N)
=\frac{sN}{ac}+o(N).
\]
The proof works even when the interval length exceeds \(b\), since the mean lattice count over a uniformly distributed translation always equals length divided by spacing.

**The positive branches.** For each fixed \(j\ge1\), the number \(\rho_j=e^{j/a}\) is irrational (indeed transcendental by the Hermite–Lindemann theorem, as \(j/a\) is a nonzero rational). The lemma applied with \(c=\rho_j\) and \(r=r_j\) yields an unordered contribution \(sN/(a\rho_j)+o_j(N)\). The contribution of large \(j\) is uniformly negligible: if such a branch has any pair, then \(j\le a(\log N+\delta_N)\), and \(m\le Ne^{\delta_N}/\rho_j\). Moreover the allowed interval of \(n\) has length at most \(2\delta_N e^{2\delta_N}N=O_{a,b,s}(1)\), so at most \(O_{a,b,s}(1)\) integers are possible for each \(m\). Hence, for any \(J\ge1\), the normalized contribution from \(j>J\) is at most
\[
O_{a,b,s}\!\left(\sum_{j>J}e^{-j/a}+\frac{\log N}{N}\right).
\]
Taking \(N\to\infty\) and then \(J\to\infty\), the total positive-branch contribution per \(N\) is
\[
\frac{s}{a}\sum_{j\ge1}e^{-j/a}=\frac{s}{a(e^{1/a}-1)}.
\]
Combining the two types of unordered pairs and multiplying by two proves the formula for \(s>0\). At \(s=0\), equality of two distinct points would force \(\log(n/m)\) to be a nonzero rational, impossible because \(n/m\) is rational while the exponential of a nonzero rational is transcendental; hence \(R_N(0;\alpha)=0\).

Finally, the summand \(2(1-ah/s)_+\) starts with right derivative \(2/(ah)\) at \(s=ah\), while the remaining terms are differentiable there. Summing the arithmetic progression through \(\lfloor s/a\rfloor\) yields the stated fractional-part identity. The small-\(s\) strict inequality follows from \(e^t>1+t\) for \(t>0\).

## Verification
The accompanying standard-library Python program `verify.py` compares two distinct finite calculations. Direct pair enumeration checks all \(72\) combinations of six reduced rational multipliers, three sample sizes, and four windows against exact resonance-window enumeration; all agree. The latter algorithm is also compared with the predicted limiting profile at \(18\) large-cutoff configurations using \(N=50000\). It reports `CERTIFICATE_OK direct_root_agreements=72 large_cutoff_agreements=18 denominator_universality=checked`.

For example, at \(s=1.5\) and \(N=50000\), the measured normalized pair counts are \(2.41192\), \(2.41236\), and \(2.41300\) for \(\alpha=1,1/2,1/3\), respectively, against their common limit \(F_1(1.5)=2.4125968\ldots\). These are finite corroborations and do not establish convergence; the proof above supplies the infinite argument.

## Relationship to prior work
Tan, Zhang, and Zhou (arXiv:2610.22836v1, first posted 16 October 2026) prove the Poissonian limit \(2s\) for almost every real dilation of \(n+\log n\). That theorem does not assert a result at any specified rational parameter, a measure-zero set. The present exact non-Poissonian profile concerns precisely those arithmetic exceptional parameters.

Marklof and Strömbergsson (arXiv:1301.1126, 2013) analyze nearest-neighbor gap distributions of pure logarithmic sequences for arbitrary bases, and develop a broad equidistribution method for superposed lattices. Their results are particularly close when the multiplier is an integer, because the linear term then disappears modulo one. The statement here instead supplies the complete ordered pair-correlation function of the rationally twisted sequence and identifies its denominator-invariant arithmetic resonance sum; the broader lattice framework may offer another route to portions of the result. Weiß (arXiv:2304.14202, first posted 2023) calculates a non-Poissonian pair-correlation profile for the different sequence involving \(\log(2n-1)/\log2\); it does not give the claimed rational-denominator identity.

## Limitations
The limit is pointwise for fixed \(s\) and fixed nonzero rational \(\alpha\); the argument does not furnish a uniform rate as parameters vary and says nothing about irrational multipliers. The connection to general lattice-superposition results creates a residual priority risk: an existing general theorem might imply the explicit formula after additional reductions. No independent validation is asserted.

## References
1. B. Tan, Z. Zhang and Q.-L. Zhou, *Metric Poissonian Pair Correlation Property Part 1: The Case \(n+\log n\)*, arXiv:2610.22836v1 (16 October 2026), https://arxiv.org/html/2610.22836v1 .
2. J. Marklof and A. Strömbergsson, *Gaps between logs*, arXiv:1301.1126 (2013), https://arxiv.org/abs/1301.1126 .
3. C. Weiß, *An Explicit non-Poissonian Pair Correlation Function*, arXiv:2304.14202 (first posted 2023), https://arxiv.org/abs/2304.14202 .
4. C. Aistleitner, T. Lachmann and F. Pausinger, *Pair correlations and equidistribution*, arXiv:1612.05495 (2016), https://arxiv.org/abs/1612.05495 .
