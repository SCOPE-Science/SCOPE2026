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

# Verification and limits

The standalone C++17 exact census visits every rank-two multiset of sign-normalized columns at lengths two through six and compares entire dual Lee enumerators within each primal Lee enumerator class. The exhaustive counts are 60, 400, 1735, 6067, and 18401 multisets. Counts independently follow from a closed stars-and-bars subtraction, so no unseen representative class is omitted. The exact dual transform uses the quadratic integer ring with relation \(\alpha^2=1-\alpha\), explicitly asserts zero quadratic-field irrational component in each coefficient, and checks integer divisibility by 25. Every primal group has a unique dual spectrum until length seven. The discovered witness has equal primal spectra but different dual Lee-weight-four counts (56 and 60).

An independently implemented direct enumeration over all \(5^7\) vectors, with no Fourier products, reproduces both full dual enumerators (3125 codewords apiece). The observed computations are exact finite certificates for the classification through six; they do not imply an infinite-length result, a result for higher-dimensional codes, or mathematical priority over inaccessible literature.

Rerun with the source files `lee_exact_census.cpp` and `lee_direct_witness.py`. Expected terminal tags and output are reproduced in `checks.txt`.
