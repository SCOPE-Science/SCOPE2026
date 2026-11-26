# Independent mathematical audit

## correctness

PASS

In the cube rotation action the four body diagonals identify the quotient with S4. Relative quaternion scalar magnitudes 1/sqrt(2), 1/2 and 0 correspond respectively to quarter turns (4-cycles), third turns (3-cycles), and half turns (the two order-two classes). Even Chebyshev values 13 at 1, 1 at 0 and 1/2, and −1 at 1/sqrt(2) give B=12I+J−2A. On the trivial, sign, 2-dimensional, standard and twisted standard irreducibles the 4-cycle sum has scalars 6,−6,0,−2,2, with multiplicities the squared dimensions. This gives eigenvalues 24,24,12,16,8 and strict positivity. Inverting these central scalars and using the character table gives diagonal 101/1152 and off-diagonal numerators −4,−7,+9,−9 in the stated order. Jacobi's identity reduces each minor divided by det B to (101²−b_h²)/1152². The class sizes 8,3,6,6 multiply by 24/2 for unordered pairs; the unique maximizing class is the 3-cycles and the best/worst ratio simplifies to 2037/2024. I independently generated 24 proper signed permutation rotations, evaluated the kernel from squared relative quaternion scalar (1+trace(R_x^T R_y))/4, recovered eigenvalue multiplicities by an annihilating polynomial and four exact trace moments, and evaluated all 276 retained determinants directly by integer Bareiss elimination. They match 96 at 10185, 36 at 10152, and 72 each at 10120 in the two remaining classes, scaled by 1152²/det B. Replay: python3 /workspace/evidence/1.py, output /workspace/evidence/1.out. This checks the fixed degree and erasure count, not conditioning or arbitrary erasures.

## originality

PASS

The rank-24 statement and hence positive definiteness and principal nonsingularity are covered by the same-geometry all-degree rank record and are not the distinct contribution. On the inspected evidence, the degree-12 spectral multiplicities and the normalized two-erasure minor distribution, including the exact 3-cycle optimizer census, are not given by that record's rank theorem or the other relevant results.

## value

PASS

Degree 12 is the first even degree with full antipodal interpolation on this canonical configuration (the independently inspected rank table certifies all smaller even degrees as deficient). Two erasures are the first cardinality for which the relative position of erased points can matter in a transitive design. The complete determinant census distinguishes every such deletion, revealing both a strict geometrical optimizer and a tie between different rotation classes. The small ratio alone would not motivate the work; the useful exact fact is the identity and multiplicity of every maximizing deletion and the determinant penalty of each alternative at this natural full-rank degree. No claim about larger erasures or conditioning is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
