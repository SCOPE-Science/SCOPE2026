---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For the infinite 0->01,1->00 fixed point p, the exact identity p_{2i}=0, p_{2i+1}=1-p_i and valuation p_i=nu_2(i+1) mod 2 imply recurrence of any fixed factor at arbitrarily high 2-adically shifted positions. The base C_(1,1)(d) comprises (00),(01),(10) for odd d and all four pairs for even d. Splitting starting indices by parity gives exact even/odd decimation identities for ordered paired windows C_(a,b)(d); each reduced pair has maximum window length <max(a,b), while translating d by 2^(1+ceil(log2 max(a,b))) preserves d parity and moves reduced separation by a multiple of its induction period, including boundary d>=a. Hence pure periodicity holds for arbitrary a,b>=1 and every admissible d, not merely eventually. The a=b=2 sets A (d=2 mod4, six pairs), B (odd d, seven), D (d=0 mod4, seven) and least period 4 follow by substituting base maps. I independently generated a 32768-symbol prefix and checked exact C spectra/period shift for 110 mixed a,b,d sample cases, including two-letter table; the proof, not that finite prefix, supplies the infinite statement.

## originality

PASS

PASS, qualified. Rigo–Stipulanti–Whiteland define the exact equal-length boundary sets and establish automaticity for automatic words; that does not imply pure periodicity. The full primary paper was materially inspected. The highly relevant Huang–Wen occurrence/return-word manuscript remained inaccessible after authorized institutional access reported VPN disconnected; this is a named priority risk rather than a scientific rejection.

## value

PASS

The extended boundary-set invariant of a canonical automatic word is shown to satisfy a substantially stronger pure-periodic dyadic separation law, with an explicit period uniform across unequal window lengths and a sharp small-length classification. Automaticity alone permits aperiodic behavior. This is a natural combinatorics-on-words refinement useful for exact factor-boundary queries, not a routine renaming of the valuation formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
