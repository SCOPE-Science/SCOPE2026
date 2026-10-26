# Sharp rooted colour refinement on Cartesian powers of odd cycles

## Finding
For integers \(r\ge2\) and \(d\ge1\), let \(G=C_{2r+1}^{\square d}\), with the usual simple-cycle adjacency in each coordinate. Give \(o=(0,\ldots,0)\) a unique initial colour and all other vertices one common colour. Iterate ordinary synchronous one-dimensional counting colour refinement, always retaining the preceding colour in the refinement signature.

Define \(\delta(a)=\min(a,2r+1-a)\) for \(a\in\{0,\ldots,2r\}\), and for \(x=(x_1,\ldots,x_d)\), define \(j_\ell(x)=|\{i:\delta(x_i)=\ell\}|\) for \(0\le\ell\le r\) and \(D(x)=\sum_{\ell=0}^{r}\ell j_\ell(x)\). For every integer \(0\le t\le rd-1\), two vertices have the same colour after \(t\) refinement rounds precisely if either their profiles \((j_0,\ldots,j_r)\) coincide, or both have \(D>t\). In the latter clause the common colour is the single not-yet-reached class; a profile with \(D\le t\) always has its own class.

Consequently the first round at which the stable partition has been reached is exactly
\[
\tau(G,o)=rd-1.
\]
At that round, the colour classes are exactly the orbits of automorphisms fixing \(o\), with \(\binom{d+r}{r}\) classes. The class associated with \((j_0,\ldots,j_r)\), where \(\sum j_\ell=d\), has size
\[
\frac{d!}{\prod_{\ell=0}^{r}j_\ell!}\,2^{d-j_0}.
\]
Here “first stable round” means the earliest partition equal to all its subsequent refinements; the extra attempted no-change update used by an implementation to detect stabilization is not counted.

## Assumptions and scope
The cycle \(C_{2r+1}\) has vertex set \(\mathbb Z/(2r+1)\mathbb Z\), and two vertices are adjacent exactly when their difference is \(\pm1\). The Cartesian power has vertex set \((\mathbb Z/(2r+1)\mathbb Z)^d\), adjacent pairs differing by \(\pm1\) in exactly one coordinate. The graph is simple and \(2d\)-regular. Colours are partitions, not particular integer labels. The root is individualized before round zero. Parameters \(r,d\) are arbitrary integers in the indicated ranges; no restriction on the number of graph vertices is imposed.

## Proof
**Distance layers and propagation.** Graph distance from \(o\) is \(D(x)\) because each step changes a single cycle-coordinate distance by at most one, while shortest coordinate paths concatenate. Ordinary one-dimensional counting refinement at round \(t\) depends only on the radius-\(t\) initially coloured neighbourhood unfolded as a rooted walk tree. If \(D(x)>t\), that neighbourhood contains no individualized vertex. Since the underlying uncoloured Cartesian power is vertex-transitive and regular, all such vertices have the same round-\(t\) colour. At round zero, \(D=0\) is the unique root, and all vertices with \(D>0\) share the other colour.

**Recovering a profile from the preceding layer.** Fix a vertex with \(D>0\), writing its distance profile as \(j=(j_0,\ldots,j_r)\). An odd cycle has *exactly one* neighbour closer to its root among the two neighbours of every nonzero-distance vertex, including distance \(r\). Consequently there are exactly \(M=\sum_{\ell=1}^r j_\ell=d-j_0\) neighbours at graph distance \(D-1\). For each \(\ell\ge1\), exactly \(j_\ell\) such neighbours have profile \(j-e_\ell+e_{\ell-1}\), where \(e_i\) denotes the \(i\)-th standard basis vector. From the multiset of those neighbours' profiles, write \(S_i\) for the sum of the \(i\)-th profile coordinates, counted with multiplicity. The identities are
\[
S_0=Mj_0+j_1,\qquad S_i=(M-1)j_i+j_{i+1}\quad(1\le i<r),\qquad S_r=(M-1)j_r.
\]
Because \(M>0\), this data uniquely reconstructs the original profile: \(j_0=d-M\), \(j_1=S_0-Mj_0\), and \(j_{i+1}=S_i-(M-1)j_i\) for \(1\le i<r\). The reconstruction is an integer identity, not an inference from finite samples.

**Exact partition at each round.** Induct on \(t\). Assume the claimed partition after round \(t-1\). Every profile at distance at most \(t-1\) has its own known colour, and all vertices at distance greater than \(t-1\) have one common colour. A vertex with \(D=t\) has its distance-decreasing neighbours at distance \(t-1\), whose colours uniquely encode their profiles by induction. The preceding paragraph reconstructs its profile from those neighbour colours, so different profiles in layer \(t\) split. Moreover every such vertex has at least one predecessor at distance \(t-1\), whereas a vertex with \(D>t\) has no neighbour in that layer; thus layer \(t\) splits from the farther background. Old distinctions persist because the refinement signature contains the previous colour. All vertices with \(D>t\) still have one colour by the propagation argument. This proves the claimed partition for every \(t\).

**Orbit exactness, sharpness, and sizes.** Coordinatewise cycle reflections fixing zero can independently change either sign of each nonzero coordinate without changing its distance. Permutations of the \(d\) coordinate factors are graph automorphisms fixing \(o\). Their group is transitive on each profile class, so each profile lies inside one automorphism orbit. Conversely, colour refinement is automorphism-invariant, and its terminal partition separates different profiles, so no orbit crosses profiles. Hence the stable classes are precisely the full root-stabilizer orbits.

There is a unique profile with \(D=rd\): every coordinate has distance \(r\). At round \(rd-1\), all other profiles are separately coloured by the induction, and this last profile forms the remaining class. The resulting orbit partition is invariant and cannot split further. At round \(rd-2\), which is nonnegative because \(r\ge2\), profiles of distances \(rd-1\) and \(rd\) still share the background colour. Both exist (replace one distance-\(r\) coordinate by distance \(r-1\)). Therefore \(rd-1\) is the first stable round. Finally, a profile consists of a weak composition of \(d\) into \(r+1\) parts. For a chosen profile, its coordinate distances can be arranged in \(d!/\prod j_\ell!\) ways, and each nonzero distance has two signs in an odd cycle; this proves the class-count and class-size formulas.

## Verification
A self-contained Python 3 standard-library verifier, `odd_cycle_wl_verifier.py`, constructs ordinary Cartesian powers and performs the full vertex-level colour-refinement algorithm independently of a second implementation on weighted orbit quotients. It also checks every intermediate-distance-layer assertion in the tested full graphs, checks degree and downward-neighbour identities in quotient profiles, reconstructs profiles from predecessor-moment equations, and compares exact cell sizes. Execute `python3 odd_cycle_wl_verifier.py`. The accompanying `verification_output.txt` records the replayed result: `FULL_CASES 20 TOTAL_VERTICES 4006`, `QUOTIENT_CASES 56 TOTAL_PROFILES 2898`, `ALL_TESTS_PASS`. These finite checks support the general proof but do not replace its induction.

## Relationship to prior work
The usual counting colour-refinement algorithm and its relationship to stable equitable partitions are treated by Kersting, Mladenov, Garnett, and Grohe (2014). Kiefer and McKay (2020) address extremal iteration numbers for general graphs; their long-refinement constructions are not rooted odd-cycle Cartesian powers. Kluge (2022) studies 2-dimensional refinement on cyclic Cayley graphs and vertex individualization for prime-order circulants; neither result controls one-root, one-dimensional refinement on arbitrary Cartesian powers. Classical rooted Hamming products of complete graphs are distinct: the odd cycles considered here have length at least five and are not complete graphs. The present statement gives the complete *round-by-round* profile, a sharp exact stopping time, and root-orbit equality for all indicated odd-cycle lengths and Cartesian dimensions. Searches did not identify an earlier theorem giving these conclusions; this is not a guarantee of bibliographic priority.

## Limitations
Only odd cycles of length at least five and Cartesian powers of a single common cycle length are addressed. The proof uses a unique distance-decreasing cycle neighbour; this premise fails at the antipode of an even cycle. Products of unequal cycle lengths or additional individualized vertices are not covered. The assertion is about refinement partitions, not graph-isomorphism identification against arbitrary other graphs. Scientific priority remains subject to independent literature assessment.

## References
1. K. Kersting, M. Mladenov, R. Garnett, M. Grohe, “Power Iterated Color Refinement,” *Proceedings of AAAI 2014*, doi:10.1609/aaai.v28i1.8992, publicly dated 2014-06-21, https://ojs.aaai.org/index.php/AAAI/article/view/8992/8851.
2. S. Kiefer, B. D. McKay, “The Iteration Number of Colour Refinement,” *ICALP 2020*, doi:10.4230/LIPIcs.ICALP.2020.73, https://drops.dagstuhl.de/storage/00lipics/lipics-vol168-icalp2020/LIPIcs.ICALP.2020.73/LIPIcs.ICALP.2020.73.pdf.
3. L. Kluge, “Combinatorial refinement on circulant graphs,” arXiv:2204.01054v2 (2022), https://arxiv.org/html/2204.01054v2.
