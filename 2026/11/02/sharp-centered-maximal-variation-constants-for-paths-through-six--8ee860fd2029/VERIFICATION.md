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

# Exact verification and proof boundary

The complete reduction in `RESULT.md` shows that the \(\ell^1\)-sphere, intersected with the rational comparison/coordinate hyperplane arrangement, consists of convex cells on which maximal-function variation is convex. Every cell vertex is captured by an oriented rank-\((n-2)\) intersection ray. This mathematical argument, not numerical sampling, makes the finite comparison exhaustive for arbitrary real input.

Two independently implemented programs are provided: `path_maximal_exact.cpp` and `path_maximal_independent.py`. Run `c++ -std=c++17 -O2 path_maximal_exact.cpp -o path_maximal_exact && ./path_maximal_exact` and `python3 path_maximal_independent.py`. Both were executed against the packaged source. For \(n=5\), each generated 27 hyperplanes, 2925 normal triples, 2829 full-rank triples, 5658 oriented rays and 288 equality occurrences counted with multiplicity; for \(n=6\), 46 hyperplanes, 163185 quadruples, 151429 full-rank quadruples, 302858 oriented rays and 7268 equality occurrences. Every exact integer inequality passed in both programs.

For the endpoint impulse \(f=(0,\ldots,0,1)\), the input variation is \(1\) and the output variation is \((n-1)/n\). All other equality cases, larger path lengths and other exponents are outside the verified theorem. Independent external mathematical audit has not been performed.
