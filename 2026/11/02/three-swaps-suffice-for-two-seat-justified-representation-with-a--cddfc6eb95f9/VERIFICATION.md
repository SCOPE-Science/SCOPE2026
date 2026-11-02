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

# Reproducibility and exact checks

Run `g++ -O2 -std=c++17 -Wall -Wextra verify.cpp -o verify` followed by `./verify` with GCC or Clang in C++17 mode. The source uses only the C++ standard library and the compiler's integral population-count intrinsic. It enumerates anonymous profiles by nonnegative integer multiplicities for every subset of candidates, including the empty subset; consequently voter permutations are immaterial and the search is exhaustive for the declared sizes.

The verifier computes the JR predicate directly from uncovered approvers and tests each candidate using exact integer inequality \(2u_c(W)<n\). It builds the induced exchange graph on all JR pairs, runs breadth-first search from each vertex, and checks connectedness, diameter at most three, and (in tested small cases) equality to the Johnson-graph distance. All approval multiplicities, inequalities and distances are integers. The separate six-voter witness check tests both endpoints, every one of their four cross pairs, and all four committees containing the universal candidate.

An executed compiler/run produced `verification_output.txt`. The largest enumerated strata have \(490{,}314\) anonymous four-candidate eight-voter profiles and \(376{,}992\) anonymous five-candidate five-voter profiles, with no disconnected or nongeodesic JR committee pairs. The explicit six-voter five-candidate witness printed `shortest_path_length=3`.

The proof of universal connectivity and the three-edge bound is analytical; it is not inferred from enumeration. The claim of first detour at six voters among five-candidate markets is finite exhaustive and depends on correct implementation of the supplied program and compiler. Independent audit is not recorded here.
