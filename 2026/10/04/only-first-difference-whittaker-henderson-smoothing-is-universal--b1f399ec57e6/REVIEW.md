# Same-model review

## Correctness
PASS. For order one, the normal matrix is identity plus a path-graph Laplacian, hence a nonsingular irreducible \(M\)-matrix; its inverse is strictly positive and fixes the all-ones vector, so every smoother row is a probability vector. For every order \(p\ge2\), the minimal sample size \(p+1\) reduces the penalty to one binomial difference row. Sherman–Morrison gives the smoother exactly, and the \(p-2\) entry of a terminal step is \(-\alpha\binom p2\). An affine perturbation lies in the penalty nullspace and converts the witness to strictly positive, strictly increasing data. Exact-rational replay returns `VERIFY_OK`.

## Originality
PASS with residual literature risk. Explicit order-one Whittaker–Henderson weights and explicit order-two Hodrick–Prescott weights are prior work; order-one positivity itself is not claimed as a new formula, and negative HP coefficients are not claimed as a new observation. The accepted contribution is the all-order if-and-only-if classification together with the minimal-length, every-\(\lambda\) obstruction and strict monotone witnesses for all \(p\ge2\). Searches under range preservation, monotone data, positive smoother, negative weights, and equivalent difference-penalty language did not locate that classification. Older graduation or positive-linear-operator literature remains the main risk.

## Value
PASS. Difference order is a basic modeling choice in a widely used smoothing family. The theorem separates an unconditional shape-safety property of first-difference smoothing from all higher orders, shows that the loss occurs at the smallest possible sample length and at arbitrarily weak smoothing, and provides closed-form witnesses that can serve as regression tests or motivate constrained variants when nonnegativity or range preservation matters.

Same-model review: passed. Independent audit: not yet performed.
