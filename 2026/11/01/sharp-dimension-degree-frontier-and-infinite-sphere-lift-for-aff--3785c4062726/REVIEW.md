# Scientific review: sharp affine Bernstein dimension–degree frontier

## Correctness — PASS

The claim ranges over every integer \(d\ge2\), integer \(n\ge1\), and every continuous real zonal positive-definite input on \(S^d\). When \(n\le d+1\), the Boolean sign cube embeds isometrically in the sphere, the restricted group-convolution matrix is positive semidefinite, and its Walsh coefficients are all nonnegative by explicit quadratic forms. Independent signs turn Bernstein sampling into \(\sum_A\widehat h(A)t^{|A|}\); each tensor-power kernel is positive semidefinite on all spheres. This proves the positive direction and the stronger dimension lift. For \(n\ge d+2\), a normalized Gegenbauer polynomial is a valid test kernel and its degree-\(n\) output coefficient is strictly negative by an exact finite-difference calculation; Schoenberg's theorem gives failure. Direct exact-rational checks passed 2,298 supplementary assertions and verified 70 independent symbolic instances of the obstruction. No finite enumeration is used as a substitute for either universal proof.

## Originality — PASS relative to inspected evidence

The preceding mathematical result already contains the \(S^2\) classification and the all-dimensional failure direction. The present new component is the **full previously untreated positive direction for every \(d\ge3\)** and the explicit all-dimensions output lift. Otten–Nguyen–Watts (arXiv:2608.04836, Section 4 read in full) gives the \(S^2\) degree-four failure and a power-Bernstein operator on \(S^\infty\) for inputs assumed positive definite in infinite dimension, not an affine Bernstein preservation theorem for arbitrary finite-sphere inputs. Beatson–zu Castell's dimension-walk operators and Gneiting's Schoenberg framework are distinct and do not imply the finite-node result without the new hypercube argument. Equivalence, broader-coverage, database/table and claim-versus-prior implication searches found no dominating result in the consulted records. Residual risk: an unindexed historical proof may already use the hypercube restriction; search absence is not a uniqueness certificate.

## Value — PASS

This is a complete natural classification of a standard approximation operator on spherical covariance/Gram cones. The exact threshold \(n=d+1\), its first failing degree \(n=d+2\), and the positive direction's unexpected promotion of an \(S^d\)-only input to an \(S^\infty\)-positive polynomial answer the natural finite-dimension question after a known counterexample. The result includes a reusable structural lemma rather than only a numerical improvement or arbitrary parameter slice. It has a clear limit: no claim for altered nodes, geodesic Bernstein operators, or strict positive definiteness.

## Closest literature and limitations

Otten, Nguyen, Watts (2026), arXiv:2608.04836, is the motivating primary source. Schoenberg (1942), Gneiting (2013) supply the classical coefficient characterization; Beatson and zu Castell (2017) treats different dimension-hopping operators. The preceding technical finding provided the negative calculation and the \(S^2\) special case. The proof has not been independently audited and equivalent historical coverage may remain undiscovered.

Self-review: passed. Independent audit: not yet performed.
