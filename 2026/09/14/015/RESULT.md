# Irreducibility, atoroidality, index and ideal Whitehead graph of a -> bc, b -> c, c -> d, d -> a in Out(F4)

## Context

Let F4 = F(a,b,c,d) and let Phi1 be the endomorphism a |-> bc, b |-> c, c |-> d, d |-> a.
This is the composition of the transvection a |-> ab with the cyclic permutation
a -> b -> c -> d -> a. The admitted target asks for a relative train-track
determination of whether the induced class phi1 in Out(F4) is fully irreducible
(no positive power preserves a proper free-factor conjugacy class), atoroidal
(no positive power fixes a nontrivial conjugacy class), and ageometric
(no periodic Nielsen path on an expanding irreducible train-track representative),
together with the exact Handel-Mosher rotationless index and the isomorphism type
of the ideal Whitehead graph IW(phi1). Either all three properties plus exact
index and graph type are proved, or the failing property is witnessed explicitly.

## Definitions

Write A = a^{-1}, B = b^{-1}, C = c^{-1}, D = d^{-1} and let f be the rose map
induced by Phi1. Df denotes the direction map. A turn is an unordered pair of
directions. A turn is illegal if some Df-power identifies its two directions.
LW(f) is the local Whitehead graph (vertices: 8 directions; edges: turns taken by
some iterate of an edge). SW(f) is the stable subgraph on periodic directions.
IW(phi1) is the ideal Whitehead graph, which for a periodic-Nielsen-path-free
rose representative equals SW(f). The transition matrix M counts unsigned
occurrences of each generator in each edge image. The Handel-Mosher index of a
component with k vertices is 1 - k/2.

## Result

Phi1 is an automorphism; denote its class by phi1 in Out(F4). Then:

1. phi1 is fully irreducible.
2. phi1 is ageometric: the expanding irreducible train-track representative f
   below has no periodic Nielsen path (no indivisible Nielsen path for any
   positive power).
3. phi1 is atoroidal, hence hyperbolic: no positive power fixes a nontrivial
   conjugacy class.
4. phi1 is rotationless after power 12. The Handel-Mosher index sum is
   i(phi1) = 1 - 7/2 = -5/2 with index list [-5/2] (one singularity), and
   IW(phi1) is the connected complete bipartite graph K_{3,4}: 7 vertices on the
   periodic directions {a,b,c,d,A,C,D}, 12 edges (every positive-negative pair),
   diameter 2, girth 4.

The alternative branch (non-invertibility, reduction, periodic-class witness, or
Nielsen-path witness) does not occur.

## Proof / evidence

Automorphism: Psi: a |-> d, b |-> aB, c |-> b, d |-> c satisfies
Psi(Phi1(x)) = x for every generator under free reduction, so Psi = Phi1^{-1}
and f is a homotopy equivalence.

Transition matrix in order (a,b,c,d):

    M = [[0,1,1,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]],

det M = -1, char(M) = x^4 - x - 1. The polynomial p(x) = x^4 - x - 1 has a unique
positive root; p(1.22) < 0 < p(1.221), so the Perron-Frobenius eigenvalue
lambda satisfies 1.22 < lambda < 1.221 (approximately 1.2207). Moreover

    M^10 = [[3,1,2,3],[2,1,1,1],[1,2,3,1],[1,1,3,3]]

is strictly positive, so M is primitive (hence irreducible and aperiodic) with
spectral radius at least 5^{1/10} > 1. Thus f is an expanding irreducible
train-track candidate.

Direction map: Df: a|->b, b|->c, c|->d, d|->a, A|->C, B|->C, C|->D, D|->A.
Gate equivalence gives 7 gates: {a},{b},{c},{d},{A,B},{C},{D}; the unique
illegal turn is {A,B}. The only turn inside any edge image is {B,c} from
f(a) = bc, which is legal. B is absent from Im(Df), so the Df-image of any
legal turn can never be {A,B}: f maps legal turns to legal turns and tight
paths to tight paths. Hence f is a train-track map. Positives cycle with period
4 and A -> C -> D -> A has period 3 with B -> C, so every power f^k has the same
unique illegal turn {A,B}.

Taken turns: let S_k be turns in f^k(e) over edges e and O the Df-orbit of the
seed {B,c}, which has exactly 13 elements:

    {c,B},{d,C},{a,D},{b,A},{c,C},{d,D},{a,A},{b,C},{c,D},{d,A},{a,C},{b,D},{c,A},

Df-closed, all mixed-sign, with {A,B} not in O. Induction on concatenation of
blocks shows S_k subset of O for all k; computation to k = 24 realizes every
element of O (each Df^k(seed) occurs as the middle turn of f^{k+1}(a)), so the
taken set is exactly O. The same induction for (f^k)^m = f^{km} shows taken
turns of every power lie in O, never {A,B}.

Whitehead graphs: LW has 8 directions and 13 edges (O), connected. SW deletes
the nonperiodic direction B, leaving vertices {a,b,c,d,A,C,D} and the 12 turns
of O avoiding B, i.e. every positive-negative pair: SW is K_{3,4}, connected.
By the Bestvina-Handel criterion (irreducible train-track map with connected
local Whitehead graphs), phi1 is fully irreducible.

No Nielsen paths: by the Bestvina-Handel indivisible-Nielsen-path lemma, the
illegal turn of such a path is a taken turn. Since {A,B} is the unique illegal
turn of every f^k and is never taken by any power, no f^k has an indivisible
Nielsen path, hence f has no periodic Nielsen path: phi1 is ageometric. The
index -5/2 > 1 - 4 independently confirms ageometricity via the
Gaboriau-Jaeger-Levitt-Lustig equality case.

Atoroidality: a fully irreducible automorphism is either atoroidal or geometric
(induced by a pseudo-Anosov on a surface with boundary, whose boundary class is
periodic and appears as a periodic Nielsen path on every train-track
representative). Ageometricity excludes the geometric case, so phi1 is
atoroidal; with full irreducibility, Brinkmann's theorem gives a hyperbolic
mapping torus.

Index and IW: Df-periods are 4 on positives and 3 on {A,C,D}, so Df^12 fixes
all 7 periodic directions and f^12 is rotationless. With no periodic Nielsen
paths, IW(phi1) = SW(f) = K_{3,4} (7 vertices, 12 edges, connected, diameter 2,
girth 4; bipartition {a,b,c,d} vs {A,C,D}). One component with 7 vertices gives
index sum 1 - 7/2 = -5/2 and list [-5/2].

## Limitations

Finite certificate steps use exact integer arithmetic reproduced by
output/artifacts/certify.py. Deductions to full irreducibility, the
indivisible-Nielsen-path obstruction, ageometric-implies-nongeometric
atoroidality, and the rotationless index formula rely on the standard
Bestvina-Handel, Brinkmann, and Handel-Mosher theorems cited above, whose
proofs are not re-derived here.

## Reproducibility

Run `python3 output/artifacts/certify.py` (requires numpy). It checks: (1) the
explicit inverse, (2) det/char-poly/Perron interval/M^10 positivity, (3) gates
and the unique illegal turn, (4) exact 13-turn closure with {A,B} never taken,
(5) LW connected and SW = K_{3,4}, (6) persistence of the illegal turn for
powers 1..12. All checks print OK.

## References

- Bestvina-Handel, Train tracks and automorphisms of free groups.
- Bestvina-Feighn-Handel, laminations and Nielsen-path structure.
- Gaboriau-Jaeger-Levitt-Lustig, index theory and ageometric case.
- Handel-Mosher, rotationless index and ideal Whitehead graphs; axis bundles.
- Brinkmann, hyperbolic mapping tori of atoroidal fully irreducibles.
- Pfaff, Ideal Whitehead Graphs in Out(F_r) II-IV (complete graphs, rank-3
  census, cut-vertex constructions): nearest prior scope, disjoint from K_{3,4}.
