# Independent mathematical audit

## correctness

PASS

For a,b>0, direct independent symbolic differentiation of Psi=(-x²+y²+z²)/(2a)-z/(ab) along F=(y-bx,yz-x,a-y²) gives L_F Psi=z-1/b+(y-bx)²/(ab); ordinary divergence is z-b, so div_{e^-Psi} F=1/b-b-(y-bx)²/(ab). Weighted Jacobian transport thus yields nonexpansion at b=1 and exponential rate b-1/b for b>1 along any existing local flow segment. At E_±=(±sqrt(a)/b,±sqrt(a),1/b) the square vanishes and rate is attained; for b<1 weighted divergence is positive there. For every compactly supported invariant probability, integral L_F Psi=0; equality in integrated defect forces y-bx=0 on almost every full orbit via invariance, then x,y constant and z=1/b, except the x=y=0 orbit z(t)=z(0)+at which cannot stay compact; hence precisely mixtures of E_±. Oseledets + Liouville on compact ergodic supports identify the Lyapunov sum. Euclidean Jacobian carries an endpoint Psi coboundary and is not claimed to contract pointwise outside compact sets. SymPy algebraic premises independently checked, and analytic flow/invariant-measure arguments reconstructed beyond script output.

## originality

PASS

Best-of-knowledge PASS: exact quadratic weighted cohomology, global sharp b=1 sign frontier and equality classification for every compact invariant probability go beyond published numerical Lyapunov plots and divergence z-b. Similar Nosé–Hoover coboundaries for a different field do not imply this system without conjugacy.

## value

PASS

This identifies an explicit globally positive integrating weight, a sharp physically meaningful damping threshold across all phase points, and a classification of stationary measures saturating the Lyapunov-sum bound. It improves qualitative/numerical chaos evidence into rigorous invariant constraints without presuming attractor existence, a substantive dynamical statement rather than mere divergence sign arithmetic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
