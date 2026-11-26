# Independent mathematical audit

## correctness

PASS

The four linear characters see only the pair sums u on Q8/{±1}; the faithful irrep sees the pair differences v with determinant sum(v_c^2), and its block vanishes exactly when v=0. For real amplitudes this leaves ranks 0 and 2 only. The rank of the regular multiplication operator equals the sum of dimensions times Fourier-block ranks (the adjoint convention replaces f by its inverse-indexed function and preserves rank). The product lower bound also follows by greedily taking translated rows with a nonzero entry outside the union of the previous supports; those rows are independent, and a maximal union covers all eight positions. Odd support excludes either sector alone. One nonzero Walsh coordinate forces u nonzero at all four positions, which excludes complex weighted rank 3 at t=3 and forces real weighted rank at least 6 there; rank 2 at t=5,7 needs one sector alone. Over the reals odd supports 5,7 need both sectors and cost at least 5. At real t=6 a nonzero v costs at least 4; if v=0, u has exactly three nonzero entries, impossible with one or two nonzero Walsh coordinates. All sixteen reported upper witnesses were recomputed by exact rank of 8×8 regular multiplication over algebraic number fields, yielding both displayed profiles. Replay: python3 /workspace/reproductions/group_rank.py (SymPy). This checks witnesses, not impossibility for unrestricted amplitudes; the latter follows from the sector arguments. The supplied checker and verification notes were inspected, not executed.

## originality

PASS

The supported distinction is the simultaneous exact-support classification across coefficient fields, especially the real table and its discrepancies at 3,5,6,7. Credit the prior rank-weighted bound and exact two-point row. A distinct later Resultary complete complex spectrum genuinely determines the entire complex table, not merely a related object; it does not determine the real table and gives no evidence of prior coverage of the October claim.

## value

PASS

This natural eight-element test case isolates a real-versus-complex obstruction for a genuinely matrix-valued Fourier transform: the quaternionic block permits complex isotropic rank one but forbids real rank one. A user of the invariant needs the exact-support values, not an at-most-support envelope that hides the four discrepancies. The table is useful as a benchmark for sharp finite-group uncertainty and compares genuinely different coefficient fields without relying on a novelty claim for the product bound or the two-spike case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
