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

# Reproducibility and scientific limits

Run `python3 verify_gap_blocks.py` from a directory containing the standalone verification file. It has no third-party dependencies and uses Python's exact integers.

For every \(2\le d\le12\) and \(2\le t\le16\), it computes representability through additive dynamic programming up to the conductor. It independently checks every integer's membership against the Apéry-residue formula \(n\ge k_{n\bmod a}b\), where \(k_r\equiv-tr\pmod a\), \(0\le k_r<a\). It enumerates all maximal missing blocks and compares their frequency distribution to the theorem. It separately takes successive differences of exact semigroup-membership indicators, locates nonzero polynomial exponents, and checks their full exponent-spacing distribution, number, and weighted degree. A second route uses explicit two-dimensional enumeration of \(ua+vb\) for 30 smaller parameter choices, independent of the dynamic program.

Actual execution output:

```text
VERIFY_OK general_cases=165 checked_integers=1058035 gap_blocks=109065 independent_enumeration_cases=30 exact_integer=yes
EXAMPLE d=2 t=2 a=5 b=7 gap_block_counts=[(1, 6), (2, 1), (4, 1)]
EXAMPLE d=3 t=2 a=7 b=10 gap_block_counts=[(1, 6), (2, 6), (3, 1), (6, 1)]
EXAMPLE d=4 t=3 a=13 b=17 gap_block_counts=[(1, 12), (2, 12), (3, 12), (4, 1), (8, 1), (12, 1)]
```

**Mathematical boundary.** The script tests finite parameter ranges and does not establish the infinite theorem. The unrestricted proof in `RESULT.md` depends on the explicit Apéry thresholds, an exhaustive row/block argument, and standard two-generator numerical-semigroup symmetry. The formula has not been independently audited or certified by an external mathematical verifier. Earlier literature may contain an equivalent implicit special case.
