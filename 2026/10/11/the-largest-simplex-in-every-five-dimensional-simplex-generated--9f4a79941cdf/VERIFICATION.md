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
# Reproducibility and limits

The supplied `verify.cpp` is standalone C++17 and contains the full finite certificate. It was compiled and executed from the packaged source directory with optimization and standard compiler warnings enabled; the final line was `VERIFY_OK`.

The checked representatives have subset sizes \(1,2,3\) and each sweep examines exactly \(5{,}949{,}147\) five-vertex completions. The respective maximum absolute determinants are \(14,17,18\). Independent inspection of all \(38{,}760\) six-tuples from the central \(20\) vertices gives determinant maximum \(18\), exactly \(30\) achieving tuples, exact equality with the \(30\) pair-cycle tuples, and no shared five-vertex subset. All the latter determinants are computed independently by two exact algorithms. Relative volume follows algebraically as \(18/(120\cdot6)=1/40\).

The analytic all-points reduction is contained in `RESULT.md`. The finite verifier cannot by itself certify claims about arbitrary nonvertex points, global historical novelty, other dimensions, or independent verification. Historical overlap remains possible.
