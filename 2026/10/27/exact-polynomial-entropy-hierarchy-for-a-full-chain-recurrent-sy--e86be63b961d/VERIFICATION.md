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

# Verification of the exact polynomial-entropy hierarchy

The package contains the complete analytical proof in `RESULT.md`, executable finite combinatorial checker `checker.py`, and the exact output `checker_output.txt` from running the checker under Python 3. The six required documents and two reproducibility artifacts are embedded in full.

The checker verifies for each integer window length from \(1\) through \(14\) that the language with at most two symbol changes has exactly \(L^2-L+2\) words. It then constructs explicit two-interface finite-block configurations with independently selected event times, for \(n=1,2,3,4\), and tests every pair in each finite family. The families contain respectively \(4,16,64,256\) configurations; pair counts are \(6,120,2016,32640\).

This test exercises the key interface-separation combinatorics but does not establish the estimates for arbitrary time horizons, arbitrary \(n\), or arbitrary compatible quotient metrics. Those assertions are obtained analytically from uniform continuity, fixed positive separation between the quotient point and the two step configurations, and \(2n\) disjoint linear-size marker windows. The quotient-suspension proof additionally uses that a passing \(n\)-point configuration retains one nontrivial interface state and at least one point near the identified constant point for \(n\ge2\).

No numerical extrapolation is treated as an infinite proof. The claims about nonwandering and chain-recurrent sets are attributed to the cited original construction. Independent external verification and historical-priority audit have not been performed.
