# Independent mathematical audit

## correctness

PASS

For deterministic scalar Signum with positive quadratic curvature and step, momentum beta in (0,1) and sign(0)=0, nontrivial return in two position steps forces one positive and one negative updated-momentum sign. Solving the TWO periodic momentum equations yields m_0=a(u-delta/(1+beta)), m_1=a(u-beta*delta/(1+beta)), and exactly beta*delta/(1+beta)<u<delta/(1+beta). These inequalities prove necessity as well as existence; endpoints lose the nonzero-sign itinerary. The two-step map with fixed sign itinerary is x_{k+2}=x_k and m_{k+2}=beta^2*m_k+(1-beta)*a*((1+beta)*x_k-delta), so the cycle family has tangential multiplier 1 and normal multiplier beta^2, not isolated asymptotic stability. Half-amplitude delta/2, crossing zero and the midpoint interval follow exactly. Reconstructed the recurrence from the actual RESULT and verifier and independently checked representative rational parameters and endpoints; grid checks are corroboration, not the all-parameter proof.

## originality

PASS

Best-of-knowledge new complete period-two manifold and exact two-step normal multiplier for the specified discrete momentum-sign algorithm. The primary algorithm source explains stochastic Signum but not a fixed-step scalar quadratic cycle classification; fixed-step oscillations of related RMSprop/Adam and nonsmooth sign methods use different maps. No stronger inspected statement entails this particular family. Search incompleteness is explicit.

## value

PASS

A complete exact classification of a continuum of neutrally stable cycles in a standard sign-momentum optimizer addresses a motivated fixed-step stability question. It separates fixed step-induced half-amplitude from momentum-controlled cycle-center bias and gives the actual normal convergence multiplier, contrasting with a claim of a unique attracting periodic orbit. This is a structural boundary for a natural algorithm, not an arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
