# Reflection characters of linear hexagonal-chain independence complexes

## Finding
For every integer \(n\ge 1\), let \(G_n\) be the linear chain of \(n\) hexagons defined below. The horizontal row exchange \(h\) and longitudinal end reversal \(v\) generate a Klein four-group acting simplicially on \(\operatorname{Ind}(G_n)\). The top reduced rational homology
\[
V_n=\widetilde H_n(\operatorname{Ind}(G_n);\mathbb Q)
\]
has dimension two. Its exact character, ordered at \((1,h,v,hv)\), is
\[
\bigl(\chi_n(1),\chi_n(h),\chi_n(v),\chi_n(hv)\bigr)=
\begin{cases}
(2,0,2(-1)^k,0), & n=2k,\ k\ge1,\\
(2,0,0,2(-1)^{k+1}), & n=2k+1,\ k\ge0.
\end{cases}
\]
In particular, write \(\varepsilon_{a,b}\) for the one-dimensional rational character with \(h\) acting by \(a\in\{+1,-1\}\) and \(v\) by \(b\in\{+1,-1\}\). Then the complete rational representation is
\[
V_{2k}\cong\varepsilon_{+1,(-1)^k}\oplus\varepsilon_{-1,(-1)^k}\quad(k\ge1),
\]
\[
V_{2k+1}\cong\varepsilon_{+1,(-1)^{k+1}}\oplus\varepsilon_{-1,-(-1)^{k+1}}\quad(k\ge0).
\]
These are rational homology representations, not claims of equivariant homotopy equivalences or integral module splittings.

## Assumptions and scope
For \(n\ge1\), define the undirected finite simple graph \(G_n\) by the vertex set
\[
\{(r,j):r\in\{0,1\},\ 1\le j\le2n+1\}
\]
and the edges \(\{(r,j),(r,j+1)\}\) for \(r\in\{0,1\}\), \(1\le j\le2n\), together with the rungs \(\{(0,j),(1,j)\}\) for every odd \(j\) in \([1,2n+1]\). Thus \(G_1=C_6\); successive hexagons share an edge. This is the graph denoted \(H_{1\times1\times n}\) in Chandrakar--Singh (2025), not a square ladder or a periodic hexagonal grid.

The simplicial independence complex \(\operatorname{Ind}(G)\) contains exactly the vertex subsets spanning no graph edge. Define automorphisms
\[
h(r,j)=(1-r,j),\qquad v(r,j)=(r,2n+2-j).
\]
Both have order two, commute, and generate \(\langle h,v\rangle\cong C_2\times C_2\). Homology has coefficients in \(\mathbb Q\) unless specified. The externally established non-equivariant input is the theorem \(\operatorname{Ind}(G_n)\simeq S^n\vee S^n\) for all \(n\ge1\) [1, Theorem 3.1]; the new assertion is the explicit action of both reflections and their product on its top homology.

## Proof
**1. Alternating orbit-graph formula.** Let \(G\) be any finite simple graph and \(g\) a graph automorphism of order at most two. Remove every \(g\)-orbit of vertices containing an edge of \(G\). Form the graph \(Q_g\) whose remaining vertices are these orbits and whose distinct orbits are joined whenever a graph edge connects their members. A \(g\)-invariant independent set of \(G\) is uniquely a union of independent orbits of \(Q_g\). Let
\[
I(Q;t)=\sum_{S\in\operatorname{Ind}(Q)}t^{|S|}
\]
include the empty independent set. On an oriented simplex fixed setwise by \(g\), every chosen two-element vertex orbit contributes one sign reversal; hence its augmented alternating chain trace is \(-(-1)^{\#\text{chosen orbits}}\). The augmented (reduced) Lefschetz trace is therefore
\[
\widetilde L(g;\operatorname{Ind}(G))=-I(Q_g;-1).
\]
By the ordinary simplicial Hopf trace identity and the non-equivariant homotopy theorem [1], the only nonzero reduced rational homology of \(\operatorname{Ind}(G_n)\) is \(V_n\). Thus
\[
\chi_n(g)=(-1)^{n+1}I(Q_g;-1).
\tag{1}
\]
This sign includes the contribution of the empty simplex in the augmented chain complex.

**2. A cancellation observation.** Suppose a graph \(T\) has two distinct leaves \(p,q\) with respective distinct supports \(x,y\), and \(x\) is adjacent to \(y\). Then \(I(T;-1)=0\). Indeed, for any fixed choices away from these four vertices, contributions cancel by toggling \(p\) whenever \(x\) is absent, and by toggling \(q\) whenever \(y\) is absent. Any uncancelled choice would contain both adjacent vertices \(x,y\), which is impossible.

**3. Row exchange.** For \(g=h\), every odd-column row-pair orbit contains a rung and is inadmissible. The remaining \(n\) even-column orbits are mutually nonadjacent, so \(Q_h\) is an edgeless graph on \(n\) vertices. Hence \(I(Q_h;-1)=(1-1)^n=0\), proving \(\chi_n(h)=0\).

**4. End reversal.** If \(n=2k\) is even, folding the columns about the midpoint \(j=n+1\) identifies \(Q_v\) with the original hexagonal chain \(G_k\): its two rails have \(2k+1\) columns and rungs at all odd columns. By [1, Theorem 3.1],
\[
I(G_k;-1)=-\widetilde\chi(\operatorname{Ind}(G_k))=2(-1)^{k+1}.
\tag{2}
\]
Equation (1) gives \(\chi_{2k}(v)=2(-1)^k\). If \(n\) is odd, the two midpoint vertices are fixed, have no rung, and become distinct terminal leaves in \(Q_v\), supported by the adjacent ends of the last rung at column \(n\). Step 2 gives \(I(Q_v;-1)=0\), hence \(\chi_n(v)=0\).

**5. Combined reflection.** When \(n\) is even, the two midpoint vertices form an inadmissible orbit under \(hv\) because their column carries a rung. The remaining orbit graph has two rails of length \(n\), rungs at odd columns, and two leaves at the terminal even column, supported by adjacent vertices on the preceding odd rung. Step 2 gives \(\chi_n(hv)=0\).

When \(n=2k+1\) is odd, the middle column has no rung. The \(hv\)-orbit graph consists of \(G_k\) (for \(k\ge1\)) with an additional vertex \(w\) adjacent to the two ends \(x,y\) of its last rung. Inclusion--exclusion on \(w\) gives
\[
I(Q_{hv};-1)=I(G_k;-1)-I(G_k\setminus\{x,y\};-1).
\]
The graph in the second term has two terminal leaves supported by the previous rung's adjacent ends, so its value at \(-1\) is zero by Step 2. Equation (2) now implies \(I(Q_{hv};-1)=2(-1)^{k+1}\). For \(k=0\), the quotient graph is a triangle, whose independence polynomial at \(-1\) is \(-2\), the same formula. Equation (1) yields \(\chi_{2k+1}(hv)=2(-1)^{k+1}\).

**6. Representation.** The four preceding traces determine the character. Since \(C_2\times C_2\) is a finite abelian group of exponent two, every irreducible rational representation is a one-dimensional sign character. Decomposing using the displayed traces gives exactly the two stated direct sums. This completes the proof for every \(n\ge1\).

## Verification
The standalone standard-library program `verify_hex_symmetry.py` independently constructs the graph, automorphism orbits, and quotient-conflict graph. An exact recursive evaluation of \(I(Q_g;-1)\) checks 56 cases: each of four group elements for every \(1\le n\le14\). Separately, for \(1\le n\le4\), it enumerates invariant independent faces in the **original** graph, computes the orientation sign of every fixed simplex directly, and checks 16 resulting reduced Lefschetz traces without using the quotient formula. Running `python3 verify_hex_symmetry.py` returned:

`VERIFY_OK 56 orbit-graph evaluations (n=1..14) and 16 direct signed fixed-face enumerations (n=1..4)`

These exhaustive finite checks are cross-checks, not the proof of the all-parameter theorem. The proof is Steps 1--6 and uses the independently published non-equivariant input [1].

## Relationship to prior work
Chandrakar--Singh [1], first posted 2025-12-24, prove that \(\operatorname{Ind}(G_n)\simeq S^n\vee S^n\). Their theorem supplies the two-dimensional homology group but not its reflection character. Distinct two-dimensional \(C_2\times C_2\)-representations share that underlying vector-space dimension, so the claimed actions do not follow from the wedge formula without further computations. Our orbit-graph argument supplies those computations, including a parity-dependent switch in which reflection acts by a common scalar.

Jonsson [2] studies cross-cycles for *periodic quotients* of square, triangular and hexagonal lattices; its specified objects and cross-cycle degree classification are different from the finite planar hexagonal chains and their reflection characters here. Work on automorphism representations of *matroid* independence complexes [3] likewise has a different combinatorial object. The signed simplicial Hopf trace formula and evaluation of independence polynomials at \(-1\) are standard inputs, not new general methods claimed here. Literature and mathematical-record searches did not identify an earlier equivalent all-parameter character statement; this is a qualified originality assessment, not a proof of absolute novelty.

## Limitations
The theorem determines only the rational top reduced homology representation for these linear chains. It does not determine the integral representation lattice, give an equivariant homotopy decomposition, classify wider hexagonal grids, or treat arbitrary graph automorphisms beyond the displayed Klein four-group. Its use of the homotopy type in [1] is essential. Unindexed or unpublished equivalent work remains possible, and [2] was compared from its accessible abstract, not from a complete full-text inspection.

## References
[1] Himanshu Chandrakar and Anurag Singh, *Independence Complexes of Hexagonal Grid Graphs*, arXiv:2512.21318v1 (public 2025-12-24), Theorem 3.1 and Section 3. https://arxiv.org/pdf/2512.21318

[2] Jakob Jonsson, *Certain Homology Cycles of the Independence Complex of Grids*, Discrete & Computational Geometry **43** (2010), 927--950, DOI:10.1007/s00454-009-9224-9.

[3] Luca Moci and Gian Marco Pezzoli, *Representations of automorphism groups on the homology of matroids*, European Journal of Combinatorics **94** (2021), 103312, arXiv:2001.03760.
