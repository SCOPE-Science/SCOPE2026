# Signed-permutation universality and a sharp four-dimensional obstruction for paired Rademacher trace estimation

## Finding
For any two real symmetric matrices of order at most three, the minimum variance among **all couplings** of one Rademacher trace probe for each matrix is attained by taking the second probe to be a deterministic signed coordinate permutation of the first. This universality fails first in order four, including for positive-definite matrices arbitrarily close to the identity. Explicitly, let \(C,D\) have zero diagonal and upper-triangular entries, in the edge order \((12,13,14,23,24,34)\), given by
\[
(-2,2,-3,2,2,2),\qquad (-1,2,2,3,-3,3).
\]
For \(A=I_4+\varepsilon C\) and \(B=I_4+\varepsilon D\), every \(0<\varepsilon<1/8\) gives two positive-definite matrices for which the unrestricted minimum variance of the unbiased paired estimator \(r^{\mathsf T}Ar-s^{\mathsf T}Bs\) is exactly \(8\varepsilon^2\), whereas the minimum variance under deterministic signed coordinate permutations \(s=Pr\) is exactly \(12\varepsilon^2\). The latter restriction therefore incurs the sharp factor \(3/2\) for this explicit pair at every admissible \(\varepsilon\).

## Assumptions and scope
A Rademacher vector in dimension \(n\) is uniformly distributed on \(\{-1,1\}^n\), with independent fair signs. In a **paired** trace estimate \(r^{\mathsf T}Ar-s^{\mathsf T}Bs\), the two vectors have these prescribed marginal distributions; the joint distribution may otherwise be arbitrary. Such a coupling produces an unbiased estimate of \(\operatorname{tr}(A)-\operatorname{tr}(B)\). A signed coordinate permutation \(P\) is an orthogonal matrix with exactly one entry, equal to either \(+1\) or \(-1\), in every row and column. We compare unrestricted coupling with \(s=Pr\) for a fixed signed coordinate permutation \(P\). Both choices use one quadratic-form evaluation for each matrix; no efficiency assertion is made about selecting \(P\) from matrix-free information.

The theorem is for *real symmetric* matrices and an individual paired trace estimate. No positive-definiteness is needed for the universal result in orders one to three; positive-definiteness holds for the explicit order-four obstruction. Let \(\mathcal S_n=\{(1,r_2,\ldots,r_n):r_i\in\{-1,1\}\}\), with \(m=2^{n-1}\). Define the centered values \(q_A(r)=r^{\mathsf T}Ar-\operatorname{tr}(A)\), and order the multiset \(\{q_A(r):r\in\mathcal S_n\}\) increasingly as \(q_{A,(1)}\le\cdots\le q_{A,(m)}\), with repetition.

## Proof
**The unrestricted optimum.** A centered quadratic Rademacher form is invariant under replacing its argument by the negative vector. Consequently each centered probe has the uniform empirical distribution on \(\mathcal S_n\), and every admissible pairing of the two full sign vectors induces a coupling between these two empirical scalar distributions. Conversely, a coupling of the two antipodal classes lifts to a coupling of the full vectors: conditionally choose the class representatives according to that coupling, then multiply each representative by a fair global sign. Each resulting marginal is uniform on the full sign cube. For two equal-mass real distributions, the elementary uncrossing inequality
\[
(a-c)^2+(b-d)^2\le (a-d)^2+(b-c)^2 \qquad (a\le b,\ c\le d)
\]
shows that sorted-to-sorted matching minimizes squared distance. Splitting a transportation plan into permutation plans, or iteratively uncrossing, proves the exact universal value
\[
V_*(A,B)=\frac1m\sum_{j=1}^{m}\left(q_{A,(j)}-q_{B,(j)}\right)^2.\tag{1}
\]
This scalar rearrangement principle is classical; the finding concerns the more restrictive implementation of the matching by signed coordinate permutations.

**Universality through order three.** Signed coordinate permutations act on the \(m\) antipodal classes \([r]=\{r,-r\}\). In order one this is the sole class. In order two the sign flip of one coordinate exchanges the two classes, so the induced group contains all their permutations. In order three there are four classes, represented by the four body diagonals of a cube. The signed coordinate group has \(2^3 3!=48\) elements; its center \(\{I,-I\}\) acts trivially on the classes. In fact this kernel is exactly \(\{I,-I\}\): the four diagonal directions are pairwise nonorthogonal, so an orthogonal linear transformation preserving each of their one-dimensional lines must have the same eigenvalue \(+1\) or \(-1\) on all four, and hence be \(I\) or \(-I\). Thus the induced group has \(48/2=24=4!\) elements and equals the full permutation group of the four classes. Every sorted matching in equation (1) can therefore be realized by some deterministic signed coordinate permutation. This proves the universal statement for \(1\le n\le3\), including ties.

**A strict obstruction in order four.** Set the upper-triangular entries of \(C,D\) as in the Finding, with zero diagonals, and let \(A=I_4+\varepsilon C\) and \(B=I_4+\varepsilon D\). The sums of absolute off-diagonal entries in the rows of \(C\) and \(D\) are each bounded by eight. As each is symmetric, \(0<\varepsilon<1/8\) implies all eigenvalues of both matrices lie in the positive interval \((1-8\varepsilon,1+8\varepsilon)\). In particular, both are positive definite and their condition numbers tend to one as \(\varepsilon\) tends to zero.

Writing \(c=( -2,2,-3,2,2,2)\) and \(d=(-1,2,2,3,-3,3)\), for \(r=(1,u,v,w)\) the centered quadratic values divided by \(2\varepsilon\) are the six-edge Walsh expressions
\[
\sum_{i<j}c_{ij}r_ir_j,\qquad \sum_{i<j}d_{ij}r_ir_j.
\]
As \((u,v,w)\) runs lexicographically through \(\{-1,1\}^3\), the two exact lists are
\[
(9,-5,5,-1,-3,-9,1,3),\qquad (0,4,-8,8,-2,-10,2,6).
\]
Their sorted lists are
\[
(-9,-5,-3,-1,1,3,5,9),\qquad(-10,-8,-2,0,2,4,6,8).
\]
The eight squared differences sum to \(16\). Equation (1), including the factor \((2\varepsilon)^2\), gives \(V_*(A,B)=4\varepsilon^2\cdot16/8=8\varepsilon^2\).

To exhaust the fixed signed-coordinate permutations, write \((Pr)_i=\sigma_i r_{\pi(i)}\), where \(\pi\) is a permutation of four coordinates and \(\sigma_i\in\{-1,1\}\). Since flipping all signs leaves quadratic forms unchanged, it suffices to fix \(\sigma_1=1\) and test eight remaining sign choices. Orthogonality of the six nonconstant Walsh edge characters yields
\[
\operatorname{Var}(r^{\mathsf T}Ar-r^{\mathsf T}P^{\mathsf T}BP r)
=4\varepsilon^2\left(\sum_{i<j}c_{ij}^2+\sum_{i<j}d_{ij}^2-2\sum_{i<j}c_{ij}\sigma_i\sigma_j d_{\pi(i)\pi(j)}\right).
\tag{2}
\]
The first two sums are \(29\) and \(36\). For a reproducible integer exhaustion, list the largest possible last cross-sum over the eight signs for each of the 24 coordinate permutations, in lexicographic one-based permutation order:
\[
\begin{array}{c|rrrrrrrr}
\pi &1234&1243&1324&1342&1423&1432&2134&2143\\
\max_\sigma&18&14&18&11&18&17&31&27\\[2pt]
\pi&2314&2341&2413&2431&3124&3142&3214&3241\\
\max_\sigma&15&23&19&29&31&23&13&18\\[2pt]
\pi&3412&3421&4123&4132&4213&4231&4312&4321\\
\max_\sigma&19&30&27&23&11&22&15&26
\end{array}
\]
The global maximum is exactly \(31\), attained for example by the coordinate swap \(\pi=(2,1,3,4)\) and all positive signs. Substituting in (2) gives \(4\varepsilon^2(29+36-62)=12\varepsilon^2\). Comparing with the unrestricted optimum proves the asserted strict factor \(3/2\). The 24-by-eight search is exhaustive, not a sample or numerical optimization.

## Verification
The standalone standard-library `verify.py` enumerates the exact action on antipodal Rademacher classes in dimensions one through four, confirming image sizes \(1,2,24,192\); for the two explicit four-dimensional matrices it computes the integer Walsh values, the sorted cost \(16\), and the restricted minimum cost \(24\) across all \(192\) signed-permutation actions. It checks strict diagonal dominance for every \(0<\varepsilon<1/8\), and uses exact rational arithmetic to confirm the values \(1/32\) and \(3/64\) at \(\varepsilon=1/16\). Execute `python verify.py` with Python 3; no external packages are required. The all-dimensional rearrangement identity and the order-three group argument are analytic, while the four-dimensional finite exhaustive certificate is independently replayable from the embedded code.

## Relationship to prior work
Dharangutte and Musco's dynamic trace-estimation analysis studies tracking changing matrix traces, with DeltaShift using Rademacher probes in coupled differences. Their material establishes variance bounds for that design, not the minimal variance among all possible couplings of the two probe laws or an exact classification of couplings realized by signed coordinate permutations. Epperly, Tropp, and Webber's XTrace work studies exchangeable stochastic trace estimators and symmetrization across independent probe vectors; it does not determine the present fixed-cost paired-coupling implementability frontier. Both methods motivate the precise question, but the general scalar sorted-matching formula is a standard rearrangement fact rather than a newly invented optimal-transport theorem. Likewise, the cubic signed-permutation action on body diagonals is classical; the new content combines it with an exact matrix-probing universality statement and an explicit first-dimensional positive-definite obstruction.

## Limitations
The positive-definite counterexample is an exact two-matrix example, not a statement that signed coordinate permutations are uniformly suboptimal in order four. The factor \(3/2\) is exact for the displayed pair, not a claimed universal worst-case factor. The optimal scalar coupling may require information about matrix entries that is unavailable without extra matrix-vector products, so the result does not claim an efficient matrix-free algorithm or an advantage under an end-to-end computational cost model. It applies to one paired probe, real symmetric matrices, and fixed signed coordinate maps, not Gaussian probes, nonlinear estimators, or multiple mutually dependent samples. Independent external validation has not been performed.

## References
1. Aditya Dharangutte and Christopher Musco, “Dynamic Trace Estimation,” arXiv:2110.13752v1 (26 October 2021), especially algorithmic construction and difference-estimator analysis.
2. Ethan N. Epperly, Joel A. Tropp, and Robert J. Webber, “XTrace: Making the Most of Every Sample in Stochastic Trace Estimation,” arXiv:2301.07825v1 (19 January 2023), especially exchangeability and symmetrization.
