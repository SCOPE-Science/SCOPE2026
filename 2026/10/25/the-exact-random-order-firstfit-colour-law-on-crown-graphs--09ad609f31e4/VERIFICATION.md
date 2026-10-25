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
# Reproduction and limits

The standalone `verify.cpp` uses only the C++17 standard library; compile with `c++ -O2 -std=c++17 verify.cpp -o verify` and execute `./verify`. It directly simulates ordinary irrevocable smallest-admissible-colour vertex arrivals in every order of each \(K_{n,n}-M_n\) for \(2\le n\le5\). There are exactly \(4!+6!+8!+10!=3{,}669{,}864\) orders. For each cardinality it compares the histogram with the differences of two integer-valued predicted tail counts. It independently calculates linear extensions by exhaustive subset dynamic programming on the precedence relations for \(3\le n\le9\), \(1\le t\le n-2\), and compares to the closed-form recurrence (28 checks). The check printed:

`VERIFY_OK exhaustive_crown_orders=3669864 poset_cases=28 maximal_order_count_n5=43200`

The source code and mathematical exposition are included, rather than only a log. The proof of the dichotomy and the poset recurrence is general for all \(n\ge2\). Running finite cases does not by itself certify the infinite statement. Potential historical coverage under other terminology and independent proof review remain unresolved.
