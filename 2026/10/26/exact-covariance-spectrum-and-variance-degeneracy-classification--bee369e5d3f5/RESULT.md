# Exact covariance spectrum and variance-degeneracy classification for fixed-composition random colorings

## Finding
For any integer \(N\ge4\), prescribe positive integer color-class sizes \(r_1,\ldots,r_b\) summing to \(N\). Assign these color multiplicities uniformly at random to \([N]\), with distinct color labels. For each unordered pair \(e=\{i,j\}\), define \(Y_e=\mathbf1\{\text{the endpoints have the same color}\}\). Let \(C\) be the covariance matrix of all \(\binom N2\) pair indicators. Put
\[
M=\binom N2,\qquad
p=\frac{\sum_a r_a(r_a-1)}{N(N-1)},\qquad
\mu=\frac1N\sum_a r_a(r_a-1),\qquad
s^2=\frac1N\sum_a r_a(r_a-1)^2-\mu^2.
\]
The complete covariance spectrum is:
\[
\begin{array}{c|c|c}
\text{invariant edge-weight subspace}&\text{multiplicity}&\text{eigenvalue}\\
\hline
\text{constant edge weights}&1&0\\
\text{centered vertex stars}&N-1&\displaystyle\lambda_{\rm star}=\frac{Ns^2}{(N-1)(N-2)}\\
\text{zero-sum weights with zero vertex degrees}&\displaystyle\frac{N(N-3)}2&\displaystyle\lambda_{\rm cyc}=\frac{(N-1)p(1-p)-2s^2/(N-2)}{N-3}.
\end{array}
\]
Here the last subspace is called the *cycle-type* edge module, without asserting that it is the usual oriented cycle space. Both nonconstant eigenvalues are nonnegative. The star eigenvalue vanishes **exactly when all \(r_a\) are equal**; the cycle-type eigenvalue vanishes **exactly when the size multiset is \(\{N\}\), \(\{1,\ldots,1\}\), or \(\{N-1,1\}\)**.

For arbitrary real weights \(w_{ij}=w_{ji}\), let \(W=\sum_{i<j}w_{ij}\), \(d_i=\sum_{j\ne i}w_{ij}\), and \(t_i=d_i-2W/N\). The exact finite-sample variance is
\[
\boxed{\displaystyle
\operatorname{Var}\left(\sum_{i<j}w_{ij}Y_{ij}\right)
=\lambda_{\rm star}\frac{\sum_i t_i^2}{N-2}
+\lambda_{\rm cyc}\left(\sum_{i<j}w_{ij}^2-\frac{W^2}{M}-\frac{\sum_i t_i^2}{N-2}\right).}
\]
In particular, for any simple graph \(H\) on \([N]\), let \(X_H\) count edges of \(H\) whose endpoints have matching colors, and let \(m=|E(H)|\), \(d_H(i)\) its degrees. Substituting \(w_{ij}=\mathbf1\{ij\in E(H)\}\) yields
\[
\operatorname{Var}(X_H)=\lambda_{\rm star}\frac{\sum_i(d_H(i)-2m/N)^2}{N-2}
+\lambda_{\rm cyc}\left(m-\frac{m^2}{M}-\frac{\sum_i(d_H(i)-2m/N)^2}{N-2}\right).
\]
This variance is **exactly zero** in precisely the following cases, including all \(N\ge4\):

1. If all vertices have one color, or every vertex has a different color, it is zero for every \(H\).
2. If the class-size multiset is \(\{N-1,1\}\), it is zero precisely for **regular** graphs \(H\).
3. If there are at least two color classes, all of the same size at least two, it is zero precisely when \(H\) is the empty graph, the complete graph, a star, or the complement of a star.
4. For every other size multiset, it is zero precisely when \(H\) is empty or complete.

All exceptional graph classes are up to relabeling; stars have \(N-1\) edges. The result is about unrestricted random color assignments with exactly prescribed color counts; it does not require proper colorings.

## Assumptions and scope
Integers \(N\ge4\), \(b\ge1\), \(r_a\ge1\), \(\sum_a r_a=N\), and \(H\) any deterministic simple graph on \([N]\). Color labels are distinct, but the equality indicators depend only on the induced partition, so equal-size color labels have no effect. The sample space of colorings has cardinality \(N!/\prod_a r_a!\). All expectations, variances, and covariances are taken over that finite uniform sample space. No asymptotic hypotheses, graph density assumptions, or independence assumptions on the color indicators are made.

The first nonconstant eigenspace consists of weights \(w_{ij}=a_i+a_j\) with \(\sum_i a_i=0\); the second consists of weights \(\sum_{j\ne i}w_{ij}=0\) for every vertex. These are orthogonal to each other and to constant weights. Their dimensions are \(N-1\) and \(N(N-3)/2\), respectively.

## Proof
**1. Deterministic pair and vertex sums.** By the fixed class sizes,
\[\sum_{i<j}Y_{ij}=\sum_{a=1}^b\binom{r_a}2\quad\text{almost surely}.\]
Thus the covariance operator annihilates constant edge weights. The row sum of the indicator vector at vertex \(i\) is
\[R_i=\sum_{j\ne i}Y_{ij}=r_{c(i)}-1,\]
where \(c(i)\) denotes its random color. Since a uniformly chosen vertex belongs to class \(a\) with probability \(r_a/N\), \(\mathbb E R_i=\mu\) and \(\operatorname{Var}(R_i)=s^2\). Also \(\sum_iR_i=\sum_a r_a(r_a-1)\) is deterministic. Exchangeability therefore gives, for distinct \(i,j\),
\[\operatorname{Cov}(R_i,R_j)=-\frac{s^2}{N-1}.\]
The nontrivial centered-vertex eigenvalue of the matrix \(\operatorname{Cov}(R)\) is consequently \(Ns^2/(N-1)\).

**2. Covariance decomposition and the star eigenvalue.** Permuting the \(N\) vertices preserves the coloring law, so \(\operatorname{Cov}(Y_e,Y_f)\) depends only on \(|e\cap f|\in\{0,1,2\}\). Its matrix belongs to the three-dimensional commutative algebra spanned by the identity, the adjacency of the line graph of \(K_N\), and the disjointness matrix. The three orthogonal invariant subspaces described above are therefore eigenspaces. Let \(B\) be the unsigned vertex-edge incidence matrix of \(K_N\). Direct counting gives
\[BB^{\mathsf T}=(N-2)I+J.\]
On centered vertex vectors its squared singular value is \(N-2\). Since \(R=BY\), the covariance eigenvalue calculated in step 1 must equal \((N-2)\lambda_{\rm star}\), giving
\[\lambda_{\rm star}=\frac{Ns^2}{(N-1)(N-2)}.\]
Each pair-indicator has mean \(p\) and variance \(p(1-p)\); thus \(\operatorname{tr}C=Mp(1-p)\). Accounting for the multiplicities \(1,N-1,N(N-3)/2\) gives
\[Mp(1-p)=(N-1)\lambda_{\rm star}+\frac{N(N-3)}2\lambda_{\rm cyc},\]
which yields the displayed \(\lambda_{\rm cyc}\). Positivity follows because \(C\) is a covariance matrix.

**3. Projection of arbitrary weights.** Orthogonal projection of the edge-weight vector \(w\) onto constants has squared norm \(W^2/M\). Its projection onto the centered-star space is the vector \(w^*_{ij}=(t_i+t_j)/(N-2)\): indeed \(\sum_i t_i=0\) and its centered vertex degree at \(i\) is \(t_i\). From \(BB^{\mathsf T}=(N-2)I+J\), the squared norm of this projection is \(\sum_it_i^2/(N-2)\). Pythagoras gives the remaining squared norm \(\sum_e w_e^2-W^2/M-\sum_i t_i^2/(N-2)\). Applying \(C\) separately on the three subspaces proves the variance identity.

**4. Classification of zero eigenvalues.** The quantity \(s^2\) is the variance of the *size-biased class size minus one*, where each color \(a\) has probability \(r_a/N>0\). It vanishes if and only if all class sizes agree. To classify \(\lambda_{\rm cyc}=0\), observe that the centered projection of each random \(0\)-\(1\) co-coloring edge vector onto the cycle-type module then has zero variance, hence is constant. In fact that constant is zero: by vertex exchangeability the expectation is the constant vector \(p\mathbf1\). Thus every co-coloring graph has an additive edge indicator \(Y_{ij}=a_i+a_j\) for some real numbers \(a_i\), with constants absorbed into the \(a_i\).

We prove the following elementary lemma. For \(N\ge4\), any \(0\)-\(1\) edge vector satisfying \(Y_{ij}=a_i+a_j\) is the incidence vector of the empty graph, the complete graph, a star, or the complement of a star. If all \(a_i\) agree, the graph is empty or complete. Otherwise choose \(a_i>a_j\); for any \(k\) distinct from \(i,j\), \(Y_{ik}-Y_{jk}=a_i-a_j>0\). Since each left-side term is binary, \(a_i-a_j=1\), \(Y_{ik}=1\), and \(Y_{jk}=0\). The remaining \(N-2\) vertex coefficients are all \(-a_j\). Their mutual edges equal \(-2a_j=t\in\{0,1\}\), and the edge \(ij\) equals \(1-t\). If \(t=0\), the graph is a star centered at \(i\); if \(t=1\), it is the complement of a star centered at \(j\). This establishes the lemma.

A co-coloring graph is **a disjoint union of complete cliques** of sizes \(r_a\); neither a star nor a complementary star is such a union except that the complement of a star is exactly \(K_{N-1}\sqcup K_1\). Therefore \(\lambda_{\rm cyc}=0\) only for the all-singleton, one-class, or one-singleton-plus-one-remaining-class compositions. Conversely those three produce co-coloring edge vectors that are respectively always zero, always one, or the complement of a star; all lie in the additive edge space, so the cycle-type variance is zero. This proves the equivalence.

**5. Classification of graph statistics of zero variance.** A real weighted statistic has variance zero if and only if its weights lie in the kernel of \(C\), since \(C\) is positive semidefinite. If both nonconstant eigenvalues are positive, only constant edge weights survive; for binary graph edge vectors, these are precisely the empty and complete graphs. With equal class sizes and at least two classes of size at least two, only constants and centered stars survive; their sum is the additive edge space, whose binary points are exactly the four graph classes in the lemma. In the \(\{N-1,1\}\) case, a random singleton vertex \(J\) is uniform, and
\[X_H=m-d_H(J).\]
Thus the variance vanishes exactly if all degrees of \(H\) agree. Finally the all-singleton and one-class compositions make every \(Y_e\) deterministic. This covers the stated cases exhaustively.

## Verification
Run \(\texttt{python3 verify.py}\) using Python 3 standard libraries. The independent exact-rational checker directly enumerates all color assignments for each integer partition of \(N=4,5,6,7,8\), checks the pair covariances, all three eigenvalue relations, seven general integer-weight edge statistics, and exhaustive graph zero-variance classification for every simple graph on 4 and 5 vertices. It passed 8,268 exact assertions over 60 class-size compositions, 108,879 assignments, and 7,488 graph/composition cases. No floating-point tolerance enters. Finite enumeration is not a proof of the all-\(N\) statements, which follow from the preceding algebra and classification lemma.

## Relationship to prior work
Bhattacharya, Diaconis, and Mukherjee (2017, DOI below) study monochromatic edges of arbitrary graphs with **independently sampled** random colors, including independent nonuniform color probabilities; their theorems are mostly distributional limits, not exact prescribed-composition covariance ranks. Bhattacharya and Mukherjee (arXiv:1707.05889) examine connected monochromatic subgraph counts and dense-graph limits under independent colors. Fixing the number of vertices of each color, as done here, introduces a global constraint: it forces the total number of same-color pairs to be deterministic, and it can create nontrivial zero-variance graph statistics.

Filmus and Lindzey (2022, Section 9) establish a representation-theoretic pair-colocation structure for **equal-block-size perfect hypermatchings**; the equal-block pair module and the disappearance of centered vertex stars are therefore not new concepts. A published study of sharp Fourier-projection norms on such uniform set partitions likewise develops the same residual pair module and its overlap kernel, but addresses a different endpoint-norm/Poisson-limit problem. The asserted contribution is the all-class-size, exact *covariance eigenvalues* together with the *complete finite-graph zero-variance classification*, including unequal compositions and regular-graph exceptions. These distinctions are implications about different probability laws and stronger classification targets, rather than reliance on different titles or notation.

## Limitations
This result is only a second-moment statement under a fixed finite color-composition null model. It neither supplies the full distribution of \(X_H\) nor establishes any normal approximation. It does not cover random class counts, weighted colors with conditional interactions, or the proper-coloring distribution. Independent historical-priority review has not been performed. Classical general randomization-variance formulas or representation-theoretic treatments of partition association schemes could implicitly contain portions of the covariance computation; no exhaustive claim of historical novelty is made. The two-eigenvalue decomposition for equal-block partitions overlaps established representation theory, whereas the all-composition rank transitions and graph classification are the substantive assessed extension.

## References
1. B. B. Bhattacharya and S. Mukherjee, *Monochromatic Subgraphs in Randomly Colored Graphons*, arXiv:1707.05889, first posted 2017-07-18, https://arxiv.org/pdf/1707.05889.
2. B. B. Bhattacharya, P. Diaconis, and S. Mukherjee, *Universal Limit Theorems in Graph Coloring Problems with Connections to Extremal Combinatorics*, Annals of Applied Probability 27 (2017), 337–394, https://doi.org/10.1214/16-AAP1205.
3. Y. Filmus and N. Lindzey, *Simple Algebraic Proofs of Uniqueness for Erdős–Ko–Rado Theorems*, arXiv:2201.02887v1 (2022-01-08), Section 9, https://arxiv.org/pdf/2201.02887.
4. *A Poisson asymptotic for sharp Fourier projection norms on uniform set partitions*, published public research record, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-poisson-asymptotic-for-sharp-fourier-projection-norms-on-unifo--65a32e191d85.
