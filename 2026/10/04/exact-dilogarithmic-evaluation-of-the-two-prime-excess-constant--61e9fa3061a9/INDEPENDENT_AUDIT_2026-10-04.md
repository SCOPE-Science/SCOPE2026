# Independent mathematical audit

## correctness

PASS

Differentiating the stated auxiliary Phi gives log(w)/(w+2), so the three antiderivatives differentiate to the corresponding profile pieces. Endpoint substitution leaves Li_2(-1/2), Li_2(-3/4), and Li_2(-1)=-pi^2/12 and yields the displayed closed form. The independent verifier evaluates the convergent dilogarithm series and separately performs split Simpson quadrature, agreeing to about 1e-15. The numerical check corroborates the exact antiderivative proof.

## originality

PASS

Hughes defines the same two-prime excess integral, reports its decimal value, and uses it in the density lower bound, but the accessible source material does not supply the displayed dilogarithmic closed form. Resultary's direct semantic match is the audited finding itself, with no earlier exact symbolic evaluation located. Standard dilogarithm references supply generic identities rather than this evaluated constant.

## value

PASS

The constant occurs explicitly in a quantitative density lower bound. Replacing quadrature by an exact expression provides a reusable symbolic value for comparison and certification, resolving a natural exact constant used by the source.

The dated certificate retains the supplied scientific assessment, sources and limitations.
