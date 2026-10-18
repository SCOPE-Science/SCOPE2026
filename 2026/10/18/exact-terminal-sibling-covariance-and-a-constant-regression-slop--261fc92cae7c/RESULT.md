# Exact terminal-sibling covariance and a constant regression slope in random recursive trees

## Finding
For every integer \(n\ge4\), a uniformly random recursive tree has an exact positive covariance between its number of terminal vertices and its number of unordered pairs of terminal siblings:
\[
\boxed{\operatorname{Cov}(L_n,C_n)=\frac n8.}
\]
In the same range,
\[
\mathbb E L_n=\frac n2,\qquad \operatorname{Var}(L_n)=\frac n{12},\qquad
\mathbb E C_n=\frac n6,\qquad
\mathbb E[L_nC_n]=\frac{n^2}{12}+\frac n8.
\]
Thus the least-squares linear regression coefficient of \(C_n\) on \(L_n\) is exactly
\[
\frac{\operatorname{Cov}(L_n,C_n)}{\operatorname{Var}(L_n)}=\frac32
\]
for **every** \(n\ge4\), not merely in the large-tree limit. The exceptional boundary values are \(\operatorname{Cov}(L_2,C_2)=0\) and \(\operatorname{Cov}(L_3,C_3)=1/4\).

A birth-order-resolved companion identity gives, for \(2\le i<j\le n\) and \(n\ge3\),
\[
\boxed{\Pr\{i,j\text{ are terminal siblings}\}
=\frac{i-1}{(n-1)(n-2)}.}
\]
The probability is independent of the *younger* child's birth position once the older birth position is fixed.

## Assumptions and scope
Begin with the root vertex labeled \(1\). For every \(t=2,3,\ldots,n\), vertex \(t\) chooses a parent \(P_t\) independently and uniformly from \(\{1,\ldots,t-1\}\). All \((n-1)!\) parent-choice vectors are equiprobable. Edges are oriented away from the root.

A **terminal vertex** is a vertex with no children (outdegree zero); write \(L_n\) for the number of terminal vertices. This convention **does not** count the root as a leaf when its undirected graph degree is one. It is consequently different from the unrooted degree-one convention sometimes used for growing trees.

For every vertex \(v\), let \(\ell_v\) be the number of its children that are terminal vertices. Define
\[
C_n=\sum_{v=1}^{n}\binom{\ell_v}{2}.
\]
Each unordered pair of terminal siblings is counted once. A parent with three terminal children contributes three pairs, not one; no binary-branching assumption is imposed. All probabilities and expectations refer to this exact random-tree law.

## Proof
**1. Changes from one uniform attachment.** Fix the complete rooted tree on \(n\) vertices and let \(V\) be the parent selected uniformly for vertex \(n+1\). For each existing nonroot vertex \(v\), write \(I_v=1\) when it is terminal and \(0\) otherwise; the root has \(I_1=0\) for \(n\ge2\). The new vertex is terminal. Therefore
\[
\Delta L:=L_{n+1}-L_n=1-I_V.
\]
If \(V\) is not terminal, adding one terminal child creates \(\ell_V\) new sibling pairs. If \(V\) was terminal, its parent loses that terminal child; precisely \(\ell_{P_V}-1\) sibling pairs disappear, while \(V\)'s newly acquired terminal child creates no pair. Consequently
\[
\Delta C:=C_{n+1}-C_n
=\ell_V-I_V(\ell_{P_V}-1),
\]
where the second term is interpreted as zero when \(V=1\) (which cannot be terminal for \(n\ge2\)).

Every terminal vertex is a child of exactly one vertex, so
\[
\sum_v\ell_v=L_n,\qquad
\sum_{v:I_v=1}(\ell_{P_v}-1)=\sum_u\ell_u(\ell_u-1)=2C_n.
\]
Since \(\ell_v=0\) when \(v\) itself is terminal, the conditional one-step moments are
\[
\begin{aligned}
\mathbb E[\Delta L\mid T_n]&=1-\frac{L_n}{n},\\
\mathbb E[\Delta C\mid T_n]&=\frac{L_n-2C_n}{n},\\
\mathbb E[\Delta L\,\Delta C\mid T_n]&=\frac{L_n}{n}.
\end{aligned}
\]
The third equality is particularly useful: only attachments to nonterminal vertices contribute to the product of increments, and their terminal-child counts sum to \(L_n\).

**2. Closed unconditional moment recurrences.** Put \(m_n=\mathbb E L_n\), \(q_n=\mathbb E L_n^2\), \(c_n=\mathbb E C_n\), and \(t_n=\mathbb E[L_nC_n]\). Expanding the conditional moments gives, for all \(n\ge2\),
\[
\begin{aligned}
m_{n+1}&=(1-1/n)m_n+1,\\
q_{n+1}&=(1-2/n)q_n+(2-1/n)m_n+1,\\
c_{n+1}&=(1-2/n)c_n+m_n/n,\\
t_{n+1}&=(1-3/n)t_n+c_n+(q_n+m_n)/n.
\end{aligned}
\]
These are exact equalities, not asymptotic approximations. For the initial two-vertex rooted edge, \(L_2=1\) and \(C_2=0\), so \(m_2=q_2=1\) and \(c_2=t_2=0\).

The first two recurrences imply by induction that
\[
m_n=\frac n2\quad(n\ge2),\qquad
q_n=\frac{n^2}{4}+\frac n{12}\quad(n\ge3),
\]
where the \(n=3\) second-moment base is \(q_3=5/2\). The third recurrence yields \(c_n=n/6\) for all \(n\ge3\), with base \(c_3=1/2\).

At three vertices, the attachment of vertex \(3\) to vertex \(1\) or \(2\) has probability \(1/2\) each; the outcomes have \((L_3,C_3)=(2,1)\) and \((1,0)\), respectively. Thus \(t_3=1\). Substituting into the last recurrence at \(n=3\) gives \(t_4=11/6\). With the displayed formulas for \(m_n,q_n,c_n\), the last recurrence becomes
\[
t_{n+1}=\left(1-\frac3n\right)t_n+\frac{5n+7}{12}
\qquad(n\ge3).
\]
The initial value at \(n=4\), followed by induction, gives
\[
t_n=\frac{n^2}{12}+\frac n8\qquad(n\ge4).
\]
Consequently
\[
\operatorname{Cov}(L_n,C_n)=t_n-m_nc_n
=\left(\frac{n^2}{12}+\frac n8\right)-\frac n2\frac n6
=\frac n8\qquad(n\ge4).
\]
Similarly \(\operatorname{Var}(L_n)=q_n-m_n^2=n/12\) for \(n\ge3\), proving the stated constant regression coefficient.

**3. Resolving the contribution of an individual sibling pair.** Fix \(2\le i<j\le n\). The event that \(i\) and \(j\) have the same parent has probability \(1/(j-1)\), because after the parent of \(i\) has been selected, the uniform parent choice of \(j\) matches it with that probability. For \(i\) to remain terminal until \(j\) arrives, none of the vertices with indices between them may attach to \(i\), with probability
\[
\prod_{t=i+1}^{j-1}\frac{t-2}{t-1}=\frac{i-1}{j-2}.
\]
After \(j\) arrives, both siblings remain terminal exactly when no later vertex attaches to either one, an independent event of probability
\[
\prod_{t=j+1}^{n}\frac{t-3}{t-1}
=\frac{(j-1)(j-2)}{(n-1)(n-2)}.
\]
Empty products are interpreted as one. Multiplication yields the claimed probability \((i-1)/((n-1)(n-2))\). Summing over all sibling pairs independently verifies
\[
\mathbb E C_n=
\frac{\sum_{i=2}^{n-1}(n-i)(i-1)}{(n-1)(n-2)}=\frac n6
\qquad(n\ge3).
\]

## Verification
A dependency-free Python verifier (`verify.py`) independently enumerates all \((n-1)!\) parent-choice vectors for each \(2\le n\le8\), computes the two statistics from explicit parent arrays, and checks each pair-event probability exactly using rational arithmetic. It also evaluates the four one-step moment recurrences using `fractions.Fraction` through \(n=150\). It passed **6,596 exact rational assertions** in the packaged replay. The analytic induction and elementary products, not finite enumeration, establish the statements for unrestricted \(n\).

## Relationship to prior work
Bryc, Minda, and Sethuraman's 2008 preprint studies a one-dimensional leaf-count Markov chain in uniformly random recursive trees and, separately, cherry counts in the **Yule splitting model**. Section 1.2.2 describes the uniform recursive attachment model; Section 1.2.3 defines the different Yule cherry process. Neither displayed one-dimensional result supplies the joint covariance of terminal count and sibling-pair count within the uniform recursive attachment model.

Janson's 2004 published treatment gives asymptotic laws and covariances for counts of vertices **classified by their own outdegree** in recursive trees. Those marginal degree-count statistics do not by themselves determine the terminal-children adjacency statistic \(C_n\), whose value depends on how terminal vertices are grouped under parents. Its original full text could not be fetched in this review, and an earlier implicit derivation remains possible.

Hartle and Krapivsky's later 2025 paper studies mean leaf-neighbor profiles and the separate marginal distribution of total degree-one leaves in growing recursive trees. Its undirected-degree-one convention can include a degree-one root and is not interchangeable with the rooted outdegree-zero convention adopted here. The reviewed sections do not state the exact finite-size mixed moment derived above.

## Limitations
The theorem concerns only **uniform recursive attachment** with independently and uniformly sampled older parents; it does not apply unchanged to uniformly labeled Cayley trees, preferential attachment, plane-oriented recursive trees, or Yule–Harding binary trees. The result is an identity about covariance and least-squares slope, not a claim of stochastic monotonicity or a full joint distribution. The root/terminal convention and the all-pairs counting of terminal siblings are essential. Independent historical-priority confirmation remains necessary, especially because some earlier general increasing-tree enumerators may contain an implicit equivalent formula.

## References
1. S. Janson, *Asymptotic degree distribution in random recursive trees*, Random Structures & Algorithms **26** (2005), 69–83, first online 2004-11-16, DOI: 10.1002/rsa.20046. Author-hosted preprint: https://www2.math.uu.se/~svantejs/papers/sj155.pdf .
2. W. Bryc, D. Minda, S. Sethuraman, *Large deviations for the leaves in some random trees*, arXiv:0809.4741v1, publicly submitted 2008-09-27; Advances in Applied Probability **41** (2009), 845–873. https://arxiv.org/abs/0809.4741 .
3. H. Hartle, P. L. Krapivsky, *Statistics of leaves in growing random trees*, arXiv:2511.04085v1, 2025-11-06. https://arxiv.org/abs/2511.04085 .
