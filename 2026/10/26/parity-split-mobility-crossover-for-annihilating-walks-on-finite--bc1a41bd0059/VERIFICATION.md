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

The claim specifies a finite K_{1,m}, integer m>=1, total hub departure rate nu>0 (not per-edge), unit departure from each occupied leaf, uniform hub destination, instantaneous pair annihilation, and hitting time of <=1 particle. For a hub-vacant state B_k, b_0=b_1=0 and b_k=1/k+a_{k-1} for k>=2. For hub-occupied A_k, a_0=0 and (k+nu)a_k=1+k(1+nu/m)b_{k-1}+nu(m-k)b_{k+1}/m. With b_{k+1}=1/(k+1)+a_k when k<m and an empty final term when k=m, this becomes a_k=b_{k-1}+(t+c)/k-d/(k+1), t=m/(m+nu), c=m*nu/(m+nu), d=nu(m+1)/(m+nu). At k=1,2 the boundary b_0=b_1=0 applies; at k>=3 this is a_k-a_{k-2}=1/(k-1)+(t+c)/k-d/(k+1). Summing separately by parity gives the two exact harmonic formulas printed in RESULT.md and b_k. Finite state, strict decrease in particle count at collisions and positive probability of collision from each transient state yield finite mean and uniqueness. Substituting k=m yields the full-occupancy formulas. Harmonic asymptotics give for fixed nu the even/odd logarithmic constants gamma_E+nu(1-log2)-1 and gamma_E+nu log2, respectively; odd-minus-even is 1+nu(2log2-1)>0. For nu_m=o(m), errors from t-1 and c-nu_m are o(log m+nu_m); for nu_m/m->theta in (0,infty) divide by m and obtain theta/(1+theta) times 1-log2 (even) or log2 (odd). Independent numerical generator solves, not supplied verifier logs: full labeled generator transient systems m=1..6 with nu in {1,3,2m+1}, totaling 657 transient state comparisons, max absolute discrepancy <1.5e-13; 8 additional asymptotic spot checks for m=1001,1002,10001,10002 with fixed nu=2 or nu≈m/2 show convergence. These finite calculations are corroborative only; infinite result follows from analytic recurrence and harmonic estimates. Independently reconstructed Git tree SHA from seven file blobs equals ffcdd9afa3efd479b4481ae4e2855365553b02e8.

## originality

PASS

Qualified best-of-knowledge novelty for the arbitrary positive site-dependent hub-total-rate all-initial-state continuous-time expectation and its two parity-specific rate-scaling limits. A closely related single-species star system is explicitly covered in Cristali et al. Proposition 1: homogeneous discrete move-count distribution for 2n initially occupied leaves with empty hub, NOT a fresh finding. Its transition-step law does not provide arbitrary hub-total-rate clock means without another generator calculation. Athreya-Swart develop general constructions and dualities; Krapivsky-Ben-Naim-Redner study particle-specific heterogeneous diffusion densities on extended systems. Full preprints inspected. Searches of published findings and literature did not exhibit the matching all-rate claim; nonhits do not prove originality. General finite-state resolvent methods could mechanically produce these formulas when applied with this generator, and unknown prior star-specific papers may exist; those are residual priority risks.

## value

PASS

The expected time for irreversible pair annihilation on a natural high-degree finite network is a meaningful kinetic observable. Changing the total central departure rate while fixing leaf clocks creates a nontrivial site-mobility parameter and reveals parity-sensitive behavior of the fully occupied system. The result gives exact all-initial-state finite means and identifies both the logarithmic-order rate where a new leading logarithmic coefficient appears and the order-m rate with different nonzero linear-time constants, all with explicit coefficients. A future investigator comparing mobility prescriptions, annihilation-vs-coalescence, or discrete-vs-continuous clocks could use these exact reference formulas. This is a modest but genuine self-contained structural/asymptotic fact; not a general-graph theorem, higher-moment law, or claim that elementary lumping itself is novel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
