---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The sole fold is cell w=n-q-1 with slope -(n-1); all other cells translate with unit slope. Mod-d residues give a length-(m-1) forced string ending at the hub plus d-1 disjoint deterministic m-cycles receiving but not returning edges, yielding the block determinant and entropy. Their iterate m translates each cell to itself, proving neutral identities; any itinerary using the fold has derivative magnitude >=n-1 and cannot be identity on an interval. For gcd=1 all closed Markov walks traverse an expanding fold and identify one unique periodic fixed point per walk, with boundary addresses checked against the n-knot orbit, giving trace(M^k), determinant zeta, and hub return lengths. Independently built all 44 transition matrices for 3<=n<=10 and all q and checked their entire symbolic characteristic polynomials; separately enumerated exact rational closed-itinerary points for (n,q)=(3,1),(4,1),(4,3),(5,2) at k<=6 without duplicates. These finite checks support but do not prove the all-parameter result.

## originality

PASS

Best-of-knowledge originality of the exact final combined claim, after reviewing primary statements and Resultary hits; credited known partial antecedents. Wang studies the same interval-covering graph and a characteristic number for general transitive permutations, while the present statement explicitly specializes the affine modular rotations and adds gcd-block entropy, full periodic-island measure and coprime Artin–Mazur zeta. Wang Proposition 3.5 identifies characteristic numbers with shortest Markov cycles in general, and Example 3.7(1) gives sorted 1..n-1 for q=1. That component is KNOWN for the one-step shift and is not independently novel. The general graph framework does not supply the exact gcd decomposition, entropy polynomial, zeta or noncoprime neutral lengths for arbitrary q. Generic entropy-from-Markov and trace/determinant zeta identities automatically yield the displayed formulas once the claimed new specific graph structure and endpoint coding are proved; the theorem is the arithmetic family identification, not a new zeta identity. Neither Wang’s general inequalities nor the q=1 example logically forces the q-coprime independence or d>1 island decomposition without the residue-class argument.

## value

PASS

The gcd of a natural modular permutation controls exact entropy, persistence of positive-measure periodic islands and the full zeta function; the coexistence of expanding folding dynamics with neutral intervals is a substantive, reusable interval-dynamics classification. The known q=1 shortest-cycle component is contextual, not the whole value claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
