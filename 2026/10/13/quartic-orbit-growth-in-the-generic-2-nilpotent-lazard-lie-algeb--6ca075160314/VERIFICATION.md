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
The theorem has an ordinary proof from the free 2-step Lie algebra, its marked quotients, and Fraïssé homogeneity. The accompanying `verification.py` is a finite consistency check, not an exhaustive proof of the infinite statement.

It enumerates all subspaces in reduced row-echelon form for \(\mathbb F_2^s\) through \(s=6\) and \(\mathbb F_3^s\) through \(s=4\), checking those counts against the Gaussian-binomial Galois-number formula. For exterior-square dimensions arising from \(n\le4\) over \(\mathbb F_2\), it constructs the quotient image of every exterior basis vector, treats that list as a marked bracket signature, reconstructs the kernel from the signature, and verifies that all kernels give distinct signatures.

It also checks the elementary lower and upper bounds on \(G_s(q)\) used in the asymptotic proof for \(q\in\{2,3,4,5\}\) and \(1\le s\le24\). The script performs 120 assertions and prints `VERIFY_OK`.
