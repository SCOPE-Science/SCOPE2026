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

The package contains `verify_paley.py`, `verification_output.txt`, `independent_check.py`, and `independent_output.txt`. These are ordinary reproducible programs and records, not independent mathematical certification. Running each script with Python 3's standard library and comparing standard output to the corresponding embedded record reproduced both outputs byte-for-byte.

The main program enumerates every odd prime power \(q\equiv1\pmod4\) below \(241\), builds the finite field, certifies extension-polynomial irreducibility, verifies graph symmetry and quadratic-residue cardinality, and checks every normalized quadruple \(\{0,1,a,b\}\) with all sixteen adjacency patterns. The output includes all exact minimum witness counts and the first attaining configuration in field-coordinate encoding. The independent program uses quadratic-character exponentiation and direct pattern histograms at nine field orders that include the sharp boundary and exceptional-order cases.

The infinite \(q\ge241\) assertion is not based on experiments. Its character-sum lower bound is derived in `RESULT.md`: six quadratic pair terms contribute at most six, four cubic terms at most \(8\sqrt q\), the quartic term at most \(3\sqrt q\), and four excluded anchor terms at most thirty-two. Hence every pattern has more than two witnesses once \(q\ge241\). The irreducible-polynomial and all-pattern checks are executed by the supplied program; the mathematical proof of completeness of affine normalization is written in `RESULT.md`.

Limitations: finite enumeration is exhaustive only in the finite interval stated; a failed computation is never interpreted as an infinite impossibility proof. Historical priority is qualified because the full 1993 Ananchuen–Caccetta article was inaccessible, although its abstract and a full relevant thesis discussion were compared. No independent external audit was conducted.
