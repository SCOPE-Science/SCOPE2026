# Sharp two-sided perturbation envelopes for operator-woven orthonormal bases

## Finding
Fix an integer \(m\ge2\) and \(t\ge0\). Consider an orthonormal basis \(F=(e_j)_{j\in J}\) in any complex Hilbert space \(H\), and \(m\) invertible bounded operators \(U_1,\dots,U_m\) satisfying
\[
U_1=I_H,\qquad \|U_i-I_H\|\le t\quad(2\le i\le m).
\]
For every partition \((\sigma_i)_{i=1}^m\) of \(J\), choose the weaving
\[
\mathcal W_\sigma=\{U_i e_j:j\in\sigma_i,\ 1\le i\le m\}.
\]
Let \(S_\sigma\) be its positive Bessel frame operator, whether or not its lower frame bound is positive. Taking the infimum of its optimal lower constant over all such spaces, operators and partitions, and the supremum of its optimal upper constant over the same class, gives exactly
\[
\boxed{L_m(t)=\bigl(\max\{0,1-\sqrt{m-1}\,t\}\bigr)^2},
\qquad
\boxed{U_m(t)=\bigl(1+\sqrt{m-1}\,t\bigr)^2}.
\]
Both extremal functions are exact for every \(m,t\), not just asymptotic bounds. A single rank-one construction attains both endpoints below the critical radius. For every \(m\ge3\), the critical radius is attained by families in which **each individual transformed basis remains a Riesz basis but one weaving fails to span**.

## Assumptions and scope
The base frame is an orthonormal basis. The operators \(U_i\) are required to be bounded and invertible; thus all individual source sequences \(U_iF\) are Riesz bases. The index set may be finite or countably infinite, and the extremal problems range over all allowed Hilbert-space dimensions and partitions. Empty partition classes are allowed, but the sharp constructions below use a partition with **every class nonempty**.

Write \(r=m-1\) and \(x_+=\max\{x,0\}\). Precisely,
\[
L_m(t)=\inf_{H,F,(U_i),\sigma}\inf_{\|f\|=1}
\sum_{i=1}^{m}\sum_{j\in\sigma_i}|\langle f,U_i e_j\rangle|^2,
\]
\[
U_m(t)=\sup_{H,F,(U_i),\sigma}\sup_{\|f\|=1}
\sum_{i=1}^{m}\sum_{j\in\sigma_i}|\langle f,U_i e_j\rangle|^2.
\]
No uniform lower frame bound is presupposed for the weavings; this is what the first extremum measures.

## Proof
**Universal bounds.** Identify \(H\) isometrically with the coefficient space \(\ell^2(J)\) through the orthonormal basis. Let \(C_0:H\to\ell^2(J)\) be the unperturbed analysis map and \(C_\sigma\) the weaving analysis map. If \(j\in\sigma_i\), their coefficient difference at \(f\) is
\[
\langle f,(U_i-I_H)e_j\rangle
=\langle (U_i-I_H)^*f,e_j\rangle
\]
(up to the harmless choice of inner-product linearity convention). The difference vanishes on \(\sigma_1\). Orthogonality of the coefficient coordinate sets gives
\[
\begin{aligned}
\|(C_\sigma-C_0)f\|^2
&=\sum_{i=2}^m\sum_{j\in\sigma_i}
|\langle (U_i-I_H)^*f,e_j\rangle|^2\\
&\le\sum_{i=2}^m\|(U_i-I_H)^*f\|^2
\le r t^2\|f\|^2.
\end{aligned}
\]
Since \(\|C_0f\|=\|f\|\), the triangle and reverse-triangle inequalities imply
\[
(1-\sqrt r\,t)_+\|f\|\le\|C_\sigma f\|
\le(1+\sqrt r\,t)\|f\|.
\]
Squaring proves the asserted universal lower and upper estimates and the existence of all upper Bessel bounds.

**Exact extremizers.** Set \(H=\mathbb C^m\) with its canonical basis and
\[
h=\frac{e_1+\cdots+e_r}{\sqrt r}.
\]
For each sign \(\epsilon\in\{-1,+1\}\), define
\[
U_1=I_H,\qquad U_{j+1}=I_H+\epsilon a\,|h\rangle\langle e_j|
\quad(1\le j\le r).
\]
Every rank-one difference has operator norm exactly \(a\). Take the nonempty partition
\[
\sigma_1=\{m\},\qquad \sigma_{j+1}=\{j\}\quad(1\le j\le r).
\]
The chosen synthesis map sends \(e_j\) to \(e_j+\epsilon a h\) for \(j\le r\) and fixes \(e_m\); equivalently,
\[
T_\sigma=I_H+\epsilon a\sqrt r\,|h\rangle\langle h|.
\]
Because \(|h\rangle\langle h|\) is an orthogonal rank-one projection, the singular values are \(1\) on \(h^\perp\) and \(|1+\epsilon a\sqrt r|\) on \(\mathbb Ch\). The choice \(\epsilon=+1\), \(a=t\) gives exact optimal upper energy \((1+t\sqrt r)^2\). All these \(U_i\) are invertible: each rank-one update has determinant \(1+a/\sqrt r>0\).

For \(0\le t<1/\sqrt r\), choose \(\epsilon=-1\), \(a=t\). Then all \(U_i\) are invertible (indeed \(a<1\)), and the weaving attains the lower bound \((1-t\sqrt r)^2\).

If \(r\ge2\) and \(t\ge1/\sqrt r\), choose \(\epsilon=-1\), \(a=1/\sqrt r\). Every individual operator is still invertible, with rank-one determinant
\[
1-\frac1r>0.
\]
But \(T_\sigma h=0\), so the weaving is incomplete and the optimal lower bound is \(0\). This attains the remaining lower envelope.

For \(r=1\) and \(t\ge1\), use \(\epsilon=-1\) and any \(0\le a<1\) approaching \(1\). Every operator remains invertible and the selected weaving has optimal lower bound \((1-a)^2\to0\). Thus the **infimum** is zero, without claiming its attainment in the invertible class.

**First nontrivial singular weaving.** For \(m=3\), set \(r=2\), \(a=1/\sqrt2\), and use the explicit matrices
\[
U_1=I_3,\quad
U_2=\begin{pmatrix}1/2&0&0\\-1/2&1&0\\0&0&1\end{pmatrix},\quad
U_3=\begin{pmatrix}1&-1/2&0\\0&1/2&0\\0&0&1\end{pmatrix}.
\]
Both nontrivial operators have determinant \(1/2\) and distance \(1/\sqrt2\) from \(I_3\). The weaving with source \(2\) at coordinate \(1\), source \(3\) at coordinate \(2\), and source \(1\) at coordinate \(3\) has first two vectors opposite, so is incomplete despite all three complete source bases.

## Verification
The proof is analytic for every integer \(m\ge2\); no finite enumeration is used to infer an infinite assertion. The coefficient-difference identity supplies the bounds for arbitrary separable Hilbert spaces. The extremal matrices have exact rank-one spectra, so the equality and critical cases are also exact.

An independent exact symbolic calculation for dimensions \(m=2,3,4,5\) verified that the selected lower synthesis maps at half the critical radius have squared singular values \(1/4\) and \(1\), and that at the critical radius their ranks drop by one. This computation is a finite consistency check only; the general proof is the rank-one projection formula above.

## Relationship to prior work
Li--Jiang--Xu's *On weaving frames in Hilbert spaces*, Theorem 4 (Theorem 2.7 in the 2019 preprint), gives a perturbation radius proportional to \(1/\sqrt{m-1}\) for multiple operator images of one frame. Its theorem is framed as a **sufficient** condition, not an optimality classification. An independent analysis of the distinction between left and right inverses supplies a valid perturbation lower estimate when the reference operator is surjective; that estimate **does not imply the existence of any extremizing family**.

The present statement closes precisely that sharpness gap in the canonical identity/orthonormal-basis model: it determines **both** optimal envelopes for **all** radii, supplies finite-dimensional rank-one equality constructions, and proves loss of wovenness at the critical radius for \(m\ge3\) even though every individual source sequence remains a Riesz basis. Neither the published sufficient estimate nor its corrected form establishes these extremal facts.

Calderón--Ruiz's *On perturbations of woven pairs of frames* treats **two** frames and stability under analysis/synthesis perturbations, and its operator result gives a sufficient closeness condition for a woven pair. Xiang's work on perturbation of woven \(K\)-\(g\)-frame **pairs** has a different, operator-valued setting. These results do not state the exact multiplicity-dependent minimax profile for \(m\) transformed copies of an orthonormal basis.

## Limitations
These are exact universal constants for an orthonormal base frame and reference operator \(I_H\), not a claim about optimal constants for arbitrary nontight frames or arbitrary surjective reference operators. The extremal quantities range over Hilbert-space dimensions; a fixed dimension smaller than \(m-1\) may obey sharper bounds.

For \(m=2\) at radius \(t\ge1\), zero is the infimum but need not be attained within the class of **invertible** source operators. For \(m\ge3\), the zero lower envelope is attained by invertible sources at the critical radius itself.

An unindexed source may already describe these rank-one extremizers; no inference of novelty is drawn merely from the absence of a search result.

## References
1. D. Li, J. Jiang and Y. Xu, *On weaving frames in Hilbert spaces*, Operators and Matrices 17(3) (2023), 809--822, DOI 10.7153/oam-2023-17-53; first public preprint arXiv:1901.01360v1, 5 January 2019.
2. P. Calderón and M. Ruiz, *On perturbations of woven pairs of frames*, arXiv:2101.07351v1 (2021).
3. Z.-Q. Xiang, *Some new results on the weaving of \(K\)-\(g\)-frames in Hilbert spaces*, Open Mathematics 19(1) (2021), 1315--1329, DOI 10.1515/math-2021-0103.
