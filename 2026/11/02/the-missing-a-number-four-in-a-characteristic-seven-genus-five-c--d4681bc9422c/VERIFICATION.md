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

The connected tame degree-four Kummer cover has two inertia-two and four inertia-four branch points and none at infinity, yielding genus five. The claimed five forms are regular by the local orders at these places and independent by characters and numerator degrees. Cartier picks powers 7r+6; its character blocks are 1→3, 3→1 and 2→2. For the 1→3 block the image numerator is even of degree at most four and vanishes at w=±1 by regularity, so the coefficients of w² and w⁴ determine it. Directly extracting [X^10] and [X^17] of G(X)^5 over F_7[s,v] reproduced the two beta polynomials; the other off-diagonal block gives the stated two independent affine-linear alpha forms. There is a second exact certificate independent of the uploaded Gröbner-basis result: put D=3s²+5s+6. Then beta_1=(s−1)(v−D), beta_0(1,v)=v²(v−2)²(v−1), Delta(1,v)=3v²(v−2), and beta_0(s,D)=−2 Delta(s,D)^2. Thus on Delta≠0 the only beta zero is (1,1), where v−D is a unit and the surviving factor v−1 is simple. The alpha ideal is also (s−1,v−1). The central block is [X³](X²−sX+v)^3=−t³ H_7(u/t), whose three simple roots are 2,4,6; it vanishes at both points above (1,1). The ordered-parameter map is étale there, so the full Cartier zero locus is reduced. The ranks are therefore 3,2,0; each of the three distinct ratio lines has four valid F_7 pairs, and subtracting the two rank-zero pairs gives the claimed frequencies.

## originality

PASS

The family and the Legendre factor in the central block are known, as is existence of genus-five superspecial curves in characteristic seven. The distinct supported claim is the full one-step Cartier classification for this exact two-parameter family, including synchronized failure of both other blocks at just the reduced two-point locus, with no a=4. Compared actual same-family results give supersingularity from a stable criterion rather than these block ranks; the other catalogued classifications examined are not this one.

## value

PASS

This is a complete geometric stratification of a natural previously studied family where the stable invariant does not answer the finer Cartier question. The synchronization of two distinct blocks and reduced rank-zero locus explains the missing a=4 and gives a usable marked locus without testing parameters individually. The small F_7 frequency table is ancillary, not the basis for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
