# Independent mathematical audit

## correctness

PASS

At (x,m,v)=(0,0,V), gradient and first moment are zero so v+=V for all V≥0. For V>0, v>lambda²x² locally fixes the Yogi sign branch and v+=v-(1-beta2)lambda²x² has derivative dv+=dv. Because m+=0 at equilibrium, denominator variation in x-update contributes no first-order term. The 2×2 transverse block has trace 1+beta1-(1-beta1)chi_V and determinant beta1; Jury conditions with 0<beta1<1 give exactly 0<chi_V<2(1+beta1)/(1-beta1), equivalently V>Vc when qstar>eps. At V=Vc>0 the roots are -1,-beta1; beta2 enters only quadratic drift; at V→∞ a transverse eigenvalue approaches +1. Independently checked the symbolic trace/determinant in SymPy. No differentiable V=0 assertion.

## originality

PASS

The original Yogi method and sensitivity to moment initialization were published, but the scalar optimizer-state fixed ray, exact sharp transverse Jury boundary, beta2 linear decoupling and asymptotically slow normal rates are not stated in the inspected defining paper or identified indexed later records.

## value

PASS

The analysis identifies a non-isolated continuum of optimizer-state equilibria and a sharp initialization-dependent normal-stability threshold for a widely studied adaptive method; it quantifies the tradeoff between moment inertia and arbitrarily slow local rates and distinguishes state stability from parameter convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
