# Single-flat-band positive mixing for line graphs with crossing square cycles

## Finding

Let \(H=(V,E)\) be any finite simple undirected graph, with \(m=|E|>0\). Suppose that **each edge \(e\in E\) belongs to two simple four-cycles whose edge sets intersect in exactly \(\{e\}\)**. Write \(L(H)\) for its line graph, whose vertices are the edges of \(H\), and let \(A=A(L(H))\) be the unweighted adjacency matrix. For the continuous-time quantum walk \(U(t)=\exp(itA)\), its infinite-time average mixing matrix is
\[
\widehat M(L(H))=\lim_{T\to\infty}\frac1T\int_0^T U(t)\circ U(-t)\,dt.
\]
The following explicit **positive-definiteness certificate** holds:
\[
\boxed{\widehat M(L(H))\succeq P\circ P\succeq \frac{1}{16m}I_m,}
\]
where \(P\) is the orthogonal projector onto the adjacency eigenspace of eigenvalue \(-2\). In particular, \(\widehat M(L(H))\) has rank exactly \(m\), and its smallest eigenvalue is at least \(1/(16m)\). A single flat-band spectral projector suffices for strict positivity.

For every integer \(d\ge3\), the line graph of the \(d\)-dimensional binary hypercube satisfies
\[
\boxed{\operatorname{rank}\widehat M(L(Q_d))=d\,2^{d-1}},
\qquad \lambda_{\min}\bigl(\widehat M(L(Q_d))\bigr)\ge\frac{1}{16d\,2^{d-1}}.
\]
More generally, the conclusion holds for the line graph of a Cartesian product of **three or more** finite simple graphs, each with at least one edge, provided each factor has no isolated vertices. The statement is about each product edge; no connectivity hypothesis is required.

The two-factor hypercube is a genuine boundary case: \(L(Q_2)\cong C_4\) has average-mixing rank \(2\), strictly below its four vertices. Hence within \(\{L(Q_d):d\ge2\}\), positive-definite average mixing holds exactly when \(d\ge3\).

## Assumptions and scope

All matrices and spaces are real for the spectral decomposition of \(A\); the quantum evolution \(U(t)\) is complex and unitary. The graph \(H\) is finite, simple, unweighted, and undirected. Its line graph has one vertex for each root edge. The symbol \(\circ\) denotes entrywise multiplication, and \(\succeq\) denotes the Loewner order on real symmetric matrices. The square-cycle hypothesis specifies **two distinct four-cycles for every root edge**, with precisely that edge in common, not merely two cycles that share additional edges or vertices. Shared vertices other than the endpoints of the selected edge are irrelevant.

Let \(B\) be the **unsigned** vertex-edge incidence matrix, so \(B_{v,e}=1\) when vertex \(v\) is an endpoint of edge \(e\) and zero otherwise. Then \(B^{\mathsf T}B=2I_m+A\). It follows that the eigenspace of \(A\) at eigenvalue \(-2\) is \(\ker B\) and its orthogonal projector is \(P\). This eigenspace is nontrivial under the square-cycle hypothesis.

## Proof

**Step 1: Flat-band alternating vectors.** A simple four-cycle \(C=(v_0,v_1,v_2,v_3,v_0)\) has an alternating signed edge vector \(c_C\in\mathbb R^E\). It takes values \(+1,-1,+1,-1\) on its four consecutively ordered edges and vanishes on every other edge. Each vertex of the cycle is incident to one positive and one negative marked edge. Consequently \(Bc_C=0\), so \(Pc_C=c_C\), and \(\|c_C\|_2=2\).

**Step 2: Local pairwise products isolate coordinates.** Fix an arbitrary root edge \(e\), and choose four-cycles \(C_e,D_e\) guaranteed by the hypothesis, with \(E(C_e)\cap E(D_e)=\{e\}\). Choose alternating vectors \(c_e=c_{C_e}\) and \(d_e=c_{D_e}\) as above. Since the vectors have only this one common nonzero coordinate, their entrywise product is \(c_e\circ d_e=\sigma_e\mathbf e_e\), where \(\sigma_e\in\{-1,+1\}\) and \(\mathbf e_e\) is the coordinate unit vector at edge \(e\). In particular their **coordinatewise product**, unlike each individual vector, is supported on one prescribed edge.

**Step 3: An exact projector-square identity.** For every \(z\in\mathbb R^E\), write \(D_z=\operatorname{diag}(z)\). Since \(P\) is a symmetric orthogonal projector,
\[
\begin{aligned}
 z^{\mathsf T}(P\circ P)z
 &=\operatorname{tr}(P D_z P D_z)\\
 &=\operatorname{tr}\bigl((P D_z P)^2\bigr)
 =\|P D_z P\|_F^2.
\end{aligned}
\]
Both equalities follow by expanding the trace and using \(P^2=P\). The right-hand side is nonnegative and vanishes exactly when the compressed diagonal operator \(P D_z P\) vanishes.

**Step 4: Quantitative injectivity.** Since \(Pc_e=c_e\) and \(Pd_e=d_e\), for each root edge \(e\) we have
\[
\begin{aligned}
 |z_e|
 &=|c_e^{\mathsf T}D_z d_e|
 =|c_e^{\mathsf T}P D_z P d_e|\\
 &\le \|c_e\|_2\,\|P D_z P\|_2\,\|d_e\|_2
 \le4\|P D_z P\|_F.
\end{aligned}
\]
Summing the squared inequalities over all \(m\) root edges yields
\[
\|z\|_2^2\le16m\|P D_z P\|_F^2
 =16m\,z^{\mathsf T}(P\circ P)z.
\]
Thus \(P\circ P\succeq I_m/(16m)\) without assuming that the four-cycle witnesses chosen for different edges are independent or disjoint.

**Step 5: From one eigenspace to quantum average mixing.** Let \(\{E_\theta\}\) be the orthogonal spectral projectors of \(A\), with one projector for each **distinct** eigenvalue. The standard time-averaging calculation is
\[
\widehat M(L(H))=\sum_\theta E_\theta\circ E_\theta.
\]
Indeed, writing \(U(t)=\sum_\theta e^{it\theta}E_\theta\), every cross-frequency term with distinct frequencies has zero infinite Cesàro average. Each term \(E_\theta\circ E_\theta\) is positive semidefinite by the Schur-product theorem, including terms from eigenspaces of multiplicity greater than one. Since the projector for eigenvalue \(-2\) is \(P\),
\[
\widehat M(L(H))\succeq P\circ P\succeq I_m/(16m),
\]
proving the theorem for every eligible root graph.

**Step 6: Cartesian products and the sharp hypercube boundary.** Consider \(H=G_1\square\cdots\square G_r\) with \(r\ge3\) and each factor containing at least one edge. Every product edge changes precisely one coordinate, say coordinate \(i\). Choose distinct coordinates \(j,k\ne i\) and an edge in each of the factor directions \(j,k\) incident to the corresponding current factor vertices. The two coordinate squares in directions \((i,j)\) and \((i,k)\) are simple four-cycles sharing exactly the original product edge. This proves the hypothesis for all product edges, even if the factors have disconnected components, since each factor has no isolated vertices. In particular each \(Q_d=K_2^{\square d}\), for \(d\ge3\), satisfies it; the hypercube has \(d2^{d-1}\) edges.

For \(d=2\), the line graph is the four-cycle \(C_4\). Its adjacency eigenspaces have eigenvalues \(2,0,-2\), with multiplicities \(1,2,1\). Let \(F\) be the antipodal permutation matrix. The spectral-projector formula gives \(\widehat M(C_4)=J_4/8+(I_4+F)/4\); the eigenvalues are \(1,1/2,0,0\). Therefore the rank is \(2\), confirming that the threshold \(d\ge3\) is sharp within the indicated hypercube family.

## Verification

An independent exact-arithmetic verifier is supplied as `verify.py`. It enumerates four-cycles, searches for a pair intersecting in exactly each prescribed edge, and checks the alternating incidence-nullspace conditions. For five small root graphs it reconstructs the rational orthogonal projector onto \(\ker B\) by a nullspace basis and a rational Gram inverse, verifies \(P^2=P\), and tests strict positivity of \(P\circ P-I_m/(16m)\) using exact fraction-valued \(LDL^{\mathsf T}\) elimination. It additionally checks square-cycle witnesses for all hypercubes \(Q_d\) with \(3\le d\le7\) and confirms that \(Q_2\) does not satisfy the certificate hypothesis.

To replay, run `python3 verify.py` in a directory containing this supplied file. The final success line is `VERIFY_OK exact_projectors 5 certificate_edges 861 cycle_witnesses 1087 nonexample_Q2_confirmed`. Exact projector instances include \(Q_3\), \(Q_4\), \(K_3\square K_2\square K_2\), \(P_3\square K_2\square K_2\), and \(K_{3,3}\). All numerical values printed for \(LDL^{\mathsf T}\) pivots describe elimination pivots, not eigenvalues. These checks are finite corroborations, **not** a substitute for the arbitrary-graph argument in Steps 1–5.

## Relationship to prior work

Godsil's original average-mixing theorem and Coutinho–Godsil–Guo–Zhan's commutant approach establish the general spectral-projector/Schur-product framework used in Step 5. Coutinho and collaborators' *Irrational quantum walks* provides a relevant study of exact spectral time averaging; the present certificate relies on its standard mathematical setting rather than asserting a new averaging identity. Coutinho and Guo's survey highlights the importance of full-rank average mixing. The classical unsigned-incidence identity and the \(-2\) flat band of line graphs are known, including in Kang's 2026 discussion of line-graph flat-band states. None of those identities alone establishes that **coordinatewise products of localized four-cycle modes span the full edge-coordinate space**. The finding here is the explicit two-cycle criterion, its universal quantitative lower bound, and its Cartesian-product consequences.

## Limitations

The two-four-cycle hypothesis is **sufficient, not claimed necessary**. Failure of the certificate hypothesis does not imply singular average mixing; in particular the lower bound may be conservative and need not be the optimal gap. The theorem concerns unweighted simple root graphs and the adjacency Hamiltonian of their line graphs. It does not address Laplacian Hamiltonians, magnetic/sign-weighted edges, or randomized observation-time averages. For the Cartesian-product corollary, each factor must have **no isolated vertices**, not merely contain one edge; otherwise product edges in isolated-coordinate fibers can lack the needed squares. The general theorem itself remains valid without any connectivity restriction.

## References

1. C. Godsil, “Average Mixing of Continuous Quantum Walks,” arXiv:1103.2578; *Journal of Combinatorial Theory, Series A* 120 (2013), 1649–1662.
2. G. Coutinho, C. Godsil, K. Guo, H. Zhan, “A New Perspective on the Average Mixing Matrix,” arXiv:1709.03591; *Electronic Journal of Combinatorics* 25 (2018), P4.14.
3. G. Coutinho, P. Ferreira Baptista, C. Godsil, T. Jung Spier, R. Werner, “Irrational quantum walks,” arXiv:2208.08971 (first publicly submitted 2022-08-18), *SIAM Journal on Applied Algebra and Geometry* 7 (2023), 567–584.
4. G. Coutinho and K. Guo, “Selected Open Problems in Continuous-Time Quantum Walks,” arXiv:2404.02236 (2024), Section 4.
5. M. Kang, “Schur States and Many-Body Quantum Walks on Line Graphs,” arXiv:2605.01953v2 (2026), Section 6, unsigned-incidence identity and flat-band orbitals.
6. P. Baptista, G. Coutinho, V. Marques, “Unexpected Averages of Mixing Matrices,” arXiv:2308.16378 (2023), for comparison with alternative observation-time averages.
