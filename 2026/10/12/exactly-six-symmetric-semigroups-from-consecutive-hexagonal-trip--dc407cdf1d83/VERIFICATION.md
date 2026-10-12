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

# Verification record

Run `python3 verify.py` with Python 3's standard library. The program uses no input files or external packages and prints `EXACT_CERTIFICATE_OK indices=2,3,6,7,8,18 checked=2..60 independent_apery=59 oeis_F=29 universal_cutoff=61` before listing the five genuine three-generator witness certificates and the two-generator special case.

The exact finite check loops over all 59 indices from 2 through 60. Each candidate pair is tested with its integer gcd; for every factorization under consideration, it loops over all possible nonnegative first coefficients, determines the second coefficient by divisibility, and concludes membership or nonmembership without heuristic truncation. Separately, Dijkstra's shortest paths on the residue graph modulo the smallest generator obtain the complete Apéry set, yielding exact Frobenius number and genus for every one of the 59 indices. The first 29 Frobenius numbers reproduce OEIS A069758. In both independent tests precisely indices 2,3,6,7,8,18 satisfy symmetry. The n=3 case uses the two-generator reduction rather than the three-minimal-generator criterion.

To verify the infinite step, use the elementary gcd identities and inspect the strict inequalities at n=61: the four positive polynomials in the proof are increasing on [61, infinity). The g=3 pair tests are impossible by the two adjacent integer bounds; in the g<=30 case any factorization forces x+y=g and x=g/2+g/(4n+3), which cannot be integral. The finite checker verifies relevant boundary inequalities but cannot certify infinitely many values on its own; that is done algebraically in the proof.

There has been no independent external audit, no Lean verification, and no assertion that finite source searches establish publication priority.
