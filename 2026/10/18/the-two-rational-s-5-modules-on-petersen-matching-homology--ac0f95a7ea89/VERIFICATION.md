---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and verification

Run `python3 verify_invariants.py` and `python3 verify_character.py` from the directory containing these files. Both use only the Python 3 standard library. No external datasets, downloaded graph definitions, or precomputed chain matrices are needed.

The first program enumerates matchings using the complement-of-line-graph definition, constructs the fixed chain complexes for all seven conjugacy types, and calculates **exact rational** invariant differential ranks by Gaussian elimination over `fractions.Fraction`. It also checks signed boundary equivariance on every enumerated orbit. Its final line is `INDEPENDENT_ORBIT_PROOF_OK`.

The second program creates the Petersen graph with a different edge ordering, computes oriented simplicial boundaries over a large prime field, explicitly traces the induced action on all five boundary-image spaces, and uses chain additivity to recover the two homology-character rows. Its final line is `DIRECT_CHAIN_CHECK_OK`. Because rational ranks and characters are already obtained by the first program, no claim that a modular calculation by itself proves an exact rational result is necessary.

The invariant-chain construction includes the augmented empty simplex and uses the alternating deletion boundary. For each cycle type the code exhausts all coherent oriented simplex orbits and all differential columns; seven cycle types cover all 120 group elements by conjugacy. At no stage are an ordinary matching complex and a two-matching complex conflated. The checks establish precisely the rational \(S_5\)-representation stated in `RESULT.md`, not an integral or equivariant-homotopy classification.

Scientific limitations and possible unindexed prior computations remain as stated in `RESULT.md`. Independent review of these artifacts has not been performed.
