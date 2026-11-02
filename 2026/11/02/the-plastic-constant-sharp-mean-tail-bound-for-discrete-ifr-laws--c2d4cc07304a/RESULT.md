# The plastic-constant sharp mean-tail bound for discrete IFR laws with adjacent mass dominance

## Finding

Let \(X\) be an integer-valued integrable random variable with log-concave survival probabilities \(S_j=\Pr(X\ge j)\), meaning \(S_j^2\ge S_{j-1}S_{j+1}\) for all integers \(j\). If an integer \(m\) satisfies \(\mathbb E X\ge m\) and
\[
\Pr(X=m+1)\ge\Pr(X=m)>0,
\]
then
\[
\boxed{\Pr(X\ge m+1)\ge c_*=\rho-1=0.32471795724474602596\ldots,}
\]
where \(\rho>1\) is the unique positive solution of \(\rho^3=\rho+1\) (the plastic constant). This is a **sharp** universal inequality, with an explicit equality law below. It also characterizes that equality law uniquely, up to integer translation.

This result concerns the natural adjacent-mass ratio one. It neither asserts nor relies on a formula for all positive adjacent-mass ratios.

## Assumptions and scope

The support of \(X\) may be unbounded on either side, and the survival sequence is required to be log-concave, not necessarily the probability mass sequence. Integrability is needed to compare the positive and negative means. The equality law is one-sided unbounded and has finite expectation. Shifting \(X\) by \(-m\), it suffices to prove the assertion for \(m=0\). The inequality concerns \(\Pr(X\ge1)\); when \(m=\mathbb E X\) is an integer this equals the strict mean-exceedance probability.

For the sharpness law, put \(a=\rho\), \(r=a/(1+a)\), \(b=1-1/a\), and \(t=r^2=a^{-4}=a-1\). Define the survival function by
\[
S_j=\begin{cases}1,&j\le-1,\\r,&j=0,\\t b^{j-1},&j\ge1.\end{cases}
\]
Equivalently, the mass at \(-1\) is \(1-r\), the mass at zero is \(r-t\), and the mass at any \(j\ge1\) is \((t/a)b^{j-1}\). This is a probability law because its survival function decreases from one to zero. Its consecutive survival ratios are \(1\), then \(r,r\), then \(b,b,\ldots\), and \(0<b<r<1\), so it is IFR. Both adjacent masses are \(t/a=r-t\). Furthermore,
\[
\mathbb E(X_+)=ta=\frac1{1+a}=\mathbb E((-X)_+),
\]
thus \(\mathbb E X=0\) and \(\Pr(X\ge1)=t=c_*\).

## Proof

**1. Consequences of the IFR condition.** Write \(t=\Pr(X\ge1)>0\), \(p_j=\Pr(X=j)\), \(x=t/p_0\ge1\), and \(y=1+1/x\), so \(S_0=ty\) and \(S_1=t\). Log-concavity of \((S_j)\) is equivalent to the nonincrease of the consecutive positive ratios \(S_{j+1}/S_j\). At and to the right of index one, \(S_{j+1}/S_j\le S_2/S_1=1-p_1/t\). Since \(p_1\ge p_0=t/x\), summing this geometric bound gives
\[
\mathbb E(X_+)=\sum_{j\ge1}S_j\le\frac{t^2}{p_1}\le tx.
\]
To the left, all successive ratios are at least \(S_1/S_0=1/y\). Consequently, \(S_{-k}\le ty^{k+1}\) for every \(k\ge0\). It follows that
\[
\mathbb E((-X)_+)=\sum_{k\ge0}(1-S_{-k})
\ge F_t(x):=\sum_{j\ge1}(1-ty^j)_+.
\]
The mean constraint therefore implies \(F_t(x)\le tx\).

**2. A universal envelope at the claimed constant.** Let \(a>1\) solve \(a^3=a+1\) and put \(c=a^{-4}=a-1\). The algebraic identities
\[
1+\frac1a=a^2,\qquad a+a^2=a^4=\frac1c
\]
follow directly. We prove the deterministic inequality
\[
F_c(x)\ge cx\qquad\text{for all }x\ge1.
\]
This statement is sharp, with equality at \(x=a\).

If \(1\le x\le a\), then
\[
F_c(x)\ge1-c(1+1/x)\ge cx,
\]
because \(x+1+1/x\) is nondecreasing for \(x\ge1\) and equals \(1/c\) at \(x=a\).

If \(a\le x\le3\), retain the first two summands, using \(z_+\ge z\):
\[
F_c(x)\ge2-c(y+y^2).
\]
The function \(H_2(x)=x+y+y^2=x+2+3/x+1/x^2\) is convex on \((0,\infty)\). At \(x=a\), \(H_2(a)=2/c\), while \(H_2(3)=55/9<2/c\). Convexity proves \(H_2(x)\le2/c\), establishing the assertion on this interval.

If \(3\le x\le6\), retain four summands:
\[
F_c(x)\ge4-c\sum_{j=1}^4 y^j.
\]
The function \(H_4(x)=x+\sum_{j=1}^4(1+1/x)^j\) is convex, since every nonconstant inverse-power summand is convex. Its endpoint values are \(H_4(3)=943/81\) and \(H_4(6)=15511/1296\), both strictly less than \(4/c\). Thus \(F_c(x)\ge cx\) on this interval too.

If \(x\ge6\), use \((1+1/x)^j\le e^{j/x}\). The function \(f(u)=(1-ce^u)_+\) decreases on \([0,\infty)\), and the elementary left-Riemann-sum comparison yields
\[
F_c(x)\ge\sum_{j\ge1}f(j/x)
\ge x\int_0^\infty f(u)\,du-f(0)
=x(-\log c-1+c)-(1-c).
\]
It is enough that \(6(-\log c-1)\ge1-c\). For a rational certificate, \(331/250<a<4/3\), as follows by evaluating \(u^3-u-1\) at these endpoints. Since \(\log a\ge2(a-1)/(a+1)\), we have
\[
6(-\log c-1)=6(4\log a-1)
>\frac{402}{581}>\frac{175}{256}>1-c.
\]
This completes the fourth interval and the deterministic envelope.

**3. Sharpness and equality.** Suppose \(t<c\). For fixed \(x\), the function \(F_t(x)\) decreases with \(t\); hence \(F_t(x)\ge F_c(x)\ge cx>tx\), contradicting the mean constraint. Therefore \(t\ge c\). The law in the preceding section attains equality.

Uniqueness follows from the strictness of the envelope away from \(x=a\). For \(1\le x<a\), the first-term comparison is strict; for \(a<x\le3\), strict convexity and the smaller second endpoint make the two-term bound strict; the bounds for \(x\ge3\) are strict. Thus equality forces \(x=a\), \(t=c\). Equality in the negative-mean bound forces all mass below zero to be at \(-1\); equality in the right-geometric bound forces \(p_1=p_0\) and the right survival ratios to equal \(1-p_1/t\) at every index. These conditions uniquely recover the displayed equality law.

## Verification

The standalone script `verify.py` checks the polynomial isolation of \(a\) by rational arithmetic, all stated finite-interval endpoint bounds, the integral inequality, the sharpness law, and additional finite-distribution examples. On execution it reported 20,589 passed assertions, including 331 qualifying randomly generated finite IFR laws. Its output is in `verification_output.txt`. The infinite-dimensional bound and uniqueness use the preceding proof, not these finite numerical checks. No independent audit has been performed.

## Relationship to prior work

Ai, Karagiannis, Kuželka and Pelekis, *On the probability that a discrete IFR random variable exceeds its mean* (arXiv:2610.24726v1, first posted 17 October 2026), prove \(\Pr(X\ge m+1)\ge\gamma/(1+2\gamma)\) for \(0<\gamma\le1/2\) under \(p_{m+1}\ge\gamma p_m>0\). That gives \(1/4\) at the local-ratio condition used here, by applying their theorem with \(\gamma=1/2\). It does not imply the sharp constant \(c_*>1/4\). In fact merely substituting \(\gamma=1\) into their displayed formula would give \(1/3\), which the equality law here disproves: a new extremal geometry occurs beyond the paper's stated parameter range.

The earlier nonnegative-support IFR estimate attributed in that paper to Shah is a lower bound for \(\Pr(X\ge k)\) when \(k\) does not exceed the mean; it does not directly give the strict mean-exceedance bound at the next integer. The classical continuous IFR bound of order \(1/e\) uses a continuous law and does not apply to this lattice extremizer. Mathematical-record and literature searches described in `AUDIT.json` did not identify the same sharp adjacent-mass-one statement; absence from search is not a proof of priority.

## Limitations

The bound requires log-concave survival, integrability, and local adjacent-mass dominance at an integer at or below the mean. It does not assert the optimum for other prescribed local ratios, an improvement for arbitrary IFR variables without local information, or a continuous analogue. Its extremizer has a geometric positive tail and an atom at one point below the threshold. The full-text applications and later proofs of the motivating preprint were unavailable to reread in the present source session; priority risk remains even though its visible principal theorem has a different parameter domain.

## References

1. J. Ai, V. Karagiannis, O. Kuželka and C. Pelekis, *On the probability that a discrete IFR random variable exceeds its mean*, arXiv:2610.24726v1 (2026-10-17), https://arxiv.org/abs/2610.24726 and https://arxiv.org/html/2610.24726v1. The initial source inspection covered the abstract, definitions, related results, Theorems 2 and 3, and the beginning of the proof of Theorem 2.
2. S. Shah, discrete IFR survival estimate, as reported and cited in reference 1, §1.2. Its complete primary text was not inspected.
3. R. Barlow, F. Proschan and A. W. Marshall, continuous IFR survival bound, as reported in reference 1, §1.2. The original source was not independently inspected.
