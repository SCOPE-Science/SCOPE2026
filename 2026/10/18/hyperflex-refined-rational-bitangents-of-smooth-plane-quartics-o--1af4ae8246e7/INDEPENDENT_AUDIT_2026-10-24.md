# Independent mathematical audit

## correctness

PASS

The finite theorem is explicitly limited to normalized homogeneous ternary quartic equations over F3 and PGL3(F3) orbits. A rational line cut of the curve has even divisor 2P+2Q or 4P precisely when its nonzero binary quartic restriction is a scalar square of a rational binary quadratic; discriminant b²−ac distinguishes nine proper (nonzero) and four repeated-root projective squares. Geometric smoothness is equivalent to rank 36 of the S4^3→S7 gradient-multiplication matrix because the homogeneous partial derivatives are a degree-three regular sequence with quotient top degree 6; Euler degree 4 invertible mod3 eliminates F separately. Source make_tables.py generates group action, thirteen line restrictions, and gradient matrices; census.cpp explores all normalized forms by four elementary PGL3(F3) generators, classifies all 1,557 projective orbits totaling 7,174,453 forms, with 805 smooth orbits/4,099,680 smooth forms. The 1,557 archived orbits.csv rows were independently reaggregated and match all these totals; its unique r+h≥10 row is code 78805, size 312, (r,h)=(9,1), one rational point. Fresh independently implemented line-square restriction arithmetic for F=X⁴+2X³Z+2X²Y²+XZ³+Y⁴ reproduces exactly nine proper bitangents, one hyperflex, and one rational point. This is a finite exact algorithmic proof contingent on the inspected coefficient-action and smoothness algorithms; the full 7.17-million-form orbit traversal was inspected but not rerun in this turn, and the source independent Gröbner tests were not rerun.

## originality

PASS

Best-of-knowledge originality attaches specifically to contact-type resolved F3 joint spectrum and unique 312-form projective maximum orbit, not to Frobenius unrefined rational-bitangent counts already studied.

## value

PASS

The proper-versus-hyperflex distinction is a natural Weierstrass contact invariant for canonical genus-three plane quartics. Complete F3 rational contact joint distribution, number of orbits, and the single maximizing orbit are exact, reproducible finite arithmetic-geometry data useful in studying small-field moduli and ramification; no larger-field theorem is required for this motivated complete finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
