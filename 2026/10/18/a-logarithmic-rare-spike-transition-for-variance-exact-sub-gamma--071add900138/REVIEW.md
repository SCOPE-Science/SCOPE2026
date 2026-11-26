# Independent mathematical audit

## correctness

PASS

The centered rate-one Poisson cumulant is E[exp(tJ)-1-tJ], so the stated G kernel gives the exact normalized mixture (1-w_B)G_0(t)+w_BG(Bt), with w_B=e^(-h_B)B^2/V_B and V_B tending to v_0. The scale variational formula follows by rearranging on t<1/c and bounding Psi by 1/t outside that range. At z=Bt=h_B-2 log(B/h_B)+s, z/h_B tends to one and t tends to zero. Consequently w_BG(z) is asymptotic to 2 exp(s)(h_B/z)^2/V_B, giving both fixed-s limits with the stated normalization. To check the global optimum, for t below (1-epsilon)h_B/B the Psi upper bound is O(1)+O(B^3 exp(-epsilon h_B)), using the bounded Beta transform derivative. Above that threshold use 1/t. At (1+epsilon)h_B/B the spike contribution diverges, so Psi is asymptotic to 1/t there, proving c_B~B/h_B after epsilon decreases to zero. For every fixed integer r the spike moment e^(-h_B)B^r tends to zero. The centered cumulants then imply moment convergence, and a Poisson coupling with vanishing spike probability and convergent deterministic centers gives weak convergence. For the limiting law the series G(tJ_0) is bounded by (1-Kt/3)^(-1) on t<3/K, giving a finite scale. When J_0=1 the origin attains the lower bound in the limit t down to zero, proving scale 1/3. The origin slope for the spiked laws tends to 1/12-1/9=-1/36; continuity on [0,infinity), decay at infinity and the diverging supremum then give an interior global maximizer for large B. The diagnostic checker was inspected, not executed. It does not establish a global optimization limit or uniformity for varying s.

## originality

PASS

The transform, the exact variational representation and qualitative interior optima are covered by Chen and are not new. The distinct claim is the sharp moving-spike scale and fixed-s logarithmic profile for a bounded Poisson base, with discontinuity despite convergence of every fixed moment. The closest rare-jump catalogue theorem overlaps in mechanism but not the stated hypothesis regime or profile.

## value

PASS

The true variance and all fixed moments can stabilize while the best right-sided sub-gamma scale diverges at a precise rate. The explicit transition shows where the escaping spike dominates despite a locally decreasing canonical profile. This quantifies a real instability of variance-exact concentration bounds, not just a fixed numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
