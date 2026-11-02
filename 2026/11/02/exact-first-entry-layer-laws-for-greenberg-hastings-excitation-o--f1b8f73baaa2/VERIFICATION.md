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
# Reproduction of first-entry layer checks

Run `python3 finite_certificate.py` using Python 3. The code enumerates every admissible 0/1/at-least-2 nonhub-color class and compares each of the thirteen labelled first-periodic-entry exponential generating functions against its proposed formula as a formal polynomial identity. It does not extrapolate from a finite range of graph sizes. The exact output recorded during execution is in `finite_output.txt`.

Independently, compile `independent_direct.cpp` with `g++ -O3 -std=c++17 independent_direct.cpp -o check_direct` and run `./check_direct`. The checker updates every individual vertex color directly and compares all observed least periods and first-entry layer counts for twelve complete state spaces, including both small-order boundary cases and the graph with two six-vertex cliques. Exact execution output is in `direct_output.txt`.

These checks provide a complete finite symbolic proof of the displayed all-size expressions and an independently structured finite-size cross-check. They do not certify any different update rule, any uninspected graph family, or the absence of mathematically equivalent prior literature. Independent audit was not performed.
