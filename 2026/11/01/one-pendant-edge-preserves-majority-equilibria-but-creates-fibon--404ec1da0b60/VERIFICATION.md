---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For synchronous tie-retaining strict-neighbor-majority on C_n with one leaf, symmetric integer W with diagonal tie-retention loops makes all local fields odd and nonzero; the two-time Lyapunov pairing increases strictly unless s(t+1)=s(t-1), establishing eventual period at most two for all n>=3. A flip at any degree-two rim vertex forces neighbors to flip; propagation yields the all-flip alternating even-n orbit. Otherwise only root/leaf flip with endpoints opposite and all interior constant runs length >=2. Opposite endpoints imply an even number of runs, giving generating function 2R(z)^2/(1-R(z)^2), R=z²/(1-z), coefficient F_{n-2}-q_{n-3}; add one even-n alternating orbit. Fixed states require no singleton runs, counted by trace of four-state transfer matrix with char polynomial (lambda²-lambda-1)(lambda²-lambda+1), hence H=L_n+2cos(pi n/3). Independently enumerated all states at n=3,...,10 and agreed with both formulas (H,N): (2,0),(6,1),(12,2),(20,5),(30,6),(46,9),(74,12),(122,21). The finite check corroborates the all-n proof.

## originality

PASS

Classical Goles-Olivos/Benjamini et al period-at-most-two theorem is recognized and used only as context; it does not give a complete labelled recurrent-orbit census after one extra pendant edge. Haslegrave-Cannings one nonconformist changes an update rule, not graph neighborhood, and examines possible periods rather than this Fibonacci count. No statement-equivalent or stronger coverage found; historical priority risk in local-rule combinatorics remains.

## value

PASS

One local graph perturbation leaves equilibrium count unchanged yet creates Fibonacci-many distinct genuine two-cycles, including two-cycles on odd cycles previously admitting none. The structural flip-set classification and exact transfer/run-count formulas expose a nontrivial amplification phenomenon that a future study of local perturbation dynamics can use; it is not a routine restatement of period-at-most-two.

The dated certificate retains the supplied scientific assessment, sources and limitations.
