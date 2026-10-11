# Independent mathematical audit

## correctness

PASS

The exact package proof and verifier agree. The complement of the defining exponent set is 10,11,14, giving parity-check polynomial x cubed plus x plus omega and a three-row cyclic generator. The verifier reconstructs GF(16), the F4 subfield, the cyclotomic cosets, generator polynomial, rank three, and Euclidean self-orthogonality, then exhausts all 64 codewords and obtains weights 0:1, 11:45, 12:15, 15:3. Independently, the normalized generator columns are 15 distinct points of PG(2,4); the six missing points are exactly one projective line plus one off-line point. The 21 projective lines meet the retained set in 0, 3, or 4 points with multiplicities 1, 5, 15, which proves the weight distribution. Exhaustion of all 21 two-dimensional message subspaces gives support sizes 14 or 15 and proves the second generalized Hamming weight 14; the other generalized weights are 11 and 15.

## originality

PASS

The Li--Cao--Li primary article reports the exact Example 4.16 cyclic code as an optimal self-orthogonal quaternary [15,3,11] code, but the inspected article material does not state its full weight enumerator, generalized Hamming weights, or the line-plus-point projective complement. A targeted Resultary search for the exact parameters, projective description, enumerator, and generalized-weight tuple did not return a prior equivalent published finding. The projective interpretation is not mechanically determined by the parameter row alone: it reconstructs the actual column set and then explains all nonzero weights and the second generalized weight.

## value

PASS

The source code is singled out as an optimal self-orthogonal cyclic code, so its exact projective geometry is a natural invariant rather than an arbitrary small-code computation. The line-plus-point complement simultaneously explains the complete weight distribution and the generalized Hamming weights, making the result structurally useful for recognizing or comparing equivalent representatives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
