# Independent mathematical audit

## correctness

PASS

The uniform initial point gives J=1 on contraction and P(J=j | expansion)=2^(-j-1), hence E[J]=1 and τ=1+H_J, with H_0=0. After launch, levels strictly above zero follow a walk with up probability q=1-p and down probability p until the hit. An independent reflection check verifies the constant and signs: for N=n−1 and a free walk S_N started at zero, P(H_j>N)=P(1−j≤S_N≤j)+(1−(p/q)^j)P(S_N≥1+j). Reflecting a path's segment through its first hit converts start j to start −j and increases the number of up steps by j, which gives the weight (p/q)^j in the subtracted paths. With p=p_n and fixed j>0, the first interval contains exactly j points of the allowed parity; Stirling's formula gives mass asymptotic to 2φ(u)/sqrt(n) at each (φ is the standard normal density). The ordinary limit for this triangular array of bounded increments gives P(S_N≥1+j)→Φ(−u), since the drift of S_N/sqrt(n) tends to −u and the variance to 1. Also sqrt(n)(1−(p_n/q_n)^j)→−2uj. The binomial maximum is bounded by C/sqrt(n) uniformly for large n, and the positive part of 1−(p_n/q_n)^j is at most C_u j/sqrt(n), by the geometric sum when p_n≤q_n and zero otherwise. This bounds the scaled tail by C'_u j and justifies averaging the fixed-height limit against the geometrically bounded launch laws. The result is 2φ(u)−2uΦ(−u), with derivative −2Φ(−u). Eventual escape from j>0 is 1−(p/q)^j for p<q and zero otherwise; averaged over J it adds scaled mass −2u for u<0. The ballot proof's parity factor and the n−1 horizon are therefore consistent. The stated generating function also follows directly from h=z(p+qh²) and E[h^J]=qh+p/(2−h).

## originality

PASS

The verified overlap covers the dyadic model, the biased-walk transforms, the same top-band generating function and the critical u=0 slice. Pass the two-sided moving-bias return-duration profile, including the escaped mass, rather than any of those ingredients. No inspected stronger result supplies the fixed-height survival asymptotics at the required window or their averaged top-band consequence.

## value

PASS

The scale is forced by balancing mean walk drift over n steps with sqrt(n) fluctuations, not by choosing arbitrary parameter values. The exact crossover quantifies how critical slow returns change under either sign of a perturbation, and on the transient side separates escape from paths that will return after the observation horizon. That distinction is invisible from the recurrence dichotomy and from the exact critical amplitude alone. The result supplies a duration profile complementary to the known geometric launch/reset and depth quantities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
