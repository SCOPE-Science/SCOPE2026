# Independent mathematical audit

## correctness

PASS

The printed stochastic equations have drifts A(y,z)x, B(x,z)y, C(x,y)z and common multiplicative sigma x/y/z dW. Each coordinate axis is invariant by pathwise uniqueness, and restriction is geometric Brownian motion dX=a_i X dt+sigma X dW. For every p>0, exact p-moment exponent p a_i +[p(p-1)/2]sigma² makes a_i+(p-1)sigma²/2<0 necessary for p-th-moment exponential stability for all small axis states. For printed Parameter Set 1, a_x=0.2*10*0.1+2-5=-2.8 and Eq16–18 restricted to x-axis are -2.8x<=-x, 0<=0, 0<=0. With sigma=3, E[x_t²]=x0² exp(3.4t) while almost-sure log exponent -7.3, disproving a noise-independent criterion on that invariant boundary. Independently computed exact rational coefficients a_x=-14/5, a_y=-9/5, a_z=-1/2 and second-moment exponent 17/5. A qualification is that pointwise source inequalities tested on x-axis are NOT a proof they hold throughout a 3D neighborhood; counterexample precisely addresses source no-noise drift test on invariant axis, not a global verification of an alternate neighborhood-uniform premise.

## originality

PASS

Geometric Brownian p-moments and the general principle that stochastic stability must account for noise are standard prior art, not claimed as novel. The genuine contribution is the direct exact invariant-axis reduction and specific violation of Wen–Mo equations (16)–(18) at the paper’s own Parameter Set 1. The source PDF was compared against its own printed stochastic model and noise-free criterion; related noise-aware Wang 2024 finance and Wang 2025 carbon-supply models do not give this specific correction.

## value

PASS

The counterexample is specific to a published applied stochastic evolutionary-game theorem and changes what its noise-blind criteria can guarantee. It establishes an exact variance-sensitive obstruction while cleanly separating almost-sure sample-path decay from exploding second moments; substantive for mathematical interpretation of market-noise stability, not a generic textbook example alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
