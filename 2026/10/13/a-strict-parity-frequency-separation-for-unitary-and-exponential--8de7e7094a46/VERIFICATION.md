---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The prime-power quotient is rho_p(a)=(1+p^a)/sum_{d|a}p^d (with rho_p(0)=1); rho_p(1)>1 and rho_p(a)<1 for a>=2. Disjoint odd valuation cylinders for p<=19, conditioned on odd parity and squarefree at all larger primes, have exact mass W_o=31076642675170427132493824/35968987080950832137604375 and 18058 selected vectors. The Euler-product factor and pi<22/7 yield strict liminf>17/20. Selected even cylinders have 32591 vectors, mass W_e=38646621072482317819/148330460379458857500 >13/50 and small-prime ratio<11/12. The infinite tail product T is controlled by a convergent 100th moment; prime-product rational bound B<1/70 and Markov give even failure density >897/3500, hence success limsup <3/4. Checked convergence of conditional divisor-sum moment by g(q)=O(1/q) and finite-modulus CRT, not inferred from finite patterns. Independent code rederived both masses/counts and moment bound.

## originality

PASS

Trudgian asks the overall comparison-frequency question and supplies a squarefree lower bound; his Section 4 does not give separate odd/even conditional inequalities. The complete published finite-cylinder result 831dd476bf82 proves only an unconditional overall lower bound 0.753659844..., which cannot imply the contrasting conditional bounds. Best-of-knowledge PASS with unindexed analytic-number-theory risk.

## value

PASS

The two conditional populations of a classical unresolved comparison-density problem have provably separated frequencies by more than 1/10. Distinct analytical lower and upper density arguments are required; it is not an arbitrary short finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
