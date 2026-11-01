# Integral conjugation homology and quotient topology of cyclic Frobenius group clique complexes

## Finding

Let \(P\ne1\) be a finite abelian \(p\)-group, of order \(N\), and let \(H=C_m\) be cyclic of order \(m>1\) acting on \(P\) by automorphisms, with **no nonzero fixed point for any nonidentity element of** \(H\). Assume \(\gcd(p,m)=1\), and let \(G=P\rtimes H\). Let \(X_G\) be the clique complex whose vertices are nonidentity prime-power-order elements of \(G\), where pairwise commuting vertices of mutually distinct prime orders span a simplex (equivalently, vertices of pairwise distinct prime-power prime supports which commute).

Write \(m=\prod_{i=1}^{r}q_i\), where the \(q_i\) are the maximal powers of the distinct prime divisors of \(m\), and put
\[
  b=\prod_{i=1}^{r}(q_i-2),\qquad
  D_i=(C_{q_i})\setminus\{1\},\qquad
  L=\bigotimes_{i=1}^{r}\ker\bigl(\mathbb Z[D_i]\xrightarrow{\varepsilon}\mathbb Z\bigr).
\]
Here \(\varepsilon\) sends every basis element to \(1\), and \(L\) has integral rank \(b\), including rank zero if a factor is \(q_i=2\).

**Complete simplicial decomposition.** The complex \(X_G\) is the disjoint union of \(N\) simplicial complexes each isomorphic to \(D_1*\cdots*D_r\), together with \(N-1\) isolated vertices. For \(r\ge2\), it therefore has exactly \(2N-1\) connected components. Each nontrivial component is homotopy equivalent to \(\bigvee^{b} S^{r-1}\) (interpreted as contractible when \(b=0\)), and the only reduced integral homology is
\[
\widetilde H_0(X_G;\mathbb Z)\cong\mathbb Z^{2N-2},\qquad
\widetilde H_{r-1}(X_G;\mathbb Z)\cong\mathbb Z^{Nb}.
\]
These degrees are distinct because \(r\ge2\). For \(r=1\), the complex consists entirely of \(Nm-1\) isolated vertices, so only \(\widetilde H_0\cong\mathbb Z^{Nm-2}\) remains.

**Complete integral conjugation action, for \(r\ge2\).** Let \(G\) act on \(X_G\) by conjugation. Write a group element \((a,h)\) and label the complement components by \(x\in P\). On their labels the action is affine, \(x\mapsto a+h(x)\). Then
\[
\widetilde H_{r-1}(X_G;\mathbb Z)\cong\mathbb Z[P]\otimes_{\mathbb Z} L,
\]
where \(G\) acts on \(\mathbb Z[P]\) through this affine permutation and trivially on \(L\). On degree zero, the integral action is exactly the augmentation kernel
\[
\widetilde H_0(X_G;\mathbb Z)=\ker\left(
\mathbb Z[P]_{\mathrm{affine}}\oplus\mathbb Z[P\setminus\{0\}]_{\mathrm{linear}}
\xrightarrow{\varepsilon}\mathbb Z\right).
\]
Consequently the rational top-degree character, if \(r\ge2\), has just three values:
\[
\operatorname{tr}\bigl(g\mid\widetilde H_{r-1}(X_G;\mathbb Q)\bigr)
=\begin{cases}Nb,&g=1,\\0,&g\in P\setminus\{0\},\\b,&g\in G\setminus P.\end{cases}
\]

**Orbit-space topology.** The geometric quotient by conjugation satisfies
\[
  |X_G|/G\;\cong\; |X_H|\;\sqcup\;
  \underbrace{\{\mathrm{pt}\}\sqcup\cdots\sqcup\{\mathrm{pt}\}}_{(N-1)/m\ \mathrm{points}},
\]
where the number of isolated points is integral because \(H\) acts freely on \(P\setminus\{0\}\). Thus for \(r\ge2\), the quotient has \(1+(N-1)/m\) components and \(b\) spheres of dimension \(r-1\) in its unique nontrivial component.

## Assumptions and scope

The fixed-point-free hypothesis means that each \(1-h:P\to P\) is bijective for \(h\ne1\). The kernel is an abelian **single-prime** group; the assertion about its isolated vertices is not claimed for a kernel involving several distinct primes. The complex uses the **prime-power decomposition** construction of Bate, Everitt and Ford, not the ordinary commuting graph or the independent-generating-set complexes on groups. The group action is inner conjugation, and the quotient above is an actual topological orbit space, not a homotopy orbit construction.

## Proof

**1. Unique complementary cosets.** Use additive notation on \(P\) and multiplication on \(H\):
\[
 (a,h)(c,k)=(a+h(c),hk).
\]
For each \(x\in P\), put \(H_x=(x,1)H(-x,1)\). Its elements are \(((1-h)x,h)\) for \(h\in H\). When \(h\ne1\), the endomorphism \(1-h\) is invertible, so each \((a,h)\) with \(h\ne1\) belongs to exactly one \(H_x\), namely \(x=(1-h)^{-1}a\). Distinct \(H_x\) intersect only in the identity. Elements in \(P\setminus\{0\}\) have \(p\)-power order; an element in \(H_x\setminus\{1\}\) has the same order as its unique \(h\)-coordinate and hence has order coprime to \(p\).

**2. Exact commuting criterion.** For \(h,k\ne1\), let \(u=((1-h)x,h)\in H_x\) and \(v=((1-k)y,k)\in H_y\). Since \(H\) is abelian, direct multiplication shows
\[
 uv=vu\quad\Longleftrightarrow\quad
 (1-h)(1-k)(x-y)=0\quad\Longleftrightarrow\quad x=y.
\]
The final equivalence uses invertibility of both factors. Also, if \(a\in P\setminus\{0\}\) and \((c,h)\notin P\), commutation would force \(h(a)=a\), which is impossible. Thus every nontrivial element of \(P\) is an isolated vertex in \(X_G\), and no simplex joins two different complements.

**3. The full simplicial decomposition.** The vertices in \(H_x\) correspond to the nonidentity elements of prime-power order in the cyclic group \(H\); commuting is automatic inside \(H_x\), and a simplex contains at most one element from each prime-power primary factor. Hence the induced subcomplex is \(D_1*\cdots*D_r\). Step 2 proves these are all the simplices. The disjoint-union decomposition follows.

**4. Integral homotopy and homology.** Each \(D_i\) has \(q_i-1\) isolated vertices and \(\widetilde H_0(D_i;\mathbb Z)=\ker\varepsilon_i\), a free lattice of rank \(q_i-2\). The integral join Künneth formula gives the indicated tensor product \(L\) in degree \(r-1\), with all other reduced homology zero. The join is a wedge of top-dimensional spheres: the two-factor case is the complete bipartite graph \(K_{q_1-1,q_2-1}\), and adjoining another discrete set is a wedge of suspensions (or a cone if it has one vertex). If \(r\ge2\), each join is connected; adding \(N-1\) isolated points yields \(2N-1\) components and the claimed homology. If \(r=1\), all \(N(m-1)+N-1=Nm-1\) nonidentity elements of prime-power order are isolated vertices.

**5. Integral \(G\)-modules.** Conjugation by \((a,h)\) carries \(H_x\) to \(H_{a+h(x)}\). Under the distinguished identification \(H_x\cong H\), the \(H\)-coordinate of each element is unchanged, because \(H\) is abelian. Thus every affine component permutation acts identically on its internal integral homology, giving \(\mathbb Z[P]\otimes L\) with trivial coefficient action. On the isolated vertices \(P\setminus\{0\}\), conjugation acts by \(c\mapsto h(c)\); on all components, \(H_0\) is their permutation lattice and reduced \(H_0\) is its augmentation kernel. For \(g\in G\setminus P\), the affine map \(x\mapsto a+h(x)\) has exactly one fixed point because \(1-h\) is invertible. A nontrivial pure translation has none, and the identity has \(N\), yielding the three character values.

**6. The geometric quotient.** Conjugation is transitive on the \(N\) copies of \(X_H\), with stabilizer of \(H_0=H\) equal to \(H\) itself (by uniqueness in Step 1). This stabilizer fixes every point of \(X_H\), since \(H\) is abelian. The quotient of the union of those copies is therefore homeomorphic to \(|X_H|\). Meanwhile \(G\) acts on the kernel's nonidentity elements through \(H\), freely and with orbits of size \(m\). This gives the asserted isolated-point quotient.

## Verification

Run `python verify.py` with Python 3 standard library only. It directly enumerates group elements and the prime-power commuting edges in four independent cyclic scalar-action examples \((|P|,m)=(7,6),(13,12),(31,15),(43,21)\), compares exact vertex, edge and component counts, checks the unique-complement labels of every edge, and checks the bipartite induced subgraphs. The computed first Betti numbers are \(0,26,93,215\). An additional three-prime-factor local check records \(f=(12,44,48)\) and reduced Euler characteristic \(15\) for \(X_{C_{105}}\). These checks are **finite corroboration**; Steps 1–6 establish the universal statement.

For example, \(C_{31}\rtimes C_{15}\) with scalar action by multiplication by \(7\) has \(61\) connected components, \(\widetilde H_1\cong\mathbb Z^{93}\), and a quotient homeomorphic to \(K_{2,4}\) disjoint union two points.

## Relationship to prior work

Bate, Everitt and Ford introduced precisely this prime-power clique complex in July 2026. Their Lemma 3 and Proposition 9 identify the join structure and ordinary homology of the **nilpotent** complement; their Section 2.2 explicitly treats cyclic rotations inside dihedral groups, and Section 2.6 gives non-mono-connected examples from wreath products. These results provide the ingredient \(X_H\) but not the new fixed-point-free semidirect-product decomposition, its unrestricted kernel-size dependence, the complete integral conjugation modules, or the topology of the orbit space.

Cameron's earlier group simplicial-complex constructions use independence and generation relations, so their simplices are not those of this prime-power commuting complex. Known Frobenius-partition descriptions for Engel graphs concern a different edge relation and do not state this topology or integral character.

## Limitations

The theorem requires an abelian \(p\)-group kernel, cyclic complement and fixed-point-free complement action. No corresponding decomposition is asserted for non-abelian kernels, noncyclic complements, or actions with nonzero fixed points. It concerns ordinary integral homology under conjugation, not order-sheaf homology or equivariant stable homotopy. For \(q_i=2\), the corresponding join is a cone and contributes no positive-degree homology. Finite tests do not prove the all-parameter claim; the formal proof does. Independent mathematical validation and exhaustive comparison against unindexed literature have not been performed.

## References

1. M. Bate, B. Everitt and S. Ford, *Clique complexes of groups and order sheaves*, arXiv:2607.22369v1 (first public 2026-07-24), especially Lemmas 1, 3, Section 2.2, Section 2.6 and Proposition 9. https://arxiv.org/abs/2607.22369
2. P. J. Cameron, *Simplicial complexes defined on groups*, arXiv:2410.22260v1 (2024-10-29); journal version in *Open Mathematics* 23 (2025), 20250171. https://arxiv.org/abs/2410.22260
