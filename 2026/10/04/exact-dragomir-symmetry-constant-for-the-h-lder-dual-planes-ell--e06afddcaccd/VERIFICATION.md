---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For a smooth \(\ell_p^2\) unit vector \(x=(a,b)\), Birkhoff--James orthogonality fixes the tangent direction \(y\) up to scale. The functional characterization of Dragomir approximate orthogonality reduces the best reverse threshold to the norm-one functional annihilating \(x\), producing the scalar factor \(c_p(u)\) in RESULT.md. For \(p=3\) and \(p=3/2\) the dual formulas coincide. With \(w=\sqrt{u(1-u)}\), the reciprocal cube is \((1+2w)(1-2w^2)\); its derivative has the unique interior maximum at \((\sqrt7-1)/6\), and substitution gives \((17+7\sqrt7)/27\). The stated \(\varepsilon_D\) follows exactly. An independent 200001-point scan of \(w\in[0,1/2]\) located the same unique maximizer and reproduced \(0.4087812568462646\), while the radical identity was checked symbolically/numerically.

## originality

PASS

The closest full primary paper proves qualitative global Dragomir approximate symmetry in every finite-dimensional Banach space and gives the functional machinery used by the audited proof, but full-text search found no \(\ell_p\) computation and no exact global constant. The earlier 2018 approximate-symmetry paper is identified by the 2020 primary source as concerning the distinct Chmieliński notion in the relevant smooth-space result. Resultary found the current exact constant and nearby but different Banach-space invariants, not a prior implication-equivalent value.

## value

PASS

The parameter is the sharp global quantitative version of a standard asymmetry question for Birkhoff--James orthogonality. Computing it exactly for a canonical smooth conjugate pair of non-Hilbert planes, and showing the extremum is genuinely interior rather than axial or diagonal, gives a meaningful benchmark for the general qualitative theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
