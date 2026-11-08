# Independent mathematical audit

## correctness

PASS

For a leaf-first sweep, independent leaf best responses give c' = F(c)=max(0,1-sδ+sδ²c). F is increasing, so c_0=1 gives the sharp worst case for every initial leaf state. With a=1-sδ and b=sδ², the untruncated recurrence y_r=b^r+a(b^r−1)/(b−1), or 1+ra if b=1, crosses zero first at ceil(log Theta/log b) (or ceil(1/(sqrt(s)−1))), and clipping preserves the first crossing. At δ<=1/s the starting hub-one state approaches its positive/interior or boundary equilibrium without attaining it. A final leaf-only sweep reaches (0,1,..,1) when δ>1/s. The one-sweep condition sδ(1−δ)>=1 is possible first at s=4; endpoints yield logarithmic laws. A successful random word of r full leaf-first blocks followed by s leaves has probability (s!)^(r+1)/(s+1)^(r(s+1)+s), proving geometric absorption tail from ANY state. Uniform random permutation places the hub after K uniform leaves K=0..s, yielding the deactivation probability. An independent exact Fraction-based sweep check reproduced the hub cutoff in rational cases for s=2..11 and denominators <=14; finite tests do not prove real-parameter formulas.

## originality

PASS

Published 2014 network-game results already give the star Nash equilibrium, and the 2026 source studies the same stochastic best response and numerical tolerance-based convergence. The assessed result is the exact order-specific first hitting index and endpoint asymptotics, plus a positive-probability all-state absorption-word tail and exact single-permutation hub deactivation probability. These do not follow from the earlier equilibrium existence or tolerance-based experiments, although some pieces are elementary iteration and related order-specific coordinate-descent results could overlap.

## value

PASS

The precise distinction between approaching equilibrium and hitting it exactly is a natural question for continuously-valued public-goods games. A canonical star exhibits a sharp δ=1/s transition, logarithmic first-zero divergence at both ends, a previously unquantified one-sweep degree threshold, and an exact random asynchronous absorption certificate. These separate scheduling protocols and answer a motivated dynamical gap, not a generic recurrence exercise without context.

The dated certificate retains the supplied scientific assessment, sources and limitations.
