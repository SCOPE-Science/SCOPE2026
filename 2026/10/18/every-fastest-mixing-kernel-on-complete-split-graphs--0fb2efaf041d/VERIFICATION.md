---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Averaging under S_r x S_s gives optimal average cross x, with unique minimizer of max(1-ra,(r+s)a-1); for s<=2r Rayleigh saturation of between-block contrast and independent differences forces B=xJ, and for s>2r capacity saturation plus the independent-block compression trace forces B=xJ and A=0. Block eigenvalues reduce the entire optimizer face to A1=c1 and spectrum(A|U_r) inside [-mu,mu]; trace and nonnegative diagonal bound exact T interval attained by invariant core. Independent numeric eigenvalue endpoints at (r,s)=(2,3),(3,2),(3,6),(2,7) confirm all phases; finite checks do not prove all sizes.

## originality

PASS

Statement-level best-of-knowledge check: Complete split joins, star clique lifts, FMMC symmetric semidefinite optimal face and optimizer equality conditions searched. Jafarizadeh clique-lift reduction dominates scalar optimum and yields invariant construction but inspected statement does not classify every non-invariant optimum. Optimal value and a constructed symmetric lift cannot determine the full set of all optimizers; Rayleigh equality and trace-saturation proof yield the added universal rigidity.

## value

PASS

Characterizes all optimal reversible uniform-stationary kernels rather than an optimal value or single construction, making symmetry rigidity, optimizer nonuniqueness, internal-edge usage, and phase transitions exact and useful in fastest-mixing design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
