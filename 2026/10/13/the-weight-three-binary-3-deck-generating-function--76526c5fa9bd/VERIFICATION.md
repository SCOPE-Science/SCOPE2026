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
# Verification

Run `python3 verify.py` beside `certificate.json`.

The verifier performs three independent finite checks of the all-length proof's ingredients. First, for every weight-\(3\) binary word through length \(12\), it compares the eight closed deck-coordinate formulas with direct enumeration of every three-position subsequence. Second, for every weight-\(3\) word through length \(35\), it groups exact decks, checks that no class has more than two words, and confirms that every two-word class is the uniquely predicted partner pair. Third, through length \(50\), it enumerates all oriented parameters \(a,c,e\ge0\), \(t\ge1\) and matches their count to the coefficient of
\[
\frac{z^7}{(1-z)^2(1-z^2)(1-z^4)}.
\]

The finite replay checks the algebra and the parametrization; the proof in `RESULT.md`, not the finite cutoff, establishes the theorem for every \(n\).
