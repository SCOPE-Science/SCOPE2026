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

# Reproduction and boundaries

The analytic argument in `RESULT.md` proves the pointwise iterate identity for finite and infinite base graphs with maximum degree at most two, using only local majority identities. No experiment on a finite sample of graphs is substituted for that argument.

Run `python3 verify_degree2.py`. It checks the exact first-periodic-entry distributions for path and cycle coronas with two through eight base vertices, the degree-three star trajectory, and the unwhiskered odd-cycle comparison for \(m=1,\ldots,12\). Compare its output against `verify_degree2_output.txt`.

Compile `verify_all_small.cpp` with `g++ -O3 -std=c++17 -Wall -Wextra verify_all_small.cpp -o verify_all_small`, and execute `./verify_all_small`. It exhaustively enumerates all labelled simple base graphs with maximum degree at most two on one through six vertices and all binary initial configurations of their one-leaf coronas. It checks the identity \(F^4(z)=F^2(z)\) for each case. Compare its output against `verify_all_small_output.txt`. Across all graph-size instances, it checks 2,163 graph structures and 7,880,484 configuration–graph pairs.

The two implementations differ in graph representation and majority-update logic. Both completed with `VERIFY_OK`. Finite enumeration corroborates the exact local proof but does not itself establish the result for arbitrarily large or infinite graphs. External independent validation has not been performed.
