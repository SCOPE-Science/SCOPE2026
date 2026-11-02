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

# Verification details

The accompanying standalone Python 3 standard-library checker computes the Eisenstein norm, unit group, conjugation, residues at the norm-three and norm-four primes, and every candidate norm-compatible six-point configuration.

It constructs exactly 24 nonzero allowable differences, examines all \(\binom{24}{5}=42{,}504\) rooted candidates, accepts 54 norm-compatible configurations, divides them into three symmetry orbits of sizes 12, 36 and 6, and checks the prime-residue occupancy profiles of each orbit. No candidate has both required almost-uniform profiles. Four separate positive witnesses for degrees one through four also pass the exact residue and difference tests.

Use `python3 verify_eisenstein_optimal.py` in any Python 3 installation with the standard library. The program prints the orbit representatives and profiles, each positive witness, and an explicit `VERIFY_OK` marker when all assertions succeed.

The proof that this finite enumeration is exhaustive uses the restriction that no pair difference is divisible by any prime ideal of residue norm at least six, nor by the square of either prime ideal of residue norm three or four. This restriction is mathematical and universal; the finite check itself cannot prove that prerequisite. The proof and actual program jointly establish the stated result, conditional only on the standard pre-existing local-optimality and \(n+2\) existence theorems, which are cited. No external independent audit has been performed.
