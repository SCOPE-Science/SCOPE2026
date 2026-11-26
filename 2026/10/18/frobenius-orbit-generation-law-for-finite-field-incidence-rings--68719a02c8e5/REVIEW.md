# Independent mathematical audit

## correctness

PASS

The diagonal image is polynomial evaluation from F_p[X_1,…,X_k]. Each coordinate is onto exactly when its label generates F_q, or has Frobenius orbit length e; equal kernels for two surjective evaluations are equivalent to conjugacy by a Frobenius power. Distinct maximal kernels give simultaneous surjectivity by CRT, and subfield Möbius inversion gives the number of full orbits. On a cover, the two-by-two restriction is a quotient map. Once its diagonal is full, a nonzero radical kernel gives the whole off-diagonal line by left scalar multiplication using diagonal lifts. If the kernel vanishes the image is commutative; commuting with the lift of (1,0), having off-diagonal entry t, forces each generator's cover entry to be t times its difference of diagonal entries. Conversely this common t places the image in a proper conjugated diagonal algebra. Globally, B∩J is nilpotent and B/(B∩J) is the full separable diagonal product over F_p. A Wedderburn–Malcev complement inside B is also a complement to J in A, so conjugacy by 1+J moves it to the standard diagonal algebra. Conjugation preserves cover-surjectivity; diagonal idempotents then cut out arbitrary cover matrix units with coefficients, whose saturated-chain products give every allowed entry. Thus given valid diagonals, cover restrictions factor independently and the noncovers are free. The count, probability, ratio where defined, and minimum follow, including c=0, k=1 and e=1. Independent exact replay `python3 /workspace/reproductions/incidence_gf4.py` used the F_2-span of words on the two-vertex algebra and returned 1440 unassisted and 2880 scalar-assisted pairs out of 4096; this checks the example, not the universal proof. The frozen verifier was read, not executed.

## originality

PASS

The supported distinct contribution is the complete count for nonprime coefficients without adjoining field scalars, including its local-to-global lifting and the exact factorization. The scalar-assisted law (and thus the prime-field case) and the diagonal quotient count are prior. The full 2023 generator paper could not be inspected; this is a named residual risk, not proof for or against coverage.

## value

PASS

Generation without the coefficient field is a natural distinct operation. The exact law resolves the interaction of a Galois-separation requirement and a nonzero radical, for arbitrary posets and every positive tuple length, with a clean conditional cover count and a poset-independent ratio once size is fixed. It determines when the known scalar-assisted census overstates generation and by precisely how much. The F_4 example exhibits the difference but is not the contribution by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
