# Polynomial rare-left-tail counts for the Ulam–Kac adder and a universal Mahonian deficit

## Finding

Let \(U_t\), for integers \(t\geq0\), be independent and uniform on \(\{0,\ldots,t\}\). Define the Ulam–Kac adder by \(X_0=1\) and \(X_{t+1}=X_t+X_{U_t}\). For integers \(n\geq r\geq0\), set
\[
A_{n,r}=n!\Pr\{X_n=n+1+r\}.
\]
For **each fixed surplus \(r\)**, there are explicitly computable nonnegative integers \(h_{r,0},\ldots,h_{r,r}\) such that
\[
\boxed{A_{n,r}=\sum_{k=0}^{r}h_{r,k}\binom{n-r}{k}\quad(n\geq r),\qquad h_{r,r}=1.}
\]
Thus the exact rare-left-tail path count is a degree-\(r\) polynomial in the number of steps, with a positive integer binomial-basis representation. For \(r\geq1\), its next coefficient is \(h_{r,r-1}=2(r-1)\).

Write \(M_{n,r}\) for the **Mahonian number**, the number of permutations of \(\{1,\ldots,n\}\) with exactly \(r\) inversions, equivalently
\[
M_{n,r}=[z^r]\prod_{t=0}^{n-1}(1+z+\cdots+z^t).
\]
For every **fixed integer \(r\geq3\)**, the exact-degree leading discrepancy and its sharp relative limit are
\[
\boxed{M_{n,r}-A_{n,r}=(r-2)\binom{n-r}{r-2}+O_r(n^{r-3}),}
\]
\[
\boxed{\lim_{n\to\infty}n^2\left(1-\frac{A_{n,r}}{M_{n,r}}\right)=r(r-1)(r-2).}
\]
The coefficient \(r(r-1)(r-2)\) is exact, not numerical. In particular, the history feedback first appears two polynomial degrees below the leading near-minimal count.

## Assumptions and scope

All variables \(U_t\) are jointly independent and have the stated uniform distributions. All probabilities are for the original discrete-time process, without a mean-field or continuous-time approximation. The polynomial identity holds for every \(r\geq0\) and every integer \(n\geq r\); the Mahonian comparison and limit hold for every fixed integer \(r\geq3\) as \(n\to\infty\). No asymptotic uniformity in a growing surplus is asserted. For a binomial coefficient with nonnegative integer upper index, the usual convention \(\binom{m}{k}=0\) for \(k>m\) is used.

## Proof

**1. Freeze the early history.** Write \(e_t=X_t-(t+1)\), so \(e_0=0\) and the recursion becomes
\[
e_{t+1}=e_t+U_t+e_{U_t},\qquad e_t\geq0.
\]
A length-\(n\) history \((u_0,\ldots,u_{n-1})\), with \(0\leq u_t\leq t\), has probability exactly \(1/n!\). Fix \(r\) and the first \(r\) choices. Let \(\mathcal P_r\) consist of precisely those prefixes for which the resulting \(e_r\leq r\), and retain the resulting values \(e_0,\ldots,e_r\). If the final excess is \(r\), all later chosen indices must be at most \(r\), because choosing an index \(j>r\) contributes \(j+e_j>r\) to the nondecreasing excess. Conversely, every subsequent choice from \(\{0,\ldots,r\}\) adds exactly the *frozen* amount \(j+e_j\); later evolution cannot change an earlier \(e_j\).

With \(B_{\mathbf u}(z)=\sum_{j=1}^r z^{j+e_j}\), therefore, for all \(n\geq r\),
\[
A_{n,r}=\sum_{\mathbf u\in\mathcal P_r}
[z^{r-e_r}](1+B_{\mathbf u}(z))^{n-r}.
\]
Expanding by the binomial theorem gives the promised **finite** coefficients
\[
\boxed{h_{r,k}=\sum_{\mathbf u\in\mathcal P_r}
[z^{r-e_r}]B_{\mathbf u}(z)^k\in\mathbb Z_{\geq0},\qquad0\leq k\leq r.}
\]
Only \(k\leq r\) contributes because all nonzero terms in \(B_{\mathbf u}\) have degree at least one. When \(r=0\), the empty prefix gives \(A_{n,0}=1\).

**2. Top two coefficients.** For \(k=r\), a nonzero term requires \(e_r=0\) and \(r\) later choices each contributing one. The unique zero-excess prefix chooses index zero every time, and the only later increment of size one is index one; hence \(h_{r,r}=1\). For \(r\geq2\) and \(k=r-1\), a prefix of excess zero requires exactly one later increment two and \(r-2\) increments one, contributing \(r-1\). A prefix of excess one is obtained by choosing index one at exactly one of times \(1,\ldots,r-1\); its \(r-1\) possibilities each permit only all-one later increments. Thus \(h_{r,r-1}=2(r-1)\) for \(r\geq2\). For \(r=1\), direct inspection gives \(h_{1,0}=0\), as required.

**3. Compare with inversion codes.** The insertion construction for permutations shows that the inversion number has the same law as \(\sum_{t=0}^{n-1}U_t\). Thus \(M_{n,r}\) is the coefficient displayed above. Repeating the frozen-prefix argument **without feedback** gives coefficients \(\widetilde h_{r,k}\) in the same basis \(\binom{n-r}{k}\), with \(e_t\) replaced throughout by \(s_t=\sum_{i<t}u_i\) and each positive later increment weighted simply by its index \(j\). The previous paragraph proves \(\widetilde h_{r,r}=h_{r,r}=1\) and \(\widetilde h_{r,r-1}=h_{r,r-1}=2(r-1)\).

It remains to compare \(k=r-2\), assuming \(r\geq3\). Such a coefficient only uses prefixes with final excess zero, one or two. There is **no feedback** in a prefix with excess at most two: a positive feedback term \(e_{u_t}\) requires a previous positive choice and a subsequent selected index at least two; the resulting excess is at least four. Therefore the same prefixes of excess zero, one and two appear in both coefficient sums. For excess zero, the later-polynomial coefficients coincide. For excess two, all \(r-2\) later positive increments must equal one, so they also coincide.

For a prefix of excess one, exactly one of the positions \(1,\ldots,r-1\) selects index one, yielding \(r-1\) possible prefixes. In the inversion-code model, the \(r-2\) later positive increments must sum to \(r-1\), so precisely one selects index two; there are \(r-2\) choices. In the adder, if the unique early nonzero choice occurred at **time one**, then \(e_2=1\) and selecting index two later contributes three, not two; that entire prefix loses its \(r-2\) choices. For each of the other \(r-2\) prefixes, \(e_2=0\), so no contribution is lost. Consequently
\[
\widetilde h_{r,r-2}-h_{r,r-2}=r-2.
\]
All lower terms have degree at most \(r-3\) in \(n\). It follows that
\[
M_{n,r}-A_{n,r}=(r-2)\binom{n-r}{r-2}
+\sum_{k=0}^{r-3}(\widetilde h_{r,k}-h_{r,k})\binom{n-r}{k}.
\]
Since \(M_{n,r}=n^r/r!+O_r(n^{r-1})\), division gives the stated exact inverse-square limit.

## Verification

Run `python3 artifacts/verify.py` using Python's standard library. The script independently enumerates every index history for \(0\leq n\leq9\), recomputes both sets of finite-prefix coefficients for \(0\leq r\leq9\), checks the binomial-basis identities, and checks the top-coefficient and exact discrepancy identities. It reports **164 exact checks passed**. As examples, the computed adder coefficients are \((h_{3,0},\ldots,h_{3,3})=(0,4,4,1)\), \((h_{4,0},\ldots,h_{4,4})=(3,10,12,6,1)\), and \((h_{5,0},\ldots,h_{5,5})=(15,32,37,24,8,1)\). The verifier uses integer arithmetic; its finite exhaustive checks corroborate the analytic proof and do not establish the all-parameter results by enumeration.

## Relationship to prior work

Ben-Naim and Krapivsky [1, p. 2] introduce the same history-dependent sequence and record the isolated endpoint identities \(\Pr(X_n=n+1)=1/n!\) and \(\Pr(X_n=n+2)=(n-1)/n!\), but not a fixed-surplus polynomiality theorem or a Mahonian correction. Bonner [2, Sections 1–4 and 6] develops asymptotics of the **moments** of the adder and identifies first-passage questions; these moment results do not imply the present point probabilities. The author's expanded later treatment [3, Chapter 3] is also moment-centered. Standard Mahonian counts [4] provide the *comparison* law, not the recursive-adder count. The classical Brauer-chain enumeration [5] aggregates by endpoint without fixing the chain length; it does not give these joint fixed-length/fixed-surplus coefficients. No claim of a new inversion-count identity is made.

## Limitations

The result describes a fixed number of units above the minimum possible adder value, not the typical value or a surplus growing with \(n\). It does not establish a finite-\(n\) sign for the Mahonian minus adder coefficient outside the asserted asymptotic regime, nor a global stochastic order, a central limit theorem, or any open first-passage classification. Although the inspected sources do not provide the stated polynomial and discrepancy result, equivalent earlier formulations in broader addition-chain literature remain a bibliographic risk.

## References

[1] E. Ben-Naim and P. L. Krapivsky, *Growth and Structure of Stochastic Sequences*, arXiv:cond-mat/0208072v1, first posted 2002-08-05, especially pp. 1–2. https://arxiv.org/abs/cond-mat/0208072

[2] G. Bonner, *On the moments of the Ulam-Kac adder*, arXiv:2303.03606v1, first posted 2023-03-07, especially Sections 1–4 and 6. https://arxiv.org/abs/2303.03606

[3] G. Bonner, *Random Entanglement and History-Dependent Random Sequences*, 2025 dissertation, Chapter 3. https://asset.library.wisc.edu/1711.dl/SR36Z64DI2RXU8U/R/file-761d0.pdf

[4] OEIS A008302, Mahonian numbers: permutation inversion-count triangle. https://oeis.org/A008302

[5] OEIS A008927, Brauer/star-addition chains counted by endpoint. https://oeis.org/A008927
