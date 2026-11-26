# Independent mathematical audit

## correctness

PASS

Reconstructed the affine returns in temporal order over Q(t): see /workspace/tent_symbolic_replay.py (run with python -B; SymPy). It reproduced all six nonzero determinants, the closed-triangle margins and the four branch signs for each primitive word. Each product of n branches is (√2 t)^n times an orthogonal matrix, so no formal return matrix has eigenvalue 1 in this interval. The necklaces 0000, 0101, 1111 yield precisely the two fixed points and one 2-cycle from words 0, 1, 01; the latter has seed (2t/(2t²+1),2t/(2t²+1)) strictly left and its image strictly right. The 0001 word always passes, and 0011 and 0111 pass iff P=4t⁴−2t−1≥0: their time-one x−1 has, respectively, sign −P and +P, with all other signs strict. The seed lies in the triangle and then forward invariance applies to the admissible orbit, not to a wrong-branch formal iterate. The positive factors can be checked already for t>1/√2: 4t⁴−4t³+1≥37/64, 4t⁴−2t+1>0 by monotonicity from 1/√2, 4t⁴+4t³−1>0, and the nontrivial triangle margin has the strictly positive sum of squares (2t²−t)²+(t−1)². P increases strictly with P(τ)=√2−2τ<0 and P(1)=1. The stated rational bracket has opposite signs. Modulo P the two new seeds agree exactly, and their time-one point is on the fold; the two descriptions represent one orbit, which has x₀<1<x₂ and thus period four. Away from the root, strict labels distinguish the primitive necklaces and exclude periods one and two. This gives the 1/2/3 trichotomy and 8/12/16 fixed-iterate counts including endpoints. Off-fold four-step expansion is 4t⁴>1. The supplied rational checker was inspected, not run, and cannot by finite sampling establish the equality case.

## originality

PASS

The established family, its eventual attractor and endpoint symbolic dynamics are not contributions here. The supported distinct result is the complete low-period census over the closed parameter interval, particularly the exact interior transition and geometric identification of the two words at equality. The closest same-family primary preprint was available; the final journal version remains an access risk, not affirmative contrary evidence.

## value

PASS

The interval is the natural expanding-chaotic regime studied for a standard planar tent family, not an arbitrary numerical slice. The exact primitive count and polynomial threshold distinguish the actual periodic geometry from a count of admissible words: two new word types first give just one geometric orbit. This is a usable short-period benchmark and fold-boundary example, not a recensus of the already understood full-shift endpoint alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
