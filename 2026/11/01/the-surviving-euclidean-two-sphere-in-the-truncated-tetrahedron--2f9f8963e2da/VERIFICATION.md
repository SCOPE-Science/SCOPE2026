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

# Reproducibility and limits

Execute `python3 verify.py` with Python 3 and no external packages. The checker reads the three JSON matching certificates and rebuilds all required simplices, complete directed Forman incidence graphs, and their acyclicity. It also explicitly reconstructs the integral geometric fundamental cycle and checks the primitive map to a sphere obtained via 146 elementary free-face collapses. The expected deterministic output is included as `verification_output.txt`; success terminates with `VERIFY_OK`.

The verifier performs exhaustive **finite** proofs for these twelve vertices and stated distance classes. The topological deductions then use standard discrete Morse theory and classification of closed surfaces. It does not explore arbitrary truncated polyhedra, nor does a successful check establish publication priority or independent certification. Independent audit has not been performed.
