# Independent mathematical audit

## correctness

PASS

Order the points cyclically; normalized circular angular gaps have Dirichlet(1,...,1) distribution. The exact identities P=2sum sin(G_i/2), A=0.5sum sin G_i give P=2pi-S3/24+S5/1920+O(S7), A=pi-S3/12+S5/240+O(S7). Dirichlet factorial moments yield covariance limit v_kl=(k+l)!-(1+kl)k!l!, specifically v33=360,v35=28800,v55=3254400. The least-squares projection coefficient Cov(S3,S5)/Var(S3)=320pi^2 n^-2+O(n^-3) removes cubic-predictable S5 variation; exact rational arithmetic independently verifies projected constant 2^10/320^2*(3254400-28800^2/360)=9504, perimeter 40 and correlation deficit 9504/(2*160)=297/10. Exponential spacings and the multivariate delta method prove jointly Gaussian limits and orthogonal Gaussian independence. Remainder S7 is L2-small via exact Dirichlet moments. No unsupported inference from finite-n numeric simulations.

## originality

PASS

The 2011 Bélisle source establishes marginal asymptotics for precisely this circle-sampling model, but complete article access was not achieved and is preserved as a historical risk. Xu–Meng–Li (2019) and the full publisher 2021 Wang–Xu–Liu paper present fixed-coefficient extrapolation, including Lemma 2.2 for the linear combination 4/3 semiperimeter−1/3 area; that is already known and excluded. The optimal *population least-squares* slope, mixed cubic/quintic covariance projection and sharp correlation deficit are additional claims not determined by the stated fixed slope. Resultary queries for circle-sampled area/perimeter covariance and regression found no dominating published result.

## value

PASS

For two canonical jointly measured geometric observables, leading correlation tends to one but hides a new finer-scale fluctuation. The exact best linear predictor quantifies how much area uncertainty remains when perimeter is known: residual variance is only 33/113 of the previously studied fixed-slope remainder. The joint independent Gaussian limits and correlation coefficient give a transferable statistical description of random cyclic hulls; this is a nontrivial optimal-projection refinement, not a rebranding of a known fixed combination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
