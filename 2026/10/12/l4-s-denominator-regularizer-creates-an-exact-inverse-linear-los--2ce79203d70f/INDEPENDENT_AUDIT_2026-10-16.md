# Independent mathematical audit

## correctness

PASS

With L=lambda x^2/2, v=g=lambda x and q_t=min(S_t,L_t)/L_t, the exact update is x_{t+1}=c_t x_t, c_t=1-(alpha/2)(1-gamma q_t)*(lambda^2 x_t^2)/(lambda^2 x_t^2+epsilon), 0<c_t<1. Therefore q_{t+1}=min(1,(1+1/tau)q_t/c_t^2), which reaches 1 by ceil(log(1/gamma0)/log(1+1/tau)) and stays locked. With A=alpha(1-gamma)/2>0, z=lambda^2 x^2/epsilon then z_{t+1}=z(1-Az/(1+z))^2, decreases to zero and 1/z_{t+1}-1/z_t ->2A; Stolz yields t z->1/(2A), hence tL->epsilon/[2alpha(1-gamma)lambda]. Independently checked recurrence, default tracker cap 288, and long numerical tail; source verify.py is corroboration not proof. q_t presumes initial loss L(x0)>0, thus the stated nonzero trajectory domain; x0=0 is the separate trivial stationary exception.

## originality

PASS

The original L4 NeurIPS 2018 scheme explicitly contains the denominator epsilon and forgetting tracker but does not derive finite tracker lock or the exact inverse-linear asymptotic; existing scaled Polyak and stochastic SPS analyses have different state dynamics and no identical practical L4 theorem.

## value

PASS

Determines exactly how a small numerical regularizer changes the asymptotic convergence *class* from geometric to inverse-linear in a natural diagnostic quadratic of a named optimizer. Although very-late asymptotics for tiny epsilon may be practically invisible, the singular perturbation and tracker-lock law are precise reusable algorithmic facts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
