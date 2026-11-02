# Bipartiteness, strong reality, and Frobenius–Schur spectra of graphical 2-groups

## Finding

Let \(\Gamma\) be a finite simple graph with ordered vertex set \(\{1,\ldots,n\}\), edge set \(E\), and \(m=|E|\). Let \(k=\mathbb F_q\), where \(q\) is a power of two. The associated graphical group has a complete complex irreducible Frobenius–Schur indicator distribution controlled by weighted quadratic forms. In particular, the following four conditions are equivalent:

1. \(\Gamma\) is bipartite.
2. Every complex irreducible character of the graphical group has Frobenius–Schur indicator \(+1\).
3. Every group element is conjugate to its inverse by an involution (strong reality).
4. Every group element is conjugate to its inverse (reality).

The equivalence holds independently for every choice of \(q\) of characteristic two. More precisely, define \(Q_t(x)=\sum_{\{i,j\}\in E,\ i<j}t_{ij}x_ix_j\) for \(t\in k^E\), and let \(W_t\) be the alternating matrix with \((i,j)\)-entry \(t_{ij}\) along edges and zero otherwise. Write \(\operatorname{rank}_k W_t=2s\). There are exactly \(q^{n-2s}\) distinct irreducible characters above the central character \(\lambda_t(z)=(-1)^{\operatorname{Tr}_{k/\mathbb F_2}(\sum t_{ij}z_{ij})}\); all have degree \(q^s\), and all have the same indicator

\[
\nu_t=q^{s-n}\sum_{x\in k^n}(-1)^{\operatorname{Tr}_{k/\mathbb F_2}(Q_t(x))}.
\]

Let \(R_t=\ker W_t\). The indicator is zero precisely when \(Q_t|_{R_t}\) is nonzero. Otherwise \(Q_t\) descends to a nonsingular quadratic form on \(k^n/R_t\), and \(\nu_t\) is the corresponding finite-field Arf sign (either \(+1\) or \(-1\)). Thus the displayed formula determines the complete indicator spectrum, including multiplicities, for every graph.

## Assumptions and scope

All graphs here are finite, simple, nonempty, and allowed to have isolated vertices. Let \(k^E\) have coordinates indexed by edges with the smaller endpoint written first. The underlying set of \(G=G_\Gamma(k)\) is \(k^n\times k^E\), and its multiplication is

\[
(x,z)(y,w)=(x+y,z+w+\beta(x,y)),\qquad
\beta(x,y)_{ij}=x_i y_j\quad(i<j,\ \{i,j\}\in E).
\]

The central subgroup \(Z=\{(0,z):z\in k^E\}\) need not be the full center if there are isolated vertices. Its characters \(\lambda_t\) nevertheless index the sectors in the theorem. The group is finite, of class at most two and exponent at most four. Its multiplication is associative because \(\beta\) is bilinear. Define the alternating commutator form \(B_t(x,y)=Q_t(x+y)-Q_t(x)-Q_t(y)\), represented by \(W_t\). All ranks are over \(k\); the trace always means the absolute field trace to \(\mathbb F_2\).

## Proof

**Step 1 (irreducible degrees and their multiplicities).** Fix a central character \(\lambda_t\). The quotient of the complex group algebra by the relations \((0,z)=\lambda_t(z)1\) is the twisted group algebra of the additive group \(k^n\) with multiplier \(\lambda_t(\beta(x,y))\). Two basis elements commute in this algebra exactly when their commutator pairing \((-1)^{\operatorname{Tr}(B_t(x,y))}\) is one. Its radical is exactly \(R_t=\ker W_t\): if a vector pairs trivially with all others under the trace pairing, all its \(k\)-linear pairing coefficients vanish because the absolute trace pairing on \(k\) is nondegenerate. Hence the center of this semisimple algebra has dimension \(|R_t|=q^{n-2s}\). Each simple summand has matrix size \(q^s\), by the standard finite Heisenberg/twisted-group-algebra decomposition, since the quotient by the radical has size \(q^{2s}\). Thus precisely \(q^{n-2s}\) irreducibles lie above \(\lambda_t\), each of degree \(q^s\). Summing their squared degrees gives \(q^n\) for each \(t\), hence \(|G|=q^{n+m}\) across all central characters, as required.

**Step 2 (indicator formula).** The square of any group element is

\[
(x,z)^2=(0,\beta(x,x)),\qquad
\beta(x,x)_{ij}=x_i x_j.
\]

It follows that every irreducible \(\chi\) lying above \(\lambda_t\) satisfies \(\chi((x,z)^2)=q^s(-1)^{\operatorname{Tr}(Q_t(x))}\). The defining Frobenius–Schur average over the \(q^{n+m}\) group elements therefore gives exactly the displayed \(\nu_t\).

**Step 3 (the zero and Arf cases).** For \(r\in R_t\) and all \(x\), \(Q_t(x+r)=Q_t(x)+Q_t(r)\). Translation by \(r\) forces the Gauss sum to vanish whenever \(\operatorname{Tr}(Q_t(r))=1\). If the restriction \(Q_t|_{R_t}\) is nonzero, then some scalar multiple of an \(r\) has trace-one value, since \(Q_t(ar)=a^2Q_t(r)\) and the field-trace pairing is nondegenerate. Conversely if the restriction is zero, the sum equals \(q^{\dim R_t}\) times the quadratic Gauss sum of the nonsingular induced form on \(k^n/R_t\). For its \(2s\)-dimensional symplectic basis, the familiar hyperbolic/anisotropic two-plane calculation gives the Gauss sum \(\pm q^s\); the sign is the Arf sign. The formula therefore yields only the allowed values \(0,\pm1\) with the asserted criterion.

**Step 4 (bipartite graphs are totally orthogonal and strongly real).** If \(V=L\sqcup R\) is a bipartition, then \(Q_t(x)=x_L^{\mathsf T}M_t x_R\). Put \(r=\operatorname{rank}M_t\). Then \(\operatorname{rank}W_t=2r\), while direct summation first over \(x_L\) gives \(\sum_x(-1)^{\operatorname{Tr}Q_t(x)}=q^{n-r}\). Therefore \(\nu_t=+1\) for every \(t\), and hence for every irreducible character. Moreover, for any \(g=(x,z)\), set \(h=(x_R,0)\), where \(x_R\) is zero on \(L\) and agrees with \(x\) on \(R\). There are no edges within \(R\), so \(h^2=1\). If \(x_R\ne0\), then \(h\) has order exactly two. The central commutator \([h,g]\) has edge coordinate \(x_i x_j\) for every edge, which equals the square coordinate of \(g\). In an exponent-four group of class two, this implies \(hgh^{-1}=g^{-1}\). If \(x_R=0\), then \(g^2=1\): for \(g\ne1\), choose the inverting involution \(h=g\), and for \(g=1\), choose any nonidentity vertex generator, which is an involution because \(n\ge1\). Thus every element is inverted by an involution.

**Step 5 (an odd cycle obstructs reality).** Suppose \(\Gamma\) is not bipartite and choose a simple odd cycle \(C\) of length \(\ell\). Pick \(a\in k\) with \(\operatorname{Tr}(a)=1\). Put \(t_{ij}=a\) on the edges of \(C\), and zero on all other edges, including chords. Let \(r\in k^n\) have coordinate one on the cycle vertices and zero elsewhere. Every cycle vertex has exactly two incident selected edges, so \(W_t r=0\), whereas \(Q_t(r)=\ell a=a\ne0\). Step 3 gives \(\nu_t=0\), and Step 1 guarantees the existence of irreducibles in that sector. Such irreducibles are not real-valued, so \(G\) cannot be a real group. Every strongly real group is real. Combined with Step 4, all four conditions are equivalent.

**Step 6 (a quaternionic witness).** For the complete graph on four vertices over \(\mathbb F_2\), set all six edge weights to one. Then \(W_t\) has rank four and \(Q_t(x)=\binom{\mathrm{wt}(x)}2\bmod2\). Its Gauss sum is \(1+4-6-4+1=-4\), hence \(\nu_t=2^{2-4}(-4)=-1\). Step 1 gives exactly one irreducible in this sector, of degree four. Consequently there are graphical groups with quaternionic irreducibles as well as those with nonreal irreducibles.

## Verification

A standalone finite-field checker enumerates all labeled simple graphs with at most four vertices over \(\mathbb F_2\). For each edge-character choice it computes the weighted adjacency rank and the quadratic Gauss sum, checking that the inferred indicator is \(0\), \(+1\), or \(-1\), that bipartite graphs have only \(+1\), and that every nonbipartite graph has some zero indicator. It also tests a triangle, a four-cycle and the complete graph on four vertices over \(\mathbb F_4\). For each graph, the independent identity relating involution counts and the indicator-weighted character degrees is checked. The exact run prints `GRAPHICAL_FS_INDICATORS_OK 75 3 nonbipartite 24 negative 1`. Execute `python3 check_graphical_fs.py` with the standard Python library. These finite checks do not prove the assertions for arbitrary graphs or fields; Steps 1–6 are the general proof.

## Relationship to prior work

O'Brien and Voll, *Enumerating classes and characters of p-groups* (arXiv:1203.3050v1, 2012-03-14), derive class and character distributions using the Lazard correspondence in nilpotency class strictly less than the characteristic. Their hypotheses therefore do not treat class-two graphical groups at characteristic two, and their results do not state the graph bipartiteness/reality criterion or indicators. Rossmann and Voll, *Groups, graphs, and hypergraphs: average sizes of kernels of generic matrices with support constraints* (arXiv:1908.09589v2), develop the graphical-group construction and class-number zeta-function formulas. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields* (arXiv:2107.05564v1; DOI:10.1112/blms.12665), determines conjugacy class-size distributions and describes related character-degree enumeration questions. The latter published full text does not state Frobenius–Schur indicators or graph-theoretic reality conditions. The present result concerns ordinary complex Frobenius–Schur types, a refinement not implied by conjugacy-class-size or character-degree distributions alone. Generic theory of quadratic Gauss sums underlies the proof and is not claimed as new.

## Limitations

The theorem applies to the displayed graphical group over finite fields of characteristic two, not to arbitrary class-two groups or characteristic-odd graphical groups. It gives indicators and multiplicities per central-character sector, not a classification of irreducible character values at every element. The result does not claim priority over all unindexed literature on strongly real special two-groups; an equivalent theorem under another construction remains a residual historical risk. Its finite checker covers only small graph sizes and field orders.

## References

1. E. A. O'Brien and C. Voll, *Enumerating classes and characters of p-groups*, arXiv:1203.3050v1, first publicly available 2012-03-14, https://arxiv.org/abs/1203.3050.
2. T. Rossmann and C. Voll, *Groups, graphs, and hypergraphs: average sizes of kernels of generic matrices with support constraints*, arXiv:1908.09589v2, https://arxiv.org/html/1908.09589v2.
3. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564v1, https://arxiv.org/abs/2107.05564; DOI:10.1112/blms.12665.
4. F. G. Frobenius and I. Schur, classical Frobenius–Schur indicator theorem (used as standard background).
