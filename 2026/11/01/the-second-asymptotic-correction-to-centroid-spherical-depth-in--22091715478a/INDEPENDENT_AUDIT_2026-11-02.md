# Independent mathematical audit

## correctness

PASS

PASS. Similarity-normalized regular d-simplex points have independent Dirichlet(1,...,1) barycentric vectors. Exact geometry gives centroid in the diameter ball iff ΣP_iQ_i<=1/m (m=d+1), equivalently Σ(E_i-mean E)(F_i-mean F)<=0 with independent Exp(1). Conditional on E, standardized coefficients b_i sum zero and sum squares one; exact characteristic function of Σb_i(F_i-1) has log Σ_{j>=2}(it)^j M_j/j. Gaussian Fourier inversion yields 1/2+(2π)^(-1/2)[M3/3-3M5/5+5M3M4/4-35M3^3/54] with integrated remainder O(m^-2) on controlled samples, negligible complement using exponential moments, small-max and empirical concentration. Checked the expansion signs and Gaussian moments directly, not via Monte Carlo. Exact exponential central moments μ2=1, μ3=2, μ4=9, μ5=44, covariance contractions mVar(U2)->8 and mCov(U2,U3)->36, plus E U2=1-1/m,E U3=2-6/m+O(m^-2), give E M3=2m^-1/2-27m^-3/2+o(m^-3/2), E M5=44m^-3/2, E M3 M4=18m^-3/2, E M3^3=8m^-3/2, so coefficient -9-132/5+45/2-140/27=-4883/270. Checked normalization m=d+1; finite 3,000-sign checks and Monte Carlo in verify.py are corroboration ONLY. The analytic good-event and Fourier-tail argument is needed for the asymptotic theorem; no finite-dimensional monotonicity claimed.

## originality

PASS

PASS, best-of-knowledge with significant explicit historical-priority risk. Existing general asymptotic/Edgeworth work on sample correlation for nonnormal variables provides a framework, but the accessible description of Ogasawara (2006) states expansion through m^-1 and does not display the explicitly evaluated m^-3/2 coefficient for the independent exponential-centered covariance sign statistic. The present calculation is a concrete second nonzero simplex-volume coefficient; an exact specialized older evaluation could subsume it but was not verified. The full 2006 primary article was inaccessible after searching preprint/OA and authorized institutional access; the absence of access alone is not a negative originality verdict.

## value

PASS

PASS. The centroid-diameter-ball depth of two independent uniform-volume simplex points is a natural similarity-invariant high-dimensional probability. Its first two nonzero coefficients give a concrete rate and the first signed correction beyond the positive m^-1/2 leading term; the -4883/270 correction is not implied by the leading coefficient. The exact value calibrates the non-Gaussian sample-correlation skewness phenomenon and is useful as a precise benchmark for higher-order asymptotics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
