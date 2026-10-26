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

# Verification of the commuting-variety transition

Run `python3 verify.py` from this package directory. The verifier uses standard-library finite arithmetic and does not need a network connection. It tests both relevant exterior degrees by constructing literal wedge-multiplication matrices over \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\), with 80 seeded samples of each of the two ranks for each generator count. It also tests the exact three-stratum cardinality identities, the nondegenerate \(20\)-dimensional six-generator middle wedge pairing, and 80 seeded singularity checks for each five-generator alternating map. Expected output: `VERIFY_OK_EXTERIOR_COMMUTING_COMPONENT_TRANSITION`.

The verifier cannot establish that an algebraic variety is irreducible. The proof uses explicit one-parameter degenerations, a vector-bundle description on an open chart, and the irreducibility of a quadratic hypersurface of polar rank \(40\). The tests cover prime finite fields, while the proofs cover all odd-characteristic fields and all odd prime-power field sizes. Lower-dimensional or embedded scheme-theoretic structure is not asserted.
