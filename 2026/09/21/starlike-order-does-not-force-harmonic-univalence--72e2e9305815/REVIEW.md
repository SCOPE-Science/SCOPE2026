# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The construction was checked algebraically and against the local geometry near the boundary point z=1.

The identity g'(z)=z h'(z) gives dilatation omega(z)=z. For beta>0, Na<1, so h' is zero-free in the disk and the Jacobian is positive. The starlike-order calculation reduces exactly to the positive-real-part Möbius factor (1-w)/(1-aw), and radial approach w->1 shows that beta is the exact order.

For nonunivalence, H=h-g satisfies H'=(1-z)h'. Its boundary expansion has a nonreal real-level branch x(y)=c y^2+O(y^4), where c=N(1-beta)/(3 beta). The stated integer condition makes c>1/2, which puts that branch inside the unit disk. Real coefficients then pair conjugate points on this branch to the same harmonic value. The sign in the disk condition and the Taylor coefficients were independently rechecked. A supplementary high-precision computation verifies representative cases beta=1/2, 0.9, and 0.99.

## Originality

**PASS, to the best of our knowledge.** Zhu and Huang (2015), Remark 18, explicitly ask for the sharp beta in the locally univalent sense-preserving class with starlike analytic part of order beta. Nagpal and Ravichandran (2012/2014) give a nonunivalent order-zero example with g'=z h', but not a family reaching arbitrarily high starlike order. Hotta and Michalski (2014) characterize coefficient/distortion behavior for locally one-to-one harmonic maps with starlike analytic part and do not state the universal negative threshold result found here.

The comparison also included exact and synonymous searches for the Zhu-Huang threshold question, the polynomial form h(z)=z-a z^N, the relation g'=z h', and counterexamples with starlike order approaching one. No prior theorem located in those comparisons implies or states the present all-orders obstruction.

A potentially relevant source not fully inspected is E. Yavuz, “Harmonic univalent functions with Janowski starlike analytic part,” RIMS Kôkyûroku 1626 (2009), 127–134. Available metadata identifies a Janowski-starlike sufficient class, but the full text was not available in the inspected repository view. It remains a residual originality risk, as do differently parameterized sufficient-subclass papers not indexed by the terminology above.

## Value

**PASS.** The result changes the qualitative answer to the 2015 threshold question: no beta<1 can serve as a universal sufficient order. The construction is explicit up to a one-line integer choice, reaches exact orders arbitrarily close to one, and explains failure through a boundary fold of H=h-g. It also shows that the earlier order-zero counterexample mechanism is not confined to weakly starlike analytic parts.

## Limitations

- The result is negative and universal only with respect to starlike order; extra assumptions on the analytic part or dilatation may restore univalence.
- The endpoint convention at order one is degenerate and is not treated as a nonempty strict starlike-order class here.
- The literature comparison is targeted rather than exhaustive, and the Yavuz 2009 full text was not inspected.
- Independent audit has not been performed.
