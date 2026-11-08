# Independent mathematical audit

## correctness

PASS

For t<1, a generic hyperplane-section vertex is precisely a crossed simplex edge. Gaussian/Haar two-ray angles split into n distinguished edges and n(n-1)/2 others, yielding exact arccosine F_n(t). The derivative sign algebra reduces to (n-2)(n+1)(2t+nt²), zero for n=2 and strictly negative for n>=3, with stated centroid curvature. A Gaussian normal gives exact sign-count V=K_m(m-K_m); for t=1 the apex replaces collapsing incident edges and iid Gaussian rank is uniform, giving V=1+K(n-K). For fixed t>0, empirical CDF convergence yields V/m²=>Phi(tZ)(1-Phi(tZ)); at t=c/sqrt m, an empirical-CDF stochastic-equicontinuity expansion and a joint independent CLT produce Gaussian sign imbalance with variance 1/4-1/(2pi)+c²/(2pi), hence the squared-normal deficit. Independent arithmetic checks reconstructed F_n and derivatives for n=2..24; the actual verify.py includes finite simulations and rank checks, which do not prove infinite limits.

## originality

PASS

Known Resultary central expected vertex count, central chi-square limit and joint central face-vector law are appropriately credited. They are all centered t=0 results; they do not entail axial strict monotonicity, noncentral finite means, the t=1 jump, or the dimension-dependent displacement crossover. Prior random projection and deterministic section volume papers study different random variables/models.

## value

PASS

Moving the section through the centroid-to-vertex axis is the natural first noncentral deformation of a standard random polytope section. The exact finite mean, sharp geometric endpoint discontinuity, and two-scale fluctuation crossover answer structural probabilistic questions, not numerical sampling or a mere renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
