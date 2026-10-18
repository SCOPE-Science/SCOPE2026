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

# Reproduction and limits

The general statement follows from the displayed gradient equations and explicit rational tangent points in `RESULT.md`; no finite computer experiment is used to establish the infinite-parameter smoothness assertion.

For \(q=5\), compile `verify.cpp` using `g++ -std=c++17 -O3 verify.cpp -o verify`, and execute `./verify`. The program canonicalizes all nonzero homogeneous cubic coefficient vectors modulo the \(4\) nonzero scalars, checks each of the \(31\) projective points exactly modulo \(5\), and forms tangents only at smooth zeros. Each tangent's incidence mask is the explicit dot-product condition on normalized projective points. In the completed execution, \(2{,}441{,}406\) classes were examined, zero were tangent-filling, and maximum coverage was \(29\) of \(31\) points. The quartic witness has \(11\) rational points and its rational tangents cover all \(31\).

The enumeration is exhaustive for cubic forms over \(\mathbb F_5\) but does not classify cubics over other fields. Finite verification does not independently establish general geometric smoothness; that rests on the written proof. No independent mathematical audit has been performed.
