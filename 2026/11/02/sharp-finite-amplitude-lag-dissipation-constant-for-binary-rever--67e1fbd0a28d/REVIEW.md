# Independent mathematical audit

## correctness

PASS

For an irreducible two-state reversible generator with q=a/(a+b), s=a+b, h(x)=log[x/(1-x)], the flux expression is sigma_s(x)=s(x-q)[h(x)-h(q)]. Thus the squared indicator lag/entropy production is exactly F_q(x)/s=(x-q)/{s[h(x)-h(q)]}. Differentiation gives N_q=h(x)-h(q)-(x-q)h'(x), N_q'=-(x-q)h''(x); h'' changes sign only at x=1/2. For q<1/2, F is smaller than its q-limit to the left, strictly rises on (q,1/2], then has precisely one non-equilibrium maximum x_q in (1/2,1) before descending to zero at x=1; q>1/2 follows reflection, q=1/2 follows h'(x)>=4. At the unique root F=x_q(1-x_q); hence C=x_q(1-x_q)/s versus balanced C=1/(4s). With L=log((1-q)/q), y=(1-x_q)^-1 solves y-qy²/(y-1)-L-log(y-1)=0; bracketing y=L+log L+o(1) yields the reported rare-output expansions and C/tau_m~1/[q log(1/q)]. Independent bisection/grid/derivative calculations for q=.1,.01,.3,.5,.7 and rare q=1e-8 matched the root and values, but finite checks do not imply the global statement. Frozen result and verifier scripts were read.

## originality

PASS

The global two-state finite-amplitude extremal coefficient and non-equilibrium equality state go beyond the cited near-equilibrium memory normalization and general nonsharp entropy bounds. Qualified best-of-knowledge only: classical two-state functional-inequality optimization might implicitly contain the same secant quotient.

## value

PASS

The optimal coefficient tests the exact finite-amplitude accuracy versus entropy-production tradeoff for the simplest reversible computation channel; its strict deviation from the usual integrated-memory coefficient is quantitatively important for rare equilibrium states, not merely a normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
