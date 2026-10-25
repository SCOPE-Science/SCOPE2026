# A complete second-moment inverse theorem for random simplex vertex distances

## Finding
For every integer \(d\ge1\), a labeled nondegenerate Euclidean \(d\)-simplex is uniquely recoverable up to Euclidean isometry from the covariance of \(d\) squared vertex-distance differences to one point chosen uniformly from its interior. No first moments, coordinates, pairwise vertex distances, or higher moments are needed. Conversely **every** real symmetric positive-definite \(d\times d\) matrix arises as that covariance for precisely one labeled isometry class of nondegenerate simplices. Thus the covariance provides global coordinates on the full shape-and-scale space of labeled simplices.

Precisely, write the simplex vertices \(v_0,\ldots,v_d\), and for an interior-uniform point \(X\) define
\[
Y_i=\|X-v_i\|^2-\|X-v_0\|^2,\quad 1\le i\le d,\qquad S=\operatorname{Cov}(Y_1,\ldots,Y_d).
\]
Put \(m=d+1\), let \(I\) be the identity and \(J\) the all-ones \(d\times d\) matrix, and set \(C=(mI-J)/(m^2(m+1))\). The Gram matrix \(G_{ij}=\langle v_i-v_0,v_j-v_0\rangle\) is exactly
\[
\boxed{G=\tfrac12 C^{-1/2}(C^{1/2}SC^{1/2})^{1/2}C^{-1/2}.}
\]
All matrix square roots here are the **unique symmetric positive-definite roots**. Consequently, every squared edge length is obtained from \(G_{ii}\) and \(G_{ij}\), and the \(d\)-dimensional volume is
\[
\boxed{\operatorname{Vol}_d=\left[\frac{m^{d+1}(m+1)^d\det S}{4^d(d!)^4}\right]^{1/4}.}
\]

## Assumptions and scope
The simplex is full-dimensional in a Euclidean space of dimension \(d\), with distinguished labeling \(0,1,\ldots,d\), and \(X\) is distributed by normalized \(d\)-dimensional Lebesgue measure on it. The result includes \(d=1\) and all higher finite dimensions; it concerns *covariances of differences of squared distances*, not covariances of the unsquared distances, and does not reconstruct unlabeled input when the order of the observable coordinates is unknown.

## Proof
Translate \(v_0\) to the origin and form the nonsingular \(d\times d\) edge-column matrix \(V=[v_1-v_0\ \cdots\ v_d-v_0]\), so \(G=V^\top V\) is symmetric positive definite. Every uniform interior point has barycentric representation \(X=v_0+V\lambda\), where \((1-\sum_{i=1}^d\lambda_i,\lambda_1,\ldots,\lambda_d)\) is Dirichlet with all \(d+1\) parameters equal to \(1\). Hence the standard simplex integrals give \(\mathbb E[\lambda_i]=1/m\), \(\operatorname{Var}(\lambda_i)=(m-1)/(m^2(m+1))\), and \(\operatorname{Cov}(\lambda_i,\lambda_j)=-1/(m^2(m+1))\) for \(i\ne j\). This is exactly \(\operatorname{Cov}(\lambda)=C\).

The identity \(\|X-v_i\|^2-\|X-v_0\|^2=G_{ii}-2(G\lambda)_i\) cancels every quadratic term in \(X\). It follows immediately that
\[
S=4GCG.
\]
The eigenvalues of \(mI-J\) are \(1\) once (along the all-ones vector) and \(m\) with multiplicity \(d-1\), so \(C\) is positive definite. Multiply the covariance identity by \(C^{1/2}\) on both sides:
\[
C^{1/2}SC^{1/2}=4(C^{1/2}GC^{1/2})^2.
\]
The matrix \(C^{1/2}GC^{1/2}\) is positive definite. The uniqueness of the positive-definite matrix square root therefore forces the stated inversion. Conversely, any \(S\succ0\) gives \(G\succ0\) by the displayed formula, and a Cholesky factor \(V\) realizes it as a Euclidean simplex, so the covariance map is onto. Gram uniqueness makes it one-to-one up to Euclidean isometry; the forward and inverse maps are smooth on the positive-definite cone.

Furthermore, \(\det C=1/[m^{d+1}(m+1)^d]\), because \(mI-J\) has determinant \(m^{d-1}\). Therefore
\[
\det S=4^d(\det G)^2\det C,
\qquad \det G=(d!\operatorname{Vol}_d)^2,
\]
which gives the volume formula. All equality, positivity, labeling, and boundary statements follow from the same identities, with no probabilistic limiting argument.

## Verification
The proof is exact. A standalone `verify.py` runs 56 independent full-rank numerical covariance inversions and associated volume recoveries in dimensions \(1\) through \(7\), additionally checking the analytic covariance against empirical Dirichlet samples (600,000 points per dimension for dimensions \(1\) through \(4\)). The program reported PASS. These finite tests supplement rather than establish the all-dimensional argument.

## Relationship to prior work
Classical Gram/distance geometry reconstructs simplices **given their edge lengths**. Here the edge-length Gram matrix is reconstructed from the observable second moments of **random squared vertex-distance differences**; it is not input data. Meckes and Meckes (2005, arXiv:math/0505618) analyze normal approximation of linear projections of random vectors uniform in a regular simplex, not this inverse metric problem for arbitrary simplices. Li and Qiu (2016) study moments of a distance from one vertex to a uniformly distributed interior point in a triangle; their single-vertex radial-moment calculations do not specify or invert the joint covariance of \(d\) squared-distance differences in arbitrary dimensions. General shape-space descriptions also use Gram-type coordinates but do not themselves establish that the proposed covariance observable is a complete coordinate.

## Limitations
The sampling law must be uniform over the entire simplex and the observable must retain vertex labels and cross-covariances. Measurement noise may require projecting an empirical covariance onto the positive-definite cone; no statistical error bound or condition number estimate is claimed. The smooth inverse is defined for nondegenerate simplices; singular covariances belong to a separate boundary analysis. Novelty relative to any unindexed probabilistic inverse-geometry treatment remains a bibliographic risk. Independent validation has not been performed.

## References
- E. S. Meckes and M. W. Meckes, *The central limit problem for random vectors with symmetries*, arXiv:math/0505618, first publicly posted 2005-05-27, https://arxiv.org/abs/math/0505618.
- H. Li and X. Qiu, *Moments of Distance from a Vertex to a Uniformly Distributed Random Point within Arbitrary Triangles*, Journal of Applied Mathematics (2016), https://doi.org/10.1155/2016/8371750.
- H. Le and D. Barden, *On Simplex Shape Spaces*, Journal of the London Mathematical Society 64 (2001), 501–512, https://doi.org/10.1112/S0024610701002332.
