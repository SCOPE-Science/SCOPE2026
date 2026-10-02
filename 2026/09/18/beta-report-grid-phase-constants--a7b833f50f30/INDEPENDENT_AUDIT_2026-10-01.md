# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-a7b833f50f30`

## Correctness — PASS

After the likelihood-coordinate change, the null and alternative are exponential with rates 1 and \(\theta\), so regular-cell likelihood ratios strictly decrease with the cell index. The oracle boundary crosses exactly the two stated lattice diagonals, giving the exact null and alternative boundary masses and the two Neyman--Pearson randomization formulas. Independent symbolic expansion of those formulas reproduces the two branches of \(\Phi(\rho)\) and the common coefficient \(1/24\) at \(\rho=1/2\). The committed deterministic evaluator was read completely; its finite-resolution values converge to the same limiting constant and phase curve. The factor-four comparison is only within the specified log-evidence lattice family, exactly as claimed.

### Correctness sources

- research package RESULT.md
- artifacts/verify.py and artifacts/verification.txt
- Dubey--Huo arXiv:2609.19708
- independent symbolic Taylor expansion of both exact deficit branches

### Correctness residual risks

- The theorem does not optimize over all measurable report partitions.
- The finite evaluator uses floating arithmetic, but the accepted leading coefficient was independently derived symbolically from the exact formulas.

## Originality — PASS

Dubey and Huo prove the optimal inverse-square loss exponent and report grid-alignment behavior for equal-width reports, while classical high-rate quantization theory gives general second-order mechanisms. Fresh Resultary and literature searches found no source giving the audited exact two-boundary-diagonal formulas, the piecewise phase function \(\Phi\), the universal half-cell minimizer, or the factor-four leading-constant improvement for this two-site Beta fixed-level problem.

### equivalent_formulations

Searches:
- Resultary: two-site Beta report quantization phase constant half-cell
- arXiv:2609.19708 grid alignment
- shifted/offset Neyman--Pearson quantizer phase

Evidence:
- The exact semantic match was the audited record.
- The motivating paper's abstract states inverse-square optimal loss and the two-site Beta benchmarks, not the phase constant.

Reasoning:
Equivalent formulations in p-value coordinates and exponential likelihood coordinates were compared; the phase law is the same claim after the monotone coordinate change.

### broader_coverage

Searches:
- Poor 1988 fine quantization
- Goyal--Hero 2003 high-rate detection quantization
- Villard--Bianchi 2010 Neyman--Pearson high-rate quantization

Evidence:
- These works provide broad asymptotic quantization frameworks, not the exact finite boundary decomposition or this phase optimizer.

Reasoning:
General second-order asymptotics do not mechanically determine the lattice-alignment function without the instance-specific boundary calculation.

### exact_database_or_table

Searches:
- Resultary exact search and source numerical benchmark tables

Evidence:
- No existing table was found that already contains the phase curve or exact finite-L formula.

Reasoning:
The package produces values from a derived closed formula rather than recomputing a known table.

### claim_vs_prior_implication

Searches:
- claim versus Dubey--Huo inverse-square theorem
- claim versus general high-rate detection formulas

Evidence:
- Prior results establish the rate order, not the phase-dependent leading coefficient or theta-independent optimizer.

Reasoning:
The audited exact coefficient is additional information not implied by the published order bound alone.

### source_inspections
- **Report resolution in federated multiple testing under family-wise error control** — https://arxiv.org/abs/2609.19708. Trigger: Direct motivating source and same Beta benchmark. Material read: Current primary abstract/theorem scope. Method: Primary-source scope comparison. Assessment: Covers the globally optimal inverse-square exponent and finite Beta examples, not the audited grid-phase law. Evidence: The abstract states inverse-square decay and equal-width attainment of the order, without a phase-dependent leading constant.
- **Assigned exact phase evaluator** — artifacts/verify.py. Trigger: Finite-resolution numerical corroboration. Material read: Complete source and recorded output. Method: Line-by-line inspection plus independent symbolic expansion of the exact formulas in RESULT.md. Assessment: Numerical values and phase convergence are consistent with the exact symbolic theorem. Evidence: The reported half-phase scaled deficits approach the stated limit and the phase samples approach \(\Phi(\rho)\).

### checked_sources

- https://arxiv.org/abs/2609.19708
- https://doi.org/10.1109/18.21219
- https://doi.org/10.1109/TIT.2003.814482
- https://arxiv.org/abs/1004.5529
- research package RESULT.md and artifacts/verify.py
- fresh Resultary semantic search

### residual_risks

- A specialized quantization paper using an equivalent shifted-lattice normalization could have been missed, though no such source was located.
- The motivating paper is very recent, so follow-up overlap risk is nontrivial.

## Scientific value — PASS

The exact leading constant is motivated by a published inverse-square quantization theorem and observed grid-alignment oscillations. The result explains those oscillations analytically and identifies a phase choice that uniformly cuts the leading loss by a factor of four within a natural likelihood lattice, giving a precise benchmark a future report-design analysis can reuse.

### Value sources

- Dubey--Huo report-resolution theorem and Beta benchmark
- classical high-rate detection quantization
- research package exact phase law

### Value residual risks

- The result is deliberately family-optimal rather than globally optimal over all report partitions.

## Limitations

- One hypothesis and two homogeneous sites only.
- Phase optimality is within the displayed equal-step log-evidence lattice family.
- The report-space test may randomize at the final likelihood-ratio atom.
- Originality is best-of-knowledge.

## Disposition

**PASSED**
