# Independent mathematical audit

## correctness

PASS

For a,b>-1 with Jacobi normalization P_n(1)=(a+1)_n/n!, the first extremum from the right is x_{1,1}=-1, x_{1,2}=(b-a)/(a+b+4), and x_{1,3}=(b-a+2R)/(a+b+6) with R²=(a+3)(b+3)/(a+b+5). Independently reconstructed degrees 2,3 via SymPy Jacobi polynomials and verified derivative vanishing and values M1=(b+1)/(a+1), M2=(b+2)/[(a+1)(a+b+4)], M3=2(b+3)[a-b+(a+b+4)R]/[(a+1)(a+2)(a+b+6)^2]. Positivity of parameters and the first-minimum sign justify exact two-inequality parameter tests. As a→-1+, multiplying each M_j by a+1 gives L1=b+1, L2=(b+2)/(b+3) and the stated radical L3; L2-L1 has sign opposite to b²+3b+1. The positive U,V difference of squares factors as -(b+2)(b+4)(b+5)^3(b³+7b²+14b+4), producing the unique bc≈-0.341032918083 and open b range ( (sqrt(5)-3)/2, bc) of first-pass/second-fail near a=-1. Independently checked a=-19/20,b=-3/8: M1=12.5, M2=1300/107≈12.14953 and M3≈12.17973, consistent with the exact rational R² certificate. The excluded a=-1 is never asserted.

## originality

PASS

Castillo arXiv:2608.01404 is the closest current normalized-Jacobi first-index relative-extremum work, with an all-degree theorem for a,b>-1/2, whereas the new open reversal region lies at a near -1. Wong–Zhang 1994 boundary-parameter (0,-1) and eventual-degree papers do not entail the exact interior first two tests; Castillo–Hang weighted Jacobi–Radau is a different weighted one-parameter family. An indexed Resultary first-discrete-threshold Jacobi–Radau result is not the same P_n^(a,b)/P_n^(a,b)(1) object. Current primary arXiv full text for Castillo remained unavailable and Oxford reported VPN disconnected; implicit discussion of finite tests is a priority risk, but no direct stronger covering theorem was verified.

## value

PASS

The n=1→2 and n=2→3 comparisons are the first nontrivial necessary conditions in a live all-degree monotonicity problem, not arbitrary chosen computations. Their exact two-parameter inequality boundaries and the strict open reversal near the natural singular Jacobi parameter a=-1 demonstrate that passing one natural necessary test is insufficient for the next. The algebraic cubic frontier and exact interior counterexample are independently useful even though the full all-degree parameter classification is unresolved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
