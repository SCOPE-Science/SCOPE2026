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

Gaussian radial Toeplitz eigenvalue identity and repeated integration by parts yield exact S1 distance <= exp(2ε)-1 from each monomial projection, with oscillating finite blocks c_j J P_{<N_j}. N_j=2^(j²), c_j=j/N_j, ε_j=N_j^-3 give summable S_p norms for each p>1. Gaussian-weighted L2 seminorms controlled by recursively spaced R_j ensure admissibility and identify T_g with the S_p operator sum. Heat peaks HB_j(0)=2j E(exp(-s))>=2j exp(-2ε_j), Gaussian cross contributions summable by the separation recursion, so Hg(R_j)>=3j/2. Virtanen trace-class heat bound then rules out S1. The uniform-bump numerical surrogate from the package is not proof for the smooth bump; the integration-by-parts identities are. Remaining technical reliance is the cited endpoint theorem and Fock operator identification.

## originality

PASS

Best-of-knowledge qualified priority: The class T_g∈cap_{p>1}S_p with unbounded critical heat is already established existentially by Virtanen 2609.11853; the added quantifier is a deterministic real C∞ explicitly specified witness with quantified block errors. The quantified already-known claim is existence of some admissible all-p>1 counterexample. The new claim adds a fixed smooth real formula and deterministic separation, not logically implied by mere existence, with further explicit trace-norm blocks. An unsuccessful search is not novelty proof; sources and risks delimit the decision.

## value

PASS

A constructive real C∞ witness is a substantive explicitness gap left by Virtanen’s nonconstructive Baire-category theorem: it supplies a deterministic finite recursion, trace-norm control of actual smooth Toeplitz building blocks and arbitrarily large critical heat peaks, not merely a new name or finite example. The precise S_p/S1 endpoint is natural to Fock Toeplitz operator theory; extreme amplitudes limit applications but not mathematical significance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
