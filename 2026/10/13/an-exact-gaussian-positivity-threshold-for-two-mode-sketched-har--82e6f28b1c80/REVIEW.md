# Independent mathematical audit

## correctness

PASS

Orthonormal eigenvectors turn restrictions SU and SV into independent isotropic s-Gaussians. Numerator ||SAb||^2>0 simultaneously for all nonzero b almost surely (full rank on 2-plane). The denominator is b^T H b for H with diagonals mu||U||^2 and L||V||^2 and off-diagonal (mu+L)U·V/2 divided by s. Sylvester gives H>0 iff cosine²(U,V)<4kappa/(kappa+1)^2; H indefinite otherwise except measure-zero equality. Gaussian spherical cosine² has Beta(1/2,(s-1)/2), giving the probability. Its monotonicity and CLT yield sharp uniform row budget: at s/kappa=t, probability tends to 2Phi(2sqrt t)-1; the strict inverse threshold follows by sandwich. For fixed s, beta density at zero gives the stated Gamma prefactor kappa^{-1/2}. Independently checked low-row exact beta expressions at kappa=2,10,100 and Sylvester algebra; no false implication from a fixed b to a uniform b.

## originality

PASS

The sketched harmonic Petrov–Galerkin construction and a right-half-plane requirement are from Güttel–Liu–Nyman 2026. Existing ordinary Ritz reorthogonalization and fixed-direction Gaussian-product facts do not identify this joint one-sketch/all-vectors success event. Classical Sylvester and Gaussian beta facts are acknowledged, not novel individually. Full primary sketch-and-restart article inaccessible in this run; best-of-knowledge comparison has explicit high relevance risk.

## value

PASS

This is an exact, motivated stability precondition for a sketched harmonic extraction algorithm: protecting an entire two-mode invariant plane using one shared random sketch has a sharp linear-in-condition-number row cost, unlike condition-independent informal guarantees. Precise probability and confidence constant are useful design facts, without pretending to prove the full restarted algorithm converges.

The dated certificate retains the supplied scientific assessment, sources and limitations.
