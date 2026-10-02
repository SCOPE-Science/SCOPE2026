# Independent audit — A one-parameter maximal-rank family with a rank-two middle summand

Audit date: 2026-10-01 (UTC) UTC

Final disposition: **PASSED**

## Correctness — PASS

Fresh symbolic algebra verifies \(B^2-4AC=64(u^2+3)^3\), both conjugate cube identities and both displayed sections. The third-summand condition reduces to \(Y^2=X^3+16\); the inspected LMFDB entry 27.a4 has rank zero and torsion \(\mathbb Z/3\mathbb Z\), leaving only excluded \(u=\pm1\). Bao's stated criteria then give ranks \((1,2,0)\).

## Originality — PASS

Bao gives the general rank formula, while a related same-day SCOPE record only classifies possible rank-three mechanisms and notes an isolated \((1,2,0)\) example. Resultary searches found no prior parameterized family equivalent to the one audited here.

### equivalent_formulations

Compared the actual coefficients and (1,2,0) decomposition.

Evidence: No equivalent one-parameter coefficient family found.

### broader_coverage

Neither inspected source states this explicit rational family.

Evidence: Bao supplies the general formula and an isolated mechanism; the sibling record classifies mechanisms.

### exact_database_or_table

The family is not a table recomputation.

Evidence: LMFDB supplies only the auxiliary Mordell curve data.

### claim_vs_prior_implication

No prior statement inspected implies the exact family.

Evidence: General criteria require a nontrivial parameterization and global exclusion argument to obtain this family.

## Source inspections


- **Bao's rank formula for the elliptic-curve family** (arXiv:2609.16349): PRIMARY_GENERAL_FORMULA. Material read: arXiv abstract; direct full-text and institutional fallback attempts failed. Evidence: Abstract states an explicit rank formula and generators for all curves in this class.

- **Rank-three mechanism obstruction and a correction to Bao's Example 6.3** (Resultary 2026/9/18/SCOPE-rank-three-mechanism-obstruction-j0-elliptic-surfaces--5cc1d9554668): RELATED_NOT_COVERING. Material read: complete RESULT.md. Evidence: Identifies (1,2,0) as a possible mechanism and discusses Bao's isolated example, but does not give this family.

- **LMFDB elliptic curve 27.a4** (LMFDB 27.a4): SUPPORTS_AUXILIARY_EXCLUSION. Material read: curve properties, simplified model, Mordell–Weil rank and torsion. Evidence: Rank zero and torsion group Z/3Z for the simplified Mordell model.


## Scientific value — PASS

Turning an isolated maximal-rank mechanism into an explicit infinite rational family with a global Mordell-curve obstruction is a natural reusable construction in the newly classified parameter space.

## Residual risks and limitations


- Bao's full preprint could not be retrieved through the available full-text routes, so Example 6.4 could not be reread directly. The primary abstract, LMFDB data and complete same-day SCOPE comparison were inspected.
