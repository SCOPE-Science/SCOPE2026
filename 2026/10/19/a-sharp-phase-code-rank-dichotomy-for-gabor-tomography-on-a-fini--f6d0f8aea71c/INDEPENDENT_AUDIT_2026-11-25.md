# Independent mathematical audit

## correctness

PASS

For each Weyl matrix W_l, the measurement at k is g_z* W_k* W_l W_k g_z, namely g_z*W_l g_z times the symplectic character of k labeled by l. Nondegeneracy of the finite-field trace pairing makes those characters distinct and orthogonal. Thus the columns indexed by nonzero ambiguity coefficients are independent and the zero columns span the kernel. In the standard conjugate-linear-first convention g_z*W_l g_z is exactly the conjugate of B_z(l)/(2q-1); no index reflection is needed with this convention. For zero displacement the cross transform is q[ u=0 ]+q[ v=0 ]-1. An axial displacement leaves its full axis with two endpoint corrections (z-1) and (conj(z)-1) times the character at the displaced origin. A mixed displacement meets the cross only at (a,0) and (0,b), where both products have unit phase. The flat axial count is q each. Mixed coefficients cannot cancel in odd characteristic, and in characteristic two vanish on exactly the trace-one half for each mixed displacement. This gives the stated flat rank and the code-independent ceiling. The odd sign code's axial values are q-4 or -2(1+character), nonzero. In characteristic two the cubic code's axial values are q-3, -3 or z-conj(z), all nonzero including q=2, so the kernel is exactly the forced mixed-label span. Binary sign coding leaves axial zeros at trace one for every nonzero axial displacement; order one is flat, proving the asserted minimum root order 3, and 2 is minimal in odd characteristic. Subtracting flat from optimal counts gives 2(q-1)(q²-q). The frozen script and stdout were inspected, not rerun; its dense Gram calls at q=2,3,4 concern sign and cubic test codes, while coefficient checks cover the flat rank as well. The proof is for the full orbit and fixed-modulus one-center-phase cross family, over complex operators; it is not a pure-state result.

## originality

PASS

Credit the exact cross-specific characteristic and code-order law, not the known ambiguity-rank reduction or a claim of all-window optimality. The closest broad cross statement covers one component exactly (the odd flat rank), but is indexed later and stops at flat odd-order indicators. The earlier inspected full-support one-coordinate ranks apply on a different group and geometry. No earlier equivalent complete claim was established.

## value

PASS

Linear measurement completeness and exactly which operators are invisible are natural design invariants for a sparse two-axis aperture. One site suffices to remove all lost directions in odd characteristic, whereas binary arithmetic forces precisely characterized invisible directions no phase at that site can remove. The ceiling, explicit kernel and least discrete root order answer distinct useful design questions and are not consequences of the general frame criterion without the cross-specific calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
