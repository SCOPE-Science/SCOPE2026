# Independent mathematical audit

## correctness

PASS

Rebuilt the incoming-state Laplace backward system with generator matrix [[s+a,-a],[a,-(s+a)]], right absorbing u_+(1,s)=1 and sticky wall u_-(0,s)=(a+g)u_+(0,s)/(a+g+s). Matrix square s(s+2a)I yields exact initial transform F(s)=1/[cosh(z)+s(s+2a+g)/(s+a+g) sinh(z)/z]. Comparing the transform low-order expansion and independent backward moment ODEs in the inspected verifier recovers EY=1+a+a/(a+g) and the displayed rational variance. Independently differentiated the variance: V_a=2Q/[3(a+g)^3], Q_aa=24a²+(36g+24)a+12g²+24g>0, Q_g>=3 for a>=0,g>=0. For h(g)=min_{a>=0}Q(a,g), h(0)<0 by a=1/4, h(1)>0 by positive coefficients, and h strictly increases, establishing a unique positive double root and the exact stationary point count. At that nondegenerate root Q_g,Q_aa>0, Taylor with sqrt(g_c-g) yields the claimed coefficient; mean derivative 1+g/(a+g)^2>0. Numerical nondegenerate roots and moment identities checked symbolically, but are not substitutes for the global convexity proof.

## originality

PASS

Best-knowledge PASS for the exact global variance-extrema phase classification for directed left-end initial injection and enhanced sticky-wall release, not for the general first-passage transform or computable moments. Angelani 2023 generic-boundary theory includes a Laplace-exit-time framework that in principle determines all moments, so this mathematical antecedent is credited. Earlier run-and-tumble first-passage work treats mean exits; Angelani 2024 mean-optimal rates use central/symmetric starts, not this variance observable. Mercado-Vásquez–Boyer examines variance-related fluctuations for a stochastically gated target, a different boundary mechanism and optimization parameter. No inspected primary result identified the unique (a_c,g_c) double root and all-g variance count; possible implicit derivation remains residual risk.

## value

PASS

The threshold changes the qualitative variance-versus-bulk-tumbling response from a maximum/minimum pair to monotonic growth while the mean remains strictly increasing in the same experiment. This natural stochastic transport observable, exact boundary-rate tuning transition and square-root collision are concrete physically interpretable quantities not implied merely by a transform formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
