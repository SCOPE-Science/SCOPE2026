# Sharp diagonal and off-diagonal amplification in two-by-two semidefinite projection

## Finding

Let \(\mathbb S^2\) be the real symmetric \(2\times2\) matrices. Write \(\Pi(X)\) for the Frobenius-nearest positive-semidefinite matrix and \(\|X\|_{\max}=\max_{i,j}|X_{ij}|\). Define the global entrywise modulus and the single-entry moduli by
\[
L=\sup_{X\ne Y}\frac{\|\Pi(X)-\Pi(Y)\|_{\max}}{\|X-Y\|_{\max}},\qquad
L_{ij}=\sup_{X\ne Y}\frac{|\Pi(X)_{ij}-\Pi(Y)_{ij}|}{\|X-Y\|_{\max}}.
\]
Then the exact sharp constants are
\[
\boxed{L=L_{11}=L_{22}=\tfrac32,\qquad L_{12}=L_{21}=\tfrac98.}
\]
All these suprema are **unattained by any distinct finite pair**. The diagonal amplification of \(3/2\) is approached at equal-diagonal rank-one matrices; the off-diagonal amplification of \(9/8\) is approached at rank-one matrices whose normalized off-diagonal magnitude equals \(1/2\). For every \(n\ge2\), block embedding consequently gives the lower bound \(L_n\ge3/2\) for the analogous entrywise modulus of Frobenius projection onto \(\mathbb S^n_+\); no higher-dimensional equality is asserted.

## Assumptions and scope

The matrices are **real and symmetric**; input and output are measured using the maximum of the absolute matrix entries, **not** the matrix \(\infty\)-induced row-sum norm. The nearest-point optimization uses the **Frobenius** norm, not the entrywise norm. All input matrices are allowed, without trace, correlation-diagonal, rank, or entrywise positivity restrictions. The spectral positive part \(\Pi(X)=X_+\) is uniquely defined.

## Proof

**1. Exact projection.** Write
\[
X=\begin{pmatrix}m+d&z\\z&m-d\end{pmatrix},\qquad r=(d^2+z^2)^{1/2}.
\]
The eigenvalues are \(m\pm r\). If \(m\ge r\), then \(\Pi(X)=X\); if \(m\le-r\), then \(\Pi(X)=0\). In the mixed-sign region \(-r<m<r\), with \(r>0\),
\[
\Pi(X)=\frac{m+r}{2}
\begin{pmatrix}1+d/r&z/r\\z/r&1-d/r\end{pmatrix}.
\]
By swapping the two coordinate axes and conjugating by \(\operatorname{diag}(1,-1)\), which preserve the two norms and interchange the diagonal outputs, it suffices to analyze \(\Pi_{11}\) and \(\Pi_{12}\) with \(c=d/r\ge0\), \(s=z/r\ge0\), \(c^2+s^2=1\), and \(t=m/r\in(-1,1)\).

**2. Diagonal derivative.** For inputs \(x=m+d\), \(y=m-d\), and \(z\), direct differentiation yields
\[
\frac{\partial\Pi_{11}}{\partial x}=
\frac{(1+c)^2+(1+t)(1-c^2)}4,\quad
\frac{\partial\Pi_{11}}{\partial y}=-\frac{t(1-c^2)}4,\quad
\frac{\partial\Pi_{11}}{\partial z}=\frac{s(1-tc)}2.
\]
The first and third coefficients are nonnegative. Their absolute row sum is therefore
\[
R_{11}(c,t)=
\begin{cases}
(1+c+s+t(s^2-cs))/2,&0\le t\le1,\\
(1+c+s-tcs)/2,&-1\le t\le0.
\end{cases}
\]
Each branch is affine in \(t\), so its maximum is bounded by the three endpoints \(t=-1,0,1\). At these endpoints,
\[
R_{11}(c,-1)=\frac{(1+c)(1+s)}2
\le\frac{3/2+\sqrt2}{2}<\frac32,
\]
using \(c+s\le\sqrt2\), \(cs\le1/2\);
\[
R_{11}(c,0)=\frac{1+c+s}{2}\le\frac{1+\sqrt2}{2}<\frac32,
\]
and
\[
R_{11}(c,1)=1+\frac{(1-c)(c+s)}2
\le1+\frac{(1-c)(1+c)}2\le\frac32.
\]
The last inequality uses \(s\le1\) and has equality **only** when \(c=0,s=1,t=1\). Accordingly, throughout the open mixed-sign region, \(R_{11}<3/2\); its supremum is \(3/2\). The same bound holds for \(\Pi_{22}\) by exchanging axes.

**3. Off-diagonal derivative.** Correct differentiation of \(\Pi_{12}=z/2+mz/(2r)\) gives
\[
\frac{\partial\Pi_{12}}{\partial x}=\frac{s(1-tc)}4,\quad
\frac{\partial\Pi_{12}}{\partial y}=\frac{s(1+tc)}4,\quad
\frac{\partial\Pi_{12}}{\partial z}=\frac{1+tc^2}{2}.
\]
All three are nonnegative for \(-1\le t\le1\). Hence
\[
R_{12}(c,t)=\frac{s+1+tc^2}{2}\le
\frac{s+1+c^2}{2}=1+\frac{s-s^2}{2}\le\frac98.
\]
The last bound is sharp exactly at \(s=1/2\), \(t=1\) (with \(c=\sqrt3/2\)). It is strict in the open mixed-sign region. In the positive-definite and negative-definite regions the derivatives are the identity and zero, respectively, so the same coordinatewise bounds hold there.

**4. Global bounds and nonattainment.** The map \(X\mapsto X_+\) is continuous and locally Lipschitz; this follows directly from its spectral formula or from Hilbert-space metric-projection nonexpansivity. On a line segment not entirely contained in the singular determinant surface, only finitely many segment parameters have determinant zero. On each remaining open subinterval the applicable derivative row sum has the stated upper bound, and is **strictly** below that bound. Integration proves strict inequalities for each nonzero segment difference. If the determinant vanishes identically on a segment, then all its nonzero matrices are scalar multiples of a fixed rank-one symmetric matrix (two independent real symmetric rank-one matrices cannot span a determinant-zero affine line). On this line the positive-part map is scalar positive-part multiplication along a fixed matrix, hence is \(1\)-Lipschitz in entrywise maximum norm. Thus neither \(3/2\) nor \(9/8\) is realized by distinct inputs; both are valid global sharp suprema.

**5. Sharp perturbations.** For the diagonal entry, set
\[
A=\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
B_\varepsilon=A+\varepsilon\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad\varepsilon>0.
\]
Then \(\|B_\varepsilon-A\|_{\max}=\varepsilon\), \(\Pi(A)=A\), and with \(r_\varepsilon=(1+2\varepsilon+2\varepsilon^2)^{1/2}\),
\[
\Pi(B_\varepsilon)_{11}=\frac{(1+r_\varepsilon)(r_\varepsilon+\varepsilon)}{2r_\varepsilon},\qquad
\lim_{\varepsilon\downarrow0}\frac{\Pi(B_\varepsilon)_{11}-1}{\varepsilon}=\frac32.
\]
For the off-diagonal entry, put
\[
C=\begin{pmatrix}1+\sqrt3/2&1/2\\1/2&1-\sqrt3/2\end{pmatrix},\qquad
D_\varepsilon=C-\varepsilon\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]
For small positive \(\varepsilon\), \(D_\varepsilon\) has eigenvalues of opposite sign and, writing \(q_\varepsilon=(1-\varepsilon+\varepsilon^2)^{1/2}\),
\[
\Pi(D_\varepsilon)_{12}
=\frac{(1-\varepsilon+q_\varepsilon)(1/2-\varepsilon)}{2q_\varepsilon},\qquad
\lim_{\varepsilon\downarrow0}\frac{1/2-\Pi(D_\varepsilon)_{12}}{\varepsilon}=\frac98.
\]
The two limits complete all sharpness assertions. A block-diagonal embedding, with zeros in unused rows and columns, proves the higher-dimensional lower bound.

## Verification

Run `python3 verify.py` using the Python 3 standard library. It uses exact rational dual-number differentiation at Pythagorean parameter points, tests the derived Jacobian formulas and local bounds, and checks both perturbative sharpness limits numerically at 70-digit precision. The complete program reports **407 passed assertions**. It is an independent algebraic check of the local formulas, not a substitute for the parameter-uniform inequalities or the global integration argument supplied above.

## Relationship to prior work

Higham (1988) provides the general Frobenius nearest-semidefinite matrix formula; Malick–Sendov (2006) gives the Clarke generalized Jacobian in all dimensions; Šilhavý (2015) develops further geometric projection-derivative formulas. The present claim is not their projection formula or generalized derivative, but the **exact entrywise maximum-norm optimization**, its distinct diagonal/off-diagonal sharp values, and finite-pair nonattainment. A previous exact result for standard Lorentz-cone projection under the standard coordinate maximum norm does not subsume the statement: the linear isometry sending \((m,d,z)\) to \(\begin{psmallmatrix}m+d&z\\z&m-d\end{psmallmatrix}\) changes the coordinate maximum norm to \(\max\{|m|+|d|,|z|\}\), not \(\max\{|m|,|d|,|z|\}\). No uniqueness of publication priority follows from a negative literature search.

## Limitations

Only real symmetric \(2\times2\) matrices are completely classified. The lower bound for larger matrices is not asserted optimal. There is no extension here to complex Hermitian inputs, nearest correlation matrices, other coordinate weightings, or projections defined in a different objective norm. The 2015 source's full text could not be retrieved, so an earlier equivalent entrywise calculation there or in unindexed literature remains a priority risk. Day-level source dating is based on a verified repository deposit; an earlier journal publication is known but its original public calendar day was not established.

## References

1. N. J. Higham, *Computing a nearest symmetric positive semidefinite matrix*, Linear Algebra Appl. **103** (1988), 103–118. DOI: 10.1016/0024-3795(88)90223-6. Repository record: https://eprints.maths.manchester.ac.uk/363/ (deposit date 2006-07-05).
2. J. Malick and H. S. Sendov, *Clarke generalized Jacobian of the projection onto the cone of positive semidefinite matrices*, Set-Valued Analysis **14** (2006), 273–293. DOI: 10.1007/s11228-005-0005-1. Author manuscript: https://www.stats.uwo.ca/faculty/hssendov/Publications/CGJPCPSDM.pdf.
3. M. Šilhavý, *Differentiability of the metric projection onto a convex set with singular boundary points*, J. Convex Anal. **22** (2015), 969–997. DOI: 10.68381/jca22052. Abstract: https://journalofconvexanalysis.com/articles/jca22052/.
