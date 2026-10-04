# Same-model review

## Correctness
PASS. The argument identifies the coordinate-squaring map as the function-field quotient by the 256-element projective sign group using the exact generic fiber size. Transitivity of a Galois group on prime divisors above a fixed prime divisor gives one sign orbit for each 64-component diagonal family. The explicit square reflection exchanges the two quotient lines, and orbit--stabilizer yields the stated stabilizer orders. `verify_orbit.py` checks the finite permutation and order arithmetic.

## Originality
PASS. The motivating paper gives the ingredients separately: the full automorphism group, the two 64-conic families, and the reflection. It does not state that the 128 conics form one automorphism orbit, nor the two stabilizer orders. Its later discussion still refers to two families. The older quasi-hyperbolicity paper proves finiteness phenomena but does not classify these conics or their orbits. Direct semantic and exact-phrase searches for the orbit/stabilizer statement and equivalent quotient language found no covering result. Residual risk remains for unindexed literature.

## Value
PASS. Auel--Singer explicitly leave open whether their 128 conics are all conics on the surface. Showing that the entire known catalogue is one automorphism orbit is a structural reduction directly adjacent to that classification problem: one representative determines every known conic by symmetry, and any additional conic must lie outside this known orbit. The stabilizer orders quantify the symmetry of a representative and can be used in subsequent orbit-counting or incidence calculations.

## Closest literature and limitations
Auel--Singer, arXiv:2609.09351v1, is the closest source and contains all geometric premises but not the orbit theorem proved here. Bruin--Thomas--Várilly-Alvarado, arXiv:1912.08908, proves algebraic quasi-hyperbolicity of the same surface but not a conic-orbit classification. This result does not settle completeness of the 128 conics and does not determine the abstract stabilizer groups.

Same-model review: passed. Independent audit: not yet performed.
