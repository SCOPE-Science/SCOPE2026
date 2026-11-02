# Independent mathematical audit

## correctness

PASS

Solved the coupled backward Laplace equations using stationary gate mean F and difference W. The exact transform is 1/[cosh(sqrt u)+q sqrt u sinh(sqrt u)*h(z+u)], z=(alpha+beta)L^2/D, q=beta/alpha, h(z)=coth(sqrt z)/sqrt z. Expansion yields m=1/2+q h(z), v=m^2-m/3+1/12-2(m-1/2)h'(z)/h(z). The Mittag-Leffler expansion of h as an integral of a strictly positive Laplace kernel makes (log h)' strictly increasing from -infinity to 0. Therefore every datum in the strict feasible half-region has exactly one z, q, and pair of positive rates. Independently tested rate reconstruction and moment floor for multiple parameter choices, with independent backward boundary-matrix checks in the inspected package. The inequality is strict at any finite positive rate.

## originality

PASS

Rate inference from full gated first-passage distributions and short-time detection tails was established by Kumar-Scher-Reuveni-Santhanam (2023), and forward gated diffusion moment transforms by Bressloff-Lawley/Bressloff. The inspected Kumar author-preprint main text and supplemental Section S6 explicitly use short-time density limits (not only the stationary-gate absorption mean and variance at one initial point); they do not provide this globally bijective two-moment image or the sharp variance feasibility floor. Best-of-knowledge originality survives, with cautious specialist-literature residual risk.

## value

PASS

An experimentally natural inverse problem is reduced from a full distribution to two low-order time statistics, and an exact attainable region plus sharp unrealizable boundary is proved for the nontrivial coupled-boundary model. Exact structural identifiability and feasibility can inform inverse diffusion studies even if noisy statistical conditioning is not covered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
