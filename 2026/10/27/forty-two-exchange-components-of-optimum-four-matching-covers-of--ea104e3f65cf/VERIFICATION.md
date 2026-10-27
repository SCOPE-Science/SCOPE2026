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

# Reproduction of the finite certificate

Use Python 3 with only its standard library. From this directory, run:

```
python3 verify_recursive.py
python3 verify_local_csp.py
python3 verify_recursive.py --certificate
```

`verify_recursive.py` reconstructs all \(30\) edges and independently enumerates \(32\) perfect matchings by removing pairs of unmatched vertices. It checks the absence of a three-cover, tests every one of the \(35{,}960\) four-element subsets for complete edge coverage, and calculates all exchanges, component types, and doubled-matching extension counts. It has an exact backtracking isomorphism test and stores no precomputed matching list. Its normal output is recorded verbatim in `recursive_output.json`; its `--certificate` output is `certificate.json`.

`verify_local_csp.py` instead assigns nonempty subsets of four colors to each edge, requiring a \((2,1,1)\) partition of colors at every cubic vertex. At the chosen root the global color names are normalized; \(400\) valid rooted assignments represent \(200\) unordered four-covers because the two colors on the doubled root edge remain interchangeable. This second enumeration independently rebuilds the exchange graph and its component profiles. Its output is recorded in `local_csp_output.json`.

The checks completed: \(200\) minimum covers, \(220\) exchange edges, \(42\) components, and class multiplicities \(10,20,10,2\) for component orders \(1,5,7,10\). The first program additionally verifies graph isomorphisms within each class and extension multiplicities \(5^{10},6^{10},7^{10},10^2\) over doubled-edge matchings. Both output files are included as byte-exact reference logs; outputs alone are not mathematical certificates without the documented exhaustive programs.

Scope is the specified \(20\)-vertex graph only. No proof concerning all flower snarks or all cubic graphs is claimed. The computations and proof have received no independent external audit.
