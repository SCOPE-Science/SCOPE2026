# Independent Audit — 2026-09-29

**Record:** `2026/09/12/012`  
**Title:** Sharp local (non-)unimodularity dichotomy at isolated rank-zero points in dimension 4  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `938581d5d3bbc28fcffc6fcf1ce7ccbdf20f78e8`  
**Disposition:** **PASSED**

## Independent checks

- Recomputed the conformal modular vector field and jet obstruction symbolically.
- Recomputed the Jacobian bivector, its sum-of-squares isolation identity, Casimir rank bound, and zero divergence.
- Checked the isolated-zero flow-fixing argument directly from preservation of the Poisson tensor.

## Three-axis assessment

- **Correctness — PASS**: Both local models check out. For pi_c=|x|^2 d1∧d2, the modular vector field has nonzero linear part (-2x2,2x1,0,0) while every Hamiltonian field is divisible by |x|^2, so the modular class cannot be Hamiltonian. For the Jacobian bracket from the two stated quadratic Casimirs, pi^13+pi^24=|x|^2, the bracket has rank exactly two off the origin, and direct divergence is zero. The flow argument that a Poisson vector field fixes an isolated zero is also correct.
- **Originality — LIMITED**: Jacobian Poisson structures are known to be unimodular, and the conformal example/jets give an elementary complementary obstruction. The contribution is the explicit juxtaposition tailored to the admitted local question, not a broad new modular-class theorem.
- **Scientific value — PASS**: The pair of explicit germs correctly demonstrates that isolated rank-zero plus punctured rank-two data do not determine local unimodularity in the degenerate 1-jet stratum. This is useful for ruling out an overbroad local route to the compact nondegenerate target.

## Findings

- The current record tree exactly matches the assigned tree SHA.
- Independent symbolic recomputation gives X_mod(pi_c)=(-2x2,2x1,0,0).
- For the Jacobian bracket, independent expansion gives pi^13+pi^24=x1^2+x2^2+x3^2+x4^2 and identically zero modular divergence.
- The record explicitly limits itself to the degenerate vanishing-1-jet stratum and does not claim resolution of the compact nondegenerate problem.
- The repository's `output/artifacts/...` path is stale; the packaged checker is `artifacts/verify.py`, which is a reproducibility-path issue rather than a scientific defect.

## Sources compared

- Kosmann-Schwarzbach, Poisson Manifolds, Lie Algebroids, Modular Classes: a Survey: https://sigma-journal.com/2008/005/ — Standard reference for modular vector fields/classes and unimodularity.
- Ortenzi–Rubtsov–Tagne Pelap, Integer solutions and H-invariant Jacobian Poisson structures: https://arxiv.org/abs/1103.4267 — Provides Jacobian-Poisson context; Jacobian structures are standard unimodular examples.

## Limitations

- The examples have vanishing linearization and therefore do not settle the compact target with a nondegenerate rank-zero point.
- No compactification with exactly one singular point is constructed.

This audit is independent of the repository's pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
