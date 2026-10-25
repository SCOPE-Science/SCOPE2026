# Independent mathematical audit

## correctness

PASS

Let A(t)=2K_Y(t)/t², V=A(0). The optimal variance-exact MGF pole parameter is precisely sup_{t>0}(A(t)-V)/[t(s+A(t))]; for fixed-jump centered Poisson let m(x)=2(e^x-1-x)/x², x=bt, r=s/(lambda b²). The objective c_s/b= sup_{x>=0}(m(x)-1)/(x[r+m(x)]), whose derivative has the sign of (r+1)D-U², U=m-1, D=xm′-U. The coefficient ratios of U²/D strictly increase: rho_j=2[2^(j+6)-(j+6)^2-(j+6)-2]/[(j+1)(j+5)(j+6)], with rho_0=4/3 and an explicitly positive all-j finite-difference polynomial. Therefore R=U²/D rises continuously from 4/3 to infinity: unique boundary maximizer x=0 for r<=1/3 and unique interior x>0 for r>1/3. As x→infinity, U~2e^x/x² and D~(x-3)U; stationarity implies m(x_r)/r=x_r-3+o(1), giving x_r=log r+3 log log r-log2+o(1) and b/c_s=x_r+1+o(1). For a nonzero spectrally positive Lévy measure with bounded essential positive endpoint b, upper bounds on A-V for t<(1-delta)log(s/V)/b and the positive mass near b for t>(1+delta)log(s/V)/b squeeze c_s log(s/V)→b; compactified optimizer and strictly positive numerator yield strict decrease in s. Fresh Fraction checks verified 21 rho_j identities and 20 differences; these finite checks do not establish all-j strictness.

## originality

PASS

The canonical sub-gamma variational expression and general Gaussian-convolution inequality are expressly prior results in Chen (arXiv:2610.00032). Chen–Wang signed-jump Skellam work already contains related logarithmic rare-positive-jump saddles and a 3 log log correction; signed negative jumps and Gaussian variance are analytically different mechanisms. The variance-proxy-frontier paper changes v for a fixed distribution rather than convolving with Gaussian noise. No inspected accessible statement implies the exact r=1/3 transition, unique Poisson optimizer, or all bounded-positive-jump endpoint limit. Best-of-knowledge PASS with explicit unresolved full-text priority risks.

## value

PASS

Optimal concentration envelopes matter because Gaussian smoothing changes the true-variance normalization and can shift the controlling saddle from the third cumulant to a global MGF level. The exact threshold r=1/3, unique saddle, two-term inverse-pole asymptotic and universal leading support-endpoint coefficient quantify a natural probabilistic regularization effect and are nontrivial sharp boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
