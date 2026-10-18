# Independent mathematical audit

## correctness

PASS

PASS. Source RESULT.md c2bfe9db88d0632fd097eca98641c3e15952f3ba inspected. Membership in cube+t*cross-polytope is sum_i (abs(x_i)-1)_+<=t; choosing the k excess coordinates in signed orthants proves vol(K)=2^d sum_{k<=d}binom(d,k)t^k/k!. Polar support inequality ||y||_1+t||y||_infty<=1; ordering nonnegative absolute coordinates and putting y_i=sum_{j>=i}z_j (unit Jacobian) yields polar volume 2^d/prod_{j=1}^d(t+j). R_d(t) thus exact and R_d(0)=R_d(infty)=1, R_d'(0)=d-H_d>0 for d>=2 so finite interior maximizer. Uniform Stirling/Laplace with t=ds produces saddle rho^2=s(1-rho) and Psi(s)=rho-log(1-rho)-(1+s)log(1+s)+s log s. Derivative under saddle gives h(y)=y-log(1+y+y^2), y=(1-rho)/rho; h'(y)=y(y-1)/(1+y+y^2) establishes single positive saddle y*>1 and positive max gamma. Independent arbitrary-precision root y*=1.793282132900761..., s*=0.199634949883..., gamma*=0.261152459394... and exact Fraction R_d(t)>1 for d=2,3,4,5,8,20 at t=1/2,1. For any global t_d, bounds R_d(t)<=exp(2 sqrt(d*t)) and <=exp(d^2/t) exclude t_d/d->0 or infinity; compact-uniform convergence + unique Psi maximizer give all t_d/d->s*, (log max R_d)/d->gamma. High-d independent log-sum-exp checks d=50,150,500 give rates tending gamma. No finite computation substituted for infinite argument.

## originality

PASS

PASS for the growing-dimensional optimization, subject to historical Laguerre asymptotic risk. Volume formula and cube plus cross-polytope low-d evaluations are partly known (Fisikopoulos 2013), the general volume product/mimimum problem is classical (Kim-Zvavitch 2013, Fradelizi-Meyer-Zvavitch 2023), and a public 5D ray computation covers limited d=5 specializations. None of these finite tables or local-minimality statements implies the unique global maximizer scale t_d/d->s* and exponential maximum rate gamma*. Polynomial numerator is a Laguerre polynomial, so a different notation in classical asymptotic optimization could potentially give exact same theorem; that risk is retained. Resultary unavailable, not evidence of novelty.

## value

PASS

PASS. The volume product is a central affine-invariant object and the cube/cross-polytope are canonical Hanner extremizers. Determining how their Minkowski interpolation develops a global interior maximum, with exact asymptotic maximizing scale and exponential growth rate in unbounded d, is a natural unresolved quantitative convex-geometry question, not an arbitrary finite slice or a mere restatement of classical stability. The proof provides universal localization of all global maximizers and a new variational asymptotic. No claim about global Mahler conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
