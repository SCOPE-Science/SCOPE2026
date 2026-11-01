# Birth-rank phase transition in degree–path-length dependence of random recursive trees

## Finding
For every integer \(n\ge3\), let \(T_n\) be a uniformly random recursive tree with vertices \(1,\ldots,n\) and root \(1\). Write \(D_{n,j}\) for the number of direct children of vertex \(j\) and \(L_n\) for the sum of all root distances. For every \(1\le j\le n\),
\[
F_{n,j}:=\operatorname{Cov}(D_{n,j},L_n)
=\frac nj-1+\sum_{s=j}^{n-1}\left(\frac1s-\frac n{s^2}\right).
\]
The birth-rank profile \(F_{n,j}\) has precisely one negative-to-positive sign transition among \(1\le j<n\), with a possible zero at that transition. In particular, \(F_{n,1}<0\), \(F_{n,n-1}=(n-2)/(n-1)^2>0\), and \(F_{n,n}=0\). Let \(j_n\) be the *least* birth rank with \(F_{n,j_n}>0\). Then
\[j_n\sim\sqrt{\frac n{\log n}}\qquad(n\to\infty).\]
Thus the degree of an early-born vertex and total tree path length have negative dependence, whereas the corresponding covariance is positive for vertices born after the sharply located crossover.

## Assumptions and scope
The parent \(P_t\) of each vertex \(t=2,\ldots,n\) is independent of all other choices and uniform on \(\{1,\ldots,t-1\}\). Distances count edges. The outdegree \(D_{n,j}=\sum_{t=j+1}^{n}\mathbf1_{\{P_t=j\}}\) excludes the parent edge. At \(j=n\), this count is deterministically zero. All formulas are exact for finite integer \(n\) unless an asymptotic limit is explicitly displayed. This is a covariance statement, not a claim of stochastic monotonicity or conditional independence.

## Proof
Fix \(j<t\le n\), and set \(A_{t,j}=\mathbf1_{\{P_t=j\}}\). The tree on vertices \(1,\ldots,t-1\) is independent of \(P_t\). The expected depth of vertex \(r\) is \(H_{r-1}\), where \(H_0=0\) and \(H_m=\sum_{s=1}^m 1/s\). Hence the expected depth of a uniformly chosen parent for vertex \(t\) is
\[
\frac1{t-1}\sum_{r=1}^{t-1}H_{r-1}=H_{t-1}-1.
\]
Changing the parent of \(t\) changes the depth of \(t\) and of each eventual descendant of \(t\) by the same amount. Conditional on its original birth time \(t\), its expected final subtree size is \(n/t\): starting at size one, each successive birth at size \(s\) joins that subtree with probability its current size divided by \(s\), so its mean is multiplied by \((s+1)/s\), telescoping to \(n/t\). All later attachment choices are independent of \(P_t\). Accordingly,
\[
\operatorname{Cov}(A_{t,j},L_n)
=\frac1{t-1}\frac nt\big(1+H_{j-1}-H_{t-1}\big).
\]
The identity uses \(\operatorname{Cov}(A,Z)=\Pr(A=1)\{\mathbb E[Z\mid A=1]-\mathbb E[Z]\}\); it remains valid although the depth of vertex \(j\) is itself random. Summing this identity over \(t=j+1,\ldots,n\), expanding the harmonic difference, and changing the order of the *finite* double sum gives
\[
F_{n,j}=n\sum_{t=j+1}^{n}\frac{1+H_{j-1}-H_{t-1}}{t(t-1)}
=\frac nj-1+\sum_{s=j}^{n-1}\left(\frac1s-\frac n{s^2}\right).
\]
The root covariance is strictly negative: its summand for \(t=2\) is zero and all summands for \(t\ge3\) are negative. At the penultimate birth rank \(j=n-1\), the displayed formula simplifies to \((n-2)/(n-1)^2>0\). Subtraction of neighboring covariance formulas yields
\[
F_{n,j+1}-F_{n,j}=\frac{n-j(j+1)}{j^2(j+1)}.
\]
Thus \(F_{n,j}\) initially increases and subsequently decreases (one difference may be zero). Since it begins strictly negative, is positive at \(n-1\), and finally reaches \(F_{n,n}=0\), all nonpositive interior values lie before all positive interior values. There can be at most one interior zero.

To locate the transition, for \(j\to\infty\) with \(j=o(n)\), the harmonic-number and reciprocal-square-sum estimates give
\[
F_{n,j}=\log(n/j)-\frac{n}{2j^2}+O\!\left(\frac n{j^3}+\frac1j+\frac1n\right).
\]
For any fixed \(a>0\), substitute \(j=\lfloor a\sqrt{n/\log n}\rfloor\):
\[
\frac{F_{n,j}}{\log n}\longrightarrow \frac12\left(1-\frac1{a^2}\right).
\]
For fixed \(a<1\) this is negative, and for fixed \(a>1\) it is positive. The proven unique sign transition therefore implies \(j_n/\sqrt{n/\log n}\to1\).

## Verification
The companion `verify.py` exhaustively enumerates every recursive-parent sequence for sizes \(3\le n\le8\) and checks the formula for every vertex with exact rational arithmetic. It separately checks the sign-transition structure and neighboring-difference identity for \(3\le n\le500\), using exact arithmetic. Reproduce with `python3 verify.py` (standard library only). These finite computations are corroborating checks, not substitutes for the above all-size analytical argument.

## Relationship to prior work
The classical probability literature treats degrees and path lengths of random recursive trees. Janson's *Asymptotic degree distribution in random recursive trees* (2004 public online date) addresses aggregate counts of vertices at each outdegree, rather than the covariance of the outdegree of a **given birth rank** with total path length. An earlier finding on root attachments supplies an exact negative root-attachment/path-length profile; it is the \(j=1\) boundary, but it does not state the nonroot sign reversal or its square-root-over-logarithm transition scale. The present claim keeps the precise vertex birth rank instead of averaging it away.

## Limitations
This work concerns the independent-parent uniform recursive-tree model, not general preferential-attachment or plane recursive trees. It determines a covariance and its transition rather than a full joint distribution. Searches and available abstracts do not establish exhaustive historical priority: detailed full texts of every older degree/path-length publication were not accessible for comprehensive comparison. No independent mathematical audit has been performed.

## References
1. S. Janson, *Asymptotic degree distribution in random recursive trees*, Random Structures & Algorithms **26** (2005), 69–83, DOI: 10.1002/rsa.20046; first available online November 16, 2004.
2. R. T. Smythe and H. Mahmoud, *A survey of recursive trees*, Theory of Probability and Mathematical Statistics **51** (1995), 1–27. Historical background only; not relied on for a noncoverage assertion.
