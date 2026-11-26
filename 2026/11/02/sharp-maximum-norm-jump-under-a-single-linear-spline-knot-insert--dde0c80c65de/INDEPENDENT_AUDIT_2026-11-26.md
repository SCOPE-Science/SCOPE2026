# Independent mathematical audit

## correctness

PASS

Use the peak-one hat h with nodes (0,t,1), rather than a truncated power. Its affine projection is (1−t)+(2t−1)x from its first two moments. The residual H has nodal values −(1−t), 2t(1−t), −t; these show ||H||∞=max(t,1−t). Its squared L² norm is the difference between 1/3 and 1/4+(2t−1)^2/12, namely t(1−t)/3. The left and right roots are t/(1+2t) and (2−t)/(3−2t); since ∫H=0, twice the negative triangle areas give ||H||₁=4t(1−t)/[(1+2t)(3−2t)]. The nested-space increment is the rank-one orthogonal projection with kernel H(x)H(y)/||H||₂². The measurable input sgn(H) attains the L∞-to-C norm. Multiplying the norm factors yields the formula. Reflection and differentiating on the left half give the unique midpoint minimum 3/2 and unattained boundary supremum 4. The inequality against 3 there is 4t²−8t+1>0, giving the stated threshold with its reflection. The quadratic inner product is −t(1−t)/12, so the increment on x² is −H/4, giving both the endpoint identity and the nonvanishing limit on fixed smooth data.

## originality

PASS

This is the first nonaffine Franklin detail on a finite free-endpoint interval, so the rank-one construction itself is classical. The closest exact increment norm located is for a bi-infinite grid, where the optimizer is reversed and the collapsing limit differs. The inspected general projector results concern each whole projector separately; nearby finite-element results impose different norm or mesh hypotheses. The claimed finite-interval all-t norm and fixed smooth-data obstruction were not found as statements or as specializations of those results.

## value

PASS

This is the smallest nested refinement that isolates what a newly introduced spline degree of freedom can do in max norm. Two individually bounded least-squares projectors can have an increment with norm tending to 4, and the persistent error for a fixed smooth quadratic shows the effect is not an artifact of adversarial inputs varying with t. The sharp formula also separates the finite free-endpoint setting from whole-line spline refinement, which has a different dependence on knot placement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
