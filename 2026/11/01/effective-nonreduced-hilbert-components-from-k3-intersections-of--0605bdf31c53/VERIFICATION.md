---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For a smooth triple quadric S, adjunction gives a K3 with h²=8, hE=1 and E²=−2. The line/surface incidence is a nonempty smooth open of the bundle of Gr(3,18) over Gr(2,6), of dimension 45+8=53. Along a fixed line the three quadric normal gradients can have rank three everywhere (e.g. the consecutive rows (s,t,0,0), (0,s,t,0), (0,0,s,t)); away from the line the defining system is basepoint-free. The bundle 2h+E is generated off E using 2h and along E by lifting 1 from O_E(D)=O_E, since H¹(2h)=0. It is nef and big, with D²=34, hD=17 and DE=0. General |mD| is smooth by Bertini and avoids E; H¹(−mD)=0 gives connectedness. Kawamata–Viehweg and duality give H¹(±rD)=0 for r≥1. The bundles mD−2E=4h+(m−2)D and (m−1)D−2E=4h+(m−3)D for m≥3 have the required Kodaira vanishing. At m=2 the latter is 2h−E; restricting quadrics surjects onto H⁰(O_E(2)), so H¹(2h−E)=0. These are effective replacements for the uses of eventual vanishing in Nasu, not a direct application of the printed m≫0 statements. The flag criterion needs H¹(E)=0, H¹(C)=0 and the nonzero coefficient m in the line-bundle obstruction relation; all hold over C. The restriction map H⁰(N_{S/P⁵})→H¹(N_{E/S}) is onto: N_{E/P⁵}=O_E(1)^4, N_{E/S}=O_E(−2), and global normal sections surject onto H⁰(O_E(2)^3). The resulting nonzero flag obstruction functional gives codimension one for deformations of S preserving C. With N=O_S(2h)^3, H⁰ and H¹ of N(E−C)=O_S((1−m)D)^3 vanish, and the exact sequence with quotient O_E^3 gives H⁰(N(−C))=0 and H¹(N(−C))=C³. Thus the smooth flag tangent injects with cokernel of dimension three. For each exterior tangent direction the lift to a genuine polar section uses the first vanishing, and Nasu's Theorem 1.2 with the compatibility in Lemma 2.10 gives a nonzero primary obstruction class in H¹(N(3E)) restricting to the exterior obstruction on C. Indeed H¹(N(3E−C))=0 by duality and the shifted vanishing just checked, so restriction is injective. This supports all uses of Proposition 4.7 at m=2 and higher. Lemma 2.11 applies to the regular embeddings and smooth flag; the absence of unobstructed primary directions outside the flag, not merely tangent excess, proves the component assertion. The unique triple-quadric surface is recovered from C because (2h−mD)h<0, and the lines on it are rigid. Thus the image dimension is 53+dim|mD|=17m²+54, with generic tangent excess three; the reduced component is generically smooth in characteristic zero, so its ambient Hilbert structure is generically nonreduced. Adjunction and degree give 17m²+1 and 17m, respectively, and at m=2 the four numerical values match. At m=1 the H⁰-vanishing for N(E−C) fails, so the argument is silent there. The supplied integer script was inspected; it cannot verify the deformation steps and was not executed.

## originality

PASS

The supported distinct claim is the effective range m≥2 for the complex triple-quadric nonreduced component, including degree 34 and genus 69. Nasu proves the same construction with its numerical pattern and mechanism for sufficiently large m. Even the individual low-degree vanishing H¹(2h−E)=0 appears in his Remark 4.2; it is not itself a new result. The distinct work is to establish that the whole flag and obstruction proof applies down to the fixed endpoint, rather than claiming either a new family or a new obstruction mechanism. No inspected statement or unconditional stronger theorem supplies that effective component conclusion.

## value

PASS

The explicit cutoff removes an unknown large-m hypothesis in a natural Hilbert-component construction, yielding the concrete smooth degree-34 genus-69 family with dimensions 122 and 125 and a rigorously nonreduced generic scheme structure. This supplies a usable low-degree boundary instance with an obstruction proof, not just an intersection calculation and not a claim of absolute minimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
