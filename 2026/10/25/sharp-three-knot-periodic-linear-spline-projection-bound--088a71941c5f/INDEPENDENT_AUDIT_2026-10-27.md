# Independent mathematical audit

## correctness

PASS

For positive a,b,c, the cyclic three-hat Gram matrix is G=(1/6)[[2(a+c),a,c],[a,2(a+b),b],[c,b,2(b+c)]]. The reproducing kernel K(x,y) is affine in evaluation x within each arc; convexity of ∫|K(x,y)|dy reduces the L∞ norm to three knots. Its knot-0 inverse row (A,−X,−Y)/D is verified by direct symbolic inversion, and ∫K=1 makes the norm 1+2 times its negative area Q. The proof exhausts X,Y≥0, X<0, Y<0; X,Y cannot both be negative. The displayed exact positive-coefficient polynomials R,T prove 2/3−Q>0 in the first and second regimes, with the third by symmetry. Independent SymPy algebra verified inverse identities and positive-denominator formulations; the degeneration (a,b,c)=(ε²,1,ε) has Q→2/3 exactly, while a=b=c yields 16/9. This proves a strict per-mesh norm <7/3 and unattained global supremum 7/3; no reliance on finite samples.

## originality

PASS

Passenbrunner, Orthogonal projectors onto spaces of periodic splines (arXiv:1608.06720v2, 2016), Theorem 1.4, explicitly proves a constant c_k independent of number and placement of knots, via Gram estimates; full primary PDF and proof Sections 1-3 inspected. It does not specify c_2=7/3 at exactly three knots or a nonattaining extremizing family. Nonperiodic results of Shadrin and Passenbrunner–Shadrin apply more broadly to interval knots but do not yield this exact periodic three-knot envelope. Best of knowledge PASS with residual historical finite-dimensional calculation risk.

## value

PASS

Three knots are the first genuinely variable-mesh finite-dimensional periodic degree-one projector. Determining the sharp 7/3 amplification, proving that no positive mesh attains it, and identifying a two-scale singular extremal geometry give a natural exact stability boundary not obtainable from qualitative mesh-independent boundedness alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
