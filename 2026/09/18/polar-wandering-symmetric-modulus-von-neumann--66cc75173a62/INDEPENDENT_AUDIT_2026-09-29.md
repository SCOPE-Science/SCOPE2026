# Independent audit — Polar-wandering spectral projections for symmetric moduli in von Neumann algebras

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/18/polar-wandering-symmetric-modulus-von-neumann--66cc75173a62`
**Audited tree:** `19729e7d26fcfbe312458f5982b7a2fb3c765e10`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

**PASS.** Summing the standard positive 2x2 blocks and conjugating by the polar unitary gives U*PU+Q >= 2|X| >= 2a. A nonzero vector in E intersect U*EU would make both contributing quadratic forms strictly less than a, contradicting that inequality. In a finite von Neumann algebra, modularity and unitary invariance of the center-valued dimension give 2 Tr_Z(E)<=1 and hence E is subequivalent to 1-E. When the polar unitary is a scalar multiple of a symmetry, adding the basic inequality to its conjugate yields S+VSV>=2a and the threshold doubles exactly as stated.

### Independent checks

- Verified positivity of [[|X_j^*|,X_j],[X_j^*,|X_j|]] and the conjugation that turns the summed off-diagonal block into |X|.
- Checked the open spectral intervals [0,a) for P+Q and [0,a) for S in the polar-Hermitian case are exactly what makes the quadratic-form contradictions strict.
- Verified U is unitary because X is invertible and |X^*|=V|X|V when U is a scalar multiple of the symmetry V.
- Checked the modular center-valued dimension identity on projections and the comparison equivalence Tr_Z(p)<=Tr_Z(q) iff p is Murray--von Neumann subequivalent to q in a finite von Neumann algebra.
- Checked the M_3 sharpness logic and the separate one-sided-modulus obstruction cited from the matrix source.

## Originality

**PASS.** PASS to the best of current searchable knowledge. Bourin--Lee and Aouichaoui--Lee give finite-matrix symmetric-modulus inequalities and median eigenvalue statements. Nurahemet--Ospanov extend positive-block/log-submajorization technology to tau-measurable operators, but no located source states the specific polar-wandering meet-zero relation or its center-valued half-dimension consequence.

### Literature and chronology checked

- https://arxiv.org/abs/2609.20094 — Aouichaoui--Lee, Solutions to some open problems in matrix analysis, submitted 2026-09-17; proves a finite-matrix symmetric-modulus eigenvalue inequality.
- https://arxiv.org/abs/2602.19607 — Bourin--Lee, Triangle inequalities for the operator symmetric modulus; finite-matrix symmetric-modulus inequalities and polar-Hermitian improvements.
- https://files.ele-math.com/articles/oam-17-45.pdf — Nurahemet--Ospanov (2023), On 2x2 positive matrices of tau-measurable operators; lawful open-access full text. It proves log-submajorization consequences of positive blocks in semifinite von Neumann algebras but not the audited polar-wandering/center-valued projection theorem.

## Scientific value

**PASS.** The result extracts a dimension-free projection-packing mechanism from a sharp matrix median inequality, extends it to arbitrary von Neumann algebras, and yields a genuinely center-valued statement in finite/type-II settings where ordered eigenvalue lists are unavailable.

## Limitations

- The result is a structural extension and synthesis of standard block positivity, polar decomposition, and projection comparison rather than new foundational von Neumann algebra technology.
- The center-valued half-dimension conclusion needs finiteness; only the meet-zero statement survives without that hypothesis.
- The theorem treats bounded algebra elements and not arbitrary unbounded tau-measurable summands.

## Publication guard

The current source tree on `main` matched the assignment tree `19729e7d26fcfbe312458f5982b7a2fb3c765e10` exactly during this audit. The guarded change-set records the independent-audit evidence and updates only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels are preserved unchanged.
