# Independent mathematical audit

## correctness

PASS

Direct expansion of the exact Fromage map gives the norm identity. The sharp lower bound on \((x^\top Hx)/(\|x\|\|Hx\|)\) is attained by the two-eigenvalue witness with squared coordinate ratio \(\mu/L\), producing exactly the submitted condition-number factor and the \(\eta=1\) minimizer. Removing only the Fromage prefactor gives the submitted proportional-update quadratic and its sharp interval. In one shifted dimension the official update is multiplication by \((1+\eta)/\sqrt{1+\eta^2}\) below the minimizer and \((1-\eta)/\sqrt{1+\eta^2}\) above it; the trapping interval and logarithmic circle translation follow exactly. The official implementation was read and confirms that even at zero gradient the global \(1/\sqrt{1+\eta^2}\) prefactor is still applied. Fresh numerical identities independently reproduced the sharp witness and the circle-coordinate conjugacy.

## originality

PASS

Bernstein et al. define the exact prefactored Fromage rule and compare it with LARS, but do not give a sharp condition-number analysis on centered SPD quadratics. Gitman--Dilipkumar--Parr already analyze the unprefactored one-dimensional proportional update and show fixed-step oscillation near a nonzero minimizer; that prior result is therefore not credited as new here. The audited contribution that survives comparison is the exact prefactored Fromage behavior: the centered sharp factor together with the translated-map rotation conjugacy. No Resultary hit or inspected primary source implied those statements.

## value

PASS

The theorem isolates a mathematically sharp origin-dependence pathology in a named optimization rule: centering yields an accelerated-looking condition-number factor, while translation creates persistent nonconvergence with an exact dynamical normal form. The contrast is structurally informative beyond a numerical counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
