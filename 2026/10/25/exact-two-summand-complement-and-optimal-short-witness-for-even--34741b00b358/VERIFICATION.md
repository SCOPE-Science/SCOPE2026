---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Let w(m)=s_F(m) mod 2, based on canonical weights F1=1,F2=2. The recursion W1=0,W2=01,W_{j+1}=W_j complement(W_{j-1}) follows from unique Zeckendorf leading-weight decomposition and has |W13|=377. Independently enumerated every 21-factor of W13 (132 distinct); W14 has same factors, set complement-invariant, and checked all 20 crossing factors for each of four periodic length20 suffix states S13..S16. The suffix relation S_{j+2}=complement S_j and stable prefix make this a genuine induction covering every future factor, rather than finite-prefix extrapolation. Every such factor has a zero in one of positions 20−a with a∈{0,4,6,7,9,10} and all those a have even weight; hence for every n>=20 some n−a has even weight. Direct finite small checks prove all n=6..19 representable and n<6 exceptions precisely 1,2,3,5. n=34 has no even-parity complement for a<10 among available small-even a=0,4,6,7,9, but 34=10+24 works; thus the uniform maximum 10 is sharp. Independent checker reconstructs the 132 factors, four joins, and all n<3000; the unbounded result is proved by induction.

## originality

PASS

PASS qualified for the exact complement and sharp bounded first summand of the even-Zeckendorf-parity set. Rajasekaran–Shallit–Smith (2020) develop automata for additive questions on Fibonacci representations and explicitly illustrate two Fibonacci-odd sums/differences; the full article could not be read (authorized institutional source returned vpn_disconnected), so it remains a material possible priority risk, and no whole-document noncoverage is asserted. Shallit 2022 studies the same Fibonacci parity word but its theorem concerns maximum-order complexity. No accessible inspected statement logically implies the even-class complement and optimal witness 10. A broader Fibonacci-automatic additive classification could conceivably dominate the result; the finding is best-of-knowledge.

## value

PASS

The exact complement of E+E and the smallest universal short witness are canonical additive properties of the Fibonacci–Thue–Morse parity set, a natural automatic numeration sequence. The finite-factor induction yields a uniform infinite bound and an optimal obstruction at 34, rather than a casual finite initial search or arbitrary numerical threshold. Such a precise bounded representation theorem can be used in later automatic-additive studies without a general theorem being required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
