# Self-review

## Correctness — PASS

The ordinal chain's least open neighbourhood is exactly its initial segment. Hence infinite accumulation is decided by counting the points of a set below each ordinal. The first \(\omega\) elements of every infinite subset give a unique limiting threshold, and all images are tails. The proof then shows that taking one more derivative advances a tail threshold by ordinal addition of \(\omega\), while limit iterates intersect tails by taking the supremum of thresholds. This verifies every displayed formula, including noncommutativity of ordinal multiplication and the base stage. The precise removal stage of a point and the least ordinal realizing a given rank follow from strict monotonicity and continuity of left multiplication by \(\omega\) in its right factor.

`checker.py` independently evaluated the finite \(m\)-point analogue on 12,282 labelled subset cases (147,450 derivative comparisons) and 1,100 finite rank cases; it returned `ALL_CHECKS_OK`. These tests do not establish the infinite or transfinite statements, for which the symbolic induction is indispensable. Boundary cases \(\theta=0\), finite \(\theta\), \(\theta=\omega\), empty sets and first-infinite-block thresholds equal to \(\theta\) are expressly covered.

## Originality — PASS within inspected evidence

Yoàv Montacute's *Halo Semantics for Modal Logic* (arXiv:2606.31885v1, §§4, 6.1–6.3, conclusion) was read in its accessible full-text version. Its Theorem 6.4 proves the halo-to-accumulation identification and Theorem 6.14 constructs a general transfinite decomposition. It does not give the arbitrary-subset first-\(\omega\)-block form on Alexandrov ordinal chains, the exact pointwise transfinite tail formula, the rank \(\min\{\gamma:\omega\gamma\ge\theta\}\), or the least-order-type realizations. These computations are not entailed by a merely existential decomposition without the chain-specific neighbourhood reduction and ordinal arithmetic.

Classical Hausdorff ordinal Cantor–Bendixson ranks and their countable spectrum are recognized prior art. The result is not a new proof of that general spectrum: it concerns the *different*, non-\(T_1\), initial-segment Alexandrov topology and a full normal form for arbitrary valuations. Published research-record searches using halo, ordinal chain, infinite-accumulation, and condensation/rank terminology located no mathematical statement dominating this one. The closest related records describe the indiscrete halo logic and ordinary Cantor–Bendixson ranks of unary-function type spaces; neither implies the presented formula. A historical source describing the same initial-segment topology under a different name could still predate this computation; the search does not prove absolute priority.

## Mathematical value — PASS

The 2026 infinite-accumulation modality makes a general transfinite decomposition available but does not quantify how long it lasts on concrete non-Hausdorff spaces. The new exact normal form answers that natural rank question for **every** ordinal in a canonical Alexandrov chain class and **every** valuation. It gives all point-removal stages, proves no fixed countable ordinal bounds the ranks of countable such spaces, and identifies the least order types for each rank. These are precise calibration examples for \(\omega\)-scattered topological modal semantics, not isolated small-order experiments. The elementary order-statistic ingredient is acknowledged; the value lies in the complete transfinite classification and sharp canonical realizations.

## Closest literature and limitations

Primary source: Montacute (2026), Theorems 6.4 and 6.14. Background: classical Cantor–Bendixson theory of Hausdorff ordinal spaces; other published research records on purely nonstandard halo logic and ordinary type-space ranks. The calculation applies to ordinal initial-segment Alexandrov topologies; it does not classify arbitrary infinite Alexandrov spaces or provide new general modal completeness axioms. The finite checker validates only a threshold analogue. Older equivalent formulations remain a priority risk.

Self-review: passed. Independent audit: not yet performed.
