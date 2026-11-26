# Independent mathematical audit

## correctness

PASS

For exactly three distinct eigenvalues 0<a<b and E=11^T/n, independently interpolate the step as alpha I+gamma L+(1-alpha)E. Writing Q=(12+6ah+a^2 h^2)(12+6bh+b^2 h^2), substitution at a and b gives gamma=-12h(12-ph^2)/Q and 1-alpha=12hp(6h+sh^2)/Q, where s=a+b and p=ab. This reproduces every off-diagonal bracket F_w=12w+6ph/n+p(s/n-w)h^2. The scalar multiplier is a quotient of strictly positive completed squares, so the symmetric step is positive definite, has positive diagonal, and fixes the all-ones vector. For w<=s/n the bracket is strictly positive at h>0, even on nonedges. For w>s/n it is concave with positive constant and exactly one positive root, the stated H_w. At such a root h>sqrt(12/p), so increasing w makes the bracket strictly smaller. Thus the maximum conductances are exactly the first zero entries and stay negative thereafter; h=0 is the identity, and the horizon itself is nonnegative. In the strongly regular case the common-neighbor relation yields sum s=2k-lambda+mu and product p=v mu. Both distinct positive eigenvalues occur, since one nonzero eigenvalue alone would force a complete weighted support. Substitution gives the stated cutoff, with Petersen 1+sqrt(5), Paley equality in the all-step condition, and s=3m-2 for the triangular graph, exceeding or equaling v exactly for 4<=m<=6. Replay by the affine interpolant or RESULT.md lines 35–83; the frozen exact-rational checker was inspected but not executed. Repeated eigenvalue multiplicities are permitted; directed, more-than-three-spectral-value, and internal-stage claims are excluded.

## originality

PASS

The supported distinct claim is the exact dynamic end-step classification throughout the connected weighted class with exactly three spectral values, including which entries first vanish, the explicit finite horizon, and the absence of reentry. The strongly regular static boundary has prior coverage through the M-property, and complete multipartite all-step positivity has direct prior coverage. Exact later dynamic overlaps on narrower families are material but not evidence of earlier priority.

## value

PASS

This gives a sharp nonnegativity guarantee for a standard fourth-order end step, not a stability bound or a static graph label. It identifies the first failing edges, computes the exact horizon when finite, and rules out reentrant positivity for the full weighted spectral class. These are useful structural tests on a natural family where generic sufficient estimates can be vacuous. The preexisting static graph classifications need not be counted as new to support that value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
