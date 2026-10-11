---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The field-trace identity gives the displayed cubic phase, and the nonidentity Pauli expectations reduce to nondegenerate quadratic Gauss sums of magnitude \(d\), yielding the stated stabilizer purity. For entanglement, removing row phases leaves the coefficient matrix \(d^{-1}\omega^{cxy^2}\). Its Gram matrix is circulant; additive Fourier diagonalization gives eigenvalue \(d^{-1}\#\{y:cy^2=k\}\), which is one root at zero, two roots for half the nonzero frequencies and no roots for the rest. Fresh independent numerical diagonalization at \(d=5,7,11\) reproduced exactly the predicted multiplicities.

## originality

PASS

The cubic Alltop family and its mutually unbiased-basis role are prior art, and the recent maximal-magic work supplies the relevant magic-value context. Best-of-knowledge novelty is restricted to the exact bipartite Schmidt spectrum for the natural \(\mathbf F_{d^2}\cong\mathbf F_d^2\) tensor factorization. Resultary searches returned no independent all-prime spectrum formula. The complete Knipfer et al. body was not accessible through the open route, and an authorized institutional fallback attempt was safety-blocked and not retried; that remains a residual risk rather than a failure.

## value

PASS

The exact spectrum supplies a dimension-uniform entanglement structure for a canonical infinite Alltop family realizing the known magic benchmark. It explains a concrete rank and entropy stratum and is a natural structural invariant for comparing higher-dimensional magic candidates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
