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

Using E(y)^2/y²−1=Σ Ω_i(y^{q_i}−1)=(y−1)F(y), with F=ΣΩ_i (y^{q_i}−1)/(y−1), the drift sign is minus sign F for E,y>0. F(1+)=ΣΩ_i q_i=2q0. For q<0 or q>1, φ_q is strictly increasing on y>1 by derivative g_q'=q(1−q)y^{q−2}(y−1)<0 and g_q(1)=1. φ_1≡1; φ_0≡0. Hence F is nondecreasing and, whenever q0<0, strictly increasing. The mandatory positive q>=1 fluid makes F eventually positive (q=1 constant positive or q>1 divergent) while negative-q contributions tend to zero from below. This proves existence and uniqueness iff q0<0; at q0=0 F immediately positive. For no accelerating component all q>=1, F positive. Curvature cancels by normalization; no restriction Ωk sign beyond H>0 and normalization. Independent exact algebra and ΛCDM root z≈2.08876043244513 (Ωm=.3, ΩΛ=.7) confirm the illustrative case; finite example is not the theorem proof.

## originality

PASS

Qualified best-of-knowledge: Sandage/Loeb established drift observable, Alves et al. explicit ΛCDM crossing and Lobo et al. general constant-w mixture equations. The inspected Lobo full paper discusses typical nontrivial zero and low-z deceleration but does not state the exact iff-and-unique theorem for the separated exponent class, while its formulas strongly overlap. Present theorem adds monotonic divided-power zero-count classification, not new cosmological equations.

## value

PASS

The existence and number of positive-redshift drift sign changes are natural global observables in standard constant equation-of-state cosmologies. Unlike mere root formulas or numerical plots, the theorem provides a sharp, all-mixture topological root count in terms of the local observable q0, even with curvature; the exponent separation explains exactly why it works. This is an independently useful structural lemma, albeit short and confined to a physically motivated but not universal fluid class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
