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

# Reproducible verification

The standalone `verify.py` uses Python standard library only and constructs every object from the definitions. Invoke `python3 verify.py` from the directory containing this document. No input data, downloaded tables or external packages are required.

The computation checks 164 disconnected triples, a complete face vector of `(12,66,220,495,792,924,792,489,164)`, and 3954 nonempty faces. All 23208 Hasse covers are visited, and every vertex of the directed matching graph is visited by a topological sort; the full matching has 1968 pairs and leaves critical cells in dimensions 0,7,8 of counts 1,6,11.

Exact signed elimination constructs a six-by-eleven integral Morse boundary. Rational rank is 5. The specified rank-five minor has determinant -1, proving the nonzero Smith factors are all units. Independently, complete mod-two boundary ranks for the original simplicial complex are `(11,55,165,330,462,462,330,158)`.

The final homotopy step is mathematical: the seven-skeleton is a wedge of seven-spheres and its dimension-seven homotopy classes are degree vectors; integral elementary changes of degree bases cancel unit-degree seven/eight cell pairs. A mod-two computation alone could not justify that step or torsion-freeness.

Scope and limits: the computation is exhaustive for the specific twelve-vertex graph but does not establish a uniform theorem for larger graph families. Its outputs do not constitute an independent audit.
