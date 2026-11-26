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

For a right quandle the medial identity is equivalent to pairwise commutation of the relative translations s_a s_d^{-1} for a fixed d; these generate the displacement group D. The subgroup N=[D,D] is normal in the inner group, and s_{n(b)}=n s_b n^{-1} for n∈N. The latter equality and normality show that its orbits respect both operands, including right division. The quotient displacement group is an abelian image of D. A homomorphism to a medial quandle intertwines translations and inverses with those on its image; hence it kills the commutator action and factors uniquely through the quotient. For the given formula s_(y,h)=ζ^{-1}Ψ_h, where Ψ_h is diagonal right action and ζ(x,g)=(x^g,g) commutes with it. Relative translations with h=1 as the reference are exactly Ψ_h, proving D=Ψ(G) and N=Ψ(G′), also for nonfaithful or nontransitive actions. For n≥2, the marked stabilizer fixes the marked cycle pointwise and its remaining permutations are rotations and equal-length exchanges. A remaining even cycle or repeated odd cycle length yields an odd stabilizer element; distinct odd lengths give only even rotations. Thus precisely those remaining distinct-odd partitions cause a split, including the empty partition. Counting the split types gives the baseline plus split bonus. Independently, each even S_n class contributes 2 m_1(λ) in Burnside's sum because the centralizer size cancels the class-size denominator. The two sum formulas are for n≥2, where the index is two; the separate n=1 value is one. A fresh enumeration of marked representative orbits for n=2,…,7 matches both expressions (4,6,10,16,24,36) and the splitting criterion. Replay/output: /workspace/branches/af26e821-43be-4b7f-8fd0-9cb2d977fde7/independent_marked_counts.py and independent_marked_counts.txt in the same directory. The general result is proved, not inferred from these finite cases.

## originality

PASS

Credit the explicit marked alternating-orbit census of the universal medial quotient. The displacement computation and orbit-quotient argument are direct applications of earlier action-quandle and displacement theory, not a new general mediality criterion or commutator theory. Earlier marked S_n component parameters, unmarked class splitting, and unmarked conjugation medialization do not state the marked stabilizer rule and both enumerations for the action quandle.

## value

PASS

The calculation gives an explicit census of the universal medial quotient of a natural action-quandle family. A mark changes which cycle lengths constrain splitting, so the familiar unmarked conjugacy quotient cannot recover the labeled component refinements. The stabilizer rule decides each split without constructing the large quandle table, and the two formulas give direct and independent ways to compute its size. Value rests on that marked invariant, not on the standard displacement criterion by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
