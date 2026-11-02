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

For every three-one circular binary word with cyclic zero gaps (a,b,c), a rotation beginning at a marker has form 1 0^R 1 0^T 1 0^L; examining all proper border starts at either later marker shows it is unbordered iff L>R. A rotation beginning at the first zero after a marker is the reversal counterpart and is unbordered iff R>L; all other start positions share the same first/last zero and have a one-symbol border. Thus each unequal adjacent gap contributes exactly one unbordered rotation, and equal gaps contribute none. If gaps not all equal the word is primitive (its proper power exponent would be three, forcing equal gaps), hence U=1_{a!=b}+1_{b!=c}+1_{c!=a} is a count of DISTINCT conjugates, with possible values 0,2,3. For m zeros there are B=binom(m+2,2) ordered triples; all-equal δ=1_{3|m}, two-equal necklaces P-δ with P=floor(m/2)+1, and all-distinct (B-3P+2δ)/3. Orbit-size weighting yields E U=3(1-P/B) for uniform linear words. Independent direct border checks on every three-one linear word for m=0..15 confirmed necklace distribution and expected counts, including periodic case m=0; proof is for all m. The four-marker counterexample explicitly limits scope.

## originality

PASS

Holub–Müller's primary 2015 paper classifies words with exactly two unbordered conjugates by fully bordered pairs; it does not in the inspected theorem specify the three-one gap-local position law nor the full exact distribution including three unbordered conjugates. Clokie–Gabric–Shallit's 2019 paper analyzes unrestricted random binary words, unlike fixed three-one content. Harju–Nowotka's 2004 paper is highly relevant ('Border correlation of binary words') but full text was inaccessible; any embedded three-marker specialization is a genuine priority risk, not presumed absent.

## value

PASS

Unbordered rotations are a standard border-correlation invariant. The special natural sparse fixed-content family has a complete local classification, a sharp bounded spectrum despite arbitrarily long words, exact necklace generating function and probability law. This is a motivated exact classification rather than an arbitrary list of a few lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
