# Independent mathematical audit

## correctness

PASS

In a block of size b, the Pawlak boundary contains the whole block if the sample is nonempty and proper, and none otherwise. The two excluded events have total probability q_b, and disjoint blocks have independent contributions. Singleton factors are 1. For b>=2 the odds ρ_b=(1−q_b)/q_b are known and positive; normalize by the positive constant term F(0). The coefficient in degree b after cancelling only known factors in degrees below b is exactly m_bρ_b: multiple selections of a degree-b factor and all higher factors have degree >b. Apply this in the truncated power-series ring through degree K or through deg F for the full inversion; an empty universe and an all-singleton partition both correctly give F=1. Knowing |X| recovers the singleton number by subtraction. The sharp raw-prefix example at p=1/2 gives equal constants 2^(−2K−2), no positive terms through K, fixed total 2K+4 and two classes, yet only (K+1,K+3) has positive coefficient in degree K+1. The rough-pair lattice is the independent block product of two- and three-element chains. At p=1/2 the profiles (2,4) and (3,3) both have two three-element factors but clearly different boundary laws. In a fresh integer replay (`python3 /workspace/review-evidence/exact_checks.py`), all 291 partition/bias cases and 71865 subset evaluations agreed with factorization. This does not prove general inversion. The frozen verify_boundary.py was inspected, not run; its use of int.bit_count() requires Python 3.10+, not the stated 3.8 minimum.

## originality

PASS

The product law is a direct use of independent block contributions and the Pawlak lattice structure is established context. The distinct contribution supported on inspected evidence is the exact recovery of the nonsingleton multiplicities from this boundary-size observable, its degree-local recovery and sharp fixed-metadata obstruction, and the resulting separation from the abstract lattice. Nearby indexed results recover different invariants, under different observation models, or on tolerance rather than equivalence relations.

## value

PASS

The boundary is a canonical rough-set observable. Its size law distinguishes equivalence granulations of fixed universe size even when their abstract rough-set lattices are indistinguishable, and the sharp degree cutoff specifies precisely which sizes survive a restricted exact observation. This is an interpretable inverse classification and a concrete information-loss witness, not just a routine calculation of a PGF or expectation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
