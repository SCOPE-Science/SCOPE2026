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

Run `python3 verify_fibonacci_visibility.py` in a Python 3.10+ environment. It uses only the standard library and does not read any auxiliary data file.

The code enumerates Fibonacci words directly and computes graph edges as legal bit flips. It independently identifies eligible vertices by checking whether distinct neighbors of a candidate have a second common neighbor, and by the zero-run condition. The two descriptions agree for all words of lengths \(2\) through \(14\). For lengths \(2\) through \(6\) it checks all subsets of the eligible vertices against a fresh all-pairs shortest-path search in the original graph. For lengths \(2\) through \(14\) it also enumerates independent sets in each component of the conflict graph by the include/exclude identity, multiplies the component polynomials, and verifies the component edges against all actual distance-two midpoint pairs. It asserts the coefficient recurrence and greedy lower bound in every tested dimension.

Expected maxima from the recursive finite check for dimensions \(2\) through \(9\) are respectively \(2,3,5,5,9,12,14,24\). These are not premises of the proof and are not claimed as independently certified numerical publications. Successful execution ends with `VERIFICATION_OK`.

The universal claims are proven by the distance-two rerouting lemma, the zero-run equivalence, a rational generating function, and the greedy independent-set bound. The only nontrivial asymptotic algebra is the factorization \(1-z^2-z^3-z^4=(1+z)(1-z-z^3)\), with the unique smallest-modulus pole at \(z=1/\lambda\), where \(\lambda^3-\lambda^2-1=0\). The verifier cannot establish priority or exclude an overlapping unpublished result.
