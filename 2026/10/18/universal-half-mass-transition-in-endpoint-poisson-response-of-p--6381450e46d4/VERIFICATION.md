---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

For mean-zero f, bridge current equals F=sum_H f=−sum_path f, path differences satisfy u(j)−u(j−1)=sum_{k≥j}f(k). On H, write u=a+v, v=L_H^dagger(f_H−F 1_o), and impose global mean zero to derive exactly u(p)=sum_{k=1}^p b_k f(k)+(m/N)v(o), b_k=[mk+k(k−1)/2]/N. The spectral gap gives |v(o)|≤(m+√m)/γ. Optimizing the reduced linear functional over the zero-sum unit cube is rigorously the minimum ℓ1 deviation from a constant, thus T0=min_c(m|c|+sum|b_k−c|). Riemann scaling B_λ(x)=λx+x²/2 with coefficient/Riemann error ≤1/N yields continuous median profile: an atom of mass λ at zero drives a switch when λ=1/2, giving the two explicitly integrated cubics and one-sided Φ′′ values −1,0. For clique H=K_m the Green head term produces exact coefficients −1/N repeated m−1, 0, and b_k; median identity follows. Independent SciPy pseudoinverse/median comparisons for (m,p)=(2,1),(2,3),(3,3),(5,4),(8,2) agree to numerical precision. General uniform limit holds for γ bounded below; no full-matrix operator norm asserted.

## originality

PASS

Palacios–Gómez–Del Río 2014 derives hitting time identities via electric voltages, including cut-edge formulas; Beveridge 2015/2016 derives Green kernel entries from hitting times; Jonasson proves extremal lollipop commute times. These classical identities do not evaluate the sharp balanced ℓ∞ mean-zero forcing at the tip or its atom-induced half-mass cubic phase transition, nor give quantitative head-gap uniform bounds. The exact median duality is standard convex optimization and is credited; its graph-specific coefficient formula and universal phase profile are the assessed contribution.

## value

PASS

Bounded-source Poisson response of graph Laplacians is a natural stability/amplification invariant. The sharp tip profile for any uniformly gapped head, the nonsmooth second-derivative half-mass transition and factor-four endpoint amplification are precise reusable facts for Green operators on lollipop-style graphs, not arbitrary numerical examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
