# Independent mathematical audit

## correctness

PASS

For the real Day--James hexagon N(u,v)=max(|u|,|v|,|u-v|), 0<r<=rho and p=4, separate convexity reduces fixed-scale maximization to 36 ordered vertices. The exact envelope is max(1+(r+t)^4,(1+rt)^4+max(r,t)^4). Independently enumerated all 36 vertex pairs over multiple r,t checks (diagnostic, not continuum proof) and differentiated both scalar branches symbolically. The RESULT.md proof: A_r(t) increases through t=1 for r<=rho; B_{0,r}(t) increases on [0,r] because its derivative E_r>0 using (1+t²)^3(1-t²)>=1 for t<=rho<.84; B_r(t) on [r,1] has exactly one maximum because t³[1-(1+rt)^(-3)] strictly increases. Its t=1 critical derivative is r(r³+2r²-2). Thus t_r in (r,1], (t_r³-r)(1+rt_r)^3=t_r³, and quotient is ((1+rt_r)^4+t_r^4)/(4(1+r^4)(1+t_r^4)). At r=rho t_r=1. Finite sampling does not prove the vertex envelope, but algebraic case checking and continuum convexity do; the analytic derivative argument covers all r.

## originality

PASS

Ni--Liu--Zhou 2025 Example 2.6 assumes (1-r)(1+r)^3<1 at p=4, algebraically r>rho; the complementary 0<r<=rho has a distinct adjacent-vertex maximizing branch not obtained by substituting into their hypothesis. The older balanced Yang--Wang hexagon/octet constants do not imply unequal-weight optimization. Resultary returned the focal record plus other generalized/Jordan/James invariants, no found implication. This is a best-of-knowledge comparison, not proof of exhaustive literature coverage.

## value

PASS

Fills the exact omitted parameter half of a published named invariant on a natural six-vertex benchmark, identifies an interior extremal scale and exact phase boundary; not a mere reparameterization because the maximizing vertex orbit switches. This finite polygon computation solves a mathematically motivated hole, not an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
