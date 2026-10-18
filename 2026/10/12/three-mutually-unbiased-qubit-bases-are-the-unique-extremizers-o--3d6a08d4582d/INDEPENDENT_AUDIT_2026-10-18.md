# Independent mathematical audit

## correctness

PASS

Let g(x)=h((1+x)/2), H(s)=g(sqrt(s)). The analytic derivative H(s)=−(sqrt(s)/(1−s)−artanh(sqrt(s)))/(4s^{3/2})<0 proves strict concavity on 0<s<1. For orthonormal axes squares s1+s2+s3=1, Jensen gives maximum H(1/3)=beta*, and concavity at simplex vertices gives minimum 2ln2/3. For arbitrary axes, test r=n_i to bound Bmin, equality forces all axes orthogonal. For Bmax singular 3x3 axis matrix A admits r in ker A giving ln2>beta*. For invertible A, trace(C)=3, C=AA^T; averaging over sign epsilon gives average ||A^{-1}epsilon/sqrt3||²=tr(C^{-1})/3≥1, strict unless C=I. A norm>1 witness yields a normalized r with all |n_j·r|<1/sqrt3, so Bmax>beta*. Independent symbolic Hessian sign checks and a nonorthogonal exact frame test corroborate strictness; proof is analytic for every triple.

## originality

PASS

Puchała et al. explicitly pose the global MUB extremality as Conjecture 1, know the MUB endpoint values, and discuss N=2 L=3 numerically; that does not imply global comparison with all other projective triples or rigid uniqueness. Related symmetric-POVM endpoint bounds treat fixed POVMs, not arbitrary triple optimization. Resultary qubit minimax results concern different measurement tasks.

## value

PASS

The precise first nontrivial dimension and three complementary measurements are central to entropic certainty theory. Both global extremal directions and exact uniqueness settle a named conjectural special case, not merely re-evaluate the known MUB points.

The dated certificate retains the supplied scientific assessment, sources and limitations.
