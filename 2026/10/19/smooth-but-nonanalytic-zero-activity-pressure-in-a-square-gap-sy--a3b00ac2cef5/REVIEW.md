# Independent mathematical audit

## correctness

PASS

Admitted blocks can be extended on both sides to marked words; concatenating returns of lengths 2 and 5 gives every sufficiently long bridge. For each z>0 the decreasing renewal sum gives a unique positive root p. On an ergodic component with positive marker frequency, Kac and Abramov reduce the variational bound to the relative entropy against the law q_m=z exp(−p(m²+1)). The return alphabet has finite one-symbol entropy under a finite mean length, and equality in the entropy-rate bound requires independent returns. The q-renewal measure attains the bound, whereas the zero-marker component is the all-zero point mass and has strictly smaller pressure. After Poisson summation, set w=√p and let E(w)=2√π∑_{j≥1}exp(−π²j²/w²), extended by zero at w=0. Gaussian bounds dominate every fixed derivative at zero, so E is smooth and flat. The equation F(w,z)=2w−z exp(−w²)(√π−w+E(w))=0 has derivative 2 in w at (0,0); the analytic surrogate deletes E and has the same full Taylor jet. Expanding the surrogate gives the displayed coefficients. For w₀=√P_an, the mean-value theorem for F on [w₀,w] gives w−w₀=z exp(−w₀²)E(w₀)/(2+o(1)), because both endpoints tend to zero and F_w is continuous there. Using E(w₀)∼2√π exp(−π²/w₀²), w∼w₀∼√π z/2, gives exactly the leading pressure gap with coefficient 4P_an. Its strict positivity rules out analyticity. Finally the equilibrium marker frequency is the inverse mean length, with mean asymptotic 1/(2p) from the differentiated theta expansion; h=p−ρ log z then yields the entropy law. Independently computed direct Gaussian roots, using 320 decimal digits and truncating at the ceiling of √(760/P_an), with a geometric sum-tail bound below 10^(−320), gave correction ratios 0.9028980, 0.9390685 and 0.9567343 at z=0.35, 0.25 and 0.2. The supplied checker was inspected but not executed; its documented replay is `python3 verify.py` from the package directory with mpmath. Finite numerical agreement is not the boundary proof.

## originality

PASS

Credit the exact square-gap zero-activity result: a smooth yet nonanalytic pressure with a specified analytic Taylor representative and an exact positive leading flat correction. The general mixing and renewal facts and the Gaussian theta identity are established inputs. The closest same-schedule sources inspected have related but non-equivalent stated conclusions.

## value

PASS

This explicit renewal system distinguishes a smooth pressure at zero activity from an analytic one even though all Taylor coefficients agree with a concrete analytic branch. The exact positive scale and prefactor resolve the discrepancy missed by any power expansion. That distinction, rather than the standard renewal equation or leading density scale alone, gives the example scientific use in studying boundary regularity of symbolic pressure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
