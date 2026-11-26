# Independent mathematical audit

## correctness

PASS

A nonzero projection of the exact rank-one sketch onto e_S recovers H_S; P_S is diagonal and the independently sampled spectral estimator gives eta=alpha(P_S)_{TT}. For each coordinate the four equiprobable environments yield gains alpha, alpha, alpha t, alpha/t. Conditioning on the held environment and averaging the gradient sample gives Q(g)=(1+(1−g)^2)/2. With independent gradients over time the cached law therefore averages Q(g)^k, whereas fresh environments average Q(g) before the kth power. Summing the two coordinate squares requires no coordinate independence and includes k=0 and zero initial coordinates. Only alpha/t can reach 2, giving the cached boundary rho=alpha/(2−alpha) with residual weight 1/4 there. For alpha=1/2 the refreshed factor is (s²−4s+24)/32 with s=t+1/t>2; monotonicity on t in (0,1) yields the stated unique cutoff and its equality/divergence cases. Independently, at rho=1/4, alpha=1/2 the exact Q-values are 5/8, 181/200, 13/8, with fresh weighted average 189/200. The cached divergence is consistent with decaying conditional means since the mean multipliers 1−g/2 have modulus below one. This is conditional mean decay, not an absolute first-moment or almost-sure claim.

## originality

PASS

The exact finite-environment phase boundaries for this particular spectral-step/gradient-sampling mechanism are distinct in the inspected material. The qualitative principle that sampling reuse can change second-moment stability is already known and is not credited as new.

## value

PASS

The two-coordinate interpolating system isolates a specific pitfall of the existing spectral-step design: perfect conditioning of the full Hessian and decaying mean iterates do not preclude mean-square divergence when both sampled quantities are reused. The exact nonempty stability gap supplies a useful counterexample and quantitative boundary for the prescribed comparison, rather than an arbitrary finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
