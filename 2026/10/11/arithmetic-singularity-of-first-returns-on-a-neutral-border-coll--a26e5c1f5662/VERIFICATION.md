---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For τ=2cosφ∈(-2,2), δ_R=1 and any left trace ℓ, the right-affine first coordinate before a switching hit is exactly X_n=(1−cos((n+1)φ))/(2−τ)+e sin((n+1)φ)/sinφ for x(0)=1/2+e. The first return is N(x)=min{k≥1:X_(k−1)≤0}: x≤0 returns immediately, while right iterates produce negative second coordinate until left branch is used. For rational α=p/q the first-coordinate sign is positive at the tangent point until k=q and X_(q−1)=0 for every x. For irrational α, factorization into 2sin(θ/2)[r sin(θ/2)+(e/sinφ)cos(θ/2)] proves one-sided target arcs with exact inclusive endpoint, ε(e)=arctan(2|e|tan(φ/2))/π. Density gives eventual returns for e≠0 and none for e=0. Badly-approximable lower bound ||kα||≥κ/k gives N≥c/|e|; convergent residues ±1 mod q_j and q_j≤O(1/ε) for bounded partial quotients give N≤C/|e| on both sides. Unbounded partial quotients provide k_j||k_jα||→0 and corresponding e_j with |e_j|N(x*+e_j)→0. Uniform return boundedness away from x*=1/2 plus layer cake yields Leb{N>n}=Θ(1/n) on [0,1] and divergent mean for bounded type. Independent SymPy check confirmed exact ellipse invariance under the right map and representative rational first returns q=3,4,6; all-parameter statements rest on these exact proofs, not on the repository's reported 309 finite diagnostics. The only use of the left trace is after return, so ℓ is genuinely arbitrary.

## originality

PASS

Qualified novel boundary first-return arithmetic. Sushko–Gardini 2008 proves the neutral invariant tangent ellipse and center quasiperiodicity, which are explicitly prior. Simpson 2025 §6.2 studies the same determinant-one center line, rotation-number branches and Arnold tongues, but does not establish the off-ellipse first-section return law or arithmetic tail. Simpson 2026 return theorems explicitly assume repelling determinant δ_R>1 and do not cover the neutral case. Classical continued-fraction and shrinking-target recurrence bounds are standard antecedents, not newly claimed. The matching Resultary record is the assessed finding itself, not independent precedent. No independent primary claim found covering this exact theorem, with unindexed and journal-version overlap retained as priority risks.

## value

PASS

A neutral focus is a natural singular boundary separating center and repelling focus regimes in this piecewise-linear family. The result classifies the full real horizontal section by finite versus infinite return, provides an exact one-sided circle-code, identifies a sharp arithmetic condition for uniform inverse-distance blowup, and derives a 1/n heavy tail and infinite mean under finite-section Lebesgue sampling. These are motivated quantitative return-time statistics, not merely repackaging the known invariant ellipse. It is limited to δ_L=0, δ_R=1, μ=1 and bounded-type tails; no claim of a new general shrinking-target theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
