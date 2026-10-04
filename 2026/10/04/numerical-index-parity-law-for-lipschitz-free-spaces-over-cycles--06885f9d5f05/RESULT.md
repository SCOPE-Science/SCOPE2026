# Numerical-index parity law for Lipschitz-free spaces over cycles
## Finding
For every integer \(n\ge 6\), let \(C_n\) be the cycle on vertices \(v_0,\ldots,v_{n-1}\), give every edge length \(1\), and equip the vertex set with the induced shortest-path metric. Over the real scalars,
\[
n\!\left(\mathcal F(C_n)\right)=
\begin{cases}
1,& n\text{ even},\\[2mm]
\dfrac{n-2}{n-1},& n\text{ odd}.
\end{cases}
\]
Thus the numerical index of the Lipschitz-free space over a higher cycle has an exact parity law: every even cycle gives numerical index \(1\), while an odd cycle gives the strictly smaller value \((n-2)/(n-1)\).

## Assumptions and scope
All Banach spaces are real. The cycle has unit edge lengths and the shortest-path metric. The numerical index of a real Banach space \(X\) is
\[
n(X)=\inf\{v(T):T\in\mathcal L(X),\ \|T\|=1\},
\]
where
\[
v(T)=\sup\{|x^*(Tx)|:x\in S_X,\ x^*\in S_{X^*},\ x^*(x)=1\}.
\]
The claim is restricted to \(n\ge6\); no assertion about novelty of smaller cycles is included.

## Proof
Write \(e_0,\ldots,e_{n-1}\) for the standard basis of \(\ell_1^n\), \(\mathbf 1=(1,\ldots,1)\), and
\[
X_n=\ell_1^n/\operatorname{span}\{\mathbf 1\},
\]
with quotient map \(q\). We first identify \(\mathcal F(C_n)\) isometrically with \(X_n\). For a Lipschitz function \(f\) on the cycle, put
\[
b_i=f(v_i)-f(v_{i+1}),
\]
with indices read modulo \(n\). The edge increments satisfy \(\sum_i b_i=0\), every zero-sum increment vector integrates to a function on the cycle, and the graph metric gives
\[
\|f\|_{\mathrm{Lip}}=\max_i|b_i|.
\]
Hence \(\operatorname{Lip}_0(C_n)\) is isometric to
\[
H_n=\{b\in\mathbb R^n:\sum_i b_i=0\}\subset\ell_\infty^n.
\]
Since \(H_n^\perp=\operatorname{span}\{\mathbf1\}\) in the canonical \(\ell_1^n\)-\(\ell_\infty^n\) pairing, duality gives \(\mathcal F(C_n)\cong X_n\).

The quotient unit ball is
\[
B_{X_n}=\operatorname{conv}\{\pm q(e_i):0\le i<n\}.
\]
Each \(q(e_i)\) is exposed: the vector \(h\in H_n\) with \(h_i=1\) and \(h_j=-1/(n-1)\) for \(j\ne i\) has \(\|h\|_\infty=1\), takes value \(1\) on \(q(e_i)\), and has absolute value strictly below \(1\) on every other \(\pm q(e_j)\). Thus the extreme points of \(B_{X_n}\) are exactly these \(2n\) points.

The dual ball is
\[
B_{X_n^*}=H_n\cap[-1,1]^n.
\]
A vertex of this hyperplane section has at least \(n-1\) active coordinate constraints. If \(n=2k\) is even, its extreme points are exactly the sign vectors with \(k\) coordinates equal to \(1\) and \(k\) equal to \(-1\). Indeed, leaving one coordinate strictly inside \([-1,1]\) would force it to cancel an odd integer sum, which is impossible. If \(n=2k+1\) is odd, every extreme point has exactly one zero coordinate, while the remaining coordinates consist of \(k\) copies of \(1\) and \(k\) copies of \(-1\).

For \(u=q(a)\in X_n\) and an index \(i\), define
\[
c_i(u)=\max\{|\langle h,u\rangle|:h\in\operatorname{ext}B_{H_n},\ h_i=1\}.
\]
For a finite-dimensional polyhedral space, the numerical radius may be tested on extreme primal points and extreme norming dual points: for a fixed norming functional, the relevant linear functional attains its maximum on an extreme point of the corresponding face, and then the same argument in the dual face reduces to an extreme dual point. Consequently, if \(Tq(e_i)=u_i\), then
\[
\|T\|=\max_i\|u_i\|,\qquad v(T)=\max_i c_i(u_i).
\]

Assume first that \(n=2k\). For a representative \(a\), sort its coordinates. The quotient norm is the sum of the largest \(k\) coordinates minus the sum of the smallest \(k\) coordinates. The balanced sign vector that is \(1\) on the largest half and \(-1\) on the smallest half is norming. If its \(i\)-th coordinate is \(-1\), change its sign. Therefore
\[
c_i(u)=\|u\|
\]
for every \(u\in X_n\) and every \(i\). It follows that \(v(T)=\|T\|\) for every operator \(T\), hence \(n(X_n)=1\).

Now let \(n=2k+1\) be odd and set
\[
\alpha=\frac{n-2}{n-1}.
\]
Choose a representative \(a\) whose median coordinate value is \(0\). Then
\[
\|q(a)\|=\sum_j|a_j|=:S.
\]
Let \(p\), \(q\), and \(z\) be the numbers of positive, negative, and zero coordinates of \(a\). Median centering gives \(p,q\le k\). A norming extreme dual vector is obtained by fixing the signs on the nonzero coordinates to agree with \(a\), choosing one zero coordinate of the dual vector, and assigning signs to the remaining zero coordinates so that the total sum is zero; the parity and size conditions are exactly \(|p-q|\le z-1\) and \(p-q\equiv z-1\pmod 2\), both automatic from \(p,q\le k\). Hence a norming extreme dual vector can be chosen with nonzero \(i\)-th coordinate unless \(i\) is the unique zero median and there are exactly \(k\) positive and \(k\) negative coordinates. After a global sign change it then has \(h_i=1\), so \(c_i(q(a))=S\).

In the exceptional case, let
\[
\delta=\min\!\left(\min_{a_j>0}a_j,\ \min_{a_j<0}(-a_j)\right).
\]
Because there are \(2k=n-1\) nonzero coordinates, \(S\ge(n-1)\delta\). If the minimum is attained at a positive coordinate, take an extreme dual vector with \(h_i=1\), zero at that minimum coordinate, value \(1\) on the other positive coordinates, and value \(-1\) on all negative coordinates. If the minimum is attained at a negative coordinate, reverse the signs on the nonzero coordinates and put the unique dual zero at that minimum coordinate. In either case
\[
c_i(q(a))\ge S-\delta\ge\alpha S.
\]
Thus \(v(T)\ge\alpha\|T\|\) for every operator \(T\), so \(n(X_n)\ge\alpha\).

For sharpness, put \(\delta=1/(n-1)\) and
\[
w=(0,\underbrace{1,\ldots,1}_{k},\underbrace{-1,\ldots,-1}_{k}).
\]
For each \(i\), let \(a^{(i)}\) be the cyclic shift of \(\delta w\) whose zero coordinate is \(i\), and set \(u_i=q(a^{(i)})\). Every \(u_i\) has norm \(1\), and the cyclic shifts satisfy \(\sum_i u_i=0\). Since \(\sum_iq(e_i)=0\) is the only linear relation among the spanning vectors \(q(e_i)\), there is a well-defined operator \(T\) with
\[
Tq(e_i)=u_i.
\]
Its norm is \(1\). For every extreme dual vector with \(h_i=1\), the unique zero coordinate of \(h\) is different from \(i\), so at most \(n-2\) nonzero entries of \(a^{(i)}\) contribute. Hence
\[
|\langle h,u_i\rangle|\le(n-2)\delta=\alpha.
\]
Equality is obtained by placing the dual zero at one positive coordinate and matching the remaining signs, or symmetrically at one negative coordinate. Therefore \(c_i(u_i)=\alpha\) for every \(i\), and
\[
v(T)=\alpha.
\]
This proves the odd case and completes the parity formula.

## Verification
The proof is symbolic and covers every integer \(n\ge6\). A companion exact-rational checker, `verify_cycle_index.py`, independently enumerates the extreme dual patterns for \(6\le n\le10\), verifies the explicit odd-cycle witness for \(n=7,9\), checks the cyclic compatibility relation, and exhaustively tests the lower inequality for every coefficient vector in \(\{-1,0,1\}^7\). It prints

`WITNESS_OK n=6..10`

`LOWER_STRESS_OK n=7 coefficients={-1,0,1}`

These finite computations are sanity checks only; the infinite family is established by the proof above.

## Relationship to prior work
Cobollo, Guirao, and Montesinos initiated the systematic computation of numerical indices of Lipschitz-free spaces and gave an explicit formula for every two-dimensional Lipschitz-free space, equivalently for three-point metric spaces. Their result does not determine the higher cycle family considered here. Sain, Paul, Bhunia, and Bag developed a general extreme-point method for numerical indices of finite-dimensional polyhedral Banach spaces and computed several particular low-dimensional polyhedral families; their inspected results do not state the present quotient-hyperplane parity formula. Cúth, Doucha, and Titkos analyze cycle relations and isometries in Lipschitz-free spaces over graph metrics, but the inspected cycle material does not compute numerical indices.

The present result uses those themes but supplies an exact all-dimensional family law for higher cycles, including explicit extremal operators in every odd case.

## Limitations
The statement is for real scalars, unit-edge cycles, and \(n\ge6\). No complex-scalar analogue is proved. The exact-rational checker tests only finitely many small cases and is not used as a substitute for the general argument. Literature searches covered the directly relevant Lipschitz-free numerical-index paper, a general polyhedral numerical-index paper, graph-cycle Lipschitz-free literature, and targeted quotient/hyperplane terminology; an older equivalent computation under different Banach-space terminology remains a residual bibliographic risk.

## References
1. Ch. Cobollo, A. J. Guirao, V. Montesinos, “The numerical index of 2-dimensional Lipschitz-free spaces,” arXiv:2304.13183v1 (2023).
2. D. Sain, K. Paul, A. Bhunia, S. Bag, “On the numerical index of polyhedral Banach spaces,” arXiv:1809.04778 (2018).
3. M. Cúth, M. Doucha, T. Titkos, “Isometries of Lipschitz-free Banach spaces,” Journal of the London Mathematical Society 110 (2024), e70000, DOI 10.1112/jlms.70000.
