# A two-mechanism reentrant stability law for a three-species antagonistic feedback loop

## Finding

**Theorem (complete one-link stability diagram).** Let \(d,a,b,c,e>0\) and let \(t\geq0\). Consider the real community matrix
\[
J(t)=\begin{pmatrix}
-d&a&-t\\
-b&-d&c\\
t&-e&-d
\end{pmatrix},
\qquad S=ab+ce,\qquad G=be-ac.
\]
Every interacting species pair has opposite-signed effects, and \(t\) is the common absolute strength of the third reciprocal interaction. Write **Hurwitz stable** when every eigenvalue of \(J(t)\) has strictly negative real part, and **unstable** when at least one eigenvalue has strictly positive real part.

The complete alternatives are as follows.

1. If \(-2d\sqrt{d^2+S}<G<4d\sqrt{4d^2+S}\), then \(J(t)\) is Hurwitz stable for every \(t\geq0\).
2. If \(G>4d\sqrt{4d^2+S}\), there are exactly two distinct positive transition values
\[
t_{\mathrm{osc},\pm}=\frac{G\pm\sqrt{G^2-16d^2(4d^2+S)}}{4d}.
\]
The matrix is unstable precisely between these values; elsewhere away from the transition points it is Hurwitz stable. In the unstable interval exactly two eigenvalues have positive real part, forming a complex-conjugate pair. At each transition the spectrum is \(-3d\) together with \(\pm i\sqrt{3d^2+S+t^2}\).
3. If \(G<-2d\sqrt{d^2+S}\), there are exactly two distinct positive transition values
\[
t_{\mathrm{real},\pm}=\frac{-G\pm\sqrt{G^2-4d^2(d^2+S)}}{2d}.
\]
The matrix is unstable precisely between them, with exactly one positive real eigenvalue. At each transition the matrix has a simple zero eigenvalue and its two other eigenvalues have strictly negative real part.
4. At either equality \(G=4d\sqrt{4d^2+S}\) or \(G=-2d\sqrt{d^2+S}\), there is one positive transition value, respectively \(G/(4d)\) or \(-G/(2d)\), where the matrix has a neutral spectral mode but no interval of instability. Everywhere else it is Hurwitz stable.

These alternatives exhaust all positive parameters and all \(t\geq0\). In particular, a *single increasingly strong reciprocal antagonistic pair* can destabilize an otherwise self-regulated three-species system and then restore its local stability, through either an oscillatory or a real-eigenvalue mechanism.

Three species are the minimum size for this effect among matrices having strictly negative diagonals and only reciprocal opposite-signed off-diagonal pairs: every such matrix whose undirected interaction graph is a forest is Hurwitz stable for all its permitted interaction magnitudes. This forest statement is an established diagonal-stability observation, included here to identify the sharp topology, not claimed as new.

Two exact witnesses, each with \(d=1\), are:

- **Oscillatory instability:** \((a,b,c,e)=(1,4,1,4)\). The unstable interval is
\[
\frac{15-\sqrt{33}}4<t<\frac{15+\sqrt{33}}4.
\]
- **Real-eigenvalue instability:** \((a,b,c,e)=(4,1,4,1)\). The unstable interval is
\[
\frac{15-3\sqrt{21}}2<t<\frac{15+3\sqrt{21}}2.
\]
Both witness intervals are nonempty, and each matrix is stable at \(t=0\) and again for all sufficiently large \(t\).

## Assumptions and scope

The finding concerns local linear stability of a continuous-time ecological community matrix with equal self-regulation \(-d\) and three reciprocal predator–prey (opposite-sign) pairs. The first two interaction pairs have independent positive magnitudes \(a,b,c,e\); the varied pair has magnitudes both equal to \(t\). This is a controlled *local-response* model, not a claim that an arbitrary ecological intervention keeps all nonlinear demographic parameters fixed.

For each value of \(t\), the matrix can be realized as the Jacobian at the strictly positive state \((1,1,1)\) of a generalized Lotka–Volterra system \(\dot x_i=x_i(r_i(t)+\sum_j J_{ij}(t)x_j)\), with \(r(t)=-J(t)(1,1,1)^\top\). Maintaining that fixed equilibrium across \(t\) in this realization changes the intrinsic growth vector. Accordingly, no claim about a one-parameter intervention with fixed intrinsic rates, global attraction, existence of nonlinear periodic orbits, or ecological persistence follows automatically.

At a neutral transition point the theorem describes the Jacobian spectrum only; it does not pronounce nonlinear asymptotic stability. When \(t=0\) the third pair is absent and the interaction graph is a path.

## Proof

**Step 1: characteristic polynomial.** Direct expansion about the common diagonal term gives
\[
\det(\lambda I-J(t))=(\lambda+d)^3+(S+t^2)(\lambda+d)+Gt.
\]
Consequently its monic cubic form is
\[
\lambda^3+3d\lambda^2+(3d^2+S+t^2)\lambda+
\left[d(d^2+S+t^2)+Gt\right].
\]
Write \(A_2=3d\), \(A_1=3d^2+S+t^2\), \(A_0=d(d^2+S+t^2)+Gt\). Because \(A_2,A_1>0\), the cubic Routh–Hurwitz criterion says that the matrix is Hurwitz stable if and only if \(A_0>0\) and \(A_2A_1-A_0>0\). Their exact forms are
\[
U(t)=d(t^2+d^2+S)+Gt,
\qquad H(t)=2dt^2-Gt+2d(4d^2+S).
\]

**Step 2: cyclic imbalance of positive sign.** If \(G\geq0\), then \(U(t)>0\) for every nonnegative \(t\). The strictly convex quadratic \(H(t)\) can be nonpositive on positive \(t\) exactly when its minimum on that half-line is nonpositive. Its discriminant is
\[
G^2-16d^2(4d^2+S).
\]
Thus, if \(G>4d\sqrt{4d^2+S}\), exactly the two stated roots exist and \(H(t)<0\) exactly between them. Otherwise \(H(t)>0\) everywhere, except for one double zero at equality. Routh's first-column signs for \(H(t)<0\) are \((+,+,-,+)\), giving exactly two right-half-plane roots; real coefficients force a conjugate pair. At \(H=0\), the cubic factors as \((\lambda+3d)(\lambda^2+A_1)\). This proves the oscillatory alternative, including neutral boundary eigenvalues.

**Step 3: cyclic imbalance of negative sign.** If \(G\leq0\), then \(H(t)>0\) for all nonnegative \(t\). The quadratic \(U(t)\) has two distinct positive roots if and only if
\[
-G>2d\sqrt{d^2+S}.
\]
When this holds, \(U(t)<0\) precisely between them. Routh's first-column signs are \((+,+,+,-)\), so there is exactly one right-half-plane eigenvalue. As the characteristic polynomial has exactly one positive real root by Descartes' rule of signs, this eigenvalue is real. At \(U=0\), the factorization is \(\lambda(\lambda^2+3d\lambda+A_1)\), giving the stated simple zero and a stable complementary quadratic. At equality, the discriminant zero gives one neutral contact without instability. Together with Step 2 this completes the all-parameter classification.

**Step 4: explicit witnesses and sharp network size.** For \(d=1\), \((a,b,c,e)=(1,4,1,4)\) gives \(S=8\), \(G=15\), \(U=t^2+15t+9\), and \(H=2t^2-15t+24\); the formula for the oscillatory interval follows. For \((a,b,c,e)=(4,1,4,1)\), \(S=8\), \(G=-15\), \(U=t^2-15t+9\), and \(H=2t^2+15t+24\), giving the real-eigenvalue interval.

For completeness, consider any finite forest of reciprocal opposite-signed interactions, with diagonal entries \(-d_i<0\). Fix a positive vertex weight at each component root, then recursively choose positive weights \(w_j\) along each edge so that \(w_iJ_{ij}=-w_jJ_{ji}\). Acyclicity makes this consistent. The diagonal matrix \(W=\operatorname{diag}(w_i)\) then obeys
\[
WJ+J^\top W=-2\operatorname{diag}(w_i d_i)\prec0.
\]
Hence its community matrix is Hurwitz stable by a strict quadratic Lyapunov function. This known forest barrier rules out any two-species example and places the first possible cycle at three species; the explicit three-species witnesses attain it.

## Verification

The included `verify.py` performs symbolic, exact-coefficient checks of the determinant expansion, Routh determinants, both threshold equations, the factorization at neutral boundaries, and all witness polynomials. It further computes characteristic-polynomial and stability-sign comparisons on a deterministic rational parameter grid, including oscillatory and real-eigenvalue examples. Its assertions verify finite and symbolic algebraic identities only; the inequalities and all-real-parameter quantifiers are proven in the foregoing argument.

Run with `python verify.py` in an environment with Python 3 and SymPy. No private files or external services are needed.

## Relationship to prior work

The standard cubic Routh–Hurwitz criterion and diagonal Lyapunov stability of antagonistic trees are established tools. Solimano and Beretta (1982) prove stability for predator–prey trees and give **sufficient** conditions for stability of cyclic loops, including product-balanced cycles. The present theorem is an *exact necessary-and-sufficient one-link parameter diagram* within an equal-self-regulation three-cycle, resolving two different loss-and-return mechanisms, rather than a new proof of the tree theorem or of Routh–Hurwitz.

Allesina and Tang (2011, first public arXiv version) analyze how predator–prey sign pairing and network structure affect ecological stability, principally through large random-matrix ensembles, not this finite exact one-link diagram. The later review by Chen and colleagues discusses sign stability and feedback loops more generally. The preexisting Krikorian (1979) and Roy–Solimano (1987) three-species loop analyses are particularly close background. Their accessible bibliographic descriptions concern global behavior and oscillations; the full mathematical text was not available for a definitive implication check here. The claimed originality is therefore limited to the explicit parametric two-mechanism local classification above, and **possible stronger prior coverage is an unresolved bibliographic risk**.

## Limitations

The result is a linear local stability classification, not a theorem of nonlinear coexistence, global ecological stability, or a proof of actual limit cycles. Equal damping and symmetric magnitudes of the varied reciprocal pair are substantial modeling restrictions. The forest obstruction is classical rather than a new result. Because closely relevant 1979 and 1987 loop papers were not available in full, independent literature verification may find a prior theorem implying the present classification. All claims about originality are conditional on that bibliographic gap.

## References

1. F. Solimano and E. Beretta, *Graph theoretical criteria for stability and boundedness of predator-prey systems*, Bulletin of Mathematical Biology **44** (1982), 579–585, DOI: 10.1007/BF02459411. Accessible full text: https://im0.p.lodz.pl/~jbanasiak/Mag11/solimano.pdf
2. S. Allesina and S. Tang, *Stability criteria for complex ecosystems*, arXiv:1105.2071, first submitted 2011-05-10. Full text: https://ar5iv.labs.arxiv.org/html/1105.2071
3. N. Krikorian, *The Volterra model for three species predator-prey systems: Boundedness and stability*, Journal of Mathematical Biology **7** (1979), 117–132, DOI: 10.1007/BF00276925. Abstract and bibliographic description inspected; full text unavailable.
4. A. B. Roy and F. Solimano, *Global stability and oscillations in classical Lotka–Volterra loops*, Journal of Mathematical Biology **24** (1987), 603–616, DOI: 10.1007/BF00275505. Abstract and bibliographic description inspected; full text unavailable.
5. C. Chen et al., *Stability of Ecological Systems: A Theoretical Review*, arXiv:2312.07737, full text: https://arxiv.org/html/2312.07737v2
