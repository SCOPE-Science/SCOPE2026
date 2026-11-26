# Independent mathematical audit

## correctness

PASS

With P=(I+gamma B)^(-1) and u=P(z−gamma b), the prox equation gives (z−u)/gamma=Bu+b, so the source normal residual is Hu+a+b with invertible Jacobian HP, in that order even for noncommuting A,B. Its Newton direction is exactly z_*−z, for z_*=(I+gamma B)x_*+gamma b. At the full trial, affine prox yields x_*+(1−theta)(y−x_*); quadratic energy above the minimum is therefore (1−theta)^2 times that at y. To check the decrease independently, put d=y−hat x. Quadratic Taylor identities and proximal optimality give phi(y)−phi(hat x)=−||d||^2/gamma+d^T(A−B)d/2, at most −gamma(2−gamma L_f)||R_nat(hat x)||^2/2. Thus every theta in [0,2] passes, strictly at nonstationarity because sigma is below that coefficient; theta=1 lands at x_*. No invertibility of the forward map is needed. For any fixed theta outside the interval, choose the scalar L=1, g=0, gamma=1/2, hat x nonzero. Acceptance requires (1−theta)^2/4<=1−2sigma. The admissible upper limit sigma=3/8 is excluded, but the right side tends down to 1/4 there, proving existence of a rejecting admissible sigma for each such theta. This is universal sharpness over the legal parameters, not a claim about every fixed sigma.

## originality

PASS

The defining paper supplies a decrease test and eventual superlinear-step result, not this global characterization of relaxed exact normal Newton on quadratics. Newton solving an affine residual by itself is standard. The supported distinction is universal acceptance for every admissible decrease parameter, including the part of the stepsize range at and above 1/L_f, together with the matching failure outside the relaxation interval. The closest inspected independent normal-map Newton algorithm uses a different merit and only an eventual unit-step guarantee.

## value

PASS

The result determines a sharp safeguard boundary for a named algorithm. In particular it gives full acceptance even in the doubled stepsize range outside the faster local theorem's hypotheses, and includes the reflection that leaves proximal-gradient energy unchanged. The simple scalar obstructions distinguish an exact universal interval from just another sufficient estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
