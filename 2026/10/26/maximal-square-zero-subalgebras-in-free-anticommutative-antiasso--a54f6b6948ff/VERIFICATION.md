---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The known free anticommutative antiassociative algebra in characteristic≠2 has graded vector-space description F(V)=V⊕Λ²V⊕Λ³V, V·V=Λ², V·Λ²=Λ³, other products zero. If a square-zero subalgebra U projects to P⊂V with dim(P)≥2, products of independent lifts have nonzero degree-two v∧u, impossible. For P=0, maximal U is W⊕Z. For P=ℓ=Kv, any lift a=v+w+z annihilates the remaining degree-two part precisely when α∈ker(v∧−:Λ²V→Λ³V)=v∧V. Thus all other maximal U are I(ℓ,w)=Z⊕(v∧V)⊕K(v+w). Direct multiplication confirms these are ideals and maximal (larger P impossible); W⊕Z is maximal for r≥3 because some v∧α nonzero. Each ℓ contributes q^{C(r−1,2)} parameters and there are (q^r−1)/(q−1) lines; thus exact total 1+((q^r−1)/(q−1))q^{C(r−1,2)}. Automorphisms preserve W⊕Z and act transitively on line/shift parameters via GL(V) and triangular generator shifts, giving two orbits. Intersections are (ℓ∧V)⊕Z for equal ℓ or distinguished ideal, dimension r−1+C(r,3); for distinct ℓ,m they are (ℓ∧m)⊕Z, dimension 1+C(r,3). Check rank3 q=3 count40, q=5 count156, q=7 count400 independently; the source C++ exhaustive q3 rank3 4-subspace census supports the theorem but is not proof. The all-rank proof is elementary yet a nontrivial complete extremal classification of a natural free algebra.

## originality

PASS

Remm arXiv:2504.04092 full primary HTML Sections 2.5 and later expressly gives the free graded exterior-degree-one-through-three algebra and seven-dimensional rank3 multiplication, so those structures are prior work. The paper's other substantive sections concern representations, (co)homology and operadic ideas; its inspected text does not enumerate inclusion-maximal abelian ideals, affine parameters, intersection spectrum, or two-orbit split. Smadyarov arXiv:2610.02852 full HTML treats general binary Zinbiel nilpotency and an Itô-style sum-of-abelian-subalgebras theorem, not this free-algebra maximal abelian classification. Ismailov–Mashurov–Smadyarov 2023 constructed the rank3 example, not its all-rank maximal-ideal lattice. Resultary queries located other finite-algebra commutativity counts but no same all-rank result. A general implicit description from prior free-algebra structure is conceivable; genuine exact maximality/orbit enumeration beyond the known model is the claimed originality.

## value

PASS

The finding gives a complete classification and finite-field count of a natural extremal property (maximal square-zero, i.e. abelian subalgebras) for all ranks of a classical free-algebra variety, proves automatically idealhood and gives automorphism orbit/intersection geometry. This is a mathematically motivated precise invariant, rather than merely restating the known exterior decomposition or a tiny ad hoc census. The rank3 fact does not masquerade as an exhaustive higher-rank computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
