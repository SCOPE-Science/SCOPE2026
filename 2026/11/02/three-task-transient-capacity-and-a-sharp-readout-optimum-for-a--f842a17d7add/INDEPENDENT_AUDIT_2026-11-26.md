# Independent mathematical audit

## correctness

PASS

Summing the four rates gives forward and reverse rates 2k cosh(θ±fx/2), so the centered output is an input-independent bias δ exp(−a cosh θ) plus an odd input response x tanh θ tanh(f/2)[1−exp(−a cosh θ)]/2. The best signed worst-input margin for the bias-matched constant is at 0 and equals C, and the opposite constant cannot have positive margin. For copying, the response term increases on [0,b] while the absolute bias decreases; inversion is its reflection. Both therefore have best margin B attained at opposite endpoints. This proves the count, including equality at positive margin, zero bias, and impossibility of four. With d=|δ|, z=exp(−a), maximizing min(dz,H(1−z^c)/2−dz^c) at fixed z either balances the strict increasing and decreasing terms or uses d=1/2 if their crossing is outside the interval. The balanced branch strictly decreases as z increases (numerator decreases and denominator increases); the other branch z/2 strictly increases. Their unique meeting is z+(1+H)z^c=H. At that point the maximizing d is 1/2, giving exactly two preparations and a unique finite positive time. The root bounds 0<H−z≤(1+H)H^c give z/H→1 and the stated power and logarithmic expansions for fixed b>0. A separate scalar root computation gave (z,T,γ)=(0.2206514320678,0.3350337566916,0.1103257160339) for k=b=f=1, agreeing with the example.

## originality

PASS

The dynamics, uniform-preparation output, and uniform finite-time copy/invert margin are exact prior coverage. The distinct finding is the arbitrary common preparation dependence of attainable tasks and the joint preparation-time optimum and weak-driving law. The inspected stronger-looking transient bound explicitly fixes uniform preparation, and the broader stationary theory cannot retain the preparation variable.

## value

PASS

This is the finite-time initialization question for a previously studied benchmark. It distinguishes a genuine change in attainable task set from a change in margin alone, shows why a maximally biased preparation is globally best despite its penalty for input-dependent tasks, and gives the uniquely timed design and its fixed-control weak-drive scaling. These conclusions are useful within the specified ensemble-mean classifier even without an experimental or wider-network claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
