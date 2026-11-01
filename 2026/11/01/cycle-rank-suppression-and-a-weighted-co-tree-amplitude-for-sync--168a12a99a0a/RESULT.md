# Cycle-rank suppression and a weighted co-tree amplitude for synchronization under graph subdivisions

## Finding
Let \(H=(V,E)\) be a fixed finite connected simple graph with at least one cycle, and fix positive integers \(\ell_e\) for its edges. Write \(r=|E|-|V|+1\). Replace each edge \(e\) by a path of \(L\ell_e\) edges, with internally disjoint paths, to obtain \(G_L\). For independent uniform three-color initialization, synchronous three-color CCA and three-state GHM have the same set of synchronizing initial configurations and the same probability \(p_L\), with

\[
p_L=\left(\frac{27}{4\pi L}\right)^{r/2}\frac{1+o(1)}{\sqrt{\mathcal K_H(\ell)}},\qquad
\mathcal K_H(\ell)=\sum_{T\text{ spanning tree of }H}\prod_{e\notin T}\ell_e.
\]

The exponent is half the cycle rank, and the amplitude is a weighted co-tree polynomial. The shared qualitative synchronization criterion is *not* asserted to be new: it is Theorem 3 of Gravner, Lyu and Sivakoff (2016). The exact finite-subdivision formula and its topology-sensitive asymptotic are the present finding.

## Assumptions and scope
All graphs are finite, undirected, simple and connected. The base graph \(H\) is held fixed while \(L\in\mathbb N\) tends to infinity. Each \(\ell_e\) is a fixed positive integer. For CCA, a vertex of color \(i\in\{0,1,2\}\) advances to \(i+1\pmod3\) exactly if a neighbor currently has that successor color. For GHM, colors one and two advance automatically modulo three; a zero advances to one exactly if it has a neighbor of color one. All vertices update simultaneously. Synchronization means all vertex colors eventually agree at every subsequent time. Initial colors are independent and uniform on three colors.

Fix arbitrary orientations of base edges and a spanning tree. Let \(B\in\{-1,0,1\}^{r\times |E|}\) be the signed fundamental-cycle matrix, one row for each non-tree edge, oriented so that the columns of non-tree edges form an identity matrix. Let \(a_m(s)=[z^s](z^{-1}+1+z)^m\). Then, *exactly* for every integer \(L\ge1\),

\[
p_L=3^{r-L\sum_e\ell_e}\sum_{\substack{\mathbf s\in\mathbb Z^E\\B\mathbf s=0}}\prod_{e\in E}a_{L\ell_e}(s_e).
\]

Only finitely many terms are nonzero, since \(|s_e|\le L\ell_e\). This formula also covers positive, unequal edge lengths and arbitrary cycle overlap; it is independent of the orientations and spanning-tree choice.

## Proof
**1. A common integer-circulation event.** For a coloring \(X:V(G_L)\to\mathbb Z_3\), put \(\delta_C(u,v)\in\{-1,0,1\}\) for the representative of \(X(v)-X(u)\pmod3\). The corresponding GHM increment is \(\delta_G(u,v)=1\) for colors \(0\to1\), \(-1\) for \(1\to0\), and zero otherwise. On a closed directed walk the *net signed counts* of transitions across the three color cuts \(0\leftrightarrow1\), \(1\leftrightarrow2\), and \(2\leftrightarrow0\) are equal, by color-flow conservation at each color. Consequently, for every closed directed walk,

\[\oint\delta_C=3\oint\delta_G.\]

In particular \(\oint\delta_C=0\) iff \(\oint\delta_G=0\), for every cycle. Theorem 3 of Gravner–Lyu–Sivakoff (2016) establishes that, on any finite connected graph, either automaton synchronizes if and only if its initial integer one-form is irrotational. The two synchronization events therefore agree *configuration by configuration*.

**2. Remove modular conditioning.** Along each oriented subdivided base edge \(e\), the CCA increments of successive colors have representatives in \(\{-1,0,1\}\). For a uniform vertex coloring, the collection of these path increments is uniform over all step assignments whose sums \(S_e\) satisfy \(B\mathbf S=0\pmod3\). Conversely, a step assignment satisfying the modular cycle constraints reconstructs three global vertex colorings, one for each root color, with no other ambiguity. If we instead take all individual increments independently and uniformly in \(\{-1,0,1\}\), then \(B\mathbf S\pmod3\) is uniform on \((\mathbb Z/3\mathbb Z)^r\), since the chord columns of \(B\) form the identity and each path sum is uniform modulo three. Therefore

\[p_L=3^r\Pr\{B\mathbf S=0\},\]

where \(S_e\) are now independent sums of \(L\ell_e\) symmetric lazy steps. Expanding their convolution counts gives the stated exact coefficient formula. This conditioning step is essential: unrestricted independent edge differences do *not* have the law of a graph coloring without the modular cycle constraints.

**3. Multivariate local limit and lattice normalization.** Let \(D=\operatorname{diag}(\ell_e)\), and write \(Q=BDB^{\mathsf T}\). The covariance of \(B\mathbf S\) equals \((2L/3)Q\), where \(Q\) is positive definite. The integer columns of \(B\) generate the whole lattice \(\mathbb Z^r\) because of its identity chord block. Each lazy step is aperiodic (its distribution assigns positive mass to zero and both signs). Its characteristic function is \(\phi(t)=(1+2\cos t)/3=1-t^2/3+O(t^4)\) near zero, and has modulus strictly less than one away from zero modulo \(2\pi\). Therefore the Fourier inversion integral for \(\Pr\{B\mathbf S=0\}\) has a unique maximum at zero on the torus. Rescaling the integral by \(L^{-1/2}\), applying the Gaussian limit in a shrinking neighborhood and exponentially bounding its complement yields

\[\Pr\{B\mathbf S=0\}=\left(\frac{3}{4\pi L}\right)^{r/2}(\det Q)^{-1/2}(1+o(1)).\]

No unaccounted parity factor or higher lattice covolume occurs, because of the zero step and the chord identity block.

**4. The co-tree determinant.** By Cauchy–Binet,

\[\det Q=\sum_{J\subseteq E,\ |J|=r}\det(B_J)^2\prod_{e\in J}\ell_e.\]

For a fundamental-cycle matrix, \(\det(B_J)\in\{-1,0,1\}\), and it is nonzero precisely when the *complement* \(E\setminus J\) is a spanning tree. This is the graphic/cographic matrix-tree identity: deleting a full set of independent cycle columns is equivalent to retaining a spanning tree. Hence \(\det Q=\mathcal K_H(\ell)\). Multiplying the local-limit expression by \(3^r\) proves the claimed asymptotic.

## Verification
The included `subdivision_sync_verify.py` uses only the Python 3 standard library. It independently counts every coloring on selected subdivided triangles, diamonds, and complete four-vertex graphs, and compares the result with the exact independent-lazy-walk convolution and co-tree enumeration. The exhaustive graph/color cases comprise six combinations of three base graphs with \(L\in\{1,2\}\). It prints `SUBDIVISION_SYNC_VERIFY_OK 6` on success. These finite experiments check normalization and combinatorial identities but do *not* prove the all-graph formula or infinite asymptotic; those are proved above.

For the uniform subdivision of a triangle, \(r=1\) and \(\mathcal K_H=3\); thus \(p_L\sim3/(2\sqrt{\pi L})\). For a diamond graph (two triangles sharing an edge), \(r=2\) and \(\mathcal K_H=8\); thus \(p_L\sim 27/(4\pi\sqrt8 L)\). The verifier confirms the exact finite-size values \(7/9\), \(47/81\) for the triangle at \(L=1,2\), and \(17/27\), \(769/2187\) for the diamond at \(L=1,2\), respectively.

## Relationship to prior work
Gravner, Lyu and Sivakoff's 2016 Theorem 3 (arXiv:1610.07320v1) already proves the graph-general qualitative equivalence between synchronization and irrotationality for each automaton. In particular, it entails that the synchronization events for CCA and GHM agree, as explained using the three cut counts above; that portion is *not* new. Their Theorem 5 supplies general cycle-related bounds in different regimes. The present claim concerns a different quantitative target: the exact uniform-random count for subdivided graphs, its \(L^{-r/2}\) decay, and the weighted co-tree amplitude. These quantitative statements were not found in the inspected sections of the source.

Matamala and Goles's earlier *Cyclic automata networks on finite graphs* (1995) is relevant historical literature whose full text was unavailable; an equivalent result there cannot be fully excluded. Standard multivariate lattice local limits, Cauchy–Binet, and the graphic matrix-tree identity are ingredients rather than new individual theorems.

## Limitations
The base graph and positive edge weights are fixed in the asymptotic; no uniform assertion is made when the graph itself or its cycle rank grows with \(L\). The formula is for three states, independent uniform colors, simultaneous updating, and *eventual synchronization*; it does not classify other attractors, transient lengths, or arbitrary biased color measures. The relative error is \(o(1)\), not a stated numerical error bound. Originality is assessed against inspected accessible sources and searchable records, not certified against every historical publication. Independent audit has not been performed.

## References
1. Janko Gravner, Hanbaek Lyu, David Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, first submitted 24 October 2016. https://arxiv.org/html/1610.07320v1 . Especially Section 2, definitions (4)–(7), Theorem 3, and Theorem 5.
2. M. Matamala and E. Goles, *Cyclic automata networks on finite graphs*, LATIN 1995, DOI:10.1007/3-540-59175-3_105. Plausible historical background; full text not inspected.
3. The multivariate lattice local limit theorem and the Cauchy–Binet/graphic matrix-tree identity are standard mathematical tools used explicitly in the proof, not cited as new results.
