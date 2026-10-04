# Sharp quadratic type growth of Simon's generic chord quotient

## Finding

Let \(U\) be the Fraïssé limit of finite separation relations equipped with an equivalence relation \(F\) whose classes have size \(2\), and let \(M=U/F\). This is the \(n=2\) member of the circular finite-cover family described by Simon in Section 6.7. Write \(f_M(m)\) for the maximal number of complete 1-types over an \(m\)-element parameter set, in Simon's notation.

Then
\[
\boxed{f_M(0)=1,\qquad f_M(1)=3,\qquad f_M(2)=9,\qquad f_M(m)=2m(m+1)\ (m\ge3).}
\]
Thus this canonical primitive rank-1 NIP example has exact quadratic type growth with leading coefficient \(2\).

Equivalently, over an \(m\)-element parameter set there are \(m\) algebraic equality types, while the largest possible number of nonalgebraic 1-types is
\[
2,\ 7,\ \binom{2m+1}{2}\quad\text{for }m=1,\ m=2,\ m\ge3,
\]
respectively.

## Chord-diagram interpretation

A finite parameter set in \(M\) lifts to finitely many 2-element \(F\)-classes on a circle with its orientation forgotten by the separation relation. In other words, it is a finite **labeled chord diagram**. A new nonalgebraic point of \(M\) is obtained by adding one further chord.

If the base has \(m\) chords, its \(2m\) endpoints cut the circle into \(2m\) complementary arcs. The two endpoints of a new chord may lie in two distinct arcs or in the same arc. Hence before quotienting by symmetries there are
\[
\binom{2m}{2}+2m=\binom{2m+1}{2}
\]
possible one-chord extensions. This is the same elementary insertion count used in the standard growth process for chord diagrams.

Because the base parameters are fixed pointwise, two placements define the same 1-type exactly when they are related by a dihedral symmetry of the finite endpoint circle that preserves every labeled base chord setwise. Thus the nonalgebraic types over a base diagram are the orbits of its pointwise dihedral stabilizer on unordered pairs of complementary arcs, with repetition allowed.

## Proof of the maximum

The preceding description immediately gives
\[
f_M(m)\le m+\binom{2m+1}{2}.
\]
For every \(m\ge3\), take the labeled chord diagram whose cyclic endpoint word is
\[
1,1,2,2,\ldots,m,m.
\]
Its pointwise stabilizer in the dihedral group of the \(2m\)-gon is trivial. A nonzero rotation moves chord 1 to a different labeled chord (or destroys its adjacent pair), while a reflection preserving every adjacent labeled pair would force the same reflection axis to bisect every pair; that can happen only for \(m\le2\). Hence all \(\binom{2m+1}{2}\) placements remain distinct over this parameter set, and
\[
f_M(m)=m+\binom{2m+1}{2}=2m(m+1)\qquad(m\ge3).
\]

For \(m=1\), a second chord either crosses the named chord or does not, giving two nonalgebraic types, plus the equality type: \(f_M(1)=3\).

For \(m=2\), there are only the crossing and noncrossing labeled two-chord bases up to separation isomorphism. The best base is the noncrossing one. Its pointwise dihedral stabilizer is a reflection of order two; on the ten unordered pairs-with-repetition of the four complementary arcs it has seven orbits. Hence there are seven nonalgebraic types and two equality types, so \(f_M(2)=9\). The bundled verifier checks this exhaustively rather than relying on a picture.

## Why the model-theoretic orbit statement holds

Simon describes this family through an interpretable finite circular cover: in the relevant case the skeletal cover consists of two circular orders in order-reversing bijection, and the quotient is obtained from a Fraïssé limit of separation relations with finite equivalence classes. The separation relation remembers the cyclic geometry exactly up to reversal. Homogeneity therefore identifies complete types over a finite parameter set with isomorphism classes of finite one-point extensions of the corresponding labeled chord diagram, which are precisely the dihedral extension orbits counted above.

This is also consistent with Simon's general observation that, in an \(\omega\)-categorical structure, complete types over a finite set are stabilizer orbits, and with his use of \(f_M(m)\) as the finite-parameter type-growth invariant for NIP homogeneous structures.

## Verification

The bundled `verify.py` independently enumerates every perfect matching of a cyclic set of \(2m\) endpoints for \(1\le m\le6\). For each labeled matching it computes the full pointwise dihedral stabilizer, its action on unordered pairs of complementary arcs with repetition, and the resulting number of one-chord extension orbits. The maximum nonalgebraic counts are
\[
2,7,21,36,55,78,
\]
so after adding the \(m\) equality types the exact values through \(m=6\) are
\[
3,9,24,40,60,84.
\]
For \(m=3,4,5,6\) these equal \(2m(m+1)\). The verifier also checks directly that the adjacent-pair diagram has trivial pointwise dihedral stabilizer for every tested \(m\ge3\) and returns `VERIFY_OK`.

## Relationship to prior work

Simon introduces \(f_M\), gives the finite-cover classification framework, and explicitly identifies the family obtained from separation relations with finite equivalence classes and quotienting by those classes. The checked paper does not state the above exact type-growth function for its two-point member.

The chord-diagram insertion count itself is standard. Acan's work on uniformly random chord diagrams explicitly notes that, with \(2m\) existing arcs, the next chord has \(\binom{2m+1}{2}\) choices of arcs for its endpoints. That combinatorial fact is not claimed as new here. The contribution is the stabilizer-orbit interpretation for Simon's quotient, the exact small-parameter corrections, and the sharp all-\(m\) formula for \(f_M\).

Targeted exact web searches and five semantic-index searches did not locate this formula, the sequence \(3,9,24,40,60,84,\ldots\) in this model-theoretic setting, or a prior computation of the one-chord extension stabilizer maximum for Simon's quotient. The residual priority risk is that the calculation may exist as an unpublished exercise or folklore consequence of the finite-cover example.

## Limitations

The result is specifically for the \(n=2\) separation-quotient member of Simon's finite-cover family. It does not assert the corresponding formula for arbitrary fiber size \(n\), where adding one quotient point inserts \(n\) endpoints and the stabilizer enumeration is more complicated.

The finite program verifies the dihedral combinatorics through six parameters. The all-\(m\) theorem for \(m\ge3\) is proved structurally by the explicit adjacent-pair base with trivial pointwise stabilizer, not extrapolated from computation.

## References

Pierre Simon, *NIP omega-categorical structures: the rank 1 case*, arXiv:1807.07102. First public version: 2018-07-18. MSC: 03C15, 03C64, 03C68, 06A05. In particular, the introduction defines \(f_M\); Example 1.1 gives the two-element circular quotient; and Section 6.7 describes the separation-relation finite-cover family.

Hüseyin Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489; Discrete Mathematics 340 (2017), 1967--1982. The chord-growth construction records the \(\binom{2m+1}{2}\) one-chord insertion count.
