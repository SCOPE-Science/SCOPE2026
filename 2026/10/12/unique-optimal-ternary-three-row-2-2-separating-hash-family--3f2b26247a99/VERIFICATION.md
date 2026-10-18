---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

An SHF of type {2,2} forbids a four-column subset with some 2+2 partition whose symbol images overlap in all three rows. Independent combinatorial enumeration of every 4-subset of 27 ternary length-three words found 16,092 forbidden four-subsets, then exhaustively checked all C(27,5)=80,730 and C(27,6)=296,010 candidate families, obtaining exactly 54 valid 5-sets and 0 valid 6-sets. For each maximum, each coordinate has multiplicities (2,2,1) and the three unique-symbol positions coincide; deleting that word leaves a binary even/odd parity class of four 3-bit words. The canonical set {000,011,101,110,222} is separating; with three independent symbol permutations per row and row permutations the natural group has 6³×6=1296 elements. Its orbit has 54 sets, hence one orbit and stabilizer order 1296/54=24. The Hamming distance multiset is 6 pairs at distance2 and 4 at distance3. These computations enumerate every finite case, not samples or a claim about other parameters; the known n≤5 upper bound was checked against Bazrafshan 2011 Prop.5.2.3.

## originality

PASS

Bazrafshan 2011 Proposition 5.2.3 supplies n≤5 and Example 5.2.4 a five-column construction, so optimum and one witness are prior. The actual original dissertation Section 5.2 pp56–57 was read in full/page images and does not classify all equality cases. The exact 54 labeled maximizers, common singleton/parity structure and one-orbit/stabilizer classification are additional finite combinatorial statements not supplied by the parent upper bound or indexed related perfect-hash work.

## value

PASS

The sharp equality classification of a natural smallest nontrivial secure-frameproof/separating hash family gives a canonical form, symmetry stabilizer and complete optimum multiplicity, useful for classifying or generating optimal codes. It resolves a structural question distinct from the known numerical optimum rather than a redundant table entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
