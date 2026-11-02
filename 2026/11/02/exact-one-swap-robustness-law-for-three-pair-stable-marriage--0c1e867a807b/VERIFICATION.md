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

# Reproducing the exact census

From a directory containing `verify_robust.py`, run `python3 verify_robust.py` with a standard Python 3 installation. It uses only `itertools`, `collections`, and `fractions`.

The code visits the complete Cartesian product of strict preference rankings, enumerates every perfect matching, and checks every potential blocking pair. For every original stable matching and adjacent swap it compares direct re-evaluation under the modified rankings with the elementary local condition that a newly promoted alternative can create a blocking pair only when the modified agent is paired with the displaced alternative. Assertions verify equality of the two decisions, the joint table and its marginals. The expected terminal output is `PASS: every altered matching independently checked against the local adjacent-swap criterion`.

For three pairs there are \(46{,}656\) complete profiles and \(559{,}872\) equally weighted profile-and-swap cases. The exact failure count is \(70{,}560\), with \(49{,}248\) failures at the higher adjacent position and \(21{,}312\) at the lower one. For two pairs there are \(16\) profiles and \(64\) profile-and-swap cases, of which \(16\) fail. These finite statements are exhaustive; they are not evidence for a general arbitrary-size law. Scientific priority is not independently audited.
