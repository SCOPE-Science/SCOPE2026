# Independent mathematical audit

## correctness

PASS

Expanding [X,[X,Y]]=X²Y−2XYX+YX² on the matrix units gives the five coefficients ae, af+bh, eh, ei+fj, hj and the five additional coefficients 2ah, 2ai, 2aj, 2bj, 2ej, up to signs and repetitions. They are necessary individually: E₁₂ and E₁₃ give eh, ei+fj and hj; E₄₅ gives af+bh; E₃₅ gives ae; E₂₃, E₂₄ and E₃₄ isolate the cross terms. No c,d,g terms survive. In characteristic two the branches h≠0, h=0 with a≠0, and h=a=0 yield C₁,C₃,C₂. Conversely each component satisfies the equations, and each has points outside the other two. The nonlinear factors are the irreducible hypersurfaces of singular 2×2 matrices (rank at most one); both and the linear component have dimension seven after adjoining their free coordinates. In odd characteristic splitting further by j in the h=a=0 branch gives D₅ for j≠0 and ei=0 for j=0, yielding the other two branches D₂ and D₃; the h≠0 and a≠0 branches give D₁ and D₄. All linear spaces satisfy the equations and their defining coordinate sets show pairwise non-containment. Disjoint branch counts give 2(q−1)q⁶+q⁴(q³+q²−q) in characteristic two and (q−1)q⁵+2(q−1)q⁴+q⁵(2q−1) otherwise, exactly the two displayed formulas. Independent enumeration gave 288, 2025, 44032 and 45625 over GF(2), GF(3), GF(4), GF(5), with direct double-bracket checks exhaustive over GF(2) and bounded over the other fields. Replay: python3 /workspace/branches/97ccf369-dd22-4370-85ec-1ca662bcdeaf/independent_sandwich_check.py. The supplied verify.py was inspected, not executed; its GF(4) operator loop has 2048 iterations but at most four distinct inputs since all extracted coefficients depend only on the initial seed modulo four. Its exhaustive seven-coordinate GF(4) equation/component check has no such restriction. The general proof is symbolic and establishes the reduced locus, not scheme-theoretic radicality.

## originality

PASS

The prior sandwich definition and the triangular and commuting-variety tools are credited. The inspected statements do not give the exact reduced decomposition and rational-point census of the single-element adjoint-square locus in both characteristics. The closest uninspected upper-triangular paper remains a named access risk rather than negative evidence. The assessment concerns only the stated reduced geometry and counts, not general priority for sandwich theory.

## value

PASS

This gives the full reduced geometry and exact point count of a natural degeneracy locus, with a change in both dimensions and component type. The size is meaningful: for n≤4 in characteristic two the noncentral entries of X² impose only monomial vanishing, whereas n=5 is the first size with noncentral two-term equations from the third superdiagonal. The determinant cones and the loss of the 2XYX term explain the jump, rather than merely supplying a small-field count or a sample of orbits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
