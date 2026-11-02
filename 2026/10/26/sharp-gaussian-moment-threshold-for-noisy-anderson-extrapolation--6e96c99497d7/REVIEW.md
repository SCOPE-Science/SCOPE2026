# Independent mathematical audit

## correctness

PASS

Independence is exact: xi=mean(epsilon_i) is jointly Gaussian and orthogonal to each column noise difference, so r0=a-R1/(m+1)+xi. Conditioning on R_{-j}, Gaussian regression gives the residual orthogonal column u_j in t=d-m+1 dimensions with nonsingular isotropic Gaussian density, whose inverse radius has finite p moment exactly when p<t by polar integration. The independent xi makes conditional alpha_j normal with variance sigma^2/((m+1)||u_j||^2), giving the matching divergence lower bound even when its mean shifts. For sufficiency, finite Gaussian moments and the u_j inverse bound control alpha. Since Z=H alpha+B, H has full column rank and B=y0-Proj_col(R)r0 has moments of all orders, no tail cancellation is possible. Tikhonov pseudoinverse operator norm <=1/(2sqrt(lambda)), giving all polynomial moments. New independent checks reconstructed Gaussian inverse covariance matrices and least-squares/output decompositions; these tests cannot prove the rare-event integrability.

## originality

PASS

Random rectangular pseudoinverse codimension moments, Anderson least-squares formulas, instability motivation, and ridge conditioning are established prior art. The specific statement for the evaluated extrapolated point with a correlated difference matrix, an independent common Gaussian residual average, and no output cancellation is a sharp new application not located in inspected primary definitions/analyses. Best-of-knowledge PASS; a broad Gaussian regression pseudoinverse theorem might imply parts under alternative wording.

## value

PASS

The one-shot extrapolation output is the actual object used by numerical optimization: its exact loss of moments at near-square memory depth predicts heavy-tailed failures that finite testing and ordinary variance analyses can miss. Distinguishing harmless fixed outer relaxation from tail-healing positive Tikhonov is practically and mathematically motivated; not a mere standard inverse-Gaussian restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
