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

To independently check the finite data, extract `verify.py` and run `python3 verify.py` using a standard Python 3 interpreter. The standalone program enumerates all derangement perfect matchings in the crown graph and constructs the forbidden complement masks \(P\setminus Q\) for every ordered pair of distinct perfect matchings. It rejects a complement precisely when one such full mask is present; this implements the original complete-forcing definition without assuming the symbolic support classification. Exhaustive tests cover all \(64\), \(4096\), and \(1048576\) edge-complement candidates for \(n=3,4,5\) and compare the entire cardinality polynomial to a second direct formula implementation. An independent construction of every star/triangle-supported complement checks the formula at \(n=4,5,6,7\). The actual captured output is in `verification_output.txt` and terminates with `VERIFY_OK`.

The finite enumeration is neither an infinite proof nor an external audit. The proof for arbitrary order uses the nice four/six-cycle frame obstructions, classification of intersecting two-element subsets, and inclusion–exclusion as detailed in `RESULT.md`. The especially relevant 2023 published primary paper was accessible only as abstract and one-page preview, so an equivalence risk persists.
