# Strict convex-order dispersion in the bi-uniform binomial mixture

## Finding

Let \(n\ge2\) be an integer, let \(0<p<1\), and set \(\mu=np\) and \(k=\lfloor\mu\rfloor\). Define \(B\sim\operatorname{Binomial}(n,p)\). The bi-uniform variable \(U\) takes values in \(\{0,\ldots,n\}\), with probabilities
\[
\Pr(U=j)=\begin{cases}
A=\dfrac{n+1-2\mu+k}{(k+1)(n+1)},&0\le j\le k,\\
C=\dfrac{2\mu-k}{(n-k)(n+1)},&k<j\le n.
\end{cases}
\]
Then \(\mathbb E U=\mathbb E B=np\), and
\[
\mathbb E\varphi(U)>\mathbb E\varphi(B)
\]
for every strictly convex real function \(\varphi\) on \([0,n]\). For every convex \(\varphi\), the same inequality holds non-strictly. More precisely, for **every real** \(0<t<n\),
\[
\mathbb E(U-t)_+>\mathbb E(B-t)_+.
\]
For a mixture \(Z_w\) having the law \(w\mathcal L(B)+(1-w)\mathcal L(U)\), \(0\le w\le1\), and every \(0\le w_1<w_2\le1\), the strict stop-loss and strictly-convex ordering holds in the direction \(Z_{w_2}<_{\mathrm{cx}}Z_{w_1}\). All inequalities become identities for the degenerate endpoint probabilities \(p=0,1\) (defined by continuity) and for \(n=1\).

## Assumptions and scope

The parameter \(p\) is the success probability of the binomial law and determines the **mean** of the bi-uniform law, not an additional mixing weight. The symbol \((z)_+=\max(z,0)\). Convex functions are evaluated only on the compact interval \([0,n]\), so their expectations are finite when the functions are finite there. The distribution \(U\) is exactly the two-level law defined by Groß (2026), with the specified convention \(k=\lfloor np\rfloor\), including integral values of \(np\). The distinct mixture parameter is \(w\).

## Proof

**Step 1: normalization and mean.** The two constants are positive for \(0<p<1\), and direct substitution gives \((k+1)A+(n-k)C=1\). Summing the two arithmetic progressions gives
\[
A\sum_{j=0}^k j+C\sum_{j=k+1}^n j=np.
\]
Thus \(U\) and \(B\) have the same total probability and the same mean.

**Step 2: monotonicity of the signed mass difference.** Write \(b_j=\binom njp^j(1-p)^{n-j}\) and \(d_j=\Pr(U=j)-b_j\). Since
\[
\frac{b_{j+1}}{b_j}=\frac{(n-j)p}{(j+1)(1-p)},
\]
\(b_0,\ldots,b_k\) is nondecreasing: \(k\le np<(n+1)p\), so every ratio through \(b_k\) is greater than one. Similarly, \(b_{k+1},\ldots,b_n\) is nonincreasing, because \(k+2>(n+1)p\). Consequently
\[
d_0\ge d_1\ge\cdots\ge d_k,\qquad
d_{k+1}\le d_{k+2}\le\cdots\le d_n.
\]
There is no assumed sign at the junction; the two constants \(A,C\) may jump in either direction.

**Step 3: the two-crossing lemma.** Any nonzero real sequence satisfying these two monotonicity chains and the two moment identities \(\sum_jd_j=\sum_j jd_j=0\) has positive entries at both endpoints and all of its negative entries in one contiguous central interval. Indeed, if \(d_0\le0\), the left chain is nonpositive and the right chain can change sign only from negative to positive. A nonzero sequence changing only from negative to positive with zero total mass has strictly positive first moment (subtract a separating constant from its indices), contradiction. Thus \(d_0>0\). The same argument with signs and indices reversed gives \(d_n>0\). The two monotonic chains now force the pattern positive, then negative, then positive, with zeros permitted at transition positions.

The difference sequence is nonzero for \(n\ge2\): if \(k\ge1\), its left block would require \(b_{k-1}=b_k\), impossible since \(k<(n+1)p\); if \(k=0\), its right block would require \(b_1=b_2\), impossible since \((n+1)p<2\). Therefore both positive tails and a negative central interval actually occur.

**Step 4: convex order.** Choose indices \(a<b\) bracketing the negative interval, with \(d_j\ge0\) outside \([a,b]\), \(d_j\le0\) inside \((a,b)\). For a convex \(\varphi\), let \(L\) be the affine line through \((a,\varphi(a))\) and \((b,\varphi(b))\). Convexity implies \(\varphi-L\le0\) inside and \(\varphi-L\ge0\) outside. Hence
\[
\mathbb E\varphi(U)-\mathbb E\varphi(B)
=\sum_{j=0}^n(\varphi(j)-L(j))d_j\ge0,
\]
using both zero-moment identities to eliminate \(L\). If \(\varphi\) is strictly convex, it lies strictly below its secant at each strictly interior point, including a point with \(d_j<0\), so the inequality is strict.

The stop-loss function \((j-t)_+\) has its sole bend at \(t\). If \(t\in(a,b)\), it lies strictly below the secant at an interior negative-mass position or has a nonzero strictly positive outside-secant term, giving strict inequality. If \(t\le a\), its secant agrees with its increasing affine branch to the right, but at \(j=0<t\) it lies strictly above the extended line, and \(d_0>0\). If \(t\ge b\), the analogous argument uses \(j=n>t\) and \(d_n>0\). Thus all interior thresholds have strict stop-loss inequalities.

**Step 5: mixtures.** For every test function, expectations under \(Z_w\) are affine in \(w\). Therefore their difference for \(w_1<w_2\) equals \((w_2-w_1)[\mathbb E\varphi(U)-\mathbb E\varphi(B)]\), proving the mixture claim. At \(n=1\) or \(p\in\{0,1\}\), the laws coincide.

## Verification

The standalone `checker.py` constructs both laws using exact rational arithmetic for every integer \(2\le n\le30\) and every \(p=j/20\), \(1\le j\le19\). It checks total mass, mean, signed-mass monotonicity, positive variance gap, and strict stop-loss inequalities at every integer threshold in \(\{1,\ldots,n-1\}\). It reports 11,020 exact-rational checks on 551 parameter pairs. These checks test formulas and boundary conventions only; universal strictness and continuous thresholds follow from the preceding analytical argument.

## Relationship to prior work

Groß, *A binomial-like probability distribution with heavy tails* (arXiv:2607.18083, first posted July 20, 2026), introduced the same bi-uniform law and mixture and proved positivity of the variance gap. That result does not itself compare all convex expectations or all stop-loss thresholds. The present statement strengthens that specific variance comparison to a complete convex-order family and strict ordering of all mixture weights.

Classical single/two-crossing characterizations of convex order are used as an elementary structural mechanism, not claimed as new. Earlier mean-matched **ordinary uniform** versus symmetric-binomial comparisons address the special \(p=1/2\) case. General relative-log-concavity theorems do not automatically settle the nonsymmetric two-level family: for example at \(n=17,p=2/5\), the binomial-to-bi-uniform probability ratio fails the relevant log-concavity inequality at the step \(k=6\).

## Limitations

No stochastic dominance of ordinary tails is asserted, nor convex ordering against a beta-binomial law. The result concerns the exact two-level law with the break at \(\lfloor np\rfloor\); it does not extend unproved conclusions to arbitrary piecewise-constant laws. A broader literature theorem expressed in a different stochastic-order formalism could subsume the argument; this remains a priority risk.

## References

1. J. Groß, *A binomial-like probability distribution with heavy tails*, arXiv:2607.18083v1 (2026), https://arxiv.org/abs/2607.18083 . Sections 3–5, especially the bi-uniform law, variance comparison, and mixture definition.
2. W. Xia and W. Lv, *Log-concavity and relative log-concave ordering of compound distributions*, Probability in the Engineering and Informational Sciences 38 (2024), 579–593, DOI:10.1017/S0269964823000293. General convex-order context; the paper does not study this bi-uniform family.
3. A. Müller and D. Stoyan, *Comparison Methods for Stochastic Models and Risks* (Wiley, 2002), standard convex-order and stop-loss theory.
