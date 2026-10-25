---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Checked the exact analytic Cesàro coefficient formula (Cf)_n=(n+1)^(-1)sum_{j<=n}f_j and the semigroup S_t/resolvent C=int_0^infty S_t dt with bound ||S_t||<=e^(-t/p) on p>=2. The n-fold semigroup moment formula gives C^(2n) moments t^(2n-1)/(2n-1)!, so any H^q dual annihilator of orbit C^(2n)1 has identically zero analytic sinh transform on |Re z|<1/p; uniqueness of sine Fourier transforms forces the annihilator to vanish, proving C² cyclic for p>=2, transferred by dense inclusion H² in H^p for all p<2. For each lambda with Re(1/lambda)>1+1/p, gamma-ratio coefficients a_n=prod_{j<=n}(1-(1/lambda)/j) decay faster than n^(-1-1/p), making Lambda_lambda(f)=sum a_n f_n continuous even in quasi-Banach H^p. Exact recurrence lambda(a_n-a_(n+1))=a_n/(n+1), checked independently for rational beta=7/2 across n0..7, proves adjoint eigenfunctionals; Vandermonde independence for distinct lambda is exact. Small regular m-gon eigenvalues with ceil(m/2) in the allowed right-sector share one mth power; so mu(C^m)>=ceil(m/2) and m>=3 is noncyclic. The cyclic orbit of C and of C² yields upper bound m and, for 2k, upper k, meeting lower k. Odd m exact multiplicity is explicitly not claimed.

## originality

PASS

The September 2026 Belli–Gül–Ross–Siskakis primary paper proves cyclicity of the original C on H^p; the submitted sharpened assertion is cyclicity of powers and sharp even-power cyclic multiplicity, not the same theorem. Abstract and accessible bibliographic material were compared; arXiv PDF/full HTML retrieval failed and the lawful institutional text request returned vpn_disconnected, so the full primary manuscript was NOT read, and it is a substantial residual risk that the results might occur in an inaccessible appendix. Resultary search showed Cesàro self-commutator, Mellin semigroup and real-variable results but no mathematical implication covering power multiplicities. Best-of-knowledge O PASS with a meaningful source-access limitation, not a claim of exhaustive priority.

## value

PASS

The abrupt C/C² versus C³ cyclicity transition and exact k-fold cyclic multiplicity of C^(2k) are natural invariant-subspace/operator dynamics questions for a classical Hardy-space operator, with a uniform quasi-Banach-to-Banach result. The eigenfunctional spectral-folding construction is structural; this is not merely rephrasing the already-known cyclicity of C.

The dated certificate retains the supplied scientific assessment, sources and limitations.
