# Restricted-source exactness in three variables in characteristics \(2\) and \(3\)
## Finding
Let \(k\) be any field of characteristic \(2\) or \(3\), let \(S=k[x_1,x_2,x_3]\), and let \(L_d\) be the space of homogeneous polynomial vector fields on \(k^3\) whose coefficient polynomials have degree \(d\) and whose divergence is zero. Let \(E_d\subseteq L_d\) be the exact subspace: \(D\in E_d\) when contraction of the standard volume form with \(D\) is an exact two-form. Then, for every integer \(d\ge 3\),
\[
E_d=[L_2,E_{d-1}].
\]
Thus, in dimension three, the restricted-source exactness recursion omitted from the cited theorem in characteristics \(2\) and \(3\) nevertheless holds in every degree.

## Assumptions and scope
The field is arbitrary except for \(\operatorname{char}k\in\{2,3\}\). No algebraic-closedness, finiteness, or perfection hypothesis is used. The grading is by coefficient degree, so the bracket of a quadratic field and a degree-\(d-1\) field has degree \(d\). The statement concerns the exact subspace \(E_d\), not all of \(L_d\) in Cartier degrees.

For a target weight \(w=(w_1,w_2,w_3)\) with \(w_1+w_2+w_3=d-1\), either all coordinates are nonnegative or exactly one coordinate is \(-1\). Put
\[
\lambda_w=(w_1+1,w_2+1,w_3+1)\in k^3.
\]
For an interior weight the exact coefficient space is \(\ker\lambda_w\) if \(\lambda_w\ne0\), and is zero if \(\lambda_w=0\). At a boundary weight with \(w_s=-1\), the raw coefficient space is the line \(k e_s\), and its exact part is that line if \(\lambda_w\ne0\), otherwise zero.

## Proof
Fix a target weight \(w\). For an anchor coordinate \(r\), write
\[
\mu_r=(1,1,1)+e_r,
\qquad K_r=\ker\mu_r.
\]
The quadratic divergence-free fields of anchor type \(r\) have coefficient vectors \(a\in K_r\). If \(b\) is the coefficient vector of an exact predecessor of weight \(w-e_r\), the coefficient of their bracket in target weight \(w\) is
\[
c=\lambda_w(a)b-\lambda_w(b)a.
\]
This is the weightwise bracket formula obtained by differentiating the two monomial vector fields.

The predecessor exact space is explicit. If the target is interior and \(w_r>0\), it is \(\ker(\lambda_w-e_r)\) when \(\lambda_w-e_r\ne0\), and zero otherwise. If the target is interior and \(w_r=0\), the predecessor is a boundary weight and its exact space is the line \(k e_r\) precisely when \(\lambda_w-e_r\ne0\). If the target already has boundary coordinate \(w_s=-1\), only anchors \(r\ne s\) with \(w_r>0\) are valid; their predecessor exact space is \(k e_s\) precisely when \(\lambda_w-e_r\ne0\).

In characteristic \(p\in\{2,3\}\), every matrix in this weightwise spanning problem depends on a coordinate \(w_i\) only through two pieces of information: whether \(w_i=0\) or \(w_i>0\), and its residue modulo \(p\). Hence every possible target weight is represented by a finite signature. A zero coordinate is represented by \(0\); a positive coordinate with nonzero residue is represented by that residue; and a positive coordinate divisible by \(p\) is represented by \(p\). A boundary coordinate remains \(-1\).

The exhaustive rank calculation over the prime field gives, in characteristic \(2\), all \(50\) possible signatures and, in characteristic \(3\), all \(108\) possible signatures. For every signature, the span of vectors
\[
\lambda_w(a)b-\lambda_w(b)a
\]
from all valid anchors has exactly the same dimension as the target exact coefficient space. The detailed counts are reproduced by `artifacts/verify.py`: in characteristic \(2\), \(25\) interior signatures have rank \(2\), \(21\) boundary signatures have rank \(1\), and the remaining \(4\) signatures have zero exact target; in characteristic \(3\), the corresponding counts are \(62\), \(42\), and \(4\). There are no rank failures.

Every actual weight with \(d\ge3\) maps to one of these signatures. The excluded all-zero interior signature would have weight sum \(0\), and the excluded boundary signature with both remaining coordinates zero would have weight sum \(-1\), so neither can occur for \(d\ge3\). Finally, the matrices have entries in the prime field. A nonzero minor over \(\mathbb F_p\) stays nonzero after extension to any field of characteristic \(p\), so the rank equalities hold over every such \(k\). Summing the weight spaces proves \(E_d=[L_2,E_{d-1}]\) for every \(d\ge3\).

## Verification
The standalone checker `artifacts/verify.py` implements the finite reduction using exact modular arithmetic. It constructs the quadratic anchor kernels, predecessor exact spaces, the bracket vectors, and the target exact spaces for every canonical signature in characteristics \(2\) and \(3\), then compares ranks. Its recorded output in `artifacts/VERIFY.txt` ends with `CHECK_OK`.

This is an all-degree finite proof after the residue-and-boundary reduction; it is not an inference from checking finitely many degrees.

## Relationship to prior work
Chao Ma's *The Derived Algebra of Nonlinear Polynomial Divergence-Free Vector Fields* proves the unrestricted identity \([L_2,L_{d-1}]=E_d\) over every field and proves the stronger restricted-source identity \(E_d=[L_2,E_{d-1}]\) in characteristic \(p\ge5\). Its proof of the latter explicitly uses coefficients that require excluding characteristics \(2\) and \(3\). The same paper's three-variable discussion describes the Cartier quotient but does not supply the restricted-source recursion in those two characteristics.

The present statement is not a corollary of the unrestricted identity: in positive characteristic, \(E_{d-1}\) can be a proper subspace of \(L_{d-1}\). It closes precisely the two missing characteristics in dimension three. Older modular/vectorial Lie-algebra generation results located in the comparison search either impose characteristic greater than \(3\), concern finite-dimensional or truncated algebras, or do not state this homogeneous exact-source recursion.

## Limitations
The proof is specific to three variables. It does not establish the characteristic \(2\) or \(3\) restricted-source recursion in higher dimension, nor does it assert an analogous result for other Cartan-type or truncated Lie algebras. The originality comparison is against the cited source, targeted database searches, and the inspected nearby literature; very recent or differently phrased work could still contain an equivalent small-characteristic theorem.

## References
1. Chao Ma, *The Derived Algebra of Nonlinear Polynomial Divergence-Free Vector Fields*, Zenodo v1.0, published 2026-07-26, DOI `10.5281/zenodo.21612756`; arXiv `2610.01838v1`.
2. G. Benkart, T. Gregory, A. Premet, *The Recognition Theorem for Graded Lie Algebras in Prime Characteristic*, arXiv `math/0508373`.
3. J.-M. Bois, *Generators of simple Lie algebras in arbitrary characteristics*, arXiv `0708.1711`.
