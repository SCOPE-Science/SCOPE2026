# Scientific review

## Correctness: PASS
The graph has exactly three metric pair types and the semigroup has four explicitly computed spectral multipliers. For each pair type, the proof constructs an admissible plan; for the length-two and length-three pairs it constructs a matching Lipschitz dual potential; for adjacent pairs, every unit of positive mass must travel at least one unit and an all-edge plan attains that minimum. The positive-mass sign pattern follows from \(0<c\le v<u\) for positive time, proved without sampling. Taking a maximum over point pairs indeed equals the full Wasserstein operator contraction coefficient by disintegration over an initial coupling. Finally, explicit differentiation proves the strict time-rate statement and submultiplicativity. Boundary \(t=0\) is verified separately.

The standalone exact-rational calculation within the package was replayed successfully: `CHECK_OK exact_rational_pair_and_transport_checks= 6195 orders=5..14 bases=2,3,5`. It checks every pair at finite prescribed times, but neither substitutes for the all-time proof nor establishes historical priority.

## Originality: PASS, qualified
Münch–Wojciechowski (arXiv:1712.00875, Theorem 3.8) prove a general equivalence between Ollivier curvature lower bounds and Lipschitz/heat Wasserstein contraction bounded exponentially at the curvature rate. Cushing et al. (arXiv:1909.11565, Theorem 6.2) prove that distance-regular girth-four graphs have maximal Lin–Lu–Yau curvature. These results determine the initial contraction rate \(2\) for the present graph family, but do not determine the finite-time coefficient, strict curvature acceleration or exact long-time prefactor. The more recent operator-theoretic semigroup-curvature formulation of Lakzian (arXiv:2610.40301, §§1, 4–5) is primarily infinitesimal, not a stated explicit crown-graph kernel calculation. Targeted literature and prior-statement comparisons found no equivalent formula; this is evidence for qualified, not certified, originality. An earlier name or family-wide exact heat-kernel computation could still cover the formula.

## Mathematical value: PASS
This determines a sharp operator norm throughout continuous time for an infinite natural graph family. Curvature supplies the best *uniform exponential* rate \(2\), but the actual norm decays faster at all positive times, with a strictly increasing instantaneous logarithmic rate ending at the spectral gap \(n-2\). That separation is exact, and the two-exponential coefficient, strict submultiplicativity and persistent adjacent-pair optimality are functional-analytic properties not furnished by a first-order curvature statement alone.

## Limitations and independence
Assumptions and quantifiers are restricted to the unweighted symmetric graph Laplacian and real \(W_1\) for \(n\ge5\); no claim is made for arbitrary weights, normalized generators, or directed chains. Full prior-art priority cannot be independently certified.

Self-review: passed. Independent audit: not yet performed.
