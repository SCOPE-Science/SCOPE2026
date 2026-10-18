# Independent mathematical audit

## correctness

PASS

In char2 with B=x^m+y^m, C=y^m+z^m and P=BC, A=BC+y^{2m}, so F=P²+y^{2m}P and ∇F=y^{2m}∇P. For even m all derivatives vanish; for odd m, ∇P=(x^{m−1}C, y^{m−1}(x^m+z^m), z^{m−1}B) has no nonconstant common factor. The precise projective base locus of ∇P is three coordinate vertices, each local length (m−1)², and m² distinct transverse B=C points of length 1. Two general members in the degree-(2m−1) gradient linear system meet in (2m−1)² points counted with intersection multiplicity; deducting 3(m−1)²+m² gives residual 2m−2>0, so map dominates and this equals total function-field degree even inseparably. The alternating characteristic-two Hessian has generic projective differential rank 1 < 2, giving inseparability. The valuation −1 at a simple prime of x^m+y^m proves irreducibility of A, ensuring reduced F for odd m. Independently checked char2 polynomial identity m=3 and base-length arithmetic, with source verifier formal checks m=2..14. No finite check replaces the all-odd-m proof.

## originality

PASS

Dimca–Ilardi–Pokora–Sticlaru study the same equation over complex numbers and establish freeness and singularity data; they do not obtain the positive-characteristic gradient cancellation, full char2 base scheme, dominant inseparable total degree, or sharp 2m² collapse. The general polar map degree identity over arbitrary characteristic is background, not this explicit computation.

## value

PASS

For a natural free plane-curve family, reduction mod 2 collapses the polar map by a quadratic-in-m amount while leaving a dominant inseparable map at odd m. The exact base-point scheme and intersection calculation describe the mechanism, and provide an invariant of interest for positive-characteristic polar geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
