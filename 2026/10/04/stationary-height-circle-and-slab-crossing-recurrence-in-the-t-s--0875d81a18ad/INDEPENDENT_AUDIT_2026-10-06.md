# Independent mathematical audit

## correctness

PASS

For \(F=y^2+z^2-2mz\), exact differentiation gives \(LF=-2nz(z-m)\); stationarity therefore yields \(\mathbb E[z^2]=m\bar z\) and the variance parabola \(\operatorname{Var}(z)=\bar z(m-\bar z)\). Stationarity of \(x^2\) and \(z\) gives \(\mathbb E[x^2]=\mathbb E[xy]=n\bar z\). Applying stationarity to arbitrary antiderivatives \(\Phi(z)\) yields \(\mathbb E[xy\mid z]=nz\). At \(\bar z=0\) or \(m\), zero variance fixes the height, and invariant-support tangency leaves exactly the origin or the two nonzero equilibria. For a measure not supported on these equilibria, the continuous function \(z(z-m)\) cannot vanish almost surely, while its stationary mean is zero; hence both its negative region \(0<z<m\) and positive exterior have positive mass.

## originality

PASS

The complete open 2021 primary article was inspected. It identifies the same polynomial \(F=y^2+z^2-2mz\) as a first integral in the special conservative boundary case \(n=0\), with invariant cylinders. The audited theorem instead treats \(n>0\), where \(F\) is no longer conserved and its exact derivative becomes a stationary moment circle, a conditional product law, rigid endpoints and a slab-crossing theorem. Those implications are not stated in the inspected T-system literature. Resultary searches returned only analogous stationary laws for other flows.

## value

PASS

The T-system is a standard Lorenz-family model, and the theorem converts a known conservative-boundary polynomial into a sharp positive-damping stationary geometry: a fixed second-moment circle, rigid endpoint measures and forced recurrence on both sides of a natural slab. This is a motivated structural description of recurrent dynamics rather than a routine numerical check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
