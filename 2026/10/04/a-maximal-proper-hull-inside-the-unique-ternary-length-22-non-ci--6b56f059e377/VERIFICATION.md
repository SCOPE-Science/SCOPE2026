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
`artifacts/verify.py` uses only the Python standard library and exact arithmetic modulo \(3\).

It reconstructs the \(11\times11\) Toeplitz matrix from the published \((t,a,b)\) triple and forms \(G=[I_{11}\mid T]\). Gaussian elimination verifies \(\operatorname{rank}(G)=11\) and \(\operatorname{rank}(GG^{\mathsf T})=1\). The nullspace of the Gram matrix has dimension \(10\); multiplying a nullspace basis by \(G\) produces a hull generator whose Gram matrix is exactly zero.

The verifier exhausts all \(3^{11}=177147\) ambient messages and all \(3^{10}=59049\) hull messages, so the two minimum distances and both complete weight distributions are exhaustive finite results. It also enumerates both nonzero cosets of the hull and checks their identical weight distributions. Finally it evaluates the ternary Griesmer sum for \((k,d)=(10,10)\) as \(23\), which exceeds length \(22\).

No sampling, timeout inference, or incomplete enumeration is used. The code does not attempt to re-prove the published equivalence classification; that classification is a literature premise, while all new hull and spectrum claims are independently recomputed from the published representative.
