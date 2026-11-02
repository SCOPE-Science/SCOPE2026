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

# Reproducibility

The standalone file `verify_nash_egalitarian_boundary.py` requires only Python 3's standard library. From the directory containing the file run `python3 verify_nash_egalitarian_boundary.py`.

The checker enumerates all \((n!)^{2n}\) complete strict bipartite preference profiles for \(n=1,2,3\), and every one of the \(n!\) perfect matchings in each profile. It compares two separately written blocking-pair predicates, computes the complete stable-matching set, and checks the exact Nash-versus-egalitarian order for all unordered pairs of stable outcomes. It also computes both optimizer sets including all ties. Its recorded result at three pairs is \(46{,}656\) profiles, \(14{,}760\) stable matching pairs, all \(8{,}304\) strict-cost comparisons ordered correctly, and \(43{,}728\) equality cases versus \(2{,}928\) strict containment cases.

The same checker enumerates all twenty-four perfect matchings in the displayed four-pair witness and requires that exactly two are stable. Their scores are required to equal \((E,P)=(7,4096)\) and \((8,4608)\). The concluding marker is `VERIFY_OK exact_profiles_3=46656 pairwise_stable_comparisons_3=14760`.

All numerical comparisons use exact integers. The exhaustive finite proof is limited to sizes at most three, while a counterexample at four establishes the minimal boundary. Successful execution does not constitute independent expert verification or prove uniqueness in the research literature.
