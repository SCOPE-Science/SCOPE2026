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

The analytic checks are: (1) facet projection to the plane \(s\cdot x=1\) has barycentric coordinates \(\lambda_i=s_i y_i+(1-s\cdot y)/3\); (2) simultaneous facet activity is equivalent to \(\|y\|_1+\|y\|_\infty\le1\); (3) the edge-cone condition is \(s_i y_i+s_j y_j+2|y_k|\le1\), whose intersection over all edges is the same region; (4) all six vertex normals occur for every interior point; (5) the exact chamber integral is \(1/144\), and the volume ratio is \(1/4\). `verify.py` checks only the exact rational arithmetic. Boundaries of the locus have zero volume and contain coincident face/edge bases. Independent audit and independent validation remain unperformed.
