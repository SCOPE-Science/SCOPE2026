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

# Verification of the squarefree-square prime-cofactor theorem

The proof in RESULT.md establishes the unrestricted statement by elementary multiplicativity, a strict factor inequality for two or more squared prime supports, quadratic-residue divisibility, and explicit \(2\)-adic contradictions. Every case for the least repeated prime is handled: \(2\), \(3\), and at least \(5\).

Execute `python verify.py` with Python 3 and no third-party packages. The script independently lists actual unitary and exponential divisors using the definitions, tests every squarefree integer \(m\in[2,300]\) and every cofactor prime \(q\le101\) coprime to \(m\), and confirms exactly the two known positive examples. Expected output:

```
VERIFY_OK squarefree_m=2..300 cofactor_primes<=101 exact_pairs 4441 k_ge2_pairs 2855 solutions [(2, 5, 20), (3, 5, 45)]
```

The test exercises \(4441\) pairs, including \(2855\) with at least two distinct squared prime factors. These finite checks do not constitute an exhaustive test of the quantified infinite family. The proof is not dependent on computation or on third-party certification.
