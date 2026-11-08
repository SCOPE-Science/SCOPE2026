# Independent mathematical audit

## correctness

PASS

For H(s)=[cos(e^-1)-cos(e^{s-1})]/D, with D>0, H'(s)=e^{s-1}sin(e^{s-1})/D>0 and H''(s)>0 on [0,1]. Left roots solve the strictly convex Q=H(s)+alpha-(alpha+b)s, whose endpoints alpha and 1-b are positive. The unique s_alpha solving A(s)=sH'-H=alpha has A'=sH''>0, A(0)=0 and A(1)=H'(1)-1>1. The tangency b*=H(s)+(1-s)H'(s) gives exactly zero/one double/two left roots depending on b<b*,=,>; right roots solve H(s)+(1-b)s=1, strictly monotone and repelling because q>3/5 and H'(q)>1. Left multiplier identity G'(bs)-1=Q'(s)/b separates stable lower and repelling upper roots; endpoint Taylor bounds H'(1)<2+H'(0) establish the nontrivial lower -1 stability bound. Implicit differentiation gives b*'=(1-s)/s, b*''=-1/(s^3H'')<0; Taylor at alpha=0 gives the sqrt cusp, and ordinary nondegenerate fold gives the sqrt root/multiplier splitting. Independent high-precision alpha=.5 yields b*=0.9178276907017725; numerical tests are supplemental to convexity/interval inequalities.

## originality

PASS

Qualified PASS: The 2023 primary paper introduces exactly the cosine-skewed map and numerically explores the period-one/chaotic parameter regions, but its inspected Eq (4) and Sections 3.2 and 3.6 do not supply the global exact one/two/three fixed point count and sharp attracting region, concavity or alpha->0 sqrt cusp. Ordinary saddle-node theory supplies the local exponent, not this concrete global curve. A 2023 MOCAST conference precursor was inaccessible in full, retained as a priority risk.

## value

PASS

An explicit full two-parameter equilibrium/stability phase diagram and square-root endpoint singularity for a published nonpolynomial interval family supplies mathematical content beyond numerical bifurcation plots and generic local fold theory, including a sharp distinction between repelling-only and exactly-one-attractor regions. The endpoint cusp and concavity give usable boundaries for analyzing this exact nonlinear system.

The dated certificate retains the supplied scientific assessment, sources and limitations.
