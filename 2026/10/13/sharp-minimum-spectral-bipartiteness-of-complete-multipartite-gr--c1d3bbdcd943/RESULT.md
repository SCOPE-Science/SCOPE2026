# Sharp minimum spectral bipartiteness of complete multipartite graphs
## Finding
For integers \(N\ge r\ge3\), let \(G=K_{n_1,\ldots,n_r}\) be a complete \(r\)-partite graph with nonempty parts and \(\sum_i n_i=N\). Write the adjacency eigenvalues as \(\lambda_1(G)\ge\cdots\ge\lambda_N(G)\). Then
\[
\lambda_1(G)+\lambda_N(G)\ge r-2.
\]
Equality holds if and only if the part-size multiset is
\[
\{N-r+1,1,\ldots,1\},
\]
so the unique extremal graph up to isomorphism is the complete split graph
\[
K_{r-1}\vee\overline{K_{N-r+1}}.
\]
Therefore the normalized spectral bipartiteness has exact minimum
\[
\min \frac{\lambda_1(G)+\lambda_N(G)}{N}=\frac{r-2}{N}.
\]

## Assumptions and scope
Graphs are finite and simple. All \(r\) multipartite classes are required to be nonempty, and \(r\ge3\) is fixed along with the order \(N\). Spectral bipartiteness means \(\lambda_1(G)+\lambda_N(G)\), following the adjacency-eigenvalue terminology used in arXiv:2609.00210v1. The case \(r=2\) is excluded because every complete bipartite graph has spectral bipartiteness \(0\), so the uniqueness statement is false there.

## Proof
Order the part sizes so that
\[
1\le n_1\le n_2\le\cdots\le n_r.
\]
The adjacency matrix has \(N-r\) zero eigenvalues. Its remaining \(r\) eigenvalues are the eigenvalues \(\theta_1\ge\cdots\ge\theta_r\) of the symmetric quotient matrix \(B\), where
\[
B_{ii}=0,
\qquad
B_{ij}=\sqrt{n_i n_j}\quad(i\ne j).
\]
Set
\[
u=(\sqrt{n_1},\ldots,\sqrt{n_r})^\top,
\qquad
D=\operatorname{diag}(n_1,\ldots,n_r).
\]
Then \(B=uu^\top-D\). Rank-one eigenvalue interlacing between \(-D\) and \(B\) gives
\[
\theta_1\ge -n_1\ge\theta_2\ge -n_2\ge\cdots\ge -n_{r-1}\ge\theta_r\ge -n_r.
\]
A connected complete multipartite graph has exactly one positive adjacency eigenvalue, so \(\theta_1>0\) and \(\theta_2,\ldots,\theta_r<0\). Since \(\operatorname{tr} B=0\),
\[
\lambda_1(G)+\lambda_N(G)
=\theta_1+\theta_r
=-\sum_{i=2}^{r-1}\theta_i
\ge\sum_{i=1}^{r-2}n_i
\ge r-2.
\]

It remains to identify equality. Equality throughout forces
\[
n_1=\cdots=n_{r-2}=1
\]
and
\[
\theta_2=\cdots=\theta_{r-1}=-1.
\]
Let \(s\) be the number of parts of size \(1\). The eigenspace of \(B\) for eigenvalue \(-1\) has dimension exactly \(s-1\): vectors supported on the singleton coordinates and summing to \(0\) give \(s-1\) independent eigenvectors, while the equation \((B+I)x=0\) forces every nonsingleton coordinate to vanish and the singleton coordinates to sum to \(0\). Hence multiplicity at least \(r-2\) forces \(s\ge r-1\). Thus all but at most one part are singletons, giving the claimed complete split graph.

Conversely, for part sizes \(1,\ldots,1,L\) with \(L=N-r+1\), the eigenvalue \(-1\) has multiplicity \(r-2\), and the remaining two nonzero eigenvalues are the roots of
\[
z^2-(r-2)z-(r-1)L=0.
\]
Their sum is \(r-2\), so \(\lambda_1(G)+\lambda_N(G)=r-2\). This proves both the bound and the equality characterization.

## Verification
A standalone pure-Python checker, `verify.py`, enumerates every nondecreasing positive part-size vector with \(3\le r\le7\) and \(r\le N\le18\). It constructs the symmetric quotient, computes its eigenvalues by a Jacobi iteration, checks the lower bound, and checks that equality occurs exactly for the complete split vector. The replay result is:

`ALL CHECKS PASSED; parameter_cases=70; partition_cases=1077; equality_cases=70; max_order=18; max_parts=7; max_split_root_error=1.6e-14`

The finite computation is a stress test only; the proof above is the all-parameter argument.

## Relationship to prior work
Abiad, Kumar, and Pragada, arXiv:2609.00210v1 (first public 2026-08-31), define \(\lambda_1(G)+\lambda_N(G)\) as spectral bipartiteness and prove a general upper bound for \(K_{r+1}\)-free graphs. Their result is an upper extremal statement over a much larger class and does not imply the fixed-multipartition lower extremum proved here.

Stevanović, Gutman, and Rehman, *Ars Mathematica Contemporanea* 9 (2015), 109–113, DOI 10.26493/1855-3974.499.103, prove that the complete split graph uniquely minimizes the adjacency spectral radius, equivalently the graph energy, among complete \(r\)-partite graphs of fixed order. Their inspected result does not optimize \(\lambda_1+\lambda_N\); the least eigenvalue varies with the multipartition, so spectral-radius minimality alone does not imply the present theorem. Their characteristic-polynomial description and one-positive-eigenvalue fact are consistent with the quotient-matrix proof above.

Targeted searches for the exact sum \(\lambda_1+\lambda_N\), the phrases “spectral bipartiteness” and “complete split graph,” and equivalent complete-multipartite formulations did not locate a statement covering the theorem.

## Limitations
The theorem is only for complete multipartite graphs with a fixed number of nonempty parts. It does not claim a lower bound for arbitrary graphs of fixed clique number or chromatic number. The originality search cannot rule out an older result indexed under a different phrase such as “index plus least adjacency eigenvalue”; that terminology is the main residual literature risk. No independent audit has been performed.

## References
1. A. Abiad, H. Kumar, S. Pragada, *Localization of the Caro–Wei bound and its applications to bipartiteness*, arXiv:2609.00210v1, 2026.
2. D. Stevanović, I. Gutman, M. U. Rehman, *On spectral radius and energy of complete multipartite graphs*, Ars Mathematica Contemporanea 9 (2015), 109–113, DOI 10.26493/1855-3974.499.103.
