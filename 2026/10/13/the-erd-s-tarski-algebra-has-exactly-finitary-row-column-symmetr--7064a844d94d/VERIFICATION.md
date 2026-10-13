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

The bundled script `verify_erdos_tarski_automorphisms.py` uses exact finite combinatorics only. It is a supplementary replay of the order-theoretic core of the proof, not a substitute for the compactness argument.

It performs the following checks:

1. For every \(1\le n\le6\), it enumerates every pair of permutations \(a,b\in S_n\) and verifies that
   \[
   a(i)\le b(j)\iff i\le j\quad(0\le i,j<n)
   \]
   has the unique solution \(a=b=\mathrm{id}\).
2. On the same ranges it verifies that
   \[
   a(i)\le b(j)\iff i>j
   \]
   has no solution, matching the obstruction to swapping the two compactification points.
3. For explicit finite-support coordinate permutations on boxes through size seven, it checks that the triangular relation changes only in rows or columns meeting the support, the finite analogue of the compact-symmetric-difference converse.

Expected terminal line:

`VERIFY_OK 2609228 exact assertions/comparisons`

The general proof additionally uses the elementary facts that compact subsets of \(((\omega+1)^2)\setminus\{(\omega,\omega)\}\) avoid some neighborhood of the deleted corner, and that an eventually strictly increasing permutation of \(\omega\) is eventually the identity.
