# Independent mathematical audit

## correctness

PASS

PASS: With three hypothetical distinct p-th-root zeros A,B,C of a quartic with all five coefficient moduli one, write u for fourth root, s=A+B+C,t=AB+AC+BC. Leading and constant coefficient moduli force |u|=1. Modulus conditions |s+u|=|t+us|=1 imply two quadratics in u over cyclotomic integers. Their resultant must vanish but reduction modulo (1−ζ_p) gives the explicit integer resultant 900, nonzero for every prime p≥7. An independent SymPy determinant evaluation returned exactly 900. The proposed symmetric five-coefficient witness P=(z²−2cz+1)(z²+(2c+a)z+1), c=cos(2π/p), uses a=α+i√(1−α²); the factored discriminant (independently checked symbolically) and the p=7 cubic bound or p≥11 cosine bound show unit moduli. Complete grid evaluation at eighteen primes through 1009 found only Fourier zeros ±1. For p=5, 1+z+z²+z³+z⁴ has four nontrivial fifth-root zeros. These are universal algebraic proofs; finite grids are corroborative.

## originality

PASS

PASS (best of knowledge): Tao’s prime-cyclic support-uncertainty theorem allows four zeros for any coefficients of support five but does not impose equal nonzero magnitudes. The published complete four-tap phase-only classification and consecutive-quadrinomial parity theorem concern length four and cannot force this five-tap bound. Lalín–Smyth studies all-root unit-circle location of self-inversive polynomials, not prescribed prime-order zeros with all coefficient magnitudes one; the length-five continuous merit factor concerns a different statistic. Earlier phase-code/cyclotomic sequence literature could contain an equivalent trick but no directly covering implication was found.

## value

PASS

PASS: The first five-consecutive-tap equal-amplitude sharp Fourier-zero maximum for every prime exhibits a structural reduction of attainable zeros from unrestricted four to two, with a genuine exception at p=5 and an exact universal obstruction via cyclotomic resultant plus explicit sharpness. This is a natural invariant in phase-only finite Fourier uncertainty; not a trivial renaming of length-four antipodal cancellation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
