# Sharp arithmetic independence threshold for two binary burst-deletion ball sizes

## Finding

Let \(1\le b<c<n\) be integers, and choose a word \(X=X_0\cdots X_{n-1}\) uniformly from \(\{0,1\}^n\). Let \(D_k(X)\) be the **number of distinct** length-\(n-k\) words obtained by deleting one contiguous block of exactly \(k\) letters from \(X\), for \(k=b,c\). Put \(g=\gcd(b,c)\), \(S_k=D_k-1\), and define
\[
H(t)=\frac{1+t}{2},\qquad K(t)=\frac{1-t}{2}.
\]
Then each \(S_k\) is binomial with parameters \(n-k\) and \(1/2\); the two variables have zero covariance for every admissible \(n,b,c\); and the following exact independence threshold holds:
\[
\boxed{S_b\ \text{and}\ S_c\ \text{are independent if and only if}\ n\le b+c-g.}
\]
At the *first dependent length* \(n_0=b+c-g+1\), their joint probability generating function is exactly
\[
\boxed{\begin{aligned}
\mathbb E[z^{S_b}u^{S_c}]={}&H(z)^{n_0-b}H(u)^{n_0-c}\\
&+K(z)^{c/g}K(u)^{b/g}
  H(z)^{n_0-b-c/g}H(u)^{n_0-c-b/g}.
\end{aligned}}
\]
All exponents displayed here are nonnegative integers. In particular, the first departure from independent binomial counts is a positive cycle correction to the joint generating function for \(0<z,u<1\), despite the exact zero covariance.

## Assumptions and scope

The input bits are independent and fair; **two distinct fixed burst lengths** are observed for the same word. Exactly one contiguous block is removed for each observation, and all possible burst positions are permitted. The statistic counts distinct outputs, not deletion positions, not outputs after arbitrary two-symbol deletions, and not the size of a union of balls of different lengths. Only the binary uniform-input model is asserted. The indexing is zero-based throughout.

For a deterministic word \(x\), write \(x^{[i,k]}=x_0\cdots x_{i-1}x_{i+k}\cdots x_{n-1}\), the output when the block beginning at \(i\) of length \(k\) is removed, for \(0\le i\le n-k\). Two observations with lengths \(b\) and \(c\) produce outputs of different lengths; independence concerns the *numbers* of distinct outputs, not collisions between the output sets.

## Proof

**1. A deterministic burst-deletion identity.** For \(0\le i<j\le n-k\), comparing the deletion outputs coordinate by coordinate gives
\[
x^{[i,k]}=x^{[j,k]}\quad\Longleftrightarrow\quad
x_t=x_{t+k}\ \text{for every integer}\ i\le t<j.
\]
Thus two deletion positions produce the same output precisely when every intervening pair of shifted letters agrees. Equality classes are consecutive intervals of deletion positions, and a new output appears on advancing from position \(i\) to \(i+1\) exactly when \(x_i\ne x_{i+k}\). Therefore, with **no probabilistic assumption**,
\[
D_k(x)=1+\sum_{i=0}^{n-k-1}\mathbf1_{\{x_i\ne x_{i+k}\}}.\tag{1}
\]
This standard fixed-burst ball formula is included for completeness and is not claimed as new.

**2. Edge spins, binomial marginals, and the exact joint generating function.** Set \(\sigma_i=(-1)^{X_i}\). The \(\sigma_i\) are independent unbiased signs, and (1) becomes
\[
S_k=\frac12\sum_{i=0}^{n-k-1}(1-\sigma_i\sigma_{i+k}).\tag{2}
\]
Let \(G_n(b,c)\) be the simple undirected graph on vertices \(0,\ldots,n-1\) with \(b\)-edges \(\{i,i+b\}\), \(0\le i<n-b\), and \(c\)-edges \(\{j,j+c\}\), \(0\le j<n-c\). For each edge \(e=\{v,w\}\) set \(Y_e=\sigma_v\sigma_w\). An edge subset \(F\) has a nonzero spin-product expectation precisely if every vertex has even degree in \(F\); then the expectation is \(1\). Since \(t^{(1-Y_e)/2}=H(t)+K(t)Y_e\), expanding over all edge subsets gives the exact finite-length identity
\[
\begin{aligned}
\mathbb E[z^{S_b}u^{S_c}]={}&H(z)^{n-b}H(u)^{n-c}\\
&\times\sum_{\substack{F\subseteq E(G_n(b,c))\\\deg_F(v)\equiv0\ (\mathrm{mod}\ 2)\ \forall v}}
\left(\frac{K(z)}{H(z)}\right)^{|F\cap E_b|}
\left(\frac{K(u)}{H(u)}\right)^{|F\cap E_c|}.
\end{aligned}\tag{3}
\]
The fraction expression is used for \(0<z,u<1\); multiplying out extends it as a polynomial identity everywhere.

For one lag \(k\), edges \(\{i,i+k\}\) form \(k\) disjoint paths, hence a forest. Their edge products \(Y_e\) are jointly independent fair signs: every sign assignment on the edges of a forest is achieved by an equal number of vertex-spin assignments (one free root spin per component). Equation (2) therefore yields \(S_k\sim\mathrm{Binomial}(n-k,1/2)\).

For two distinct edges \(e\ne f\) in the simple graph \(G_n(b,c)\), the product \(Y_eY_f\) has expectation zero because the graph with those two edges has vertices of odd degree. Thus distinct edge signs are pairwise independent, even if they meet at one vertex. It follows from (2) that \(\operatorname{Cov}(S_b,S_c)=0\), for every admissible triple.

**3. The first cycle of the two-lag graph.** Let \(L=b+c\). Consider the graph \(G_L(b,c)\), and the permutation of its vertices obtained by adding \(b\) modulo \(L\). For \(v<c\), the step joins \(v\) to \(v+b\) by a \(b\)-edge; for \(v\ge c\), the step joins \(v\) to \(v-c\) by a \(c\)-edge. This permutation traces every edge exactly once and decomposes \(G_L(b,c)\) into \(g=\gcd(b,c)\) disjoint simple cycles, one in each residue class modulo \(g\). Each cycle has \(L/g\) vertices, \(c/g\) edges of length \(b\), and \(b/g\) edges of length \(c\).

Whenever \(n\le L\), the graph \(G_n(b,c)\) is the subgraph induced on vertices \(0,\ldots,n-1\) by \(G_L(b,c)\). The cycle in residue class \(r\), for \(0\le r<g\), contains the vertex \(r+L-g\); consequently no class has all vertices present unless \(n\ge L-g+1\). Thus \(G_n(b,c)\) is a forest for \(n\le L-g\). At \(n_0=L-g+1\), the class \(r=0\) is complete and every class \(r>0\) is incomplete, so \(G_{n_0}(b,c)\) contains exactly one cycle. For all larger \(n\), that cycle persists in \(G_n(b,c)\).

If \(n\le L-g\), the two labeled families of edge signs are **jointly** independent because the entire graph is a forest. Therefore their sums \(S_b,S_c\) are independent. If \(n\ge n_0\), the sum in (3) contains the empty subset and also at least the full first cycle. At any \(0<z,u<1\), all its terms are nonnegative and the cycle term is strictly positive. Hence the joint generating function is strictly greater than \(H(z)^{n-b}H(u)^{n-c}\), the product of its binomial marginals. Independence fails. This proves the if-and-only-if cutoff.

At \(n=n_0\), the **only** even-degree edge subsets are the empty set and the unique complete cycle. Its \(c/g\) edges of type \(b\) and \(b/g\) of type \(c\) give exactly the displayed two-term joint generating function. This proves every assertion.

## Verification

`verify.py` independently constructs deletion descendants as sets of strings by slicing. It exhaustively enumerates all binary input words for every \(3\le n\le11\) and every \(1\le b<c<n\), covering \(165\) parameter triples. It checks (1) word by word, all exact binomial marginal tables, the independent/dependent dichotomy including zero-probability joint cells, and all coefficients of the critical joint generating function. Run from the directory containing this document with `python3 verify.py` and expect a line beginning `VERIFIED 165`. The script uses only the Python standard library. Exhaustion through length \(11\) is corroboration; the proof above, not finite extrapolation, covers all lengths.

## Relationship to prior work

Mercer (2006) established that for a **single fixed lag** the random aperiodic autocorrelation summands are independent (Proposition 1.1) and derived their marginal moments. Because \(S_k\) is an affine transform of that autocorrelation, this fully covers our single-lag binomial marginal and is cited explicitly. The proof of Mercer’s proposition treats one lag at a time, not the independence threshold for **two distinct lag-sums**.

Levenshtein's fixed-burst deletion-ball counting identity, restated in Schoeny–Wachter-Zeh–Gabrys–Yaakobi (2016, equation (2)), and Xi–Sun–Ge (2025, Lemma 2.3), fully covers the deterministic formula (1). These works study burst-code bounds, fixed-burst ball sizes, and fixed-length burst Levenshtein balls; their inspected statements do not give the exact arithmetic two-burst-width independence threshold or the first dependent joint law. A separate published analysis of **unrestricted two-deletion** sphere-size variance uses a different channel and is not stronger coverage of two different contiguous burst widths. A published fixed-composition transition-covariance calculation uses a conditional non-iid source and concerns individual local indicators, rather than two aggregates of iid lag comparisons.

The distinguishing contribution is the **gcd-controlled first cycle in a two-lag comparison graph**, providing an all-length joint-independence criterion, not a rederivation of the standard single-lag size formula. General even-subgraph generating-function expansions are classical; the precise two-lag extremal cycle and its binary burst-deletion interpretation are the scope evaluated here.

## Limitations

No claims are made for biased or fixed-composition sources, nonbinary alphabets, three or more simultaneous burst widths, or bursts with arbitrary nonconsecutive deletions. Pairwise uncorrelatedness does not imply mutual independence; the theorem identifies the exact failure of the latter for this specific model. Searches and primary-text inspections cannot rule out an uncatalogued equivalent result phrased solely in autocorrelation, graph-cycle, or statistical-mechanics language. Independent external validation has not been performed.

## References

1. I. D. Mercer, “Autocorrelations of Random Binary Sequences,” *Combinatorics, Probability and Computing* 15 (2006), 663–671. DOI: 10.1017/S0963548306007589. First online 31 July 2006. Proposition 1.1.
2. C. Schoeny, A. Wachter-Zeh, R. Gabrys, and E. Yaakobi, “Codes Correcting a Burst of Deletions or Insertions,” arXiv:1602.06820v1 (22 February 2016), equation (2).
3. H. Xi, Y. Sun, and G. Ge, “On the Fixed-Length-Burst Levenshtein Ball with Unit Radius,” arXiv:2506.07817v1 (2025), Lemma 2.3.
4. Y. Liron and M. Langberg, “A Characterization of the Number of Subsequences Obtained via the Deletion Channel,” arXiv:1202.1644 (2012). Distinguishes arbitrary deletions from contiguous bursts.
