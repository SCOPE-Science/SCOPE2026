# Independent mathematical audit

## correctness

PASS

The characteristic central line equals the derived algebra. All automorphisms are obtained from a symplectic similitude of multiplier c and an arbitrary central shear; c=1 fixes z, and for c!=1 every fixed vector in the quotient lifts uniquely to a fixed vector after solving the scalar central equation. Fix c!=1. Its fibre has size |Sp_(2n)(q)| and any fixed space is totally isotropic. To verify the stabilizer without characteristic-dependent block coordinates, count ordered independent isotropic r-frames: at step i there are q^(2n-i)-q^i choices, and Sp acts transitively by symplectic basis extension. A multiplier-c element fixing a given frame exists by fixing the e-vectors and scaling the complementary f-vectors by c; the frame stabilizer in that fibre is thus a coset of the pointwise Sp stabilizer. Dividing frames by |GL_r(q)| gives subspaces, so the normalized product of the isotropic-subspace count and its stabilizer count is 1/|GL_r(q)|. The subspace-lattice Möbius factor (-1)^r q^(r(r-1)/2) then gives the printed finite fibre sum. There are q-2 contributing fibres and q^(2n) shears each; division by the total group order yields the stated proportion, and Euler's absolutely convergent product gives the fixed-q limit. This also proves the q=2 zero case and the n=1 specialization, with no odd-characteristic assumption. Independent bounded replay /workspace/branches/5d89a633-f68e-4ab9-97a4-e22692ea83e9/independent_check.py counted 40 of 60 matrices in each nonidentity fibre at (n,q)=(1,4) and 29160 of 51840 in the single nonidentity fibre at (2,3), yielding 1280 and 2361960 automorphisms, respectively. These are finite checks; the bundled verifier was inspected rather than executed.

## originality

PASS

The three-dimensional case is already an exact indexed result, and the finite sum and product already describe a classical general linear fixed-vector law. The supported distinction is identifying that law in every nonidentity symplectic multiplier fibre of rank n and using it to give the higher-dimensional Heisenberg automorphism count over arbitrary finite fields. The strongest inspected finite-size multiplier moment theorem is at positive congruence depth and does not include the nonidentity residue multiplier needed here. The result is not credited as a new general linear derangement formula.

## value

PASS

The exact count answers a natural intrinsic question about the action of the automorphism group on a standard two-step Lie algebra. Its useful structural content is that the multiplier-one fibre is categorically obstructed by the centre while all other fibres have the same fixed-vector-free law, controlled by half the symplectic quotient dimension. This gives a uniform density in higher dimensions and in even characteristic, rather than a new table entry at a selected small field or merely recomputing the known three-dimensional case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
