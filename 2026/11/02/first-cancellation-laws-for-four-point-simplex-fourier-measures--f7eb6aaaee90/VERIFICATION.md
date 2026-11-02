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
# Reproducibility

Run `python3 checker.py` with Python 3 and no third-party packages. The checker constructs cyclotomic polynomials by exact monic polynomial division, reduces individual roots of unity in the corresponding integer quotient rings, and compares their four-term vanishing tests against the congruence lemma. It exhaustively compares the first-zero and multiple-zero histograms for \((b,L)=(2,4),(3,2),(4,3),(6,2)\). The successful run prints `FOUR_ATOM_SIMPLEX_EXACT_CYCLOTOMIC_OK`.

Observed counts for exactly zero, one and two vanishing mask factors among residue triples modulo \(b^L\): at \((2,4)\), \((2341,1185,570)\); at \((3,2)\), \((729,0,0)\); at \((4,3)\), \((223039,38277,828)\); and at \((6,2)\), \((43329,3309,18)\). A finite exhaustive computation is a check at the stated levels, not an infinite proof. The paper's elementary geometric lemma, transition matrix, and cylinder-tail argument supply the infinite proof.

Independent audit has not been performed. The 2012 exact-object paper's complete text was inaccessible in the bounded source comparison; equivalent historical derivations remain a possibility.
