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
# Verification

Execute `python3 check_paley25.py` beside `paley25_certificate.json`. Python 3.10+ and SymPy are required. The code reconstructs all graph edges and faces without external datasets, checks the strongly regular graph parameters and the 75 four-cliques, and checks acyclicity of two entire directed Hasse diagrams.

The primary calculation checks 93,350 faces, 583,750 covering incidences and 46,529 matched pairs, leaving 1 vertex, 246 three-cells, 45 four-cells. The signed Morse differential has 1,051 nonzero entries and Smith nonzero factors 40 ones and one five. Modular ranks are 41, 41, 40, 41, 41 for primes 2, 3, 5, 7, 11. The alternate matching retains 237 three-cells and 36 four-cells and gives 31 unit factors and one five. Its integral homology agrees. The deterministic certificate is generated using `python3 check_paley25.py --write-certificate`; normal mode compares its complete UTF-8 contents rather than trusting saved logs.

The computation is finite and exact, and the inference to a homotopy classification uses the stated CW attaching-map argument. This verification is not an independent third-party audit, does not establish uniqueness in the literature, and does not imply claims for larger Paley graphs.
