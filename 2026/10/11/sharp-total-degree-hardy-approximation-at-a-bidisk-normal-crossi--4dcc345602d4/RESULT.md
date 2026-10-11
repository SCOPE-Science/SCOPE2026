# Sharp total-degree Hardy approximation at a bidisk normal crossing

## Finding
Let \(f(z,w)=(1-z)(1-w)\). In the standard Hardy space \(H^2(\mathbb D^2)\), define
\[
 E_n=\min_{p\in\mathcal P_n}\|1-fp\|_2^2,
 \quad\mathcal P_n=\{p\in\mathbb C[z,w]:\deg_{\mathrm{total}}p\le n\}, \quad n\ge0.
\]
Put \(L=n+2\), \(B=\lfloor\sqrt L\rfloor\), \(M=L-B\), and \(K=\lceil M/B\rceil\). Every integer \(n\ge0\) satisfies
\[
 \boxed{\frac2{n+4}\le E_n\le\frac2M+\frac K{M^2}}.
\]
In particular, \(E_n=2/n+O(n^{-3/2})\) as \(n\to\infty\), so the sharp squared-error leading constant is \(\lim_{n\to\infty}nE_n=2\).

There is an exact electrical interpretation: \(E_n\) is the effective resistance between the vertices \(R_0,C_0\) in the unit-conductance bipartite graph having vertices \(R_0,\ldots,R_L,C_0,\ldots,C_L\) and precisely the edges \(R_iC_j\) with \(i+j\le L\). For comparison, if \(p\) has separate degree bounds \(\deg_zp,\deg_wp\le n\), the exact minimum is
\[
 E_n^{\mathrm{rect}}=1-\left(1-\frac1{n+2}\right)^2
 =\frac2{n+2}-\frac1{(n+2)^2}.
\]
Thus \(0\le E_n-E_n^{\mathrm{rect}}=O(n^{-3/2})\). A total-degree restriction gives asymptotically the same leading error as the substantially larger rectangular polynomial space.

## Assumptions and scope
The domain is the unit **bidisk**, not the Euclidean unit ball. The Hardy norm is normalized by orthonormality of monomials:
\[
 \left\|\sum_{i,j\ge0}a_{ij}z^iw^j\right\|_2^2
 =\sum_{i,j\ge0}|a_{ij}|^2.
\]
The source polynomial is exactly \(f(z,w)=(1-z)(1-w)\), the approximating polynomial has complex coefficients and total degree at most \(n\), and the objective is the **square of the norm**. The estimate holds for every integer \(n\ge0\), including \(n=0\); the asymptotic expressions concern \(n\to\infty\).

## Proof
**1. Residuals and coefficient flows.** Since the finite-dimensional space \(f\mathcal P_n\) is closed, the minimum exists. For \(p\in\mathcal P_n\) put \(R=1-fp\). Then \(\deg_{\mathrm{total}}R\le L\), and both polynomial identities \(R(1,w)=1\) and \(R(z,1)=1\) hold. Conversely, if a polynomial \(R\) of total degree at most \(L\) has both identities, then \(1-R\) vanishes identically on \(z=1\) and \(w=1\). Polynomial division by the two relatively prime factors proves \(1-R=(1-z)(1-w)p\) with \(\deg_{\mathrm{total}}p\le L-2=n\); thus the characterization is exact.

Writing \(R=\sum_{i+j\le L}r_{ij}z^iw^j\), the restrictions are equivalent to
\[
 \sum_{j=0}^{L-i}r_{ij}=\mathbf1_{\{i=0\}},\qquad
 \sum_{i=0}^{L-j}r_{ij}=\mathbf1_{\{j=0\}}.
\]
These are exactly Kirchhoff flow-divergence constraints on the unit-resistance bipartite staircase graph with edge \(R_iC_j\) whenever \(i+j\le L\): unit flow leaves \(R_0\) and enters \(C_0\). Every coefficient is a directed edge flow, and the norm squared is its energy \(\sum|r_{ij}|^2\). Thomson's minimum-energy principle therefore identifies \(E_n\) with the effective resistance between \(R_0\) and \(C_0\). Complex flows can be reduced to real flows: the real part has the same real constraints and no greater energy.

**2. Universal lower bound.** Write \(a=r_{00}\). The other \(L\) coefficients in row zero sum to \(1-a\), as do the other \(L\) coefficients in column zero. Cauchy--Schwarz and nonnegativity of the remaining energy imply
\[
 \|R\|_2^2\ge |a|^2+\frac{2|1-a|^2}{L}
 \ge\frac2{L+2}=\frac2{n+4}.
\]
The last inequality is exact minimization of the displayed complex quadratic over \(a\in\mathbb C\); its minimizing value is \(a=2/(L+2)\).

**3. A block-transport polynomial with the sharp constant.** Put \(B=\lfloor\sqrt L\rfloor\ge1\) and \(M=L-B\ge1\). Partition \(\{1,\ldots,M\}\) into consecutive blocks \(Q\) of length at most \(B\); exactly \(K=\lceil M/B\rceil\) blocks are needed. Define a real coefficient family with \(r_{00}=0\) and
\[
 r_{i0}=r_{0i}=\frac1M \quad(1\le i\le M),
 \qquad r_{i,M+1-k}=-\frac1{M|Q|}\quad(i,k\in Q).
\]
Set every unspecified coefficient to zero. Each displayed interior pair is permitted, because for \(i,k\) in the same consecutive block we have \(i-k\le B-1\), whence
\[
 i+(M+1-k)\le M+B=L.
\]
For each positive-index row in \(1,\ldots,M\), the block terms sum to \(-1/M\) and cancel its \(r_{i0}=1/M\); likewise for each positive-index column, because \(k\mapsto M+1-k\) is a bijection. Row zero and column zero each sum to one. All larger-index row and column sums vanish. Thus these coefficients describe an admissible residual \(R\), and the quotient \((1-R)/f\) really belongs to \(\mathcal P_n\).

The two axis families contribute \(2/M\) to the squared Hardy norm. Each block \(Q\) contains \(|Q|^2\) equal-magnitude terms and contributes
\[
 |Q|^2\left(\frac1{M|Q|}\right)^2=\frac1{M^2}.
\]
Therefore \(\|R\|_2^2=2/M+K/M^2\), proving the upper bound. Here \(B=\sqrt L+O(1)\), \(M=L-O(\sqrt L)\) and \(K=O(\sqrt L)\), so the upper bound equals \(2/L+O(L^{-3/2})\), whereas the lower bound equals \(2/L-O(L^{-2})\). Consequently
\[
 E_n=\frac{2}{L}+O(L^{-3/2})
 =\frac2n+O(n^{-3/2}),\qquad \lim_{n\to\infty}nE_n=2.
\]

**4. Rectangular comparison.** In the one-variable Hardy space, the polynomial subspace \((1-z)\mathbb C[z]_{\le n}\) equals the degree-\(n+1\) polynomials vanishing at \(1\). The squared distance from \(1\) to that subspace is exactly \(1/(n+2)\), since its orthogonal complement inside degree \(n+1\) is spanned by \(1+z+\cdots+z^{n+1}\). The rectangular two-variable span is the tensor product of these one-variable subspaces; projecting \(1\otimes1\) onto it leaves squared error
\[
 E_n^{\mathrm{rect}}=1-\left(1-\frac1{n+2}\right)^2.
\]
Because the total-degree space is contained in the rectangular one, \(E_n\ge E_n^{\mathrm{rect}}\). The proven upper bound then yields \(E_n-E_n^{\mathrm{rect}}=O(n^{-3/2})\).

## Verification
The accompanying executable `check_approximation.py` uses Python's exact rational `Fraction` arithmetic only. It independently computes the least-squares Gram-matrix minimum in the polynomial basis, computes the staircase network's resistance from its Laplacian, constructs the block residual and checks polynomial divisibility, and checks the two analytical bounds. For every \(n\in\{0,1,2,3,4,5,6,7\}\), the two independently computed minima agree exactly. For instance, \(E_0=3/4\), \(E_1=7/12\), and \(E_2=17/36\). These finite-degree tests check normalization and the algebra; they do **not** replace the all-degree proof above.

To reproduce from the directory containing the supplied file, run `python3 check_approximation.py` using Python 3 with no external packages.

## Relationship to prior work
The 2026 study of Beslikas and Torkinejad Ziarati (arXiv:2609.09952, first made public 9 September 2026, primary MSC 32F45) studies critical cyclicity in bidisk Dirichlet-type spaces and provides the current motivation for quantitative cyclic approximation; it does not determine the total-degree best-error constant for this fixed normal-crossing polynomial.

The closest same-object treatment is Bénéteau, Condori, Liaw, Seco and Sola, *Cyclicity in Dirichlet-type spaces and extremal polynomials II: functions on the bidisk* (2015), Example 3, pages 51--52. It treats precisely \((1-z)(1-w)\), states cyclicity, and gives rates for explicitly chosen Riesz polynomials, commenting that these rates are not optimal. Those claims do not imply the sharp best-total-degree squared error \(2/n\) or its staircase-network representation. The distinction is one of *statements and implications*, not merely terminology.

Sargent and Sola, *Optimal approximants and orthogonal polynomials in several variables* (arXiv:2002.08790), derive a different one-variable reduction for \(1-z w\); that diagonal zero polynomial is not the two-divisor product studied here. Classical one-variable optimal-approximant results yield the rectangular benchmark but do not enforce the coupled total-degree restriction.

## Limitations
No exact closed form for each finite \(E_n\) is claimed; the precise finite values can be obtained by solving the stated finite network. The asymptotic rate is established only in the standard coefficient Hardy norm for the specified polynomial; no corresponding statement is proved for other bidisk weights, other multipliers, or other geometries. The graph interpretation can in principle be present in older combinatorial literature not identified by the searches; an independently indexed equivalent proof remains an originality risk. There has been no independent audit.

## References
1. A. Beslikas and P. Torkinejad Ziarati, *Critical cyclicity in Dirichlet-type spaces on the bidisk*, arXiv:2609.09952, first submitted 2026-09-09, https://arxiv.org/abs/2609.09952.
2. C. Bénéteau, A. Condori, C. Liaw, D. Seco, and A. Sola, *Cyclicity in Dirichlet-type spaces and extremal polynomials II: functions on the bidisk*, Pacific Journal of Mathematics **276** (2015), 35--58, Example 3, https://msp.org/pjm/2015/276-1/pjm-v276-n1-s.pdf.
3. M. Sargent and A. Sola, *Optimal approximants and orthogonal polynomials in several variables*, arXiv:2002.08790, https://arxiv.org/abs/2002.08790.
