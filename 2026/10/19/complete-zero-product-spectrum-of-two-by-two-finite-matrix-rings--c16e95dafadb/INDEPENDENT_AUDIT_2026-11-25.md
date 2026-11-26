# Independent mathematical audit

## correctness

PASS

The proof yields the full real characteristic polynomial for the exact graph in the Finding. Put n=q+1 and s=q−1. Each ordered kernel/image type contains s vertices; the incidence of types (i,j),(k,l) is j=k or l=i. Removing the self-loops gives H⊗J_s−D⊗I_s. The fiber sum-zero spaces give the displayed zero and −1 factors, while the type-constant operator is Bf_ij=s(r_j+c_i−f_ji)−1_{i=j}f_ii. Its skew differences a_i−a_j have eigenvalue −s(n−1); its skew row-null arrays have eigenvalue s. Its symmetric zero-diagonal row-null arrays have eigenvalue −s: the row-map transpose a↦(a_i+a_j)_{i<j} is injective for n≥3. The two remaining symmetric blocks use the constant diagonal/off-diagonal pair and the zero-sum diagonal/off-diagonal pair; substitution gives P_q and Q_q. The dimensions exhaust n². Both quadratics have negative constant term and neither vanishes at −1 (P_q(−1)=−(q−1)(2q²−q−2), Q_q(−1)=−q²(q−2)−1). The −s eigenspace vanishes at q=2, so rank, inertia and −1 multiplicity follow without exceptions; the energy follows from the positive square roots of the two discriminants and the remaining linear factors. The source script was inspected, not executed: its exact finite checks over F_2,F_3,F_4,F_5 corroborate the type criterion and quotient characteristic polynomial, and check the full polynomial at q=2,3. The proof, not the script, establishes the unbounded prime-power claim.

## originality

PASS

The supported distinct result is the uniform explicit diagonalization of the entire quotient and the sharp spectral consequences. The ordered type structure, within-type eigenvalues and largest eigenvalue in the odd-prime case have prior coverage and are not credited as new here.

## value

PASS

This is a natural minimal noncommutative finite matrix family, not a single selected field or a tabulated graph. The full quotient splitting resolves an explicit gap in earlier spectral reductions: uniform exact multiplicities, rank, inertia and energy are usable without diagonalizing a separate growing matrix for each field order. In particular it shows the known lower bounds are sharp and treats even and extension fields with the same proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
