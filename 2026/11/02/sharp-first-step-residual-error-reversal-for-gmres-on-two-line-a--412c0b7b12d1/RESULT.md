# Sharp first-step residual–error reversal for GMRES on two-line alternating projections

## Finding

Let two nonorthogonal, distinct lines in the real Euclidean plane meet at the origin. From a unit vector on the first line, perform either one ordinary alternating-projection sweep (project onto the first line, then onto the second) or one residual-minimizing GMRES step applied to the fixed-point equation for that same sweep. **At every nontrivial principal angle, GMRES strictly reduces the fixed-point residual relative to the sweep yet strictly increases the Euclidean distance to the common intersection.** The sharp amplification of the latter error, relative to one sweep, is
\[
\sqrt{\frac{119+21\sqrt{21}}{200}}=1.03738635424338\ldots,
\]
attained at squared line-cosine \(z_*=(5-\sqrt{21})/2\). Despite the adverse first-step solution error, unrestarted GMRES terminates after at most two steps, while repeated alternating projections approach the intersection without finite termination for this nontrivial configuration. This is a finite-horizon comparison of two specific algorithms, not a claim that GMRES converges more slowly overall.

## Assumptions and scope

Work over \(\mathbb R^2\) with the standard Euclidean norm, exact arithmetic, and two distinct nonorthogonal one-dimensional subspaces
\[
M_1=\operatorname{span}\{(1,0)^\top\},\qquad
M_2=\operatorname{span}\{(c,s)^\top\},\quad
0<c<1,\quad s=\sqrt{1-c^2}>0.
\]
Put \(z=c^2\in(0,1)\), and let \(P_i\) be the orthogonal projector onto \(M_i\). The common intersection is \(\{0\}\). Define the alternating-projection operator \(T=P_2P_1\) and \(A=I-T\). Start at \(x_0=(1,0)^\top\). One ordinary sweep is \(x_{\mathrm{AP}}=Tx_0\); one *unrestarted, conventional Euclidean-residual* GMRES step for the homogeneous nonsingular linear system \(Ax=0\), from \(x_0\), is \(x_{\mathrm G}=x_0-\alpha Ax_0\), where \(\alpha\in\mathbb R\) minimizes \(\|A(x_0-\alpha Ax_0)\|_2\). Measure solution error by distance to \(M_1\cap M_2\), equal here to \(\|x\|_2\), and fixed-point residual by \(\|Ax\|_2\).

## Proof

Direct multiplication gives
\[
T=\begin{pmatrix}z&0\\cs&0\end{pmatrix},\quad
A=\begin{pmatrix}1-z&0\\-cs&1\end{pmatrix},\quad
x_{\mathrm{AP}}=\begin{pmatrix}z\\cs\end{pmatrix}.
\]
Write \(w=Ax_0=((1-z),-cs)^\top\). Then
\[
Aw=\big((1-z)^2,-cs(2-z)\big)^\top,
\quad w^\top Aw=1-z,
\quad\|Aw\|_2^2=(1-z)(1+z-z^2).
\]
Because \(0<z<1\), this normal equation uniquely determines \(\alpha=1/D\), with \(D=1+z-z^2>1\). Consequently
\[
x_{\mathrm G}=
\frac1D\begin{pmatrix}z(2-z)\\cs\end{pmatrix}.
\]
The ordinary sweep has \(\|x_{\mathrm{AP}}\|_2^2=z\) and \(\|Ax_{\mathrm{AP}}\|_2^2=z(1-z)^2\). Expanding the GMRES vector and substituting \(c^2=z\), \(s^2=1-z\) gives the two *exact* ratios
\[
\frac{\|x_{\mathrm G}\|_2^2}{\|x_{\mathrm{AP}}\|_2^2}
=1+\frac{z(1-z)^3}{(1+z-z^2)^2}>1,
\qquad
\frac{\|Ax_{\mathrm G}\|_2^2}{\|Ax_{\mathrm{AP}}\|_2^2}
=\frac1{1+z-z^2}<1.
\]
Thus, at every allowable angle, a strictly better fixed-point residual coincides with strictly worse Euclidean solution error. Let \(f(z)=z(1-z)^3/(1+z-z^2)^2\). Elementary differentiation yields
\[
f'(z)=\frac{(1-z)^2(z^2-5z+1)}{(1+z-z^2)^3}.
\]
The quadratic has exactly one root in \((0,1)\), \(z_*=(5-\sqrt{21})/2\); the derivative changes from positive to negative there. Since \(f(0)=f(1)=0\) in the continuous endpoint extension, this is the unique global maximizer. Exact substitution gives \(f(z_*)=(21\sqrt{21}-81)/200\), and hence the claimed sharp error ratio \(\sqrt{(119+21\sqrt{21})/200}\). Also \(D\le5/4\), with equality only at \(z=1/2\); the sharp minimum residual ratio is therefore \(2/\sqrt5\).

For finite termination, \(\det(w,Aw)=-cs^3\ne0\). Hence the first two Krylov vectors span \(\mathbb R^2\), and full two-step GMRES contains \(0\) in its feasible affine space and returns the exact intersection vector. By contrast, \(T^k x_0=z^{k-1}(z,cs)^\top\) for each integer \(k\ge1\); because \(0<z<1\), it never vanishes at a finite iteration. Every equality and strict inequality above concerns the exact specified two-line configuration; no density, sampling, or asymptotic argument is needed.

## Verification

A standalone Python 3 standard-library checker, `verify.py`, evaluates the GMRES normal equation, both competing outputs, exact error and residual identities, and two-dimensional Krylov nondegeneracy for 2,485 rational unit-circle parameterizations. It also checks the algebraic maximizing value and 9,999 supplementary grid points. Run from the same directory with `python3 verify.py`, which reports `VERIFICATION_OK`. The proof's derivative sign analysis, not the finite grid, establishes the sharp all-angle statement.

## Relationship to prior work

Lerman and Zhang [1] analyze convergence of windowed Anderson acceleration on affine contractions, with explicit links between Anderson-type acceleration and GMRES. Their general results do not imply that improving the *fixed-point residual* improves Euclidean distance to the fixed point after one step: this statement separates the two metrics for the particular product of two orthogonal line projections and calculates their exact sharp competition. The classical GMRES method [2] minimizes residual rather than solution error; its fundamental definition alone does not provide the present two-algorithm, all-angle comparison. Bauschke, Deutsch, Hundal and Park [3] study acceleration of alternating projections by a **different extrapolation method**; their convergence acceleration is not a contradictory claim about one-step GMRES residual minimization. The spectral and principal-angle identities for two subspaces are classical and are not claimed as new. The asserted contribution is the explicit strict residual–error reversal, its sharp geometric constant, and the matched finite-horizon versus two-step termination behavior.

## Limitations

The theorem concerns exactly two one-dimensional subspaces of \(\mathbb R^2\), a unit starting vector on the first line, Euclidean-residual GMRES on \(I-P_2P_1\), one-step comparison, and exact arithmetic. Orthogonal or identical lines are excluded from the strict comparison. Changing initialization, ordering, acceleration variant, norm, or adding more subspaces may change the result. The maximum relative one-step Euclidean penalty is about \(3.74\%\); no claim of a large absolute penalty, no claim of an intrinsic GMRES instability, and no claim of a general complexity lower bound is made. Historical priority beyond the specifically compared material has not been exhaustively established.

## References

[1] G. Lerman and T. Zhang, *When Windowed Anderson Acceleration Converges Faster*, arXiv:2610.30073v1, first submitted 2026-10-21, https://arxiv.org/html/2610.30073v1 .

[2] Y. Saad and M. H. Schultz, *GMRES: A Generalized Minimal Residual Algorithm for Solving Nonsymmetric Linear Systems*, SIAM Journal on Scientific and Statistical Computing 7 (1986), 856–869, https://doi.org/10.1137/0907058 .

[3] H. H. Bauschke, F. Deutsch, H. Hundal and S.-H. Park, *Accelerating the convergence of the method of alternating projections*, Transactions of the American Mathematical Society 355 (2003), 3433–3461, https://doi.org/10.1090/S0002-9947-03-03136-2 .
