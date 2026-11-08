# Independent mathematical audit

## correctness

PASS

Adjoint integration by parts gives J=p(0)x0+int sigma u; minimization on each grid cell exactly yields int|sigma|-|int sigma|, zero except cells containing roots. Taylor C² remainder and 2-Lipschitz control of this local functional yield uniform h³ error for finite isolated roots. Fourier expansion g=1/12+sum(-1)^k cos(2pi k r)/(pi² k²) gives mean sum slopes/12 and m-dependent variance (2pi⁴)^(-1) sum k^-4 |sum slopes exp(2pi i k m tau)|²+O(h). Equal slopes at roots 1/4,3/4 give coefficients 1/180 for even m, 1/2880 for odd m. Independent exact rational phase moments checked. No general asymptotic fixed constant is improperly asserted.

## originality

PASS

Bourdin-Trelat gives qualitative sampled-data convergence, Aghaee-Hager optimizes free switch times, Scarinci-Veliov uses enriched within-cell switch approximations. Resultary qubit control phase law has nonlinear endpoint and cubic time loss, unlike this exact scalar linear objective and quadratic shared-phase variance.

## value

PASS

Shared-grid phase correlation and exact parity resonance quantify reproducibility/uncertainty of sampled bang-bang control; complete leading profile and sharp factor-16 variance split are motivated by actual fixed-grid restrictions, not arbitrary numerical slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
