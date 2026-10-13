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

It constructs the exponent-support ideal-intersection graph for nilpotency-length tuples \((2)\), \((3)\), \((2,2)\), and \((2,3)\). For \((2,2)\), all \(7!\) vertex permutations are examined, and the complete automorphism group has order \(48\), matching the theorem. For the checked cases, the program generates all structural automorphisms, brute-forces the determining number, constructs a coloring with exactly \(\prod_i\ell_i-1\) colors, and confirms that its color-preserving stabilizer is trivial.

It separately reconstructs the ideal-intersection graphs of \(\mathbb Z/36\mathbb Z\) and \(\mathbb Z/108\mathbb Z\) from divisor ideals, testing every pairwise intersection against the exponent-support model.

Exact replay output:

```text
ells=(2,): N=1, |Aut|=1, Det=0, distinguishing witness uses 1 colors
ells=(3,): N=2, |Aut|=2, Det=1, distinguishing witness uses 2 colors
ells=(2, 2): N=7, |Aut|=48, Det=4, distinguishing witness uses 3 colors
ells=(2, 3): N=10, |Aut|=1440, Det=7, distinguishing witness uses 5 colors
Z/36Z and Z/108Z direct ideal-intersection reconstructions OK
VERIFY_OK
```

These finite checks corroborate the arbitrary-parameter proof. They do not replace the symbolic arguments proving the true-twin partition, quotient automorphism group, determining lower bound, and general distinguishing coloring.
