# Independent mathematical audit

## correctness

PASS

Reconstructed the case split in RESULT.md:37–68. A singleton intersection contributes four Fourier coefficients; a nonempty proper intersection contributes at least two since the inverse transform of one frequency is nowhere zero. For two adjacent-pair supports there are two singleton rows and one double row; for one adjacent pair and one antipodal pair there are four singletons. With both support sizes at least two and one at least three, there are four occupied rows, contributing at least eight unless both inputs have full support. Two antipodal pairs produce just two occupied rows, each of size two iff its two values agree up to sign, otherwise four; the exclusive-or criterion is exact. In the full-support case, adjacent pure rows give a shift-one quotient that is a character times a constant; products of shifts give purity of all rows. This excludes five and forces opposite pure rows for six. For their shift-two quotient C i^(dj), applying the shift twice forces d even and C²=1. The odd-shift quotient obeys R(j+2)=(-1)^r R(j), hence has at most two allowable frequencies; squaring R(1)/R(0) shows it has just one iff (v/u)^4=(-1)^r. The shift-three quotient differs from the shift-one quotient by a character times a constant. The two six-point examples work, and singleton/singleton attains four. The frozen verification_output.txt records 65,025 small-alphabet cases (64 sparse and 80 full support-six pairs); verify_z4.py was inspected, not executed. That finite check is corroboration, not a certificate over arbitrary complex coefficients.

## originality

PASS

The validated contribution is the sharp next cardinality and the complete arbitrary-complex pair classification at six, not the minimum-support bound, its equality cases, or a general first-gap theorem. The closest indexed overlap proves exclusion of five as part of a more general exclusion of N+1 but does not supply the next stratum. The later quadrature-phase census confirms a restricted slice of one branch only. Neither the inspected general STFT theorems nor the numerical diagrams cover both exact families. Catalogue dates alone do not establish priority.

## value

PASS

This answers a natural question left after the known uncertainty equality theorem: which exceptional pairs first depart from equality? It characterizes both a sparse cancellation mechanism and a full-support character mechanism with an exact resonance boundary. That information is usable for constructing or recognizing minimal non-extremizers and is not a table lookup or merely the exclusion of one integer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
