# Independent mathematical audit

## correctness

PASS

At a=4, b=beta=c=d=e=1, f=3/2, 4<alpha<6, positive coexistence requires H=2 and P=6-alpha>0. Prey-only equation H²-3H+alpha-4=0 has roots H_- in (0,1) and H_+ in (2,3); with origin these are all four nonnegative fixed points. Origin multipliers e^(4-alpha),e^-1 are both <1; coexistence J=[[1/3,-2/3],[(6-alpha)/6,1]], trace 4/3, determinant 1-alpha/9, Jury margins alpha/9,(6-alpha)/9,(30-alpha)/9 >0, so both sinks. At prey-only H, multipliers lambda_H=1+H(3-2H)/(1+H), lambda_P=exp((H-2)/(2(1+H))). H_- is saddle. H_+ has lambda_P>1 and lambda_H crosses -1 at H=(5+sqrt41)/4, alpha_F=(29+sqrt41)/8, giving source for alpha<alpha_F, nonhyperbolic at threshold, saddle above. Algebraic checks independently recomputed original map Jacobian, exact alpha_F and inequalities; package verify.py inspected, finite parameters corroborate not replace the analytic all-alpha proof.

## originality

PASS

Read complete accessible originating Seralan et al. 2023 article §§2-5, especially exact exponential map (2.3), weak-Allee restriction stated on p.22899, and local eigenvalue Lemmas 2-3. The source analyzes alpha<a beta weak regime; for alpha>a beta the origin is a sink, whereas its weak-regime Lemma 2 says origin always saddle. Therefore its weak-region classification does not imply strong-Allee bistability, four-equilibria region, or alpha_F. Al Khabyah et al. use a different Euler-discretized strong-Allee equation; Cai et al. use a continuous diffusive counterpart (the latter was not fully accessible). Earlier Resultary Ricker source-criterion correction addresses different weak-regime stability, not this exact family.

## value

PASS

Exact local coexistence/extinction bistability and a source-to-saddle transition of the upper prey-only equilibrium resolve a natural qualitative strong-Allee regime in the same exponential ecological map. This provides all fixed points and their spectral types for a connected open parameter interval, not just one numerical witness. No global basin partition, ecological realism, or nonlinear flip bifurcation is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
