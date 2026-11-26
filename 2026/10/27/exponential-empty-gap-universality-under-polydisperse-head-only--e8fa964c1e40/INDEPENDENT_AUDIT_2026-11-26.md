# Independent mathematical audit

## correctness

PASS

At fixed finite t, bounded mark reach gives a graphical construction: for heads in a bounded window, the expected number of time-ordered backward chains of k+1 proposals is at most the window length times Λ(2ℓ₊)^k Λ^k/(k+1)!. Thus there are no infinite ancestry chains, locally the relevant Poisson graph is finite, and chronological acceptance is well defined. Survival of a fixed interval requires no interior proposal, since any head there would be accepted until the first hit. Until the first contact with the test interval, connected intervals from opposite sides cannot influence each other's decisions; the two killed half-line processes and the absent interior proposals are independent. Applying the same split at one point gives F=S₋S₊, so the interval survival probability is F exp(-Λx). Fixed endpoints have probability zero of being deposition endpoints by spatial diffuseness. All proposal heads are covered by time t, including rejected heads, so the spatial Poisson heads of positive intensity bound every vacant component on both sides. Bounded reach also gives locally finite boundary intensity and F≥exp(-2ℓ₊Λ)>0. The length-g gap contributes (g−x)₊ to the measure of possible test origins; the stationary Campbell identity and its second distributional derivative give q_t(dx)=FΛ² exp(-Λx)dx and its claimed normalization. The proof does not infer independence of gaps or a temporal stationary law. The supplied Monte Carlo script is diagnostic, not needed for the proof.

## originality

PASS

Only the generality is credited: the fixed-length, orientation-symmetric constant-rate head-only void law and the normalized gap law are already known. The inspected sources do not cover the full marked head-only claim or its factorization argument.

## value

PASS

Exact universality of the count-sampled law when the mark-dependent coverage fraction and kinetics can change is useful. The proof explains which acceptance mechanism, rather than any closure specific to fixed lengths, controls the gap law. It separates the length distribution from both coverage and correlations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
