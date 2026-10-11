# Exchange-sign Borel–Moore homology of two-point graph configurations

## Finding
For every finite connected simple graph \(G\), define \(V=H_1(G;\mathbb Z)\). Let
\[
U_2(G)=\{\{x,y\}:x,y\in |G|,\ x\ne y\}
\]
be the unordered configuration space of two distinct points on the geometric graph, and let \(\mathcal L_{\mathrm{sgn}}\) be the integral rank-one local system whose transport around a particle-exchanging loop is multiplication by \(-1\). Define the integral divided square
\[
D_2(V)=(V\otimes_{\mathbb Z}V)^{\mathrm{flip}},
\]
where the flip exchanges the two tensor factors (without a Koszul sign). There are graph-automorphism-natural isomorphisms
\[
H_i^{\mathrm{BM}}(U_2(G);\mathcal L_{\mathrm{sgn}})
\cong\begin{cases}
D_2(V),&i=2,\\
V,&i=1,\\
0,&i\ne1,2.
\end{cases}
\]
For the first Betti number \(b\), the two nonzero groups therefore have free ranks \(\binom{b+1}{2}\) and \(b\). If \(g\) is any automorphism, put \(a(g)=\operatorname{tr}(g_*\mid V\otimes\mathbb Q)\). Then
\[
\operatorname{tr}(g_*\mid H_2^{\mathrm{BM}}(U_2(G);\mathcal L_{\mathrm{sgn}})\otimes\mathbb Q)
=\frac{a(g)^2+a(g^2)}{2},\qquad
\operatorname{tr}(g_*\mid H_1^{\mathrm{BM}}(U_2(G);\mathcal L_{\mathrm{sgn}})\otimes\mathbb Q)=a(g).
\]
These are statements about Borel–Moore homology with a specified local system, not ordinary singular homology.

## Assumptions and scope
A graph is a finite connected one-dimensional CW complex with its usual topology; stating the result for finite simple graphs excludes no cycle ranks. The ordered configuration space \(F_2(G)\) consists of ordered pairs of distinct geometric points and is a two-sheeted cover of \(U_2(G)\). The sign local system is the associated \(\mathbb Z\)-bundle via the nontrivial character of the deck group \(C_2\). For a tree, \(V=0\) and all these Borel–Moore homology groups are zero. The divided square \(D_2(V)\) is *not* being identified integrally with the ordinary symmetric-power coinvariant lattice; for a basis \(e_1,\ldots,e_b\), its basis is \(e_i\otimes e_i\) and \(e_i\otimes e_j+e_j\otimes e_i\) for \(i<j\).

## Proof
**1. Relative model.** Write \(P=|G|\times|G|\), with transposition \(\tau(x,y)=(y,x)\), and write \(\Delta\) for the diagonal. Triangulate the product equivariantly so that \(\Delta\) is a subcomplex and every open cell away from \(\Delta\) has trivial stabilizer. The finite-relative-chain description of Borel–Moore homology of the open complement, with the sign local system, identifies its chain complex with
\[
C_*(P,\Delta;\mathbb Z)\otimes_{\mathbb Z[C_2]}\mathbb Z_{\mathrm{sgn}}.
\]
This follows cell by cell: the local coefficient of each off-diagonal orbit is represented by one lift, and changing that lift multiplies the coefficient by \(-1\). Boundaries into \(\Delta\) disappear. Equivariant homotopy equivalences of pairs induce chain-homotopy equivalences of these complexes.

**2. Reduction to a rose.** A connected graph of cycle rank \(b\) is homotopy equivalent to a one-vertex rose \(R_b\) with \(b\) oriented loop edges. For any graph homotopy equivalence \(f\) with inverse \(h\), the maps \(f\times f\) and \(h\times h\) form transposition-equivariant homotopy equivalences of pairs \((G\times G,\Delta G)\) and \((R_b\times R_b,\Delta R_b)\). Indeed, a homotopy \(H_t\) between one of the two composites and the identity gives \(H_t\times H_t\), which preserves the diagonal and commutes with transposition. Thus it suffices to compute the signed relative complex for \(R_b\).

**3. Integral cellular calculation.** In the quotient of the product of the rose by transposition, after deleting diagonal cells, the relative chain groups have \(b\) degree-one generators \(a_i\), one rectangular degree-two generator \(b_{ij}\) for each \(i<j\), one triangular half-square generator \(c_i\) for each \(i\), and no degree-zero generators. The rectangular boundary is zero because each loop is closed. The two non-diagonal edges of a triangular half-square contribute \(a_i\) and \(-a_i\) with exchange-sign coefficients, hence its boundary is also zero. Thus the entire signed cellular differential vanishes and
\[
H_1^{\mathrm{BM}}\cong\mathbb Z^b,\qquad H_2^{\mathrm{BM}}\cong\mathbb Z^{b(b+1)/2},\qquad H_i^{\mathrm{BM}}=0\quad(i\ne1,2).
\]
As a normalization check, using the trivial rather than sign character changes the triangular boundary to \(2a_i\), reproducing the known ordinary Borel–Moore groups: \(H_1\cong(\mathbb Z/2)^b\) and \(H_2\cong\mathbb Z^{\binom b2}\). This ordinary calculation is not claimed as new.

**4. Integral naturality and divided powers.** Transfer from the signed quotient cellular complex to the ordered relative cellular complex sends \(b_{ij}\) to the symmetrized tensor \(e_i\otimes e_j+e_j\otimes e_i\) and \(c_i\) to \(e_i\otimes e_i\). The relative long exact sequence of \((G\times G,\Delta G)\), together with the Künneth theorem and injectivity of the homology diagonal \(V\to V\oplus V\), gives \(H_2(G\times G,\Delta G)\cong V\otimes V\). Consequently, signed transfer in degree two is an isomorphism onto the flip-invariant integral tensor lattice \(D_2(V)\). The same relative sequence identifies \(H_1(G\times G,\Delta G)\) with the quotient of \(V\oplus V\) by the diagonal. On the rose generator \(a_i\), signed transfer has value \((e_i,-e_i)\), which becomes twice a generator of that quotient. Dividing the transfer by two therefore yields an integral isomorphism in degree one with \(V\). These transfer constructions commute with any graph automorphism and prove both natural identifications.

**5. Character.** Over \(\mathbb Q\), the trace on the invariant symmetric-tensor subspace of \(V\otimes V\) is half the sum of the trace of \(g\otimes g\) and the trace of \((g\otimes g)\) composed with flip. These are respectively \(a(g)^2\) and \(a(g^2)\). This proves the character formula and finishes the proof.

## Verification
The standalone standard-library script `verify.py` builds the signed and untwisted quotient relative cell-boundary matrices directly from vertices and edges. It checks that consecutive differentials compose to zero, and compares all rational and mod-two Betti numbers with the predicted formulas. In the executed check it passed 109 connected examples spanning cycle ranks zero through six, including paths, cycles, and complete graphs, with output `VERIFY_OK`. The general integral theorem is proved by the rose cellular description and transfer; finite rank checks are not a substitute for this argument. Reproduce with `python3 verify.py` using Python 3 and no third-party packages.

## Relationship to prior work
Khan's 2026 calculation gives the untwisted integral Borel–Moore groups for two unordered points on connected simple graphs (Theorem 3.4). The present statement instead computes the canonical *exchange-sign local system*, and identifies the resulting integral homology as graph-automorphism modules; the ordinary result alone does not specify either twisted groups or their representation structure. Blanchet, Palmer, and Shaukat develop twisted Borel–Moore homology for configuration spaces of surfaces with Heisenberg local systems, rather than this graph-specific sign-system calculation. Barnett–Farber's two-particle graph papers study ordinary homology of ordered configurations, not this Borel–Moore sign twist. The relationship is one of mathematical motivation and tools; priority beyond inspected sources is not claimed.

## Limitations
The proof depends on the finite-graph relative CW model and on the specific sign of the two-particle exchange. It makes no assertions about three or more particles, arbitrary local systems, or ordinary singular homology of the open configuration space. It does not identify the **integral** divided-square lattice with the ordinary symmetric-power coinvariant lattice; their natural integral structures differ in general. The identification is natural under homeomorphisms of graphs, not an assertion that arbitrary graph maps act on configurations (such maps may create collisions). Published or unindexed equivalent descriptions remain a residual literature risk. No independent audit has been performed.

## References
1. Munawar Khan, *Borel–Moore Homology of 2-Particle Unordered Configuration Spaces of Graphs via Discrete Morse Theory*, arXiv:2608.18143v1 (first public 2026-08-07), Theorem 3.4 and §§2–3. https://arxiv.org/html/2608.18143
2. Christian Blanchet, Martin Palmer, Awais Shaukat, *Heisenberg homology on surface configurations*, Mathematische Annalen 393 (2025), 1989–2056, DOI:10.1007/s00208-025-03242-2, especially §§1–3 and the Borel–Moore local-system setup. https://link.springer.com/article/10.1007/s00208-025-03242-2
3. Kathryn Barnett and Michael Farber, *Topology of configuration space of two particles on a graph, I*, Algebraic & Geometric Topology 9 (2009), 593–624, arXiv:0903.2180.
4. Michael Farber and Elizabeth Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300 (2010).
