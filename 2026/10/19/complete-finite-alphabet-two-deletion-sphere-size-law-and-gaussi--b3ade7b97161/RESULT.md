# Complete finite-alphabet two-deletion-sphere size law and Gaussian fluctuations

## Finding
Let \(q\ge 2\) and \(n\ge 2\) be integers. For \(x\in\{0,\ldots,q-1\}^n\), let \(D_2(x)\) be the **set** of distinct length-\(n-2\) subsequences obtained by deleting exactly two positions. Define \(B_{n,q}=|D_2(X)|\) for a uniformly random word \(X\). The complete exact distribution of \(B_{n,q}\), for every alphabet size and length, is given by a two-state transfer polynomial:
\[
 F_{q,n}(u,v,z)=q\begin{pmatrix}v&(q-1)u\end{pmatrix}
 \begin{pmatrix}1&(q-1)u\\v&u(q-2+z)\end{pmatrix}^{n-2}
 \begin{pmatrix}1\\1\end{pmatrix}.
\]
If \(c_{k,s,t}=[u^kv^sz^t]F_{q,n}(u,v,z)\), then the **number** of source words whose two-deletion ball has size exactly \(b\) is
\[
 N_{q,n}(b)=\sum_{k,s,t:\,\binom{k+1}{2}+s-t=b}c_{k,s,t},\qquad
 \Pr\{B_{n,q}=b\}=N_{q,n}(b)/q^n.
\]
In particular, with \(m=n-1\), its exact mean and variance are
\[
 \mathbb EB_{n,q}=\frac{1+n(q-1)+\binom n2(q-1)^2}{q^2},
\]
\[
 \boxed{\operatorname{Var}(B_{n,q})=\frac{(m-1)(q-1)}{2q^4}
 \left(2m^2(q-1)^2-m(q-1)(2q-3)+2q(q-2)\right).}
\]
For each fixed \(q\ge2\), as \(n\to\infty\),
\[
 \frac{B_{n,q}-\mathbb EB_{n,q}}{n^{3/2}}
 \ \xrightarrow{\mathrm d}\ \mathcal N\!\left(0,\frac{(q-1)^3}{q^4}\right).
\]

## Assumptions and scope
The alphabet is a set of \(q\) distinct symbols, not necessarily a field. Positions in a source word are labeled; deletion outputs are deduplicated as strings, not counted with multiplicity. No statement concerns intersections of two different deletion balls, insertion balls, or deletion-location probabilities. All finite statements hold for each integer \(q\ge2\), \(n\ge2\); the limit holds with \(q\) fixed.

For a deterministic word \(x\), let \(R\) be its number of maximal constant-symbol runs, let \(S\) be the number of such runs of length at least two, and let
\[
 T=\#\{i:2\le i\le n-1,\ x_{i-1}=x_{i+1}\ne x_i\}.
\]
These are the transition count plus one, the long-run count, and the count of length-three returns. Their exact relationship to the two-deletion sphere is
\[
 \boxed{|D_2(x)|=\binom R2+S-T.}
\]

## Proof
**1. The deterministic identity.** For a word \(w\) of length at least two and an appended symbol \(c\), every two-deletion descendant of \(wc\) either retains the final \(c\) or deletes it. Therefore
\[
 D_2(wc)=(D_2(w)c)\cup D_1(w),
\]
where \(D_1(w)\) denotes the distinct one-deletion descendants. As is immediate by deleting once from each constant run, \(|D_1(w)|=R(w)\). The intersection consists precisely of the members of \(D_1(w)\) ending in \(c\): removing their final \(c\) produces a member of \(D_2(w)\). If \(c\) equals the final symbol of \(w\), the intersection has \(R(w)\) members when the final run of \(w\) has length at least two, and \(R(w)-1\) members otherwise. This is exactly the change in \(S\), with \(R\) and \(T\) unchanged. If \(c\) differs from the final symbol, the intersection has one member precisely when \(w\) ends in a singleton run whose preceding symbol is \(c\); otherwise it is empty. In that case \(R\) increases by one, contributing the old value \(R(w)\) to \(\binom R2\), while \(T\) increases by exactly the intersection indicator and \(S\) is unchanged. Hence in both cases the right-hand side \(\binom R2+S-T\) has the required increment. The formula holds at length two, where every two-deletion ball has size one; induction proves it for all lengths and alphabets.

**2. Exact transfer polynomial.** Write \(m=n-1\), and let \(A_i=\mathbf1\{X_i\ne X_{i+1}\}\) for \(1\le i\le m\). Then
\[
 K=\sum_{i=1}^m A_i=R-1,\quad
 S=(1-A_1)+\sum_{i=2}^m A_{i-1}(1-A_i),
\]
while \(T\) counts those adjacent active edges whose second change returns to the symbol two positions earlier. There are \(q\) choices for the initial letter. The first edge either repeats the previous symbol (weight \(v\), recording a long initial run), or changes it in \(q-1\) ways (weight \((q-1)u\)). Given the previous edge, the next edge has four possibilities: repeat after repeat (weight \(1\)); change after repeat (weight \((q-1)u\)); repeat after change (weight \(v\)); or change after change (weight \(u((q-2)+z)\)), where exactly one of the \(q-1\) new symbols returns to the symbol two positions earlier. This is precisely the claimed matrix. Every source word contributes its monomial \(u^Kv^Sz^T\) exactly once. The coefficient aggregation follows from the deterministic identity. This also establishes the full law at the boundary \(n=2\), where the matrix power is zero.

**3. Variance.** For uniform letters, the edge variables \(A_i\) are independent Bernoulli with \(p=(q-1)/q\). To see this, each fixed edge pattern having \(k\) changes is realized by exactly \(q(q-1)^k\) words. Conditional on all edges, each of the \(H=\sum_{i=2}^m A_{i-1}A_i\) active edge pairs returns to the preceding symbol with conditional probability \(h=1/(q-1)\); these return indicators are conditionally independent by revealing new letters sequentially. Thus \(T\mid(A_1,\ldots,A_m)\) is binomial with parameters \(H,h\).

For \(m\ge2\), set \(Z_i=A_i-p\) and \(v_0=p(1-p)\), and let \(U=\mathbb E(B_{n,q}\mid A_1,\ldots,A_m)\). Using \(S=1+\sum_{i=2}^{m-1}A_i-H\) and \(R=K+1\), direct expansion of \(U=\binom{K+1}2+S-hH\) gives
\[
 U-\mathbb EU=p(m-1)\sum_i Z_i+\sum_{i<j}d_{ij}Z_iZ_j,
 \qquad
 d_{ij}=\begin{cases}-h&j=i+1,\\1&j\ge i+2.\end{cases}
\]
Indeed every linear coefficient is \(p(m-1)\), since \(p(1+h)=1\). The independent centered variables make the singleton products and distinct pair products mutually orthogonal, so
\[
 \operatorname{Var}(U)=mp^2(m-1)^2v_0+
 v_0^2\left(\frac{(m-1)(m-2)}2+(m-1)h^2\right).
\]
Also \(\mathbb E\operatorname{Var}(B_{n,q}\mid A)=(m-1)p^2h(1-h)\). The law of total variance, followed by elementary simplification, yields the displayed rational polynomial. For \(n=2\), the ball size is identically one and the same polynomial is zero. The mean is a consistency check from double counting \((x,y)\) with \(y\in D_2(x)\): any prescribed word \(y\) of length \(n-2\) has exactly \(1+n(q-1)+\binom n2(q-1)^2\) distinct supersequences of length \(n\).

**4. Gaussian limit.** The first summand of the centered expansion for \(U\) has variance of order \(n^3\) and obeys the usual Bernoulli central limit theorem. The quadratic summand has variance \(O_q(n^2)\), whereas the residual noise \(B_{n,q}-U\) has variance \(O_q(n)\) by the conditional-binomial formula. Both vanish in \(L^2\) after division by \(n^{3/2}\). Slutsky's theorem gives the limit with variance \(p^2v_0=(q-1)^3/q^4\).

## Verification
The standalone `verify.py` uses three structurally different checks: (i) literal enumeration of distinct deletion-output strings, (ii) the run/return formula evaluated directly on each input word, and (iii) coefficient counting from binary edge patterns and an independently implemented two-state transfer. For alphabets of sizes \(2,3,4,5,7\), complete output-size histograms agree at every length in the respective ranges \(2\)–\(12\), \(2\)–\(8\), \(2\)–\(7\), \(2\)–\(6\), and \(2\)–\(5\). The checker also compares the exact first and second moments with the closed formulas for five alphabet sizes and all lengths \(2\)–\(13\). For example, the complete distribution at \(q=3,n=5\), listed as \((\text{ball size},\text{number of sources})\), is \((1,3),(2,12),(3,24),(4,30),(5,42),(6,48),(7,42),(8,18),(9,18),(10,6)\), summing to \(243\). These finite checks corroborate, but do not replace, the all-parameter proof above.

## Relationship to prior work
Pham, Goyal, and Kiah (2021) establish asymptotic bounds for maximal **intersections** of deletion balls, while defining deletion spheres and the extremal single-center volume. Their results do not give a distribution of individual ball volumes under random centers. Swart and Ferreira (2003) give a run-based binary double-deletion count; the present identity extends the structural count to arbitrary alphabets by exposing return triples, and then counts all profiles by a two-state transfer. The published 2026 result “Exact variance of binary two-deletion sphere size” gives the binary variance \((n-1)(n-2)(2n-3)/32\); this is exactly the special case \(q=2\) of our variance formula, **not a new binary variance claim**. That result states no nonbinary or full-distribution conclusion. The nonbinary exact joint transfer law, distribution and Gaussian coefficient are the contributions here.

## Limitations
The source is uniformly distributed and independent across positions. The asymptotic limit assumes fixed alphabet size. Exact transfer enumerations can have large integer coefficients; the two-by-two matrix is a finite symbolic procedure, not a claim of constant-bit-complexity evaluation. The connection between the result and tighter code-rate bounds is motivation, not a proved code-improvement theorem. Literature searches cannot rule out an unindexed equivalent nonbinary enumeration or a specialized generating-function formulation in older string-combinatorics work.

## References
1. V. L. P. Pham, K. Goyal, H. M. Kiah, “Sequence Reconstruction Problem for Deletion Channels: A Complete Asymptotic Solution,” arXiv:2111.04255 (first posted 2021-11-08), https://arxiv.org/abs/2111.04255.
2. T. G. Swart and H. C. Ferreira, “A note on double insertion/deletion correcting codes,” *IEEE Transactions on Information Theory* 49(1), 269–273 (2003), DOI:10.1109/TIT.2002.806155.
3. “Exact variance of binary two-deletion sphere size,” public mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-variance-of-binary-two-deletion-sphere-size--6c9fe70986cc.
4. X. Wang, H. Li, F.-W. Fu, “On Sequence Reconstruction Problem for q-ary Deletion Channels,” arXiv:2609.16837 (2026), https://arxiv.org/abs/2609.16837 (studies pairwise intersections, not random single-center ball volumes).
