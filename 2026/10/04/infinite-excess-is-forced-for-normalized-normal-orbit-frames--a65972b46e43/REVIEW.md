# Review of Infinite excess is forced for normalized normal orbit frames

## Correctness

PASS. The source's scalar spectral model identifies the normalized orbit frame with normalized monomials \(u_n=z^n/\sqrt{m_n}\) and identifies its synthesis operator with \(J^*:\mathcal H_0\to L^2(\mu)\). The source proves \(\ker J^*\neq\{0\}\), proves that the spectral measure is atomic in \(\mathbb D\), and then gives the exact characterization
\[
\ker J^*=\{f\in\mathcal H_0:f(\lambda_j)=0\text{ for every atom }\lambda_j\}.
\]
After the standard outer-radius normalization, \(m_{n+1}\le m_n\), so multiplication by \(z\) is contractive on \(\mathcal H_0\). The kernel characterization is therefore invariant under multiplication by \(z\). Any nonzero kernel function generates the linearly independent family \(f,zf,z^2f,\ldots\); linear independence follows from the identity theorem for analytic functions. The coefficient support shifts right under multiplication by \(z\), yielding a nonzero kernel vector after every finite index. The unitary coefficient map transfers this directly to the original frame synthesis operator.

No finite computation is used to infer the infinite-dimensional conclusion.

## Originality

PASS. The closest primary source, arXiv:2609.23804v1, proves only that the synthesis kernel is nonzero in the relevant step and then uses one nonzero kernel function to locate the spectral measure. Its full text contains no statement of frame excess and no infinite-dimensional-kernel conclusion. The present claim needs the later zero-set characterization plus the bounded shift on the measure-dependent analytic space.

The nearest redundancy literature concerns unnormalized dynamical frames. arXiv:2312.11978v1 proves strong subsampling and finite-removal properties for a special Carleson subclass. arXiv:2505.04859v2 proves broad subsequence stability for positive Carleson spectra. arXiv:2608.11877v1 states infinite excess for finitely generated unnormalized dynamical frames of positive operators via power stability, and its abstract explicitly notes that positivity cannot generally be replaced by normality. A normalized orbit is generally not an orbit of one fixed operator, so those theorems do not imply the accepted claim.

Published-finding database searches for normalized orbit frames, infinite excess, synthesis kernels, monomial-frame redundancy, and Carleson-frame excess returned no statement covering the claim. The comparison is statement-level rather than title-level.

Residual risk remains that an equivalent observation may appear under different terminology in uncatalogued notes or subsequent work, but no such statement was found in the inspected primary sources or the published-finding database.

## Value

PASS. The recent source settles the existence and essential-spectrum side of normalized normal orbit frames and explicitly places the problem next to the redundancy theory of unnormalized Carleson frames. The new statement gives a global structural restriction on every normalized normal orbit frame: finite excess is impossible, and nontrivial coefficient dependencies occur arbitrarily far into the orbit. This strengthens the source's local “not a Riesz basis” obstruction into an infinite-redundancy theorem and supplies a mechanism—shift-invariance of the kernel—that is distinct from power-subsampling arguments for unnormalized positive operators.

Same-model review: passed. Independent audit: not yet performed.
