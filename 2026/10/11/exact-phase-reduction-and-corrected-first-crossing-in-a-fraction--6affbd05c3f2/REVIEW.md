# Independent mathematical audit

## correctness

PASS

Directly differentiated the printed nonlinear two-species delayed field at (2/3,1/3): B=[[k-2/3,-2/3],[2/3,-1/3]]. Multiplying det(s^q I−e^(−sτ)B)=0 by e^(2sτ) gives z²+(1−k)z+(2−k)/3=0 for z=s^q e^(sτ); its discriminant is (3k−5)(k+1)/3<0. Upper-root argument θ=π−atan(sqrt((5−3k)(k+1)/3)/(1−k)); modulus fixes ω=((2−k)/3)^(10/19). Since θ∈(qπ/2,π), first positive phase is (θ−qπ/2)/ω, earlier than the conjugate branch (2π−θ−qπ/2)/ω; later solutions add 2π/ω. Independent Python complex determinant gave ω=0.908501523595597, τ=1.1477399921500826 and residual 2.25e−16, with positive transversality speed 0.3940683275792385. These are spectral, not a nonlinear Hopf theorem.

## originality

PASS

Best-of-knowledge source-specific correction rather than discovery of generic delay spectral theory. The motivating full primary paper states the same characteristic equation but lists an incompatible first delay. Earlier fractional feedback-model papers have different dimensions/characteristics, and no other checked work corrects this exact example.

## value

PASS

The exact common-delay quadratic replaces numerically delicate coupled phase equations and corrects a prominent source-specific feedback bifurcation benchmark by about 0.125, reconciling the source’s stable and oscillatory examples. Whole gain interval and crossing ladders provide reusable structure; not merely rounding of a printed number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
