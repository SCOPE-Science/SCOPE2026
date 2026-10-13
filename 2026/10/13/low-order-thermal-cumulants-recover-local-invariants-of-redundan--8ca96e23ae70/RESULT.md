# Low-order thermal cumulants recover local invariants of redundancy-free Pauli anticommutation graphs
## Finding
Let \(H=\sum_{i=1}^{m}J_iO_i\) be a redundancy-free Pauli Hamiltonian, with normalized trace \(\operatorname{tr}\), Hermitian Pauli involutions \(O_i\), and anticommutation graph \(G=(V,E)\). Put \(x_i=J_i^2\) and
\[
P_r=\sum_i x_i^r,\qquad E_x=\sum_{\{i,j\}\in E}x_ix_j,
\]
\[
Q_x=\sum_{\{i,j\}\in E}x_ix_j(x_i+x_j),\qquad
W_x=\sum_i\sum_{\{j,k\}\subseteq N(i)}x_ix_jx_k,
\]
where each unordered pair \(\{j,k\}\) of neighbors of \(i\) is counted once, and let
\[
T_x=\sum_{\{i,j,k\}\text{ a triangle of }G}x_ix_jx_k.
\]
Then for \(Z(\beta)=\operatorname{tr}(e^{-\beta H})\),
\[
\log Z(\beta)=\frac{P_1}{2}\beta^2-\frac{P_2+2E_x}{12}\beta^4
+\left(\frac{P_3}{45}+\frac{Q_x+W_x-T_x}{15}\right)\beta^6+O(\beta^8).
\]
In particular,
\[
\operatorname{tr}(H^4)=3P_1^2-2P_2-4E_x,
\]
\[
\operatorname{tr}(H^6)=15P_1^3-30P_1P_2+16P_3-60P_1E_x+48Q_x+48W_x-48T_x.
\]
The fourth coefficient therefore determines the weighted total mass of anticommuting pairs. With equal nonzero coupling magnitudes, rescaled so that \(J_i^2=1\), a \(d\)-regular graph with \(m\) vertices and \(t\) triangles obeys
\[
c_4=-\frac{m(d+1)}{12},\qquad
c_6=\frac{m}{45}+\frac{m d(d+1)/2-t}{15},
\]
where \(c_4\) and \(c_6\) are the coefficients of \(\beta^4\) and \(\beta^6\) in \(\log Z(\beta)\). Hence, for fixed \(m\), those two graph-dependent cumulants recover \(d\) and \(t\). Equal-coupling regular redundancy-free Pauli Hamiltonians with the same number of terms but different degrees or triangle counts are therefore non-isospectral.

## Assumptions and scope
Redundancy-free means that every trace word in which at least one Hamiltonian term occurs an odd number of times has zero normalized trace. The Pauli specialization adds \(O_i^2=I\) and \(O_iO_j=(-1)^{a_{ij}}O_jO_i\), where \(a_{ij}=1\) exactly on anticommutation edges. These are precisely the structural ingredients used below. Couplings may be arbitrary real numbers in the weighted formulas. The regular-graph corollary assumes all coupling magnitudes are equal and nonzero and then rescales them to unit magnitude.

The statement concerns only the first nontrivial high-temperature coefficients. It does not claim that these invariants reconstruct the whole anticommutation graph, that matching them implies isospectrality, or that the expansion changes the complexity thresholds established for bounded graph degree.

## Proof
Redundancy-freeness removes every monomial in \(\operatorname{tr}(H^k)\) having an odd multiplicity. Thus \(\operatorname{tr}(H^2)=P_1\). At order four, the surviving multiplicity patterns are \((4)\) and \((2,2)\). For a pair \(A,B\), the six words containing two copies of each have total trace-sign \(6\) when \(A\) and \(B\) commute and \(2\) when they anticommute: the alternating words \(ABAB\) and \(BABA\) change sign, while the other four do not. Relative to the commuting baseline, each anticommutation edge therefore contributes \(-4x_ix_j\). The commuting baseline is the fourth moment of independent signed terms,
\[
3P_1^2-2P_2,
\]
which proves
\[
\operatorname{tr}(H^4)=3P_1^2-2P_2-4E_x.
\]

At order six the surviving multiplicity patterns are \((6)\), \((4,2)\), and \((2,2,2)\). For a \((4,2)\) pair there are fifteen words. Their sign sum is \(15\) for a commuting pair and \(3\) for an anticommuting pair: among the fifteen placements of the two copies of one letter, nine have even crossing parity and six have odd crossing parity. Hence an edge contributes the correction
\[
-12x_ix_j(x_i+x_j).
\]

For three distinct terms with multiplicity pattern \((2,2,2)\), there are ninety words. Their total sign depends only on the induced three-vertex anticommutation graph. For zero, one, two, or three edges the sign sums are respectively
\[
90,\qquad30,\qquad18,\qquad6.
\]
These counts follow by separating commuting letters. With one edge, the six signed two-letter arrangements sum to \(2\), and the commuting third letter has \(15\) placements, giving \(30\). With two edges forming a path, the two copies of the central letter have signed placement sum \(3\), while the four remaining slots contain two copies of each mutually commuting endpoint in \(6\) ways, giving \(18\). With three edges, successive signed choices give \(3\cdot2=6\). Therefore for a triple \(\{i,j,k\}\) the correction to the commuting value is
\[
-60(a_{ij}+a_{ik}+a_{jk})
+48(a_{ij}a_{ik}+a_{ij}a_{jk}+a_{ik}a_{jk})
-48a_{ij}a_{ik}a_{jk}.
\]
Multiplication by \(x_ix_jx_k\) and summation gives three graph sums. The first satisfies
\[
\sum_{\{i,j,k\}}x_ix_jx_k(a_{ij}+a_{ik}+a_{jk})=P_1E_x-Q_x.
\]
The quadratic edge products sum to \(W_x\), and the cubic edge product sums to \(T_x\). Combining these triple corrections with the \((4,2)\) correction produces
\[
\operatorname{tr}(H^6)=15P_1^3-30P_1P_2+16P_3-60P_1E_x+48Q_x+48W_x-48T_x.
\]

Now write
\[
Z(\beta)=1+\frac{P_1}{2}\beta^2+\frac{\operatorname{tr}(H^4)}{24}\beta^4+rac{\operatorname{tr}(H^6)}{720}\beta^6+O(\beta^8).
\]
Expanding the logarithm gives
\[
[\beta^4]\log Z=\frac{\operatorname{tr}(H^4)}{24}-\frac{P_1^2}{8}
=-\frac{P_2+2E_x}{12},
\]
and
\[
[\beta^6]\log Z=\frac{\operatorname{tr}(H^6)}{720}-\frac{P_1\operatorname{tr}(H^4)}{48}+\frac{P_1^3}{24}
=\frac{P_3}{45}+\frac{Q_x+W_x-T_x}{15}.
\]
This proves the weighted statement.

For equal unit-magnitude couplings, \(P_1=P_2=P_3=m\), \(E_x=|E|\), \(Q_x=2|E|\), \(W_x=\sum_v\binom{d_v}{2}\), and \(T_x=t\). If \(G\) is \(d\)-regular, then \(|E|=md/2\) and \(W_x=m\binom d2\). Substitution yields the displayed formulas for \(c_4\) and \(c_6\), so \(d\) and then \(t\) are recovered exactly.

## Verification
The algebraic proof is independent of finite experimentation. A standalone checker enumerates every simple graph on four labeled vertices, evaluates all even trace words through degree six directly from the pairwise anticommutation signs, and compares those values with the closed formulas above for a fixed nondegenerate integer coupling vector. It also checks the equal-coupling regular specialization on all regular graphs in that census. The checker is corroborative: its finite enumeration is not used to justify the all-size theorem.

## Relationship to prior work
Hastings and Schmidhuber introduce redundancy-free Hamiltonians, specialize Pauli instances to an anticommutation graph, and study the partition function through a high-temperature polymer expansion. Their paired-word analysis explains normalized traces by anticommutation crossing signs. The paper does not state the fourth- and sixth-order closed graph-invariant formulas above, nor the inverse statement that the first two graph-dependent cumulants recover degree and triangle count in the regular equal-coupling case.

Ralli, Weaving, and Love study the narrower class of noncontextual Pauli Hamiltonians and derive efficient eigenspace structure. Their full text does not formulate thermal moment identities of this kind, and noncontextuality is a different restriction from arbitrary redundancy-free anticommutation graphs. Ruh, Elman, and Chapman study frustration graphs for free-fermion solvability, including non-generic solvability, but their graph criteria concern exact fermionic mappings rather than low-order thermal cumulants.

## Limitations
The graph formulas depend essentially on redundancy-freeness. Algebraic relations among distinct Pauli terms can create additional nonzero trace words and invalidate the stated moment reduction. The weighted quantities may also hide edges incident only to zero-coupling terms. In the general weighted case, the sixth coefficient determines only the combination \(Q_x+W_x-T_x\), not \(W_x\) and \(T_x\) separately. Triangle recovery uses the additional equal-coupling regularity hypothesis. No assertion is made about higher cumulants, full graph reconstruction, or computational hardness from these low-order invariants alone.

## References
1. M. B. Hastings and A. Schmidhuber, “On The Complexity of Redundancy-Free Quantum Hamiltonians,” arXiv:2610.03697v1, first public 2026-10-02.
2. A. Ralli, T. Weaving, and P. J. Love, “Noncontextual Pauli Hamiltonians,” arXiv:2506.19778v1, 2025.
3. J. Ruh, S. J. Elman, and A. Chapman, “A graph-theoretic analysis of non-generic free-fermion solvability by Krylov decompositions,” arXiv:2610.03557v1, 2026.
