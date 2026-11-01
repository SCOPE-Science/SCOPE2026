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

# Reproducibility and limitations

Run `python verify_homotopy.py` and `python verify_equivariant.py` after installing the libraries listed in `requirements.txt`. These programs are supplied in full, not excerpts. The recorded outputs are `homotopy_output.txt` and `equivariant_output.txt`.

The homotopy checker constructs all 15 Petersen graph edges from unordered pairs of five labels, enumerates every nonempty edge subset, and independently determines matching membership from endpoint disjointness. Its 160 matched simplex/coface pairs are determined by a fixed priority order. It verifies that each simplex belongs to at most one pair, that every pair is a cover relation, and that the full reoriented face-poset Hasse diagram has no directed cycle. Exact integer boundary arithmetic then cancels those 160 pairs by \(\pm1\) pivots, verifying the critical differential is zero.

The equivariant checker builds signed integer simplicial boundary matrices and tests all relevant compositions are zero. It computes their exact rational ranks. It derives signed chain-action matrices from five-label permutations, and obtains image-space traces using invertible pivot minors modulo 101. Rational and modular boundary ranks agree, permitting character reconstruction because integral-valued homology traces in five dimensions lie between minus five and plus five. The resulting characters are compared directly with the signed five-point permutation and the Specht \((3,2)\) character identities.

**Scope:** These are full finite calculations of this fifteen-edge complex. The homotopy argument invokes discrete Morse theory and Hurewicz's theorem, and the rational quotient argument uses invariants under finite group actions. Computational exhaustion is not an independent audit or general theorem about arbitrary graphs. No statement is made about integral quotient homology or an equivariant wedge decomposition.
