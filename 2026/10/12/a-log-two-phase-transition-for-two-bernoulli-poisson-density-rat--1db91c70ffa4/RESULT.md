# A log-two phase transition for two-Bernoulli Poisson density ratios
## Finding
Let \(B_1\sim\operatorname{Bern}(p)\) and \(B_2\sim\operatorname{Bern}(q)\) be independent, where \(p,q\in[0,1)\) and \(p+q>0\). Write
\[
\lambda=p+q,\qquad
\Delta=\frac{p^2+q^2}{\lambda},
\]
let \(Q\) denote the law of \(B_1+B_2\), and define
\[
\rho(Q,\operatorname{Poiss}_\lambda)
=\sup_{k\ge0}\frac{Q\{k\}}{e^{-\lambda}\lambda^k/k!}.
\]
Then \(0<\Delta<1\), and the exact sharp envelope at fixed \(\Delta\) is
\[
\rho(Q,\operatorname{Poiss}_\lambda)
\le E_2(\Delta):=
\begin{cases}
e^{\Delta},&0<\Delta\le\log 2,\\
\tfrac12 e^{2\Delta},&\log 2\le\Delta<1.
\end{cases}
\]
The bound is attained for every \(\Delta\in(0,1)\). If \(0<\Delta<\log2\), equality occurs exactly, up to exchanging the two variables, at \((p,q)=(\Delta,0)\). If \(\log2<\Delta<1\), equality occurs exactly at \(p=q=\Delta\). At \(\Delta=\log2\), both extremal types attain the common value \(2\).

In particular,
\[
E_2(\Delta)<\frac1{1-\Delta}
\qquad(0<\Delta<1),
\]
so the conjectured \(\Delta\)-version of the Dümbgen--Wellner density-ratio bound is valid, strictly, for every Poisson-binomial law with at most two active Bernoulli parameters.

## Assumptions and scope
The parameters may be zero because the motivating Poisson-binomial formulation allows \(p_i\in[0,1)\). Thus the class is naturally the set of laws with at most two active Bernoulli summands. The result does not claim the conjectured \(1/(1-\Delta)\) bound for three or more active parameters.

The first public source date used for cohort ownership is October 8, 2019, the first arXiv submission of Dümbgen and Wellner. The arXiv record lists MSC 60E05 and 60E15.

## Proof
Set \(s=p+q\) and \(t=pq\). Since
\[
\Delta=\frac{p^2+q^2}s=\frac{s^2-2t}s,
\]
we have
\[
2t=s(s-\Delta).
\]
The three nonzero-support density ratios are
\[
r_0=e^s(1-p)(1-q),
\]
\[
r_1=e^s\frac{p(1-q)+q(1-p)}s
=e^s(1-s+\Delta),
\]
and
\[
r_2=e^s\frac{2pq}{s^2}
=e^s\left(1-\frac{\Delta}s\right).
\]
Because \(\log(1-u)<-u\) for \(0<u<1\), at least one parameter being positive gives \(r_0<1\). On the other hand, a density ratio between probability mass functions has supremum at least \(1\); here ratios for \(k\ge3\) are zero. Hence
\[
\rho(Q,\operatorname{Poiss}_s)=\max\{r_1,r_2\}.
\]

Two elementary quadratic inequalities give the feasible bounds on \(s\) at fixed \(\Delta\):
\[
p^2+q^2\le(p+q)^2
\quad\Longrightarrow\quad
\Delta\le s,
\]
while
\[
p^2+q^2\ge\frac{(p+q)^2}2
\quad\Longrightarrow\quad
s\le2\Delta.
\]
Thus \(s\in[\Delta,2\Delta]\). Holding \(\Delta\) fixed,
\[
\frac d{ds}\bigl[e^s(1-s+\Delta)\bigr]
=e^s(\Delta-s)\le0,
\]
so
\[
r_1\le e^{\Delta},
\]
with equality only when \(s=\Delta\). Likewise,
\[
\frac d{ds}\left[e^s\left(1-\frac{\Delta}s\right)\right]
=e^s\left(1-\frac{\Delta}s+\frac{\Delta}{s^2}\right)>0
\]
for \(s\ge\Delta>0\), so
\[
r_2\le\frac12e^{2\Delta},
\]
with equality only when \(s=2\Delta\).

Both endpoints are feasible. If \(s=\Delta\), then \(2pq=s(s-\Delta)=0\), so, up to permutation, \((p,q)=(\Delta,0)\), and \(r_1=e^\Delta\). If \(s=2\Delta\), equality in \(p^2+q^2\ge(p+q)^2/2\) forces \(p=q=\Delta\), and \(r_2=e^{2\Delta}/2\). Therefore the sharp envelope is the larger of these two endpoint values. They cross exactly when \(e^\Delta=e^{2\Delta}/2\), namely at \(\Delta=\log2\), giving the stated equality classification.

Finally, if \(0<\Delta\le\log2\), then
\[
(1-\Delta)e^\Delta<1
\]
because \(\log(1-\Delta)+\Delta<0\). If \(\Delta\ge\log2>1/2\), the function \((1-\Delta)e^{2\Delta}/2\) is strictly decreasing, and at \(\Delta=\log2\) it equals \(2(1-\log2)<1\). Hence \(E_2(\Delta)<1/(1-\Delta)\) throughout \((0,1)\).

## Verification
`VERIFY.py` independently evaluates the exact three point-mass ratios on a dense rational grid of Bernoulli parameters, recomputes \(\Delta\), checks the sharp envelope numerically, checks the two equality families at representative \(\Delta\)-values on both sides of \(\log2\), and checks the strict conjectured bound. It prints `VERIFY_OK grid=9800 equality_cases=6`. These finite checks are regression tests only; the proof above is analytic and does not rely on enumeration.

## Relationship to prior work
Dümbgen and Wellner define \(\Delta=\lambda^{-1}\sum_i p_i^2\), prove
\[
\rho(Q,\operatorname{Poiss}_\lambda)\le(1-p_*)^{-1},
\]
and explicitly conjecture that \(p_*\) can be replaced by \(\Delta\). They prove a stronger logarithmic estimate only in the regime \(\lambda\le1\). The present result settles their conjectured replacement for the complete at-most-two-active-parameter class and gives the exact stronger envelope within that class.

Dümbgen, Samworth, and Wellner analyze the homogeneous binomial-to-Poisson density ratio in detail. Their binomial result covers the two endpoint families used here separately: one active Bernoulli is the \(n=1\) binomial case and \(p=q\) is the \(n=2\) homogeneous binomial case. It does not state or imply without an additional heterogeneous optimization the fixed-\(\Delta\) envelope over arbitrary \((p,q)\), nor the switch of extremizer at \(\Delta=\log2\).

## Limitations
The theorem is only for at most two active Bernoulli parameters. It does not settle the Dümbgen--Wellner conjecture for three or more active parameters. An older relative-error literature exists for homogeneous binomial approximation, and a residual originality risk is that the elementary two-parameter envelope may have appeared under different terminology in a source not located by the searches reported in the review.

## References
1. L. Dümbgen and J. A. Wellner, *The density ratio of Poisson binomial versus Poisson distributions*, arXiv:1910.03444v1; Statistics & Probability Letters 165 (2020), 108862, DOI:10.1016/j.spl.2020.108862.
2. L. Dümbgen, R. J. Samworth, and J. A. Wellner, *Bounding distributional errors via density ratios*, arXiv:1905.03009; Bernoulli 27 (2021), 818--852, DOI:10.3150/20-BEJ1256.
3. S. Antonelli and G. Regoli, *On the Poisson-binomial relative error*, Statistics & Probability Letters 71 (2005), 249--256, DOI:10.1016/j.spl.2004.11.009.
