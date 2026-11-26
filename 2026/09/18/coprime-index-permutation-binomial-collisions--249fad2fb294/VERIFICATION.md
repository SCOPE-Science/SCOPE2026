---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Fan's Corollary 6.1 supplies the exact admissibility criterion. The identity gcd(q^h−1,q^e−1)=q^gcd(h,e)−1 makes every admissible ℓ_h a unit modulo L, and these ℓ_h are distinct integers strictly between 0 and L. The exponent condition modulo q−1 therefore leaves exactly the unit lifts modulo N; reduction is onto by CRT (avoid the primes of N absent from L independently). The coefficient count is N−L. For q>2 neither exponent can be zero modulo N because both equal the unit r modulo q−1. Two representatives giving the same function agree as reduced polynomials by the root bound on the N nonzero field elements. Equal ordered supports give identical data, and reversed supports force a=a′=1, d′=−d modulo L, r′=r+d(q−1). The reverse is admissible by r′=r q^h modulo L and q^hℓ_{e−h}=L−ℓ_h, with gcd(r′,q−1)=1 unchanged. The coefficient 1 is admissible exactly for q,e both odd, and there are no fixed antipodes because L>2. Hence there are exactly E double representations per antipodal index pair contained in D and no larger fibres. For q=2 all coefficients fail the condition. Inspected the frozen exact-integer script and recorded output without executing the uploaded script; it tests exponent/support combinatorics, not permutation by evaluation. A separate replay, python -B /workspace/review-evidence/5/direct_field_count.py, directly evaluated finite-field functions without Fan's criterion. Full-family counts for (q,e)=(2,2),(3,2),(3,3),(4,2),(4,3),(5,2) were 0,16,300,80,3024,144, and six subsets in the odd/odd example included same-sign and antipodal index choices. For (3,3), 288 functions had one representation and 12 had two. These finite checks corroborate but do not establish the general proof.

## originality

PASS

The distinct claim is the full equality-of-functions fibre classification across indices and its parity-corrected count for arbitrary subsets of coprime indices. Fan supplies the admissibility theorem and the fixed-index d=1 count, not this count across indices. The finite exact result is supported to the best of current knowledge, not certified first discovery.

## value

PASS

After the coprime-index admissibility classification there is a natural enumeration problem for functions, rather than parameter triples. The result gives the exact obstruction to multiplying a fixed-index count across indices and classifies every fibre, including its parity boundary and the dependence on an arbitrary restricted index set. The concrete discrepancy 312 versus 300 is a consequence of that general mechanism rather than an isolated computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
