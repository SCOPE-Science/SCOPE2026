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

The probability-measure addition theorem gives E_l E_l*=(2l+1)L_l. Independent exact arithmetic on the stated directions over Q(sqrt(5)) returned ranks (1,3,5,7,9,11,10,15,14,15,15,15,15,15,14,15) through degree 15; the row sums at 8 and 14 are exactly zero, so rank 14 identifies the full obstruction. The independently reconstructed determinants modulo 1009 for degrees 16–215 are all nonzero and agree with the 200 frozen residues; sqrt(5) maps to 244, and all coordinate and recurrence denominators are units there. The infinite range is not extrapolated. Direct dot products give two orthogonal competitors in each row and maximum off-diagonal absolute inner product (1+sqrt(5))/4. The Bernstein bound's angular factor is 1 at zero and strictly below 4/3 at every other competitor, since 1-t^2 >= (5-sqrt(5))/8 > (3/4)^4. Thus the absolute off-diagonal sum is less than 18 sqrt(2/[pi(l+1/2)]), which is below one from degree 216 using pi>3. Strict diagonal dominance proves invertibility there. The Moore–Penrose formula is E_l* (E_l E_l*)^+ y, lying perpendicular to the evaluation kernel, and its squared norm is y* (E_l E_l*)^+ y. The degree-14 defect makes the permanent cutoff sharp.

## originality

PASS

The bounded search identified a later catalogue record repeating full-rank support on the exact same orbit, a close earlier result on ten different axes, and primary work on the harmonic mean of six different axes. The later record is evidence of material overlap, not evidence that the exact result predates the frozen record. The supported distinct claim is the complete fifteen-line exact-degree profile and image statements, not the addition theorem, pseudoinverse principle, or eventual invertibility of a fixed separated node set by itself.

## value

PASS

This is an exact classification for the canonical noncrystallographic H3 orbit and a concrete invariant needed to determine which exact harmonic degrees can interpolate arbitrary data. It resolves the genuine rank reversals at degrees 8 and 14, gives the obstruction there, and sharpens a general large-degree existence argument to the precise cutoff 15. The geometry and low-degree table are not arbitrary parameters chosen after computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
