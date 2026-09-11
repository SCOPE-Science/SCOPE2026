# A sporadic non-Redei minimal blocking set of size 24 in PG(2,13)

## Context and motivation

In the Desarguesian projective plane PG(2,q), a blocking set is a set of
points meeting every line; it is nontrivial if it contains no full line and
minimal if no proper subset still blocks all lines. A Redei-type blocking set
is one for which some line meets the set in |B|-q points (a Redei line); a set
with no such line is non-Redei (sporadic). The structural question of where
linear-origin Redei examples stop and sporadic non-Redei geometry begins is a
recognized frontier: besides the sporadic non-Redei minimum example in PG(2,7),
prime planes lack documented early sporadic blockers, and PG(2,13) is the
natural laboratory. Size 24 sits just above the triangle in the small-blocker
regime; at |B|=24 and q=13 a Redei line carries exactly 24-13=11 points, so the
no-11-secant condition is precisely the intrinsic non-Redei definition, not an
ad hoc bound. The admitted target asked for exactly this decision.

## Definitions

Work in PG(2,13): 183 points and 183 lines, each line carrying 14 points.
Points and lines are represented by normalized homogeneous triples over F_13
(first nonzero coordinate equal to 1); a point (x,y,z) lies on line [A,B,C] iff
Ax+By+Cz=0 mod 13. A set B of 24 points is a minimal nontrivial blocking set
iff (i) every line contains at least one point of B, (ii) no line is contained
in B, and (iii) each point of B is essential (admits a tangent line meeting B
in exactly that point, equivalently B minus any point misses some line). It is
non-Redei iff no line meets B in exactly |B|-q = 11 points.

## Result (headline claim)

PG(2,13) contains a minimal non-Redei blocking set of size 24. Explicitly, the
24 normalized homogeneous points

B = {(0,1,8),(0,1,11),(1,0,0),(1,1,1),(1,1,2),(1,1,7),(1,2,2),(1,3,3),
     (1,3,5),(1,4,2),(1,4,4),(1,4,8),(1,5,9),(1,6,1),(1,7,3),(1,8,7),
     (1,8,8),(1,9,12),(1,10,10),(1,11,8),(1,11,11),(1,12,4),(1,12,6),(1,12,12)}

meet every one of the 183 lines, contain no full line, are minimal by inclusion
with a tangent line at each point, and no line meets B in exactly 11 points
(hence B is non-Redei).

## Proof / evidence (machine certificate, independently re-verified)

The claim is an existence witness certified by finite incidence checks over all
183 lines, re-verified from scratch by the auditor with an independent
stdlib-only script (output/artifacts/verify.py) that rebuilds the normalized
183-point/183-line model and recomputes every incidence by direct dot products:

- Blocking: 0 uncovered lines (every line meets B).
- Nontrivial: 0 lines with 14 points of B.
- Minimality: 24/24 points essential; one tangent line per point, e.g.
  (0,1,8)->[1,2,3], (0,1,11)->[1,3,8], (1,0,0)->[0,0,1], (1,1,1)->[1,1,11],
  (1,1,2)->[1,1,12], (1,1,7)->[1,1,9], (1,2,2)->[1,2,4], (1,3,3)->[1,1,3],
  (1,3,5)->[1,0,5], (1,4,2)->[1,1,4], (1,4,4)->[1,1,2], (1,4,8)->[1,1,1],
  (1,5,9)->[1,0,10], (1,6,1)->[1,2,0], (1,7,3)->[1,2,8], (1,8,7)->[1,7,3],
  (1,8,8)->[1,5,3], (1,9,12)->[1,1,10], (1,10,10)->[1,0,9], (1,11,8)->[1,3,12],
  (1,11,11)->[1,0,7], (1,12,4)->[1,7,8], (1,12,6)->[1,0,2],
  (1,12,12)->[1,2,12]; a deletion test further confirms removing any single
  point leaves some line uncovered. Note: two tangent labels printed in the
  draft, (1,1,1)->[1,1,1] and (1,1,2)->[1,1,2], are not valid tangents (each
  fails the incidence equation); the corrected tangents above are verified, so
  the conclusion is unaffected.
- Non-Redei: the secant-length distribution over the 183 lines is
  {1:99, 2:43, 3:25, 4:11, 5:2, 6:1, 7:1, 9:1} (sums to 183), maximum 9, with
  zero lines meeting B in exactly 11 points.

The script prints VERIFY_OK. The discovery route (simulated annealing) is
immaterial; the certificate stands on its own.

## Limitations

Existence witness only: nothing is claimed about uniqueness, the full size-24
spectrum or classification, Redei rigidity at other sizes, or other orders. No
general theorem beyond this exact invariant is asserted.

## Reproducibility

Run `python3 output/artifacts/verify.py` (stdlib only, seconds). It rebuilds
the normalized PG(2,13) model, checks all 183 lines for cover, nontriviality,
per-point tangents plus the deletion test, and the secant histogram with the
11-secant count.

## References

- L. Redei / Ball-Blokhuis direction theory and lacunary-polynomial machinery
  (general method background; proves no size-24 verdict).
- Gacs-Sziklai-Szonyi nuclei remarks; sporadic non-Redei minimum example in
  PG(2,7) (precedent at a different order).
- Ball-Blokhuis-Brouwer / Blokhuis et al., "Blocking sets in PG(2,p) for small
  p, and partial spreads in PG(3,7)" (classifies size 21 for p<41; leaves
  size 24 open).
- Botteldoorn-Coolsaet-Fack, "Classification of minimal blocking sets in
  PG(2,9)" (full census at a different order).
- Szonyi-Gacs-Weiner, "On the spectrum of minimal blocking sets in PG(2,q)"
  (spectrum survey; no size-24 PG(2,13) non-Redei witness).
- Kadoo, "The minimal blocking set of size 22 in PG(2,13)" (adjacent size only).
- Internal prior SCOPE040: minimal Redei-type blocking sets in PG(2,13) at
  sizes 21, 23, 24 (different stratum; its size-24 witness is Redei-type with
  11 directions, sharing neither the object nor the no-11-secant property).
