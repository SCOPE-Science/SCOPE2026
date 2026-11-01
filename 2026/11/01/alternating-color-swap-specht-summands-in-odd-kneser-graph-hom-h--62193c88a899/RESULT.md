# Alternating color-swap Specht summands in odd Kneser graph Hom homology

## Finding
For each integer \(k\ge3\), let \(n=2k+1\) and let \(G_k=\operatorname{KG}(n,k)\) be the graph on the \(k\)-subsets of \([n]\), adjacent exactly when disjoint. Let \(X_k=\operatorname{Hom}(K_2,G_k)\) be the standard graph-homomorphism polyhedral complex. The symmetric group \(S_n\) permutes \([n]\), and \(\tau\) interchanges the two vertices of the source \(K_2\). These commuting actions make \(\widetilde H_1(X_k;\mathbb Q)\) a module for \(S_n\times\langle\tau\rangle\).

**Complete rational symmetry decomposition.** With \(S^\lambda\) denoting the ordinary rational Specht module of partition \(\lambda\vdash n\) and \(\varepsilon(\tau)=-1\), there is an isomorphism
\[
\boxed{H_1(X_k;\mathbb Q)\cong\bigoplus_{j=1}^{k}\left(S^{(2k-j,j,1)}\boxtimes\varepsilon^{j+1}\right).}
\]
In particular the irreducible \(S_n\)-constituents are multiplicity-free, with **alternating signs** under source-vertex interchange. For \(k=3\), the three constituent dimensions are \(15,35,21\), respectively, and the source interchange acts by \(+1,-1,+1\). The total rank is \(71\). No other positive homology degree occurs, and the integral first homology is torsion-free.

**Integral realization.** Let \(D_k\) be the bipartite graph with left and right vertices \((A,0),(A,1)\) for every \(k\)-subset \(A\subset[n]\), and directed edges \([A,B]\) from \((A,0)\) to \((B,1)\) for every ordered disjoint pair of \(k\)-subsets. Then there is a canonical integral \(S_n\times\langle\tau\rangle\)-homology identification
\[
H_1(X_k;\mathbb Z)\cong\ker\left(\partial:\mathbb Z[E(D_k)]\to\mathbb Z[V(D_k)]\right),\qquad
\partial[A,B]=[(B,1)]-[(A,0)],
\]
with \(\sigma[A,B]=[\sigma A,\sigma B]\) and \(\tau[A,B]=-[B,A]\). Its rank is \((k-1)\binom{2k+1}{k}+1\). This formula determines the integral lattice and all integer automorphism matrices through the explicit graph boundary, not merely the rational character.

**Closed mixed-character dichotomy.** For \(\sigma\in S_n\), let \(f_1\) count its fixed points, and let \(r\) count its nontrivial permutation cycles. Then
\[
\boxed{\operatorname{tr}(\sigma\tau\mid H_1(X_k;\mathbb Q))=
\begin{cases}
1-2^r,&f_1=1\text{ and every other cycle has even length},\\
1,&\text{otherwise}.
\end{cases}}
\]
The full character at \(\sigma\) without interchange is obtained by counting invariant graph vertices and directed edges, as detailed below. In particular the \(S_n\)-invariant first rational homology vanishes, and \(|X_k|/S_n\) is rationally acyclic. The case \(k=2\) is a known Petersen-graph symmetry specialization and is **not asserted to be new**; it serves only as a consistency check.

## Assumptions and scope
The graph \(\operatorname{KG}(n,k)\) is loopless; each vertex is a \(k\)-element subset of \([n]\). The complex \(\operatorname{Hom}(K_2,G_k)\) is the regular polyhedral complex whose cells are pairs \((U,V)\) of nonempty vertex subsets satisfying \(U\times V\subseteq E(G_k)\), ordered by inclusion in each coordinate. All graph edges are oriented from left to right in \(D_k\). Specht representations are over \(\mathbb Q\); the integral result gives a lattice, not an assertion of an integral direct-sum decomposition into Specht modules. The symmetry \(\tau\) acts on pairs by \((U,V)\mapsto(V,U)\).

## Proof
**Step 1: a natural graph model.** If distinct \(k\)-subsets \(A,A'\) have a common neighbor \(B\), then \(B\subseteq[n]\setminus(A\cup A')\). The complement has size at most \(k\); if it has size \(k\), \(B\) is uniquely determined. Thus any two distinct vertices of \(G_k\) share at most one neighbor. In particular \(G_k\) contains no four-cycle. Any cell \((U,V)\) of \(X_k\) has \(|U|=1\) or \(|V|=1\), since otherwise two vertices on each side would form a four-cycle. For every vertex \((A,0)\) of \(D_k\), take the closed simplex of cells \((\{A\},V)\), with \(\emptyset\ne V\subseteq N(A)\). Similarly take the simplex of cells \((U,\{B\})\) for every \((B,1)\). These simplices cover the entire Hom complex; two cover members meet exactly at the point \((\{A\},\{B\})\) when \(A\cap B=\emptyset\) and meet nowhere otherwise; intersections of three or more members are empty. The good-cover nerve is \(D_k\). This construction is preserved by both the \(S_n\)-action and source interchange. Its natural Mayer–Vietoris nerve chain equivalence consequently identifies all integral homology representations of \(X_k\) with those of \(D_k\). Equivalently, the same reduction is the square-free box-complex collapse established in prior literature; here only its naturality and the subsequent complete symmetry computation are used.

The two-step graph induced on the left vertices of \(D_k\) is the Johnson graph: two distinct \(k\)-subsets share a right neighbor precisely when their intersection has size \(k-1\). Elementary single-element replacements connect all \(k\)-subsets, so \(D_k\) is connected. It has \(2\binom{n}{k}\) vertices and \((k+1)\binom{n}{k}\) directed left-right edges. Therefore its integral cycle lattice is free of rank \((k-1)\binom{n}{k}+1\); all reduced homology in other degrees vanishes. The asserted integral boundary and actions follow from the orientation convention, including the minus sign under the involution \(\tau\).

**Step 2: representation-theoretic chain identity.** Let \(M_k\) be the \(S_n\)-permutation module on \(k\)-subsets, and let \(P_k\) be the module on ordered disjoint pairs of \(k\)-subsets. The \(S_n\)-module of degree-zero chains of \(D_k\) is \(M_k\oplus M_k\), with \(\tau\) swapping the factors. Its degree-one chains are \(P_k\), on which \(\tau\) is the negative of pair reversal \((A,B)\mapsto(B,A)\). Since \(D_k\) is connected, the exact sequence of \(S_n\times\langle\tau\rangle\)-modules is
\[
0\longrightarrow H_1(D_k;\mathbb Q)\longrightarrow\mathbb Q[E(D_k)]
\xrightarrow{\partial}\mathbb Q[V(D_k)]\longrightarrow\mathbf 1\longrightarrow0.
\]
Here \(\mathbf 1\) is a trivial character for both factors.

**Step 3: complement parity on balanced subsets.** Fix the omitted element \(c\in[n]\). An oriented edge \([A,B]\) with \([n]\setminus(A\cup B)=\{c\}\) is determined by one \(k\)-subset \(A\) of the remaining \(2k\) elements. The permutation representation \(W_k\) of \(S_{2k}\) on those \(k\)-subsets has a multiplicity-free decomposition
\[
W_k\cong\bigoplus_{j=0}^k S^{(2k-j,j)}.
\]
The involution \(C:A\mapsto[2k]\setminus A\) acts on \(S^{(2k-j,j)}\) by \((-1)^j\). Indeed, filter the space of functions on \(k\)-subsets by the spans \(F_j\) of \(f_T(A)=\mathbf 1_{T\subseteq A}\) with \(|T|\le j\). The standard two-row Young rule identifies \(F_j/F_{j-1}\) with \(S^{(2k-j,j)}\). Since
\[
Cf_T(A)=\prod_{a\in T}(1-\mathbf 1_{a\in A})
=\sum_{R\subseteq T}(-1)^{|R|}f_R(A),
\]
the action on the \(j\)-th quotient is \((-1)^j\). As \(W_k\) is semisimple over \(\mathbb Q\) and multiplicity-free, the claim holds on each irreducible summand.

The edge module \(P_k\) is \(\operatorname{Ind}_{S_{2k}\times S_1}^{S_n}W_k\), with the oriented source interchange acting by \(-C\). By the multiplicity-one branching/Pieri rule, \(\operatorname{Ind}S^{(2k-j,j)}\) consists of the Young diagrams obtained by adding one box. Its summands carry source sign \((-1)^{j+1}\). Every three-row shape \((2k-j,j,1)\), for \(1\le j\le k\), occurs exactly once, with this sign. Every nontrivial two-row shape \((n-t,t)\), for \(1\le t\le k\), occurs twice with opposite source signs, from \(j=t-1\) and \(j=t\). The trivial \(S_n\)-shape \((n)\) occurs only from \(j=0\), with negative source sign.

The vertex module is two copies of \(M_k\), which itself has precisely one copy of each \(S^{(n-t,t)}\), \(0\le t\le k\), in both source-sign eigenspaces. For \(t\ge1\), all two-row terms therefore cancel between oriented edge and vertex chains. For \(t=0\), the negative edge term cancels the negative vertex term; the remaining positive vertex term is cancelled by the terminal trivial \(H_0\) in the exact sequence. No three-row term cancels. This proves exactly the stated decomposition with the alternating source signs.

**Step 4: mixed-character formula.** For \(\sigma\in S_n\), the vertex-chain trace of \(\sigma\tau\) is zero because it exchanges left and right. In the oriented edge module, \(\sigma\tau\) has trace minus the number of ordered disjoint pairs \((A,B)\) satisfying \(\sigma A=B\) and \(\sigma B=A\). Such a pair has a unique omitted point \(c\), which must be fixed by \(\sigma\); the other \(2k\) labels must be divided into two sets swapped by \(\sigma\). This is possible exactly when there is one fixed point and all other cycles have even length, in which case every even cycle has two alternating assignments, yielding \(2^r\) choices. Applying the exact chain identity and the trivial trace of \(H_0\) gives \(1-2^r\) in that case and \(1\) otherwise. For an unswapped \(\sigma\), if \(v(\sigma)\) is the number of invariant \(k\)-sets and \(e(\sigma)\) the number of invariant ordered disjoint pairs, the full formula is \(\operatorname{tr}(\sigma\mid H_1)=e(\sigma)-2v(\sigma)+1\). Both counts are explicit via the cycle polynomial \(\prod_{\text{cycles of length }d}(1+t^d)\): \(v(\sigma)=[t^k]\prod(1+t^d)\), and \(e(\sigma)=f_1[t^k]\prod_{\text{cycles except one fixed singleton}}(1+t^d)\), interpreted as zero when there is no fixed point.

Finally, the Specht shapes \((2k-j,j,1)\) are neither the trivial nor the sign partition for \(k\ge3\). Hence the \(S_n\)-invariant rational first homology is zero. For a finite simplicial group action, rational homology of the geometric quotient is the invariant rational homology (via equivariant barycentric subdivision and transfer), proving rational acyclicity of the quotient.

## Verification
The standalone file `verify_odd_kneser_hom.py` constructs all vertices and directed edges of \(D_k\), verifies connectedness and integral cycle ranks, computes Specht dimensions by the hook-length formula, and independently compares the complete predicted \(S_n\times\langle\tau\rangle\) character with direct fixed-cell character counts for **every permutation cycle type** for \(k=2,3,4,5\). It computes Specht character values using the Frobenius alternant coefficient formula rather than reusing the Pieri decomposition argument. The numbers of checked types are respectively \(7,15,30,56\). The degree-one ranks are respectively \(11,71,379,1849\), all matching both methods. Run `python3 verify_odd_kneser_hom.py` with the standard Python library. These finite tests are not substitutes for the unrestricted proof in Steps 1–4.

## Relationship to prior work
Kamibeppu's square-free box-complex result (2008) already supplies a general deformation to the double-cover graph; Fujii–Kimura–Nozaki and Matsushita (initially public in December 2024) establish broad ordinary Hom-complex homotopy classifications for square-free codomains. The nonequivariant homotopy reduction, the cycle rank, the generic graph-cycle chain complex and the Petersen \(k=2\) symmetric-group decomposition are **not** presented as new. The contribution here is the **complete explicit multiplicity-free rational \(S_{2k+1}\times C_2\) irreducible classification for every \(k\ge3\)**, with a nontrivial alternating source-swap sign rule and its sharp mixed-character dichotomy. The known general square-free collapses do not themselves state or tabulate the three-row Specht constituents or their full color-swap parity. The result also identifies the integral lattice and shows how the extra action appears on it. Related results for stable Kneser graphs and ordinary Kneser independence/neighborhood complexes concern different spaces or symmetry groups. An implicit equivalent representation computation in the literature cannot be excluded.

## Limitations
The equivariant direct-sum decomposition holds over \(\mathbb Q\), not over \(\mathbb Z\); the integral lattice is given instead as a cycle kernel. The theorem concerns odd Kneser graphs with \(n=2k+1\) and \(k\ge3\), not arbitrary disjointness graphs. It does not claim a decomposition of higher graph-Hom complexes with other source graphs. The square-free collapse and the Petersen \(k=2\) case were previously established. Independent mathematical validation has not been performed, and unindexed or implicit coverage remains a residual originality risk.

## References
1. S. Fujii, K. Kimura, Y. Nozaki, *Homotopy types of Hom complexes of graph homomorphisms whose codomains are square-free*, arXiv:2412.19039 (initial public submission 2024-12-26), especially Theorem 1.1 and its discussion of \(\operatorname{Hom}(K_2,H)\).
2. T. Matsushita, *Hom complexes of graphs whose codomains are square-free*, arXiv:2412.19144 (initial public submission 2024-12-26), especially Theorem 1.2 and its scope.
3. A. Kamibeppu, *Homotopy type of the box complexes of graphs without 4-cycles*, Tsukuba Journal of Mathematics **32** (2008), 307–314. The related 2008 Kyoto proceedings version is publicly accessible at https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1578-13.pdf.
4. E. Babson, D. N. Kozlov, *Complexes of graph homomorphisms*, Israel Journal of Mathematics **152** (2006), 285–312.
5. C. Schultz, *The equivariant topology of stable Kneser graphs*, Journal of Combinatorial Theory A **118** (2011), 2291–2318 (distinct restricted graph family).
