# Self-review

## Correctness

PASS. For \(a>0\), the printed treatment
\[
T_b(I)=\frac{aI}{b+I}
\]
has a singular \(b\downarrow0\) endpoint: \(T_b(0)=0\) for every \(b>0\), but \(T_b(I)\to a\) for each fixed \(I>0\). At the nominal disease-free susceptible level and \(B=0\), the positive-\(I\) vector field tends exactly to
\[
(a,-a,0).
\]
The source's own equation (3.9) independently gives infected derivative \((-a,0)\) at the same state. Hence a continuous extension cannot retain the stated disease-free equilibrium, while the extension that forces treatment to zero at \(I=0\) is discontinuous. The bundled symbolic checker verifies the limits and reproduction-number collapse exactly.

## Originality

PASS. Smooth saturated-treatment laws and their role in backward bifurcation are established prior art. The accepted contribution is the exact source-specific endpoint contradiction in the 2023 COVID-19 model. Searches by DOI, title, treatment formula, \(b=0\), reproduction-number collapse, Theorem 3.4, and correction terminology found no published source-specific repair.

## Value

PASS. The \(b=0\) theorem underpins the paper's principal control interpretation that removing treatment saturation eliminates backward bifurcation and guarantees eradication below threshold. The endpoint calculation shows that the theorem is not a classical stability theorem for the printed ODE at all: the disease-free state is incompatible with the continuous positive-infection dynamics. This changes the interpretation of a central analytical conclusion.

## Closest literature and limitations

Open prior literature uses the regular treatment form
\[
rI/(1+\sigma I),
\]
which is continuous and differentiable at the disease-free state and has a regular linear limit when \(\sigma=0\). The motivating source's \(aI/(b+I)\) is a different parameterization whose fixed-\(a\), \(b=0\) endpoint is singular.

A hybrid or nonsmooth capacity-limited model could be defined separately, but it would require a different mathematical framework. The full 2008 primary treatment paper was not available in the inspected open sources and is used only for provenance.

Self-review: passed. Independent audit: not yet performed.
