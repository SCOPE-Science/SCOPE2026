# Independent mathematical audit

## correctness

PASS

For the one-spike Hessian H=diag(kappa,1,...,1), kappa>1, and anisotropic Gaussian g=(sqrt(tau)Z1,Z2,...), q=Hg/||Hg||, the exact inverse-Rayleigh correction M=I-(1-lambda^-1)qq^T has nontrivial preconditioned two-plane eigenvalues with sum kappa+2-lambda and product kappa/lambda (lambda=1+(kappa-1)t). For 0<t<1 these bracket 1, so chi+chi^-1+2=lambda(kappa+2-lambda)^2/kappa. Exact factorization against baseline (kappa+1)^2/kappa yields chi<kappa iff t>t_*(kappa), with t_*=(2kappa+1-sqrt(4kappa+5))/(2(kappa-1)). The independent Gaussian ratio U/(U+Z1^2) is Beta((d-1)/2,1/2), giving exactly I_{T/(1+T)} where T=kappa^2 tau(1-t_*)/t_*. Expanding t_*=1-kappa^-1/2+O(kappa^-1) gives the tau kappa^3/2 frontier. W is maximized at lambda=(kappa+2)/3, t=1/3; chi_max~4kappa^2/27. Distinct unit eigenvalues for d>=3 imply generic exact arithmetic CG minimum polynomial has degree three, versus at most two before. Independently checked 49 (kappa,t) threshold points, all analytic maxima, and four large-k expansions; these checks corroborate, not replace, the analytic proof. Exact endpoints have zero Gaussian measure; no multi-sketch extension claimed.

## originality

PASS

Daužickaitė et al. 2026 actual full 21-page arXiv preprint was inspected, including §§3.1–3.2: spectral limited-memory preconditioner Eq.(7) and randomized Hessian sketch/covariance discussion. The paper does not state an exact probability of improvement for this one-vector one-spike inverse-Rayleigh model or a beta-CDF threshold; its models and formulas motivate but do not logically imply the distribution without a separate spectral reduction and stochastic integration. Earlier 2021 spectral-LMP work and 2006 approximate-eigenpair sensitivity concern construction and perturbative conditioning, not the exact nonperturbative frontier. Resultary returned unrelated spectral-filter residual distortion and stale-basis conditioning, no equivalent beta law. Novelty of the exact sharp minimal model survives, while a hidden specialized two-eigenvalue perturbation corollary remains possible.

## value

PASS

The risk of worsened conditioning despite a Ritz correction is an important mathematical boundary for randomized preconditioning. The exact Gaussian improvement probability, critical anisotropy scaling tau~kappa^-3/2, worst-case quadratic damage and three-eigenvalue CG change provide motivated quantitative diagnostics for a natural minimal model. This does not claim performance of arbitrary ensemble or Nyström algorithms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
