# Maximal cliques of the rank-one nilpotent commuting graph over finite fields

## Finding
For every integer \(n\ge 2\) and every finite field \(\mathbb F_q\), let \(V=\mathbb F_q^n\). Form the simple graph \(\Gamma_{n,q}\) whose vertices are all nonzero rank-one endomorphisms \(X:V\to V\) with \(X^2=0\); two distinct vertices are adjacent precisely when they commute.

For each nonzero proper linear subspace \(W<V\), set
\[
\mathcal C_W=\{X\in V(\Gamma_{n,q}):\operatorname{im}X\subseteq W\subseteq\ker X\}.
\]
**The maximal cliques of \(\Gamma_{n,q}\) are precisely the distinct sets \(\mathcal C_W\)**. For \(k=\dim W\), they have cardinality
\[
|\mathcal C_W|=\frac{(q^k-1)(q^{n-k}-1)}{q-1}.
\]
Hence the number of maximal cliques is \(\sum_{k=1}^{n-1}{n\brack k}_q\), with precisely \({n\brack k}_q\) of the maximal cliques indexed by \(k\)-subspaces. Here \({n\brack k}_q=\prod_{i=0}^{k-1}(q^{n-i}-1)/(q^{k-i}-1)\).

For arbitrary nonzero proper subspaces \(W,U<V\), let \(a=\dim(W\cap U)\) and \(b=\dim(W+U)\). Their maximal cliques satisfy the **exact intersection law**
\[
|\mathcal C_W\cap\mathcal C_U|=\frac{(q^a-1)(q^{n-b}-1)}{q-1},
\]
where the value is zero when \(a=0\) or \(b=n\). In particular,
\[
\omega(\Gamma_{n,q})=\frac{(q^{\lfloor n/2\rfloor}-1)(q^{\lceil n/2\rceil}-1)}{q-1}.
\]
The number of maximum cliques is \({n\brack n/2}_q\) when \(n\) is even and \(2{n\brack (n-1)/2}_q\) when \(n\) is odd.

## Assumptions and scope
The field has arbitrary prime-power order, including even characteristic. The graph includes each actual nonzero matrix as a separate vertex: scalar multiples are **not** projectivized. It excludes zero and all higher-rank nilpotents. A clique is a nonempty set of pairwise adjacent vertices; maximal means inclusion-maximal, while maximum means largest cardinality. The assertions include \(n=2\) and \(q=2\): in that boundary case every maximal clique is a singleton.

## Proof
**Step 1: commuting is mutual annihilation.** Write \(X=u\otimes\alpha\) and \(Y=v\otimes\beta\) for nonzero vectors \(u,v\in V\) and nonzero covectors \(\alpha,\beta\in V^*\), with \(\alpha(u)=\beta(v)=0\). Then \(XY=\alpha(v)u\otimes\beta\), whereas \(YX=\beta(u)v\otimes\alpha\). If these products are equal and nonzero, their images force \(u,v\) to span the same line and their kernels force \(\alpha,\beta\) to span the same covector line. Therefore \(Y\) is a nonzero scalar multiple of \(X\); but then \(XY\) is a multiple of \(X^2=0\), a contradiction. Thus \(XY=YX\) implies \(XY=YX=0\). The converse is immediate.

**Step 2: every clique is contained in a canonical one.** Let \(S\) be a nonempty clique. Put \(P=\sum_{X\in S}\operatorname{im}X\) and \(K=\bigcap_{X\in S}\ker X\). By Step 1, each image is killed by every member, so \(P\subseteq K\). As every member has rank one, \(P\ne0\); as every member is nonzero, \(K\ne V\). Consequently \(S\subseteq\mathcal C_K\), and \(\mathcal C_K\) is a clique because every product of two of its members vanishes.

**Step 3: maximality and uniqueness.** Fix \(0<W<V\). Every nonzero \(w\in W\) and nonzero \(\phi\in(V/W)^*\) gives a rank-one member \(w\otimes\phi\) of \(\mathcal C_W\). Varying \(w,\phi\) proves
\[
\sum_{X\in\mathcal C_W}\operatorname{im}X=W,
\qquad
\bigcap_{X\in\mathcal C_W}\ker X=W.
\]
If any vertex \(Y\) commutes with every member of \(\mathcal C_W\), Step 1 forces \(\operatorname{im}Y\) into the common kernel \(W\), and forces \(Y\) to kill the span of the images \(W\). Therefore \(Y\in\mathcal C_W\). This proves inclusion-maximality. Conversely a maximal clique must equal the canonical clique containing it from Step 2. The displayed image/kernel identities show that \(\mathcal C_W=\mathcal C_U\) entails \(W=U\).

**Step 4: cardinalities and intersections.** A member of \(\mathcal C_W\) is a nonzero decomposable tensor in \(W\otimes(V/W)^*\), uniquely represented by \((w,\phi)\) up to the simultaneous rescaling \((w,\phi)\mapsto(\lambda w,\lambda^{-1}\phi)\). Counting gives \((q^k-1)(q^{n-k}-1)/(q-1)\). Likewise \(\mathcal C_W\cap\mathcal C_U\) consists of nonzero decomposable tensors in \((W\cap U)\otimes(V/(W+U))^*\). This yields the intersection formula, even when one factor space is zero. Subspace counting gives the Gaussian coefficients.

**Step 5: extremal cliques.** For integer \(1\le k\le n-1\), the numerator of the size is \(q^n+1-q^k-q^{n-k}\). The sum \(q^k+q^{n-k}\) is minimized when \(k\) is as close as possible to \(n/2\). Exactly the indicated dimensions maximize the size, proving the clique number and count.

## Verification
The independent finite checker `verify_rankone_graph.py` constructs the vertices as actual matrices, tests adjacency by ordinary matrix multiplication, enumerates maximal cliques with a Bron--Kerbosch routine, reconstructs their image spaces, and checks the complete claimed clique, count, maximum, degree and pairwise intersection formulas. It does not merely evaluate the closed formulas. It covers eight configurations: \((n,q)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2)\). The \(q=4\) implementation explicitly uses \(\mathbb F_2[z]/(z^2+z+1)\). Final output: `RANK_ONE_NILPOTENT_CLIQUE_GEOMETRY_OK 8`.

A separate known rank-one commutator count implies the graph's vertex number \((q^n-1)(q^{n-1}-1)/(q-1)\) and uniform degree; those are verification cross-checks, **not** asserted as new results. The proof above, rather than finite enumeration, establishes the statements for all prime powers and dimensions.

## Relationship to prior work
Commuting graphs of full matrix algebras and nilpotent matrix subsets have long been studied: Akbari and Raja (2006) show connectivity for the nilpotent subset in higher dimensions. Britnell and Wildon (arXiv:1001.0811, initially public January 6, 2010) classify possible commuting similarity-class types and nilpotent partitions, not the entire maximal-clique geometry of this rank-one induced graph. Ou and Zhong (2016) determine graph automorphisms for **rank-one upper-triangular** matrices; their restricted vertex set is not invariant under arbitrary conjugation and is distinct from the full rank-one square-zero locus here. A previously recorded enumeration of rank-one nilpotent commutator ranks (opaque identifier `c64b3bef-2714-42c6-aeaa-b9883604b3df`) already gives commuting-pair counts and degrees, but does not determine maximal cliques or their intersection configurations. The new claim is restricted to these latter structural assertions.

## Limitations
This is a self-review, not independent validation or certified publication priority. The result does not characterize automorphisms, connectivity, graph spectra or cliques of the full nilpotent commuting graph, nor does it extend to rank-two nilpotents. Prior specialized clique results outside the checked literature could subsume it; the full 2006 Akbari--Raja article was not read, although its accessible abstract treats connectivity rather than clique classification. Finite tests cannot verify the universal quantifiers; the complete proof does that.

## References
1. S. Akbari and P. Raja, *Commuting graphs of some subsets in simple rings*, Linear Algebra and its Applications 416 (2006), 1038–1047. DOI: 10.1016/j.laa.2006.01.006.
2. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811 (initial posting 2010-01-06), Journal of the London Mathematical Society 83 (2011), 470–492.
3. S. Ou and J. Zhong, *Automorphisms of a commuting graph of rank one upper triangular matrices*, Electronic Journal of Linear Algebra 31 (2016), 774–793. DOI: 10.13001/1081-3810.3064.
