# Exact two-target path separation: a finite Bernoulli decomposition and boundary crossover

## Finding

Let \(a,b\geq1\) be integers and \(N=a+b+1\). In the uniform vertex-cutting process on the \(N\)-vertex path with its unique source at position \(0\) and two targets at positions \(-a\) and \(b\), denote by \(S_{a,b}\) the number of cuts until both targets are absent from the source-connected component. Let \(A_{a,b}\) and \(B_{a,b}\) be Poisson–binomial random variables, separately defined by
\[
 A_{a,b}=\sum_{k=a+1}^{N-1}\xi_k,\qquad
 B_{a,b}=\sum_{k=b+1}^{N-1}\eta_k,
 \quad \Pr(\xi_k=1)=\Pr(\eta_k=1)=\frac1{k+1},
\]
with independent Bernoulli summands within each sum (the two families need not be coupled). Empty sums have value zero. The **exact finite-size probability-generating-function identity** is
\[
 \boxed{\mathbb E[z^{S_{a,b}-1}]
  =\prod_{k=a+1}^{N-1}\frac{k+z}{k+1}
   +\prod_{k=b+1}^{N-1}\frac{k+z}{k+1}-1.}
\]
It follows that \(\Pr(S_{a,b}=1)=1/N\) and, for all integers \(j\geq1\),
\[
 \Pr(S_{a,b}=j+1)=\Pr(A_{a,b}=j)+\Pr(B_{a,b}=j).
\]
A sharp distributional comparison is
\[
 \boxed{d_{\rm TV}(\mathcal L(S_{a,b}-1),\mathcal L(A_{a,b}))=\frac{a}{N},\qquad
 d_{\rm TV}(\mathcal L(S_{a,b}-1),\mathcal L(B_{a,b}))=\frac{b}{N}.}
\]
In particular, the total-variation error is exactly the fractional length of the short arm when approximation uses the Bernoulli sum associated with that arm.

There are **two different limiting regimes**. If \(N\to\infty\) and \(a/N\to x\in(0,1)\), then \(S_{a,b}\Rightarrow S_x\), where
\[
 \boxed{\mathbb E[z^{S_x}]=z\bigl(x^{1-z}+(1-x)^{1-z}-1\bigr),\quad 0\le z\le1.}
\]
For each \(j\geq1\), its exact mass function is
\[
 \Pr(S_x=j+1)=\frac{x(-\log x)^j+(1-x)(-\log(1-x))^j}{j!}.
\]
Equivalently, it is a mixture of \(1+\operatorname{Poi}(-\log x)\) conditioned on a positive Poisson count, with weight \(1-x\), and \(1+\operatorname{Poi}(-\log(1-x))\) conditioned on a positive Poisson count, with weight \(x\).

By contrast, if \(a/N\to0\) (so the source approaches the left endpoint proportionally), then with
\[
 \mu_N=\sum_{k=a+1}^{N-1}\frac1{k+1}=H_N-H_{a+1}\longrightarrow\infty,
\]
one has the **boundary Gaussian crossover**
\[
 \boxed{\frac{S_{a,b}-1-\mu_N}{\sqrt{\mu_N}}\Rightarrow\mathcal N(0,1).}
\]
The right-endpoint boundary case is symmetric. The finite-size mean is
\[
 \mathbb E S_{a,b}=1+2H_N-H_{a+1}-H_{b+1}.
\]

## Assumptions and scope

Fix a finite path with labeled positions \(-a,-a+1,\ldots,-1,0,1,\ldots,b\), with one source \(0\) and targets \(-a,b\). At every step choose one vertex uniformly from the vertices still in the source-connected component, delete it, and discard components disconnected from the source. Stop at the first step when both original target vertices are absent. Once a target is discarded, it never returns. A cut of the source removes the entire source-connected component and stops the process. The random variable \(S_{a,b}\) counts **actual selected deletions**, not all vertices discarded in those deletions. The theorem holds for every integer \(a,b\ge1\). Limits range over any sequences of such integers with \(N\to\infty\). The independent Bernoulli sums above are auxiliary distributional objects, not a claim about independence of cuts on opposite arms.

## Proof

**1. One remaining target and an inert arm.** Suppose the remaining source-connected path has a target on the left arm of length \(c\ge0\) and a right arm of length \(d\ge0\) whose original endpoint target has already disappeared. Let \(F_c(d;z)\) be the generating function of additional cuts needed to remove the active target. The right-side vertices are inert as targets, but they may be chosen and shorten the right arm. The first cut removes the active target if it chooses the source or any of the \(c\) left vertices; cutting right-side vertex \(j\in\{1,\dots,d\}\) leaves exactly \(j-1\) right vertices. Therefore, for all \(d\ge0\),
\[
 F_c(d;z)=\frac{z}{c+d+1}\left(c+1+\sum_{h=0}^{d-1}F_c(h;z)\right).
\]
This also gives \(F_c(0;z)=z\). Define \(Q_c(d;z)=c+1+\sum_{h=0}^{d-1}F_c(h;z)\). Its recursion is
\[
 Q_c(0;z)=c+1,\qquad Q_c(d+1;z)=Q_c(d;z)\left(1+\frac z{c+d+1}\right),
\]
so
\[
 Q_c(d;z)=(c+1)\prod_{k=c+1}^{c+d}\left(1+\frac zk\right).
\]

**2. Two targets.** In the first cut, selecting the source (one choice) stops the process. Selecting left-side vertex \(j\) destroys the left target and leaves the right target with an inert left arm of length \(j-1\); selecting right-side vertex \(j\) is symmetric. Thus
\[
 \mathbb E[z^{S_{a,b}}]
 =\frac zN\left(1+\sum_{h=0}^{a-1}F_b(h;z)+\sum_{h=0}^{b-1}F_a(h;z)\right)
 =z\left(\frac{Q_b(a;z)+Q_a(b;z)}N-1\right).
\]
For either \((c,d)=(a,b)\) or \((b,a)\),
\[
 \frac{Q_c(d;z)}N=\frac{c+1}{N}\prod_{k=c+1}^{N-1}\frac{k+z}{k}
 =\prod_{k=c+1}^{N-1}\frac{k+z}{k+1};
\]
the last equality telescopes. Substitution yields the exact boxed generating-function identity. Both products are Bernoulli-sum generating functions because \((k+z)/(k+1)=(k/(k+1))+z/(k+1)\).

**3. Distribution and sharp total variation.** The constant term of the first product is \((a+1)/N\) and of the second is \((b+1)/N\), so subtraction of \(1\) leaves \(1/N\). For all positive degrees the subtraction vanishes. Comparing the distribution of \(S_{a,b}-1\) with that of \(A_{a,b}\), every strictly positive atom gains \(\Pr(B_{a,b}=j)\), and the zero atom loses exactly \(\Pr(B_{a,b}\ge1)=a/N\). Thus the sum of absolute atom differences is \(2a/N\), establishing the first total-variation formula; the second follows by exchanging the arms. Taking derivatives at \(z=1\) gives the exact mean formula.

**4. Macroscopic interior limit.** If \(a/N\to x\in(0,1)\), then for each fixed \(z\in[0,1]\),
\[
 \log\prod_{k=a+1}^{N-1}\frac{k+z}{k+1}
 =\sum_{k=a+1}^{N-1}\log\left(1+\frac{z-1}{k+1}\right)
 \longrightarrow(z-1)\log(1/x).
\]
Indeed, the sum of quadratic Taylor remainders is \(O(1/a)=o(1)\), and the harmonic sum tends to \(-\log x\). Likewise the other product tends to \((1-x)^{1-z}\). Generating-function convergence (or convergence of each coefficient and normalization) proves weak convergence to the displayed law. For \(j\ge1\), expanding \(x^{1-z}=x\exp(-z\log x)\) and its counterpart gives the mass formula. The masses sum to \(x((1/x)-1)+(1-x)((1/(1-x))-1)=1\), so there is no escape of mass. The formula at \(x=1/2\) reduces to \(\mathbb E[z^{S_x}]=z(2^z-1)\), the previously known symmetric limit.

**5. Endpoint crossover.** If \(a/N\to0\), the first TV identity gives \(d_{\rm TV}(\mathcal L(S_{a,b}-1),\mathcal L(A_{a,b}))=a/N\to0\). Its mean is \(\mu_N=H_N-H_{a+1}=\log(N/(a+1))+O(1)\to\infty\); its variance is \(\mu_N-\sum_{k=a+1}^{N-1}(k+1)^{-2}=\mu_N+O(1)\), hence asymptotic to \(\mu_N\). The summands are independent and bounded by \(1\), while the standard deviation diverges; consequently Lindeberg's condition holds, giving \((A_{a,b}-\mu_N)/\sqrt{\mu_N}\Rightarrow\mathcal N(0,1)\). Total-variation convergence transfers this limit to \(S_{a,b}-1\). Swapping \(a,b\) proves the other endpoint statement. This completes the proof.

## Verification

The accompanying `verify_path_cutting.py` computes the full stopping-time distribution by an **independent exact-rational Markov recurrence**, without invoking the claimed polynomial decomposition, for every ordered positive pair \((a,b)\) with \(3\le N\le12\). It compares every probability against a separately constructed Poisson–binomial product and checks total probabilities, means, positive-degree coefficient identities, and both sharp total-variation equalities. It passed 964 assertions across 55 finite path instances. Four additional exact finite-sum numerical comparisons corroborate mean formulas. This finite verification corroborates the algebra; it cannot by itself verify the asymptotic statements, which are proved in Step 4 and Step 5.

Run with a standard Python 3 interpreter from a directory containing this document's bundled `verify_path_cutting.py`:

`python3 verify_path_cutting.py`

## Relationship to prior work

The graph separation/cutting model and its balanced two-target path special case were introduced and analyzed by Burghart, *A Modification of the Random Cutting Model* (arXiv:2111.02968; first public November 4, 2021). Its Section 2, Proposition 1 establishes the limiting \(1+\operatorname{Poi}(\log2)\) law conditional on a positive Poisson count for a centered source. That **special case is not new**. The present statement derives an exact finite-size two-arm probability generating function, exact total-variation approximation by a Poisson–binomial sum, all asymmetric macroscopic limits, and the Gaussian endpoint crossover. Its centered case is consistent with, and strictly includes as a consequence, the earlier asymptotic limit. Existing general cutting/record formulations may provide alternative routes to these facts; the available source comparisons do not rule out every implicit or unpublished prior derivation.

## Limitations

The proof assumes a deterministic path, uniform deletion of one surviving source-connected vertex per step, exactly one source, and the two original endpoints as targets. It does not treat different graph families, multiple sources, weighted cutting, cutting until the source is isolated, or joint laws of discarded component sizes. The endpoint central limit theorem concerns the regime with one arm of size sublinear in \(N\), and the interior limit requires an asymptotically positive fraction on both arms. Originality is judged relative to the accessible compared sources, not certified as absolute historical priority. No independent mathematical audit has been performed.

## References

1. F. Burghart, *A Modification of the Random Cutting Model*, arXiv:2111.02968v1 (2021-11-04), revised arXiv:2111.02968v2 (2022-01-04), DOI: 10.48550/arXiv.2111.02968. Primary MSC2020 60C05. Full text: https://arxiv.org/html/2111.02968v2 .
2. F. Burghart, *A modification of the random cutting model*, *Advances in Applied Probability* 56 (2024), 287–314, DOI: 10.1017/apr.2023.22 (published online 2023-08-07).
3. S. Janson, *Random cutting and records in deterministic and random trees*, *Random Structures & Algorithms* 29 (2006), 139–179; related classical rooted-tree cutting/record model, not a verified statement of the present two-target theorem.
