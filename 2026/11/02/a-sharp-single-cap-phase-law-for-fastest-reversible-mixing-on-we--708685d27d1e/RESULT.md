# A sharp single-cap phase law for fastest reversible mixing on weighted paths

## Finding

For every finite path with at least three vertices, arbitrary positive vertex masses, arbitrary positive linear edge prices, and a positive conductance budget, placing a fixed upper cap on one specified edge produces **exactly two global optimum regimes**. Below a computable sharp cap threshold, the specified edge is saturated, all other edges remain strictly active, and the unique optimal conductance vector and optimal reversible spectral gap are explicit in the unique positive root of a quadratic. At or above the threshold, the original uncapped optimum persists. This is an optimization over *all independent edge conductances*, not a symmetric or ansatz-restricted family.

A second sharp conclusion concerns severe bottlenecks: as the designated cap \(U\downarrow0\), the maximum gap has the expansion
\[
\lambda_*(U)=\frac{U}{C}-\frac{A^2}{C^3B}U^2+O(U^3),
\]
where \(C\) is the reduced mass of the two components separated by the capped edge and \(A\) is a positive quantity determined solely by the other edge prices and the vertex masses. The leading slope depends neither on the conductance budget nor on any edge price.

## Assumptions and scope

Take an integer \(n\ge3\), masses \(m_1,\ldots,m_n>0\), prices \(c_1,\ldots,c_{n-1}>0\), budget \(B>0\), a designated edge index \(k\in\{1,\ldots,n-1\}\), and its upper capacity \(U>0\). The path edges are \(\{i,i+1\}\). Choose all conductances \(w_i\ge0\) independently subject to
\[
\sum_{i=1}^{n-1}c_iw_i\le B,\qquad w_k\le U.
\]
Let \(M=\operatorname{diag}(m_1,\ldots,m_n)\) and let \(L(w)\) be the weighted combinatorial path Laplacian. The objective is the second generalized eigenvalue \(\lambda_2(L(w),M)\), equivalently the spectral gap of the reversible continuous-time generator \(-M^{-1}L(w)\). No normalization \(\sum m_i=1\) is imposed.

For every nonnegative length vector \(d=(d_1,\ldots,d_{n-1})\), put
\[
 p_1(d)=0,\quad p_{j+1}(d)=p_j(d)+d_j,\quad
 \bar p(d)=\frac{\sum_{j=1}^n m_jp_j(d)}{\sum_{j=1}^n m_j},
\]
\[
 x_j(d)=p_j(d)-\bar p(d),\quad
 V(d)=\sum_{j=1}^n m_jx_j(d)^2,\quad
 S_i(d)=-\sum_{j=1}^i m_jx_j(d).
\]
For positive \(d\), all \(S_i(d)>0\). Set \(q_i=\sqrt{c_i}\), \(q=(q_i)\), and
\[
 \lambda_0=\frac{B}{V(q)},\qquad
 w_i^0=\lambda_0\frac{S_i(q)}{q_i},\qquad U_0=w_k^0.
\]

**Inactive-cap regime.** If \(U\ge U_0\), the unique global optimum is \(w=w^0\), and \(\lambda_*(U)=\lambda_0\).

**Active-cap regime.** Suppose \(0<U<U_0\). Define the *contracted-length* vector \(d^c\) by \(d_i^c=q_i\) for \(i\ne k\) and \(d_k^c=0\), and write
\[
 A=S_k(d^c),\quad D=V(d^c),\quad
 C=\frac{\bigl(\sum_{j\le k}m_j\bigr)\bigl(\sum_{j>k}m_j\bigr)}{\sum_{j=1}^n m_j},\quad
 E=B-c_kU.
\]
All four of \(A,D,C,E\) are strictly positive. Let \(z>0\) be the **unique positive root** of
\[
 UA z^2+(UD-CE)z-AE=0.
\]
Equivalently, for exact computation,
\[
 z=\frac{CE-UD+\sqrt{(UD-CE)^2+4UA^2E}}{2UA}.
\]
Then \(z>q_k\). Define \(d(z)\) by \(d_i(z)=q_i\) for \(i\ne k\) and \(d_k(z)=z\). The **unique unrestricted optimum** is
\[
 \boxed{\lambda_*(U)=\frac{Uz}{A+Cz}},\qquad
 \boxed{w_k^*=U},\qquad
 \boxed{w_i^*=\lambda_*(U)\frac{S_i(d(z))}{q_i}\quad(i\ne k).}
\]
Every edge receives strictly positive conductance, the total budget is exhausted, and the two formulas join continuously at \(U=U_0\).

The bottleneck expansion stated above holds for fixed masses, prices, and budget as \(U\downarrow0\). In particular, if \(M_L=\sum_{j\le k}m_j\) and \(M_R=\sum_{j>k}m_j\), then
\[
 \lim_{U\downarrow0}\frac{\lambda_*(U)}U=\frac1{M_L}+\frac1{M_R}.
\]

## Proof

**1. Path identities and positivity.** Centering gives \(\sum_jm_jx_j(d)=0\), and discrete summation by parts gives
\[
 V(d)=\sum_{i=1}^{n-1}d_iS_i(d),\qquad
 S_i(d)=\frac1{\sum_jm_j}\sum_{a\le i<b}m_am_b\bigl(p_b(d)-p_a(d)\bigr).
\]
Thus \(S_i(d)>0\) if all the lengths are positive. It also holds for \(d^c\), because \(n\ge3\) leaves at least one strictly positive length on the path and for each cut at least one cross-cut vertex pair with distinct positions. In particular, \(A,D,C>0\). If \(U<U_0\), then \(c_kU<c_kw_k^0<B\) since every other uncapped weight is positive, so \(E>0\).

**2. The uncapped optimizer and its global certificate.** For every feasible \(w\), the generalized Rayleigh principle applied to \(x(q)\) gives
\[
 \lambda_2(L(w),M)\le\frac{\sum_i c_iw_i}{V(q)}\le\frac B{V(q)}=\lambda_0.
\]
The claimed weights \(w_i^0\) exhaust the budget by the summation identity. Their edge fluxes satisfy \(w_i^0(x_{i+1}(q)-x_i(q))=\lambda_0S_i(q)\). Taking adjacent flux differences yields \(L(w^0)x(q)=\lambda_0Mx(q)\). The positive-weight path is an irreducible symmetric Jacobi problem after conjugating by \(M^{-1/2}\). Its eigenvalues are simple; by discrete Sturm oscillation its strictly increasing, centered eigenvector with exactly one sign change belongs to the second eigenvalue. Hence \(\lambda_2=\lambda_0\).

**3. Exact single-cap reduction.** Increasing the \(k\)-th length of \(d^c\) by \(z\) changes the centered coordinates by an intercomponent step, giving the exact identities
\[
 S_k(d(z))=A+Cz,\qquad V(d(z))=D+2Az+Cz^2.
\]
If the capped edge is saturated and the other lengths retain their price-square-root values, the required flux equation forces
\[
 \lambda=\frac{Uz}{A+Cz}.
\]
The remaining rates given in the theorem are positive. The budget equation follows from \(V(d)-\sum_{i\ne k}q_iS_i(d)=zS_k(d)\):
\[
 E=\sum_{i\ne k}c_iw_i
 =\lambda\bigl(V(d(z))-zS_k(d(z))\bigr)
 =\frac{Uz}{A+Cz}(D+Az).
\]
Multiplication yields \(UA z^2+(UD-CE)z-AE=0\). Its constant coefficient is negative and its leading coefficient is positive; consequently it has exactly one positive root.

The cap as a function of \(z\) is
\[
 U(z)=\frac{B(A+Cz)}{c_k(A+Cz)+z(D+Az)}.
\]
Its derivative is strictly negative, since its numerator after removing a positive common factor is \(-A(D+2Az+Cz^2)<0\). At \(z=q_k\), \(U(z)=U_0\). Therefore \(0<U<U_0\) implies \(z>q_k\) and the candidate is feasible with an exhausted budget.

**4. Global optimality and unrestricted uniqueness.** The constructed fluxes satisfy \(w_i^*d_i(z)=\lambda_*S_i(d(z))\) for *every* edge, including the capped one. Hence \(L(w^*)x(d(z))=\lambda_*Mx(d(z))\). Discrete Sturm oscillation again identifies this eigenvalue as \(\lambda_2\). For any other feasible allocation \(\tilde w\), the same test vector proves
\[
 \lambda_2(L(\tilde w),M)
 \le\frac{\sum_i\tilde w_i d_i(z)^2}{V(d(z))}
 =\frac{\sum_i c_i\tilde w_i+(z^2-c_k)\tilde w_k}{V(d(z))}
 \le\frac{B+(z^2-c_k)U}{V(d(z))}=\lambda_*.
\]
The second inequality uses \(z>q_k\), and the final equality follows from the constructed allocation. If equality holds for another allocation, equality in the Rayleigh inequality forces \(x(d(z))\) to be an eigenvector with eigenvalue \(\lambda_*\). Its edge fluxes are then uniquely determined by the first \(i\) vertex equations, yielding \(\tilde w_i d_i(z)=\lambda_*S_i(d(z))\) for all \(i\); all lengths are positive, so \(\tilde w=w^*\). The same flux argument proves uniqueness in the inactive regime.

**5. Severe-cap asymptotics.** The quadratic balance yields \(z=CB/(AU)+O(1)\) as \(U\downarrow0\). Expanding \(\lambda_*=Uz/(A+Cz)\) gives
\[
 \lambda_*(U)=\frac U C-\frac{A^2}{C^3B}U^2+O(U^3).
\]
The identity \(C^{-1}=M_L^{-1}+M_R^{-1}\) supplies the universal first-order bottleneck law. These are fixed-data asymptotics; no uniformity in masses or prices is asserted.

## Verification

The companion \(\texttt{verify.py}\) is an independently executable Python 3 program using only the standard library. It checks 245 constructed exact-rational instances of the budget, quadratic, spectral eigenvector, positivity, and active-cap threshold identities; 585 finite numerical instances comparing the formula to an independent symmetric Jacobi diagonalization; 3,852 sampled feasible competitors; and one exact four-vertex radical example. The finite checks are **supplementary**, not substitutes for the proof above.

For example, with \(n=4\), unit masses and prices, \(B=1\), and the middle edge capped at \(U=1/5\), the uncapped threshold is \(U_0=2/5\), while the exact capped solution is
\[
 z=1+\sqrt5,\quad
 (w_1^*,w_2^*,w_3^*)=(2/5,1/5,2/5),\quad
 \lambda_*=\frac{3-\sqrt5}{5}.
\]
Run \(\texttt{python3 verify.py}\) after extracting the supplied file.

## Relationship to prior work

Sun, Boyd, Xiao, and Diaconis (2006), Result 5 in section 5.2, **already determine the unique uncapped cost-weighted path optimizer with uniform vertex masses**; their section 6 gives a general reversible weighted-mass semidefinite program and dual but does not give a one-edge-cap closed form. The uncapped reference profile above is a starting point and **not claimed as a new discovery**. Fiedler's 1990 work and Wan and collaborators' 2008 work give earlier structural solutions for unconstrained tree algebraic-connectivity design. The separate contribution here is the exact single-edge capacity phase law, mass-heterogeneous quadratic resolution, uniqueness under the cap, and sharp bottleneck expansion, which are not implications explicitly provided by the materially inspected prior results.

## Limitations

The theorem requires a path, at least three vertices, strictly positive vertex masses, prices, budget, and cap, and exactly one capped edge. An actual zero cap disconnects the network and destroys strict uniqueness. No multiple-cap formula, nonpath extension, or discrete-time mixing result is asserted. No claim is made that the uncapped path solution or the general spectral SDP framework is new. Full specialist priority checking remains incomplete: Fiedler's 1990 original article could not be obtained in full, and other uncatalogued constrained-network designs may exist. The mathematical review recorded here is not an independent external audit.

## References

1. J. Sun, S. Boyd, L. Xiao and P. Diaconis, "The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem," *SIAM Review* **48** (2006), 681–699; electronically published November 2, 2006; doi:10.1137/S0036144504443821. Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf.
2. M. Fiedler, "Absolute algebraic connectivity of trees," *Linear and Multilinear Algebra* **26** (1990), 85–106; doi:10.1080/03081089008817967 (full text not inspected).
3. Y. Wan, S. Roy, X. Wang, A. Saberi, T. Yang, M. Xue and B. Malek, "On the Structure of Graph Edge Designs that Optimize the Algebraic Connectivity," *Proceedings of the 47th IEEE Conference on Decision and Control* (2008); doi:10.1109/CDC.2008.4738734. Authorized paper: https://skoge.folk.ntnu.no/prost/proceedings/cdc-2008/data/papers/0353.pdf.
4. L. Kempton, G. Herrmann and M. di Bernardo, "Distributed Adaptive Optimization and Control of Network Structures," *2016 IEEE Conference on Decision and Control* (2016); doi:10.1109/CDC.2016.7799167. This addresses distributed constrained weight adaptation, not the explicit capped-path formula.
