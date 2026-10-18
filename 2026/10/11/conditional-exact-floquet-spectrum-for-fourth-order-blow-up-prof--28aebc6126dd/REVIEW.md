# Independent mathematical audit

## correctness

PASS

For P_q(z)=product_(j=0)^3(z-eta+j), differentiation gives periodic w' in ker L and scaling yields e^t(w'-eta w) in ker L; the last identity follows from P(D+1)(D-eta)=P(D)(D-eta+4) and 4+(q-1)eta=0. This was independently checked as a polynomial identity. The reflection P(z)=P(-sigma-z), sigma=3-2eta, was also independently verified, so L*=exp(sigma t)L exp(-sigma t). Adjoint monodromy inversion forces multiplier involution mu -> exp(-sigma T)/mu. Applying it to distinct 1 and exp(T) produces exp(-sigma T) and exp(-(sigma+1)T), exhausting order four with no overlaps for q>1,T>0. No numerical orbit computation is used to infer the universal claim.

## originality

PASS

The 2015 primary paper conjectures the general-q values and only computer-certifies hyperbolicity and numerical enclosures near q=3; Matsue (2026) proves two distinguished multipliers but computes other multipliers numerically. Their results do not include or imply the exponential-adjoint operator identity, which supplies the previously missing two exact multipliers for any existing profile. Best-of-knowledge originality is conditional on searched works, not an independence certificate.

## value

PASS

The exact spectrum gives the spectral half of a published explicit conjecture conditional on profile existence; it replaces orbit-specific Floquet numerics with an all-q algebraic law and determines the hyperbolic index. This is a nonstandard structural identity, not a numerical precision upgrade.

The dated certificate retains the supplied scientific assessment, sources and limitations.
