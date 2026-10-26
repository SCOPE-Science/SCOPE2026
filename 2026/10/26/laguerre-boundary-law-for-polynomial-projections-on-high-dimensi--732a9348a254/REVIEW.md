# Scientific review

**Correctness — PASS.** Conditioning a uniform simplex point on one barycentric coordinate gives a beta marginal and a polynomial conditional expectation, which exactly identifies the vertex reproducing kernel. The moment-matrix proof checks every quantified degree and dimension. The limit uses convergent positive-definite moment matrices and explicit uniform-integrability bounds, not a numerical extrapolation. The quadratic closed formula follows from exact beta integration. The script independently checks rational moment identities and sampled high-precision evaluations.

**Originality — PASS, with residual risk.** The nearest published simplex result treats affine polynomial projection only (degree one), whereas the claim is specifically degrees at least two and a sharp growing-dimension Laguerre limit. Primary Jacobi recurrence papers supply orthogonal-polynomial machinery but do not state the specific sharp vertex \(L^\infty\)-norm / positivity-loss limit in the inspected material. Fixed-dimension boundary-trace estimates similarly neither imply the sharp dimension-asymptotic nor the exact quadratic profile. A closely equivalent Jacobi endpoint computation may exist in older unindexed literature; not all accessible full texts were reviewed exhaustively.

**Value — PASS.** Degree-fixed projection on a high-dimensional simplex is canonical in polynomial approximation. The sharp vertex positivity defect and operator-evaluation amplification quantify a concrete stability pathology: for quadratic approximation, it grows quadratically with dimension, with an explicit coefficient, while affine projection grows linearly. The general fixed-degree Laguerre law unifies all orders and provides a reproducible boundary benchmark without pretending to determine global maxima.

**Scope.** Only the point-evaluation norm and the sharp vertex negativity are determined; the global projector norm is not. The exact quadratic result applies to every positive dimension; the asymptotics require fixed degree.

Self-review: passed. Independent audit: not yet performed.
