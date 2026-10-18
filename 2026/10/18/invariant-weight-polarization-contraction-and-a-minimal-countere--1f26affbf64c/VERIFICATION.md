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

# Exact verification and boundaries

Execute `python3 verify.py` (Python 3.9+ standard library only). The program uses `fractions.Fraction`, its own rational Gaussian elimination, and independently constructs the peer-response resolvent from the stated graph data. Its reported checks include:

- Exact positivity of all entries, row stochasticity and detailed balance for the computed response matrix on the three-person counterexample and on weighted paths, stars, and complete graphs through five vertices.
- Exact fixed-point solutions for platform susceptibilities \(0,1/20,1/10,1/2,3/4,9/10,19/20\) where applicable, with conserved stationary-weighted mean and 96 strict weighted-variance comparisons on nonconstant inputs.
- An exact increasing **ordinary** variance from \(8163/819200\) to \(4179945336867/419399996328968\) between \(\beta=0\) and \(\beta=1/20\) on the three-person path, together with the positive initial derivative \(36441/458752000\).
- Sixty-four exact identities for two-person disagreement attenuation over 16 peer-susceptibility pairs and four platform levels.

The program does **not** exhaust the infinite parameter and graph families. The general conclusions are proved analytically through the resolvent, positive-definite detailed balance and spectral decomposition, independently of those examples. The exact three-person witness is fully enumerated by rational linear algebra; no floating-point tolerance is involved. The proof does not address finite peer relaxation, directed irreversibility, or heterogeneous platform susceptibilities.
