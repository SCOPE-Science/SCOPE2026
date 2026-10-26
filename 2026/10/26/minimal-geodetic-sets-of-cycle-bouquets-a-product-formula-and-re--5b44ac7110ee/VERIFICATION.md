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

Run `python3 verify.py` with Python 3 standard library. The script constructs cycle bouquets with one common vertex, computes shortest-path distances by breadth-first search, and uses the defining distance equality to recover every vertex belonging to at least one geodesic between each chosen pair. For every nonempty subset, it tests geodetic coverage and one-vertex-deletion minimality. It independently generates the classified families and compares the **entire family of sets**, not only counts; cardinality coefficients are compared separately.

The recorded execution in `verify_output.txt` contains 28 checked bouquets (21 two-petal, seven three-petal) and 104,644 examined nonempty subsets, with `PASSED` on completion. For petal lengths \((4,5,6)\), the verifier reports \(24\) sets with size multiplicities \(3,12,9\). No outside packages, web data, or privileged resources are needed.

The verifier is exhaustive only on its listed finite instances. Universality for all integer petal lengths and all \(t\ge2\) follows from the mathematical proof, not computational extrapolation. The mathematical statement has not received independent validation.
