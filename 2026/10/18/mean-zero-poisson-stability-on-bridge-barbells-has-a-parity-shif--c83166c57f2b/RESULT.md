# Mean-zero Poisson stability on bridge barbells has a parity-shifted balance optimum

## Finding

Let \(B_{a,b}\) be obtained by joining one distinguished vertex of a complete graph with \(a\) vertices to one distinguished vertex of a disjoint complete graph with \(b\) vertices by a single unit-weight edge. Assume \(2\le a\le b\), put \(n=a+b\), let \(L\) be the unnormalized combinatorial graph Laplacian, and let \(G=L^\dagger\) be its Moore–Penrose inverse. Define two sharp operator constants:

\[
U_{a,b}=\sup_{\|f\|_\infty\le1}\|Gf\|_\infty,
\qquad
W_{a,b}=\sup_{\substack{\|f\|_\infty\le1\\\sum_v f(v)=0}}\|Gf\|_\infty.
\]

The exact unrestricted constant is

\[
\boxed{U_{a,b}=\frac{2((a+1)b(b+1)-a)}{(a+b)^2}.}
\]

The exact compatibility-constrained constant is

\[
\boxed{
W_{a,b}=\begin{cases}
(a+2)/2,&b=a,\\
(a+1)(a+2)/(2a+1),&b=a+1,\\
(ab+a+b+2)/(a+b),&b\ge a+2.
\end{cases}}
\]

For both norms, the maximizing evaluation vertices are **exactly the nondistinguished vertices of the smaller clique** when \(a<b\), and the nondistinguished vertices of both cliques when \(a=b\). An unrestricted extremizing forcing is constant \(+1\) on the smaller clique and \(-1\) on the other. Constrained extremizers can be constructed by assigning \(-1\) at the lowest half of the entries of a maximizing row of \(G\), \(+1\) at the highest half, and, if \(n\) is odd, zero at a median entry; signs can be reversed.

At fixed total order \(n\), the **unique unordered pair of clique sizes maximizing \(W_{a,b}\)** is

\[
\boxed{\{a,b\}=\begin{cases}
\{2,2\},&n=4,\\
\{m-1,m+1\},&n=2m\ge6,\\
\{m,m+1\},&n=2m+1\ge5.
\end{cases}}
\]

The corresponding maxima are \(2\) for \(n=4\), \((m+1)^2/(2m)\) for even \(n=2m\ge6\), and \((m+1)(m+2)/(2m+1)\) for odd \(n=2m+1\ge5\). Thus for an even number of vertices, **equal cliques are not worst for mean-zero forcing**: moving one vertex from one clique to the other increases the exact norm by \(1/(2m)\).

If \(a/n\to\theta\in[0,1/2]\), then

\[
\frac{U_{a,b}}n\longrightarrow 2\theta(1-\theta)^2,
\qquad
\frac{W_{a,b}}n\longrightarrow\theta(1-\theta).
\]

Consequently, among all pairs \(a,b\ge2\) with \(a+b=n\), the unrestricted norm has asymptotic maximal coefficient \(8/27\), at the clique proportion \(a/n\to1/3\); the mean-zero norm has maximal coefficient \(1/4\), at \(a/n\to1/2\). For fixed \(a\ge2\) as \(b\to\infty\), the respective constants tend to \(2(a+1)\) and \(a+1\). The compatibility condition therefore changes both the global asymptotically most unstable geometry and the extreme-imbalance amplification by a factor of two.

## Assumptions and scope

All spaces, forcing vectors and operators are real; no claim is made about the mean-zero constrained norm over complex forcing vectors. The norm on vectors is the maximum absolute component. The operator \(G\) is defined on every vector, kills constants, and is the unique zero-mean solution map for \(Lu=f-(\sum_v f(v)/n)\mathbf1\). The second supremum measures the physical Poisson compatibility restriction, without changing the \(\ell^\infty\) input normalization. Every edge, including the bridge, has unit conductance. No statement is made for normalized Laplacians, multiple bridges, or clique sizes below two.

## Proof

**1. Resistance reconstruction.** In a complete graph of order \(a\), the effective resistance between any two distinct vertices is \(2/a\). The bridge is a cut edge, so the resistance between vertices in opposite cliques equals one plus the resistance from each vertex to the associated bridge endpoint. Write \(R_{ij}\) for these resistances, \(r_i=n^{-1}\sum_jR_{ij}\), and \(\bar r=n^{-1}\sum_i r_i\). The centered resistance identity gives

\[
G_{ij}=\tfrac12(r_i+r_j-\bar r-R_{ij}).
\]

Indeed \(R_{ij}=G_{ii}+G_{jj}-2G_{ij}\) and \(G\mathbf1=0\) imply this identity by twofold averaging. Alternatively, the identity and the graph Poisson equations directly verify \(LG=I-\mathbf1\mathbf1^\mathsf T/n\).

Call the bridge endpoints \(A_0,B_0\), and the other vertices \(A_1,\ldots,A_{a-1}\) and \(B_1,\ldots,B_{b-1}\). After elementary substitution the entries of an \(A_i\) row (\(i\ge1\)) are

\[
\begin{array}{c|ccccc}
\text{column}&A_i&A_0&A_j\ (j\ne i,\ j\ge1)&B_0&B_j\ (j\ge1)\\\hline
n^2G_{A_i,\,\cdot}&
\displaystyle\frac{a^2+ab^2+3ab-2a+2b^2}{a}&
 b^2-2&
\displaystyle\frac{ab^2+ab-2a+b^2}{a}&
-(ab+2)&-(ab+n+2)
\end{array}
\]

(the third column is absent when \(a=2\)). The other clique follows by swapping \(a,b\). For the bridge-endpoint row \(A_0\), the entries at \(A_0,A_i,B_0,B_j\) respectively, multiplied by \(n^2\), are

\[
a+b^2+b-2,\quad b^2-2,\quad -(ab-n+2),\quad -(ab+2).
\]

All same-clique entries of \(G\) are positive and all across-bridge entries are negative for \(a,b\ge2\). Hence the \(\ell^\infty\) norm of a row is twice the sum of its entries over its own clique. Substitution yields the unrestricted row values and differences

\[
U(A_i)=\frac{2((a+1)b(b+1)-a)}{n^2},\quad
U(A_i)-U(A_0)=\frac{2b}{n},
\]

\[
U(A_i)-U(B_j)=\frac{2(b-a)(ab+n+2)}{n^2},\quad
U(B_j)-U(B_0)=\frac{2a}{n}.
\]

Their signs prove the asserted unrestricted constant and all maximizing vertices.

**2. The exact mean-zero dual norm.** For any row \(g=(g_1,\ldots,g_n)\), linear programming duality, or the elementary median argument, gives

\[
\sup_{\substack{|f_j|\le1\\\sum_j f_j=0}}\sum_j g_jf_j
=\min_{c\in\mathbb R}\sum_j|g_j-c|.
\]

To verify equality directly, order the entries of \(g\), put \(f=-1\) on the smallest \(\lfloor n/2\rfloor\) entries and \(f=+1\) on the largest \(\lfloor n/2\rfloor\), and assign the remaining entry value zero for odd \(n\). This is feasible, and any median minimizes the absolute deviation. The opposite sign gives the absolute-value extremum.

In an \(A_i\) row, all the entries in the \(A\)-clique are above all entries in the \(B\)-clique. The \(B_0\) entry exceeds the repeated \(B_j\) entry by exactly \(1/n\). Thus, when \(b=a\), a median may be chosen anywhere between the two clique blocks; when \(b=a+1\), the median is the \(B_0\) entry; and when \(b\ge a+2\), it is the repeated \(B_j\) entry. Substitution into the median formula gives, respectively, the three stated cases for \(W(A_i)\).

Performing the same ordered-row calculation at all four vertex types gives the identities

\[
W(A_0)=W(A_i)-1,\qquad
W(B_j)=\frac abW(A_i),\qquad
W(B_0)=\frac{a^2}{n}.
\]

In each case \(W(B_j)>W(B_0)\): for \(b=a\), the difference is \(1\); for \(b=a+1\), it is \(2a/n\); and for \(b\ge a+2\), it is \(a(n+2)/(bn)\). Since \(a/b\le1\), with equality precisely when the cliques are equal, these identities prove the claimed sharp restricted norm and its exact maximizing vertices.

**3. Extremal clique allocation.** At fixed \(n\), in the region \(b-a\ge2\), the formula is \(W=1+(ab+2)/n\), strictly increasing with \(a\) for \(a<b\). For \(n=2m\ge6\), the largest candidate in this region is \((a,b)=(m-1,m+1)\), and its norm \((m+1)^2/(2m)\) exceeds the balanced value \((m+2)/2\) by \(1/(2m)\). The \(n=4\) exception is immediate. For \(n=2m+1\), the largest \(b-a\ge3\) candidate is \((m-1,m+2)\), whose norm is \((m^2+3m+1)/(2m+1)\); the nearest-balanced case \((m,m+1)\) is larger by \(1/(2m+1)\). For \(n=5\), there is only the latter candidate. These strict comparisons prove uniqueness up to interchange of the cliques.

**4. Scaling.** The exact formulas give, uniformly in \(2\le a\le b\) with \(a+b=n\),

\[
\frac{U_{a,b}}n=2\frac an\left(\frac bn\right)^2+O(n^{-1}),
\qquad
\frac{W_{a,b}}n=\frac an\frac bn+O(n^{-1}).
\]

The first limiting polynomial has its unique maximum on \([0,1/2]\) at \(\theta=1/3\), where it equals \(8/27\). The second has its unique maximum at \(\theta=1/2\), where it equals \(1/4\). Fixed-\(a\) limits follow directly from the exact formulas.

## Verification

`CHECK.py` uses only the Python standard library and constructs the integer graph Laplacian independently of the resistance formula. It computes \((L+J/n)^{-1}-J/n\) in exact rational arithmetic and compares the result to the resistance reconstruction, verifies \(LG=I-J/n\), all row sums, both sharp norm formulas, exact sets of maximizing vertices, median-forcing extremizers, and the fixed-size extremal partition for \(4\le n\le100\). It completed 195 parameter families successfully, including every \(2\le a\le9\) and \(a\le b\le16\). Reproduce from the package by running `python3 CHECK.py`. These finite checks detect errors in the algebra but do not prove the universally quantified theorem: the proof is the symbolic resistance-and-median computation above.

## Relationship to prior work

The bridge-joining pseudoinverse formulas of Ranjan, Zhang and Boley (arXiv:1304.2300, first submitted 2013-04-08), especially their clique pseudoinverse and first-join theorem, provide general entrywise Green-matrix machinery. They establish the individual matrix entries by an arbitrary-graph construction; they do not state the two sharp induced norms on bridge barbells, the distinct balancing optima under and without forcing compatibility, or the parity-shifted finite-order extremum. The present classification does not claim a new formula for a general graph's pseudoinverse. Earlier spectral results for discrete graph operators, including Bonnefont, Golénia and Keller (arXiv:1311.7221, first submitted 2013-11-28), address eigenvalue asymptotics and functional inequalities on sparse graphs, rather than the sharp maximum-norm inversion constants of this two-clique family.

The effective-resistance identity and the median formula are established general tools, not proposed as new. The mathematical contribution asserted here is their fully optimized two-parameter combination, especially the compatibility-sensitive global extremizers and the finite even-order exception. A general formula for every entry of \(G\) is not by itself a formula for the constrained \(\ell^\infty\) operator norm or its sharp optimization over all clique splits.

## Limitations

The finding is restricted to unweighted bridge barbells with both cliques containing at least two vertices. The formulas concern the centered Moore–Penrose inverse, not the normalized Laplacian, Dirichlet inverse or arbitrary forcing boundary data. The proof is analytical; the finite checker is not an exhaustive computational certificate over all integers. The prior-work assessment is limited to the cited accessible texts and searches; an exact equivalent result in another source or terminology remains a historical-priority risk. No independent mathematical verification has been performed.

## References

1. G. Ranjan, Z.-L. Zhang, D. Boley, *Incremental Computation of Pseudo-Inverse of Laplacian: Theory and Applications*, arXiv:1304.2300 (first public preprint 2013-04-08); especially Sections 2.3.2 and 3.2.1.
2. M. Bonnefont, S. Golénia, M. Keller, *Eigenvalue asymptotics for Schrödinger operators on sparse graphs*, arXiv:1311.7221 (first public preprint 2013-11-28), *Annales de l'Institut Fourier* 65 (2015), 1969–1998, DOI:10.5802/aif.2979 (primary MSC 47A10).
3. E. Bozzo, *The Moore–Penrose inverse of the normalized graph Laplacian*, *Linear Algebra and its Applications* 439 (2013), 3038–3043, DOI:10.1016/j.laa.2013.08.039 (normalized rather than combinatorial Laplacian).
4. R. B. Bapat, *Graphs and Matrices*, Springer, 2010 (classical graph Laplacians, resistance and generalized inverses; background only).
