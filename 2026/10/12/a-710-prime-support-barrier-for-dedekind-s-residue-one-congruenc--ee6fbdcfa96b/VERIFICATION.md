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

The universal proof is in `RESULT.md`. The attached `certify.py` checks all \(32\) subsets of \(\{3,5,7,11,13\}\), identifies all \(15\) compatible patterns, and computes the first \(709\) eligible prime factors for each using an exact Eratosthenes sieve through \(20{,}000\). All eligible lists have more than \(709\) entries below that cutoff, with the largest 709th eligible prime \(14{,}731\).

For every pattern it checks, using arbitrary-precision integer multiplication,
\[
\prod_{j=1}^{709}(q_{S,j}+1)<3\prod_{j=1}^{709}q_{S,j}.
\]
The maximum exact rational ratio belongs to \(S=\{11,13\}\) and is strictly less than \(3\); its 710th factor passes the threshold, illustrating why 709 is the limit of this particular five-prime majorant.

An independent, limited direct computation tests Dedekind-psi residue-one membership for every integer from \(2\) through \(100{,}000\), finding exactly the primes in that range. **This bounded scan is not the proof of the unbounded theorem.** The finite inequalities provide the certificate for the universal monotonic support argument.
