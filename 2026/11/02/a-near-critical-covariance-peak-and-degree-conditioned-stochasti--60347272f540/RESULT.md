# The near-critical maximum of root-degree–cluster covariance in recursive trees

## Finding

In a uniform random recursive tree on vertices \(1,\ldots,n\), each vertex \(j\ge2\) independently chooses a uniform parent from \(\{1,\ldots,j-1\}\). Retain edges independently with probability \(p\in[0,1]\). Write \(D_n\) for the number of children of vertex 1 **before** deletion and \(C_n(p)\) for the size of the retained component of vertex 1. Let \(L=\log n\), with natural logarithm, and \(c=\zeta(2)-1\).

For any fixed \(\lambda\ge0\), put \(p=1-\lambda/L\) once this belongs to \([0,1]\). Then
\[
 \frac{L}{n}\operatorname{Cov}(D_n,C_n(p))\longrightarrow c\lambda e^{-\lambda}.
\]
The convergence is uniform for \(\lambda\) in each fixed compact subinterval of \([0,\infty)\). In particular,
\[
 \max_{0\le p\le 1}\operatorname{Cov}(D_n,C_n(p))\sim \frac{c}{e}\frac{n}{\log n},
 \qquad (1-p_n)\log n\longrightarrow1
\]
for **every** choice of maximizing probabilities \(p_n\).

## Assumptions and scope

The tree is rooted at vertex 1 and the sample size is an integer \(n\ge3\). All parent choices and retention marks are mutually independent. The degree is measured in the original tree, not in the retained forest. The maximization is finite-sample and allows \(p\) to vary with \(n\). No finite-sample uniqueness or result for correlation is asserted.

## Proof

Let \(I_j\) indicate that the parent of vertex \(j\) is 1, and let \(X_j\) indicate root connectivity, with \(X_1=1\) and \(C_j=\sum_{i=1}^j X_i\). Write \(M_j(p)=\prod_{t=1}^{j-1}(1+p/t)\). We first recall the exact finite covariance from [1], deriving it to fix normalization and endpoints. Conditional on the history through vertex \(j-1\), \(X_j\) has expectation \(pC_{j-1}/(j-1)\). Thus \(\mathbb E C_j=M_j(p)\), and the conditional expectation of \(C_n\) given the history through \(j\) is \(M_n(p) C_j/M_j(p)\). For \(t=j-1\), \(I_j\) is independent of the preceding history and \(\mathbb E[I_jX_j]=p/t\). It follows that
\[
 \frac{\operatorname{Cov}(I_j,C_n)}{M_n(p)}
 =\frac{p}{tM_{t+1}(p)}\left(1-\frac{M_t(p)}t\right)
 =\frac1{M_t(p)}-\frac1{M_{t+1}(p)}-\frac{p}{t(t+p)}.
\]
Summing over \(j=2,\ldots,n\) gives the identity from [1]. With \(\delta=1-p\), rewriting the summand as
\[
 \frac{p}{t(t+p)}=\frac1{t(t+1)}-\frac{\delta}{(t+1)(t+p)}
\]
gives the convenient form
\[
 V_n(p):=\operatorname{Cov}(D_n,C_n(p))= M_n(p)\left[\frac1n+\delta T_n(p)\right]-1,
 \qquad T_n(p)=\sum_{t=1}^{n-1}\frac1{(t+1)(t+p)}.
\]
Each covariance summand is nonnegative since \(M_t(p)\le M_t(1)=t\). The covariance is zero at \(p=0,1\), also clear from the deterministic component sizes there. The finite function \(V_n\) is continuous, so maximizers exist.

For all \(0\le\delta\le1\),
\[
 \frac{M_n(1-\delta)}n=\prod_{t=1}^{n-1}\left(1-\frac{\delta}{t+1}\right)
 \le e^{-\delta(H_n-1)},\qquad H_n=\sum_{u=1}^n\frac1u.
\]
If \(\lambda\) is in a fixed interval \([0,K]\) and \(\delta=\lambda/L\), the log of the product is \(-\delta(H_n-1)+O(\delta^2)\), uniformly because \(\sum_{u\ge2}u^{-2}<\infty\). Since \((H_n-1)/L\to1\), the product tends uniformly to \(e^{-\lambda}\). Also \(T_n(p)\to c\) uniformly in this interval: the tails are bounded by \(\sum_{t\ge m}1/[t(t+1)]\) uniformly in \(p\), and each fixed summand tends uniformly to \((t+1)^{-2}\). Now
\[
 \frac{L}{n} V_n(1-\lambda/L)
 =\frac{M_n(1-\lambda/L)}n\left[\frac{L}{n}+\lambda T_n(1-\lambda/L)\right]-\frac{L}{n}.
\]
This proves the uniform profile.

Compact-window convergence alone does not justify maximizing over all retention probabilities. Use \(T_n(p)\le1\) and the global product bound to get, for any \(\lambda=\delta L\in[0,L]\),
\[
 0\le \frac{L}{n} V_n(1-\delta)
 \le e^{-\lambda(H_n-1)/L}\left(\frac Ln+\lambda\right).
\]
This upper bound goes to zero along any sequence with \(\lambda\to0\) or \(\lambda\to\infty\). The test point \(\lambda=1\) tends to the positive value \(c/e\); hence all maximizing sequences stay in a compact subinterval of \((0,\infty)\) for sufficiently large \(n\). On any subsequence with \(\lambda_n\to\lambda_*\), uniform convergence and comparison to the test point give \(c\lambda_*e^{-\lambda_*}\ge c/e\). Since \(\lambda e^{-\lambda}\) has its unique maximum at 1, \(\lambda_*=1\). This proves the localization of every maximizing sequence, and substituting into the uniform profile proves the claimed peak.

## Verification

The proof uses an exact covariance identity and a global bound; neither a finite parameter grid nor fixed-retention asymptotics establishes the supremum. As a small normalization check, at \(n=3\) the original tree is equally likely to be a path rooted at its end or a star rooted at its center. Their conditional component means are \(1+p+p^2\) and \(1+2p\), and their degrees are 1 and 2, giving covariance \(p(1-p)/4\), in agreement with the identity. The accompanying `verify.py` can check the finite input formula by exact enumeration and moment recurrences. Its window diagnostics illustrate rather than prove the limiting maximum.

## Relationship to prior work and limitations

[1] gives the exact same finite covariance and its fixed-retention asymptotics, explicitly not uniform at the endpoints. [2] conditions the original tree on its root degree using nested sets of root attachments; keeping common retention marks gives the conditional connectivity order directly. Neither finite identity nor conditional order is claimed here as a contribution. Baur [3] studies the root cluster near critical retention, including the \(1/\log n\) window for its size; that marginal calculation does not determine the covariance with the original degree. The specific claim here is the sharp peak and uniform critical-window response of this covariance, including why other regimes cannot contain a maximizing sequence. This comparison is bounded and does not establish historical priority beyond the sources inspected. The result is for this tree model and this covariance, not a peak of correlation or of the root-cluster size itself.

## References

1. *Exact root-degree–percolation-cluster dependence and asymptotic decoupling in recursive trees*. Resultary record `3992334979d1`, Finding and Proof §2. https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-exact-root-degree-percolation-cluster-dependence-and-asymptotic--3992334979d1
2. *Root-degree conditioning orders the nonroot offspring vector in recursive trees*. Resultary record `5277d5b0e024`, Proof steps 1–3. https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-root-degree-conditioning-orders-the-nonroot-offspring-vector-in--5277d5b0e024
3. E. Baur, *Percolation on random recursive trees*. https://arxiv.org/abs/1407.2508
