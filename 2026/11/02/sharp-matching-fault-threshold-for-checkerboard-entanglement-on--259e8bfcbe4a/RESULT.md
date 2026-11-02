# Sharp matching-fault threshold for checkerboard entanglement on even hypercubes

## Finding

Let \(d\ge4\) be **even**, let \(Q_d\) be the binary \(d\)-cube, and prepare its pure qubit graph state. For the bipartition into vertices of even and odd Hamming weight, the original entropy in bits is \(S_0=2^{d-2}\). Omit controlled-\(Z\) gates on a set \(F\) of \(k\) pairwise vertex-disjoint edges, leaving every other gate present. **For every matching with \(0\le k\le d-1\),** the von Neumann entropy and every nonzero-order Rényi entropy are exactly

\[
S_F=2^{d-2}+k.
\]

The all-placement additive law is *sharp*. At \(k=d\), there exist two explicit matchings \(F_{\mathrm{dep}}\) and \(F_{\mathrm{ind}}\) with

\[
S_{F_{\mathrm{dep}}}=2^{d-2}+d-1,
\qquad
S_{F_{\mathrm{ind}}}=2^{d-2}+d.
\]

Thus the first placement-sensitive defect count is exactly the cube dimension. These are statements about pure-state cut entanglement, not about operational fault tolerance or entanglement under noisy gate channels.

## Assumptions and scope

Vertices are the binary vectors \(x\in\mathbb F_2^d\); two vertices are adjacent exactly when their Hamming distance is one. Write \(e_i\) for the unit vector in coordinate \(i\), with indices \(0\le i<d\). Let \(E\) and \(O\) be the even- and odd-weight vertices. The graph state is \(|G\rangle=\prod_{\{u,v\}\in E(G)} CZ_{uv}|+\rangle^{\otimes 2^d}\). The cut is \(E\mid O\). Every omitted gate means *deletion of its corresponding graph edge*, not a stochastic channel. Matchings have no shared endpoints. Define \(m=2^{d-1}\); all ranks below are over \(\mathbb F_2\).

To witness sharpness, fix \(c=e_0\) (an odd vertex) and the even neighbor set \(U_0=\{c+e_i:0\le i<d\}\). Set

\[
F_{\mathrm{dep}}=\{\{u,u+e_0\}:u\in U_0\}.
\]

Let \(w=e_1+e_2\) and \(U_1=(U_0\setminus\{c+e_{d-1}\})\cup\{w\}\), where \(d\ge4\) makes \(w\) distinct from all elements of \(U_0\). Set

\[
F_{\mathrm{ind}}=\{\{u,u+e_0\}:u\in U_1\}.
\]

Each is a matching of exactly \(d\) edges: translation by \(e_0\) gives distinct odd partners for distinct even endpoints.

## Proof

**1. Cut rank and unperturbed entropy.** Let \(B\) be the \(m\times m\) binary incidence matrix from odd to even cube vertices, and let \(A=\left(\begin{smallmatrix}0&B\\B^T&0\end{smallmatrix}\right)\) be the full adjacency matrix. Hein–Eisert–Briegel's graph-state Schmidt-rank theorem identifies cut entropy with \(\operatorname{rank}_{\mathbb F_2}B\), and all nonzero Schmidt coefficients are equal.

Write \(T_i\) for translation by \(e_i\). The \(T_i\) commute and \(T_i^2=I\), hence \(A=\sum_iT_i\) satisfies \(A^2=dI=0\). In the group algebra, use independent commuting nilpotent variables \(y_i=T_i+I\) with \(y_i^2=0\). Since \(d\) is even, \(A=\sum_i y_i\). An invertible linear change of the \(y_i\), which respects their square-zero relations in characteristic two, takes this nonzero linear form to \(y_0\). Multiplication by \(y_0\) has rank \(2^{d-1}\): exactly half of the squarefree monomial basis is mapped bijectively to the other half. Consequently \(\operatorname{rank}A=2^{d-1}\), \(\operatorname{rank}B=r=2^{d-2}=m/2\), and

\[
\operatorname{im}B=\ker B^T,\qquad \operatorname{im}B^T=\ker B.
\]

**2. Minimum-distance input.** Key–Seneviratne's 2007 hypercube code theorem gives that, for even \(d\ge4\), the binary code \(C_d=\operatorname{im}A\) has minimum nonzero Hamming weight exactly \(d\). The 2007 article states this for all even \(d\ge4\) in its Section 3 and discusses the \([2^d,2^{d-1},d]_2\) parameters. Because \(A\) respects parity exchange, a nonzero vector supported on either parity class and belonging to \(C_d\) has weight at least \(d\). In particular, fewer than \(d\) distinct coordinate vectors on \(E\) are linearly independent modulo \(\operatorname{im}B\), and the analogous assertion holds on \(O\) modulo \(\operatorname{im}B^T\). This established code-distance theorem is a cited nontrivial premise, not a new claim.

**3. Independent rank updates.** We use the following elementary matrix lemma. If \(X\) has rank \(r\), \(U\) and \(V\) each have \(k\) columns, and their columns are independent modulo \(\operatorname{col}X\) and modulo \(\operatorname{row}X\), respectively, then

\[
\operatorname{rank}(X+UV^T)=r+k.
\]

Indeed, put \(X\) into block form \(\operatorname{diag}(I_r,0)\) by invertible row and column operations. The lower blocks of the transformed \(U\) and \(V\) have full column rank \(k\). Block-triangular row and column operations preserving \(X\) remove their upper blocks, so the updated matrix is a direct sum of \(I_r\) and a rank-\(k\) outer product. This proves the lemma without assuming invertibility of \(X\).

An omitted matching \(F=\{\{u_i,v_i\}\}_{i=1}^k\) changes the cut matrix from \(B\) to \(B+UV^T\), where \(U\) and \(V\) comprise the distinct even and odd endpoint indicator vectors. For \(k<d\), the minimum-distance statement in Step 2 supplies the two quotient-space independence conditions. The rank lemma yields \(\operatorname{rank}(B+UV^T)=r+k\), proving the universal formula.

**4. The dependent matching at \(k=d\).** For \(F_{\mathrm{dep}}\), let the columns of \(U\) be the \(d\) even-neighbor indicators of \(c=e_0\), and let \(V\) be the odd-neighbor indicators of the even zero vertex (the odd endpoints are precisely \(e_i\)). Their sums are \(U\mathbf1=B\delta_c\) and \(V\mathbf1=B^T\delta_0\). By the same minimum-distance theorem, the only coefficient relations modulo \(\operatorname{im}B\) or \(\operatorname{im}B^T\) are \(\mathbf0\) and \(\mathbf1\).

Let \(y\) be an odd-coordinate vector in \(\ker(B+UV^T)\), and set \(q=V^Ty\). The equation \(By=Uq\) forces \(q\in\{\mathbf0,\mathbf1\}\). The map \(V^T:\ker B\longrightarrow\mathbb F_2^d\) has image exactly the even-coordinate-sum hyperplane, since its annihilator is the one-dimensional span of \(\mathbf1\). If \(q=\mathbf0\), the solutions have dimension \(\dim\ker B-(d-1)=r-d+1\). If \(q=\mathbf1\), then \(By=B\delta_c\) so \(y=\delta_c+z\) for \(z\in\ker B\). Yet \(V^T\delta_c\) is the single indicator corresponding to \(i=0\), and \(V^Tz=\mathbf1+V^T\delta_c\) would have odd weight \(d-1\), contrary to the even-hyperplane image. Therefore no such solution exists. Hence \(\operatorname{rank}(B+UV^T)=m-(r-d+1)=r+d-1\).

**5. The independent matching at \(k=d\).** Replace the even endpoint \(c+e_{d-1}\) by \(w=e_1+e_2\). Every proper nonempty subset of the resulting \(d\) endpoint indicators has weight less than \(d\) and so cannot lie in \(\operatorname{im}B\). Their complete sum also lies outside \(\operatorname{im}B\): its image under \(B^T\) equals the XOR of the neighbor indicators of the two distinct even vertices \(c+e_{d-1}\) and \(w\), and these neighborhoods differ in every cube of dimension at least three. Translating all endpoints by \(e_0\) identifies the same independence property for the odd partners modulo \(\operatorname{im}B^T\). Apply Step 3 with \(k=d\) to obtain rank \(r+d\).

This completes both the all-placement theorem and the sharpness witnesses for every even \(d\ge4\).

## Verification

The standalone `checks/verify.py` uses integer-only Gaussian elimination over \(\mathbb F_2\); running `python checks/verify.py` produces the supplied `checks/verification_output.txt`. Exhaustive enumeration covers every matching with one, two, or three edges in \(Q_4\) (respectively 32, 400, 2496 cases). Reproducibly seeded finite samples cover matching sizes through seven on \(Q_6\) and \(Q_8\). Explicit dependent and independent threshold matchings are checked in each of these three even dimensions. Additional odd-dimensional single-edge tests document the parity boundary. There are 4031 explicitly counted matching-perturbation rank comparisons in the log, besides the initial-rank checks. No finite calculation is used to replace the universal mathematical argument or the cited hypercube code-distance theorem.

## Relationship to prior work

The graph-state cut-rank identity and equality of Schmidt coefficients come from Hein, Eisert and Briegel (2003); the broader graph-state treatment by Hein and collaborators (2006) includes general one-edge entanglement change bounds. The even-cube binary neighborhood-code parameters and minimum-distance theorem are from Key and Seneviratne (2007), independently restated by Seneviratne (2016). Here these *existing* ingredients are combined with a quotient-space rank-update analysis to establish a uniform all-matching statement, plus sharp, opposite threshold configurations at \(k=d\). The case \(d=4,k=1\) is already covered by an earlier exact two-dimensional periodic-grid calculation and is not proposed as a new special case. The result neither claims that the combinatorial code bound nor the general graph-state rank identity is novel. No matching-fault theorem with this exact threshold was identified in the inspected primary texts; historical priority is provisional.

## Limitations

Only pure ideal graph states, even cube dimensions, the parity bipartition, and vertex-disjoint omitted edges are classified. For larger fault sets, adjacent omissions, arbitrary noise, measurements, circuit depth, or alternative bipartitions, the displayed additive law need not apply. The odd-dimensional cube is outside the asserted law: \(A_d^2=I\) and the unperturbed parity cut has full rank; each single-edge omission lowers the rank by one. The novelty judgment has not undergone independent expert validation.

## References

1. M. Hein, J. Eisert, H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130, first publicly posted 2003-07-18. https://arxiv.org/abs/quant-ph/0307130 ; full text https://arxiv.org/html/quant-ph/0307130v7 .
2. M. Hein and collaborators, *Entanglement in graph states and its applications*, arXiv:quant-ph/0602096, 2006. https://arxiv.org/abs/quant-ph/0602096 ; full text https://arxiv.org/html/quant-ph/0602096v1 .
3. J. D. Key and P. Seneviratne, *Permutation decoding for binary self-dual codes from the graph \(Q_n\) where \(n\) is even*, 2007, DOI:10.1142/9789812772022_0010. Author-uploaded full text https://www.researchgate.net/publication/268243979_Permutation_decoding_for_binary_self-dual_codes_from_the_graph_Q_n_where_n_is_even .
4. P. Seneviratne, *Generalized hypercube graph \(Q_n(S)\), graph products and self-orthogonal codes*, J. Algebra Combin. Discrete Appl. 3(1) (2016), 37–44, DOI:10.13069/jacodesmath.13099. https://jacodesmath.com/index.php/jacodesmath/article/download/29/24/45 .
