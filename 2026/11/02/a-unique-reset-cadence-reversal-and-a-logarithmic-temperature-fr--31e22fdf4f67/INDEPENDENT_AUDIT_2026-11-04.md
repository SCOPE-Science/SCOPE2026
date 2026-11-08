# Independent mathematical audit

## correctness

PASS

For OU relaxation to variance D/lambda with independent N(0,cD/lambda) redraws, 0<c<1, b=(1-c)/c>0 and x=2lambda/r>0, the symmetrized centered Gaussian endpoint KL per cycle is F_b(t)=(q_b(t)+1/q_b(t)-2)/2 with q_b=1+b(1-e^{-t}). Renewal reward gives periodic rF_b(x), Poisson rE[F_b(xU)] for U~Exp(1). Direct differentiation factors F_b_second=(b e^{-t}/(2q_b³))(2(1+b)-q_b-q_b³), so it changes sign exactly once from positive to negative. The difference Δ=∫F_b_second(s)K_x(s) ds with K_x(s)=x e^{-s/x}-(x-s)_+, positive for s>0, has strictly monotone-likelihood ratio in x due decreasing Q(v)=v h_prime/h with h(v)=e^{-v}-(1-v)_+ (downward jump at v=1). This prevents two zeros and fixes positive-to-negative crossing, while Taylor small-x and integrated saturation large-x establish existence. For b→infinity, at x=xi(log b/b²)^{1/3}, the 1/(1+bu) exponential integral gives normalized Δ→-xi²/4+1/(6xi) uniformly on compact xi>0; the unique zero then gives xi*=(2/3)^{1/3}. At every fixed x>0, Δ/b→.5[x/(1+x)-(1-e^{-x})]<0. Independently integrated Δ numerically for b=1,10,1000 at x=.001,.01,.1,1,10, corroborating one sign reversal without pretending to prove it.

## originality

PASS

Qualified PASS. Farago arXiv:2605.28445 explicitly studies this harmonic Gaussian KL benchmark and periodic/Poisson reset rates in a singular-reset-width approximation. This exact finite b single-crossing and logarithmic near-zero-width frontier are not stated in the inspected primary sections, but earlier abstract variation-diminishing/convex ordering results could provide part of the proof. Other physical-work resetting papers use different observables and cannot be treated as this result.

## value

PASS

The comparison of fixed and exponential renewal clocks at equal mean duration is a natural resetting benchmark; the sign of their endpoint KL reward-rate difference is not obvious due one-inflection response. A unique threshold at each finite reset variance and an explicit (log b/b²)^{1/3} boundary quantify a noncommuting zero-width/high-rate limit, useful for rigorous modeling of reset-clock design. Does not claim full thermodynamic work or entropy production.

The dated certificate retains the supplied scientific assessment, sources and limitations.
