# Independent audit — 2026-10-01

## Final claim

The mathematical claim is accepted after repairing one source-format control character in `RESULT.md`; no scientific statement is changed by the repair.

## Correctness — PASS

Along the positive-\(a\) vertex curve, direct symbolic elimination gives \(h'=P/(4a^2)\). Dividing the quadratic \(b\) by the affine \(a\) leaves a constant remainder \(r\) and yields \(h^{(4)}=-6r^2a_1^4/a^5\le0\) (with the stated constant-\(a\) analogue). Repeated Rolle then bounds nondegenerate stationary roots, concavity of \(h''\) excludes two minimum-type crossings, and the Hessian Schur complement gives \(\det\nabla^2f=P'/(2a)\) at a stationary vertex. Independent symbolic reconstruction returned zero for all identities; the sharp example has three feasible stationary vertices with derivative signs \(-18/25,9/25,-18/25\).

Sources checked: https://arxiv.org/abs/2609.19926.

Residual risks: The sharpness example is algebraic and is not claimed to be geometrically realizable by a physical trilinear hexahedron.

## Originality — PASS

Zhang's primary paper derives the quartic \(P\), retains up to four feasible interior roots, and explicitly says some may be saddles; its implementation reports that no concavity screening is used. The inspected paper does not state the nonpositive fourth derivative, the three-root bound, uniqueness of the minimum-capable root, or the stationary determinant formula. Published-archive and hexahedral-validation searches located no earlier equivalent screen.

Sources checked: https://arxiv.org/abs/2609.19926; https://arxiv.org/abs/1706.01613; https://doi.org/10.1145/3554920.

Residual risks: The motivating preprint is extremely recent, so unindexed contemporaneous work remains possible.

## Scientific value — PASS

The theorem is a motivated structural refinement of a newly proposed exact boundary-minimum algorithm: after the same quartic root isolation, it proves that at most one interior candidate can be minimum-capable and supplies an exact curvature test. This is a reusable theorem about the special face-polynomial class, not an arbitrary numerical slice.

Sources checked: https://arxiv.org/abs/2609.19926.

Residual risks: It reduces candidate evaluation rather than algebraic root-solving degree, so the practical speed gain is problem- and implementation-dependent.

## Disposition

Repaired and passed. The corrected `RESULT.md` changes only the malformed control character in one displayed formula; `SLOGAN.txt` is unchanged.
