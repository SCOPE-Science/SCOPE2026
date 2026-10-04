# Rationality of the rank-one-point divisor for 4-by-3-by-3 tensors
## Finding
Let \(U,V,W\) be complex vector spaces of dimensions \(4,3,3\). Let \(\mathcal R\subset \mathbf P(U^\vee\otimes V^\vee\otimes W^\vee)\) be the degree-\(24\) prime divisor introduced by Sherratt: its points are tensors whose associated \(3\times3\) matrix space contains a matrix of rank at most one. Then \(\mathcal R\) is rational. More precisely, the natural incidence
\[
\widetilde{\mathcal R}=\{(\varphi,u,K):u\in\mathbf P(U),\ K\in\operatorname{Gr}(2,V),\ \varphi(u,K,W)=0\}
\]
is a \(\mathbf P^{29}\)-bundle over \(\mathbf P^3\times\mathbf P^2\), and the projection \(\widetilde{\mathcal R}\to\mathcal R\) is birational. Thus a general tensor of \(\mathcal R\) has exactly one rank-one point \(u\), and its two-dimensional kernel \(K\subset V\) is unique.

## Assumptions and scope
All varieties are over \(\mathbf C\). The tensor space has vector-space dimension \(4\cdot3\cdot3=36\). For a point \(u\in\mathbf P(U)\), contraction gives a linear map \(\varphi_U(u):V\to W^\vee\). A rank-at-most-one point is equivalently a pair \((u,K)\), with \(K\in\operatorname{Gr}(2,V)\), such that \(\varphi(u,K,W)=0\). The claim concerns the full projective divisor \(\mathcal R\), not its GIT quotient.

## Proof
Fix \((u,K)\in\mathbf P(U)\times\operatorname{Gr}(2,V)\). The equation \(\varphi(u,K,W)=0\) gives \(2\cdot3=6\) independent linear conditions on the 36 tensor coefficients. Hence the fiber over \((u,K)\) is \(\mathbf P^{29}\). These kernels form a rank-30 vector bundle, so \(\widetilde{\mathcal R}\) is a projective bundle over the rational fivefold \(\mathbf P^3\times\operatorname{Gr}(2,3)\cong\mathbf P^3\times\mathbf P^2\). In particular, \(\widetilde{\mathcal R}\) is irreducible, rational, and has dimension \(3+2+29=34\).

It remains to show that the generically finite projection to Sherratt's irreducible divisor has degree one. Consider tensors admitting two distinct rank-at-most-one points \(u\ne u'\). For fixed \((u,K,u',K')\), choose a basis of \(U\) with \(u=[e_0]\) and \(u'=[e_1]\). The six conditions from \((u,K)\) involve only the \(e_0\)-slice of the tensor and the six conditions from \((u',K')\) involve only the \(e_1\)-slice. Thus all twelve conditions are independent, for every \(K,K'\). The corresponding projective tensor fiber has dimension \(36-12-1=23\). Since the ordered parameter space of \((u,K,u',K')\) has dimension \(10\), this double-incidence locus has dimension at most \(33\), strictly below \(34\).

There is one remaining way uniqueness of \(K\) could fail at a fixed \(u\): the contracted matrix could have rank zero. For fixed \(u\), rank zero imposes nine independent linear equations on the tensor, giving projective fiber dimension \(36-9-1=26\). Allowing \(u\) and a choice of \(K\) gives dimension at most \(3+26+2=31\), again strictly below \(34\). Therefore a general incidence point has a rank-one contraction, a unique kernel \(K\), and no second point \(u'\). The projection is generically one-to-one. Since Sherratt proves that its image is the irreducible divisor \(\mathcal R\) and that the projection is generically finite, it is birational. Rationality of \(\widetilde{\mathcal R}\) therefore implies rationality of \(\mathcal R\).

## Verification
The standalone verifier checks the independent-condition counts and the dimensions \(29,34,23,33,31\) directly from the tensor-coordinate indexing. Its output ends in `VERIFY_OK`. The proof itself is symbolic and dimension-theoretic; no finite experiment is used to infer an infinite statement.

## Relationship to prior work
Sherratt constructs the same incidence variety, proves that its image \(\mathcal R\) is an irreducible degree-\(24\) divisor, and proves that the projection to \(\mathcal R\) is generically finite. The inspected paper does not assert that this map has degree one or that \(\mathcal R\) is rational. Generic finiteness alone does not imply either conclusion. The new step is the two-point incidence bound of dimension \(33\), together with the rank-zero bound of dimension \(31\), which forces generic uniqueness.

## Limitations
The projection need not be one-to-one on special tensors: special members may contain several rank-at-most-one points or a rank-zero point. No claim is made that the incidence morphism is a global isomorphism, that \(\mathcal R\) is smooth, or that the corresponding GIT quotient is rational. A residual literature risk remains that the same rationality observation occurs in older tensor literature under different terminology.

## References
Charlotte Sherratt, *The GIT of \(4\times3\times3\) tensors (determinantal cubic surfaces)*, arXiv:2609.28497v1, Proposition 4.12.
