# Independent mathematical audit

## correctness

PASS

The Euclidean orthotope displacement density is (1/V) prod_i (1-|z_i|/a_i)_+. Integrating expanded factors over a radius-r ball for 0<=r<=min a_i gives the exact Gamma-normalized polynomial. c0 fixes V; c1..c_{d-1} fix elementary reciprocal-length symmetric functions and e_d=1/V, so recover all side lengths. Perturb e_{d-1} with simple positive roots while fixing earlier coefficients proves sharp generic d-coefficient prefix. For r=a+h, disjoint coordinate caps and beta integral show the first correction coefficient t*8*kappa_{d-1}*(2a)^((d-1)/2)/(V*a*(d+1)*(d+3)), exponent (d+3)/2; all d>=3. Independent verification: Independently derived the ball monomial integration constants and d=3 cap coefficient for orthotope (1,2,3): pi/9 h^3. Inspected verify.py including its slicing quadrature, coefficient inversion and near-threshold comparisons, without relying on its advertised exit status. Analytic integration supplies the universal result.

## originality

PASS

Best-of-knowledge: inspected accessible closely related primary PDFs, searched published mathematical records for aliases/stronger results, and compared implications. Generic covariogram formula explains the starting density integral but does not supply the explicit sharp d-jet inverse recoverability and first singular-cap multiplicity when specialized to d>=3 orthotopes. Residual priority limitations are explicit.

## value

PASS

Exact local small-distance jets of random uniform pairs recover any orthotope side lengths up to ordering, with a sharp generic d-coefficient cutoff, and the first cap singularity locates and counts shortest sides. The inverse geometric statistic and breakpoint law are natural, not arbitrary truncations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
