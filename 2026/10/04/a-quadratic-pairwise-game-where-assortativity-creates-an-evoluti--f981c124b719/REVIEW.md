# Same-model scientific review

## Correctness
PASS.  The invasion-fitness definition is differentiated directly.  For the stated quadratic payoff the selection gradient is exactly \(D_r(x)=(-2+3r)(x-\tfrac12)\), so \(x^\star=\tfrac12\) is convergence stable for \(r<\tfrac23\).  At that resident, the invasion fitness is exactly \(\varphi_{1/2}^r(y)=\tfrac{2r-1}{2}(y-\tfrac12)^2\), making the same singular strategy an ESS below \(r=\tfrac12\) and a branching point for \(\tfrac12<r<\tfrac23\).  Symbolic replay agrees with every displayed identity.

## Originality
PASS with residual literature risk.  The closest primary source, Iyer and Killingback (2020), contains the generic assortment formula, proves inhibition for selected continuous social dilemmas, and then states the broader conjecture; it does not cover arbitrary smooth pairwise payoffs.  Coder Gylling and Brännström (2018) establish reduced branching under an additive public-goods structure that excludes the witness.  Leeks et al. (2019) observe branching with transmission/relatedness feedback but do not isolate increasing relatedness as the cause.  Jensen and Rigos (2018) treat finite pure-strategy matching rather than continuous adaptive-dynamics branching.  Targeted semantic searches using the conjecture wording, the generic invasion formula, derivative terminology, exact thresholds, and counterexample language found no equivalent or stronger statement.  Search failure is not a proof of novelty, so an equivalent result under different terminology remains a residual risk.

## Value
PASS.  A broad published conjecture is separated from the special payoff structures that supported it.  The exact identity \(B_r-C_r=(r-1)\pi_{12}\) identifies the mixed payoff curvature as the obstruction to any sign conclusion based on assortment alone, and the quadratic witness realizes a clean ESS-to-branching transition while convergence stability persists.

## Closest literature and limitations
The result does not challenge the specific snowdrift, tragedy-of-the-commons, or additive public-goods theorems in the cited literature.  The witness is not asserted to be a biologically calibrated social dilemma, and the conclusion is local in the standard adaptive-dynamics sense.  Post-branching dynamics, stochastic finite populations, large mutations, and endogenous assortment are outside scope.

Same-model review: passed. Independent audit: not yet performed.
