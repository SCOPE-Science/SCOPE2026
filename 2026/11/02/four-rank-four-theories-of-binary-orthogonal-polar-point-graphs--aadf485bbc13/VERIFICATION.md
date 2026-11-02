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

# Reproduction and limits

Both programs operate only on exact integers. Run the following from their directory:

```bash
python3 verify_orthogonal_types.py
python3 verify_orthogonal_direct.py
```

The first program represents each tuple by the first-independent basis, the binary-coordinate words of selected vertices and their quadratic Gram matrix. It computes complete rank-three and rank-four first-order tuple types recursively from all allowable one-vertex extensions. The allowance test uses the exact binary quadratic Gauss sum. The outputs establish exactly two rank-three and four rank-four types for representative dimensions \(r=2,\ldots,8\) and both Arf signs. The stated inequality proves the uniform extension property for every \(r\ge5\), not just the computed range.

The second program independently constructs the full singular point set and checks every possible extension type from every abstract tuple orbit of length at most three, for both signs in dimensions four, six and eight. It also checks vertex counts and the three explicit four-vertex separators. The expected successful terminal markers are \`FOUR_ROUND_CLASSIFICATION_OK\`, \`DIRECT_VERIFY_OK\`, and \`VERIFY_OK\`. The combined observed output is embedded as \`verification_output.txt\`.

These computations independently check the finite boundary construction but do not replace a mathematical proof of the large-rank statement. The historical originality assessment is not an exhaustive mathematical literature audit.
