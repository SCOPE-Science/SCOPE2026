# Universal two-scale power concentration under heterogeneous proxy delegation

## Finding

Consider the single-proxy majority model defined below, with \(m\ge1\) potential delegators and delegation probabilities \(p_1,\ldots,p_m\). Set
\[
S_m=\sum_{j=1}^m p_j,\qquad
q_j=\frac{1-p_j}{2},\qquad
h_m=\left\lfloor\frac{m+1}{2}\right\rfloor+1.
\]
Let \(U_m\) be the sum of independent Bernoulli variables with success probabilities \(q_1,\ldots,q_m\), and let \(U_{-j}\) omit coordinate \(j\). Define \(B_m\) as the root's absolute pivotality, \(L_{m,j}\) as the absolute pivotality of leaf \(j\), and
\[
R_m=\frac{B_m}{B_m+\sum_{j=1}^mL_{m,j}}.
\]

**Exact formulas, all finite \(m\).** Writing a probability with an impossible count as zero,
\[
\boxed{ B_m=1-\Pr(U_m\ge h_m)-\Pr(U_m\ge m+2-h_m), }
\]
\[
\boxed{ L_{m,j}=\tfrac12\Pr(U_{-j}=m-h_m+1)
+\tfrac12\Pr(U_{-j}=h_m-1). }
\]
These finite identities are reductions of standard pivotality definitions to Poisson-binomial probabilities; their use here is to identify the following asymptotic concentration phenomenon.

**First (absolute-power) scale.** For any sequence of probability arrays, if \(S_m/\sqrt m\to s\in[0,\infty)\), then
\[
\boxed{B_m\longrightarrow 2\Phi(s)-1},
\]
where \(\Phi\) is the standard normal distribution function. If \(S_m/\sqrt m\to\infty\), then \(B_m\to1\).

**Second (relative-power) scale.** Put
\[
\Delta_m=\frac{S_m^2}{m}-\log m.
\]
Without requiring the individual probabilities to be identical, the normalized root power satisfies
\[
\boxed{
R_m\longrightarrow
\begin{cases}
0,&\Delta_m\to-\infty,\\[2pt]
\bigl(1+\sqrt{2/\pi}\,e^{-c/2}\bigr)^{-1},&\Delta_m\to c\in\mathbb R,\\[2pt]
1,&\Delta_m\to+\infty.
\end{cases}}
\]
In particular, when \(S_m^2=m(\log m+c+o(1))\), the root's *absolute* power tends to one, but its *normalized* power has a nontrivial limit strictly between zero and one. Both scales and the critical-window constant are universal under heterogeneous delegation probabilities.

## Assumptions and scope

There are \(m+1\) unit-weight voters: one designated root and \(m\) leaves. The root directly chooses YES or NO with equal probability. Independently across leaves, leaf \(j\) delegates to the root with probability \(p_j\in[0,1]\); otherwise the leaf votes directly YES or NO with equal conditional probabilities. A delegation passes the root's vote through to that leaf. Thus the election always has \(m+1\) resolved votes, and the proposal passes precisely when at least \(h_m\) are YES. The \(p_j\) may vary arbitrarily with \(j\) and \(m\); no common value or positive lower bound is assumed.

A voter's absolute pivotality is the probability, over the independent choices of *other* voters, that forcing this voter's direct YES instead of direct NO changes the election from rejection to acceptance. In evaluating a leaf's pivotality, the leaf is forced to vote directly in the two counterfactual worlds, even when \(p_j=1\); its own random delegation choice is not sampled. For the root, switching its vote also switches every ballot delegated to it. The normalized index divides each absolute pivotality by the sum of all \(m+1\) pivotalities. This definition fixes the counterfactual convention essential to the formulas.

## Proof

**1. Exact root pivotality.** Suppose first that the root votes YES. The only NO ballots are directly cast by leaves, independently with probabilities \(q_j\). Thus the election rejects precisely when \(U_m\ge m+2-h_m\). If the root instead votes NO, the only YES ballots are directly cast by leaves, and their count has the same distribution as \(U_m\). Thus it passes precisely when \(U_m\ge h_m\). Since each resolved YES count is coordinatewise nondecreasing in the root's ballot, the event of root nonpivotality is the disjoint union of these two events. Taking complements proves the formula for \(B_m\).

**2. Exact leaf pivotality.** Hold leaf \(j\) direct in either counterfactual and sample all others. When the root votes NO, the YES ballots among the other \(m\) voters are exactly the direct YES ballots of the \(m-1\) other leaves. This count has distribution \(U_{-j}\), and leaf \(j\) is pivotal precisely when it equals \(h_m-1\). When the root votes YES, all votes except direct NO ballots are YES; the count of direct NO ballots among the other leaves has distribution \(U_{-j}\), and pivotality occurs precisely when this count equals \(m-h_m+1\). Average the two equiprobable root ballots to obtain \(L_{m,j}\).

**3. Absolute-power limit.** The mean and variance of \(U_m\) are
\[
\mu_m=\tfrac12(m-S_m),\qquad
\sigma_m^2=\tfrac14\Bigl(m-\sum_jp_j^2\Bigr).
\]
If \(S_m=O(\sqrt m)\), then \(\sum_jp_j^2\le S_m\) and \(\sigma_m^2\sim m/4\). The triangular-array Lindeberg central limit theorem applies because all summands are bounded, so each of the two upper tails in the root formula tends to \(1-\Phi(s)\). Hence \(B_m\to2\Phi(s)-1\). If \(S_m/\sqrt m\to\infty\), both tails are exponentially small by Hoeffding's inequality (their thresholds exceed the means by \(S_m/2+O(1)\)), giving \(B_m\to1\).

**4. Uniform local moderate-deviation estimate.** We establish the needed lemma, uniformly over all probability arrays with \(S_m\le m^{3/5}\), all omitted coordinates \(j\), and both integers \(k\in\{m-h_m+1,h_m-1\}\):
\[
\tag{*}
\Pr(U_{-j}=k)=\bigl(1+o(1)\bigr)
\sqrt{\frac{2}{\pi m}}\exp\!\left(-\frac{S_m^2}{2m}\right).
\]
The \(o(1)\) is deterministic and uniform over this entire class.

For the \(m-1\) summands, write \(K(t)=\sum_{\ell\ne j}\log(1-q_\ell+q_\ell e^t)\). Their mean and variance are \(\mu=(m-1-S_m+p_j)/2\) and \(\sigma^2=(m-1-\sum_{\ell\ne j}p_\ell^2)/4=m/4+O(S_m+1)\), while \(k-\mu=S_m/2+O(1)\). Since \(S_m=o(m)\), at least \(m-O(S_m)\) coordinates satisfy \(p_\ell\le1/2\), hence \(q_\ell\in[1/4,1/2]\). This ensures \(K''(t)\asymp m\) uniformly for \(|t|\le1/10\), and \(|K'''(t)|=O(m)\). There is a unique real tilt \(t_m\) with \(K'(t_m)=k\), satisfying
\[
 t_m=\frac{k-\mu}{\sigma^2}+O\!\left(\frac{(S_m+1)^2}{m^2}\right)
 =O\!\left(\frac{S_m+1}{m}\right).
\]
Furthermore, \(K''(t_m)=m/4+O(S_m+1)=m/4+o(m)\), because its third derivative is uniformly \(O(m)\) and \(|t_m|=O((S_m+1)/m)\). Taylor expansion and the variance estimate give
\[
K(t_m)-kt_m=-\frac{(k-\mu)^2}{2\sigma^2}
+O\!\left(\frac{(S_m+1)^3}{m^2}\right)
=-\frac{S_m^2}{2m}+o(1),
\]
uniformly because \((S_m+1)^3/m^2=O(m^{-1/5})\).

Under exponential tilting by \(t_m\), the independent Bernoulli probabilities become \(r_\ell=q_\ell e^{t_m}/(1-q_\ell+q_\ell e^{t_m})\). At least \(m-O(S_m)\) such probabilities belong to \([1/5,4/5]\). Their centered characteristic function is bounded in absolute value by \(\exp[-c m\sin^2(\theta/2)]\) for some fixed \(c>0\), because
\[
\left|1-r+r e^{i\theta}\right|^2
=1-4r(1-r)\sin^2(\theta/2).
\]
In the central Fourier interval \(|\theta|\le m^{-2/5}\), Taylor expansion yields the centered characteristic function \(\exp[-K''(t_m)\theta^2/2+O(m|\theta|^3)]\). The error is uniformly \(o(1)\); the integral outside this interval is exponentially small. Fourier inversion therefore gives the uniform local estimate
\[
\Pr_{t_m}(U_{-j}=k)
=\bigl(1+o(1)\bigr)(2\pi K''(t_m))^{-1/2}
=\bigl(1+o(1)\bigr)\sqrt{2/(\pi m)}.
\]
Undoing the tilt multiplies this by \(e^{K(t_m)-kt_m}\), proving (*).

Consequently, for \(S_m\le m^{3/5}\),
\[
\tag{**}
\sum_{j=1}^m L_{m,j}
=\bigl(1+o(1)\bigr)\sqrt{\frac{2m}{\pi}}
\exp\!\left(-\frac{S_m^2}{2m}\right)
=\bigl(1+o(1)\bigr)\sqrt{\frac2\pi}\,e^{-\Delta_m/2}.
\]

**5. High-delegation bound and three normalized regimes.** If \(S_m>m^{3/5}\), every target \(k\) in (*) is at least \(S_m/2-O(1)\) above the corresponding mean. Hoeffding's inequality, applied to the \(m-1\) remaining Bernoulli variables, gives \(L_{m,j}\le\exp[-c_0 S_m^2/m]\) uniformly for some absolute \(c_0>0\) and all sufficiently large \(m\). Thus \(\sum_jL_{m,j}\le m\exp[-c_0m^{1/5}]\to0\).

When \(\Delta_m\to-\infty\), necessarily \(S_m\le m^{3/5}\) eventually, and (**) makes the sum of leaf powers diverge. Since \(B_m\le1\), this forces \(R_m\to0\). When \(\Delta_m\to c\), we have \(S_m\sim\sqrt{m\log m}\), so \(B_m\to1\), and (**) gives the asserted logistic-type limit. When \(\Delta_m\to+\infty\), again \(B_m\to1\), while the leaf sum tends to zero by (**) in the moderate range and by the Hoeffding bound outside it. Hence \(R_m\to1\), completing the proof.

## Verification

Run `python3 check_heterogeneous_proxy.py` using Python 3 standard libraries. The checker computes the exact Poisson-binomial formulas with rational arithmetic and independently enumerates all three possibilities (direct NO, direct YES, delegate) for every non-counterfactual leaf. It compares both the root and every leaf pivotality for 120 heterogeneous probability profiles, covering 540 individual pivotality values and all leaf counts from one through six. Additional numerical sanity checks of the normalized logarithmic window used independent two-binomial convolutions for heterogeneous half-zero/half-positive arrays at \(m=1000,4000,16000\); these confirm approach to the predicted profile but do not substitute for the infinite-size proof.

## Relationship to prior work

Colley, Delemazure and Gilbert (2023), Sections 2 and 4 and Appendix A, establish the underlying a priori pivotality concept and finite recursive computation for proxy voting. Their main proxy-voting special case has a common delegating probability determined by a common outdegree, whereas the present theorem explicitly permits independent individual propensities. In particular, the general finite pivotality reduction, and its equal-propensity special case, are not claimed as an independent novelty; the mathematical contribution is the universal two-scale asymptotic theorem, its sharp normalized critical-window constant and its validity under arbitrary heterogeneity.

Zhang and Grossi (2021) and D'Angelo, Delfaraz and Gilbert (2022) analyze voting power on fixed delegation graphs and computational questions. Their fixed-structure formulations do not supply the random-array probability law or its asymptotic normalized phase transition. The random-weight literature, such as Boratyn and coauthors (2019), uses a different source of randomness. Gelman, Katz and Tuerlinckx (2002) discuss probabilistic voting-power models and square-root sampling scales, but do not derive this two-threshold star-proxy result.

## Limitations

The heterogeneous-propensity extension is an explicit modeling assumption; it is not asserted to follow from a rule that forces identical propensities for agents with identical outdegrees. Independence and unbiased direct votes are essential. The theorem covers one permanently direct proxy and binary majority only; it does not address interacting proxies, strategically chosen delegations, multiple decision issues or correlated votes. The precise finite values generally depend on the full array, not only on \(S_m\). The limits are asymptotic; finite numerical checks are corroboration, not proof of the infinite statements. Priority assessment remains provisional because an equivalent threshold law might be present under a different formulation in specialized voting-power literature.

## References

1. R. Colley, T. Delemazure and H. Gilbert, *Measuring a Priori Voting Power—Taking Delegations Seriously*, arXiv:2301.02462 (first posted 2023-01-06), https://arxiv.org/abs/2301.02462. Related IJCAI 2023 version, DOI:10.24963/ijcai.2023/290.
2. Y. Zhang and D. Grossi, *Power in Liquid Democracy*, arXiv:2010.07070, https://arxiv.org/abs/2010.07070.
3. G. D'Angelo, E. Delfaraz and H. Gilbert, *Computation and Bribery of Voting Power in Delegative Simple Games*, arXiv:2104.03692, https://arxiv.org/abs/2104.03692.
4. D. Boratyn and coauthors, *Average Weights and Power in Weighted Voting Games*, arXiv:1905.04261, https://arxiv.org/abs/1905.04261.
5. A. Gelman, J. Katz and T. Tuerlinckx, *The Mathematics and Statistics of Voting Power*, *Statistical Science* (2002), https://authors.library.caltech.edu/records/hpnm8-cmw66.
