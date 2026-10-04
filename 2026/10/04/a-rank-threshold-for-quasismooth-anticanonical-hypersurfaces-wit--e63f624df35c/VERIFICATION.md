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

The proof has two logically independent components. First, the singularity calculation uses the transverse quotient \(\frac1a(1^r)\), whose nontrivial ages are \(rj/a\) for \(1\le j<a\); their minimum is \(r/a\). Second, Fletcher's coordinate-subset criterion is applied directly to degree \(d=r+ma\).

The standalone checker `artifacts/verify_equal_weight_anticanonical.py` reconstructs the Fletcher test by enumerating every coordinate subset and testing weighted-semigroup reachability. On \(2\le r,m\le5\), \(1\le a\le8\), it checks \(128\) triples and agrees exactly with the closed criterion. It separately computes quotient ages and checks canonical/terminal thresholds. It then checks the exact canonical and terminal counts for every \(2\le r,m\le100\). A successful replay prints `VERIFY_OK 128 generic Fletcher cases; counts through r,m<=100`.

These finite checks are regression tests, not an exhaustive proof for unbounded parameters. The proof in `RESULT.md` establishes the universal quantifiers. No independent audit or external certification has been performed.
