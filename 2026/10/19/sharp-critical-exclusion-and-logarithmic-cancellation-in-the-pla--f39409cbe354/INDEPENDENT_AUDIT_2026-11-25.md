# Independent mathematical audit

## correctness

PASS

The cited global theorem applies inclusively at s=beta*r: alpha*s<r, both growth parameters lie strictly between 0 and 2, and the isoclines cannot coincide. Thus x tends to r and y tends to zero for strictly positive starts. In q=x-r+alpha*y the exact second update has exponent -gamma*y-beta*q, so y'/y tends to one. Taylor's formula gives q'=(1-r)q-alpha*gamma*y^2+O(q^2+y|q|+y^3). Dividing by the slowly varying y^2 yields an affine contraction asymptotically with multiplier 1-r, so q/y^2 tends to -alpha*gamma/r. Subtracting this quadratic and applying the same estimate with forcing O(y^3) gives the claimed cubic remainder without assuming initialization on a center manifold. With w=1/y the recurrence then reads w'=w+gamma+A/w+O(w^-2), where A=gamma^2/2-alpha*beta*gamma/r. It implies w/n tends to gamma, then w=gamma*n+O(log n). Subtracting (A/gamma) log n leaves summable increments of order log(n)/n^2 and hence a finite offset. This confirms the cancellation location and the signs whenever parameters remain admissible. Independent finite trajectories with two initial states per parameter set exhibit both signs and cancellation, and corroborate the stable-coordinate coefficient; they do not prove convergence.

## originality

PASS

Best-of-knowledge pass for the universal explicit logarithmic coefficient, the finite corrected constant for every interior orbit, the quantitative slaving term, and the resulting cancellation surface. Global convergence and the local transcritical mechanism are prior inputs, not new results.

## value

PASS

At invasion neutrality the excluded population dies algebraically and linearization alone predicts no timescale. The next-order log coefficient distinguishes two opposite drifts and an exact cancellation, where subtracting the leading linear reciprocal term suffices for a finite offset. The assertion is for the whole basin and provides a quantitative distinction beyond the existing global convergence and generic normal form.

The dated certificate retains the supplied scientific assessment, sources and limitations.
