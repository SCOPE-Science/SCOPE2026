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

Laga–Shnidman Lemma 7.18 fixes the τ=(x↦−x) bitangent count at four, namely infinity and three horizontal lines, with twelve other τ-pairs. For σ=(y↦ωy), projectively σ-fixed lines are either Y=0 or in the pencil AX+CZ=0. The Y=0 section is the separable quartic x⁴+ax²+b under the discriminant b(a²−4b)≠0; the finite vertical X=uZ section is Z(Y³−f(u)Z³), hence has multiplicities 1+1+1+1 or 1+3 and is never an even bitangent divisor. Infinity Z=0 has intersection 4∞ and is the sole σ-fixed bitangent. Thus n1+2n2=1, n1+3n3=4 and n1+2n2+3n3+6n6=28 give (1,0,1,4). The three horizontals are a size-3 orbit since c³=b−a²/4≠0. Equivariance of τ-pair construction then gives four free µ3-orbits on Prym-related 2-torsion. Independently reproduced discriminant and horizontal square identity; code is a consistency check, not a derivation of Lemma 7.18.

## originality

PASS

The primary source classifies the τ-involution fixed bitangents and identifies the twelve pairs with Prym two-torsion, but the independently checked σ-fixed-line classification produces a genuinely extra marked order-three action and therefore the full µ6 orbit decomposition. Existing τ orbit counts alone do not logically determine σ fixed points or the 1+3+4×6 splitting. Older classical bitangent tables remain a named residual risk.

## value

PASS

The 28 odd theta characteristics are a canonical geometric invariant of these genus-three curves and the involution/Prym-pair construction is central to their arithmetic study. Classifying the full naturally marked order-six permutation action, including four three-cycles on the 12 Prym-pair set, completes a meaningful symmetry classification. It is neither an arbitrary finite example nor just reiterating the involution count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
