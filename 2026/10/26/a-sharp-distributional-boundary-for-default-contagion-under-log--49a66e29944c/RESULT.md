# A sharp distributional boundary for default contagion under log-convex shock survival

## Finding

In an Eisenberg–Noe star clearing network with \(m\ge1\) targets, unit outside assets, equal initial net worth \(x\in(0,1/(m+1))\) for every bank, and a source whose liabilities are entirely interbank and split equally among the targets, let independent primary loss shocks share survival function \(S\) and be capped at the unit outside-asset value. If \(S(0)=1\) and \(\log S\) is convex on \([0,(m+1)x]\), then the probability that a shock to the source alone defaults all targets is \(S((m+1)x)\ge S(x)^{m+1}\), the probability that all banks default through independent direct shocks. The inequality is strict when \(\log S\) is strictly convex on the relevant interval; in particular, every non-degenerate mixture of exponential rates gives strict inequality at every feasible threshold, while a pure exponential law gives equality.

## Assumptions and scope

There are \(m+1\) banks indexed by \(0,1,\ldots,m\), all with outside assets equal to one and initial net worth \(x\). Assume \(0<x<1/(m+1)\). Bank \(0\) is the source; it has no interbank claims and total liabilities \(1-x\), all owed in equal shares to the \(m\) target banks. Each target owes only to the outside sector; its outside liabilities are chosen as \(1+(1-x)/m-x\), so its initial net worth is exactly \(x\). The liability network is acyclic, so the clearing vector is unique.

For each bank, the primary normalized loss \(Y_i\) is independent and has common survival function \(S(t)=\mathbb P(Y_i>t)\). The realized loss is \(X_i=\min(1,Y_i)\). Since \((m+1)x<1\), every threshold used below lies below the cap, and \(\mathbb P(X_i>t)=S(t)\) at those thresholds. The source is fully financially connected: all of its liabilities are owed to financial institutions.

The comparison is between (i) the event that only the source is shocked and its payment shortfall causes all targets to default, and (ii) the event that every bank defaults from its own independent direct shock. It is not a comparison of expected aggregate losses, nor a statement about arbitrary liability networks.

## Proof

Write \(q=m+1\). If the source receives a realized loss \(z>x\), its payment shortfall is \(z-x\). Because its liabilities are split equally among the targets, each target loses \((z-x)/m\) in incoming payments. Every target has initial net worth \(x\), so all targets default exactly when \((z-x)/m>x\), equivalently \(z>qx\). Thus the contagion probability is exactly \(S(qx)\); the cap at one does not alter it because \(qx<1\).

Under independent direct shocks, all \(q\) banks default directly exactly when each primary loss exceeds \(x\). That probability is \(S(x)^q\).

Set \(f(t)=\log S(t)\). Convexity of \(f\), together with \(f(0)=0\), gives
\[
 f(x)=f\!\left(\frac1q(qx)+\left(1-\frac1q\right)0\right)
 \le \frac1q f(qx).
\]
Hence \(qf(x)\le f(qx)\), so \(S(x)^q\le S(qx)\). If \(f\) is strictly convex on the relevant interval, the inequality is strict.

For an exponential-rate mixture, let \(\Lambda>0\) be a nonconstant random rate and set \(S(t)=\mathbb E[e^{-\Lambda t}]\). For every \(t>0\), \(f''(t)=\operatorname{Var}_t(\Lambda)>0\), where \(\operatorname{Var}_t\) is variance under the exponentially tilted rate law with weights proportional to \(e^{-\Lambda t}\). Thus \(f\) is strictly convex. If \(\Lambda\) is constant, then \(S(t)=e^{-\lambda t}\) and \(S(qx)=S(x)^q\), proving the equality boundary.

A concrete two-rate witness takes \(\Lambda=1\) or \(10\), each with probability \(1/2\), and \(m=1, x=1/5\). Then
\[
 S(t)=\tfrac12(e^{-t}+e^{-10t}),\qquad
 S(2/5)-S(1/5)^2=\tfrac14(e^{-1/5}-e^{-2})^2>0.
\]
Numerically, \(S(2/5)\approx0.344317842462\) while \(S(1/5)^2\approx0.227560500412\). This calculation illustrates the theorem; the proof is analytic and does not depend on numerical evaluation.

## Verification

The liability construction gives source net worth \(1-(1-x)=x\) and each target net worth \(1+(1-x)/m-[1+(1-x)/m-x]=x\). The source's total shortfall is allocated equally, so the all-target default threshold is exactly \((m+1)x\), not merely a sufficient bound. The star is acyclic, with source-to-target edges only, so there is no circular clearing ambiguity.

The included standard-library script evaluates the two-rate witness at high decimal precision and checks representative values of \(m\) and \(x\). Those finite numerical checks are supplementary only; the universal inequality follows from convexity as proved above.

## Relationship to prior work

Glasserman and Young's 2013 working paper, later published as *How Likely Is Contagion in Financial Networks?*, defines weak contagion by comparing a single-source cascade probability bound with the probability of independent direct defaults. Its Theorem 2 and Corollary 3 establish weak contagion under increasing-failure-rate (IFR) assumptions, including equal outside assets. In the probability comparison used in its bound, the same paper notes equality for pure exponential shocks when the source is fully financially connected and outside assets are equal; it also notes that Pareto-like tails can reverse the comparison at sufficiently large thresholds. The present result supplies a complementary all-feasible-threshold statement for log-convex survival and, in particular, light-tailed non-degenerate mixtures of exponential rates: latent rate heterogeneity makes the inequality strict even though the tail is not Pareto-like.

Visentin, Battiston, and D'Errico's 2016 preprint *Rethinking Financial Contagion* compares aggregate loss ordering across contagion models for arbitrary shock distributions. That observable differs from the event-probability comparison here; it does not imply the stated star-network inequality. The classical Eisenberg–Noe clearing framework supplies the payment mechanism, while the exact probability comparison follows from the liability construction and convexity argument given in this note.

## Limitations

The conclusion is restricted to an acyclic star, equal outside assets and equal initial net worth, a source whose liabilities are entirely interbank and equally allocated, independent shocks with a common log-convex survival function, and thresholds below the outside-asset cap. The strict statement is guaranteed for non-degenerate exponential-rate mixtures; no empirical calibration of bank shocks is asserted. The result compares probabilities of two specified events, not systemic-loss magnitudes, correlated shocks, recovery uncertainty, fire sales, or arbitrary networks. Broader reliability-theory results on log-convex survival are relevant background; no claim is made that the convexity inequality itself is new outside this network application.

## References

1. P. Glasserman and H. P. Young, “How Likely Is Contagion in Financial Networks?”, Office of Financial Research Working Paper 13-09, first publicly posted 21 June 2013; subsequently *Journal of Banking & Finance* 50 (2015), 383–399. DOI: 10.1016/j.jbankfin.2014.02.006. Open working-paper text: https://www.financialresearch.gov/working-papers/files/OFRwp0009_GlassermanYoung_HowLikelyContagionFinancialNetworks.pdf
2. G. Visentin, S. Battiston, and M. D'Errico, “Rethinking Financial Contagion,” arXiv:1608.07831, first posted 28 August 2016. https://arxiv.org/abs/1608.07831
3. L. Eisenberg and T. H. Noe, “Systemic Risk in Financial Systems,” *Management Science* 47(2) (2001), 236–249. DOI: 10.1287/mnsc.47.2.236.9835.
