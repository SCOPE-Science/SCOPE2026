# Independent mathematical audit

## correctness

PASS

For the specified equal-sized two-population game with three logistic environmental rates, differentiate each logit. With u_j=1/(1+theta_j), u1 d(logit n1)/dt=x-u1, u2 d(logit n2)/dt=y-u2, and 2u12 d(logit n12)/dt=x+y-2u12. The combination H=u1 logit n1+u2 logit n2-2u12 logit n12 therefore has exact constant slope Delta=2u12-u1-u2 for every interior-environment trajectory, regardless of bounded payoff matrices and interaction rate. If Delta !=0, H diverges linearly, excluding compact fully interior recurrent trajectories/invariant sets; the extremal weighted-logit inequality H<=W max{logit n1,logit n2,-logit n12} with W=u1+u2+2u12 proves exponential approach to one of the appropriate boundary-face union, rate |Delta|/W, with pointwise equality at equal signed logits. At resonance Delta=0, choosing A(0)=[[3,2],[1,0]], A(1)=[[1,0],[3,2]] and x=u1,y=u2,n12=q,n1=n2=(1/2-delta q)/(1-delta) for q near 1/2 gives explicit one-parameter continuum of interior equilibria, showing the necessary condition is attainable. Signed sign cases, invariant boundary caveats, and only core-residence bound are respected.

## originality

PASS

Betz, Fu and Masuda (2024) give the same five-dimensional evolutionary-game equations and a symmetric equilibrium reduction; their reported mismatched-ratio equilibrium obstruction is prior. The exact payoff-independent affine log-odds drift for arbitrary asymmetric feedback triples, quantified optimal exponential boundary-union envelope and explicit asymmetric resonant equilibrium continuum are not stated in the inspected original primary versions. Other two-population feedback papers model one environment or moving network densities and do not have these three cancellation equations.

## value

PASS

The resonance surface is a natural structural boundary between the possibility and impossibility of compact fully interior dynamics, independent of the population game payoffs. The sharp quantitative boundary-face escape and constructive asymmetric interior equilibrium family make the cancellation a useful dynamical theorem beyond an elementary normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
