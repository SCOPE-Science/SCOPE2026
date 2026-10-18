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
# Reproducible finite verification

Run `python3 verify_shrikhande_equivariant.py` with a standard Python 3 interpreter from the folder containing the supplied files. No packages or network resources are required. The source reconstructs the exact Shrikhande Cayley graph, enumerates all 65,536 vertex masks, and checks the face counts \((16,72,96,16)\). Over \(\mathbb F_2\), it evaluates every degree-two and degree-three boundary column and obtains ranks \(57\) and \(16\), which force the rational ranks by the chain inequality.

It constructs all twelve origin-stabilizing matrices and sixteen translations, verifies all \(192\) distinct graph automorphisms, and uses the six-cycle neighbor structure to prove no additional graph automorphisms exist. It evaluates each homology trace twice: by oriented fixed simplices, and by independent collections of vertex-permutation cycles. Both exact algorithms agree for each group element. The rational character is then decomposed by exact integer Gaussian Fourier sums, with each of four stabilizer characters asserted explicitly; the final marker is `SHRIKHANDE_EQUIVARIANT_VERIFY_OK`.

The assertions were executed successfully from `verify_shrikhande_equivariant.py`. A separate replay after its final source edits confirmed the same exact character rows, and `CHARACTER_TABLE.txt` was checked against the actual output. No approximate floating-point rank or finite-sampling inference is used. The claims are specifically rational homology and complex irreducible decompositions; the code does not constitute independent external verification.
