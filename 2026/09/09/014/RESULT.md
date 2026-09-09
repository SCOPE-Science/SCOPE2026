# Exact qubit-projective I3322 threshold for Werner states: v* = 4/5

## Context

The Collins-Gisin I3322 inequality is the unique relevant facet beyond CHSH for
three two-outcome settings per party. Collins-Gisin showed isolated mixed
two-qubit states violating I3322 but not CHSH, leaving the recognized question
whether this relevance extends to the canonical Werner family. Unlike CHSH
(Horodecki criterion), no closed-form criterion exists for 3-setting facets,
so the Werner-I3322 threshold must be optimized, not read off a formula.
Pal-Vertesi showed the unconstrained I3322 maximum needs infinite dimension;
that is a different slice from the Werner visibility curve studied here.

## Definitions

- Werner family: W(v) = v|psi^-><psi^-| + (1-v)I/4, v in [0,1],
  |psi^-> = (|01>-|10>)/sqrt(2).
- I3322 (Collins-Gisin CH form, local <= 0), with singles P(Ai), P(Bj) and
  coincidences P(AiBj):
  I = -P(A1) - 2P(B1) - P(B2) + sum_{i,j=1..3} c_{ij} P(AiBj),
  c = [[1,1,1],[1,1,-1],[1,-1,0]].
- Qubit projective measurements: Ai = (I + ai.sig)/2, Bj = (I + bj.sig)/2,
  unit Bloch vectors ai, bj in S^2.
- Werner marginals are maximally mixed (all singles = 1/2) and
  P(AiBj) = (1 - v ai.Bj)/4.
  Since sum_{ij} c_{ij} = 4:
  I(v) = -1 + (v/4) S, S := sum_{ij} d_{ij} (ai.Bj), d := -c.
- Q := max over Bloch vectors of S; then I_max(v) = -1 + vQ/4, v* = 4/Q.

## Result

Q = 5, I_max(v) = -1 + 5v/4, and the critical visibility is exactly
v* = 4/5 = 0.8.

Since (4/5)^2 = 16/25 = 0.64 > 1/2, v* = 0.8 > 1/sqrt(2) ~= 0.7071 with gap
4/5 - 1/sqrt(2) in (0.092, 0.094). Hence no Werner state with v < 0.8 --
in particular none below the CHSH threshold 1/sqrt(2) -- violates I3322 with
qubit projective measurements: I3322 is strictly weaker than CHSH on Werner
states (exact no-separation theorem, bracket width 0).

Achieving settings (planar, z = 0): A angles (0, pi/3, 2pi/3),
B angles (4pi/3, pi, 2pi/3); i.e.
A1 = (1,0,0), A2 = (1/2,sqrt(3)/2,0), A3 = (-1/2,sqrt(3)/2,0);
B1 = (-1/2,-sqrt(3)/2,0), B2 = (-1,0,0), B3 = (-1/2,sqrt(3)/2,0).
The d-weighted cosines sum to S = 2+2+1 = 5; singlet value I = -1+5/4 = 1/4,
matching Collins-Gisin.

## Proof / evidence

Local bound: deterministic maximum over a_i,b_j in {0,1} is 0 (exact check of
all 64 assignments; 20 saturate, e.g. all-1s gives -1-2-1+4 = 0).

Achievability (Q >= 5): the settings above give difference-cosines in
{0,+-1/2,+-1} and exactly S = 2+2+1 = 5 (term-by-term table in DRAFT; exact
Fraction replay in verifier).

Upper bound (Q <= 5): fix a1,a2,a3; each bj enters only via gj.Bj with
gj := sum_i d_{ij} ai, so optimal unit bj = gj/|gj| and the B-side maximum
is sum_j |gj|. With d = -c:
g1 = -(a1+a2+a3), g2 = -(a1+a2-a3), g3 = -(a1-a2).
Hence Q = max_{|ai|=1} |u+a3| + |u-a3| + |w| with u := a1+a2, w := a1-a2
(note u.w = |a1|^2-|a2|^2 = 0).
For fixed u and unit a3: |u+a3|^2+|u-a3|^2 = 2|u|^2+2 and
|u+a3|^2|u-a3|^2 = (|u|^2+1)^2 - 4(u.a3)^2 <= (|u|^2+1)^2, so
(|u+a3|+|u-a3|)^2 <= 4(|u|^2+1), attainable by a3 perp u.
Thus the a3-maximum is 2*sqrt(|u|^2+1).
Put t := |u| = |a1+a2| in [0,2]; then |w| = sqrt(4-t^2) (since
|u|^2+|w|^2 = 4) and Q = max_{0<=t<=2} g(t),
g(t) := 2*sqrt(t^2+1) + sqrt(4-t^2).
Lemma g(t) <= 5: equivalently 2*sqrt(t^2+1) <= 5 - sqrt(4-t^2); RHS >= 3 > 0,
so squaring is faithful and the claim becomes 2*sqrt(4-t^2) <= 5-t^2; here
5-t^2 >= 1 > 0, so squaring again is faithful, yielding
4(4-t^2) <= (5-t^2)^2 iff 0 <= (t^2-3)^2. Equality at t = sqrt(3)
(attained: a1,a2 at 60 degrees, a3 perp u).

Corroboration (not the proof): multi-start Bloch-vector seesaw converges to
5.000000000000001.

## Limitations

- Proven for two-qubit Werner states with projective (rank-1 Bloch-sphere)
  measurements only -- the standard reading of the Collins-Gisin Werner
  question.
- Not claimed: general POVMs, higher-dimensional or commuting-operator
  settings (Pal-Vertesi show the unconstrained I3322 maximum needs infinite
  dimension -- a different slice; whether the Werner threshold could drop
  under higher-dimensional settings is left open).
- No SDP solver was needed; the proof is exact hand-checkable algebra.

## Reproducibility

Stdlib-only verifier `output/artifacts/verify.py` replays every exact step
(local bound enumeration, S = 5, polynomial identity, g(t) dense-grid sanity,
threshold comparison) and prints VERIFY_OK in seconds:
`python3 output/artifacts/verify.py`.

## References

- D. Collins, N. Gisin, "A Relevant Two Qubit Bell Inequality Inequivalent to
  the CHSH Inequality," quant-ph/0306129.
- K. F. Pal, T. Vertesi, "Maximal violation of the I3322 inequality using
  infinite dimensional quantum systems," arXiv:1006.3032.
- R. Augusiak et al., "Local hidden-variable models for entangled quantum
  states," arXiv:1405.7321.
- M. Navascues, S. Pironio, A. Acin, "A convergent hierarchy of semidefinite
  programs characterizing the set of quantum correlations,"
  arXiv:0803.4290.
