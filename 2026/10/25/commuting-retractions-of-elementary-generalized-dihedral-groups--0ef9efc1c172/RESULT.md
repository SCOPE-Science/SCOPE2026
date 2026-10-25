# Commuting retractions of elementary generalized dihedral groups

## Finding

Let \(p\) be an odd prime, \(d\ge2\), \(V=\mathbb F_p^d\), and \(G=V\rtimes\langle s\rangle\), where \(s^2=1\) and \(svs=-v\). Let \(\mathcal E(G)\) be the set of idempotent group endomorphisms, and let \(\Gamma(G)\) be its full commuting graph: distinct endomorphisms are adjacent precisely when they commute under composition. Write \({d\brack r}_p\) for the Gaussian binomial coefficient and put
\[
 P_m(p)=\sum_{j=0}^m {m\brack j}_p p^{j(m-j)},\qquad
 Q_r(p)=\sum_{i=0}^r {r\brack i}_p p^{i(r-i)+r-i}.
\]

**Theorem.** Besides the trivial group endomorphism \(\mathbf0\), every idempotent endomorphism is uniquely \(F_{A,u}\), given by
\[
 F_{A,u}(v)=Av,\qquad F_{A,u}(s)=us,
 \qquad A^2=A,\quad Au=0,
\]
where \(A\in\operatorname{End}_{\mathbb F_p}(V)\) and \(u\in V\). Composition is
\[
 F_{A,u}\circ F_{B,v}=F_{AB,u+Av}.
\]
The number of these endomorphisms with \(\operatorname{rank}A=r\) is
\[
 N_r={d\brack r}_p p^{(r+1)(d-r)}\qquad(0\le r\le d),
\]
and thus \(|\mathcal E(G)|=1+\sum_{r=0}^d N_r\). For each rank-\(r\) vertex, its graph degree is
\[
 \deg_\Gamma F_{A,u}=P_{d-r}(p)Q_r(p),
\]
while the trivial endomorphism has degree \(\sum_{r=0}^d N_r\). Hence these formulas give the complete degree multiset, summing coincident ranks' multiplicities if necessary.

Every maximal clique consists of \(\mathbf0\) and precisely \(2^d\) commuting affine projections. More explicitly, choose a point \(x\in V\) and an unordered direct-sum decomposition \(V=L_1\oplus\cdots\oplus L_d\) into one-dimensional subspaces. Let \(A_J\) be the projection onto \(\bigoplus_{j\in J}L_j\) along the remaining lines. Then the corresponding clique is
\[
 \mathcal K(x,\{L_j\})=\{\mathbf0\}\cup
 \{F_{A_J,(I-A_J)x}:J\subseteq\{1,\ldots,d\}\}.
\]
These are **all** maximal cliques, with no duplication of \((x,\{L_j\})\). Consequently,
\[
 \omega(\Gamma(G))=2^d+1,\qquad
 \#\{\text{maximal cliques}\}=
 \frac{p^d|\operatorname{GL}_d(\mathbb F_p)|}{d!(p-1)^d}.
\]
The affine automorphism group \(\operatorname{Aut}(G)\cong V\rtimes\operatorname{GL}_d(\mathbb F_p)\) acts transitively on maximal cliques. Its action on the nontrivial idempotent endomorphisms has exactly \(d+1\) rank orbits; the trivial endomorphism is one additional orbit.

## Assumptions and scope

All groups, linear maps, and affine maps are finite. The symbol \(\mathbf0\) means the endomorphism sending every group element to the identity; it is **not** one of the maps \(F_{0,u}\), which instead map \(s\) to the involution \(us\). The parameter \(p\) is an odd prime (not an arbitrary prime power); rank is \(\mathbb F_p\)-rank. The graph includes all idempotent group endomorphisms, including the trivial endomorphism and identity. The result is about **commutation of group endomorphisms under composition**, not the usual element-commuting graph of \(G\). Every stated formula holds for all odd \(p\) and \(d\ge2\), with the dimension-one specialization independently covered in the cited prior literature.

## Proof

**Classification of homomorphisms.** The normal subgroup \(V\) is the unique Sylow \(p\)-subgroup of \(G\). Every homomorphism \(f:G\to G\) therefore restricts on \(V\) to an additive, hence \(\mathbb F_p\)-linear, map \(A\). The image \(f(s)\) has order dividing two: it is either the identity or an involution \(us\). If \(f(s)=1\), applying \(f\) to \(svs=-v\) shows \(Av=-Av\), whence \(A=0\) because \(p\) is odd. This is \(\mathbf0\). Otherwise \(f=F_{A,u}\), and the dihedral presentation shows any choice \((A,u)\) determines a homomorphism. Composition gives the displayed rule. Squaring shows \(F_{A,u}^2=F_{A^2,u+Au}\), so idempotence is equivalent to \(A^2=A\) and \(Au=0\).

**Rank census.** A rank-\(r\) linear projection is uniquely determined by its image \(U\) and its complementary kernel \(W\). There are \({d\brack r}_p\) choices of \(U\), and the complements number \(p^{r(d-r)}\), since they are graphs of linear maps from any fixed complement into \(U\). Then \(u\in W\) has \(p^{d-r}\) choices. Multiplication gives \(N_r\).

**Individual commutants.** Each affine projection \(x\mapsto Ax+u\) fixes an affine subspace: solve \((I-A)x=u\), which is possible because \(u\in\ker A\). Conjugation by an affine translation makes \(u=0\), without changing centralizer size. Set \(V=U\oplus W\), \(U=\operatorname{im}A\), \(W=\ker A\). A second affine projection \((B,v)\) commutes with \((A,0)\) if and only if \(AB=BA\), \(Av=v\), and \(Bv=0\). The first condition makes \(B\) block diagonal with projections \(B_U\) and \(B_W\), while the last two require \(v\in\ker B_U\subseteq U\). For \(\operatorname{rank}B_U=i\) there are \({r\brack i}_pp^{i(r-i)}\) choices and \(p^{r-i}\) vectors \(v\); independently \(B_W\) has \(P_{d-r}(p)\) possibilities. Thus there are \(P_{d-r}(p)Q_r(p)\) commuting nontrivial idempotents, including the vertex itself. Adding \(\mathbf0\), then subtracting the vertex itself, gives degree \(P_{d-r}(p)Q_r(p)\). The trivial endomorphism is universally adjacent because composition with it is zero on both sides.

**Maximal cliques.** Through \(F_{A,u}\leftrightarrow(x\mapsto Ax+u)\), the nontrivial idempotent endomorphisms form exactly the idempotent affine self-maps of \(V\), with composition preserved. Let \(\mathcal F\) be any pairwise commuting family. It is finite and nonempty. Its product \(E\) is again an affine idempotent, and \(\operatorname{im}E=\bigcap_{f\in\mathcal F}\operatorname{im}f\): containment follows from commuting and \(fE=E\), while each point fixed by all \(f\) is fixed by \(E\). In particular, choose a common fixed point \(x\). Translating \(x\) to the origin makes the family a commuting family of linear idempotents. These simultaneously diagonalize: split into the image and kernel of one projection, note the others preserve both subspaces, and iterate inductively. Completing a common eigenbasis yields a direct sum of \(d\) lines, and the family lies in the Boolean family of all \(2^d\) coordinate projections. Conversely, that family is pairwise commuting and maximal: any affine projection commuting with its constant map \(y\mapsto x\) fixes \(x\), while commuting with each coordinate rank-one projection forces it to be diagonal in those lines. Therefore adding \(\mathbf0\) gives precisely the maximal cliques.

For uniqueness, within a Boolean clique the unique rank-zero nontrivial member is the constant map with value \(x\), so the common point is determined by the clique. Its rank-one members then recover the unordered lines \(L_j\). The number of unordered decompositions is \(|\operatorname{GL}_d(\mathbb F_p)|/(d!(p-1)^d)\), because ordered bases are identified exactly under separate nonzero rescalings and line permutations. Multiplying by the \(p^d\) possible points proves the clique count. Finally, automorphisms of \(G\) are precisely \(F_{M,b}\) with \(M\) invertible, so the associated affine group acts transitively on all pairs \((x,\{L_j\})\). Conjugation sends any rank-\(r\) affine projection to a linear coordinate rank-\(r\) projection, proving the orbit statement.

## Verification

The standalone file `verify_dihedral.py` uses only the Python standard library and may be run as `python verify_dihedral.py`. It explicitly enumerates all idempotent matrices and permitted translations. For \((p,d)=(3,1),(3,2),(5,2)\), it computes the entire commuting graph and all maximal cliques by an adjacency-based algorithm. For \((p,d)=(3,3)\), it checks all pairwise commutation decisions and all individual centralizer counts, without enumerating its maximal cliques. For \((p,d)=(3,2)\), it additionally checks the group law, homomorphism condition, idempotence and composition directly on group elements. Its recorded terminal result is `VERIFY_OK`; the general theorem is established by the proof, not by finite testing.

## Relationship to prior work

Arvasi, Odabaş and Wensley develop computations with idempotent group endomorphisms and pairs satisfying commuting conditions in their work on crossed squares and cat²-groups. Their Section 4.4 (accepted author manuscript) explicitly gives the idempotent endomorphisms of the ordinary dihedral group of order \(2p\), namely the identity, trivial homomorphism and \(p\) reflection retractions. That dimension-one case is **prior coverage** and is not asserted new. Their general small-group tables and cat² isomorphism counts do not present a complete rank-stratified commuting graph, all maximal compatible retraction systems or degree census for the higher-dimensional elementary generalized dihedral family. The simultaneous diagonalization of commuting idempotent linear transformations is classical and is used here as an input rather than claimed as a new lemma. Related element-commuting and subgroup-commuting graphs address different vertex sets and do not by themselves imply a commuting graph of retractions. The formulas here concern \(d\ge2\) and supply the exact graph-theoretic structure for this family.

## Limitations

Only elementary abelian odd-prime rotation kernels are treated. The result does not classify idempotent endomorphisms for arbitrary odd abelian kernels, characteristic two, or non-elementary finite \(p\)-groups; nor does it classify cat²-group structures, which impose extra kernel-commutator restrictions. The degree distribution is given as a rank-indexed multiset without asserting the values from different ranks are distinct. Although the checked primary source does not imply the theorem, an equivalent enumeration may exist under alternate terminology for affine projection semigroups or compatible retractions. No independent external mathematical audit or exhaustive literature-priority proof has been performed.

## References

1. Z. Arvasi, A. Odabaş and C. D. Wensley, *Computing 3-Dimensional Groups: Crossed Squares and Cat²-Groups*, arXiv:1911.12799, publicly posted 2019-11-28; *Journal of Symbolic Computation* 114 (2023), 267–281, doi:10.1016/j.jsc.2022.04.020. Accepted author manuscript: https://pure.bangor.ac.uk/ws/portalfiles/portal/50652037/cat2_xs2_final.pdf. The relevant comparison is Section 4.4, p. 12 of the article proper (PDF page 13).
2. V. Kakkar and G. S. Rawat, *On Commuting Graphs of Generalized Dihedral Groups*, arXiv:1806.03614 (2018). This addresses commuting *elements* of groups rather than commuting endomorphisms, and is used only for the distinction of graph conventions.
