# Independent mathematical audit

## correctness

PASS

The synchronous sign-comparison update conserves total S by pair cancellation. Equal heights remain tied and displacements strictly decrease across distinct height classes. The known two-time potential rules out primitive cycles longer than two; every unequal pair must reverse ordering on a recurrent step. For an ordered k-class state with multiplicities (m_j), the displacement drop between adjacent classes equals m_j+m_{j+1}; strict reversal iff every gap 1<=g_j<=m_j+m_{j+1}-1. Given ordered multiplicities and gaps, S=nh_1+sum_j(n-M_j)g_j fixes at most one integer baseline, yielding exactly the stated multinomial modulo-n count A_{n,S mod n}. One fixed state iff n|S; other recurrent states pair to give C_n=(A-1_{n|S})/2. The gap bound gives spread<=2n-4 for n>=4, with equality precisely at (1,n-2,1), maximal gaps and n(n-1) maximal-phase cycles only at zero sum residue. Independent code separately enumerated normalized nondecreasing states and the distinct composition-gap formula for n=2..7, agreeing for every residue and recovering A_{5,*}=(401,370,300,300,370). These finite checks corroborate the all-n structural proof.

## originality

PASS

PASS best-of-knowledge for the complete energy-shell count and sharp recurrence spread census. Duffy et al. established the same sign-diffusion model and order-reversal criterion, and Long--Narayanan all-graph eventual period at most two; both are prior and expressly credited. Duffy's *complete graph two-height* theorem in the actual source is Theorem 3.4 (source RESULT cites Theorem 3.7, which concerns bipartite graphs: a bibliographic cross-reference error without affecting the proved numerical theorem). No inspected source gives the ordered-composition residue count or extremal-orbit counts. Standard degree-threshold parallel chip firing is a different update, not a matching antecedent.

## value

PASS

A conserved-total fibre is the natural invariant decomposition of the infinite integer diffusion state space. Quantifying precisely the orbit population for each total, its nontrivial dependence on S mod n, and exact sharp recurrent spread/attaining cycles answers mathematically motivated questions beyond mere periodicity. This is a uniform finite formula for all graph sizes, not an arbitrary table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
