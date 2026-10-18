# Independent mathematical audit

## correctness

PASS

Each display H_t is the complement of one omitted x_t. An s-subset remains unseen precisely if it contains every omitted element, so U_t=C(n-K_t,s-K_t) if K_t<=s, otherwise 0, pathwise. The missing-element walk chooses one of the n-1 other vertices uniformly; when K_t=k, n-k choices are new, giving p_k=(n-k)/(n-1). Therefore K_t-1 has exactly the same finite-dimensional birth-and-hold law as ordinary iid occupancy on n-1 symbols after t-1 draws; first passage to K=s+1 equals T=1+sum_{k=1}^s independent geometric(p_k). Generating function, mean, variance and Stirling marginal laws follow exactly. If s=floor(alpha n), Riemann sums give E[T]/n=-log(1-alpha) and Var(T)/n -> 1/(1-alpha)+log(1-alpha)-1; p_k bounded away from 0 ensures Lyapunov CLT. Independent direct omission-path enumeration for n<=6, t<=5 checked all occupancy laws, exact pathwise uncollected counts, geometric mean/variance identities.

## originality

PASS

Best-of-knowledge exact dense-complement reduction for the Athreya–Mukherjee–Mukherjee Markovian supercoupon process: the all-time law for arbitrary interior s is distinct from the previously studied r=s boundary and classical iid coupon formulas. The complete model and original asymptotic questions are credited.

## value

PASS

The maximally dense nontrivial display size r=n-1 is a natural limit of the Markovian supercoupon model. Its exact uncollected process, independent waiting-time representation, finite generating function and growing-s proportional-size CLT provide a complete distributional solution in a regime not handled by the source s=r asymptotic, rather than one expected-value estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
