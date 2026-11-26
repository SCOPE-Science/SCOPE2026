# Independent mathematical audit

## correctness

PASS

At any live state, the probability of reaching the facing endpoint within the next L/v without reversal is at least exp(−K); the Markov property at blocks of length L/v gives a geometric lifetime bound. The outgoing conditions are h_−(0)=0, h_+(L)=1 and m_−(0)=m_+(L)=0 for exit side and time, respectively. Independently solving gives h_+−h_−=p constant and m_+−m_−=τ−2x/v. Integrating h_−'=pλ/v and m_−'=(1+λ(τ−2x/v))/v gives the stated p and τ; at λ=0 the only pair is (1,L/v). For K>0 the centroid B/K is strictly between the endpoints. In the smooth exponential tilt with fixed mass, its derivative with respect to the tilt is L times a strictly positive variance of x/L, and concentration at the two endpoints yields the full open range and sharp unattained edges. A cosine has zero first moment by symmetry about L/2 and zero integral over a period, so small signed perturbations preserve both moments and stay positive on the compact interval; this works for every interior pair, not the deterministic p=1 pair. The supplied simulation uses integrated hazards and bisection, and the archived simulation is only a consistency check; no uploaded code was run.

## originality

PASS

Credit the previously available splitting equations and their direct integrated-rate specialization, as well as the reflecting/absorbing first-passage moment and its renewal relation to τ. The distinct claim assessed is the complete joint feasible region and inverse fibers for the two-absorbing-end injected protocol over arbitrary continuous nonnegative reversal profiles. The checked statements concern pieces, different rate families, or different boundary/start ensembles; no inspected theorem already classifies this joint design problem.

## value

PASS

The boundary-injection measurement protocol motivates the simultaneous calibration problem. The sharp feasible region says exactly which pairs of measurements can be matched by a smooth positive rate, and the moment fibers identify what this protocol can and cannot distinguish. These joint feasibility and inverse facts are useful separately from the rather short forward equations; no significance for full exit-time distributions or multi-start measurements is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
