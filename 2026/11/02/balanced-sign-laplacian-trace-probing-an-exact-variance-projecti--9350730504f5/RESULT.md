# A graph-theoretic characterization of singular permutation edge-count covariance

## Finding

Let \(N\ge4\) and let \(k,\ell\ge2\) satisfy \(k+\ell=N\). Give each unordered vertex pair a real weight \(w_{ij}=w_{ji}\) (zero on missing edges), and draw a uniform ordered partition \((A,B)\) with sizes \(k,\ell\). Write \(W_A,W_B\) for the total within-part edge weights and \(d_i=\sum_{j\ne i}w_{ij}\).

The covariance matrix of \((W_A,W_B)\) is singular **if and only if** at least one of the following holds:

1. All weighted degrees \(d_i\) are equal.
2. There are real vertex potentials \(u_i\) such that \(w_{ij}=u_i+u_j\) for every \(i\ne j\).

The second condition characterizes **exactly** when \(W_A/(k-1)+W_B/(\ell-1)\) is constant, for any of the allowed size pairs. The first characterizes when \(W_A-W_B\) is constant. In particular, for a simple unweighted graph the covariance is singular exactly for regular graphs, stars, and a clique on \(N-1\) vertices with one isolated vertex. The clique with an isolate is omitted from Theorem 3.2 of Chen and Friedman, [arXiv:1307.6294v6](https://arxiv.org/html/1307.6294v6); this family gives a counterexample to the necessity assertion in that version for every \(k,\ell\ge2\).

For an even number of vertices and \(k=\ell=N/2\), the cut weight \(C(A,B)=\sum_{i\in A,j\in B}w_{ij}\) is deterministic exactly in condition 2. In the unweighted case this leaves four graphs up to isomorphism: the empty graph, the complete graph, a star, and a clique with an isolate. Thus for the Laplacian \(L\) and uniform balanced signs \(s\), the one-query estimator \(T=(N-1)s^\top Ls/N\) has precisely this zero-variance locus. Its variance and the numerical test for it are consequences of known permutation moment formulas, as detailed below.

## Assumptions and scope

Weights are symmetric, with no self-loops. The partition distribution is uniform over all \(k\)-vertex first parts, giving full support; no random graph model is used. Signed weights are allowed for the covariance theorem. For the ordinary weighted graph-Laplacian application the edge weights can be taken nonnegative. The structural statements need both part sizes at least two. The graph-family list assumes all weights are zero or one.

## Proof

**The exchange test.** Covariance is singular exactly when some \(\alpha W_A+\beta W_B\) with \((\alpha,\beta)\ne(0,0)\) is constant on the support. Fix two distinct vertices \(i,j\), with \(i\) in the first part and \(j\) in the second. For \(x\notin\{i,j\}\) put \(\delta_x=w_{ix}-w_{jx}\). Let \(R=A\setminus\{i\}\), an arbitrary \((k-1)\)-subset of the other \(N-2\) vertices. Comparing with the partition obtained by swapping \(i,j\) gives
\[
(\alpha+\beta)\sum_{x\in R}\delta_x=\beta(d_i-d_j).
\]
Indeed, the original minus the exchanged values of \(W_A,W_B\) are \(\sum_R\delta_x\) and \(-\sum_{x\notin R\cup\{i,j\}}\delta_x\), and \(\sum_{x\ne i,j}\delta_x=d_i-d_j\).

If \(\alpha+\beta=0\), then \(\beta\ne0\), so every \(d_i=d_j\). Conversely, \(2(W_A-W_B)=\sum_{i\in A}d_i-\sum_{j\in B}d_j\) is constant when the degrees are equal. If \(\alpha+\beta\ne0\), the sum of \(\delta\) on \(R\) is constant. Because \(1\le k-1\le N-3\), we can compare subsets differing by any one replacement, proving that every \(\delta_x\) for this \(i,j\) has the same value.

To recover the potentials, choose a vertex \(p\), and let \(a_i\) be the common value of \(w_{ix}-w_{px}\) for \(x\ne i,p\). For distinct \(i,j\ne p\), symmetry in \(w_{ij}=a_i+w_{pj}\) gives \(a_i-w_{pi}=a_j-w_{pj}\), say \(b\). Set \(u_p=-b/2\) and \(u_i=w_{pi}+b/2\) for \(i\ne p\). Then \(w_{ij}=u_i+u_j\) on every pair. Conversely, under this representation \(W_A=(k-1)\sum_{i\in A}u_i\), \(W_B=(\ell-1)\sum_{j\in B}u_j\), yielding the constant relation. The exchange test with its coefficients, whose sum is positive, proves necessity specifically for this relation. In balanced parts, \(C(A,B)=W-W_A-W_B\) for fixed total weight \(W\), so it has the same constancy condition.

**Binary weights and the missing family.** If every potential is the same, the graph is empty or complete. Otherwise choose \(u_i>u_j\). For each \(x\notin\{i,j\}\), the binary weights satisfy \(w_{ix}-w_{jx}=u_i-u_j>0\), forcing \((w_{ix},w_{jx})=(1,0)\). Those other potentials all equal a common \(c\); the two distinguished ones are \(1-c,-c\). Two other vertices exist, so \(2c\in\{0,1\}\). With \(c=0\) this is a star; with \(c=1/2\) it is a clique with an isolate. The displayed potentials realize each family, as do constant potentials 0 and \(1/2\) for empty and complete respectively. More explicitly, for a clique with an isolate, the two possible within-part edge vectors are
\[
\left(\binom{k-1}{2},\binom{\ell}{2}\right)
\quad\text{and}\quad
\left(\binom{k}{2},\binom{\ell-1}{2}\right).
\]
Both have positive probability and are distinct, so their covariance has rank one. This graph is neither regular nor a star even at \(N=4\), where it is a triangle with an isolate.

## Relationship to prior work and the balanced Laplacian identity

Chen and Friedman, *A new graph-based two-sample test for multivariate and object data*, [arXiv:1307.6294v6](https://arxiv.org/html/1307.6294v6), §3, give the unweighted permutation covariance in Lemma 3.1. Their Theorem 3.2 in that version lists just regular and star graphs. Their displayed determinant already contains the numerical condition admitting the clique with an isolate. The present characterization identifies the graph families and proves the weighted incidence structure that produces this degeneracy.

Zhou and Chen, *RISE: Rank in Similarity Graph Edge-Count Two-Sample Test*, [arXiv:2112.12948v2](https://arxiv.org/html/2112.12948v2), §2.2, Theorems 2.1–2.3, give the weighted moments and the two numerical equality conditions (C1), (C2). Put \(Q=\sum_{i<j}w_{ij}^2\), \(D_2=\sum_i d_i^2\), and \(W=\sum_{i<j}w_{ij}\). In their notation \(r_0=2W/[N(N-1)]\), \(r_1^2=D_2/[N(N-1)^2]\), and \(r_d^2=2Q/[N(N-1)]\). Condition (C1) is degree constancy by the variance of the row averages. Their bracket for (C2) is \(2/[N(N-1)]\) times \((N-2)Q-D_2+2W^2/(N-1)\). The exchange argument above identifies the structural meaning of this equality without using the moment formulas.

For \(k=\ell=N/2\) the ordered-pair within counts in that paper are \(U_x=2W_A\) and \(U_y=2W_B\); the statistic \(U_w=(U_x+U_y)/2=W-C(A,B)\). Its permuted variance is therefore the cut variance, with known prefactor \(N^2/[8(N-3)]\) multiplying their bracket. Also each edge crosses a balanced cut with probability \(N/[2(N-1)]\). Since \(s^\top Ls=4C(A,B)\), these give \(\mathbb E T=2W=\operatorname{tr}L\) and
\[
\operatorname{Var}T=\frac{4(N-1)}{N(N-3)}\left[(N-2)Q-D_2+\frac{2W^2}{N-1}\right].
\]
Equivalently, define \((Bu)_{ij}=u_i+u_j\). Then \(B^\top B=(N-2)I+\mathbf1\mathbf1^\top\) and \(B^\top w=d\), so the unique least-squares potentials are \(u_i=(d_i-W/(N-1))/(N-2)\). Subtracting \(d^\top u\) from \(Q\) shows that the bracket is \((N-2)\min_u\|w-Bu\|_2^2\). This is a projection form of the prior weighted variance, not a claim of a new permutation-moment formula. The connection with degree-two harmonics on the Boolean slice is consistent with Filmus and Mossel, [arXiv:1507.02713](https://arxiv.org/abs/1507.02713), §3.2.

## Reproducibility and limitations

Run `python3 verify.py` with standard Python. It tests the stated singularity and constant-statistic equivalences using exact permutation support, exhausts all labeled simple graphs of orders 4, 5 and 6 for each allowed first-part size up to complementation, and tests weighted examples with exact integer arithmetic. These are bounded checks; the exchange proof covers all the stated sizes and real weights. The result does not assess implementations or tests based on changing the underlying weight matrix after each permutation. The correction is to the cited version of the unweighted theorem; no claim is made that no other source has noted the missing graph family.
