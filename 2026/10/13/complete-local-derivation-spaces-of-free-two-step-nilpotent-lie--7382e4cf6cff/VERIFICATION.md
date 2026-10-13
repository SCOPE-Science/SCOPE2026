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

# Computational verification and limits
Run `python3 verify.py`. No external packages or input data are needed. In prime fields, the executable lists every two-dimensional subspace in RREF and builds the exact linear conditions \(T(u\wedge v)\wedge(u\wedge v)=0\) for arbitrary linear endomorphisms of \(\bigwedge^2 K^n\). Gaussian elimination produces the nullity; it separately checks the image dimension of \(A\mapsto R(A)\) and that every basis image obeys all constraints. Expected triples of \((n,p,\text{tangent nullity},\text{image rank})\) are \((4,3,16,16)\), \((4,5,16,16)\), and \((5,3,25,25)\). The successful test prints `VERIFY_OK`.

The finite computations are only consistency tests. The proof for every field of characteristic different from \(2\), and every \(n\ge4\), is the coordinate lemma and explicit local-derivation construction in `RESULT.md`. No independent audit has been performed.
