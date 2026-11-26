---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

I derived the geometry directly. With a=tb, the outward normal to PAB can be taken as N=(bs,a−bc,abs), of norm W=bQ. Taking negative dot products with the three other unit outward normals gives cosines (a−bc)/W on PA, (b−ac)/W on PB, abs/W on AB, c on OP, and zero on OA and OB. Hence t<c gives a unique obtuse LAB edge. For a point d(c,s,0) of OB, equal distances to the planes OPA and PAB give ds=(abs−ads)/W, or d=ab/(a+W). The retained child swaps the base rays, giving b′=a and t′=d/a=1/(t+Q). The positive-root fixed-point equation has no squaring ambiguity on (0,1). Its cubic is strictly decreasing on (0,c); it has opposite signs at 1/√2 and c for c>1/√2 and no root in (0,c) below the threshold. At equality the strict t<c margin is lost; this does not classify critical or other LAB branches. At the fixed point Q_*=(1−τ²)/τ and the cubic gives 2τ²(1−cτ)=1−τ², hence f′(τ)=−1/2. Choose a small rectangle with t_max<c and sup|∂_tF|=ρ<1. The perturbation F(t,b)−F(t,0)=O(b²) and b′≤t_max b give invariance on shrinking its height and summable |t_n−τ|. The infinite product for b_n/τ^n then has positive finite limit C. For the second law, split the smooth map in t and u=b²: δ_(n+1)=A_nδ_n+G_nu_n with A_n→−1/2 and G_n→−(1−c²)τ⁴/(2Q_*). Dividing by u_(n+1)=t_n²u_n gives an affine recursion with limiting absolute slope 1/(2τ²)<1; subtracting its limiting fixed point yields convergence to the stated K. The volume is abs/6, face areas are a/2,b/2,abs/2,W/2, and PB is longest (t<c<1 and AB<b). These give the stated diameter, volume, angle, inradius and aspect asymptotics, with r_n/b_n→τ²s/(1+τ). The limiting cosine on PB equals 1/(2τ) and that on PA equals 2/(4τ²)−1, proving angle doubling on the stated angle ranges. The increasing c(τ) gives exactly the open multiplier interval (1,√2). On the published rectangle, A=t−c+s²tb² satisfies t−c<A<0 and |t−c|<Q; hence 0<1+A/Q<1 and invariance gives |∂_tF|<16/25. The summability and asymptotics therefore extend to that rectangle. Fresh, bounded 120-digit recurrence iteration for the published seed independently corroborates the constants: C_400≈0.2398563383657047471865642656963 and the aspect prefactor ≈25.01739754619044555760018; C_300 and C_400 agree to about 85 decimal places, and the normalized t error approaches K≈−0.08048577802046797135566. Replay: with mpmath at 120 decimal digits solve the displayed cubic with starts 0.78 and 0.79, then simultaneously update (t,b)=(1/(t+sqrt(1+t²−2ct+(1−c²)t²b²)),tb) from (3/4,1/4) for 300 and 400 steps at c=7/8; print b/τ^n, (t−τ)/b² and (1+τ)/(τ²√(1−c²)(b/τ^n)). The numerical agreement is corroboration, not a rigorous truncation bound or a proof of the continuum.

## originality

PASS

The source already gives the fixed-c recurrence, its invariant rectangle, and degeneration bounds. The contribution is the sharp asymptotic analysis, including the second-order displacement and limiting geometry, and the continuum of rates under the general-c LAB mechanism. The closest inspected longest-edge and planar largest-angle results use different refinement maps and do not imply these quantities.

## value

PASS

This turns the motivating mesh counterexample's bounding rates into a sharp orbit law, quantifies the diameter-to-inradius growth, and explains the parameter mechanism producing a continuum of exact rates. The second-order lag and limiting dihedral relation describe the degenerate dynamics beyond the fact of mesh failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
