# Independent mathematical audit

## correctness

PASS

With alpha=2/p, log sinh(alpha t) concavity between alpha=1 and alpha=2 gives the claimed derivative sign; the sharp mixed coefficient is reached at equal positive inputs. The simplex inball, tested against the negative radial direction, gives max_i |q-v_i|² at least r²+R²+2rR/(d-1); the coefficients match exactly at p_d. For p>2 one instead uses l_p <= l_2 on the two scalar blocks. For |t|>=a the nearest apex vertical term is at most |t|^p; for |t|<a it is at most R^p. These cover the endpoint and all scales. Below threshold the explicit s satisfies s>lambda_d and s²>q_*, giving r_f<a<R and strict opposite inequalities at a base vertex (base distances <=s<1; both apex distances >1); the mixed/Euclidean Lipschitz bound supplies the claimed positive-volume open ball. All-base ties force q=g where a nearer apex beats the bases. In the horizontal plane on the facet-centroid-to-centroid segment, writing q-g=-u(v_i-g) for 0<u<=1/(d-1), the excluded squared distance minus a retained squared distance is 2uR²d/(d-1)>0. The retained distances cross the common apex distance a before u reaches zero. Downward closure and direct alternating summation on present apex indices give the exact nerve and sign. The frozen 456 checks use floating point and discrete samples; they were inspected, not rerun, and are not used for the universal result.

## originality

PASS

Pass is for the exact dimension-dependent universal mixed-norm threshold and its constructive subthreshold nerve and signed error within this family, not for the general existence of counterexamples or for inventing the bicone mechanism. The strongest checked primary and catalogue comparators overlap substantially in mechanism but neither gives this phase theorem.

## value

PASS

The theorem gives an exact dimension-dependent boundary for when this symmetric family can obstruct Voronoi-restricted volume inclusion–exclusion, not just an isolated counterexample. The universal side, positive-measure witnesses arbitrarily near the threshold, and dimension-dependent sign are useful quantitative and combinatorial information for this natural model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
