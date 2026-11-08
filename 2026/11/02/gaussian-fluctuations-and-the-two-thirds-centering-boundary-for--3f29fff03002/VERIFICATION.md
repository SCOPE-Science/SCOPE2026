---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

At critical aligned Zipf weights, the deterministic mean discovered mass is S_N(A)/H_N, with S_N(A)=sum_i(1-e^-A/i)/i. Splitting the infinite harmonic sum and subtracting i>N gives S_N(A)=log A+2gamma-A/N+O(1/A+A/N^2+A^2/N^2). Consequently its exact root is A_N=c_theta N^theta+c_theta^2 N^(2theta-1)+O_theta(1+N^(3theta-2)). The variance of the unnormalized discovered sum satisfies A V_N(A)->1/2 and A S_N'(A)->1; the triangular-array Lindeberg bound comes from isolating i<=A^(2/3), which are discovered with overwhelming probability, while all remaining scaled summands vanish. Threshold-event inversion yields (T_N/H_N-A_N)/sqrt(A_N)=>N(0,1/2), and replacing the exact root by first-order centering creates the theta=2/3 transition. Independent high-precision finite sums and root finding for N=5000,20000,80000 and theta=1/2,2/3,0.8 checked slope and variance convergence and the positive second correction.

## originality

PASS

Müller–Šebek 2026 establishes the exact first-order critical Zipf scale and c_theta constant, which are credited. The precise Poissonized first-arrival hitting-time CLT and second-order finite-cutoff center shift are distinguished; related infinite occupancy CLTs use a fixed summable frequency law, not the finite N harmonic triangular array. The direct 2026 paper full text was unavailable by arXiv/OA and authorized institutional access returned vpn_disconnected: this limits originality confidence but is not a correctness refutation or automatic O failure.

## value

PASS

A sharp uncertainty law and finite-population bias threshold answer a natural question left by a first-order quorum-time theorem. The two-thirds boundary determines when a commonly used leading center gives wrong Gaussian uncertainty quantification, and is not a tiny numerical constant improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
