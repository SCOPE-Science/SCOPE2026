# Exact powered-distance negative type and exponential covariance on Hadamard graphs

## Finding
Let \(n\ge4\) be a multiple of four for which a real Hadamard matrix of order \(n\) exists. On its standard \(4n\)-vertex Hadamard graph let \(d\) denote shortest-path distance. For \(p>0\), the powered-distance kernel \(d^p\) is conditionally negative semidefinite precisely when
\[
0<p\le1,\qquad \sqrt n(3^p-1)\le4^p,\qquad n(2\cdot2^p-1-3^p)\le2^{p+1}-4^p.
\]
The exact squared-Euclidean embedding dimension is \(4n-1-nI_1-I_2-(2n-2)I_3\), where \(I_1\) indicates equality in the first displayed inequality, \(I_2\) indicates equality in the second, and \(I_3\) indicates \(p=1\). Thus the two independent constraints detect rank losses in spectral sectors of multiplicities \(n\) and \(1\), respectively; \(n=4\) has both losses together with a third sector and reduces to a four-dimensional Hamming realization.

The ordinary distance exponential \(K_a(x,y)=\exp(-a d(x,y))\), for \(a\ge0\), is positive semidefinite exactly for \(a=0\) or
\[
a\ge \operatorname{arcosh}((n-2)/2).
\]
For \(n>4\), at the positive endpoint its rank is \(4n-1\); above the endpoint its rank is \(4n\). For \(n=4\) the threshold is zero, the kernel has rank one at zero, and is strictly positive definite for every positive scale. For all these graphs, \(\exp(-t d^p)\) is strictly positive definite for every \(t>0\) if and only if the displayed negative-type conditions hold.

## Assumptions and scope
Take any real Hadamard matrix \(H\) of order \(n\ge4\). The vertices are signed rows \(r_i^\pm\) and signed columns \(c_j^\pm\). Join \(r_i^\varepsilon\) to \(c_j^\delta\) when \(\varepsilon\delta=H_{ij}\). Different Hadamard matrices of the same order need not yield isomorphic graphs; all have intersection array \(\{n,n-1,n/2,1;1,n/2,n-1,n\}\) and this result holds uniformly. The quantity \(d^p\) is the symmetric matrix with zero diagonal and entries \(d(x,y)^p\); conditional negative semidefiniteness means \(v^T d^p v\le0\) whenever \(\sum_xv_x=0\). A positive-definite kernel means a positive-semidefinite matrix, unless 'strict' is stated explicitly.

## Proof
Write \(A_j\) for the zero-one distance-\(j\) adjacency matrices, \(0\le j\le4\). The intersection array implies \(A_1A_j=b_{j-1}A_{j-1}+c_{j+1}A_{j+1}\) for \(1\le j\le3\) with \(b=(n,n-1,n/2,1)\) and \(c=(1,n/2,n-1,n)\), with the usual convention \(A_0=I\). The adjacency eigenvalues and their multiplicities are \(n:1\), \(\sqrt n:n\), \(0:2n-2\), \(-\sqrt n:n\), and \(-n:1\). One can read the roots from the five-by-five intersection matrix; their multiplicities follow from the total dimension and \(\operatorname{tr}(A_1^2)=4n^2\).

The eigenvalues of the ordered distance matrices \((A_0,A_1,A_2,A_3,A_4)\) on these five sectors are, respectively,
\[
(1,n,2n-2,n,1),\quad(1,\sqrt n,0,-\sqrt n,-1),\quad(1,0,-2,0,1),\quad(1,-\sqrt n,0,\sqrt n,-1),\quad(1,-n,2n-2,-n,1).
\]
These formulas can also be obtained directly from the signed-row and signed-column construction, independently of the choice of \(H\).

For \(p>0\), applying weights \((0,1,2^p,3^p,4^p)\) gives the four nonconstant spectral eigenvalues
\[
\sqrt n(1-3^p)-4^p,\quad 4^p-2^{p+1},\quad \sqrt n(3^p-1)-4^p,\quad -n(1+3^p)+2(n-1)2^p+4^p.
\]
The first is strictly negative. The second is nonpositive exactly for \(p\le1\). The last two are nonpositive exactly when the two inequalities in the finding hold. Their multiplicities give the asserted embedding rank from the centered Gram matrix \(-\tfrac12 Jd^pJ\), where \(J=I-(4n)^{-1}\mathbf1\mathbf1^T\). At \(p=1\) and \(n=4\) the three equality sectors have dimensions \(4,1,6\), leaving squared-Euclidean embedding rank \(4\). This establishes the entire exponent classification without numerical root-finding.

For the exponential kernel set \(z=e^{-a}\in(0,1]\). The five eigenvalues of \(\sum_{j=0}^4z^jA_j\), in the same order, factor as
\[
1+nz+2(n-1)z^2+nz^3+z^4,\quad
(1-z^2)(1+\sqrt n\,z+z^2),\quad
(1-z^2)^2,\quad
(1-z^2)(1-\sqrt n\,z+z^2),\quad
(1-z)^2(1-(n-2)z+z^2).
\]
For \(0<z<1\), the first three are strictly positive. Since \(n-2\ge\sqrt n\) for \(n\ge4\), the last quadratic gives the more restrictive positive-semidefiniteness condition; its smaller positive root for \(n>4\) is \(\rho_n=((n-2)-\sqrt{(n-2)^2-4})/2\). Thus positivity holds exactly when \(z\le\rho_n\), corresponding to \(a\ge\operatorname{arcosh}((n-2)/2)\). At \(z=1\) the matrix is the all-ones matrix and is positive semidefinite of rank one. The factorization proves the asserted ranks for \(n>4\). For \(n=4\), all factors are positive at \(0<z<1\). Finally, Schoenberg's finite-distance equivalence identifies conditional negative semidefiniteness of \(d^p\) with positivity of \(\exp(-t d^p)\) at every \(t>0\); in that case the points have distinct Hilbert-space images, so each positive-bandwidth Gaussian is strictly positive definite.

## Verification
The companion `CHECK.py` constructs the standard Hadamard graphs for orders \(4\), \(8\), and \(16\), calculates all shortest-path distances by breadth-first search, and compares their eigenvalues for powered distances against the exact five-sector formulas. The checker passed on these three orders. Symbolic factorization of the five eigen-polynomials is explicit in the proof and reproducible independently. The finite calculations test implementation and normalization, not the theorem for all Hadamard orders.

## Relationship to prior work
Sánchez's 2011 finite-metric theory provides the general negative-type criterion and the interval property, but does not give these Hadamard-graph inequalities or rank losses. Ma and Koolen's 2014 work states the Hadamard intersection array in the classification of twice \(Q\)-polynomial distance-regular graphs, but does not calculate powered-distance negative-type thresholds. DeVille's 2017 generalized-distance spectral framework applies to all distance-regular graphs and explicitly studies profiles \(z^j\); it gives the general method from which the exponential sector polynomials can be obtained, but the particular Hadamard-specific sharp cutoff, competing powered-distance inequalities, and squared-Euclidean rank formula are not stated in the inspected full text. These are an explicit specialization and sign analysis of that general framework, not a replacement for it. The 1989 distance-regular-graphs monograph supplies standard association-scheme background.

## Limitations
The result is conditional on the existence of the specified Hadamard matrix; existence for all orders divisible by four is not assumed or claimed. The implicit exponent inequalities are an exact classification, but no general closed elementary expression for the maximal exponent or the switch between its two potential controlling sectors is claimed. Bounded literature review does not prove global originality; equivalent specializations in older association-scheme work may exist. No external independent mathematical audit has been performed.

## References
S. Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451, posted 2011-08-02. J. Ma and J. Koolen, *Twice \(Q\)-polynomial distance-regular graphs of diameter 4*, arXiv:1405.2546, 2014. L. DeVille, *The generalized distance spectrum of a graph and applications*, arXiv:1708.02294, 2017. A. E. Brouwer, A. M. Cohen and A. Neumaier, *Distance-Regular Graphs*, Springer, 1989.
