# Independent mathematical audit

## correctness

PASS

The Cayley update is a Euclidean rotation with unwrapped angle θ(s)=2 arctan(s/2); its products preserve energy and add angles. For iid draws the one-step centered angle is θ′(h)δU+O(δ²) uniformly, with θ′(h)→1. For a complementary block it is θ″(h)δ²(U²−1/3)+O(hδ⁴), since the odd terms cancel, the fourth derivative vanishes at zero and δ=o(h). With θ″(h)∼−h/2 and Var(U²)=4/45, the one-block variance is asymptotic to h²δ⁴/45. Multiplying by T/h and T/(2h) respectively gives the stated positive constants and powers. For a block angle W, 1−|E exp(iW)|²=E[1−cos(W−W′)]∼Var(W) by uniformly vanishing width. Block independence and K Var(W)→0 then give endpoint dispersion ∼K Var(W) and the ratio κ²h⁷/30 at α=5/2. For arbitrary two-step couplings, the variance changes only through E[f(U)f(V)] for f(u)=θ(h+δu), with f′>0. Its survival-integral representation is minimized by saturating the lower Fréchet bound; continuity and strict positivity of the weights force equality of all survival probabilities, hence V=−U. This is for positive nondegenerate widths and unwrapped phase. The nominal time is fixed by the number of steps, not by synchronizing the iid physical clock.

## originality

PASS

Credit is limited to the sharp matched-marginal phase and actual endpoint-dispersion laws for harmonic midpoint, particularly the positive curvature residual and its constant. Exact energy preservation, use of the nominal grid and countermonotone optimality for a monotone transformed sum are established principles. The iid upper rate in part of the parameter range is already a consequence of prior work; it is not credited as new.

## value

PASS

This benchmark quantifies what matched positive step-length marginals and unchanged update counts do not determine: the actual dispersion of an energy-preserving integrator. Removing the leading random-clock component leaves a positive, sharply quantified midpoint-curvature residual, which is useful for distinguishing timing variation from integrator variation. The seven-power comparison is at a nominal time and does not establish a seven-power improvement over an iid procedure already synchronized to the same physical time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
