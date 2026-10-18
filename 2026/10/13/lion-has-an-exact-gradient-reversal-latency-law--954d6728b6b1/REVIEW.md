# Independent mathematical audit

## correctness

PASS

The β2 momentum recurrence with constant new gradient is affine geometric: m_{n−1}=G[(1+r)β2^(n−1)−r]; substitution in the β1 pre-sign interpolation yields c_n exactly. Because β2∈(0,1), c_n>0 iff β2^(n−1)>r/[β1(1+r)], giving the strict ceiling count and immediate threshold r=β1/(1−β1), with equality c1=0. Applying the same count to m proves N+≤Nm. Independent direct step-by-step recurrence replay with defaults yielded N+=59, Nm=69 and threshold 9, and inspected the actual source verify.py (including an exact-power boundary test). No claim is made for feedback gradients determined by an objective, weight decay, or noisy signals.

## originality

PASS

The original Lion algorithm necessarily defines the two-coefficient recurrence, and solving a scalar EMA is elementary; this priority is fully credited. But the exact gradient-reversal response, dual sign-clock latency, default 59/69 counts and 9-fold strict threshold were not observed in the original algorithm paper, Lyapunov follow-up, or targeted published records. It is an explicit motivated diagnostic consequence rather than an invention of the Lion recurrence.

## value

PASS

Lion’s two distinct momentum coefficients have a concrete, potentially surprising operational implication: after an externally forced equal-amplitude sign reversal, the default update keeps the old sign for 59 iterations and its underlying moment keeps that sign for 69. The exact ninefold immediate-flip threshold and analytic log-ceiling phase boundary are a motivated precision diagnostic for optimizer memory, offering a reproducible test to distinguish two time scales. It is a narrow but natural quantitative boundary, not a generic convergence claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
