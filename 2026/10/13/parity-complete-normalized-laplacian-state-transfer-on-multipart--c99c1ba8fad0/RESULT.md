# Parity-complete normalized-Laplacian state transfer on multipartite twin-pair networks

## Finding
For every pair of integers \(r\ge 2\) and \(m\ge 1\), let \(G_{r,m}=K_{\underbrace{2,\ldots,2}_{r\text{ parts}},m}\) be the connected simple complete multipartite graph with \(r\) independent pairs and one additional independent part of size \(m\). Set \(d=m+2r-2\). Let \(A\) be its adjacency matrix, \(D\) the positive diagonal degree matrix, \(L=I-D^{-1/2}AD^{-1/2}\), and \(U(t)=\exp(-itL)\).

**Theorem.** Distinct-vertex perfect state transfer \(U(t)e_u=\zeta e_v\) at some positive time \(t\), with \(|\zeta|=1\), is possible on \(G_{r,m}\) **if and only if** \(r\) is odd and \(m\equiv2\pmod4\). In those cases, the only possible transfers are between the two vertices of a size-two part (including the last part if \(m=2\)). All successful times, for every such pair, are exactly
\[
 t_j=(2j+1)\frac{d\pi}{2},\qquad j=0,1,2,\ldots.
\]
At the first successful time the **entire** evolution operator is the direct sum
\[
 U(d\pi/2)=\left(\bigoplus_{i=1}^{r}\begin{pmatrix}0&1\\1&0\end{pmatrix}\right)\oplus\left(\frac{2}{m}J_m-I_m\right).
\]
Thus every designated twin pair swaps simultaneously, and the remaining part undergoes an exact reflection about its uniform vector. In particular, the irregular graph \(K_{2,2,2,6}\), whose vertices have degrees \(10\) and \(6\), performs three disjoint perfect swaps simultaneously at the first time \(5\pi\).

## Assumptions and scope
All graphs are finite, connected, undirected, simple, loopless, unweighted, and have \(r\ge2\) independent size-two parts and exactly one additional independent part of size \(m\ge1\). The Hamiltonian is the **symmetric normalized Laplacian**, not the combinatorial Laplacian or an oracle-modified search Hamiltonian; a global additive scalar has already been fixed by \(L=I-D^{-1/2}AD^{-1/2}\). The vertex basis vectors \(e_u\) are Euclidean normalized. The sign convention \(\exp(-itL)\) is used; reversing the sign does not change the existence or times of transfer. The degree on every pair vertex is \(d=m+2r-2\), and the degree on every vertex of the last part is \(2r\). The border family \(r=1\) is deliberately excluded: there the transverse eigenvalue below is absent and the corresponding congruence restriction is false.

## Proof
Write \(S=D^{-1/2}AD^{-1/2}=I-L\). For each multipartite cell \(C\), let \(Z_C\) be the vectors supported on \(C\) with coordinate sum zero. Every \(z\in Z_C\) has \(Sz=0\): vertices outside \(C\) see only the sum of the entries of \(z\), and there are no edges inside \(C\). These spaces are mutually orthogonal, so the zero eigenspace contains \(Z=\bigoplus_C Z_C\), of dimension \(r+m-1\).

For the \(r\) small cells, introduce the unit vectors \(s_i=(e_{i,1}+e_{i,2})/\sqrt2\), and for the last cell introduce \(b=m^{-1/2}\sum_{v\in C_{r+1}}e_v\). The orthogonal complement of \(Z\) is \(W=\operatorname{span}\{s_1,\ldots,s_r,b\}\). Its small-cell matrix has zero diagonal and constant off-diagonal entry \(2/d\). Each difference \(s_i-s_j\) is therefore an eigenvector with eigenvalue \(-2/d\), producing an eigenspace \(T=\{\sum_i c_i s_i:\sum_i c_i=0\}\) of dimension \(r-1\).

On the remaining plane \(\operatorname{span}\{\bar s,b\}\), where \(\bar s=r^{-1/2}\sum_i s_i\), the matrix of \(S\) is exactly
\[
 B=\begin{pmatrix}\frac{2(r-1)}d&\sqrt{\frac md}\\[2pt]\sqrt{\frac md}&0\end{pmatrix}.
\]
Since \(d=m+2(r-1)\), its trace equals \(1-m/d\) and its determinant equals \(-m/d\). Its two eigenvalues are \(1\) and \(-m/d\). In particular, both are nonzero. This proves \(Z=\ker S\) (not merely an inclusion) and yields the orthogonal eigenspace decomposition with normalized-Laplacian eigenvalues \(1\) on \(Z\), \(1+2/d\) on \(T\), \(0\) on the Perron line, and \(1+m/d\) on the other plane line. If \(m=2\), the last two negative-\(S\) eigenvalues coincide and their spaces combine; the conclusions below remain unchanged.

**Only twin pairs can transfer.** The projection of a vertex \(e_u\) to \(Z\) is \(e_u-|C|^{-1}\sum_{v\in C}e_v\) if \(u\in C\), and zero for a singleton cell. Perfect transfer between distinct vertices requires their projections to each spectral eigenspace to coincide up to one common unit scalar (with the scalar phase of that eigenvalue). In particular their nonzero \(Z\)-projections must be parallel. For vertices in different cells these projections have disjoint support, so cannot be parallel unless both vanish; there is only one possible singleton cell. For two distinct vertices of one cell of size at least three, the projected vectors are not parallel: the coordinate at any third vertex forces the scalar to be \(1\), contradicting the two distinguished coordinates. In a size-two cell, the two projected vectors are opposite. Thus any possible transfer must exchange two vertices of a size-two cell.

Fix such a cell and write its vertices as \(u,v\). Their components in \(Z\) are opposite, while their components in \(Z^\perp\) agree. If the pair is one of the designated first \(r\) cells, its projections onto the Perron, transverse, and second-plane spaces are all nonzero: the Perron vector is strictly positive; \(r\ge2\) gives a nontrivial \(T\)-component; and \(B\)'s nonzero off-diagonal entry makes its eigenvectors have nonzero \(\bar s\)-components. If instead the last cell itself has size \(m=2\), the projection of its vertex onto \(T\) vanishes, but its projection onto the second-plane eigenvalue \(-m/d=-2/d\) is nonzero; this is precisely the same eigenvalue as on \(T\). Thus **in both cases** perfect transfer requires the phase on the Perron space to equal \(1\), the phase on \(Z\) to equal \(-1\), and the phases of all nonzero supported negative-\(S\) eigenvalues to equal \(1\). The Perron condition is automatic because the Laplacian Perron eigenvalue is zero. The remaining phase conditions (with the last two identical when \(m=2\)) give
\[
 e^{-it}=-1,\qquad e^{-it(1+2/d)}=1,\qquad e^{-it(1+m/d)}=1.
\]
The first equality gives \(t=h\pi\), where \(h\) is a positive odd integer. Substitution into the other two shows that both \(2h/d\) and \(mh/d\) must be **odd integers**. Since \(h\) is odd, \(2h/d\) is an odd integer exactly when \(d=2q\) with \(q\) odd and \(q\mid h\). Writing \(h=q\ell\), with \(\ell\) odd, the second quotient is \(m\ell/2\); it is an odd integer exactly when \(m\equiv 2\pmod4\). As \(q=d/2=m/2+r-1\), the condition that \(q\) be odd is then equivalent to \(r\) odd. Conversely these two congruences imply all three required phases whenever \(h\) is an odd multiple of \(q\). This proves necessity, sufficiency, and the complete successful-time set \(t=(2j+1)q\pi\).

Finally, at \(q\pi\), \(U=+I\) on \(Z^\perp\) and \(U=-I\) on \(Z\). Denote by \(P_Z\) the orthogonal projector onto the direct sum of within-cell zero-sum spaces. Then \(U=I-2P_Z\). On a cell of cardinality \(a\), \(P_Z=I_a-J_a/a\), hence \(U|_C=2J_a/a-I_a\). For each \(a=2\) this is a swap, and for the last cell of size \(m\) it is exactly the displayed reflection. This proves the global matrix statement without appealing to finite enumeration. \(\square\)

## Verification
The accompanying standalone `verify.py` uses only Python's standard library and exact rational fractions. Reproduce with `python3 verify.py` from the package directory. It constructs the full vertex-level transition matrix \(P=D^{-1}A\), which is similar to \(S\), for all \(2\le r\le7\) and \(1\le m\le14\). It checks the four-factor annihilating polynomial for \(P\), within-part and transverse eigenvectors, both quotient coefficients, the exact kernel projector obtained from the nonzero eigenvalues, and the parity condition by integer-only divisibility. The output is `VERIFY_OK exact_fraction_graphs=84 transfer_cases=12 first_irregular=K_2_2_2_6 time=5pi`.

The finite checks corroborate algebraic identities and test boundaries; they do not establish universal quantifiers. Those follow from the preceding symbolic decomposition and odd-integer divisibility argument.

## Relationship to prior work
Coutinho and Baptista (2022), Theorem 5, establish general rational-spectrum and strong-cospectrality criteria for perfect transfer under the normalized Laplacian. Their paper supplies the general phase viewpoint but does not give this two-parameter complete-multipartite classification, its sharp parity criterion, all transfer times, or the full simultaneous propagator. Monterde (2021/2022), especially Sections 3 and 6, develops a general theory of strong cospectrality for twins and joins—including normalized adjacency—but does not calculate these exact transfer-time congruences or the full unitary for \(G_{r,m}\). Sun and Das (2020), Theorem 3.1, provide the normalized-Laplacian characteristic polynomial for **all** complete multipartite graphs; their work is a stronger spectral statement and is acknowledged as such, but the spectrum alone does not determine the signs of spectral projectors, the transfer condition, or the explicit propagator without additional argument. Alvir and collaborators (2014/2016) develop normalized-Laplacian transfer under weak graph products and transfer for the *combinatorial* Laplacian on double cones. Their double-cone theorem does not cover the nonregular-base example \(K_{2,2,2,6}\) under the normalized operator.

For comparison with the special regular boundary \(m=2\), this theorem includes known cocktail-party-type state-transfer situations; the substantive contribution is the full parameter classification including **irregular** \(m>2\), global simultaneous swaps, and transfer time formula. The result does not claim a new general strong-cospectrality theorem or a new formula for the general complete-multipartite spectrum.

## Limitations
Only one large (possibly singleton) cell is allowed; no transfer classification is asserted here for arbitrary complete multipartite part-size vectors, nonuniform edge weights, graph potentials, or other Hamiltonians. The restriction \(r\ge2\) is essential to this stated congruence characterization because for \(r=1\) the transverse spectral sector disappears. Search-based literature comparisons may miss synonyms or poorly indexed results; independence from existing research is not claimed. Verification is analytic with reproducible finite tests, not an independent mathematical audit.

## References
1. G. Coutinho and P. Ferreira Baptista, *Quantum Walks in the Normalized Laplacian*, arXiv:2209.04668v1 (first submitted 2022-09-10 UTC), especially Section 3 and Theorem 5. https://arxiv.org/html/2209.04668v1
2. H. Monterde, *Strong Cospectrality and Twin Vertices in Weighted Graphs*, arXiv:2111.01265v2 (2022; first preprint 2021-11-01), especially Sections 3 and 6. https://arxiv.org/html/2111.01265v2
3. S. Sun and K. C. Das, *Normalized Laplacian spectrum of complete multipartite graphs*, Discrete Applied Mathematics 284 (2020), 234–245, DOI:10.1016/j.dam.2020.03.041, particularly Theorem 3.1.
4. R. Alvir, S. Dever, B. Lovitz, J. Myer, C. Tamon, Y. Xu, and H. Zhan, *Perfect State Transfer in Laplacian Quantum Walk*, arXiv:1409.5840v1 (2014), especially the normalized-Laplacian weak-product discussion.
