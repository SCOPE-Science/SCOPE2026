# Bidiagonal record–descent dependence in Mallows permutations

## Finding
For an inversion-weighted Mallows permutation, the full covariance matrix between upper-record indicators and adjacent-descent indicators is exactly bidiagonal. Its nonzero entries have opposite signs, and their row sums are negative for every parameter. Specifically, for \(q>0\), let \([m]_q=1+q+\cdots+q^{m-1}\). Then for every \(n\ge2\), \(1\le i\le n-1\), and \(1\le j\le n\),
\[
\operatorname{Cov}(R_j,D_i)=
\begin{cases}
\dfrac{[i+1]_q-1-q}{(1+q)[i]_q[i+1]_q},& j=i,\\[4pt]
-\dfrac{q}{(1+q)[i+1]_q},&j=i+1,\\[4pt]
0,& \text{otherwise}.
\end{cases}
\]
For \(i\ge2\), the \(j=i\) entry is positive, and every \(j=i+1\) entry is negative. The exceptional first diagonal entry \(\operatorname{Cov}(R_1,D_1)\) is zero because \(R_1=1\). Consequently,
\[
\operatorname{Cov}(K_n,T_n)=-\frac{q}{1+q}\sum_{i=1}^{n-1}\frac{1}{[i]_q[i+1]_q}<0,
\]
where \(K_n=\sum_j R_j\) counts upper records and \(T_n=\sum_iD_i\) counts descents. At the uniform point \(q=1\), \(\operatorname{Cov}(K_n,T_n)=-(n-1)/(2n)\).

## Assumptions and scope
Let \(S_n\) be the permutations of \(\{1,\ldots,n\}\) in one-line notation. For \(q>0\), the Mallows law is
\[
\mathbb P(\Pi=\pi)=\frac{q^{\operatorname{inv}(\pi)}}{[n]_q!},\quad
[n]_q!:=\prod_{t=1}^n[t]_q,\quad
\operatorname{inv}(\pi)=\#\{(a,b):a<b,\ \pi_a>\pi_b\}.
\]
Set \(R_1=1\) and for \(2\le j\le n\), \(R_j=\mathbf1\{\Pi_j>\max_{1\le t<j}\Pi_t\}\). Set \(D_i=\mathbf1\{\Pi_i>\Pi_{i+1}\}\) for \(1\le i<n\). The assertions hold for every finite \(n\ge2\) and every fixed real \(q>0\), including \(q=1\) and \(q>1\). No assertion is made at the excluded parameter \(q=0\) or for non-Mallows rank models.

## Proof
For each \(1\le t\le n\), let \(U_t\) be the rank of \(\Pi_t\) among \(\Pi_1,\ldots,\Pi_t\), with rank one for the smallest. The map from a permutation to its insertion ranks \((U_1,\ldots,U_n)\) is bijective and
\[
\operatorname{inv}(\Pi)=\sum_{t=1}^{n}(t-U_t).
\]
Indeed, when entry \(\Pi_t\) is inserted into its prefix, exactly \(t-U_t\) preceding values exceed it, accounting for all inversions whose right endpoint is \(t\). The Mallows normalization factors, so the \(U_t\) are independent and
\[
\mathbb P(U_t=r)=\frac{q^{t-r}}{[t]_q}\quad(1\le r\le t).
\]
In particular \(R_t=\mathbf1\{U_t=t\}\), \(\mathbb P(R_t=1)=1/[t]_q\), and \(D_i=\mathbf1\{U_{i+1}\le U_i\}\): the new entry at step \(i+1\) is below the preceding entry exactly when its insertion rank does not exceed that entry's previous prefix rank.

The marginal descent probability is \(\mathbb P(D_i=1)=q/(1+q)\): swapping the entries at adjacent positions changes the inversion count by exactly one, and pairs the descent and ascent configurations with relative weights \(q:1\). If \(j\notin\{i,i+1\}\), then \(R_j\) depends only on \(U_j\), whereas \(D_i\) depends only on \((U_i,U_{i+1})\); hence the covariance vanishes.

When \(j=i\), conditioning on \(R_i=1\) fixes \(U_i=i\). Since \(U_{i+1}\) is independent, \(\mathbb P(D_i=1\mid R_i=1)=\mathbb P(U_{i+1}\le i)=1-1/[i+1]_q\). Therefore
\[
\operatorname{Cov}(R_i,D_i)
=\frac1{[i]_q}\left(1-\frac1{[i+1]_q}-\frac q{1+q}\right)
=\frac{[i+1]_q-1-q}{(1+q)[i]_q[i+1]_q}.
\]
For \(i=1\) this vanishes because \([2]_q=1+q\). For every \(i\ge2\), the numerator equals \(q^2+\cdots+q^i>0\).

When \(j=i+1\), the event \(R_{i+1}=1\) forces \(U_{i+1}=i+1\), hence forces \(D_i=0\). Thus
\[
\operatorname{Cov}(R_{i+1},D_i)
=-\mathbb P(R_{i+1}=1)\mathbb P(D_i=1)
=-\frac{q}{(1+q)[i+1]_q}.
\]
Finally, \([i+1]_q=[i]_q+q^i\) and \((1-q)[i]_q=1-q^i\) give the exact row-sum simplification
\[
\operatorname{Cov}(R_i,D_i)+\operatorname{Cov}(R_{i+1},D_i)
=-\frac q{(1+q)[i]_q[i+1]_q}.
\]
Summing over \(i\) and using bilinearity of covariance proves the displayed total-covariance formula and its strict negative sign. For \(q=1\), \([i]_1=i\) and the telescoping identity \(\sum_{i=1}^{n-1}1/(i(i+1))=1-1/n\) yields \(-(n-1)/(2n)\). This completes the proof.

## Verification
A standalone pure-Python exact-rational enumerator in `verify.py` checks all \((i,j)\) matrix entries and their row sums against direct weighted enumeration of every permutation for \(2\le n\le7\) and \(q\in\{1/2,1,2\}\). It additionally checks the negative total-covariance formula and the uniform simplification. Run `python3 verify.py` alongside this document; the final line is `ALL_RECORD_DESCENT_CHECKS_PASS`. These finite checks support arithmetic and indexing, while the proof above establishes all admissible finite sizes and positive real parameters.

## Relationship to prior work
The Mallows inversion-weighted law and its independent rank-insertion construction are standard. Gnedin and Olshanski develop general \(q\)-exchangeability, and Bhatnagar and Peled prove distributional properties of induced orderings of Mallows permutations; in particular, their independence lemma and the adjacent-descent marginal do not give the two-index record/descent cross-covariance matrix. Carlitz and Scoville studied global Eulerian–record-count generating polynomials; subsequent work on their inversion-weighted analogues likewise treats aggregate statistics rather than covariance localization by record and descent positions. The present exact signed bidiagonal profile and its all-\(q\) negative aggregate are more specific information than either marginal law or a global count generating function alone.

## Limitations
The statement concerns ordinary upper records and adjacent descents under the one-parameter Kendall-inversion Mallows law; other ranking biases, alternative record definitions, or dependencies beyond covariance are not classified. It does not imply negative association of all increasing functions, or statistical independence of distinct record and descent indicators from their vanishing covariance alone. The calculation is an exact identity, not a claimed central limit theorem. Prior results on general inversion-weighted permutations might allow another formulation of part of this identity; the cited comparisons do not establish an exhaustive literature uniqueness theorem.

## References
1. A. Gnedin and G. Olshanski, *\(q\)-exchangeability via quasi-invariance*, Annals of Probability 38 (2010), 2103–2135; first version arXiv:0907.3275 (2009-07-20). https://arxiv.org/abs/0907.3275
2. N. Bhatnagar and R. Peled, *Lengths of Monotone Subsequences in a Mallows Permutation*, Probability Theory and Related Fields 161 (2015), 719–780; first version arXiv:1306.3674 (2013-06-16). https://arxiv.org/abs/1306.3674
3. L. Carlitz and R. Scoville, *Generalized Eulerian numbers: combinatorial applications*, Journal für die reine und angewandte Mathematik 265 (1974), 110–137. https://eudml.org/doc/151403
4. Y. Dong, Z. Lin, and Q. Pan, *A \(q\)-analog of the Stirling-Eulerian Polynomials*, arXiv:2404.09777 (2024). https://arxiv.org/abs/2404.09777
5. A. Gnedin and V. Gorin, *Record-dependent measures on the symmetric groups*, Random Structures & Algorithms 46 (2015), 688–706, arXiv:1202.3680. https://arxiv.org/abs/1202.3680
