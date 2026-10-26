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

The proof is mathematical and covers every \(n\ge1\). The included standalone Python 3 script `verify.py` implements two independent finite enumerations: enumerate all three-symbol words with adjacent symbols distinct for \(1\le n\le13\), and enumerate all six-arc multiplicity vectors of total weight \(0\le e\le12\) using the elementary directed Euler-trail criterion. Both count 2-abelian observation classes and compare with direct coefficient extraction of the stated rational generating function.

Run `python3 verify.py`. Expected output: `TERNARY_HOMOPOLYMER_FREE_2ABELIAN_PASS brute_lengths=1..13 euler_arc_totals=0..12`.

These finite checks do not establish the all-length theorem independently of its proof. The constant-word boundary (\(n=1\)), the even-length two-vertex balanced support correction, and one-start open trails are handled explicitly. Completeness of literature and independent external validation are not claimed.
