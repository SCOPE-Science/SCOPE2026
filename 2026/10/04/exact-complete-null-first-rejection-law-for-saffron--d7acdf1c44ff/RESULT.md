# Exact complete-null first-rejection law for SAFFRON

## Finding
Consider constant-\(\lambda\) SAFFRON applied to an infinite sequence of independent null p-values \(P_1,P_2,\ldots\sim\mathrm{Unif}(0,1)\). Let the initial wealth be \(W_0\), let \(\gamma_j\ge 0\) satisfy \(\sum_{j\ge1}\gamma_j=1\), and define
\[
a_j=\min\{\lambda,W_0\gamma_j\}.
\]
Then the probability that SAFFRON ever makes a rejection, which equals its limiting complete-null FDR, is
\[
\mathrm{FDR}_\infty
=1-\prod_{j\ge1}\frac{1-\lambda}{1-\lambda+a_j}.
\]
If \(J\) denotes the stage at which the first rejection occurs, then
\[
\Pr(J=j)=
\left(\prod_{i<j}\frac{1-\lambda}{1-\lambda+a_i}\right)
\frac{a_j}{1-\lambda+a_j}.
\]
Here stage \(j\) is the period after exactly \(j-1\) previous p-values have exceeded the candidate threshold \(\lambda\).

When the cap is inactive, equivalently \(W_0\gamma_1\le\lambda\) for nonincreasing \(\gamma\), put \(c=W_0/(1-\lambda)\). The law becomes
\[
\mathrm{FDR}_\infty=1-\prod_{j\ge1}(1+c\gamma_j)^{-1}.
\]
For any allocation with total gamma mass one,
\[
\frac{c}{1+c}\le
1-\prod_{j\ge1}(1+c\gamma_j)^{-1}
\le 1-e^{-c},
\]
with the endpoints attained in the closure by increasingly concentrated and increasingly diffuse allocations, respectively. Because SAFFRON requires \(W_0<(1-\lambda)\alpha\), hence \(c<\alpha\), its complete-null eventual FDR is strictly below \(1-e^{-c}<\alpha\) in the uncapped regime. The general capped formula is no larger than the uncapped expression, so the same strict upper bound remains valid. For the illustrative normalized initial wealth \(c=0.025\), every uncapped gamma allocation has limiting FDR between approximately \(0.02439024\) and \(0.02469009\).

## Assumptions and scope
The result assumes the original constant-\(\lambda\) SAFFRON rule, independent exactly uniform null p-values, an infinite complete-null stream, and a deterministic nonnegative gamma sequence summing to one. No statement is made here about mixed null/non-null configurations, dependent p-values, time-varying candidate thresholds, or power. The first product formula includes threshold capping. The simplified gamma-product and its two-sided envelope require the uncapped condition.

The classification is sequential multiple testing; related sequential-multiple-testing literature explicitly lists MSC \(62L10\), which is used as the primary classification here.

## Proof
Before any rejection, the published SAFFRON recursion reduces to
\[
\alpha_t=\min\{\lambda,W_0\gamma_{t-C_{0+}(t)}\},
\qquad
C_{0+}(t)=\sum_{i=1}^{t-1}\mathbf 1\{P_i\le\lambda\}.
\]
Thus
\[
t-C_{0+}(t)=1+\sum_{i=1}^{t-1}\mathbf 1\{P_i>\lambda\},
\]
so candidate p-values that do not reject leave the gamma index unchanged, whereas a noncandidate increments it. At stage \(j\), three disjoint outcomes are possible on each fresh null p-value: rejection with probability \(a_j\), a nonrejecting candidate with probability \(\lambda-a_j\), and a noncandidate with probability \(1-\lambda\). The middle outcome repeats the same stage.

Consequently, after summing the geometric loop, the probability of rejecting before advancing from stage \(j\) is
\[
r_j=\frac{a_j}{a_j+1-\lambda},
\]
and the probability of advancing without a rejection is
\[
s_j=\frac{1-\lambda}{a_j+1-\lambda}.
\]
Independence of successive p-values gives
\[
\Pr(J=j)=\left(\prod_{i<j}s_i\right)r_j.
\]
The event of never rejecting is the event of advancing through every stage, hence has probability \(\prod_{j\ge1}s_j\). This proves the first two formulas. Under the complete null, the false discovery proportion is zero before the first rejection and one after any rejection, so \(\lim_{t\to\infty}\mathrm{FDR}(t)=\Pr(J<\infty)\).

If \(a_j=W_0\gamma_j\) for all \(j\), division by \(1-\lambda\) gives \(s_j=(1+c\gamma_j)^{-1}\). The infinite product converges because
\[
0\le\sum_j\log(1+c\gamma_j)\le c\sum_j\gamma_j=c.
\]
For the envelope, expansion of the positive product gives
\[
\prod_j(1+c\gamma_j)\ge1+c\sum_j\gamma_j=1+c,
\]
while \(\log(1+x)\le x\) gives
\[
\prod_j(1+c\gamma_j)\le e^c.
\]
Taking reciprocal complements yields the stated bounds. Concentrating gamma mass in one coordinate approaches the lower endpoint; spreading it over more and more nearly equal coordinates approaches the upper endpoint. Finally, capping replaces \(W_0\gamma_j\) by a smaller \(a_j\), reducing each stage rejection hazard and therefore reducing the eventual rejection probability.

## Verification
A standalone verifier accompanies this result. With exact rational arithmetic it exhaustively enumerates short outcome strings for a finite gamma schedule and compares them with an independent dynamic program using the published pre-first-rejection threshold recursion. It also checks the stage-factorization formula and the algebraic envelope on several rational gamma allocations. It prints `VERIFY_OK` only if all checks agree.

The computational checks are finite consistency checks, not a substitute for the infinite-product proof above.

## Relationship to prior work
Ramdas, Zrnic, Wainwright, and Jordan introduce SAFFRON, define candidates by \(P_t\le\lambda\), and give exactly the constant-\(\lambda\) threshold recursion used above. Their paper proves online FDR control and studies power as a function of \(\lambda\) and \(\gamma\), but the inspected algorithm, proof, and simulation sections do not state the complete-null first-rejection distribution or the product for attained FDR.

Fisher later extends FDR control of SAFFRON and LORD++ to a form of local positive dependence and adaptive stopping. The inspected article does not state a complete-null exact first-rejection law. Fischer and coauthors' exhaustive ADDIS work is the closest conceptual comparison: it explicitly exploits independent uniform p-values under the global null to make an online FWER procedure exhaust its error level. Its object is an exhaustive ADDIS FWER construction rather than the attained FDR of the original SAFFRON rule; it does not state the SAFFRON gamma-product or the concentration/diffusion envelope above.

## Limitations
The exact law concerns only the event of the first rejection under the complete null. After a rejection, SAFFRON's reward terms enter and the displayed stage process no longer describes the full rejection-count distribution. Uniform nulls and independence are essential to the exact geometric-stage calculation. The originality search cannot rule out an older equivalent derivation under alpha-investing or renewal-process terminology; that residual risk is retained in the review.

## References
Ramdas, A., Zrnic, T., Wainwright, M., & Jordan, M. (2018). *SAFFRON: an Adaptive Algorithm for Online Control of the False Discovery Rate*. Proceedings of Machine Learning Research 80, 4286–4294. arXiv:1802.09098.

Fisher, A. (2024). *Online false discovery rate control for LORD++ and SAFFRON under positive, local dependence*. Biometrical Journal 66(1), 2300177. DOI: 10.1002/bimj.202300177.

Fischer, L., et al. (2024). *An exhaustive ADDIS principle for online FWER control*. Biometrical Journal. DOI: 10.1002/bimj.202300237.
