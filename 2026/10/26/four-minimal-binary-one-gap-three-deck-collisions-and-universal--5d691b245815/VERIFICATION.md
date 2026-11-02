---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Definitions: B_j(w) is an ordered multiplicity vector for length-j subsequences whose consecutive selected indices differ by >=2, and the observation consists of all B_1,B_2,B_3. Independently enumerated all 8192 labelled 13-bit words by direct combinations of indices; obtained 8188 distinct 14-coordinate signatures, exactly 8184 singletons and four doubletons, matching each listed reverse pair. Independently checked injectivity for all 3<=n<=12 and punctured B_1,B_2 equality under deletion of either/both endpoint bits for all four pairs. The arbitrary-context lemma is proved by fixing exterior selected indices: any exterior selection leaves <=2 interior indices, with at most first/last interior indices forbidden; the four intact/punctured deck equalities exhaust cases. Thus any one block can be replaced within arbitrary contexts, yielding 2^m distinct colliding words at length 13m (not asserting maximal multiplicity). The optimal 8188 codewords and 16 maximal codebooks are exact class choices. Independently computed symmetry fixed-choice counts 16,0,4,4 for identity/reversal/complement/reverse-complement, giving six orbits by Burnside. A separate check of 25 two-sided contexts corroborated but is not an infinite proof. Actual RESULT.md/CHECK.py at assigned Git blob IDs were inspected.

## originality

PASS

The length-13 first collision threshold and one displayed pair are already in Golm et al. 2022, and all such novelty is excluded. Rigo–Stipulanti–Whiteland 2023 prove that general gapped binomial equivalence does not respect arbitrary concatenation and discuss local 2-deck conditions. The four-class exhaustive census, exact optimal-codebook orbit count, weaker B<=2 boundary-puncture sufficient condition, and unpadded universal B<=3 substitutions are more specific statements not found in inspected earlier statements. The original Golm 2022 complete text could not be retrieved, so its appendix/lemmas remain a material priority risk.

## value

PASS

The first nontrivial reconstruction ambiguity is a canonical finite cut-off; identifying every collision class is a meaningful exact invariant of the one-gap channel. Arbitrary-context stability is a structural property beyond a known isolated counterexample and yields rigorously exponential collision families in arbitrarily long words; optimal uniquely decodable codebooks and their symmetry classification quantify the exact coding consequence. The result does not claim new threshold or a general congruence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
