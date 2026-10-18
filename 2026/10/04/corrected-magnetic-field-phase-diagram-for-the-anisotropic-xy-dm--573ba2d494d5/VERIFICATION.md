---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For 0<G<K and T>0 the two explicit Gibbs X-state concurrence candidates f1,f2 are equivalent to q_B>2 and q_B<0 because all squared quantities are nonnegative. If Δ_B≤K then q′>0. If Δ_B>K, sinh(2Kβ)/sinh(2Δβ) strictly decreases because x coth x increases, so q has exactly one maximum; q(0)=1 and q→−∞. For fixed β, q strictly decreases as B increases, and the maximum decreases continuously from ∞ to 1, producing a unique B_* where max q=2. The claimed three/one crossings follow. At large B, the q=0 condition gives β_c=(log(2Δ/G)+o(1))/Δ and T_c~B/log(2B/G). The claimed B*=1.7495575301980955 for J=1,γ=.6,D=.5 matches the inspected bounded bisection code. The isotropic-in-plane G=0 case gives field-independent cosh²(Kβ) threshold. All conclusions are analytic; code is supplemental.

## originality

PASS

NARROW. The XY–DM Hamiltonian is locally unitarily equivalent, under opposite z rotations of the two spins removing the odd-block phase of J+iD, to the 2002 anisotropic *DM-free* XY dimer with J_eff=√(J²+D²) and anisotropy γ_eff=G/J_eff. The 2002 Kamta–Starace paper already gives the exact thermal concurrence via spin-flipped eigenvalues, Fig. 4 depicting the reentrant thermal zero curves, and a B/log B high-field threshold; NONE of those generic physical observations or that asymptotic is original to this package. However the complete **analytic uniqueness theorem for one field B_* defined by max_β q_B=2, with all-β three-crossing classification and its exact value at the 2008 source parameters** is neither stated nor proven in the full earlier article (which explicitly says the finite-T concurrence is generally evaluated numerically). Showing unique maximum and B_* for all 0<G<K uses nontrivial hyperbolic-ratio monotonicity, not merely reparameterization or a table lookup. This narrower mathematical statement survives, so O PASS solely for that new rigorous classification and source-specific correction; broader physical claims are PRIOR COVERED.

## value

PASS

The rigorously unique B_*(G,K) is a natural, nontrivial invariant marking disappearance of a distinct finite-temperature entanglement interval. The complete root-count classification of the naturally parameterized Gibbs dimer is independently useful for control and validation of numerical phase contours. The exact source-point value and theorem are meaningful even though previous work already graphed thermal revival and proved field dependence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
