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

At arbitrary integer m≥3, g=m²−1, k=m²−m−1 and a=m−2, b=m(m−2), c=k−1 satisfy 0<a<b<c<k<g. The carry equations kℓ+L=h+gU and kh+V=ℓ+gR, with digit 0≤h,ℓ<g and carries 0≤R,L,U,V<k, give mℓ≡L−h (mod g), hence unique ℓ=[m(L−h)]_g since m²≡1 mod g. From 0≤V<k one obtains max(0,ceil((gR−k+1)/k))≤h≤min(g−1,floor((gR+g−1)/k)), which at R=0,a,b,c gives candidate high-digit sets {0,1},{a,a+1,a+2},{c,k,k+1},{g−2,g−1}. The extra a+2 candidate at L=a,c has V=1−2m,−m−1 <0; extra c at L=0,b has V=g,g+m−2≥k. All remaining 16 ordered entries in the claimed table satisfy the two equations as polynomial identities and carry bounds for all m≥3. The eight states are closed and all reachable from star via the sole start edge star→B (h,ℓ)=(1,k); even pivots A,C,F,H, odd pivots A,D,E,H; all reach A, so no Young pruning. Thus the same marked 9-vertex graph is isomorphic for all m to m=3, Y(8,5). Independently implemented symbolic SymPy substitution verified 16 algebraic identities; exact BFS from original carry equations independently matched all 8 states, 16 edges and labels for each m=3,…,100. The finite test corroborates; universal proof rests on the symbolic inequalities/identities and induction on reachable states.

## originality

PASS

Best-of-knowledge original: the exact theorem is Kendrick (2015), Conjecture 39, explicitly posed without proof; a symbolic all-m exhaustive carry table now supplies the missing universal derivation. Sloane gives the m=3 graph and known 1089/complete cases; Holt’s derived-family example uses reversed notation Y(5,8) and still asks related isomorphism questions. Later primary permutiple methods are broader in algorithms but do not state or imply the exact all-parameter graph shape without separately performing this proof. Actual Resultary/literature searches found no covering theorem; this is not a guarantee of priority.

## value

PASS

Mathematically motivated exact theorem: establishes precisely Kendrick’s explicitly numbered open Conjecture 39 (2015) for an infinite quadratic base/multiplier family, with an exhaustive symbolic mechanism rather than more sample bases. A uniform marked eight-state Young automaton determines permissible reverse-multiple carry paths, pivots and reusable transfer-matrix enumeration for each parameter m. This is a nontrivial all-parameter structural classification of a natural family, not a textbook substitution, arbitrary finite slice, or known-table recomputation; it does not claim neighboring graph-isomorphism conjectures or preservation of digit labels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
