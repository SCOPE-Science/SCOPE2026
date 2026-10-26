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

# Reproduction checks

Execute `python3 verify.py` with Python 3.8 or newer. The script uses only standard-library data structures. No generated third-party data, files, network connection, probabilistic trials, or external solver are required.

The script directly computes the binary Rudin–Shapiro symbols by counting overlapping adjacent `11` bits and independently obtains the same \(65{,}536\)-symbol prefix from the four-letter substitution. It constructs the complete eight-element two-letter language by an exhaustive substitution-closure algorithm, enumerates all 64 length-eight windows within the eight length-sixteen source-pair images, and confirms the even/odd parity factor sets have sizes 24 and 32 with no intersection.

For powers of two \(B=8,16,\ldots,1024\), it checks the exact dyadic five-block identities, verifies pairwise distinctness of all \(4B\) length-\(B+1\) factors beginning at indices below \(4B\), and verifies the length-\(B+1\) copy at \(4B\). It determines the first collision and earlier position directly for every length from 1 through 384, agreeing with the displayed formula. These finite reproductions corroborate the arithmetic and exhaustive certificate; the all-length conclusion is established in `RESULT.md` by the substitution congruence and block argument.

The work has not been subjected to an external independent audit; historical-priority assessment remains limited by the accessible prior literature.
