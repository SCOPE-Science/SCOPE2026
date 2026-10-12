# Observable-centered Gaussian fluctuations of coupon-collector sibling deficits

## Finding

The first-order sibling coupon deficit counts share one exponential random limit. Once the observed main completion time is used to remove that common fluctuation, **all fixed-index sibling deficits have asymptotically independent Gaussian residuals**.

Fix any integer \(J\ge2\). Draw i.i.d. coupons uniformly from \(n\ge2\) types until the first time \(K_n\) that all types have appeared. For \(2\le j\le J\), let \(U_{n,j}\) count the types seen fewer than \(j\) times by that instant. For \(t>0\), define
\[
q_j(t)=\frac{\sum_{r=1}^{j-1}t^r/r!}{e^t-1},\qquad m_{n,j}(t)=1+(n-1)q_j(t),\qquad v_{n,j}(t)=(n-1)q_j(t)(1-q_j(t)).
\]
Set \(S_n=K_n/n\), \(W_n=n e^{-S_n}\), and \(R_{n,j}=\bigl(U_{n,j}-m_{n,j}(S_n)\bigr)/\sqrt{v_{n,j}(S_n)}\). Then
\[
\boxed{(W_n,R_{n,2},\ldots,R_{n,J})\Longrightarrow(W,Z_2,\ldots,Z_J),}
\]
where \(W\sim\operatorname{Exp}(1)\), the \(Z_j\) are independent standard normal variables, and the entire normal vector is independent of \(W\). In particular, the limiting residuals are independent not only across albums but also of the observed completion-time statistic.

Writing \(a_{n,j}=(\log n)^{j-1}/(j-1)!\), the same assertion equivalently yields the **unstudentized mixed-Gaussian limit**
\[
\boxed{\left(W_n,\left(\frac{U_{n,j}-m_{n,j}(S_n)}{\sqrt{a_{n,j}}}\right)_{j=2}^J\right)\Longrightarrow\left(W,(\sqrt W Z_j)_{j=2}^J\right).}
\]
This is distinct from the already-known first-order convergence \(U_{n,j}/a_{n,j}\Longrightarrow W\).

There is also an exact finite-size description and a sharp conditional decorrelation rate. In the standard independent Poisson embedding, let \(M_n\) be the time when all \(n\) independent rate-one coupon clocks have fired at least once. For \(2\le i<j\le J\),
\[
\operatorname{Corr}(U_{n,i},U_{n,j}\mid M_n)
=\sqrt{\frac{q_i(M_n)(1-q_j(M_n))}{q_j(M_n)(1-q_i(M_n))}}
\sim\sqrt{\frac{(j-1)!}{(i-1)!}}(\log n)^{-(j-i)/2}
\quad\text{in probability}.
\]
The last estimate is a relative asymptotic for every fixed pair of distinct album indices.

## Assumptions and scope

Only a uniform, independent, one-coupon-at-a-time model is used. The number \(J\) of album indices is fixed as \(n\to\infty\). The stopping index \(K_n\) and the residual counts are observable from the discrete coupon sequence; the auxiliary Poisson time is **not** required to compute any of the displayed centered statistics. Exact conditional identities hold for every \(n\ge2\) and all \(t>0\). The Gaussian limits do not assume unproved conjectures about general nonuniform coupon frequencies.

## Proof

**1. An exact stopped Poisson representation.** Attach independent exponential waiting intervals of rate \(n\) to the i.i.d. uniform coupon labels. Poisson splitting realizes these as \(n\) independent rate-one counting processes \(N_1(t),\ldots,N_n(t)\), while the superposition \(N(t)=\sum_iN_i(t)\) has rate \(n\). Let \(E_i\) be the first jump of the \(i\)th process. The continuous completion time is \(M_n=\max_i E_i\); the total number of draws then is precisely \(K_n=N(M_n)\). The \(E_i\) are i.i.d. \(\operatorname{Exp}(1)\), so
\[
\mathbb P(M_n\le t)=(1-e^{-t})^n,\qquad n e^{-M_n}\Longrightarrow W\sim\operatorname{Exp}(1),\qquad M_n-\log n=O_{\mathbb P}(1).
\]
Almost surely there is a unique last first-arriving type, whose count at \(M_n\) is exactly one. Conditional on the maximum \(M_n=t\) and its last type, all other independent Poisson counts are distributed as independent \(\operatorname{Poisson}(t)\) variables conditioned to be at least one: this follows by conditioning the independent processes on their independent first-arrival events \(E_i<t\). Consequently, for each \(j\ge2\), every non-last type is missing from the \(j\)th album with conditional probability
\[
q_j(t)=\mathbb P(1\le\operatorname{Poisson}(t)<j\mid\operatorname{Poisson}(t)\ge1)
=\frac{\sum_{r=1}^{j-1}t^r/r!}{e^t-1}.
\]
The vectors of missing indicators for distinct non-last types are independent and identically distributed; within each vector they are nested in \(j\). Therefore, **exactly** conditional on \(M_n=t\),
\[
\begin{aligned}
\mathbb E(U_{n,j}\mid M_n=t)&=m_{n,j}(t),\\
\operatorname{Var}(U_{n,j}\mid M_n=t)&=v_{n,j}(t),\\
\operatorname{Cov}(U_{n,i},U_{n,j}\mid M_n=t)&=(n-1)q_i(t)(1-q_j(t))\quad(i<j).
\end{aligned}
\]
These establish the conditional correlation formula without approximation.

**2. Conditional Gaussian fluctuations.** Put \(a_{n,j}=(\log n)^{j-1}/(j-1)!\). Uniformly for \(w\) in any compact subset of \((0,\infty)\), at \(t=\log(n/w)\),
\[
(n-1)q_j(t)=w a_{n,j}(1+o(1)),\qquad (n-1)q_j(t)(1-q_j(t))=w a_{n,j}(1+o(1)).
\]
Thus every fixed-coordinate conditional variance diverges, whereas for distinct \(i<j\), the covariance normalized by \(\sqrt{a_{n,i}a_{n,j}}\) is asymptotic to \(w\sqrt{a_{n,i}/a_{n,j}}\), which vanishes. The centered independent vector summands, after their respective \(\sqrt{a_{n,j}}\) scalings, are bounded in norm by a constant times \(a_{n,2}^{-1/2}\to0\). The multivariate Lindeberg–Feller theorem, or its characteristic-function proof, therefore gives uniformly on such compact sets
\[
\left(\frac{U_{n,j}-m_{n,j}(M_n)}{\sqrt{a_{n,j}}}\right)_{j=2}^J
\Bigm|\ (n e^{-M_n}=w)
\Longrightarrow (\sqrt w Z_j)_{j=2}^J,
\]
with mutually independent standard normals. This compact-uniform conditional statement and tightness of \(n e^{-M_n}\), with no mass at zero in its limit, imply the corresponding unconditional joint convergence with \(W\). Dividing by the exact conditional standard deviations instead of \(\sqrt{a_{n,j}}\) gives a standard normal vector independent of \(W\). The asymptotic correlation rate follows from the preceding exact covariance formula and \(q_i/q_j\sim a_{n,i}/a_{n,j}\).

**3. Replacing the unobservable continuous clock by the actual draw count.** The total-counting martingale \(N(t)-nt\) has predictable quadratic variation \(nt\). Optional isometry at the integrable stopping time \(M_n\) yields
\[
\mathbb E(K_n-nM_n)^2=n\,\mathbb E M_n=nH_n,
\]
where \(H_n=\sum_{r=1}^n1/r\). Hence
\[
S_n-M_n=O_{L^2}(\sqrt{\log n/n})=o_{\mathbb P}(1).
\]
For fixed \(j\), on bounded strips \(|t-\log n|\le A\), differentiation of the explicit \(q_j\) gives \(|q_j'(t)|\le C_{A,j}(\log n)^{j-1}/n\). The mean-value theorem, tightness of \(M_n-\log n\), and the preceding \(L^2\) estimate imply
\[
(n-1)(q_j(S_n)-q_j(M_n))=O_{\mathbb P}(a_{n,j}\sqrt{\log n/n})=o_{\mathbb P}(1),
\]
and \(v_{n,j}(S_n)/v_{n,j}(M_n)\to1\) in probability. Moreover \(n e^{-S_n}/(n e^{-M_n})\to1\) in probability. Slutsky's theorem completes both joint limit claims with the observable centering, and all finite-size conditional identities remain exact. \(\square\)

## Verification

The standalone stdlib checker `verify.py` independently evaluates two finite exact-rational formulas for each \(\mathbb E U_{n,j}\), testing \(2\le n\le23\), \(2\le j\le9\), and checks the finite conditional covariance–correlation algebra on a separate grid of positive parameters. Its current replay passes **221 checks**. This is a finite consistency test only; the infinite \(n\to\infty\) claims follow from the proof above. Run with `python3 verify.py`.

## Relationship to prior work

Long's 2026 theorem proves, for every fixed \(J\), the first-order common-exponential limit \((U_{n,j}/a_{n,j})_{j=2}^J\Longrightarrow(W,\ldots,W)\), mixed moments and asymptotically perfect **unconditional** correlations. It also represents deficits through Poissonized arrival spacings. The present theorem resolves a different, second-order question: after subtracting the **random conditional mean based on the observed stopping index**, do the remaining fluctuations correlate, and what is their joint limiting law? The normal independence, mixed-Gaussian alternative, and sharp conditional decorrelation rate are not consequences of the stated first-order convergence alone.

Ilienko's 2026 infinite-dimensional coupon deficit theorems and related point-process work also identify first-order exponential and Poisson limits, not the observable stopping-time-centered multivariate normal law above. Doumas–Spektor's 2026 paper and Long's radial-transform paper concern finite-alphabet extremality of expectations and transforms, not this asymptotic second-order law. Generic conditional central limit theorems are used as standard tools; their general forms are not asserted to be new.

## Limitations

The result treats fixed album indices and uniform independent sampling; growing-index and unequal-frequency extensions are not proved. The exact finite-size conditional formulas condition on the auxiliary Poisson completion time, but the asserted asymptotic centered statistics need only the discrete observed completion index. A full quantitative convergence rate and an independent priority verification are not supplied. Older or unindexed work under alternative occupancy terminology may contain equivalent fluctuation conclusions.

## References

1. C. D. Long, *Extremality and Limit Laws for the Siblings of the Coupon Collector*, arXiv:2606.29635v1 (first public release 2026-06-28), especially Theorem 5 and Section 6.
2. A. Ilienko, *Limit theorems in the extended coupon collector's problem*, VMSTA (published online 2026-08-11), DOI:10.15559/26-VMSTA306, especially the deficit and mixed-Poisson limit theorems.
3. C. D. Long, *Radial Transform Extremality for the Siblings of the Coupon Collector*, arXiv:2606.31391v1 (2026-06-30).
4. A. V. Doumas and S. Spektor, *Equal probabilities maximize the expected deficit in the siblings of the coupon collector*, arXiv:2606.21591v1 (2026-06-19).
