# No sign-canceling F2 floor shape exists: universal nonnegativity of r-real multiplicities

## Context

Floor diagrams (Brugallé–Mikhalkin) encode tropical curve counts on
h-transverse toric surfaces. On the Hirzebruch surface F2, a recognized
program asks where real (Welschinger-signed) floor recursion stalls.
The admitted target conjectured a sharp obstruction: an explicit minimal
admissible F2 floor shape whose total Welschinger-signed contribution over
all markings equals zero by exact pairwise cancellation of nonzero
opposite-sign terms, with every strictly smaller shape contributing nonzero.
Admission's preflight assumed such opposite-sign samples exist
(multiple nonzero markings of opposite signs) and that no lookup decides the sum.

## Definitions

We use the standard Brugallé–Mikhalkin conventions fixed by the target
([BM08], planar case, Defs 3.1/3.5/3.8). A genus-0 floor diagram D on an
h-transverse polygon Δ has floors v with θ(v) ∈ dl(Δ) and
θ(v)+div(v) ∈ dr(Δ), where div(v) = incoming − outgoing weights.
For the Hirzebruch class aB+bF on Fn the polygon has dl = {0^a} and
dr = {n^a}. A marking m: {1,…,s} → D assigns one index to each vertex
and edge; two marked diagrams are equivalent if they agree on vertex/edge
occupancy modulo leaf symmetry. For admissible r with s−2r ≥ 0, let
Im(m,r) be the union of r-pairs {s−2k+1,s−2k+2} whose images are
non-adjacent, and let or be half the number of vertices in m(Im(m,r))
with odd divergence. Let A = Edge(D) ∖ m({1,…,s−2r}). Then

  μ^R_r(D,m) = (−1)^{or} ∏_{e ∈ A} w(e)

if (D,m) is r-real and every even-weight edge contains a point of
m(Im(m,r)), and 0 otherwise.

## Result

**Theorem (TARGET negative resolution).** Under the standard
Brugallé–Mikhalkin r-real multiplicity, no admissible F2 floor shape at
any degree or cleft type admits exact pairwise Welschinger sign
cancellation. Every floor of every F2 diagram has divergence 2 (even),
so or = 0 identically, (−1)^{or} = +1, and every marking multiplicity
lies in {0} ∪ Z_{>0}. Opposite-sign nonzero markings do not exist; the
only shape-level zeros are vacuous sums of zeros, which fail the
target's cancellation mechanism and nonvacuity requirement.

## Proof / evidence

**Lemma 1 (F2 divergence parity).** For Fn, θ(v)+div(v) ∈ dr = {n^a}
with θ(v) = 0 forces div(v) = n per floor. For F2 (n = 2), div(v) = 2
for every floor of every admissible diagram, at any (a,b).

**Lemma 2 (trivial sign).** or counts odd-divergence vertices in
m(Im(m,r)). By Lemma 1 there are none, so or = 0 and (−1)^{or} = +1
for every (D,m,r).

**Proposition.** If μ^R_r(D,m) = 0 there is nothing to show; otherwise
μ^R_r = +∏_{e ∈ A} w(e) ≥ 1. Hence no negative term occurs on F2.

**Corollary.** Pairwise cancellation of nonzero terms needs a positive
and a negative nonzero term on the same shape; the negative term never
occurs. Any Σ_m μ^R_r = 0 is a sum of zeros (vacuous), not a
cancellation, and the target's existential conjunction (cancellation
plus nonvacuity plus minimality) is false.

The mechanism is F2-specific: on F1 (n = 1) divergences are odd, or can
be nonzero, and μ^R_r genuinely takes both signs (cf. [BM08] Table 1,
μ^R_2 = −1 entries for plane cubics). The (−2)-twist is what kills the sign.

**Computed certificate (corroboration only).** The stdlib-only script
`output/artifacts/verify.py` implements Def 3.8 in full (r-reality
equivalence, even-edge rule, or count — not an assumed nonnegativity)
and enumerates all genus-0 diagrams, markings up to equivalence, and all
admissible r for F2 classes (a,b) ∈ {(1,0),(1,1),(2,0),(2,1)}: 9
diagrams total, zero negative values (VERIFY_OK). Per-marking ledgers in
`output/artifacts/ledger.json` include a vacuous-zero witness
((a,b) = (2,0) weight-2 elevator shape, all-zero ledger) and positive
witnesses (weight-1 shape r-sums 6,6,4,2 over 6 markings; (1,0) sums 1;
(2,1) weight-3 values 3,3,1,1,1). The universal quantifier rests on the
parity proof, not the window.

## Limitations

(i) Convention-relative: standard Brugallé–Mikhalkin real multiplicity
only; nonstandard sign rules are outside the claim. (ii) Genus-0
floor-diagram setting of the target. (iii) Real floor recursion on F2
cannot stall via the conjectured pairwise-cancellation mechanism; stalls
via vacuous vanishing, absent markings, or correspondence failure are
not excluded — a concrete redirection for mapping real-vs-complex
divergence on rational surfaces.

## Reproducibility

Run `python3 output/artifacts/verify.py` (stdlib only) to replay the
window census and regenerate `output/artifacts/ledger.json`; expect
VERIFY_OK and WITNESS_OK.

## References

[BM07] E. Brugallé, G. Mikhalkin, Enumeration of curves via floor
diagrams, arXiv:0706.0083. [BM08] E. Brugallé, G. Mikhalkin, Floor
decompositions of tropical curves: the planar case, Gökova Proc. 15
(2008), 64–90 (arXiv:0812.3354). [GMS13] A. Gathmann, H. Markwig,
F. Schroeter, Broccoli curves and the tropical invariance of
Welschinger numbers, Adv. Math. 240 (2013) (arXiv:1104.3118). [Bru20]
E. Brugallé, On the invariance of Welschinger invariants,
arXiv:1811.06891.
