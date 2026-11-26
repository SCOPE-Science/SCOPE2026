# Minimum zero forcing sets of triangle-core annihilating-ideal graphs

## Finding

Let \(F_n(m)\) consist of \(n\ge1\) triangles with one common vertex \(c\), plus \(m\ge1\) pendant leaves, all at \(c\). The two vertices other than \(c\) in each triangle form a *triangle pair*. Under standard zero forcing:

- If \(m\ge2\), then \(Z(F_n(m))=n+m-1\). The minimum sets choose one vertex from each triangle pair and all but one pendant leaf, for \(m2^n\) sets.
- If \(m=1\), then \(Z(F_n(1))=n+1\). A minimum set chooses one vertex from each triangle pair and one extra vertex: the center, the pendant leaf, or the second vertex in exactly one triangle pair. There are \(2^{n-1}(n+4)\) such sets.
- Let \(K_3(1,1,1)\) be a triangle with one pendant leaf at each of its three core vertices. It has zero forcing number two and exactly nine minimum pairs: two leaves, or a core vertex and a leaf not attached to it.

For finite commutative rings with identity whose annihilating-ideal graphs contain a cycle and have only triangles as simple cycles, the resulting values are as follows. Write \(F_1(m)=K_3(m)\).

| Graph | Zero forcing number | Number of minimum sets |
|---|---:|---:|
| \(K_3(1)\) | \(2\) | \(5\) |
| \(K_3(2)\) | \(2\) | \(4\) |
| \(K_3(3)\) | \(3\) | \(6\) |
| \(K_3(1,1,1)\) | \(2\) | \(9\) |
| \(F_{2^r}(2)\), \(r\ge1\) | \(2^r+1\) | \(2^{2^r+1}\) |
| \(F_{(q+1)/2}(1)\), \(q=p^k\), \(p\) an odd prime, \(k\ge1\) | \((q+3)/2\) | \(2^{(q-1)/2}(q+9)/2\) |
| \(F_{(q-1)/2}(3)\), same range of \(q\) | \((q+3)/2\) | \(3\cdot 2^{(q-1)/2}\) |

The last row at \(q=3\) repeats \(K_3(3)\). The two odd-field families at a common \(q\) have equal zero forcing numbers and unequal numbers of minimum sets. In the two-leaf family the number of triangles is a power of two, not an arbitrary even number.

## Proof of the zero forcing classification

A blue vertex may force its unique white neighbor. If the two vertices of a triangle pair start white then neither can be the first of the pair to be forced: the center sees both, and both members are white. Two white pendant leaves at the center likewise cannot be forced first. Thus every starter meets each triangle pair and uses at least \(m-1\) leaves. For \(m\ge2\) both lower bounds are tight simultaneously: a chosen leaf forces \(c\), one chosen vertex per triangle pair forces its mate, and \(c\) forces the last white leaf. Equality in the lower bound specifies exactly these starters.

For \(m=1\), a set with one per triangle pair and no extra vertex stalls, since each blue vertex sees its white mate and the white center. At size \(n+1\), if the extra vertex is \(c\), complete the pairs and then force the leaf; if it is the leaf, first use it to force \(c\); if it is a second vertex in a pair, a vertex in that pair first forces \(c\). These are exhaustive, and their numbers are \(2^n,2^n,n2^{n-1}\), respectively.

For \(K_3(1,1,1)\), one core vertex cannot move alone, and one leaf can force its core vertex but then stalls. With two leaves blue, their core vertices become blue and either can force the third core vertex, after which its leaf is forced. If the starter is a core vertex and a leaf at another core vertex, use the leaf to make that second core vertex blue. The second core vertex then forces the third core vertex, and the remaining leaves are forced. Two core vertices, or a core vertex and its own leaf, stall. This gives \(3+6\) minimum pairs.

## Finite-ring scope and parameter check

For a finite commutative ring with identity, the annihilating-ideal graph has an edge between distinct nonzero ideals \(I,J\) when \(IJ=0\); its vertices are the nonzero ideals with nonzero annihilator. A finite commutative ring is a product of finite local rings. In a finite local ring the maximal ideal is nilpotent, so a proper ideal is annihilated by a nonzero ideal; the same conclusion holds for any proper ideal of the product by taking a coordinate where the ideal is proper. Hence the vertices are exactly the nonzero proper ideals.

If there are at least four local factors, four ideals supported on different single coordinates give a four-cycle. With three factors, the same happens if one factor is not a field: take two distinct ideals supported in that factor and one in each other factor, and alternate the two groups to obtain the cycle. A product of three fields instead gives \(K_3(1,1,1)\), by disjointness of singleton and doubleton supports. With two factors that are both nonfields there are two distinct nonzero ideals supported in each coordinate and all cross products vanish, yielding a four-cycle. For two factors \(k\times B\) with \(k\) a field and \(B\) local, two distinct nonzero proper ideals \(I,I'\) of \(B\) supply the cycle
\[
k\times0,\quad 0\times I,\quad k\times J,\quad 0\times I',\quad k\times0,
\]
where \(J\) is any nonzero minimal ideal of \(B\), which annihilates both \(I\) and \(I'\). If \(B\) is a field there is just an edge; if it has exactly one nonzero proper ideal \(M_B\), then \(M_B^2=0\) and the four vertices are a path, not a triangle. Thus the only nonlocal case with a cycle and no longer cycle is the product of three fields.

Now let \(R\) be local, with maximal ideal \(M\) and residue field \(k\). Minimal nonzero ideals lie in the socle \(\operatorname{Ann}(M)\) and are universal vertices. If the socle had dimension at least two over \(k\), its minimal ideals would include at least three distinct lines. These together with \(M\), distinct from the lines in this case, yield a four-cycle. There is therefore exactly one minimal nonzero ideal \(C=\operatorname{Ann}(M)\), and every nonzero ideal contains it. In the presence of a cycle we have \(M\ne C\), and \(M\) is a leaf at \(C\). Among vertices other than \(C\) a vertex cannot be adjacent to two others, as those three vertices and the universal vertex would yield a four-cycle. The graph is thus some \(F_n(m)\), with \(C\) its center and \(M\) one of its leaves.

In this local case the annihilator operation on ideals is an involution. To see this, extend a nontrivial additive character of \(C\) to the additive group of \(R\). For the resulting character \(\chi\), the pairing \((x,y)\mapsto\chi(xy)\) is nondegenerate: every nonzero principal ideal contains \(C\). The orthogonal of an ideal \(I\) under this pairing is precisely \(\operatorname{Ann}(I)\), because if \(xI\ne0\) it contains \(C\) and \(\chi\) is not trivial on it. Orthogonality for the perfect finite-group pairing now gives the double annihilator identity.

For a triangle pair \(I,J\), \(\operatorname{Ann}(I)\) contains \(J\); if unequal to \(I\), it is a noncentral neighbor of \(I\) and must be \(J\). If instead it equals \(I\), then \(J\subsetneq I\) and \(\operatorname{Ann}(J)\) contains \(I\), so is a noncentral neighbor of \(J\) and must also be \(I\), contradicting injectivity. Hence \(\operatorname{Ann}(I)=J\) and \(\operatorname{Ann}(J)=I\). For any leaf \(L\ne M\), the annihilator cannot be \(C\) by injectivity, nor a distinct noncentral vertex because \(L\) has no such neighbor. Thus \(\operatorname{Ann}(L)=L\) and \(L^2=0\).

Ideals \(I,U\) in different triangle pairs are incomparable: containment of one in the other would annihilate the larger ideal's mate. Their intersection is \(C\): any strict intermediate ideal below \(I\) and above \(C\) annihilates the mate of \(I\), and so would have to equal that mate; the mate cannot also be contained in \(U\). Their sum is \(M\): it is not a triangle ideal, since it contains ideals from two different pairs, and cannot be another leaf since \(IU\ne0\). If \(n\ge2\), comparing any two ideals in the same pair with a fixed ideal \(U\) in another pair now shows that the two have the same cardinality, since their sums with \(U\) are both \(M\) and their intersections with \(U\) both \(C\). In particular all triangle pairs are incomparable in this case. When a pair \(I,J\) is incomparable, both ideals cover \(C\), since any strict intermediate ideal annihilates the other. For \(n\ge2\) we can then write \(M/C\) as the direct sum of two simple modules by using ideals from different pairs. If \(n=1\) and the single pair is incomparable, its intersection is \(C\) and its sum is also \(M\): if its sum were another leaf, that sum's square would be zero and would imply \(I\subseteq\operatorname{Ann}(I)=J\), impossible. Thus this case also gives the direct sum of two simple modules.

For the remaining local case \(n=1\), suppose \(C\subsetneq J\subsetneq I\) in the triangle pair. An extra leaf \(L\ne M\) must be incomparable with both: \(L\subseteq I\) would give \(LJ=0\), and if \(L\) contained either one then \(L^2=0\) would give a noncentral neighbor. The sums \(I+L\) and \(J+L\) therefore cannot be triangle ideals, or leaves other than \(M\) (their squares are nonzero because \(IL\) and \(JL\) are nonzero). Both sums are \(M\). Their intersections with \(L\) equal \(C\), since any strict intermediate ideal between \(C\) and \(I\) must equal \(J\) and \(J\) is not contained in \(L\). The sum/intersection cardinality identity would give \(|I|=|J|\), a contradiction. Thus there is no extra leaf: the graph in this case is \(K_3(1)\), realized, for example, by \(k[t]/(t^5)\).

Finally, when \(M/C\) is a direct sum of two simple modules it is a two-dimensional vector space over \(k\). The ideal product gives a well-defined nondegenerate symmetric bilinear form \(M/C\times M/C\to C\cong k\): \(M^2\subseteq C\), \(MC=0\), and a vector orthogonal to all of \(M/C\) must lie in \(\operatorname{Ann}(M)/C=0\). The proper ideals strictly between \(C\) and \(M\) are the \(q+1\) lines of this space, where \(q=|k|\). Perpendicularity pairs the lines by an involution. Its fixed lines are the isotropic lines and give the leaves besides \(M\); its two-cycles give the triangle pairs. In odd characteristic a nondegenerate symmetric binary form has zero or two isotropic lines (diagonalize and solve a nonzero square equation). This gives respectively \(F_{(q+1)/2}(1)\) and \(F_{(q-1)/2}(3)\). In characteristic two an alternating form makes every line isotropic, hence produces no triangles. A nonalternating form has exactly one isotropic line: the square map on the finite field is bijective, so its quadratic self-pairing is the square of a nonzero linear form. Then \(m=2\) and \(2n=q=2^{r+1}\) for \(r\ge0\). The case \(r=0\) is \(K_3(2)\).

All stated bilinear-form cases are realized by taking the ring \(k\oplus k^2\oplus kz\), with products of vectors given by the form multiplied by \(z\), and with \(z(k^2\oplus kz)=0\). This is associative because all products of three elements of its maximal ideal vanish. In odd characteristic take a split binary form or the diagonal form \(x^2-dy^2\) for a nonsquare \(d\); in characteristic two take a nonsingular nonalternating diagonal form. This proves the realizable parameter ranges used in the table. Substituting them into the graph formulas gives the stated zero forcing values and counts.

## Verification and relation to prior work

The accompanying bounded graph checker enumerates all starters by size for \(1\le n\le6\), \(1\le m\le4\), and for \(K_3(1,1,1)\), testing exact equality of the predicted and enumerated minimum-set families. It also checks the algebraic specialization at sample parameter values, not ring existence or the exclusion of other rings. The universal graph and ring arguments above are analytic.

Yu and Wu study the ring classification for cores consisting only of triangles [1]. The finite-ring argument is included here to make the parameters supporting the zero forcing table explicit; ring classification is not claimed as new. The zero forcing polynomial of Boyer et al. [2] is a general cardinality framework. Equal-blade windmills, and triangle friendship graphs without a center leaf, do not have the mixed triangle-and-pendant structure above. The additional conclusions here are the exact minimum starter families, counts and their finite-ring specialization, not the full zero forcing polynomial or a characterization of individual rings beyond their graph types.

1. H. Yu and T. Wu, “Commutative Rings \(R\) Whose \(C(AG(R))\) Consist of Only Triangles,” *Communications in Algebra* 43 (2015), 1076–1097. DOI: 10.1080/00927872.2013.847950.
2. K. Boyer et al., “The zero forcing polynomial of a graph,” *Discrete Applied Mathematics* 258 (2019), 35–48. DOI: 10.1016/j.dam.2018.11.033.
