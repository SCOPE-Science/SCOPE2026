# Independent mathematical audit

## correctness

PASS

PASS. For |z|=1 and s>0, u=z^n and v=epsilon z^-k are unit complex numbers with u+v=-delta s real nonzero, which forces v=conjugate(u), hence z^(n-k)=epsilon. Enumerating all roots of this equation gives the finite wall list sigma_j=-2delta cos((2pi j+n0 chi)/L) for L=(n-k)/gcd(n,k), n0=n/g, chi=0 or pi according to epsilon; keep positive levels, with conjugate-pair multiplicities. At every unit zero the real Jacobian |n z^(n-1)|^2-|k epsilon conjugate(z)^(k-1)|^2=n^2-k^2>0, so there is a unique local real-analytic root branch. Let w=z'/z and u=z^n,v=epsilon z^-k; implicit differentiation gives w=-delta v/(n+k) and w'=[nk-(n^2+nk+k^2)v^2]/(n+k)^3. Real parts give the claimed first and second logarithmic radial derivatives because Re(v)=-delta s/2 and Re(v^2)=s^2/2-1. Independently checked these real-linear equations exactly at four root/parameter examples, including (n,k)=(9,1) walls s=sqrt2 and s=2 with second derivatives 9/1000 and -41/500. All roots cross outward because positive velocity; away from walls no boundary roots, so homotopy invariance and zero winding at sufficiently large s give signed index g sum_j 1_{sigma_j>s}. Exact wall multiplicities at s=2 and strictly intermediate walls were checked. No unsigned total zero count, global branch continuation or nonreal coefficient deformation is claimed.

## originality

PASS

PASS, with specific prior-implication risk. Barrera–Barrera–Navarrete, Unimodular Zeros of Selmer's Harmonic Trinomials (arXiv:2610.22132), completely classifies unit roots at the single coefficient s=1, including 2g multiplicity; that fixed-point theorem is prior, not a novel crossing statement. Barrera–Campa–Navarrete (arXiv:2602.11296) gives broad general harmonic-trinomial parameter-space trochoid loci and zero/modulus phenomena, so it may imply the crossing-location or winding portion with computation. Brilleslyper et al. (2020, DOI:10.1090/bproc/51) give an all-parameter zero-count staircase for a different deformation where the anti-analytic coefficient, rather than the real constant, varies. The inspected primary treatments do not state the uniform positive wall derivative and universal second logarithmic radial jet with its curvature-sign switch; these are the narrow originality center. The signed staircase is not independently counted as new if implied by earlier Bohl/root-count theory. Unindexed local root-sensitivity results remain a priority risk.

## value

PASS

PASS. Varying the constant term is a natural one-parameter continuation of the fixed-coefficient harmonic Selmer family. The all-exponent exact local crossing velocity, second-order curvature formula and sharp acceleration sign boundary supply nontrivial stability data at every possible unit-circle wall; the signed winding staircase puts that motion in a complete, delimited phase context. An explicit (9,1) example sees both curvature phases. This precise local jet is motivated even without a new global unsigned zero-count theorem, and is not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
