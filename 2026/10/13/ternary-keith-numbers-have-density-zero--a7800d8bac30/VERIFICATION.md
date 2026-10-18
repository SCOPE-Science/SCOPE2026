---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The published Klazar–Luca recurrence comparisons and product-poset antichain bound extend to base 3; verified the missing parameter window by choosing α=7/20 with α>1/3 and 3^α<3/2 (equivalent 2^20<3^13). Exact binomial Chernoff/entropy upper tail shows strings with ≥αn zero digits are ≤3^n e^(−cn). With fewer zeros, at least r≈(1−α)n nonzeros and known recurrence estimates force n·2^{m−n}≈3^n and only O(1) possible recurrence indices m per n. For a common r-digit prefix and fixed m, comparable distinct suffixes in {0,1,2}^{n−r} produce nonzero Keith-sequence difference M both ≳(3/2)^n and <3^{αn+1}, impossible. Hence suffixes form antichain of size O(3^{n−r}/√n); counting prefixes gives O(3^n/√n) n-digit Keith numbers and K_3(x)≪x/√log x. Finite examples are not infinite proof.

## originality

PASS

Klazar and Luca prove the density upper bound for decimal/general base≥4 and expressly flag base3 as unavailable to their parameter inequalities. The new zero-rich binomial large-deviation threshold rather than their crude estimate makes a feasible window at base3 and preserves the rest of their proof. The extension is therefore not literally established by the older published base range and is a motivated genuine missing case.

## value

PASS

Settles the first excluded ternary base of a known Keith-number asymptotic counting theorem with a quantitative density-zero bound, answering a conspicuous gap named in the primary source.

The dated certificate retains the supplied scientific assessment, sources and limitations.
