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

Run `python verification/check_ties.py` with Python 3.10 or later. The program uses only the standard library; it builds exact rational distributions and directly enumerates all ballot lists for up to four voters. It also calculates the exact irrational pair-equality sum and the fixed-lattice asymptotic scaling at selected sample sizes. The program's numerical approximations are not substitutes for the stated local-central-limit-theorem proof. For a fixed irrational score, its distribution enumeration uses exact integer-pair equality; numerical arithmetic appears only in comparing the score of the third committee, for the tested value \(\alpha=\sqrt2-1\).

Checked: rational \(\alpha=1/2\) exact winning-tie probabilities for \(n=1,\dots,8\), irrational \(\alpha=\sqrt2-1\) for \(n=1,\dots,7\), direct independent ballot enumeration for \(n\le4\), and rational and irrational leading pair-collision constants at \(n=100,400,1000\). All assertions in the checker passed in the packaged environment. Infinite limiting assertions rely on the full-lattice local central limit theorem and nondegenerate conditional Gaussian limits stated in the proof.

An independent scientific audit has not been performed.
