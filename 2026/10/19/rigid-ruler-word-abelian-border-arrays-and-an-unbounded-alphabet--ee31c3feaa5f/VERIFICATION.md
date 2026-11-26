---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Independently reconstructed the array and inverse induction from the proper Abelian-border definition. Subtracting both equal Parikh vectors from the full vector interchanges lengths j and i-j, even when the blocks overlap. Write d=2^nu2(i). If i=d, the final ruler letter first occurs there, so all proper suffixes contain a letter absent from all proper prefixes. If i>d, then nu2(i-d+j)=nu2(j) for 1<=j<d by divisibility, and the terminal valuation equals nu2(d); the length-d blocks are identical. Every shorter positive suffix length contains the terminal letter which is not yet in the matching prefix, so the longest Abelian border has length i-d. Conversely, assume the earlier letters of a realizing word are already identified by valuation. At i=2^k, reusing the letter at level s<k would make the first and last length-2^s blocks identical by the valuation identity, contrary to the required zero. This forces a new letter. At nonpowers of two, the length-d Abelian border is prescribed by complementarity, and the known length-(d-1) parts agree letter-for-letter, leaving only the terminal letter to match the prefix's level-nu2(i) letter. This also works at d=1 (empty known blocks); n=1 is immediate. Exactly the levels 0 to floor(log2 n) occur, giving necessity and sufficiency of the claimed alphabet size for this family and only a lower bound on the worst-case M(n). Inspected frozen RESULT.md lines 35–66, VERIFICATION.md and verify.py. The finite restricted-growth checks are corroborative; the all-alphabet and all-length claims follow from the reconstruction, not from executing the supplied script, which was not run.

## originality

PASS

Best-of-knowledge pass for the arbitrary-alphabet inverse theorem for this family and the resulting unbounded alphabet obstruction, not for the ruler word itself, complementary Abelian-border lengths, binary reconstruction, or the finite ternary census. Relevant inspected sources provide material neighboring coverage, without establishing the combined claim; the inaccessible ordinary-border paper remains an explicit source risk.

## value

PASS

The inverse problem is not injective over larger alphabets, and introducing many letters in one example word alone would not rule out a small-alphabet representative. This natural dyadic family proves rigidity where the general inverse fails and supplies an explicit logarithmic obstruction to any fixed universal alphabet. It separates the exact minimum for the family from the still broader extremal function M(n).

The dated certificate retains the supplied scientific assessment, sources and limitations.
