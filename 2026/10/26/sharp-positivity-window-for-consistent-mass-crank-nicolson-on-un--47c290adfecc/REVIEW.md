# Independent mathematical audit

## correctness

PASS

For every n>=3 and z=tau/h²>=0, assembled consistent P1 finite-element M=h(4I+T)/6, K=(2I-T)/h, so the dimensionless update P=(aI+(1-3z)T)^{-1}((4-6z)I+(1+3z)T), a=4+6z. At 0<z<1/3 alternating similarity of the Stieltjes inverse makes every distance-two entry negative; z=0 gives I, z=1/3 gives (I+T)/3. For z>1/3, b=3z-1, A=aI-bT is Stieltjes and P=(-1-2/b)I+(36z/b)A^{-1}: all offdiagonals positive and the Green formula shows end diagonals are least. Their continuants D_0=1,D_1=a,D_j=aD_{j-1}-b²D_{j-2} yield the unique endpoint root rho_n>1/3: 36zD_{n-1}=(3z+1)D_n. Sine-eigenbasis monotonicity gives uniqueness; Schur complements show rho_n strictly increasing; the half-line Green limit selects rho∞ as root 0.747597827128115 of 27z³−207z²+141z−1. Independent exact-fraction inversion for n=3..8 across the lower/upper boundaries reproduces all signs and P3(7/10) positive; the analytic Green proof, not that sampling, covers all n.

## originality

PASS

Faragó–Horváth 2006 gives general finite-element discrete maximum principle time-step conditions (including 1/3-to-2/3 under broader forcing/boundary quantification), and Li–Huang gives sufficient anisotropic mesh bounds. Neither inspected statement fixes the sharp zero-boundary unforced *interior map* nonnegativity threshold rho_n, as the exact n=3,z=7/10 positive example shows. Separate Resultary CN Markov and filtered results use different operators. Earlier 2001 proceedings and inaccessible complete SIAM paper remain priority risks.

## value

PASS

A sharp mesh-dependent positivity window for the standard consistent-mass Crank–Nicolson discretization is directly useful for choosing nonoscillatory timesteps and distinguishing interior positivity from a full discrete maximum principle. The discontinuous failure at small positive z and unexpected positive range past 2/3 are meaningful structural boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
