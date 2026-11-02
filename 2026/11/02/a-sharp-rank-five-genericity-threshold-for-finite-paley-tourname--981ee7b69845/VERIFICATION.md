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

# Verification and reproducibility

The attached C++17 program enumerates every prime \(q\equiv3\pmod4\) with \(7\le q<191\) plus \(q=27\). These are **all** prime powers in the range: higher odd powers are at least \(3^5=243\) or \(7^3=343\). For each order, the program constructs the actual field and square set; its field of order 27 is \(\mathbb F_3[X]/(X^3+2X+1)\), a field since the cubic has no roots in \(\mathbb F_3\). It directly verifies the antisymmetric tournament relation.

Translation invariance reduces four-subset testing to all unordered triples \(1\le a<b<c<q\) added to \(0\). Every possible sign pattern is checked by exact bitset intersections, excluding the four selected vertices. The output records \(\binom{q-1}{3}\) tested four-sets per order and an explicit first failed pattern when relevant; no random sampling is involved. A second minimum over the all-positive orientation pattern tests \(S_4\). In each checked order, \(S_4\) holds exactly when \(P_4\) holds.

Reproduction commands:

```sh
g++ -O2 -std=c++17 -Wall -Wextra -pedantic paley_tournament_p4_verifier.cpp -o paley_check
./paley_check
```

The attached output is the complete stdout of this command and terminates in `EXHAUSTIVE_FINITE_CASES_OK`. For order 103, the explicit witness \(\{0,1,16,47\}\) has no common dominated vertex. An independent direct quadratic-residue check of that set gave an empty witness list.

The proof for \(q\ge191\) is symbolic and independent of the finite certificate: it uses the exact degree-one and degree-two character sums and Weil bounds for squarefree polynomials of degrees three and four to show every desired extension class has positive size. The theorem makes no claim that finite checking by itself establishes the infinite result.

The logical step uses the five-round Ehrenfeucht–Fraïssé game and the rank-five form of the four-point extension axioms. No independent external audit has been conducted.
