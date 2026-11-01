# Independent mathematical audit

## correctness

PASS

The normalized positive principal mixed Neumann–Dirichlet eigenmode makes conditional survival exp(-lambda int D_J dt), so Feynman–Kac gives the symmetric positive 2x2 killing matrix. Explicit inversion yields m=(1+2s)/(1+2s-delta²), c=1+2delta²/(1+2s)². With a=1-1/m and e=c-1, the inverse delta=sqrt(2)a/sqrt(e), s=a/e-1/2 has the exact image m>1, 2a²<e<2a; both endpoints are excluded. A new SymPy independent inverse/moment calculation matched the exact formulas. Labels exchange and singular limits are specified.

## originality

PASS

General forward first-passage integrated-diffusivity/Feynman–Kac theory, notably Grebenkov 2019, is prior work. Its inspected exact two-state model supplies a forward distribution, not a global bijective inverse with the strict physically realizable (m,c) region under precisely the principal-mode ensemble. Chen et al 2015 infer states from confined displacement distributions, not these two absorption-time moments. Specific inverse remains best-of-knowledge new.

## value

PASS

The theorem identifies exactly which observed dimensionless first-passage mean and variance can arise, and reconstructs two hidden physical parameters from two scalar measurements. The sharp compatibility region is a natural identifiability boundary, with clear restrictions on initial preparation, labels and calibration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
