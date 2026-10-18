# Independent mathematical audit

## correctness

PASS

For a,b,u0>0 and unforced scalar u'= -a u-b u^2, R=b*u0/a. Reciprocal transformation solves u=u0 e^-at/(1+R(1-e^-at)). Monomial Carleman lift is upper bidiagonal y_j'=-ja y_j-jb y_(j+1). Order-N finite-section first component is u0 e^-at sum_{k=0}^{N-1}(-R(1-e^-at))^k, giving exact relative error z(t)^N. Finite-horizon uniform convergence iff z(T)<1; R>1 critical time tc=a^-1 log[R/(R-1)]. On infinite half line uniform absolute convergence iff R<=1; at R=1 optimizing x(1-x)^N/(2-x) yields x_N=(N+1-sqrt(N^2+1))/N and u0/(2eN) asymptotic. Under source scaling c/a=(1+R)/2, alternating vector Rayleigh quotient (N/2)[(c-a)N-(a+c)] positive for N>(R+3)/(R-1); the latter is a sufficient order, not minimal. Independent exact rational finite checks corroborate the closed forms.

## originality

PASS

The original Li–An R<1 dissipativity theorem and R>1 finite-horizon numerics supply motivation but not this scalar sharp all-time threshold. Earlier Muñoz-Sánchez–Elena–Oteo 2025 full OA article constructs the same-type Riccati Carleman recurrence and small-order approximants, not an all-N exact remainder with the finite-horizon iff/R=1 uniform critical rate/source-scaling Rayleigh obstruction in inspected relevant sections. Forets–Pouly develops broad local error bounds not same all-time boundary. Bibliography in submitted RESULT.md misattributes authors of 2025 article despite correct DOI; this must be corrected before public use.

## value

PASS

A concrete globally stable dissipative scalar equation on which finite unshifted Carleman truncations fail at late time for R>1 gives a sharp boundary to naive extrapolation of a numerical algorithm’s R<1 condition. The critical rate N^-1, exact failure time and lifted Hermitian obstruction quantify a natural algorithmic cutoff, rather than an arbitrary Riccati exercise; explicitly no claim about other embeddings or multidimensional necessity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
