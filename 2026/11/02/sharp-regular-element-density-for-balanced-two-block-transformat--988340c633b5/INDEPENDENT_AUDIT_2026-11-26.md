# Independent mathematical audit

## correctness

PASS

For the repaired claim, each block character has m^(2m) maps. Every bijective character permits a block-respecting inner inverse, whereas a collapsed character permits one precisely when the two restriction images are comparable: the whole target block must be taken to a common source block that provides all preimages. Inclusion–exclusion gives R_m=1/2+a_m-b_m/2 for inclusion and equal-image probabilities. Stirling counts by containing image size give the exact supporting count. The inclusion occupancy weights have EGF H(z,w)=1+(e^z-1)e^w. Requiring both tilted means to equal one yields y=x/(1-e^(-x)) and e^(-y)=1+(x-1)e^x, with opposite monotonicities on (0,1) giving uniqueness. The covariance entries x,y,y-1 follow from the first and factorial second moments, and (0,0),(1,0),(1,1) give both positive definiteness and the full difference lattice. The centered characteristic function has uniformly subunit modulus away from zero on the torus; the local Gaussian integral gives mass (1+o(1))/(2*pi*m*sqrt(D)) at the joint mean. Stirling cancels 2*pi*m exactly, leaving C=1/sqrt(D). The saddle minimizes the strictly convex log generating function in log coordinates minus the two coordinates, so rho<=H(1,1)/e²<1. The equal-image proportion conditional on inclusion is bounded by (1-p)^m divided by the local mass at the joint mean, where p>0 is the tilted probability of occupying a cell only in the first map. It is therefore negligible. Independently enumerated m<=3 gave 4/4,60/64,2400/2916. The newly written bounded check under repairs/3 reproduces C=1.2107009912852933 and rho=0.6967429565725238 and the correction ratios 1.00209145 and 1.00104079 at m=40 and 80, and returned VERIFY_OK. The frozen verifier was inspected, not run; it prints twice the density prefactor as C but uses half of that label in its comparison. The replacement reports the correct C and avoids floating subtraction from one half. Finite checks do not replace the asymptotic argument.

## originality

PASS

The frozen scope does not pass originality for its separately assessed exact enumeration: a distinct indexed result supplies a strictly stronger rank enumerator whose value at one is identically the exact count. The catalogue dates do not settle priority or remove mathematical overlap. The complete repair narrows the contribution to the sharp exponential correction including its prefactor, retaining the exact count as credited background. The compared rank record gives qualitative exponential convergence and an upper bound but not this sharp asymptotic; the other inspected structure and enumeration sources do not supply it. The revised distinct claim passes on the available evidence, without priority certification.

## value

PASS

The repaired asymptotic supplies an explicit rate and prefactor for the rare contribution of the collapsed block characters in a canonical nontrivial partition monoid. It goes beyond the structural criterion, exact finite count and known loose exponential bound by resolving how small the excess fraction is and identifying the underlying occupancy mechanism. The precision is intrinsically meaningful for this probability, rather than a numerical recomputation of a known table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
