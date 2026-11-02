---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

One length-k palindromic duplication corresponds bijectively to an inverse start where a 2k block is a palindrome. Two consecutive valid starts enforce a constant 2k+1-symbol overlap, and both deletion histories give the same parent; every consecutive run of valid starts therefore contributes at most one parent and gives upper bound ceil(m/2), m=n−k+1. For k≥3 with 4∤k, explicit period-four words (aabb)^ω when k odd or (abba)^ω when k≡2 mod4 have precisely the even valid starts and pairwise distinct inverse parents, attaining the bound for all n≥k. When m odd≥3, equality forces alternating valid starts 101...01, and composition of palindrome reflections at start separation 2 enforces global period four, leaving exactly q(q−1) distinct maximizing received words (a≠b). For 4|k and n=k+2, starts 0 and 2 force period four but deletion offsets k are period multiples, giving identical parents; adjacent valid starts also collide, hence maximum one. Independent full brute-force enumeration of all binary received words for k=3..7 and n through k+4 under length≤17 reproduced the maximum and odd-m maximizers; no finite check substitutes for the all-n proof.

## originality

PASS

Lenz–Wachter-Zeh–Yaakobi (2017) Appendix A already gives collision/run-based inverse palindrome sphere bounds; the generic upper bound mechanism is not novel. Their same-length-two case also has related abba behavior. Zabokritskiy (2026) counts potential inverse starts and handles forward multiple-duplication problems; it is not shown to classify the sharp all-k inverse parent count. The assessed remainder is simultaneous all-alphabet sharpness for every k≥3 with 4∤k, rigidity and exact maximizer enumeration when m odd, and the first 4|k obstruction. A less-indexed coding lemma could cover this and remains a priority risk.

## value

PASS

The inverse list size controls worst-case ambiguity of a natural DNA palindromic-duplication channel. Its exact maximum, all-symbol period-four extremal rigidity and the true divisibility-by-four threshold answer a motivated finite-alphabet extremal problem; not a mere enumeration of small words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
