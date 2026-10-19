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

# Verification of the cubic-chain retraction image enumerator

Run `python3 verify_cubic_retracts.py` in the directory containing this document and the checker. Only the Python standard library is required.

The program enumerates every local polynomial function for \(q=2,3,4\), identifying function duplicates when \(q=2\) due to \(s^2=s\). It verifies exactly \(16,243,1024\) distinct local maps for a fixed output residue, respectively. Separately, it constructs all \(1024\) distinct unary polynomial self-maps of \(\mathbb F_2[t]/(t^3)\), evaluates \(F(F(x))=F(x)\) for each of the eight inputs, and checks every predicted coefficient by number of fixed residue fibers and full fibers.

Observed exhaustive binary rank counts are \(8,16,32,8,1\) for image cardinalities \(1,2,4,5,8\) respectively; total \(65\). The printed terminal condition is `ALL_EXACT_CHECKS_PASSED`.

The proof's infinite-family step is not computer-certified: it follows from Taylor expansion, CRT independence, functional idempotence, and finite combinatorics. The checker uses no external theorem prover and does not establish global literature novelty or independent audit.
