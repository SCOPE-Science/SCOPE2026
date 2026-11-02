---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For all a,b>=1, every orientation matrix X with even 2x2 rectangle parity admits representation X_ij=r_i+s_j over F2; fixing the first row/column proves existence, and simultaneous r,s complement accounts for the exact twofold gauge, including singleton sides. Under (σ,τ), invariance requires r_i+r_σ(i)=s_j+s_τ(j)=d. For d=0 there are 2^(cσ+cτ) lifts, and d=1 has the same number precisely if each cycle of σ and τ is even; divide by the twofold gauge for the side-preserving fixed count. For a=b=n, side swap reverses orientation, leading to r_(τ∘σ)(i)=r_i+1; solutions exist iff every cycle of θ=τ∘σ has even length, yielding 2^cθ actual matrices. Under reordering of r and s by Hamming weights, (p,q) is equivalent to (a−p,b−q); side swap on the equal-size weight grid is (p,q)->(n−q,p) of order four. Burnside yields U_ab=((a+1)(b+1)+[2|a][2|b])/2 and V_n=((n+1)^2+3[2|n])/4. An independently written exhaustive binary-matrix checker enumerated seven shapes through (3,4), counted every fixed character directly (288 comparisons), confirming all formulas; the proof covers all positive sizes.

## originality

PASS

Qualified best-of-knowledge PASS: Coskey–Ellis Lemma4.1 gives the two-class parity/rank-one representation and Jasiński et al defines the semigeneric age; those are credited and do not alone state the full permutation character or sharp side-swapping even-cycle obstruction. The published semigeneric Stirling-layer result counts labelled tuple-orbits but not this unlabeled age symmetry character; random bipartite reduct result counts other switching orbits. A specialized finite symmetry enumeration under alternative terms remains possible.

## value

PASS

The first nontrivial two-class layer of the semigeneric homogeneous-digraph age has a complete natural group action by vertex relabellings and (when balanced) class exchange. The exact fixed-point character and all-even obstruction classify which automorphisms preserve an orientation, with polynomially many isomorphism classes versus exponentially many labels. This is a useful exact symmetry classification, not merely a relabeling of the known matrix factorization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
