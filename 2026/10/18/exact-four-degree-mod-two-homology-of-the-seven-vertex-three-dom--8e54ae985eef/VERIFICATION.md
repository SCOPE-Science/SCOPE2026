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

# Finite verification and scientific limits

Compile: `g++ -std=c++17 -O2 verify_d73.cpp -o verify_d73`.

Run both complete calculations: `./verify_d73` and `./verify_d73 --reverse`. Both must terminate with `VERIFY_OK` and agree on the entire face vector and all four reduced mod-two Betti numbers.

The two calculations enumerate all \(2^{21}\) labeled graphs, retain exactly 287277 faces (including the empty face), check the entire Hasse graph of 287276 nonempty faces and 2113692 cover relations, and use exhaustive Kahn topological sorting to prove each discrete-Morse matching acyclic. The forward matching has critical-cell counts 1 in degree 0 and \(162,941,269,41\) in degrees 6–9; its mod-two Morse boundary ranks are \(0,56,262,6\). The reverse matching has critical-cell counts 1 in degree 0 and \(161,760,85,37\) in degrees 6–9; its boundary ranks are \(0,55,82,2\). Each independently produces \(106,623,1,35\). The face-vector Euler characteristic is \(-551\), matching \(106-623+1-35\).

The verifier computes exact field-two linear algebra, not floating-point approximations. The tests are exhaustive because the finite object has 21 possible graph edges, each represented by one bit. The matching's acyclicity is checked explicitly; the computation is not a heuristic search. Nevertheless a successful local replay is not independent external audit, and these checks do not determine integral torsion or a homotopy wedge decomposition.
