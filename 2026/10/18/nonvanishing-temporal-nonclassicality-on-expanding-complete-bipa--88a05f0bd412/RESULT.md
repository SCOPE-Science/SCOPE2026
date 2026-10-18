# Nonvanishing temporal nonclassicality on expanding complete bipartite quantum walks

## Finding
For arbitrary positive integers \(m,n\), consider the graph \(K_{m,n}\), its combinatorial Laplacian \(L\), the energy-dephased continuous-time quantum walk
\[
\mathcal L_\gamma(\rho)=-i[L,\rho]-\frac{\gamma}{2}[L,[L,\rho]],\qquad \gamma>0,
\]
and a site-localized initial walker \(\rho_0=|v\rangle\langle v|\) with \(v\) in the part of size \(m\). Use position-projective measurements and the time-averaged, two-time Kolmogorov-consistency defect of Luppi, Benedetti and Smirne [1], denoted \(\overline K_{m,n}(t)\). Define its long-time value \(R_{m,n}=\lim_{t\to\infty}\overline K_{m,n}(t)\).

Then the exact law for every \(m,n\ge1\) is
\[
\boxed{R_{m,n}=\begin{cases}
\displaystyle\frac{2n(m+n-2)}{(m+n)^3},&m=1,2,\\[5pt]
\displaystyle\frac{2(m-1)(m-2)}{m^3}+\frac{2n(m+n-2)}{m(m+n)^3},&m\ge3.
\end{cases}}
\]
The value is independent of the strictly positive dephasing rate \(\gamma\). For any fixed \(m\), the limit over growing opposite-part size is
\[
\boxed{\lim_{n\to\infty}R_{m,n}=\begin{cases}0,&m=1,2,\\\displaystyle\frac{2(m-1)(m-2)}{m^3},&m\ge3.\end{cases}}
\]
For \(m\ge3\), the displayed finite-size correction is strictly positive and at most \(2/[m(m+n)]\). Among all fixed positive integer \(m\), the surviving limit is uniquely maximized by \(m=5\), with exact value \(24/125\). Hence, expanding the other part of the network does **not** invariably suppress residual temporal nonclassicality; the surviving contribution depends on the size of the part containing the initial site.

## Assumptions and scope
The graph is finite, simple, unweighted and complete bipartite, with both part sizes at least one. The Hamiltonian is the **combinatorial Laplacian**, not the adjacency or normalized Laplacian. The rate \(\gamma\) is any fixed positive real number for each finite graph, and it acts by the Lindblad generator above. Site measurements are the rank-one projectors \(|x\rangle\langle x|\). The initial position lies in the size-\(m\) part, so interchanging the initial part requires swapping \(m\) and \(n\). The order of limits is first \(t\to\infty\), then \(n\to\infty\); no uniform-in-size relaxation-time claim is made.

More explicitly, let \(\Phi_t=e^{t\mathcal L_\gamma}\) and \(\mathcal D(X)=\sum_x|x\rangle\langle x|X|x\rangle\langle x|\). Write \(p_t(x)=\langle x|\Phi_t(\rho_0)|x\rangle\) and \(p_{s,t}^{\mathrm{ins}}(x)=\langle x|\Phi_{t-s}\mathcal D\Phi_s(\rho_0)|x\rangle\), for \(0\le s\le t\). The exact normalization is
\[
K(s,t)=\frac12\sum_x|p_{s,t}^{\mathrm{ins}}(x)-p_t(x)|,\qquad
\overline K_{m,n}(t)=\frac1t\int_0^t K(s,t)\,ds.
\]
This is the nonselective-intermediate-position-measurement defect, not a distance between two freely chosen random walks.

## Proof
**1. Long-time reduction.** Let \(P_\lambda\) be the mutually orthogonal spectral projectors of \(L\), indexed by its *distinct* eigenvalues, and put \(\mathcal E(X)=\sum_\lambda P_\lambda XP_\lambda\). Because \(\gamma>0\), the spectral representation of \(\Phi_t\) makes it converge to \(\mathcal E\) for every finite graph, exponentially on each cross-eigenspace block. With \(F_{xy}=\sum_\lambda |(P_\lambda)_{xy}|^2\), the site distribution after \(\mathcal E\) is \(F e_v\). Inserting the site measurement followed by another energy pinching gives \(F^2 e_v\). For intermediate times satisfying \(s\to\infty\) and \(t-s\to\infty\), the corresponding inserted and uninserted distributions converge to these two limits. Since \(0\le K(s,t)\le1\), the fraction of averaging times within any fixed bounded distance of either endpoint vanishes. First choosing that bounded distance large and then sending \(t\to\infty\) yields
\[
R_{m,n}=\frac12\|(F-F^2)e_v\|_1.
\]
This general reduction is also Eq. (B8) of [1] and is **not** asserted to be new.

**2. Exact projectors.** Put \(N=m+n\), and write \(J_{a,b}\) for an all-ones \(a\times b\) matrix. Relative to the ordered parts, the Laplacian is
\[
L=\begin{pmatrix}nI_m&-J_{m,n}\\-J_{n,m}&mI_n\end{pmatrix}.
\]
Its spectral projectors include \(P_0=J_N/N\), the rank-one projector \(P_N\) with entries \(n/(mN)\) within the first part, \(m/(nN)\) within the second and \(-1/N\) across parts, and the two within-part zero-sum projections
\[
Q_A=\operatorname{diag}(I_m-J_m/m,0_n),\qquad
Q_B=\operatorname{diag}(0_m,I_n-J_n/n),
\]
with eigenvalues \(n\) and \(m\), respectively. Empty zero-sum sectors are zero projections. When \(m=n\), their eigenvalues coincide and the correct projector is \(Q_A+Q_B\); since the two matrices have disjoint supports, their entrywise square is still \(Q_A\circ Q_A+Q_B\circ Q_B\). Therefore the following calculation applies without an exceptional balanced case.

**3. Mixing-operator eigenmodes.** The entrywise-square projector sum \(F=\sum_\lambda P_\lambda\circ P_\lambda\) is symmetric and stochastic. Cross-part entries are \(F_{xy}=2/N^2\), while for \(x,y\) in the first part,
\[
F_{xy}=\frac1{N^2}+\frac{n^2}{m^2N^2}+(\mathbf{1}_{x=y}-1/m)^2.
\]
The analogous second-part entries replace \((m,n)\) by \((n,m)\). Thus \(F\) acts on: the all-ones vector with eigenvalue \(1\); the vector \(w=\mathbf{1}_A/m-\mathbf{1}_N/N\) with eigenvalue \(1-2/N\); the first-part zero-sum space with eigenvalue \(1-2/m\); and, when present, the second-part zero-sum space with eigenvalue \(1-2/n\). These spaces are orthogonal and span all \(N\) coordinates.

Decompose \(e_v=\mathbf{1}_N/N+w+u\), where \(u=e_v-\mathbf{1}_A/m\). Consequently,
\[
(F-F^2)e_v=A_m u+B_N w,\quad
A_m=\frac{2(m-2)}{m^2}\ (m\ge2),\quad
B_N=\frac{2(N-2)}{N^2}.
\]
For \(m=1\), \(u=0\) and the coefficient \(A_m\) is taken as zero. The coordinates of this difference are
\[
\begin{aligned}
d_v&=A_m(m-1)/m+B_Nn/(mN),\\
d_{A\setminus\{v\}}&=-A_m/m+B_Nn/(mN),\\
d_B&=-B_N/N.
\end{aligned}
\]
Each of the last two values is repeated \(m-1\) and \(n\) times, respectively.

**4. Sign classification and limits.** When \(m=1,2\), the coefficient \(A_m\) vanishes; the first-part coordinates are nonnegative and the second-part coordinates nonpositive. Hence the positive total mass, equal to half the \(\ell^1\) norm, is \(B_Nn/N\). For \(m\ge3\), the inequality \(4mn\le N^2\) gives
\[
B_Nn/N <2n/N^2\le1/(2m)<A_m.
\]
Thus only \(d_v\) is positive, and the total positive mass is \(d_v\). Substituting the coefficients gives precisely the two claimed formulas. At fixed \(m\), the second summand is bounded by \(2/[mN]\) and vanishes as \(n\to\infty\). Finally, the fixed-part residual \(g(x)=2(x-1)(x-2)/x^3\) for \(x\ge3\) has derivative \(g'(x)=-2(x^2-6x+6)/x^4\). It increases until \(x=3+\sqrt3\) and decreases thereafter; the unique maximizing positive integer \(m\) is therefore \(5\), with \(g(5)=24/125\). This proves all assertions.

## Verification
The standard-library script `verify.py` constructs all distinct-eigenvalue spectral projectors from exact rational entries, merges coincident eigenspaces, confirms orthogonality, idempotence and resolution of the identity, and independently evaluates \(\frac12\|(F-F^2)e_v\|_1\). It compares the resulting exact fractions with the formula in **70** graph instances, including both initial-side sizes one and two and balanced cases. The resulting output is `VERIFY_OK 70 exact projector/rational-residual cases; limiting optimum 24/125`. Separately, numerical symmetric eigendecomposition checked all \(361\) pairs with \(1\le m,n\le19\). The proof above, not the finite tests, covers all positive sizes and all positive dephasing rates.

## Relationship to prior work
Luppi, Benedetti and Smirne [1] introduced the two-time consistency quantifier, proved the general long-time expression in terms of the spectral-projector mixing matrix, and computed the complete-graph and cycle examples. Their Appendix B also gives the two vertex-dependent values for the three-vertex path, which agree with the corresponding cases here. The present analysis does not claim those definitions, the universal reduction, or that small-graph example; it supplies the complete arbitrary-rectangular bipartite evaluation and its fixed-part macroscopic, size-threshold and unique-optimizer consequences.

Baptista, Coutinho and Marques [2] studied average mixing matrices for **adjacency-Hamiltonian** walks, including an obstruction to uniform average mixing on large complete bipartite graphs. Their uniform-mixing property is not the present Laplacian, energy-dephasing, two-time consistency defect. Mohan, Tamon, Xu and Zhan [3] study the **trace** of the Laplacian average mixing matrix (graph laziness), with results including stars. The trace does not by itself specify the vertex-conditioned nonlinear quantity \(\|(F-F^2)e_v\|_1\); their complete text was not available for full comparison, so possible implicit coverage remains a stated priority risk.

## Limitations
All graphs are complete bipartite and the initial condition is localized. The long-time result holds only for strictly positive energy-basis dephasing; it is not a statement for unitary evolution or position-basis noise. The macroscopic limit holds in the order \(t\to\infty\), then \(n\to\infty\), without a rate uniform in network size. The assertion of novelty is restricted to the exact bipartite residual and its nonvanishing and optimizing asymptotics; it is neither a general theory of temporal nonclassicality nor a claim of publication priority. Established projector-average formulas supply substantial prior ingredients.

## References
[1] P. Luppi, C. Benedetti and A. Smirne, “Temporal nonclassicality in continuous-time quantum walks,” *Physical Review A* **113**, 042212 (2026), DOI: 10.1103/11ty-bsfy; first public preprint arXiv:2512.18873v1 (2025-12-21); particularly Eq. (9) and Appendix B, Eqs. (B7)–(B8).

[2] P. Baptista, G. Coutinho and V. Marques, “Unexpected Averages of Mixing Matrices,” arXiv:2308.16378 (2023), especially Section 3.1 (complete bipartite graphs).

[3] A. Mohan, C. Tamon, Y. Xu and H. Zhan, “Laziness of Quantum Walks on Graphs,” arXiv:2608.20739 (2026). The available abstract addresses Laplacian average-mixing trace and its extremizers; full-text comparison was inaccessible.
