# Review of the integral cohomology lattice theorem

## Correctness — PASS
The assertion is for ordinary integral singular cohomology of the normal complex surfaces associated with genuine two-dimensional matrix pencils. The proof uses the precise birational resolution and contracted-curve configuration in [1, Propositions 3.7, 4.1, 4.5 and Theorem 4.6]. Its critical step is **integral**, not merely rational: the classes of contracted chains are adjacent differences of the total exceptional basis, hence form a saturated path-incidence lattice; if the line at infinity contracts, its coefficient on the pullback line class is one, preserving saturation. This makes the integral restriction map in the Leray sequence surjective and rules out degree-three torsion. The integer cup-product pairing is then calculated in an explicit integral basis of the orthogonal complement. The stated determinant follows from an exact rank-one determinant identity. A standalone checker verifies multiple nontrivial finite block configurations but is not the basis of the proof.

## Originality — PASS, with literature risk
The nearest original manuscript [1] supplies the rational numerical Weil-divisor pairing and the resolution geometry. Its Theorem 4.8 is over \(\mathbb Q\), not an integral description of ordinary singular cohomology, and the inspected sections do not give the primitive integral orthogonal complement or exclude torsion in degree three. Searches specifically for matrix-pencil Schubert compactifications, integer cup products, torsion-free cohomology and Kronecker-block lattice presentations produced no identified result with the stated integral formula. Chataur--Cirici [2] work in rational homotopy and do not give this integral calculation. An equivalent calculation elsewhere remains a genuine residual risk; the search evidence does not prove global novelty.

## Mathematical value — PASS
The new statement is a complete **integral ring classification for all matrix-pencil Schubert compactifications**, rather than a finite example or a routine rational-rank restatement. Integrality matters because isolated cyclic quotient singularities can introduce lattice-index and torsion phenomena that a rational intersection pairing cannot detect. The formula isolates precisely which Kronecker data survive in the integral cup-product ring, computes discriminants, and proves that detailed singular indices, eigenvalues and Jordan multiplicities are invisible to this topological invariant. This can be used to distinguish and compare singular Schubert surfaces with the same rational ranks.

## Closest literature and limitations
[1] V. Galgano, F. Gesmundo, H. Keneshlou, *Schubert compactifications of matrix pencils*, arXiv:2610.07164v1, Sections 3.3 and 4.1--4.3 (read in the available primary PDF).

[2] D. Chataur, J. Cirici, *Rational homotopy of complex projective varieties with normal isolated singularities*, arXiv:1503.05347 (abstract inspected; different rational focus).

Not claimed: an integral Chow ring, local class groups, intersection cohomology, a homeomorphism classification, or positive-characteristic analogues. Relevant older general surface topology may contain an equivalent specialization; no claim of exhaustive coverage is made.

Self-review: passed. Independent audit: not yet performed.
