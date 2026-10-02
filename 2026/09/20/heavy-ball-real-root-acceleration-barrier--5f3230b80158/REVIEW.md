# Review status

Fresh mathematical audit completed on 2026-10-01 UTC.

Scientific disposition: **passed**.

- Correctness: **PASS.** With \(t=\sqrt\beta\), the all-real-root condition is exactly \(|s_\lambda|\ge2t\) for every \(\lambda\). Since \(s_\lambda\) is an affine decreasing interval, it must lie wholly in the positive branch \(s_L\ge2t\) or the negative branch \(s_\mu\le-2t\). On the positive branch, the worst root is at \(\mu\) and the best admissible step is \((1-t)^2/L\); direct polynomial evaluation shows its factor is strictly larger than \(1-\mu/L\) for every \(t>0\). On the negative branch, evaluating the magnitude polynomial at \(q=(L-\mu)/(L+\mu)\) shows the larger root is strictly above \(q\) for every \(t>0\). The \(t=0\) minimax problem gives unique equality at \(\alpha=2/(L+\mu)\). The nonnegative-root frontier follows from the same positive branch. The package replay independently checks representative condition numbers and the Polyak endpoint/interior root pattern.
- Originality: **PASS.** Classical and modern heavy-ball sources analyze optimal parameters, critical damping, and real/complex root regimes. The inspected Hagedorn–Jarre full text gives the modal spectral-radius formulas and treats real versus complex discriminants, but no inspected source states the constrained interval minimax theorem that an all-real-root tuning cannot beat optimal fixed-step gradient descent, nor the exact nonnegative-root frontier.
- Scientific value: **PASS.** The theorem gives a sharp structural boundary between overdamped/all-real interval tuning and robust acceleration, including the unique equality case and a stronger nonnegative-root frontier. This is a natural classification with direct interpretation for fixed-parameter quadratic optimization.

Detailed evidence is recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and
`INDEPENDENT_AUDIT_2026-10-01.json`. Earlier scientific review rationales are
preserved in `AUDIT.json` as prior review evidence and are not used as substitutes
for this fresh audit.
