# Independent mathematical audit

## correctness

PASS

Split the latent Poisson population into independent Poisson counts for detection subsets. A joint cumulant on distinct visits is the total rate of subsets containing those visits; singleton cumulants also include false detections. Thus mu_i=lambda*p_i+phi_i, C_ij=lambda*p_i*p_j and T=lambda*p_1*p_2*p_3. The third joint cumulant is the centered cross-moment, not the raw product moment. Dividing gives p_i=T/C_jk and lambda=C_12*C_13*C_23/T^2; subtracting lambda*p_i gives phi_i. The strict inequalities give precisely the positive interior detection and abundance parameters, and the three weak inequalities give precisely phi_i>=0, including zero false counts. Substitution in the Poisson construction realizes every feasible seven-tuple. For the two-visit pair the exact singleton-only and shared Poisson rates are (7/10,5/4,1/2) under both parameter sets, hence the whole joint law coincides. For every finite visit count, s>1 with s*max p_i<1 preserves all means and off-diagonal covariances under the stated scaling; the marginal variances equal the means, so all moments through order two agree. The analytic argument, not the 3456 finite checks recorded in the certificate, proves the full claim.

## originality

PASS

Credit the classical Poisson subset decomposition and uncontaminated N-mixture moment analysis. The supported distinction is the parameter and moment-image characterization with unknown visit-specific Poisson backgrounds and fixed independent Bernoulli detection, including the sharp visit and moment-order obstructions. No available source statement compared establishes that combination.

## value

PASS

The extra Poisson singleton sources create a real latent abundance/background ambiguity. The exact feasible region gives a population-level check of the model and the sharp contrast tells investigators both why adding a third survey works and why collecting only pair summaries of many surveys cannot help. This is a natural complete identification result, not a claim of improved fitting or statistical power.

The dated certificate retains the supplied scientific assessment, sources and limitations.
