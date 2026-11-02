# Exact second-neighbor correlation in one-shot antagonistic adsorption

## Finding

In the one-shot two-colour antagonistic adsorption process on the integer line, two sites separated by one intermediate site have **strictly positive same-colour occupancy covariance at every positive observation time and every nondegenerate colour bias**. The entire second-neighbor joint probability has an exact one-dimensional integral representation.

Put \(\alpha\in(0,1)\), \(\beta=1-\alpha\), and \(\gamma=\sqrt{\alpha\beta}\). Define
\[
h_A(u)=\cosh(\gamma u)-\sqrt{\beta/\alpha}\,\sinh(\gamma u),\quad H_A(t)=\int_0^t h_A(u)\,du,
\]
\[
J_A(t)=\int_0^t h_A(u)^2\,du,\qquad M_A(t)=\int_0^t\bigl(H_A(t)-H_A(s)\bigr)^2\,ds.
\]
For every \(0<t\le1\) and \(i\in\mathbb Z\), with \(A_i(t)\) the indicator that site \(i\) has accepted colour \(A\) by time \(t\),
\[
\boxed{\Pr(A_i(t)=A_{i+2}(t)=1)=\alpha^2\bigl[H_A(t)^2-\beta M_A(t)\bigr],}
\]
and
\[
\boxed{\operatorname{Cov}(A_i(t),A_{i+2}(t))
=\alpha^2\bigl[H_A(t)^2-\beta M_A(t)-J_A(t)^2\bigr]>0.}
\]
The analogous statements for \(B\) follow by exchanging \(\alpha\) and \(\beta\).

For the balanced choice \(\alpha=\beta=1/2\), these laws simplify to
\[
\Pr(A_i(t)=A_{i+2}(t)=1)=\frac{1-(1+t)e^{-t}}2,
\quad
\operatorname{Cov}(A_i(t),A_{i+2}(t))
=\frac{1-2te^{-t}-e^{-2t}}4.
\]
In particular, the full-time covariance is \((1-2e^{-1}-e^{-2})/4>0\). The nonconsecutive pattern \(A,X,A\), where \(X\) denotes a still-empty site, has exact probability
\[
\Pr(A_i(t)=1,\ X_{i+1}(t)=1,\ A_{i+2}(t)=1)
=\alpha^2\bigl[(1-\alpha t)H_A(t)^2-\beta M_A(t)\bigr].
\]
This is a two-cluster separation statistic, not a consecutive-block count.

## Assumptions and scope

Each \(i\in\mathbb Z\) independently receives one uniformly distributed attempt time \(U_i\in[0,1]\) and one independently assigned proposed colour, \(A\) with probability \(\alpha\) and \(B\) with probability \(\beta\). At \(U_i\), its proposed particle is permanently accepted precisely when neither nearest neighbour already contains the opposite colour; otherwise that site's sole attempt fails. No later attempt occurs. All sites begin empty. Observation time satisfies \(0<t\le1\), and all probability is with respect to the independent times and colours. The infinite process is well-defined almost surely by its decreasing-time ancestor paths.

The claim concerns pairs at distance exactly two, the first separation at which the middle site can mediate an interaction. It does not assert that the entire accepted-colour field is positively associated.

## Proof

**1. One-sided shielding.** Temporarily hold the candidate site vacant until a proposed \(A\) arrival at time \(u\). Let \(h_A(u)\) be the probability that its right-side neighbour has not acquired a blocking \(B\) particle before that arrival; define \(h_B\) with the colours reversed. A blocking proposal at the neighbouring site must occur at some \(v<u\) and must survive its *other* neighbour. Since the candidate is vacant before \(u\), independence of the remaining half-line gives the Volterra equations
\[
h_A(u)=1-\beta\int_0^u h_B(v)\,dv,\qquad
h_B(u)=1-\alpha\int_0^u h_A(v)\,dv.
\]
Thus \(h_A'=-\beta h_B\), \(h_B'=-\alpha h_A\), both with initial value one. Solving this two-dimensional linear system gives the displayed expression for \(h_A\), and
\[
h_B(u)=\cosh(\gamma u)-\sqrt{\alpha/\beta}\,\sinh(\gamma u).
\]
The shielding probabilities are strictly between zero and one on \((0,1]\). The left and right half-lines surrounding a single site are independent conditional on its attempt, so
\[
\Pr(A_i(t)=1)=\alpha\int_0^t h_A(u)^2\,du=\alpha J_A(t).
\]
This is consistent with the established one-point density of the model.

**2. Exact nonconsecutive pair.** Fix sites \(i\) and \(i+2\), condition on both proposing \(A\) at respective times \(u,v\le t\), and independently reveal the exterior half-lines to the left of \(i\) and right of \(i+2\). Their respective nonblocking probabilities are \(h_A(u)\) and \(h_A(v)\). The central site \(i+1\) prevents simultaneous acceptance if and only if it proposes \(B\) before both endpoint attempts: such a proposal is accepted because neither endpoint has yet attempted. If its \(B\) proposal occurs after the earlier endpoint accepted \(A\), it is rejected, and cannot obstruct the later endpoint. A proposal of \(A\) at the central site never obstructs either endpoint. Thus the remaining conditional factor is exactly \(1-\beta\min(u,v)\), and
\[
\Pr(A_i(t)=A_{i+2}(t)=1)
=\alpha^2\int_0^t\int_0^t h_A(u)h_A(v)\bigl[1-\beta\min(u,v)\bigr]du\,dv.
\]
Fubini's theorem and \(\min(u,v)=\int_0^t\mathbf 1_{s\le u}\mathbf 1_{s\le v}\,ds\) give the stated \(M_A\) representation. The only way for the central site to be occupied when both endpoints contain \(A\) is for it also to contain \(A\). Its colour and attempt time contribute \(\alpha t\), so \(\Pr(A,A,A)=\alpha^3tH_A(t)^2\). Subtracting from the pair formula gives the displayed \(A,X,A\) law.

**3. Strictly positive covariance.** Since \(h_B'(u)=-\alpha h_A(u)\) and \(0<h_A(u)\le1\), we have \(h_B(u)\ge1-\alpha u\). Therefore
\[
h_A(1)=1-\beta\int_0^1h_B(u)\,du
\le \alpha(1+\beta/2).
\]
Moreover,
\[
\alpha(1+\beta/2)^2=1-(3\beta^2+\beta^3)/4<1.
\]
Consequently \(h_A(1)^2<\alpha=1-\beta\). The function \(f(s)=h_A(s)^2+\beta s\) satisfies \(f(0)=1\), \(f(1)<1\), and
\[
f''(s)=2\beta^2h_B(s)^2+2\alpha\beta h_A(s)^2>0.
\]
Strict convexity therefore gives \(h_A(s)^2<1-\beta s\) for every \(0<s\le1\). For any \(0<u\le v\le t\le1\), \(h_A\) is strictly decreasing and hence
\[
h_A(u)h_A(v)\le h_A(u)^2<1-\beta u
=1-\beta\min(u,v).
\]
It follows that
\[
\frac{\operatorname{Cov}(A_i(t),A_{i+2}(t))}{\alpha^2}
=\int_0^t\int_0^t h_A(u)h_A(v)
\bigl[1-h_A(u)h_A(v)-\beta\min(u,v)\bigr]du\,dv>0.
\]
All inequalities are strict on a set of positive measure. Exchanging labels proves the statement for \(B\).

**4. Balanced closed form.** At \(\alpha=\beta=1/2\), \(h_A(u)=e^{-u/2}\). Direct integration of the displayed double integral gives \(\Pr(A_i(t)=A_{i+2}(t)=1)=[1-(1+t)e^{-t}]/2\). Since the one-point probability is \((1-e^{-t})/2\), subtraction of its square gives the stated covariance.

**5. Infinite-volume justification.** A site's status depends only on proposed arrivals reachable by a nearest-neighbour chain whose attempt times strictly decrease. A chain of length \(k\) has probability at most \(1/(k+1)!\) for a prescribed direction. The probability of an ancestor reaching distance \(k\) is thus bounded by \(2/(k+1)!\). This tends to zero, permitting the limit from finite paths and justifying conditional exterior independence and the Volterra equations.

## Verification

The independent standard-library script `checker.py` calculates the exact random-arrival, random-colour joint law on finite paths using rational recursive enumeration, for multiple path sizes, biases and observation times. It separately checks the analytic one-point marginal against the published density formula, the balanced closed form, the positive covariance on a parameter-time grid and numerical convergence as the path boundary recedes. It reports 8,859 passed assertions when executed with `python checker.py`. Finite-path computations are diagnostics; the infinite-volume and strict-sign conclusions rest on the analytic proof above, not on a finite enumeration.

## Relationship to prior work

Do Amaral and dos Santos (2023) formulated the one-attempt two-species antagonistic process and obtained its exact one-site densities. Their article's main derivation and conclusion concern those densities; a nonconsecutive two-site law is not stated. Do Amaral and dos Santos (2022) treat the different single-species nearest-neighbour-exclusion model, where *all* adjacent occupation is forbidden and a distance-dependent pair correlation can be calculated. Martins, Dickman and Ziff (2022/2023) consider repeated proposals and percolation in two-species antagonistic adsorption, a different attempt mechanism. Consecutive monochromatic-block probabilities do not determine the frequency of \(A,X,A\), which probes correlations between separate accepted clusters. The present contribution is the distance-two joint law and its universal strict positive-covariance classification; existing one-site formulas are used as established inputs and not claimed as new.

## Limitations

The exact formulas require one proposed particle per site, independent uniform attempt times, independent two-colour marks, one-dimensional nearest-neighbour blocking and \(0<\alpha<1\). At \(t=0\) or a deterministic colour, the strict covariance claim does not apply. There is no asserted corresponding sign theorem at arbitrary separation or on higher-dimensional graphs. Independent scientific validation and exhaustive historical-priority certification have not been performed; as with any literature comparison, unindexed earlier correlation calculations remain a residual risk.

## References

1. C. S. do Amaral and D. C. dos Santos, *One-dimensional AB random sequential adsorption with one deposition per site*, first public preprint 16 June 2023, arXiv:2306.09786v1, https://arxiv.org/abs/2306.09786.
2. C. S. do Amaral and D. C. dos Santos, *Density and correlation in a random sequential adsorption model*, first public preprint 11 October 2022, arXiv:2210.05627v1, https://arxiv.org/abs/2210.05627.
3. P. H. L. Martins, R. Dickman and R. M. Ziff, *Percolation in two-species antagonistic random sequential adsorption in two dimensions*, first public preprint 9 November 2022, arXiv:2211.04622v1, https://arxiv.org/abs/2211.04622.
