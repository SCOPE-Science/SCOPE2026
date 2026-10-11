# Independent mathematical audit

## correctness

PASS

On the two scalar quadratics, the SARAH recursion is exactly multiplicative: \(v_t=v_{t-1}[1-\alpha(1+\sigma_t h)]\). This gives the stated mean-square factor \(q=(1-\alpha)^2+\alpha^2h^2\) and exact stability interval. Writing \(x_t=x_0[1-\alpha\sum_{j<t}P_j]\), the condition \(q<1\) makes the product series absolutely summable in L1 and L2; the perpetuity identity gives the stated residual second moment. At \(\alpha=1\), the cumulative sign products are iid Rademachers, and the \(h=1/2\) signed binary expansion is uniform on [-1,1]. Independent finite path enumeration reproduced the multiplier second moments for several parameter choices.

## originality

PASS

The defining SARAH paper proves that the recursive direction decays in a single inner loop and explicitly presents that behavior as a stability advantage; its algorithm still uses finite inner loops and outer full-gradient resets. Later work proves last-iterate convergence for finite/restarted SARAH and studies averaging/tuning. None of the inspected sources gives the almost-sure random limit of one inner loop run forever, its exact positive residual floor, or the Bernoulli-convolution/uniform slice. The audited theorem exposes a distinction not resolved by the published direction-decay theory.

## value

PASS

The result directly qualifies a published selling point of SARAH: vanishing recursive directions need not certify that a single long inner-loop iterate approaches the optimizer. The exact residual floor and uniform limiting example provide a sharp, reusable boundary case for variance-reduced optimization theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
