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

# Verification of the square-zero alternating-matrix rank formula

Execute `python3 verify.py`. The script constructs every symmetric zero-diagonal matrix over the indicated small even fields from upper-triangular coordinates; it separately computes the full square, row-echelon rank, and predicted fiber count. It uses exact polynomial-basis arithmetic for \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\). It exhausts sizes \(2\) through \(6\) over \(\mathbb F_2\), \(2\) through \(4\) over \(\mathbb F_4\), and \(2\) through \(3\) over \(\mathbb F_8\). It also checks closed-form support through size \(16\) for all three fields. Expected terminal marker: `VERIFY_OK_ALTERNATING_SQUAREZERO_CHAR2`.

Compile `verify.cpp` with `g++ -O2 -std=c++17 verify.cpp -o verifybin` and execute `./verifybin`. An independent implementation enumerates all alternating matrices of size seven over \(\mathbb F_2\), size five over \(\mathbb F_4\), and size four over \(\mathbb F_8\). Expected terminal marker: `VERIFY_OK_ALTERNATING_SQUAREZERO_CPP`.

Representative exact counts by rank are \(\{0:1,2:3\}\) for size four over \(\mathbb F_2\), \(\{0:1,2:75\}\) for size six over \(\mathbb F_2\), \(\{0:1,2:315\}\) for size seven over \(\mathbb F_2\), \(\{0:1,2:255\}\) for size five over \(\mathbb F_4\), and \(\{0:1,2:63\}\) for size four over \(\mathbb F_8\).

The finite checks are not a certificate for unbounded \(n\) or untested fields. The proof uses the isotropic-image/alternating-form bijection and exact subspace counts. No external certification or independent audit has been carried out.
