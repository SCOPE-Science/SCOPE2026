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

The standalone checker `verify_fan.py` uses only the Python 3 standard library. Run `python3 verify_fan.py` from the directory containing this file. Its success signal is `FAN_PRODUCT_CAPACITY_CHECK_OK`.

The checker constructs every point and maximal extension of \(P_{b,m}\) for \(1\le b\le3\) and \(1\le m\le3\), and enumerates all maximal-point colourings relevant to fork targets up to the proposed capacity plus one. Each accepted colouring induces a candidate map; the program checks monotonicity and back-lifting directly on the entire generated upset. Five small cases are cross-checked by a separate enumeration of every function from all source worlds to the target fork, independent of the maximal-colour parametrization. Results include exact generated-subframe capacities \(0,2,2\) for \(b=1\), across \(m=1,2,3\), and capacity \(b\) for \(b=2,3\) across all three tested powers. A capacity of zero denotes no obtainable fork of arity at least two.

The mathematical proof is essential beyond these finite sizes: no finite census certifies the universal product/p-morphism statements or uniqueness against earlier literature. The published Jankov--de Jongh theorem is used for the characteristic-formula separation, and Xiao’s distributive-lattice theorem for the initial equality. Independent audit and independent validation have not been performed.
