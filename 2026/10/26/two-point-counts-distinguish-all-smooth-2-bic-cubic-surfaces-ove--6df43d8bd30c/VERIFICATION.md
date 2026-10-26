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
# Verification protocol

Run `python3 checks/classify.py` and `python3 checks/verify.py` from the package root. Expected outputs are included in `checks/classify_output.txt` and `checks/verify_output.txt`. Each ends in `PASS`. These are executable checkers, not independent external certification. The first uses orbit closure under elementary basis transvections over \(\mathbf F_2\), the second independently constructs all invertible basis transformations and evaluates the extension-field points via explicit \(\mathbf F_4\) multiplication.

The exhaustive domain is the full \(65536\)-element coefficient set of \(4\times4\) binary matrices, restricted by exact rank to \(20160\) smooth cases, not a sample. There are ten entire congruence orbits. Numerical extension-field checks are finite and exact; they prove nothing for arbitrary finite fields, arbitrary cubic equations, or higher extensions. The point-count-isomorphism statement follows from this complete finite-domain partition plus the anticanonical embedding argument.
