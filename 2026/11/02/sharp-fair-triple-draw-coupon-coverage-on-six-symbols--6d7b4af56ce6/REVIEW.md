# Scientific review: sharp six-symbol fair triple coverage

## Correctness — PASS

The result is formulated for a nonempty simple three-uniform family on six symbols, all blocks equally probable, with constant vertex degree. Fairness forces an even number \(M\) of blocks and degree \(M/2\). Inclusion-exclusion, with all denominators positive, yields the exact expectation \(22+M/(M-1)-\sum_e M/(M-c_e)\), where the fifteen pair codegrees sum to \(3M\). Strict discrete convexity bounds the sum by the balanced integer codegree vector. Evaluating the complete ten-member list of admissible even support sizes yields a unique optimal *support size* \(M=10\); equality of the convex bound at that size forces all pair codegrees to equal two. The displayed ten-block design meets those constraints. The smaller-alphabet cutoff uses divisibility for four symbols and the unique five-cycle complement for five symbols. An independent exact-rational absorbing-state dynamic calculation reproduces the critical expectations, and `verify.py` passes all 53 checks. The mathematical argument, not finite enumeration, certifies the universal bound over the stated finite class.

## Originality — PASS (subject to historical-priority risk)

The publicly posted June 2026 preprint by Barak-Pelleg and Berend supplies a fair seven-point Fano counterexample, further projective-plane and star mechanisms, and explicitly leaves exact maximization among fair supports open. Its substantive mathematical sections and full paper were examined; they give neither a six-point extremum nor the pair-codegree equality classification. Grunbaum–Yaakobi's 2025 source formulates the fair extremality conjecture, establishes general coverage identities and gives special-case results and global bounds; its full relevant sections were examined, without a six-symbol classification. The authors' public source-code repository lists projective, affine, star and full-support computations, not a global six-symbol optimization. The relevant published mathematical-record search hits concern distinct 3-uniform packing or 3-union-free problems, not expected coverage times. No source inspected directly implies the exact maximum or the first counterexample order. Absence of an indexed covering result cannot prove priority; an uncatalogued older calculation of this small instance remains possible.

## Mathematical value — PASS

The source explicitly singles out sharp fair-mechanism maximization as an open structural question. The theorem closes its first nontrivial six-symbol triple instance, improves the smallest demonstrated fair counterexample order from seven to six, and gives a sharp equality condition in the natural language of block designs. It is a complete motivated extremal classification, not a selection of arbitrary finite parameters or a routine recomputation of the full model. The pair-codegree reduction exposes the reason the design optimizer is optimal and is potentially useful in larger fair-coverage classifications.

## Closest primary literature and limitations

- D. Barak-Pelleg and D. Berend, *Fano Geometry and Slow Coupon Collecting*, arXiv:2606.28216v1, https://arxiv.org/abs/2606.28216 — full paper and its mathematical results inspected; demonstrates seven-point Fano counterexample and declares the general maximum open.
- Y. Grunbaum and E. Yaakobi, *General Coverage Models: Structure, Monotonicity, and Shotgun Sequencing*, arXiv:2510.25305v1, https://arxiv.org/abs/2510.25305 — relevant full mathematical sections inspected; supplies framework, a conjecture, and bounds, not this classification.
- Public published-finding corpus records on triple packings and union-free triple systems were compared at the statement level; they concern different objectives and do not state a six-symbol coupon-coverage maximum.

The theorem concerns simple fair supports, fixed block size three and expected time; no weighted, multisupport or larger-order result is asserted. The proof is self-reviewed only. No independent validation or independent originality certification has occurred.

Self-review: passed. Independent audit: not yet performed.
