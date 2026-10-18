---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Periodic recurrence x_{k+1}+x_{k-1}=1+|x_k| is equivalent for each of all 2^p sign words to an affine rational system with closed sign inequalities, including zero coordinates. Exact Gaussian elimination handles regular and singular systems; rational Fourier–Motzkin elimination decides every affine feasible cell. The script actually enumerates all p<=11 and classifies feasible singular cells; independently written linear solving plus LP feasibility reproduced all 11 feasible word counts and all primitive isolated orbit counts. Strict nonzero coordinates of enumerated 5-/11-cycles allow exact derivative products with stated traces. No claim is made beyond period 11 or that all period-six cycles are isolated.

## originality

PASS

The 2009 Abu-Saris–Al-Jubouri primary 9-page paper treats this exact α=1,β=-1,γ=1 special case but proves generic periodicity conditions, minimal periods 2/3 and global-all-orbit conditions; it does not enumerate p=5..11. MathWorld presents one period-five orbit in five outer hexagonal regions; the independently verified second hyperbolic five-orbit lies outside that restricted picture. The original Devaney 1984 article could not be materially read; the possibility of historical exact short-period data remains a residual risk. Best-of-knowledge original for the complete global <=11 rational sign-word census.

## value

PASS

Determining exactly which short least periods and how many isolated prime-five and -eleven cycles occur in an iconic piecewise-affine planar map is a natural complete finite classification. The elliptic/hyperbolic return derivatives distinguish genuine dynamical structures, and exact sign-boundary feasibility makes the finite result meaningful rather than a partial experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
