# Sharp negative type survives the midpoint subdivision of balanced complete bipartite graphs

## Finding

Let \(G_n\) be the graph obtained by replacing every edge of \(K_{n,n}\) by a two-edge path, for an integer \(n\ge2\). Its vertices are \(A_1,\ldots,A_n\), \(B_1,\ldots,B_n\), and one midpoint \(E_{ij}\) for each old edge \(A_iB_j\). Let \(d\) be its unweighted shortest-path metric and set
\[
\beta_n=\log_2\!\left(\frac{n}{n-1}\right).
\]
Then for every real \(p\ge0\), the powered-distance kernel \(d^p\), with zero diagonal also at \(p=0\), is conditionally negative definite if and only if \(0\le p\le\beta_n\). Equivalently, for all \(t>0\) the kernel \(\exp(-t d^p)\) is positive semidefinite if and only if \(0\le p\le\beta_n\), where the quantifier *for all \(t>0\)* is essential.

At the sharp endpoint \(p=\beta_n\), the least Euclidean dimension for a configuration whose squared interpoint distances are \(d^{\beta_n}\) is
\[
\begin{cases}4,&n=2,\\ n^2+2n-2,&n\ge3.\end{cases}
\]
Thus introducing \(n^2\) edge midpoints preserves precisely the sharp negative-type exponent of the original balanced biclique, but for \(n\ge3\) increases the endpoint Euclidean realization rank from \(2n-2\) to \(n^2+2n-2\).

## Assumptions and scope

The permutation symmetries of the two old bipartition classes make these kernels invariant under the finite group \((S_n\times S_n)\rtimes C_2\); the proof uses its invariant orthogonal sectors. The graph is the once-subdivided \(K_{n,n}\), *not* the metric realization of its edges as continua and not a different subdivision length. Every vertex, including every new midpoint, is included. The distances between distinct vertices are as follows: old vertices of the same type are distance \(4\), opposite old types distance \(2\); an old vertex to a midpoint is distance \(1\) if incident and \(3\) otherwise; midpoint pairs are distance \(2\) if they share an old endpoint, and \(4\) otherwise. All diagonal distances are zero. Define conditional negative definiteness by
\[
\sum_{x,y\in V(G_n)}c_xc_y d(x,y)^p\le0
\quad\text{whenever}\quad\sum_x c_x=0,
\]
for arbitrary real coefficients. For \(p=0\), set the off-diagonal entries equal to \(1\). The exponent concerns the *finite vertex set*, not all points in the corresponding continuous network.

## Proof

Write \(a=2^p\), \(b=3^p\), and \(c=4^p\). Decompose the real coefficient space under independent permutations of the \(A\)- and \(B\)-indices into the following mutually orthogonal sectors, restricting to vectors whose coefficient sum is zero.

First, the midpoint matrix \((u_{ij})\) with every row sum and column sum zero has dimension \((n-1)^2\) and is an eigenspace of the powered-distance matrix with eigenvalue
\[
L=c-2a.
\]
Second, each zero-sum direction in the original \(A\)-coordinates couples only with the corresponding normalized midpoint row direction. The same holds for \(B\) and midpoint columns. For every such direction the quadratic form has symmetric matrix
\[
M=\begin{pmatrix}
-c&\sqrt n(1-b)\\
\sqrt n(1-b)&n(a-c)+c-2a
\end{pmatrix},
\]
occurring twice with multiplicity \(n-1\). Third, within the coefficient vectors constant on each of the three vertex families, the mean-zero subspace has two orthogonal directions. One takes \(+1\) on the \(A\)'s, \(-1\) on the \(B\)'s, and zero on midpoints, with quadratic form
\[
Q_- = 2n((n-1)c-na).
\]
The other takes \(+1\) on all \(2n\) original vertices and \(-2/n\) on all \(n^2\) midpoints, with quadratic form
\[
Q_+=2(n-1)(3n-2)c+2(n^2+4n-4)a-8n\bigl(1+(n-1)b\bigr).
\]
The two constant directions are orthogonal and mutually uncoupled by symmetry. These sectors have total dimension \((n-1)^2+4(n-1)+2=n^2+2n-1\), the entire mean-zero space.

Set \(p=\beta_n\). Then \(a=n/(n-1)\), \(c=a^2\), and \(Q_-=0\). For \(n\ge3\), write \(h=1/(n-1)\in(0,1/2]\) and \(s=\log_2 3\in(19/12,2)\). The first sector has \(L=a(a-2)<0\). The bottom-right entry of \(M\) simplifies to \(-2a\), and
\[
\det M=2a^3-n(b-1)^2>0.
\]
To see the strict inequality, use \(b=a^s<a^2\), whence \(n(b-1)^2<n(a^2-1)^2=(1+h)h(2+h)^2<2(1+h)^3=2a^3\). The middle inequality follows from \(2-2h^2-h^3>0\) for \(0<h\le1/2\). Hence \(M\) is strictly negative definite.

For the remaining constant direction, exact simplification gives
\[
Q_+=-8n(n-1)\left[b-\left(1+\frac32h+\frac12h^2\right)\right].
\]
The bracket is positive. Indeed \(3^{12}>2^{19}\) implies \(s>19/12\). For \(0\le u\le h\le1/2\), the second derivative of \((1+u)^s\) is
\[
s(s-1)(1+u)^{s-2}>
\frac{19}{12}\frac7{12}\frac45>
\frac23.
\]
Here \((1+u)^{s-2}>(3/2)^{-1/2}>4/5\). Taylor's theorem gives
\[
b=(1+h)^s>1+\frac{19}{12}h+\frac13h^2
\ge1+\frac32h+\frac12h^2,
\]
with the last inequality equivalent to \(h(1-2h)\ge0\). Thus \(Q_+<0\). The only zero direction is therefore the \(A/B\) contrast.

When \(n=2\), \(p=\beta_2=1\), so \((a,b,c)=(2,3,4)\). The mixed midpoint eigenvalue \(L\) vanishes, while the two standard blocks are strictly negative definite (diagonals \(-4\), off-diagonal magnitude \(2\sqrt2\)). Both constant mean-zero directions have zero quadratic form. The mean-zero nullity is exactly three.

Consequently \(d^{\beta_n}\) is conditionally negative definite for every \(n\ge2\). The standard interval property of negative type, alternatively the Bernstein-function preservation of conditional negative definiteness, extends this to every \(0\le p\le\beta_n\).

For \(p>\beta_n\), the same original-vertex contrast has
\[
Q_-=2n\,2^p\bigl((n-1)2^p-n\bigr)>0,
\]
so conditional negative definiteness fails. The sharp exponent follows. Schoenberg's characterization of exponential kernels establishes the stated equivalence with positivity for every \(t>0\). Finally the rank of the centered squared-distance Gram matrix \(-\tfrac12 H D_{\beta_n}H\) is the number of vertices minus one minus the mean-zero nullity; the already-determined nullities give the stated minimum Euclidean dimensions.

## Verification

The accompanying `checker.py` constructs all distances directly from vertex types and indices. It compares the centered powered-distance spectra at the exact candidate exponent for \(n=2,3,\ldots,11\) and checks the exceptional rank counts. It also checks violation above the endpoint and the explicit decomposition inequalities. Use `OPENBLAS_NUM_THREADS=1 python checker.py` with Python 3 and NumPy installed. All infinite-parameter assertions are proved above without reliance on finite tests.

## Relationship to prior work

Sánchez, arXiv:1108.0451 (first public 2011-08-02), obtains \(\beta_n\) for *unsubdivided* \(K_{n,n}\) and gives a general distance-matrix method. The present theorem proves that inserting all edge midpoints does **not** create an earlier obstruction and determines the much larger endpoint embedding rank; neither conclusion is entailed by the old-vertex induced submetric, which supplies only an upper bound. Murugan, arXiv:1112.5657, gives an elegant determinant criterion for vertex-transitive finite metrics, but for \(n\ge3\) the subdivision graph is not vertex transitive: old vertices have degree \(n\), while midpoints have degree \(2\). Campbell–Hendrey–Lund–Tompkins, arXiv:2501.07098, study negative type of *continuous metric graphs* and long subdivisions; their vertex-set subdivision corollary concerns a substantially larger subdivision length and does not imply this exponent or endpoint rank.

## Limitations

Only balanced complete bipartite graphs with each edge subdivided exactly once are treated; no assertion is made for unbalanced bicliques, longer subdivisions, or continuously parametrized edges. The result is a finite-dimensional harmonic decomposition and not a classification of arbitrary graph subdivisions. Originality searches were necessarily bounded, so an older equivalent result in specialized graph metric-embedding literature remains a risk. The analytic proof is supplied for independent checking; independent mathematical audit has not been performed.

## References

- Stephen Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451, 2011, https://arxiv.org/abs/1108.0451.
- Mathav Kishore Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657, first public 2011, https://arxiv.org/abs/1112.5657.
- Rutger Campbell, Kevin Hendrey, Ben Lund, and Casey Tompkins, *Metric graphs of negative type*, arXiv:2501.07098, 2025, https://arxiv.org/html/2501.07098v2.
- I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society 44 (1938), 522–536.
