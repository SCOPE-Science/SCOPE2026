# Independent mathematical audit

## correctness

PASS

Independent curvature check: for d=β−α>0 and w in (0,1), let p=Bx^d/(A+Bx^d) be the density contribution fraction of the higher-shape component. Its derivative is dp/dx=d p(1−p)/x. The mixture score is −λ+(α−1+dp)/x (here dp means d times p), so the scaled curvature is −(α−1)−d p+d²p(1−p). Since p spans (0,1) for every permitted rate and weight, α<1 fails as p→0, and for α≥1 and 0<d≤1 the curvature is strictly negative. For d>1, the quadratic has its unique maximum at p=(d−1)/(2d), where Bx^d/A=(d−1)/(d+1) and the maximum equals (d−1)^2/4−(α−1). When it is positive and α≥1, its nonpositive endpoint limits and strict downward quadratic shape give exactly one positivity interval (left endpoint x=0 if α=1) and negative curvature elsewhere outside its closure; solving the equivalent t=B x^d/A quadratic gives the stated endpoints. At the d>1 equality threshold only the maximizer has zero curvature; (α,d)=(1,1) instead has strictly negative curvature on x>0. Shapes (2,5) and (2,6) give maxima 0 and 5/4, respectively, confirming the sharp examples. At excluded endpoint weights the density is a single Gamma, and the violating point for shapes (2,6) can escape to a support boundary as one weight vanishes. The frozen rational checker was inspected, not run; the analytic replay applies to all real shapes, unlike the finite instances.

## originality

PASS

Bounded comparison supports the sharp common-rate, distinct-shape phase boundary and its attained normalized-curvature refinement. The general mixture differentiation identity is standard; the assessed claim is the exact weight-independent classification for this family, not the differentiation rule. The strongest inspected records have different variable parameters or a different distribution family.

## value

PASS

This is a complete exact test for global log-concavity in a natural, common-rate model, not a finite algebraic example. In particular, two individually log-concave components can fail the density shape constraint for every interior weight; adjusting a weight only moves the failure region. The sharp square-root gap gives a usable Erlang model-design rule, with an explicit curvature witness and tangency at equality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
