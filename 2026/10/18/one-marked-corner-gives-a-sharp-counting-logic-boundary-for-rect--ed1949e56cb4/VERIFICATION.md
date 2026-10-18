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

# Verification

**Reproducible commands** (Python 3.8+; no third-party dependencies):

```sh
python3 verify_corner_grids.py
python3 verify_small_square_forcing.py
```

Observed output:

```text
PASS: 88 grid sizes; canonical partitions, switched witnesses, connectivity and colour-sensitive four-cycle counts
PASS: side 2 equitable labelled completions 1 one isomorphism class
PASS: side 3 equitable labelled completions 4 one isomorphism class
```

The first program independently constructs all tested grids, runs globally canonically encoded colour refinement, and checks the orbit-partition claim. For square sides \(4\) through \(12\) it constructs the changed matching and checks equality of joint-refinement histograms, connectedness, and the distinct number of four-colour four-cycles. The second program enumerates the forced equitable bipartite matching choices and verifies by explicit vertex maps that each yields an isomorphic small square.

These computations are finite. The full parameter range follows from the structural proofs in `RESULT.md`. No external formal proof or independent audit has been performed.
