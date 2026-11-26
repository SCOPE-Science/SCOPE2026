# Independent mathematical audit

## correctness

PASS

For θ>0, T=(R−(1−θ)I)/θ with R=(I+tL)⁻¹, t=θh. The inverse is entrywise nonnegative: factor out 1+t times the maximum weighted degree (with the factor understood as 1+t d_max), and expand the resulting inverse as a Neumann series in the nonnegative matrix t(d_max I−L)/(1+t d_max), whose row sums are <1. Only the diagonal can obstruct positivity. On the orthogonal complement of the constant vector all eigenvalues of L are positive by connectedness and at most nw by the edge-energy comparison to the capped complete graph. Consequently R_ii decreases strictly to 1/n and is at least (1+tw)/(1+ntw). At t>0 equality requires every spectral component of e_i−1/n·1 to have eigenvalue nw, i.e. L e_i=nw(e_i−1/n·1). Comparing off-diagonal entries in this column gives exactly c_ij=w for each j≠i, with no constraint on peripheral edges. Solving the diagonal condition gives the displayed H and the θ cutoff. Strict monotonicity and the endpoint limit give the exact horizon behavior; for θ=0 it follows directly from 1−h d_i. The introductory phrase ‘row-stochastic … although it need not be entrywise nonnegative’ should be read as ‘has unit row sums’; under the usual nonnegative convention it is stochastic only in the positivity region. This wording does not alter the explicit theorem or proof.

## originality

PASS

The defensible contribution is the exact weighted capped-graph comparison with identification of all equality graphs across the full θ interval. The prior spectral/diagonal criterion and complete-graph comparison already contain the numerical Crank–Nicolson bound when combined with the elementary capped spectral estimate, and the all-θ scalar comparison is a short extension. Do not credit those ingredients as stand-alone new claims. The checked earlier work does not supply the exact graph-family equality classification for arbitrary capped conductances and θ.

## value

PASS

An exact step-size guarantee and a complete extremizer classification answer a motivated numerical-positivity question. In particular, one saturated vertex rather than a complete graph suffices, and adding, removing or reweighting peripheral edges cannot improve the worst horizon in that case. This specifies when the bound can and cannot be improved for a graph, unlike a norm/CFL guarantee alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
