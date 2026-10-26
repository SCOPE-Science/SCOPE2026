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

Run `python3 verify.py` from the package directory. The program requires only the Python 3 standard library and uses exact integer or `fractions.Fraction` calculations. The completed check printed `PASS 304959 exact arithmetic assertions`.

The checks construct exact cyclic ballots realizing all upper and lower endpoints and their midpoints for every feasible \((m,r,k,t)\) with \(2\le m\le12\). They check all one- and two-ballot profiles through five candidates (selecting all optimal committees for the single-ballot case) and an additional fixed-seed set of profiles. The 51-voter ten-candidate witness is reconstructed exactly, yielding score \(1828/2295\) with both winners outside the designated eight-candidate party.

The general theorem depends on an explicit rearrangement inequality and constructive proof. Finite checks alone do not certify statements for unbounded candidate or voter counts. Historical priority was investigated from available research, but no independent audit or complete literature exhaustiveness is asserted.
