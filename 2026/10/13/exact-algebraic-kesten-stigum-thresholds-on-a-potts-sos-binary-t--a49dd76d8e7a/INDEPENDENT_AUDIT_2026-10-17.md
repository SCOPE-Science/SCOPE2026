# Independent mathematical audit

## correctness

PASS

On the specified three-state Potts–SOS Cayley tree branch r=theta², x=1, the printed boundary law reduces to F(theta,y)=y³-theta*y²+2theta*y-2=0 with y>0. The nontrivial eigenvalue quadratic has zero constant term and reduces to {0,rho}, rho=y(theta-y)/(2theta+y²). The binary-tree Kesten–Stigum equality 2rho²=1 gives polynomial K=2y²(theta-y)²-(2theta+y²)². Independent symbolic Sylvester resultant verifies Res_y(F,K)=16P(theta) for the stated octic. The exact rational Sturm argument in RESULT and verifier proves P has precisely two positive roots in disjoint rational intervals; over Q(sqrt2) its two quartic factors distinguish rho=-1/sqrt2 at theta_minus and rho=+1/sqrt2 at theta_plus. Substitution and sign brackets put the large crossing on the middle of three positive cubic branches. Independent numeric root/branch calculation agrees at 0.166699331094 and 9.706301627792; decimal checks do not prove global root count. This is the Kesten–Stigum sufficient non-extremality threshold only, not an exact extremality criterion.

## originality

PASS

Rahmatullaev–Rasulova (2021) provide the same cubic and spectral setup and report two decimal Kesten–Stigum crossing parameters from Maple, but do not supply an exact octic, its two positive-root certification, its splitting over Q(sqrt2), or the assignment of the two crossings to specific positive boundary-law branches. Pure SOS 2015 is a different interaction. The broader 2022 lambda-model paper was only available at abstract level, an explicit priority risk; this access limit alone does not imply failure or prove uniqueness.

## value

PASS

The two Kesten–Stigum thresholds control a natural spectral sufficient non-extremality test and had been provided as computer decimals. Converting them to exactly the two positive roots of one octic, factoring by signs of eigenvalue crossings, and certifying the relevant positive boundary-law branches supplies a reusable rigorous phase-threshold description with algebraic isolation. This is more than adding decimal precision, and no false necessary/sufficient extremality assertion is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
