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

# Reproducibility and mathematical checks

Run `python verify.py` with standard Python 3.9 or newer. The code uses no third-party dependencies.

The source-level mathematical certificate is the four-part combinatorial proof in `RESULT.md`; it covers all integers \(n\ge7\). The program supplies separate finite corroboration, not an infinite proof.

1. A graph-neighbor checker exhaustively tests subsets by increasing size for \(2\le n\le7\). Its exact optima and labeled multiplicities, at lengths \(n=2,3,4,5,6,7\), are respectively \((3,6),(4,3),(6,78),(7,99),(8,99),(9,96)\). This method directly counts vertices and graph neighbors without using the column transfer predicate.
2. An eight-mask-column dynamic program enumerates all two-dominating sets by minimum cardinality and exact multiplicity for \(1\le n\le200\); for each \(7\le n\le200\), it returns minimum \(n+2\) with precisely \(96\) realizations.
3. A separate extremizer generator builds the four boundary profiles using all six rainbow phases and the two independent binary choices at each end, then tests every vertex-level constraint and checks distinctness for \(7\le n\le40\) and lengths \(n=100,150,200\).

Independent experimental methods agree with the fully symbolic proof. No tests outside the stated bounds were used to support an infinite inference. No independent external review, formal theorem-prover certification or general-circumference classification is claimed.
