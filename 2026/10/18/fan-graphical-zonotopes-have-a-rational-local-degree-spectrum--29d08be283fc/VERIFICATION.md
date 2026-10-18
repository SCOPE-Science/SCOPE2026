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

The supplied `check_fan.py` has no external package dependencies and uses only Python's standard library. Run `python3 check_fan.py` from the directory containing this file. Its final line is `VERIFY_OK` on success.

The checker independently enumerates all \(2^{2m-1}\) directed assignments on the \(m\)-path fan's edges for each \(1\le m\le8\), filters acyclic orientations by Kahn topological sorting, finds all Hasse covers by deleting an edge and testing alternate reachability, and compares complete excess histograms with the symbolic recurrence. It also checks the oriented-path sink binomial identity for lengths \(1\) through \(10\). For \(1\le m\le7\) it independently counts the zonotope edges by the graphical contraction formula and compares them with half the weighted sum of the histogram degrees. The enumeration is exhaustive **only for those finite sizes**. The proof in `RESULT.md`, not an extrapolation, establishes the unlimited parameter range and toric smoothness statement.

The principal polynomial coefficients checked by this implementation for \(m=3,4,5,6,7,8\) are respectively \(16+2u\), \(42+12u\), \(110+50u+2u^2\), \(288+180u+18u^2\), \(754+600u+102u^2+2u^3\), and \(1974+1908u+468u^2+24u^3\).
