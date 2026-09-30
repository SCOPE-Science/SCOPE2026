# Independent Audit — 2026/09/19/auxiliary-shift-ieq-sav-monotonicity-threshold--9bfec1a7acd9

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `6e96f6476e5cc7a74cf5124de19ec1a9a50889c2`
- Disposition: **PASSED**

## Correctness

**PASS** — The homogeneous IEQ/SAV conjugacy and threshold algebra check exactly. After normalizing C0 so that epsilon^2 C0/|Omega|=c, S_n=(sqrt(V)/epsilon)Q_n and r^n=(sqrt(V)/epsilon)q^n make the two phase and auxiliary updates identical. Eliminating q^1 gives the stated rational u^1(c); symbolic differentiation confirms strict increase in c. Solving u^1=1 gives tau_*(c), whose derivative and endpoint limits agree with the record, and solving at fixed x gives the unique c_crit in the intermediate regime. The source positivity factor for the second step then makes sign(u^2-u^1)=sign(u^1(1-(u^1)^2)), so the three-region phase diagram follows. Independent symbolic algebra reproduces c_crit, and the u0=1/2, x=2 example gives c_crit=9/64 exactly.

## Originality

**PASS** — Li-Wang's current paper establishes that IEQ and SAV can generate wrong-signed increments for large steps and that strict reversals persist under small nonhomogeneous perturbations. Earlier IEQ/SAV literature discusses the auxiliary shift, consistency and accuracy, but targeted searches did not locate the exact homogeneous conjugacy after shift normalization, the closed-form monotone overshoot threshold tau_*(c), or the fixed-step shift bifurcation c_crit. The audited result is therefore a source-specific sharpening of a newly identified failure mechanism rather than a claim that shift dependence of auxiliary-variable methods is itself new.

## Scientific value

**PASS** — The result identifies the auxiliary energy shift as a genuine discrete dynamical parameter even though it is inert in the continuous gradient flow, quantifies exactly how it moves the reversal threshold, and unifies the IEQ and SAV homogeneous mechanisms. This gives a clear diagnostic for a practical method parameter and explains why larger shifts can worsen pointwise dynamical fidelity in this setting.

## Sources

- Pointwise Monotonicity of the Allen-Cahn Flow and Dynamical Limitations of Energy-Stable Schemes (Pansheng Li; Dongling Wang): https://arxiv.org/abs/2609.19023 — Primary 2026 source establishing IEQ/SAV wrong-sign pointwise increments for sufficiently large time steps.
- Efficient invariant energy quadratization and scalar auxiliary variable approaches without bounded below restriction for phase field models (Zhengguang Liu): https://arxiv.org/abs/1906.03621 — Prior auxiliary-shift/IEQ-SAV background; it does not state the audited Allen-Cahn shift phase diagram.
- Improving the accuracy and consistency of the scalar auxiliary variable (SAV) method with relaxation (Ming Jiang; Zengyan Zhang; Jia Zhao): https://doi.org/10.1016/j.jcp.2022.110954 — Prior SAV consistency/accuracy work, distinct from the exact homogeneous reversal threshold.

## Limitations

- The exact conjugacy holds only on spatially homogeneous states; away from them IEQ and SAV are different schemes.
- The sign diagram concerns the first two steps from consistent initialization and is not a global convergence or stability theorem.
- No uniform perturbation radius in the shift parameter is supplied for nonhomogeneous data.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "symbolic_derivative_checked": true,
  "critical_shift_example": "9/64"
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence; no repository write was performed. Open-access and preprint sources were checked first. No current assigned record required Oxford Download.
