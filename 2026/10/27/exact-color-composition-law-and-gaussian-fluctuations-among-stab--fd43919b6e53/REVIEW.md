# Independent mathematical audit

## correctness

PASS

A change occurs exactly when the two neighbors agree against the vertex, so a fixed coloring has no singleton run. In a nonconstant profile the r blue runs and r white runs are alternating. Subtracting one from each run size gives the two positive-composition factors; mark one labeled blue-run start, count n choices for its location, then divide out r marks. This handles n=3 and the monochromatic and singleton-count endpoints. The pair-state trace counts labeled closed walks with one factor of z per blue vertex. Its quartic at z=1 factors as (λ²−λ−1)(λ²−λ+1), yielding the Lucas plus cosine total. The implicit derivatives of the Perron root are λ′(1)=φ/2 and λ″(1)=(5−√5)/40, so log λ(e^t) has second derivative (5+3√5)/40 at zero. The other three roots are simple at z=1 and have modulus ≤1 there. After factoring out λ(e^t)^n, each of their normalized powers contributes O(n²φ^(−n)) to the first two derivatives at zero; the Perron gap uniformly near zero gives the centered √n-scale Gaussian limit by the moment-generating function. Exact centering follows from complementing the colors. An independently written finite reproduction compared direct one-step synchronous updates, the run sum and the weighted trace through n=16 coefficient by coefficient; all agreed, including total 2206 at n=16. It did not execute the supplied verifier and does not certify the limiting arguments. Uniform fixed-point sampling is not assumed to equal a law induced by the dynamics.

## originality

PASS

The inspected same-model literature establishes the fixed-point/run equivalence and unweighted growth order. The supported distinct claim is the blue-count distribution on labeled uniform majority fixed points, including the explicit variance density and the sharp exponential scale of the variance error. Neither the unweighted total in isolation nor the method of transfer matrices and Perron-root perturbation is credited as new.

## value

PASS

Blue occupation is a natural state variable for this uniform majority-fixed-point ensemble, not an arbitrary filter or an absorption probability. The full labeled composition law and its explicit variance density expose excess fluctuations relative to independent fair colors that the equilibrium count cannot reveal. The result is useful as an exact benchmark for this ensemble without claiming a general opinion-dynamics theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
