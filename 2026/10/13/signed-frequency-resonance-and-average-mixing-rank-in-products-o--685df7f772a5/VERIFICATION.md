---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Since A(K_n)=J−I, U_n(t)=exp(−it)[I+(exp(int)−1)J/n]. Its Schur transition probability is P^0+(n−2+exp(int)+exp(−int))P^1/n. For a Cartesian Kronecker sum, U(t) and M(t) tensor factor synchronously. Time averaging selects only zero Fourier frequencies. Tensor idempotents P_S then yield exact indexed eigenvalues and multiplicities; every coefficient is a sum of nonnegative weights (zero selection allowed exactly for n>=3), proving the signed-balance condition and the iff positive definite property. For three factors (2,m,n), all 4 sectors without the binary factor have positive λ and total rank mn; of sectors with binary factor only full sector can balance, iff |m−n|=2, restoring (m−1)(n−1) rank. Independent numerical spectral-projector Schur-square calculation gave ranks 12 for (2,3,4), 23 for (2,3,5), 39 for (2,4,6), 9 for (2,3,3), 4 for (2,2,2), and 9 for (3,3). One exact SymPy direct-rank attempt timed out; no impossibility inference was made, and analytic proof establishes the unbounded statement.

## originality

PASS

Godsil and Coutinho–Godsil–Guo–Zhan give the general Schur-square projection identity, and individual clique evaluations are classical. Neither inspected primary text states the mixed-alphabet constant-Laurent-coefficient indexed spectrum nor classifies the sharp binary/nonbinary signed-resonance rank jump. The generic spectral recipe can reconstruct a given finite graph but does not itself supply this all-parameter arithmetic coefficient classification.

## value

PASS

The average-mixing rank is a natural quantum-walk invariant. The complete mixed-alphabet tensor spectrum and sharp first nontrivial resonance characterize where the rank jumps for an infinite graph family, treating eigenvalue collisions rather than assuming independent factor time averages.

The dated certificate retains the supplied scientific assessment, sources and limitations.
