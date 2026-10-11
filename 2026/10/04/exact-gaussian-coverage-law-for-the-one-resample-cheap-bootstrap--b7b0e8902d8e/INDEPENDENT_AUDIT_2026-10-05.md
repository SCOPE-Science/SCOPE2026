# Independent mathematical audit

## correctness

PASS

Conditioned on bootstrap counts \(N_i\), the sample-mean error and bootstrap displacement are orthogonal Gaussian linear forms because the displacement coefficients \(N_i-1\) sum to zero. The conditional variance ratio is \(Q_n=n^{-1}\sum_i(N_i-1)^2=2C_n/n\), where \(C_n=\sum_i\binom{N_i}{2}\). The ratio of the independent standardized normals is Cauchy, yielding the exact conditional arctangent coverage and hence the occupancy mixture. Strict concavity gives finite-n undercoverage. In this audit, direct labeled resampling for n=2,3,4 independently reproduced the collision laws and the n=2 coverage 0.475; the inspected verifier independently checks the stated collision moments through n=30. The Taylor calculation from the exact first two moments gives the displayed \(1/n\) coefficient.

## originality

PASS

Lam's complete primary text defines the exact B=1 interval and proves asymptotic exactness for every fixed positive resample count. Its higher-order section states a two-sided \(O(n^{-1})\) coverage error whose coefficient is a high-dimensional integral that is not available in closed form. The audited Gaussian calculation instead gives an exact all-n occupancy mixture, strict sign of the finite-sample error, and a closed-form first-order coefficient. Resultary and targeted literature searches found no equivalent Gaussian one-resample identity.

## value

PASS

The one-resample regime is the defining extreme-computation case of Cheap Bootstrap. An exact finite-sample calibration law showing systematic undercoverage even in the Gaussian mean benchmark, together with the closed first-order deficit, is a motivated statistical design fact with direct practical interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
