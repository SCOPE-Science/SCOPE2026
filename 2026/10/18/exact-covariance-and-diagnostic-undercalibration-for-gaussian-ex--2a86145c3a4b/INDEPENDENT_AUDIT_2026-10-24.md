# Independent mathematical audit

## correctness

PASS

For A=lambda I_n and f(0)=0,c=f(lambda)>0 the Nyström matrix is lambda times projection; with 1≤k≤n, Xi=c[(k−1)+Ri] where Ri is squared Gaussian residual in dimension d=n−k+1, giving chi²_d mean d and var2d. Conditional on the other k−2 columns, two independent standard Gaussian vectors in m=d+1 dimensions share angle theta; E(sin⁴ theta)=(m²−1)/(m(m+2)), implying Cov(Ri,Rj)=2d/(d+3). Averaging yields VarH=2c²d(n+3)/(k(d+3)) and ES²=2c²d(d+2)/(k(d+3)), so ratio=(n+3)/(n−k+3); for k=n+1 all leave-one-out spans full R^n and H=nc exactly. Independently rederived beta-angle formulas algebraically and cross-checked 3 dimension pairs with 40,000 fresh Gaussian pair draws each (statistical corroboration only). Special k=1 no diagnostic; k=n leading absolute variance but shrinking relative variance. Universal proof is exact conditional rotational symmetry, not Monte Carlo.

## originality

PASS

The generalized leave-one-out estimator, exchangeability, dispersion diagnostic and correlation identity are established in FlexTrace and XTrace. The claim newly evaluates the actual nonzero off-diagonal covariance and sharp calibration factor for isotropic flat-spectrum unnormalized Gaussian FLEXTRACE, including near full-rank collapse and exact n+1 transition. The primary XTrace article is read, including the general correlation/diagnostic identity; this exact d-dependent angular covariance is not an evaluated theorem there. The March 2026 FlexTrace full text could not be retrieved from OA endpoints or authorized Oxford VPN, making possible unpublished/supplement exact specialization a material priority risk, but the specificity and derivation support best-of-knowledge O.

## value

PASS

Even for the most elementary flat spectrum, correlated leave-one-out terms cause an exact failure of the naive dispersion diagnostic near the rank threshold. The dimension-and-sample-specific correction (n+3)/(n−k+3) and contrast with k=n+1 exactness provide a useful controlled benchmark for trace estimator uncertainty quantification, and explicitly separate absolute from relative risk and prior residual-normalization fixes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
