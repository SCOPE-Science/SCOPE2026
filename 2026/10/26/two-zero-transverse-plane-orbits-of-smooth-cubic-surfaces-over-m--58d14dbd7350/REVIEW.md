# Scientific review

## Correctness

**PASS.** Exact exhaustive enumeration of binary cubic surface equations (\(2^{20}-1\) nonzero forms) uses an algebraically complete rank test for geometric surface smoothness and a degree-at-most-three closed-point criterion for singular plane cubics. Both critical facts are proved in `RESULT.md`. Independently checking the two representative equations with symbolic Gröbner bases confirms all fifteen sections singular; group orbit enumeration of the complete 1708-mask exceptional set yields orbit sizes 28 and 1680. The count of all smooth binary cubic surfaces is 322560. Included code and outputs were executed successfully.

## Originality

**PASS, qualified.** The 2024 Asgarli–Duan–Lai transversality bounds do not cover this small-field parameter. Vikulova identifies the maximally symmetric 28-orbit by its automorphism order 720, but does not determine zero smooth sections or the additional 1680-orbit. Published research-record and primary text comparisons found no equivalent theorem or stronger encompassing statement. Karaoğlu's 2021 Dickson-derived full article could not be accessed; the possibility of implicit coverage in older tables remains an explicit publication-priority risk. The 28-orbit's known existence is not new.

## Value

**PASS.** The theorem completely resolves a natural finite-field Bertini boundary case, proves a sharp zero-or-at-least-four plane-section gap, and separates two geometrically distinct projective classes of obstructions. The additional 1680-orbit shows failure of smooth rational hyperplane sections is not solely a consequence of the known fully point-filling cubic surface.

Self-review: passed. Independent audit: not yet performed.
