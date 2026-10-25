# Mathematical assessment of the square Monge inball classification

## Correctness — PASS

The projected Frobenius norm of a coordinate facet normal within the mass-one hyperplane is \(\sqrt{1-n^{-2}}\), while an adjacent Monge facet normal has norm 2. The resulting inball inequalities reduce to a nonnegative matrix with adjacent Monge slacks at least one. A quadratic baseline \(D^0_{ij}=(j-i)(j-i-1)/2\) has unit slacks and total mass \(n^2(n^2-1)/12\). The identity assignment minimizes any Monge array; averaging all permutation assignments proves this lower mass, and equality of all assignment costs forces zero mixed differences. Thus every optimum is \(D^0_{ij}+u_i-u_j\) with \(0\le u_i-u_{i+1}\le1\). The corresponding centers form an \(n-1\)-cube. The coordinate zeros and Monge slacks prove the full facet tangency spectrum. Exact rational examples and independent numerical LP runs corroborate but do not substitute for the general proof.

## Originality — PASS, qualified

Erickson and Kretschmann (arXiv:2311.07522v2, Theorem 5.3) establish the exact facet system and neighboring combinatorial geometry, but not the claimed Euclidean radius and equality cube. Rudolf and Woeginger (DOI:10.1007/BF01415751) address cone extremal rays. Erickson and Jones (arXiv:2609.09508) investigate a Stanley decomposition, normalized volume and Ehrhart series. The accessible portion of that newer text does not yield an inball result; its full 31-page text could not be obtained and is not declared non-covering. Searches of published mathematical findings surfaced the present claim as a self-match and other unrelated polytope inball statements. The classification requires an additional sharp permutation-averaging and equality theorem beyond the known facet list. Historical priority remains best-of-knowledge, not certified.

## Mathematical value — PASS

The normalized Monge cost polytope is a natural object. The exact perturbation-robustness radius, its \(n^{-4}\) order, the positive-dimensional complete set of optimal centers, and variable contact counts form a concrete geometric classification not given by a vertex or facet census alone.

## Scope and limitations

Only the nonsymmetric square family in the sum-one normalization, intrinsic Frobenius distance and \(n\ge2\) is covered. No rectangular extension, alternative norm, John ellipsoid or global priority certification is claimed. The 2026 same-family full text and older cone-ray paper were not fully inspected.
