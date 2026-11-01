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

# Reproducibility and precise limits

`python3 verify_gp10_twoind.py` is executable with Python 3.10 or newer and the standard library. It regenerates both generalized Petersen graphs from modular edges, tests all \(2^{20}\) vertex subsets per graph, constructs all faces and stagewise matching pairs, and topologically sorts every oriented Hasse incidence to certify acyclicity.

The exact matching counts are 31,565 and 31,000; the nonempty-face counts are 63,142 and 62,048. The complete Hasse incidence counts are 410,500 and 400,760. The critical dimensions are \((0,5,6,7)\) with multiplicities \((1,1,6,4)\) for the dodecahedron, and \((0,6,7)\) with multiplicities \((1,3,44)\) for Desargues. The recursive signed integral Morse calculation produces primitive unit minors for the nonzero differentials: \(-1\) for the one-by-one and four-by-four dodecahedral minors, and \(-1\) for the three-by-three Desargues minor. The dodecahedral adjacent differentials compose to zero. Independently, full original simplicial boundary elimination over \(\mathbb F_2\) recovers the stated Betti dimensions.

The test ends with `GP10_TWO_INDEPENDENCE_INTEGRAL_HOMOTOPY_CERTIFICATE_OK`; it does not claim to replace external peer verification. All proofs concern only these two graph instances and the induced-maximum-degree-at-most-one simplicial complex. Nothing has been independently audited.
