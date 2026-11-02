---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

The companion `checker.py` is a self-contained Python 3 program requiring only standard-library modules. Execute `python checker.py` in the same directory. During preparation it returned:

```
PASS 12252 exact or precision-tested assertions; all critical thresholds and density comparisons passed.
```

The exact-arithmetic part enumerates all admissible three-component Fourier exponent triples for \(N=3M\), \(1\le M\le35\); verifies the multiplicity equals the classical Eisenstein divisor count for all \(m<m_*(M)\); and checks that the count is strictly smaller at the constructed first clipped value \(m_*(M)\). The numerical part checks the circular-segment CDF against finite-shell eigenvalue counts for \(N=300,600,1200\) at seven test points each and checks the asymptotic square-root density coefficient at three positive offsets.

Every finite test is supplementary. The infinite-dimensional claims depend on the mathematical arguments in `RESULT.md`, specifically the prime-decomposition count, the sharp first-excluded lattice-point proof, and the uniform bounded-perimeter discretization argument. The arithmetical divisor formula is classical. Historical priority remains provisional, and no separate independent audit or external validation has been performed.
