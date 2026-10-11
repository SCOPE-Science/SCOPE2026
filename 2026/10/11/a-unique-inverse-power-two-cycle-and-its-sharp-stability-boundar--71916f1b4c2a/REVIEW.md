# Scientific review: inverse-power two-cycle classification

## Correctness — PASS

The claim is for every \(p>1\), \(0<a<1\), and \(b>0\) on the positive half-line, with a more explicit local-stability conclusion only at \(p=2\). The two cycle equations yield the necessary and sufficient ratio identity \(a=(r^p-r)/(r^{p+1}-1)\). Hyperbolic-sine reduction gives a strictly decreasing bijection from positive ratio parameters onto \((0,(p-1)/(p+1))\), proving existence and uniqueness without finite enumeration. The quadratic-inverse sum/product identities recover the two points and the exact second-iterate multiplier \(9a^2+6a-2\). Its strict monotonicity proves the attracting/repelling dichotomy. The packaged standard-library checker passed 1,804 finite identities; these tests are not used as proof of the continuum statements.

Boundary limitations are explicit: at \(a=(\sqrt2-1)/3\) only multiplier \(-1\) is established, and at \(a=1/3\) the primitive cycle disappears into the fixed point. Neither nonlinear critical stability nor a global attractor claim is made.

## Originality — PASS, with residual risk

The closest primary source is Le Van et al., arXiv:2610.01610v1, Proposition 5 and Appendix A.2. It supplies the existence half of the two-cycle threshold, not a necessity or uniqueness classification, explicit coordinates, or a sharp two-step stability multiplier. Its discussion explicitly warns that existence need not imply attraction. The present claim therefore is not the paper's sufficient-condition corollary. The 2018 full-text article by Abdelrahman et al. concerns nonlinear terms homogeneous of degree zero in delayed variables; its periodicity theorems do not cover the negative-degree single-state inverse-power term. The standard local derivative criterion itself is acknowledged as known.

Targeted searches for this exact map, the alternative ratio formulation, the quadratic multiplier, and older rational/difference-equation aliases, along with comparison against existing published mathematical records and own prior claims, found no mathematically dominating statement. Search absence alone is not a proof of novelty. Residual risk is an equivalent calculation in older unindexed difference-equation or economic-model literature.

## Mathematical value — PASS

The 2026 motivating paper highlights the mismatch between an oscillatory orbit's existence and whether it attracts nearby states. The theorem resolves that mismatch for a natural analytic exponent, while also giving a complete existence and uniqueness test for all inverse powers. The independent parameter boundary \((\sqrt2-1)/3\) separates repelling from attracting innovation cycles, and the scale parameter \(b\) affects the cycle positions but not their stability. Exact coordinate formulas let model users distinguish merely possible biennial oscillations from locally persistent ones. This is a motivated classification of a canonical reduced model, not a claim about all periods or the full economic system.

Same-model review: passed. Independent audit: not yet performed.
