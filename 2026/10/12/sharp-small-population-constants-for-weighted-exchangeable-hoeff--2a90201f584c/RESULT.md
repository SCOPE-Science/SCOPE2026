# Sharp small-population constants for weighted exchangeable Hoeffding inequalities

## Finding
For \(N\in\{3,4,5,6\}\), let \(C_N^\star\) be the least constant such that, for every exchangeable \((X_1,\ldots,X_N)\) taking values in \([-1,1]^N\), every real weight vector \(w\in\mathbb R^N\), and every \(\lambda\in\mathbb R\),
\[
\log\mathbb E\exp\left\{\lambda\sum_{i=1}^Nw_i(X_i-\overline X_N)\right\}
\le \frac{\lambda^2 C_N^\star}{2}\sum_{i=1}^N(w_i-\overline w_N)^2.
\]
The exact four constants are
\[
\boxed{C_3^\star=\frac1{\log2},\quad C_4^\star=\frac43,\quad C_5^\star=\frac1{2\log(3/2)},\quad C_6^\star=\frac65.}
\]
For \(N=3,5\), extremality involves a nonzero exponential tilt; for \(N=4,6\), it is witnessed in the variance limit. These values evaluate a natural optimal-constant sequence that was left in variational form in the cited 2026 literature.

## Assumptions and scope
Exchangeability means joint invariance under every permutation, without independence or infinite extendibility. Coordinates lie in the closed interval \([-1,1]\); weights may have either sign. Natural logarithms are used. If the centered weight vector vanishes the inequality is trivial. All four values are global constants for every admissible law and all real tilts; no finite numerical search assumption is imposed.

## Proof
**Exact reduction credited to Lee and Kim.** Their convex-vertex and two-level-weight reduction (Proposition 2 and Remark 1 of [1]) shows that the sharp constant equals
\[
\max_{1\le k,m\le N-1}\frac{8N}{m(N-m)}\sup_{t\ne0}\frac{\psi_{N,k,m}(t)}{t^2},\qquad
\psi_{N,k,m}(t)=\log\mathbb E e^{t(H-km/N)},
\]
where \(H\) is hypergeometric with population size \(N\), \(k\) marked individuals and sample size \(m\). This reduction is established in [1], not asserted here as new. Exchanging the marked and sampled sets and complementing either reduces consideration to \(1\le k,m\le\lfloor N/2\rfloor\). An upper bound \(\psi''(t)\le V\) implies \(\psi(t)\le Vt^2/2\) for every real \(t\), since \(\psi(0)=\psi'(0)=0\).

**Bernoulli ingredients.** For a Bernoulli law with success probability \(0<p<1\), the sharp Kearns--Saul result [2] is
\[
\sup_{t\ne0}\frac{\log\mathbb E e^{t(B-p)}}{t^2}
=\begin{cases}\displaystyle\frac{1-2p}{4\log((1-p)/p)},&p\ne\frac12,\\[2pt]\frac18,&p=\frac12.\end{cases}
\]
The first expression is attained at \(t=2\log((1-p)/p)\); the symmetric case has the indicated supremum as \(t\to0\). Hoeffding's lemma supplies the additional universal bound \(\psi_B(t)\le t^2/8\).

**Three individuals.** By complement and interchange only \((k,m)=(1,1)\) remains, so \(p=1/3\). Multiplication of the Bernoulli optimum by \(8\cdot3/(1\cdot2)=12\) gives \(C_3^\star=1/\log2\).

**Four individuals.** Cases with \(m=1\) are bounded by \((8\cdot4/3)(1/8)=4/3\), with equality at \(k=2\) in the limit \(t\to0\). For \(k=m=2\), the centered MGF is \((2+\cosh t)/3\). For each \(j\ge1\), \((2j)!\ge 6^j j!/3\): it is an equality for \(j=1,2\) and increases thereafter by the ratio \((2j+1)(2j+2)/(6(j+1))=(2j+1)/3\ge1\). Termwise power-series comparison therefore gives \((2+\cosh t)/3\le e^{t^2/6}\), and multiplication by \(8\cdot4/(2\cdot2)=8\) gives \(4/3\). Thus \(C_4^\star=4/3\).

**Five individuals.** The \(m=1\) Bernoulli cases \(k=1,2\) give \(3/(2\log4)\) and \(1/(2\log(3/2))\), respectively. The latter is larger since \((3/2)^3<4\), and is attained at nonzero tilt. For \(m=2,k=1\), interchanging \(m,k\) reduces to the previously computed Bernoulli case but with smaller normalizing factor. For \(m=k=2\), write \(u=e^t>0\). The probability-generating polynomial is \((3+6u+u^2)/10\); the exponential-tilt variance is exactly
\[
V(u)=\frac{6u(u^2+2u+3)}{(u^2+6u+3)^2},\qquad
V'(u)=\frac{-6(u^2-3)(u^2-2u+3)}{(u^2+6u+3)^3}.
\]
It has its global maximum \((\sqrt3-1)/2\) at \(u=\sqrt3\). Consequently its normalized sub-Gaussian constant is at most \(5(\sqrt3-1)/3\), strictly smaller than \(1/[2\log(3/2)]\). An exact elementary certificate for the strict comparison is \(\sqrt3-1<11/15\), \(\log(3/2)<11/27\), and \(10(11/15)(11/27)=1210/405<3\). The logarithmic bound follows from the alternating series for \(\log(1+1/2)\) through its fifth positive-ending term. This completes \(N=5\).

**Six individuals.** The \(m=1\) cases have normalized bound \(6/5\) by Hoeffding's lemma; \(k=3\) attains it as \(t\to0\). For \(m=2,3\) it is enough to bound the tilted variance by \(m(6-m)/20\): respectively \(2/5\) and \(9/20\). Cases \(k=1\) are Bernoulli and have tilted variance at most \(1/4\). For the three remaining symmetry-distinct pairs, putting \(u=e^t\) and writing \(D\) for the relevant probability-generating polynomial, direct differentiation yields the following identities, with every right-hand side nonnegative for \(u>0\):
\[
\begin{aligned}
(k,m)=(2,2):\quad &D=u^2+8u+6, &\frac25-\psi''(t)&=\frac{2(u^2-2u+6)^2}{5D^2};\\
(k,m)=(2,3):\quad &D=u^2+3u+1, &\frac25-\psi''(t)&=\frac{(u-1)^2(2u^2+u+2)}{5D^2};\\
(k,m)=(3,3):\quad &D=(u+1)(u^2+8u+1), &\frac9{20}-\psi''(t)&=\frac{9(u-1)^2(u^4+18u^2+1)}{20D^2}.
\end{aligned}
\]
The \((2,3)\) case is controlled even by \(2/5<9/20\) when the sample and marked-set roles are reversed. Integrating the variance bounds twice shows \(\psi(t)/t^2\le m(6-m)/40\), yielding \((8\cdot6/[m(6-m)])\psi(t)/t^2\le6/5\) uniformly. This proves \(C_6^\star=6/5\).

To realize each lower bound as an exchangeable law, choose a uniform random permutation of the deterministic population with \(k\) entries \(+1\) and the remainder \(-1\); choose the two-level centered weights with a block of size \(m\), as in [1]. The stated nonzero tilt or variance limit then forces the sharp constant. No stronger closed-form claim is made for other population sizes.

## Verification
The standalone `check.py` uses symbolic polynomial arithmetic to re-derive the three tilted-variance identities for \(N=6\), the critical-point calculation for \(N=5\), and the hypergeometric means and variances for every parameter pair with \(2\le N\le6\). It checks the exact rational comparisons and analytical-bound certificates used above. Run `python check.py` with Python 3 and SymPy installed. Finite symbolic checks support, but do not replace, the universal argument and the cited reduction and Bernoulli lemma.

## Relationship to prior work
Lee and Kim [1] prove the global Hamming-slice and two-level reduction and state the exact variational identity defining \(C_N^\star\), but supply general upper/lower envelopes rather than the four evaluated values. The Bernoulli optimum [2] and elementary Hoeffding lemma are prior results used directly. This contribution is the exact evaluation at four consecutive natural population sizes via nontrivial finite hypergeometric log-MGF domination. Unlike simply substituting sizes into [1]'s upper bound, the resulting constants are smaller and sharp. Published comparisons were made to related exchangeable bounds [3] and to mathematical-record results concerning Bernoulli and randomization, which do not provide this four-size classification.

## Limitations
These four formulas do not identify the optimal constant for \(N\ge7\), its asymptotic first-order coefficient, or uniqueness of all maximizing populations or weights. The \(N=4,6\) optimal values are suprema, not necessarily attained at a nonzero tilt. Earlier work already contains the exact hypergeometric variational characterization; priority for a previously unindexed independent small-size evaluation cannot be conclusively excluded. No independent audit or formal certification is claimed.

## References
[1] S. Lee and I. Kim, *A Sharper Hoeffding Bound for Weighted Sums of Exchangeable Random Variables*, arXiv:2608.04900, 2026, esp. Proposition 2 and Remark 1, https://arxiv.org/html/2608.04900v2.

[2] E. Schlemm, *The Kearns--Saul inequality for Bernoulli and Poisson-binomial distributions*, arXiv:1405.4496, 2014, https://arxiv.org/abs/1405.4496.

[3] R. Barber, *A Hoeffding inequality for weighted sums of exchangeable random variables*, arXiv:2404.06457, 2024, https://arxiv.org/abs/2404.06457.
