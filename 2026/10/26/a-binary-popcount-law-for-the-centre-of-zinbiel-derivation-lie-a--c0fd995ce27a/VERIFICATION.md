---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For the stated integral multiplication and n>=2, e_1 generates the algebra, so a derivation is determined by its value on e_1. In the derivation identity, after factoring out (a+b+h-2)!/((a-1)! b! h!), the left side has factor a+b+h-1 and the two right sides have factors a+h-1 and b. This verifies the identity over the integers and hence over any field; truncation preserves it by degree. The indicated maps extend the arbitrary generator images, and their brackets follow by evaluating on e_1. Fixing a partner, distinct basis terms have distinct output degrees, so no mixed central term can survive by cancellation. The partner 1 forces i=1 in characteristic 0 or i=1 modulo p in characteristic p. Partner 2 rules out i=1 in characteristic 0 and all such i<n for odd p; the top degree is then central exactly as stated. In characteristic 2, for odd i with s trailing ones, Lucas carry tests give both binomial coefficients even for 2<=j<2^s, both odd at j=1, and exactly one odd at j=2^s. Thus centrality means the first nonzero partner is beyond the cutoff. With N=n+1 the inequalities for i=2^s(2u+1)-1 say that digit s of N must be one and its remainder modulo 2^s at most 2^s-2. These are exactly one-bits above the trailing run, of length nu_2(n+2), including the no-admissible-bits case. At n=2^r-3 this gives r-1. The 360 finite cases reported in the inspected checker and verification notes are corroboration; the uploaded script was not executed.

## originality

PASS

The contribution is the Lie centre for every truncation, in particular the characteristic-two homogeneous basis and exact dimension law. The Zinbiel multiplication and the divided-power Witt presentation are established background. The closest indexed results address different invariants or different Lie brackets; no covering arbitrary-truncation theorem was found in the checked sources.

## value

PASS

The Lie centre is a natural invariant of the derivation algebra. The result classifies the actual central degrees and their dimension for every truncation, revealing unbounded growth governed by binary carries in characteristic two versus dimension at most one in odd characteristic. This is not just a re-expression of the known multiplication or a finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
