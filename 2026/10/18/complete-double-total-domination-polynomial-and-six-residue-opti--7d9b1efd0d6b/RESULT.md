# Complete double total domination polynomial and six-residue optimizer census of circular ladders

## Finding

Let \(P_n=C_n\square K_2\) be the circular ladder, for every integer \(n\ge3\). Let \(T_n(z)\) count double total dominating vertex subsets by their cardinality: 
\[
T_n(z)=\sum_{D\subseteq V(P_n):\ |N(v)\cap D|\ge2\ \forall v\in V(P_n)}z^{|D|}.
\]
For each integer \(L\ge3\) define
\[
F_L(x)=1+\sum_{k=1}^{\lfloor L/3\rfloor}\frac{L}{k}\binom{L-2k-1}{k-1}x^k.
\]
Then the *complete* double total domination polynomial is
\[
\boxed{T_n(z)=\begin{cases}
z^{2n}F_{2n}(z^{-1}),&n\text{ odd},\\
z^{2n}F_n(z^{-1})^2,&n\text{ even}.
\end{cases}}
\]
The expressions denote ordinary polynomials with nonnegative integer coefficients; the apparent negative powers cancel. These formulas count each subset exactly once, for every cardinality. Their associated exact minimum is
\[
\gamma_{\times2,t}(P_n)=\begin{cases}
2n-\lfloor2n/3\rfloor,&n\text{ odd},\\
2n-2\lfloor n/3\rfloor,&n\text{ even}.
\end{cases}
\]
The minimum numerical parameter was studied previously; the all-subset polynomial, its cycle-square classification, and its exact optimizer multiplicity are the present findings. In particular the number \(M_n\) of subsets attaining that minimum is
\[
\boxed{M_n=\begin{cases}
9,&n\equiv0\pmod6,\\
n(\lfloor2n/3\rfloor+1),&n\equiv1\pmod6,\\
\left(n(n+1)/6\right)^2,&n\equiv2\pmod6,\\
3,&n\equiv3\pmod6,\\
n^2,&n\equiv4\pmod6,\\
2n,&n\equiv5\pmod6.
\end{cases}}
\]
For example, \(M_7=35\), \(M_8=144\), \(M_9=3\), and \(M_{10}=100\). Every optimum is described constructively in the proof.

## Assumptions and scope

All graphs are finite, simple, undirected. The cycle \(C_n\) is indexed by \(\mathbb Z/n\mathbb Z\) and has \(n\ge3\) vertices. The vertex set of the Cartesian product \(P_n\) is \(\mathbb Z/n\mathbb Z\times\{0,1\}\), with edges between \((i,a)\) and \((i\pm1,a)\), and between \((i,0)\) and \((i,1)\). Every vertex has degree three. An open packing is a vertex set containing no distinct vertices that share a common neighbor. A double total dominating set \(D\) satisfies \(|N(v)\cap D|\ge2\) for **every** vertex \(v\), including vertices already in \(D\). The notation \(C_L^2\) denotes the square of a cycle: distinct vertices are joined if their distance along \(C_L\) is one or two. The polynomial \(F_L\) is the independent-set polynomial of \(C_L^2\).

## Proof

**1. Complement equivalence.** Because the prism is cubic, \(|N(v)\cap D|\ge2\) holds for every \(v\) if and only if \(|N(v)\cap(V(P_n)\setminus D)|\le1\) holds for every \(v\). The latter says exactly that the complement \(S=V(P_n)\setminus D\) is an open packing. Thus complementation is a bijection, reversing cardinalities.

**2. The common-neighbor conflict graph.** Build a graph \(H_n\) on the vertex set of \(P_n\); distinct vertices are adjacent in \(H_n\) exactly when they have a common neighbor in \(P_n\). From
\[
N_{P_n}(i,a)=\{(i-1,a),(i+1,a),(i,1-a)\},
\]
its edges are exactly the pairs of forms \((i,a)(i\pm2,a)\) and \((i,a)(i\pm1,1-a)\), with indices modulo \(n\), suppressing repeated edges. Indeed, these arise from choosing two different neighbors of a given center; conversely all such pairs visibly have that center as common neighbor. This statement is valid even for the small cycles \(n=3,4\).

Define a two-regular auxiliary graph \(Q_n\) whose edges are \((i,a)(i+1,1-a)\) for every \(i\) and \(a\). A single step toggles the layer and advances the index by one; its connected components are cycles. Traversing \(n\) advancing steps returns to the original layer precisely when \(n\) is even. It follows that
\[
Q_n\cong\begin{cases}C_{2n},&n\text{ odd},\\C_n\sqcup C_n,&n\text{ even}.\end{cases}
\]
The pairs at graph distance one or two in \(Q_n\) are exactly the two edge types listed for \(H_n\). Hence **as graphs on the same explicitly labeled vertices**, \(H_n=Q_n^2\), and therefore
\[
H_n\cong\begin{cases}C_{2n}^2,&n\text{ odd},\\C_n^2\sqcup C_n^2,&n\text{ even}.\end{cases}
\]
An open packing in \(P_n\) is precisely an independent set in \(H_n\). This is a bijection of entire set families, not just a comparison of maximum cardinalities.

**3. Exact cycle-square enumerator.** Fix \(L\ge3\) and \(1\le k\le\lfloor L/3\rfloor\). An independent \(k\)-set in \(C_L^2\) has all \(k\) forward cyclic gaps between consecutive chosen vertices of length at least three, and every such gap pattern gives an independent set. After distinguishing one chosen vertex, ordered gaps \((g_1,\ldots,g_k)\) satisfy \(g_j\ge3\) and \(\sum_jg_j=L\). There are \(\binom{L-2k-1}{k-1}\) such compositions. Each chosen distinguished origin can be any of the \(L\) named positions, but each undistinguished set is counted \(k\) times. Thus the number of independent \(k\)-sets is \(\frac{L}{k}\binom{L-2k-1}{k-1}\). The empty independent set contributes one; no set can exceed \(\lfloor L/3\rfloor\). This proves the formula for \(F_L\).

**4. Distribution and optimizer classification.** For odd \(n\), a complement open packing is exactly an independent set in \(C_{2n}^2\), so its cardinality enumerator is \(F_{2n}\). For even \(n\), it is an independent set independently in each copy of \(C_n^2\), so the enumerator is \(F_n^2\). Reversing cardinalities yields the stated formula for \(T_n\). Maximum independent sets in \(C_L^2\) are exactly the cyclic \(\lfloor L/3\rfloor\)-sets with cyclic gaps at least three, as proved in step 3. Therefore all minimum double total dominating sets are exactly their complements, with one squared cycle if \(n\) is odd and independent choices in two squared cycles if \(n\) is even. This explicitly classifies every optimum.

The coefficient of top degree in \(F_L\), with \(L=3q+r\) and \(r\in\{0,1,2\}\), is \(3\) if \(r=0\), \(L\) if \(r=1\), and \(L(q+1)/2\) if \(r=2\). This follows directly by substituting \(k=q\) in the binomial formula. The stated minimum cardinalities are the complement sizes. For odd \(n\) apply the top coefficient with \(L=2n\); for even \(n\) square the top coefficient with \(L=n\). Splitting by the six residues of \(n\) proves all six cases of \(M_n\).

## Verification

The standalone standard-library program `verification/verify.py` performs four logically distinct finite corroborations: it directly enumerates all \(349{,}440\) subsets of the underlying prism vertex sets for \(3\le n\le9\) and checks the double-total rule at each vertex; it independently enumerates all open packings through a conflict-graph backtracking search for \(3\le n\le13\); it verifies literal conflict-edge equality with the auxiliary-cycle square and the component lengths for \(3\le n\le100\); and it compares maximum sizes and six-residue counts for \(3\le n\le400\). The provided text `verification/output.txt` is the actual standard output. Invoke `python3 verification/verify.py` from the package root. The finite checks support, but do not substitute for, the proof for every integer \(n\ge3\).

## Relationship to prior work

Henning and Maritz (2006, Section 5.4), as also recorded by Ediz (2009), already study the double total domination **number** of prism graphs; the minimum value alone is not presented as new. Bermudo, Sánchez, and Sigarreta (2017, Section 4) obtain total \(k\)-domination results and bounds for Cartesian cylinders, but not a distribution of all double-total sets. Brešar, Klavžar, and Rall (arXiv first public 10 September 2023, Theorem 2.2) prove an extremal open-packing theorem for prisms over bipartite base graphs, which includes even cycles; their theorem provides a maximum cardinality, not an entire cardinality enumerator, and its bipartiteness hypothesis does not include odd cycles. Li, Yue, and Zhang (2023) study the double total domination number on Cartesian products of **paths**, another distinct graph family. The present all-set bijection with an auxiliary squared cycle, its odd/even splitting, and the full polynomial and optimizer counts do not follow from the listed numerical theorems alone. Counting independent sets of squared cycles by circular gap compositions is elementary and is not claimed as an independent invention. The comparison is a best-knowledge literature assessment, not a proof that no earlier equivalent formula exists.

## Limitations

The theorem assumes a cubic circular ladder with \(n\ge3\); it does not address the non-simple convention \(C_2\), arbitrary ladder widths, or general degree classes. Previously established numerical minimum results are acknowledged. The independently checked computations are finite. Equivalent count formulas in obscure or unindexed sources remain possible; no independent scientific audit has been performed.

## References

1. M. A. Henning and J. E. Maritz, *Stratification and Domination in Prisms*, Ars Combinatoria **81** (2006), 343–358. Published paper: https://combinatorialpress.com/ars-articles/volume-081-ars-articles/stratification-and-domination-in-prisms/ ; Section 5.4.
2. S. Ediz, *On Stratified Domination in Prisms*, International Mathematical Forum **4** (2009), 2355–2362. https://www.m-hikari.com/imf-password2009/45-48-2009/edizIMF45-48-2009.pdf .
3. S. Bermudo, J. L. Sánchez, and J. M. Sigarreta, *Total k-domination in Cartesian product graphs*, Periodica Mathematica Hungarica **75** (2017), 255–267. DOI: 10.1007/s10998-017-0191-2; Section 4.
4. A. Cabrera Martínez and F. A. Hernández-Mira, *New Bounds on the Double Total Domination Number of Graphs*, Bulletin of the Malaysian Mathematical Sciences Society **45** (2022), 443–453. DOI: 10.1007/s40840-021-01200-0.
5. L. Li, J. Yue, and X. Zhang, *Double total domination number of Cartesian product of paths*, AIMS Mathematics **8** (2023), 9506–9519. DOI: 10.3934/math.2023479.
6. B. Brešar, S. Klavžar, and D. F. Rall, *Packings in bipartite prisms and hypercubes*, arXiv:2309.04963, first public 10 September 2023, and Discrete Mathematics (2024). https://arxiv.org/abs/2309.04963 ; Theorem 2.2.
