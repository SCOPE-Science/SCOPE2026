# Exact negative Zagreb–Wiener covariance in uniform Cayley trees

## Finding
For every integer \(n\ge2\), choose a tree \(T\) uniformly from the \(n^{n-2}\) trees with labeled vertex set \([n]\). Define its first Zagreb index and Wiener index by
\[
Z(T)=\sum_{v=1}^{n}\deg_T(v)^2,\qquad
W(T)=\sum_{1\le u<v\le n}d_T(u,v).
\]
For falling factorials \((a)_0=1\), \((a)_r=a(a-1)\cdots(a-r+1)\), set
\[
h_n=\sum_{k=1}^{n-1}\frac{(n-2)_{k-1}}{n^k}.
\]
Then
\[
\boxed{\operatorname{Cov}(Z(T),W(T))
=\binom n2[4-(n+6)h_n]
=2n(n-1)-\frac{n+6}{n}\mathbb EW(T).}
\]
The covariance vanishes exactly at \(n=2,3\), is strictly negative for every \(n\ge4\), and obeys
\[
\operatorname{Cov}(Z(T),W(T))\sim-\sqrt{\pi/8}\,n^{5/2},\qquad
\frac{\operatorname{Cov}(Z(T),W(T))}{\mathbb E W(T)}\longrightarrow-1.
\]
A distance-conditioned identity underlying this result is
\[
\boxed{\mathbb E[Z(T)\mid d_T(u,v)=k]
=5n-11+\frac6n+\frac{(k-1)(2n-k(k+1))}{n(k+1)}}
\]
for all distinct fixed \(u,v\in[n]\) and all \(1\le k\le n-1\).

## Assumptions and scope
The distribution is uniform over all *labeled unrooted* trees on \([n]\); it is not the increasing/random-recursive tree law, an unlabelled-tree law, or a preferential-attachment law. The distance sum counts each unordered vertex pair exactly once. Falling-factorial factors with zero length equal one. The case \(n=2\) is included, and conditioning on maximal distance \(k=n-1\) is understood separately below.

## Proof
**Step 1: marked-path enumeration.** Fix distinct labels \(u,v\) and let \(K=d_T(u,v)\). A path with \(k\) edges and prescribed endpoints has \((n-2)_{k-1}\) ordered choices of its interior vertices. Contract this fixed path (containing \(s=k+1\) vertices) and keep the other \(n-s\) vertices separate. The weighted Cayley forest-extension formula asserts that a forest with component sizes \(s_1,\ldots,s_c\) is contained in exactly \(n^{c-2}\prod_{i=1}^c s_i\) labeled trees. Indeed, a tree on the contracted components with edges \(ij\) lifts in \(s_i s_j\) ways, and the weighted Prüfer enumeration of these component-trees is \((\sum_i s_i)^{c-2}\prod_i s_i\). Thus, for a specified path, the number of completions is \((k+1)n^{n-k-2}\). Dividing by the Cayley total yields
\[
\Pr(K=k)=\frac{(k+1)(n-2)_{k-1}}{n^k},\quad 1\le k\le n-1.
\]
When \(k=n-1\) the prescribed path spans every vertex and has exactly one completion, consistent with this expression.

**Step 2: square-degree regression under the marked path.** Put \(s=k+1\), \(c=n-k\), and assume initially \(c\ge2\); write \(r=c-2=n-k-2\). The forced degrees on the path sum to \(2k\), and their squares sum to \(4k-2\). In the contracted tree, the special vertex of weight \(s\) has degree
\[
B=1+\operatorname{Bin}(r,s/n),
\qquad \mathbb EB=1+rs/n,
\qquad\mathbb E[B(B-1)]=2rs/n+r(r-1)s^2/n^2.
\]
This follows from the weighted Prüfer word: the \(c-2\) letters are independent, with probability \(s/n\) of being the contracted path-vertex and \(1/n\) of being each other vertex. Each of the \(B\) external edges is attached uniformly and independently to one of the \(s\) path vertices. If \(L_i\) denotes their attachment counts and \(f_i\) the forced path degree, the conditional expected path contribution to \(Z\) is
\[
4k-2+\Bigl(1+\frac{4k}{s}\Bigr)\mathbb EB+
\frac{\mathbb E[B(B-1)]}{s}.
\]
Indeed, \(\sum_i f_i^2=4k-2\), \(\mathbb E\sum_i 2f_iL_i=(4k/s)\mathbb EB\), and \(\mathbb E\sum_i L_i^2=\mathbb EB+\mathbb E[B(B-1)]/s\). Each of the other \(c-1\) vertices has degree \(1+\operatorname{Bin}(r,1/n)\) marginally, so their combined expected squared-degree contribution is
\[
(c-1)\Bigl(1+\frac{3r}{n}+\frac{r(r-1)}{n^2}\Bigr).
\]
Adding these contributions and simplifying gives the boxed conditional regression. For \(c=1\), the tree is the prescribed Hamiltonian path and \(Z=4n-6\), which is exactly the regression formula at \(k=n-1\). Independently, in the ordinary Prüfer coding a fixed vertex has degree \(1+\operatorname{Bin}(n-2,1/n)\), hence
\[
\mathbb EZ=5n-11+6/n.
\]

**Step 3: exact mixed covariance.** Write \(t_k=(n-2)_{k-1}/n^k\) and \(S_j=\sum_{k=1}^{n-1}k^j t_k\). The recurrence \(nt_{k+1}=(n-1-k)t_k\), with \(t_1=1/n\), \(t_n=0\), gives, by summing polynomial multiples and telescoping,
\[
S_1=1-h_n,\qquad S_2=(n+1)h_n-1,\qquad
S_4=(3n^2+11n+1)h_n-(8n+1).
\]
In particular,
\[
\mathbb EK=\sum_{k=1}^{n-1}k(k+1)t_k=S_2+S_1=nh_n.
\]
By conditioning on \(K\) and subtracting \(\mathbb EZ\),
\[
\begin{aligned}
\operatorname{Cov}(Z,K)
&=\sum_{k=1}^{n-1}(k+1)t_k\,k\,
  \frac{(k-1)(2n-k(k+1))}{n(k+1)}\\
&=\frac{-S_4+(2n+1)S_2-2nS_1}{n}\\
&=4-(n+6)h_n.
\end{aligned}
\]
Since \(W=\sum_{u<v}d_T(u,v)\), symmetry and linearity multiply this pairwise covariance by \(\binom n2\). The mean relationship \(\mathbb EW=\binom n2nh_n\) yields the alternative exact expression in the finding.

**Step 4: strict sign and asymptotic.** At \(n=2\) or \(n=3\), the Zagreb index is constant, so the covariance is zero. For every \(n\ge4\), the first four nonnegative terms of \(h_n\) satisfy
\[
(n+6)\sum_{k=1}^{4}t_k-4
=\frac{8(n-3)^2(n-2)}{n^4}>0.
\]
Therefore \(4-(n+6)h_n<0\). Finally the established Cayley-tree Wiener mean asymptotic \(\mathbb EW\sim\sqrt{\pi/8}\,n^{5/2}\), together with the exact covariance identity, yields the two stated limits.

## Verification
The accompanying standalone `verify.py` independently generates every Prüfer sequence for \(2\le n\le8\), reconstructs tree degrees and distance sums, and checks the exact identity from direct mixed moments. It additionally checks the complete distance-conditioned regression for each admissible distance. It verifies \(280{,}392\) labeled tree instances, \(28\) aggregate equalities/sign checks and \(56\) conditional probability/regression equalities using rational arithmetic. The script is finite corroboration; Step 1–4 establish the all-size theorem.

## Relationship to prior work
Janson (2003) establishes the distributional and moment asymptotics of the Wiener index for simply generated trees, including uniform labeled Cayley trees. The whole inspected article studies Wiener, path length, and their mixed moments, not the mixed first-Zagreb/Wiener covariance. Wagner (2014) studies additive small-toll functionals of random trees under primary MSC 60C05; such marginal limit theorems do not supply the displayed exact cross-moment with the nonlocal Wiener statistic. Feng and Hu (2011) study Zagreb moments in the *random recursive* tree model, a distinct distribution. Hollas (2005) studies randomly assigned vertex marks on trees rather than deterministic Zagreb and Wiener indices. The present finite conditional regression and covariance are not determined by those statements. Literature under alternative graph-index names or an unindexed joint enumerator remains an originality risk.

## Limitations
This is an exact first mixed moment, not the full joint distribution. The asymptotic uses an established first-moment theorem for the Wiener index, whereas the finite covariance and strict sign follow from the proof given here. Exact rational enumeration only covers \(n\le8\), not all \(n\). No independent external audit has been conducted. The absence of an equivalent identity in the inspected and searched sources is not a proof of absolute priority.

## References
1. S. Janson, *The Wiener Index of Simply Generated Random Trees*, Random Structures & Algorithms 22 (2003), 337–358. DOI: https://doi.org/10.1002/rsa.10074. First online 2003-03-03.
2. S. Wagner, *Central Limit Theorems for Additive Tree Parameters with Small Toll Functions*, Combinatorics, Probability and Computing 24 (2015), 329–353. DOI: https://doi.org/10.1017/S0963548314000443. First online 2014-09-08; primary MSC 60C05.
3. Q. Feng and Z. Hu, *On the Zagreb Index of Random Recursive Trees*, Journal of Applied Probability 48 (2011), 1189–1196. DOI: https://doi.org/10.1239/jap/1324046027.
4. B. Hollas, *Asymptotically Independent Topological Indices on Random Trees*, Journal of Mathematical Chemistry 38 (2005), 379–387. DOI: https://doi.org/10.1007/s10910-005-6474-5.
5. S. G. Wagner, *Correlation of Graph-Theoretical Indices*, SIAM Journal on Discrete Mathematics 21 (2007), 33–46. DOI: https://doi.org/10.1137/050631446.
6. A. Q. M. Al-Saedi, R. I. Nabiyyi and M. Javanian, *Limit Law for Zagreb and Wiener Indices of Random Exponential Recursive Trees*, International Journal of Foundations of Computer Science (2024), DOI: https://doi.org/10.1142/S0129054124500060 (different random-tree model).
