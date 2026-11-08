# Independent mathematical audit

## correctness

PASS

For E=diag(1,0), J=[[0,-1],[1,0]], R=diag(0,r), r>0, consistent initial (1,1/r), E_eps=diag(1+eps,eps), eigenmode decomposition of the unsplit ODE gives the slow eigenvalue -> -1/r, fast -> -r/eps and unsplit exact endpoint -> (t,t/r) with t=e^{-h/r}. The exact Strang conservative–dissipative–conservative matrix is C D C with theta=h/(2sqrt(eps(1+eps))), q=e^{-rh/eps}, C=[[cos theta,-delta sin theta],[sin theta/delta,cos theta]], D=diag(1,q). After scaling the second endpoint coordinate by sqrt(eps), the split endpoint equals (cos^2 theta,cos theta sin theta)+o(1), uniformly in phase. Continuous theta->infinity covers the entire radius-1/2 circle. Error squared in E_eps tends to t^2+(1-2t)cos^2 theta, hence exact positive liminf=min(t,1-t), limsup=max(t,1-t), equal 1/2 at h=r log2. E_eps-orthogonality of C and contraction of D give unconditional split energy dissipation. Independent SciPy matrix-exponential evaluations at three h,r pairs corroborate phase envelope but finite eps values are not asserted to equal the limits.

## originality

PASS

Bounded best-of-knowledge scientific comparison: Second order for each fixed eps allows eps-dependent constants and does not imply convergence for fixed h as eps->0. The example exhibits an order-of-limits obstruction with positive lower error; established general stability does not contradict it or provide these exact values. The targeted Resultary query and primary works were compared on objects, hypotheses, implication and parameters, not simply titles. No decisive prior-coverage theorem identified; this is not a proof of historical priority.

## value

PASS

A minimal explicit, dissipative index-one descriptor problem shows exact-subflow Strang splitting can be energy-stable and individually consistent but not uniformly accurate as regularization becomes singular. The full circle and sharp nonzero error range are stronger and more informative than an isolated failure example; a motivated numerical-analysis boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
