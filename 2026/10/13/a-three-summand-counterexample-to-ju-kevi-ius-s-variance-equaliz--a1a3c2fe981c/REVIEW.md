# Independent mathematical audit

## correctness

PASS

The Juškevičius family uses the half-open (x,x+2] definition, and its canonical cells include all the proposed positive parameters, including 1. For the centered mixture of nu_k and nu_(k+1), the variance is the corresponding convex combination of (k^2-1)/3 and ((k+1)^2-1)/3. The mixing weight on the smaller variance strictly increases with alpha, and the endpoint formulas agree across cells. Thus variance is strictly decreasing and 1/2 is the unique common parameter for total variance 3. T(1) is a point mass, T(1/2) is Rademacher, and in T(2/5) the mixture weights 3/5 and 2/5 assign probability 1/5 to each of five consecutive integers. The original convolution has integer multiplicities (1,1,2,2,2,1,1)/10 on -3,...,3, so the heaviest possible two-adjacent-site window has mass 2/5. The comparison convolution has masses (1,3,3,1)/8 on -3,-1,1,3, so any such half-open window contains at most one atom and the maximum is 3/8. All variables are independent and the gap is 1/40. No optimality or classification is claimed.

## originality

PASS

The supported distinct finding is the explicit failure at the variance-one matching boundary alpha_*=1/2, with the five-point T(2/5) and exact gap 1/40. The unrestricted conjecture's falsity by itself is NOT a distinct first refutation: Mattner–Roos's older Schur-concavity discussion and adjacent-window identity already imply a refutation in the three-point T regime. At the present total variance 3 that regime cannot give any heterogeneous comparison, because each of its three variances is at most one. Thus that earlier result does not cover the boundary witness, and no implying comparison at this variance was verified.

## value

PASS

The specific counterexample probes the natural transition at matched alpha_*=1/2, the maximal mean variance of the three-point regime in which any heterogeneous choice at that variance is impossible. A five-point factor can reach it, and the exact mass comparison isolates the discrete adjacent-window effect at a Rademacher comparator. A further arbitrary refutation of the conjecture, which already follows from older work, would not on its own pass value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
