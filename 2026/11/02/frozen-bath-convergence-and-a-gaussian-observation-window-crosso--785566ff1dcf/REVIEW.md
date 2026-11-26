# Independent mathematical audit

## correctness

PASS

For the stationary tracer-only reset model at fixed r>0, the generator of x²+γq² is 4−rx²−2(x−q)². This is coercive for each fixed γ; the no-reset Gaussian transition supplies irreducibility, and conditioning on reset times gives the strong Feller property. The second-moment equations give V=1+H, (rγ+1)H=γ+U, and (r+2)U=2H+2, verifying the displayed moments, uniform bounds, and V→1/k. The compensated reset martingale has variance t(2+rU). On the γ timescale the tracer integral equals the bath integral divided by 1+r plus the stated remainder. For the bath-minus-OU difference the Volterra solution is R(u)−k∫₀ᵘ exp(−k(u−v))R(v)dv; its deterministic-time and integrated L² estimates do not require an unjustified bound on the expected pathwise supremum. Tight stationary initial bath laws therefore limit to the unique invariant OU Gaussian. For the joint limit, use test products and a countable smooth core to obtain the frozen generator identity for almost every q. With finite conditional second moment it extends by cutoff to e^{iξx}. The difference δ of any two candidate characteristic functions solves δ′=(iq−ξ−r/ξ)δ off zero; boundedness at zero forces the coefficient of e^{iqξ−ξ²/2}|ξ|^{−r} to vanish on both sides. The last-reset exponential age law gives the claimed invariant kernel. For comparable windows the Gaussian variance is the integrated stationary OU covariance divided by (1+r)²s². Second moments converge as well: for the coupled OU process its covariance differs from stationary OU covariance by (Vγ−1/k)e^{−k(u+v)}, and the integrated difference errors vanish in L². Short windows have a frozen initial bath plus an O(T⁻¹) mean-square tracer error; long windows follow from positivity of the mean matrix exponential and the resolvent integral (U+γH)/r=O(γ). Φ=2∫₀¹(1−u)e^{−zu}du checks normalization and strict decrease. This establishes the asserted regimes and joint weak limit, not uniform tails. The supplied finite moment/covariance checker was inspected, not executed or used as proof.

## originality

PASS

Best of current knowledge, the distinct claim is rigorous joint invariant-law convergence and the distributional observation-window classification. The generator, model, quasi-static candidate (including its frozen-q construction), and much second-order information already exist and get no originality credit. The strongest exact same-protocol comparisons do not give the joint convergence or Gaussian path-average laws.

## value

PASS

This resolves a concrete approximation for a pre-existing stochastic model as an actual joint stationary limit, and identifies when averaging fails to remove a calibration offset despite arbitrarily long observations. The middle-window law gives the full distribution, including the explicit interpolation between noncommuting limits; covariance alone cannot replace it. Scope is fixed r, stationary start and tracer-only resetting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
