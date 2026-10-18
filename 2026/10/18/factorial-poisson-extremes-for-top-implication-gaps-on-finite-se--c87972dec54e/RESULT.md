# Factorial Poisson extremes for top-implication gaps on finite semi-Heyting chains

## Finding
For every integer \(n\geq2\), equip the fixed \(n\)-element bounded chain with a uniformly chosen semi-Heyting implication \(\to\), and write its elements \(c_0<\cdots<c_{n-1}=\top\). Define the top-implication gap \(K_{i,n}=n-1-j\) when \(c_i\to\top=c_j\), for \(0\leq i\leq n-2\). The gaps are independent, and for \(m=n-1-i\) their exact law is
\[
\Pr(K_{i,n}=k)=\frac{1}{k!E_m}\quad(0\leq k\leq m),\qquad E_m=\sum_{r=0}^m\frac1{r!}.
\]
Thus each gap is a Poisson(1) variable conditioned to be at most its remaining chain length. The finite row enumeration underlying this identity is previously known [1,2]; the finding here is the asymptotic profile and factorial extreme-value law extracted from it.

For any integer thresholds \(t_n\to\infty\) with \(t_n=o(n)\) and \(n/t_n!\) bounded, let \(Z_n(t_n)=\#\{0\leq i\leq n-2:K_{i,n}\geq t_n\}\), and put \(\mu_n=n/(e\,t_n!)\). Then the total-variation distance satisfies
\[
d_{\mathrm{TV}}\bigl(\mathcal L(Z_n(t_n)),\operatorname{Poisson}(\mu_n)\bigr)\longrightarrow0.
\]
In particular, along every subsequence for which \(\mu_n\to\lambda\in[0,\infty)\), one has \(Z_n(t_n)\Rightarrow\operatorname{Poisson}(\lambda)\) and
\[
\Pr\!\left(\max_{0\leq i<n-1}K_{i,n}<t_n\right)\longrightarrow e^{-\lambda}.
\]
The maximum itself satisfies
\[
\frac{\max_{0\leq i<n-1}K_{i,n}}{\log n/\log\log n}\longrightarrow1
\quad\text{in probability}.
\]
Moreover, for every fixed \(k\geq0\), the proportion of gaps equal to \(k\) converges in probability to \(e^{-1}/k!\), and their average converges in probability to \(1\).

There is a marked sampling distinction: uniformly sampling an admissible *unary top-implication reduct* (rather than uniformly sampling the full binary expansion) makes the gaps independent and uniform on \(\{0,\ldots,n-1-i\}\). Under that second sampling law, the sum of the gaps, divided by \(n(n-1)\), converges in probability to \(1/4\); for uniformly sampled full implications, the sum divided by \(n-1\) converges to \(1\).

## Assumptions and scope
A semi-Heyting algebra is a bounded distributive lattice with binary operation \(\to\) such that, for every \(x,y,z\),
\[
x\wedge(x\to y)=x\wedge y,\quad
x\wedge(y\to z)=x\wedge((x\wedge y)\to(x\wedge z)),\quad
x\to x=\top.
\]
There is one labelled linear chain for each size and all distinct operations on this fixed chain are equiprobable. No distributions on arbitrary lattices, subvarieties, or random partial orders are asserted. The quantitative Poisson approximation holds for growing integer thresholds satisfying the two stated conditions; positive finite limiting Poisson means are naturally seen along subsequences because factorial scales are discrete.

## Proof
**Finite row normal form (published structural input, checked here).** Fix a row indexed by \(i<n-1\), let \(m=n-1-i\), and let \(c_i\to\top=c_j\) with \(i\leq j\leq n-1\). The axioms force \(c_i\to c_h=c_h\) for \(h<i\), \(c_i\to c_i=\top\), and \(c_i\to c_h=c_j\) for \(h>j\). For each \(i<h\leq j\), the value \(c_i\to c_h\) can independently be any chain element at least \(c_h\). Conversely, any such row choices across all indices satisfy the axioms. Indeed, the second semi-Heyting axiom only constrains \(c_i\to c_h\) when \(c_h<i\); the third axiom reduces, when its first argument exceeds its second, to constancy of truncations of the second row above the first argument, which is immediate from the displayed row form. The other cases are direct. This is the familiar row construction of [1,2], not an independently claimed classification.

The number of rows with the selected \(j\) is therefore
\[
\prod_{h=i+1}^{j}(n-h)=\frac{m!}{(n-1-j)!}=\frac{m!}{k!}.
\]
Summing over \(k=0,\ldots,m\) gives \(m!E_m\) possible rows. Because distinct rows may be selected independently, a uniformly chosen complete implication makes all \(K_{i,n}\) independent with the displayed exact probabilities. In particular, \(1\leq E_m\leq e\).

**Factorial extreme law.** Reindex rows by \(m=1,\ldots,n-1\) and put
\[
p_{m,t}=\frac{\sum_{k=t}^{m}1/k!}{E_m}\quad(m\geq t),\qquad p_{m,t}=0\quad(m<t).
\]
For \(m\geq2t\), the elementary estimates \(\sum_{k=t}^{\infty}1/k!=(1+O(1/t))/t!\), \(E_m=e+O(1/(m+1)!)\), and \(\sum_{k>m}1/k!\leq 2/(m+1)!\) imply
\[
p_{m,t}=\frac{1+O(1/t)}{e\,t!}
\]
uniformly as \(t\to\infty\). There are only \(2t\) exceptional small rows, and for every \(m\), \(p_{m,t}\leq2/t!\). Therefore, whenever \(t=o(n)\),
\[
\sum_{m=1}^{n-1}p_{m,t}=\frac{n}{e\,t!}\bigl(1+O(1/t)+O(t/n)\bigr),
\quad
\sum_{m=1}^{n-1}p_{m,t}^{\,2}\leq\frac{4n}{(t!)^2}.
\]
With \(n/t!\) bounded, the first sum differs from \(\mu_n\) by \(o(1)\), and the second is \(o(1)\). The independent-indicator Poisson approximation (which follows, for example, by coupling each Bernoulli indicator to a Poisson variable of equal mean) gives
\[
d_{\mathrm{TV}}\bigl(\mathcal L(Z_n(t)),\operatorname{Poisson}(\textstyle\sum_m p_{m,t})\bigr)\leq\sum_m p_{m,t}^2.
\]
Poisson laws with means differing by \(\delta\) have total-variation distance at most \(|\delta|\), proving the first assertion and its zero-count consequence.

For maximum localization, let \(L_n=\log n/\log\log n\) and choose thresholds \(t_n^\pm=\lfloor(1\pm\varepsilon)L_n\rfloor\), with a harmless upward integer adjustment for the upper bound. Stirling's formula yields \(n/(t_n^+!)\to0\) and \(n/(t_n^-!)\to\infty\) for every fixed \(0<\varepsilon<1\). The upper bound follows from \(\Pr(Z_n(t_n^+)>0)\leq\sum_m p_{m,t_n^+}\to0\); the lower bound from \(\Pr(Z_n(t_n^-)=0)\leq\exp(-\sum_m p_{m,t_n^-})\to0\). This proves the convergence of the normalized maximum.

**Empirical law and contrasting samplings.** For fixed \(k\), \(\Pr(K_{i,n}=k)=1/(k!E_m)\to e^{-1}/k!\) as \(m\to\infty\). A Cesàro average gives the limiting mean frequency, and independence bounds its variance by \(1/(n-1)\). The means \(\mathbb E K_{i,n}=E_{m-1}/E_m\to1\), and \(\mathbb E K_{i,n}^2\leq2e\), proving the asserted average convergence by the same argument. Under uniform sampling of the unary reduct, each \(c_i\to\top\) can independently be any \(c_j\) with \(j\geq i\) because all these choices admit some row completion; therefore the corresponding gaps are independent discrete uniforms with means \(m/2\) and variances \(m(m+2)/12\). Summing means and variances yields the \(1/4\) limit.

## Verification
The provided standard-library Python program `verify.py` separately exhausts all binary tables on chains through size three, tests every semi-Heyting axiom, and confirms the row construction gives precisely all valid tables. It also generates and verifies all \(10{,}400\) operations on the five-element chain, reproduces the row counts \(1,2,5,16,65\), checks top-reduct fibers, and compares the two finite sampling distributions. Reproduce with `python3 verify.py`. No finite execution is treated as proof of any limit; those follow from the preceding estimates.

## Relationship to prior work
Monteiro–Cornejo–Viglizzo [1] explicitly give the constructive enumeration of all semi-Heyting structures on finite chains. Cornejo–Monteiro–Sankappanavar–Viglizzo [2] supply refined finite counts and extension/subalgebra problems. All finite row formulas used above are consequently credited as published input or direct consequences of that input. The focus here is instead the independent truncated-Poisson row-gap interpretation, the factorial-scale Poisson law for rare exceptional unary values, maximum-gap localization, and contrast between two natural uniform samplings. Neither inspected paper's main results or discussed sections state these stochastic asymptotics. Historical work by Abad–Cornejo–Díaz Varela [3] supplies earlier finite chain enumeration; its full text was not independently inspected and is an explicit originality risk.

## Limitations
Originality is not established by a failed search: equivalent probabilistic asymptotics might appear under different terminology in prior random-algebra work. In particular, the finite row normal form and the finite fiber formulas are not new. The factorial critical scale produces positive limiting means chiefly along subsequences; there is no claim of one nonoscillatory limit at arbitrary sequence \(n\). The proof covers fixed finite chains only, assumes uniform distribution on complete binary expansions, and distinguishes that distribution from uniform distribution on the unary reducts. No independent review has been performed.

## References
[1] L. F. Monteiro, J. M. Cornejo, I. D. Viglizzo, *A recursive formula for the number of semi-Heyting algebras definable on a finite chain*, arXiv:1710.02408 (first public version 2017-10-06), https://arxiv.org/abs/1710.02408.

[2] J. M. Cornejo, L. F. Monteiro, H. P. Sankappanavar, I. D. Viglizzo, *A note on chain-based semi-Heyting algebras*, Mathematical Logic Quarterly 66(4) (2020), 409–417, https://doi.org/10.1002/malq.201900070.

[3] M. Abad, J. M. Cornejo, J. P. Díaz Varela, *The variety generated by semi-Heyting chains*, Soft Computing 15(4) (2011), 721–728, https://doi.org/10.1007/s00500-010-0604-0 (historical background; full text not inspected).
