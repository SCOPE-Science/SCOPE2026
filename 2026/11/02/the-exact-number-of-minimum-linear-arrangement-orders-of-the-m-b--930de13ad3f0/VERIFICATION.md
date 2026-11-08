---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For every n>=4, b(S)=2r(S)+u(S) counts cycle-run boundaries and unmatched antipodal rungs. Parity and run analysis give minima beta(k): 3 at size 1 and 2n-1, 4 at even k, 5 at the other odd k. The paired order attains every beta(k), so sum minima is 9n-8. Even optimal intermediate prefixes are cyclic blocks of whole rung columns. For four initial and terminal vertices the permitted square permutations number 16 each; each of n-4 interior 2-vertex steps has 2 adjacent columns x 2 within-rung orders=4 choices. Therefore n*16*4^(n-4)*16=n*4^n distinct labeled optimal orders. Independently computed every 2^(2n) subset cut and exact DP optimum chain counts for n=4,5,6,7: 1024,5120,24576,114688, matching theorem; finite values corroborate, not prove general n.

## originality

PASS

The sizewise minimal boundary values and width-five construction belong to Greeni–Rajasingh 2016; the additional equality characterization and exact number n*4^n of all minimum-total-length orders are not derived in the inspected paper. McSorley 1998 has a potentially relevant title but full text inaccessible; best-of-knowledge PASS qualified by this risk.

## value

PASS

Counting all optimum labeled graph arrangements is a natural exact ambiguity/degeneracy invariant of graph embedding; a classification of the optimizer fiber is stronger than a single optimal layout or known objective and could support uniform enumeration and sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
