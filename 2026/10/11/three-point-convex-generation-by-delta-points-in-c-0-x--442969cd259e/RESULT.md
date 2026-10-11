# Three-point convex generation by Delta-points in \(c_0(X)\)
## Finding
Let \(X\) be a nonzero real Banach space containing a Delta-point. Write
\[
c_0(X)=\left\{(x_k)_{k\ge 1}:\ \|x_k\|\to0\right\},\qquad \|(x_k)\|=\sup_k\|x_k\|.
\]
Then every \(z\in B_{c_0(X)}\) is the arithmetic mean of three Delta-points of \(c_0(X)\). More precisely, there exist \(u^{(1)},u^{(2)},u^{(3)}\in\Delta_{c_0(X)}\) such that
\[
z=\frac{u^{(1)}+u^{(2)}+u^{(3)}}3.
\]
Thus a single Delta-point in \(X\) forces an exact equal-weight three-point convex generation of the entire unit ball of its \(c_0\)-sum.

## Assumptions and scope
All Banach spaces are real. A Delta-point is understood in the standard sense: \(d\in S_X\) is a Delta-point when, for every \(\varepsilon>0\), it belongs to the closed convex hull of the points of \(B_X\) at distance at least \(2-\varepsilon\) from \(d\).

The only non-elementary input is the coordinate-lifting fact used in Lemma 3 of arXiv:2609.28569v1: if \(w=(w_k)\in S_{c_0(X)}\) and one coordinate \(w_m\) is a Delta-point of \(X\), then \(w\) is a Delta-point of \(c_0(X)\). That fact is also a special case of Theorem 4.1(2)(d) of arXiv:2410.04706.

## Proof
Fix \(d\in\Delta_X\) and \(z=(z_k)\in B_{c_0(X)}\). Since \(z_k\to0\), choose three distinct indices \(m_1,m_2,m_3\) such that
\[
\|z_{m_j}\|\le \frac13\qquad(j=1,2,3).
\]
For each \(j\in\{1,2,3\}\), define
\[
q_j:=\frac{3z_{m_j}-d}2.
\]
Then
\[
\|q_j\|\le\frac{3\|z_{m_j}\|+\|d\|}2\le1.
\]
For \(r\in\{1,2,3\}\), define \(u^{(r)}\in c_0(X)\) by leaving all coordinates outside \(\{m_1,m_2,m_3\}\) equal to those of \(z\), and on the selected coordinates setting
\[
u^{(r)}_{m_j}=\begin{cases}d,&j=r,\\q_j,&j\ne r.\end{cases}
\]
Finite modification preserves membership in \(c_0(X)\). Every coordinate has norm at most one, while the \(m_r\)-coordinate equals \(d\) and hence has norm one. Therefore \(u^{(r)}\in S_{c_0(X)}\). By the coordinate-lifting fact, each \(u^{(r)}\) is a Delta-point of \(c_0(X)\).

For a selected coordinate \(m_j\), exactly one of the three vectors contributes \(d\) and the other two contribute \(q_j\). Hence
\[
\frac{d+2q_j}3=\frac{d+3z_{m_j}-d}3=z_{m_j}.
\]
All unselected coordinates agree with \(z\) in all three vectors. Thus
\[
z=\frac{u^{(1)}+u^{(2)}+u^{(3)}}3,
\]
as claimed.

## Verification
The proof uses no finite experiment, numerical approximation, or asymptotic inference. The norm estimate for each compensating coordinate is exact, the three selected indices exist because \(z\in c_0(X)\), and the barycentric identity is checked coordinate by coordinate.

The proof was stress-tested at the boundary \(\|z_{m_j}\|=1/3\): the estimate still gives \(\|q_j\|\le1\). It also covers \(z=0\), points of norm strictly below one, and points of norm one. The construction does not require the chosen small coordinates to vanish.

## Relationship to prior work
Lemma 3 of arXiv:2609.28569v1 proves that the same hypothesis implies every element of \(B_{c_0(X)}\) is the average of four Delta-points. Its proof also establishes the coordinate-lifting fact used above. The present statement strengthens that finite representation from four equal-weight Delta-points to three.

Theorem 4.1(2)(d) of arXiv:2410.04706 characterizes Delta-points in vector-valued \(C_0(L,X)\) spaces and supplies the relevant coordinate mechanism at isolated norm-attaining points. Inspection of that theorem and searches for equal-weight three-point, four-point, finite convex-generation, and Caratheodory-type formulations did not reveal a statement implying the three-point representation.

## Limitations
No minimality assertion is made: the result does not claim that two Delta-points can never suffice in a particular space or for a particular vector. It gives a universal width-three representation under only the existence of one Delta-point in \(X\). The argument is for the countable \(c_0\)-sum and uses the availability of three arbitrarily small coordinates.

## References
1. Johann Langemets, *Erratum and a counterexample to “Stability of diametral diameter two properties”*, arXiv:2609.28569v1, especially Lemma 3.
2. Han Ju Lee, Óscar Roldán, and Hyung-Joon Tag, *On various diametral notions of points in the unit ball of some vector-valued function spaces*, arXiv:2410.04706, especially Theorem 4.1(2)(d).
