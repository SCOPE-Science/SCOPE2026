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

Two standard-library programs are provided. Run `python verify_schrijver.py` to check all four third-vertex adjacency patterns against every pair of distinct vertices of stable Kneser graphs in the included parameter ranges; no quantifier-depth cutoff is assumed by the *proof*. Run `python verify_boundary.py` to check sharp explicit alternating-set witnesses by independent brute-force subset enumeration. The corresponding stdout files are included and were regenerated from the package source.

`verify_schrijver.py` examines 36 graph instances: \(r=2\) and \(5\le n\le12\); \(r=3\) and \(7\le n\le17\); \(r=4\) and \(9\le n\le20\); \(r=5\) and \(16\le n\le20\). Every tested instance agrees with the threshold \(n\ge4r-1\). For passing instances the program checks every distinct vertex pair, totaling at least 17,610,597 passing-instance pairs.

`verify_boundary.py` independently checks 48 alternating-edge witnesses for \(2\le r\le7\), \(2r+1\le n\le4r-1\), confirming the exact complement independence number \(\lceil(n-2r)/2\rceil\). For \(n=4r-1\) this number is \(r\), as expected.

**Unproved by computation:** the theorem for all untested parameters, the infinite-round logical equivalence, and historical priority. The path lemma, explicit constructions, and three-pebble strategy in `RESULT.md` are the mathematical proof of the general claim. Independent mathematical audit: not performed.
