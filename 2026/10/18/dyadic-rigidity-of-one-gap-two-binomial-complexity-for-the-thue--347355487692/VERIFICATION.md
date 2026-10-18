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

# Reproducibility

Run `python3 verify.py` using Python 3 standard libraries. The included complete script first performs exact symbolic enumeration of all seven cut families and their complements, obtaining twelve rational-polynomial profiles in each parity. It then verifies for every pair of different profiles that at least one coordinate difference retains a nonzero sign on the full real half-line \(h\ge4\), by expanding in \(h-4\) and checking coefficient signs. This is a finite exact-algebra certificate of the no-collision step, not sampling at finitely many dyadic lengths.

Next, the program directly counts all allowed non-adjacent selected index pairs in all four families of substituted-word cuts at lengths \(8,16,32,64,128\), and agrees exactly with the symbolic candidates. Finally it enumerates consecutive factors of longer Thue–Morse prefixes at lengths \(8,16,32,64\) and agrees with the cuts. The last two checks are finite checks, not an infinite proof. The infinite argument also requires the mathematical exhaustiveness and reachability proof stated in `RESULT.md`. No independent audit or formal proof certification has occurred.
