---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The stationary (X,Y) Markov generator on x^i y^j is −(i+ρ1_{j>0})x^iy^j+i x^{i−1}y^{j+1}+j(j−1)x^iy^{j−2}. Independently solved all degree≤4 moment recurrences, built 6×6 cubic semigroup generator in basis (x³,x²y,xy²,y³,x,y), and used rational matrix resolvent to verify the claimed exact Laplace transform of Aρ(t)=E[X0³Xt]−E[X0Xt³] for arbitrary symbolic ρ,p>0. Fresh direct matrix-generator differentiation gave derivatives n=0,1,2 identically zero, n=3 equal 72(2ρ²−3ρ−3)/(ρ(ρ+1)²(ρ+2)(ρ+3)) and n=4 equal −24(7ρ²−14ρ−12)/(ρ(ρ+1)²(ρ+2)), positive at ρ*=(3+√33)/4. Leading pole residues give negative long-lag for ρ<1 and positive for ρ>1, with explicit ρ=1 double pole; hence 1<ρ<ρ* has a sign reversal. Sign symmetry kills lower odd moments, covariance symmetry kills degree two, proving fourth-degree first nonzero witness; all moments finite under exponential renewal ages.

## originality

PASS

For Fourth-order time-direction statistic and lag sign reversal under harmonic filtering of resetting Brownian forcing: exact final statement and implication were compared against relevant published original mathematical statements and Resultary findings. The novel rational transform is not a corollary of the limited prior moments without the new polynomial-semigroup computation; the same model's stationary distribution is prior work. Best-of-knowledge qualified by explicitly named risks.

## value

PASS

A sharp observable-only irreversible temporal statistic for a physically motivated stationary non-Gaussian forcing model (despite covariance equivalence to a reversible Gaussian process) identifies a nontrivial reset-rate transition and lag-dependent sign reversal. The exact rational Laplace law and rate/lag boundaries provide diagnostic structure beyond known stationary marginals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
