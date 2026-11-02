---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Any tree has precisely one size-b-part spoke with two edges (otherwise disconnected if none, four-cycle if at least two); the remaining b-1 spokes choose one of two attachments independently. This is a bijection giving b2^(b-1) trees. For independent trees equal bridge spokes have probability 1/b, with intersection 2+Bin(b-1,1/2); unequal bridges yield 2+Bin(b-2,1/2). Thus X=law 2+Bin(b-2,1/2)+Bern(1/(2b)) independently, support [2,b+1], mean (b+1)²/(2b), variance (b-1)(b²-b+1)/(4b²). Binomial unimodality and the convolution difference give exact total variation p*binom(b-2,floor((b-2)/2))/2^(b-2) with p=1/(2b). Fresh all-pairs exact rational enumeration b=2..6 agreed. The bridge-spoke bijection proves arbitrary b.

## originality

PASS

Qualified PASS: Read current 17-page Sept 2026 Bóna–Burghart–Wagner revision in full; §4 balanced-multipartite asymptotic Poisson and §5 fixed-k bipartite approximate binomial do not imply the precise finite all-b correction. General fixed-forest containment formulas of Li–Chen–Yan may yield a route to derive it, but the exact independent factorization and finite TV were not located. A historical K2,b specialized overlap formula remains possible.

## value

PASS

PASS: A natural known random-spanning-tree intersection problem has a particularly meaningful exactly solvable smallest fixed-side boundary. The Bernoulli bridge-collision term and sharp finite total-variation discrepancy refine existing approximate fixed-k binomial results, independently valuable without a general k extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
