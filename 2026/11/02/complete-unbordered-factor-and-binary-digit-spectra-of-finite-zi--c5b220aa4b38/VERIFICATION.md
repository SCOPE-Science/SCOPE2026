---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

This PASS applies to repairs/3/RESULT.md, not the literal unrestricted family sentence in frozen RESULT.md line 6. That sentence omitted 'unbordered': at n=r=2 the factor a1 a2 a1 has greatest letter a2 and i=j=1, so it contradicts the unrestricted assertion. The repair states the qualifier, distinguishes the all-factor family, and corrects the script's Python requirement to 3.10. In the repaired theorem a proper border cannot use the unique middle letter; hence only a left prefix and right suffix can match. If both top bits are one, the suffix-lower-block, top letter, prefix-lower-block word occurs at both ends, giving a proper border. If one top bit is one, a candidate reaching the top letter cannot match on the other side; the remaining tests are exactly the lower-bit tests, as they are when both top bits vanish. This proves the iff by induction down to the single marker. The marker position and length ensure uniqueness; factors avoiding higher letters lie in copies of Z_r. Disjoint bits add without carries, so length ℓ determines which bits to distribute between two sides and each of the s2(ℓ−1) bits gives two choices. The allowed ranks give n−ceil(log2 ℓ), including ℓ=1 and n=1, the length maximum has only the top rank, and independent three-way bit choices sum to (3^n−1)/2. Independent direct border checks in branches/d2d340da-216b-4b91-99e8-98649a997a14/literal_border_repro.py (literal_border_results.jsonl) matched full families and spectra at ranks 1–8 and all 21,845 marker tests at m=0,…,7; those checks are not the general proof.

## originality

PASS

For the repaired claim, credit is limited to the bitwise border filter and the exact distinct-factor spectrum it yields. The unrestricted all-factor parametrization is already present in Wojcik's slides and a distinct Resultary record; the revision gives explicit credit. The dyadic closed-factor theorem is close in method, but its test is for an exactly-twice border, not for the existence of a border at any bit position.

## value

PASS

Unborderedness measures loss of prefix–suffix repetition in a recursively palindromic word. The exact iff converts that string property to a binary test; the spectrum reveals a sharp half-length cutoff and popcount multiplicities at every rank. It distinguishes a natural class from all factors and from the closed and fixed-order Lyndon subclasses, and is useful without enumerating substrings. This value survives the necessary wording correction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
