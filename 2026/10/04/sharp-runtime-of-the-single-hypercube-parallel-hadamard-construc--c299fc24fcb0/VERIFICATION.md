---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The proof is correct. Tensor factorization of the normalized hypercube evolution shows every entry at Hamming distance d has magnitude determined by powers of sine and cosine. Diagonal corrections preserve magnitudes, so flat Hadamard magnitudes force the first positive hypercube time nπ/4. At such a time the entrywise Walsh-to-cube ratio factors uniquely into row and column phases indexed by Hamming weight. Any sequence of nonnegative loop-singleton layers of total duration T assigns each vertex an accumulated time between zero and T; modulo a common scalar the required phases therefore need a directed circular arc of length at least π/2 for n=1, π for n=2, and 3π/2 once four weight classes occur. Nested masks attain those costs. Independent exact phase-identity checks through n=8 reproduce the construction, but the all-n proof is analytic.

## originality

PASS

Best-of-knowledge originality passes with the focal full-text access limitation retained. Herrman--Wong introduce the hypercube simplification and parallel Hadamard construction; Wong supplies the looped-versus-loopless isolated-vertex phase primitive; Chan characterizes uniform mixing and complex Hadamard behavior for cube-related graphs. No checked source or Resultary record states an architecture-sharp elapsed-time lower bound for one normalized hypercube interval sandwiched by arbitrary loop-singleton phase layers.

## value

PASS

The result certifies time optimality inside a concrete dynamic-walk gate architecture already used for parallel Hadamards. Separating the unavoidable hypercube mixing time from the exact diagonal phase-synthesis cost gives a useful architectural lower bound, not merely another implementation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
