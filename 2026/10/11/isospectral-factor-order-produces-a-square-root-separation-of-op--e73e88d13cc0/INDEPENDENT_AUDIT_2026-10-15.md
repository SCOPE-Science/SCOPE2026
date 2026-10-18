# Independent mathematical audit

## correctness

PASS

For Q C⁴ P-periodic, a,b>0, δ→∞, the first-order inverses G_u and G_b have positive causal kernels with exponential averages a and b. The bilateral homogeneous solutions of both triangular Floquet systems have no nonzero bounded whole-line orbit (multipliers exp(-aP), exp(-bP) strictly less than one), so the unique bounded inverse gives the best Ulam residual-to-solution constant, and the test residual g≡1 saturates it. Carefully checking factor order gives KA=(1/b) max v, v=G_u 1, while KB=max w, w=G_b v. The period formula for v has the normalization 1/(1-exp(-aP)). Laplace expansion of its numerator near the preceding max of Q and the e^{-δQ(t)} Gaussian pulse near Q-min produce pulse height C exp(δΔ)/sqrt δ and mass C' exp(δΔ)/δ. Concentrating a positive pulse through G_b makes the output maximum asymptotic to the pulse mass divided by 1-exp(-bP), so the two prefactors and square-root ratio are as claimed. Independently evaluated quadrature for Q=sin t, P=2π, a=b=1 at δ=10,25,60: normalized KA/asymptotic 1.123,1.047,1.019; KB/asymptotic .662,.717,.778; KA/(sqrtδ KB) decreasing toward predicted 0.3982. Numerical tests are not the δ→∞ proof. The scalar expansions have identical mean a+b, mean ab and identical Floquet multipliers.

## originality

PASS

Prior Green-operator theorems already yield general exact best Ulam constants; Darboux-type factor swap and matching monodromy spectrum are also classical. The noncovered claim is a sharp two-order large-modulation comparison with full prefactors despite matched Floquet multipliers and coefficient averages.

## value

PASS

Optimal Ulam constants quantify worst-case error amplification, while Floquet multipliers quantify homogeneous spectral stability. An exact arbitrarily large square-root mismatch between two isospectral periodic equations is an instructive structural counterexample to spectral surrogates for uniform residual sensitivity, with universal two-saddle prefactors; this is not a trivial factor permutation identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
