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

# Reproduction of finite checks

The two included programs are independent finite checks of the formulas, while the unrestricted proof is in `RESULT.md`.

1. Compile `verify.cpp` with `g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify.cpp -o verify` and execute `./verify`. It constructs each graph edge by edge and updates every state by the parity of bit-masked open neighborhoods, with no use of the symbolic proof's coordinate reduction. `verification_output.txt` gives the observed 24 graph parameter pairs and aggregate **827,208** configurations, evenly split between immediate-periodic and one-step entrants. It tests \(F^7=F\), the four iterate-fixed counts, and primitive-orbit integrality for every enumerated configuration.
2. Execute `python3 rank_check.py`. It builds adjacency rows anew and computes binary matrix products and ranks by exact integer-bit elimination. `rank_output.txt` records checks across 168 parameter pairs \(0\le p,q\le12\), excluding the empty graph, reaching 73 vertices. This independently confirms \(\operatorname{rank}A=n-1\), \(A^7=A\), and \(\dim\ker(A^j-I)=d_j\) for \(j=1,2,3,6\).

Neither a finite enumeration nor a successful process exit proves the assertion for arbitrary \(p,q\); the symbolic invariant-subspace and fixed-space derivations are required for that conclusion. The code uses only local binaries and standard C++/Python facilities, and does not depend on external files other than those embedded alongside it.
