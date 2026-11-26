# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md lines 46–116. Each residual has just one nonzero column, so its squared spectral (and Frobenius) loss is the squared orthogonal rejection D/u or D/v. On span(a,b), aaᵀ−bbᵀ has trace u−v and determinant −D, yielding exactly the stated opposite-sign eigenvalues. Rotating each independent Gaussian row to these eigenvectors makes the sketch norm difference (λ₊X+λ₋Y)/s for independent χ²_s variables; X/(X+Y) is Beta(s/2,s/2). The comparison event is the lower tail at q=−λ₋/(λ₊−λ₋). The beta variable has a density, so there are no ties for any full-rank input, including u=v; the scope's wording about a possible special equal-norm degeneracy is unnecessary and there is no such exception under the hypotheses. The equal-original-norm losses indeed coincide. For s≥2 a symmetric beta density is nondecreasing up to 1/2 and has average density one there, giving I_q≤q≤v/(u+v); inserting this in the exact risk gives 2D/(u+v). At s=2 the beta law is uniform (and unequal orthogonal columns give equality in the finite-Gram bound); balanced columns attain the finite-Gram bound for any s and give the global sharp limit 2, not attained at finite σ₁/σ₂. Jensen gives the first-moment bound. For s=1 diagonal inputs have exact Cauchy-tail mispivot probability (2/π)arctan(1/κ), so normalized squared risk grows as 2κ/π. An independent nonorthogonal exact replay is Gram data (u,v,τ)=(4,1,3/2): X,Y are exponential for s=2, the mispivot is X<Y/7, p=1/8 by direct integration, and risk=77/128≤7/10. Inspected VERIFICATION.md and check_pivot.py; the supplied script was not executed and its reported 21,092 finite checks are not a proof of the uniform bound. Scope is the first maximum-sketch-norm decision on two fixed real independent columns, with Gaussian sketch and mean-square loss in the original space.

## originality

PASS

The Gaussian quadratic-form and beta-ratio identities are standard, and the norm-proportional baseline and some sketched pivot probabilities have exact prior or catalogue coverage. The supported distinct claim is the arbitrary-Gram, unconditional mean-square comparison for the max-norm decision and its sharp one-versus-two-row guarantee; the evidence does not establish publication priority.

## value

PASS

The rule and loss are natural in sketched column selection: one extra sketch row changes mean-square projection loss from unbounded in condition number to a sharp dimension-free bound. The exact probability works for correlated sketches of the two columns, and the risk comparison to norm-proportional selection is stronger than reporting just the limiting factor two. The threshold is not a claim about later pivots, mean angle or high-probability error.

The dated certificate retains the supplied scientific assessment, sources and limitations.
