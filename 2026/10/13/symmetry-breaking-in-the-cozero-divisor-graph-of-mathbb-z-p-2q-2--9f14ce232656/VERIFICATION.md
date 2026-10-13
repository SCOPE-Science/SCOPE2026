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

The standalone `verify.py` artifact was read from its actual packaged path before replay.

It constructs the seven gcd-class quotient from the exponent-pair incomparability rule and exhausts all \(7!\) vertex permutations. Exactly four quotient automorphisms occur, and the quotient has no false-twin or true-twin pair.

For several distinct prime pairs, the verifier evaluates all seven class sizes and confirms that only the identity quotient automorphism preserves them. It checks
\[
\operatorname{Det}=N-7
\]
as the sum of the seven class contributions and verifies that the largest class size is
\[
(p-1)(q-1)\max\{p,q\}.
\]

The program then constructs the full cozero-divisor graph directly from gcd divisibility for \(\mathbb Z/36\mathbb Z\), \(\mathbb Z/100\mathbb Z\), and \(\mathbb Z/225\mathbb Z\). Every class size, interclass adjacency block, and maximal-twin-class assertion agrees with the symbolic proof.

Exact replay output:

```text
quotient automorphisms: [('A', 'B', 'C', 'D', 'E', 'F', 'G'), ('C', 'D', 'A', 'B', 'E', 'G', 'F'), ('F', 'D', 'G', 'B', 'E', 'A', 'C'), ('G', 'B', 'F', 'D', 'E', 'C', 'A')]
p=2, q=3: N=23, Det=16, D=6, weighted quotient rigid
p=2, q=5: N=59, Det=52, D=20, weighted quotient rigid
p=3, q=5: N=104, Det=97, D=40, weighted quotient rigid
p=5, q=3: N=104, Det=97, D=40, weighted quotient rigid
p=3, q=7: N=188, Det=181, D=84, weighted quotient rigid
p=5, q=7: N=384, Det=377, D=168, weighted quotient rigid
Z/(36)Z direct graph OK: 23 vertices
Z/(100)Z direct graph OK: 59 vertices
Z/(225)Z direct graph OK: 104 vertices
VERIFY_OK
```

The direct finite cases corroborate the theorem. The arbitrary-prime result is established by the symbolic gcd-class decomposition, the complete quotient automorphism enumeration, and the three explicit arithmetic obstructions to nonidentity weighted symmetries.
