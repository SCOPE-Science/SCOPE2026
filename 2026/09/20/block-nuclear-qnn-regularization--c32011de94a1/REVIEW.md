# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Scientific disposition: **passed**.

- Correctness: **PASS.** The block-nuclear lower bound was reconstructed atom by atom. Each signed neuron contributes a rank-one block with nuclear norm \(2|\alpha|\) and a quadratic block with nuclear norm \(|\alpha|\), giving \(R\ge\Omega\). Dualizing the off-diagonal block yields \(\Omega\ge\|z\|_2\). Pure quadratic and pure linear axes realize the nuclear and Euclidean norms exactly; for aligned rank-one aggregates the two signed atoms give \(R=\max\{|s|,|t|\}\). For orthogonal rank-one data, the three-atom construction has cost \((S^2+2ST+2T^2)/(S+2T)\), and an independently re-derived feasible quadratic dual polynomial attains the same value. The committed numerical script is only corroborative.
- Originality: **PASS.** The complete motivating preprint was inspected. It gives separate nuclear/Euclidean lower bounds and a regularized least-squares surrogate, but not the full block-nuclear bound or the exact induced atomic norms on the aligned and orthogonal families.
- Scientific value: **PASS.** The result strengthens a current QNN regularization bound and computes exact induced regularizers on natural low-rank families, including a strict gap example. These formulas clarify what the convex relaxation actually penalizes and are mathematically reusable.

Detailed evidence is recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and
`INDEPENDENT_AUDIT_2026-10-01.json`. Earlier review evidence remains historical
evidence and is not relabeled as independent verification.
