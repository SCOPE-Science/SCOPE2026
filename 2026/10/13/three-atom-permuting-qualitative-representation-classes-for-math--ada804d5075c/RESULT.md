# Two atom-permuting qualitative representation classes for \(\mathfrak E_8^{\{3\}}\)

## Finding

The seven-colour trichromatic chromatic algebra \(\mathfrak E_8^{\{3\}}\) has exactly two qualitative representation classes up to simultaneous permutation of the base points and diversity atoms: one on seven points and one on eight points. The eight-point class is the unique perfect one-factorization of \(K_8\). Its group allowing colour permutations has order \(42\) and vertex orbits of sizes \(1\) and \(7\). **Only deletion of the fixed vertex** gives a qualitative representation on seven points. Deleting any vertex of the other orbit leaves a colouring with just 29 of the required 35 triples.

## Assumptions and scope

In the edge-colouring interpretation, no triangle may use fewer than three colours, and every unordered triple of distinct colours must appear on a triangle. This uses the qualitative representation convention of Al-Juaid, Jackson, Koussas and Kowalski [1]. Their base-size and unique-extension theorem gives sizes seven and eight here, and every seven-point representation extends to an eight-point representation. Permuting the seven diversity colours preserves the algebra's operations; the classification does not keep the names of individual atoms fixed.

## Proof

### The eight-point class

At any vertex of an eight-point representation all seven incident colours are distinct; otherwise two like-coloured edges would form part of a forbidden triangle. Each colour is therefore a perfect matching, and the colouring is a one-factorization. Call a one-factorization perfect when the union of every two factors is a Hamiltonian cycle. The union of two distinct factors on eight vertices is either one 8-cycle or two 4-cycles. In the latter case the two colours can appear together on a triangle only by using one of the four diagonals of the two 4-cycles for the third edge. These diagonals cannot realize all five choices for that third colour. Thus a qualitative factorization of \(K_8\) must be perfect. Seah and Stinson [2] give uniqueness of the perfect one-factorization up to isomorphism.

Use the standard affine construction of [1, Lemmas 5.1–5.2], with vertices \(\mathbb F_7\cup\{\infty\}\) and colours \(\mathbb F_7\):
\[
c(x,y)=(x+y)/2\quad (x,y\in\mathbb F_7,\ x\ne y),\qquad c(\infty,x)=x.
\]
At a finite vertex \(x\), the colours to the other finite vertices run over all colours except \(x\); that last colour occurs on the edge to \(\infty\). Thus the colouring is proper and is a one-factorization. Given distinct colours \(a,b,c\), the finite vertices
\[
a+b-c,\qquad a+c-b,\qquad b+c-a
\]
are distinct and their pairwise midpoints are \(a,b,c\). Conversely, the midpoint equations force this unordered vertex triple for any finite triangle with those colours. This proves qualitative coverage already on the seven finite vertices, hence also on all eight. Combined with necessity and perfect-factorization uniqueness, it proves the converse as well: every perfect one-factorization of \(K_8\) is qualitative.

### Which deletions are representations?

A colour triple has an additional triangle through \(\infty\) precisely when one of its members is the midpoint of the other two, i.e. when the triple is a three-term arithmetic progression. There can be at most one midpoint in a distinct triple over \(\mathbb F_7\): if two members were each the midpoint of the other two, their difference multiplied by 3 would be zero. For a triple \(\{s-d,s,s+d\}\), the additional triangle has vertices \(\infty,s-d,s+d\), whereas the finite triangle has vertices \(s-2d,s,s+2d\). The two witnesses are disjoint. Thus no single deletion destroys a progression triple.

For instance the colours \(\{2,4,5\}\) are not a progression and occur only at the finite triangle \(\{0,1,3\}\), so deletion of \(0\) fails. Translations of the field extend to automorphisms fixing \(\infty\) and relabelling colours, so the same holds at every finite vertex. More precisely, the colour triple on a finite triangle is an affine image of its vertex triple: if \(S\) is the sum of the three vertices, associate each vertex \(v\) with the opposite colour \((S-v)/2\). Of the \(\binom62=15\) finite triangles through a fixed finite vertex, nine are progressions: there are \(7\cdot3=21\) progression triangles, each counted at three vertices, distributed equally by translation. The other six are unique witnesses for six different non-progression colour triples. A finite deletion therefore leaves \(35-6=29\) colour triples. Deleting \(\infty\) leaves all 35 finite witnesses. By the extension theorem any seven-point qualitative representation is one of the restrictions just classified, so there is exactly one seven-point class.

### Automorphisms

Every colour-permuting automorphism fixes \(\infty\) because it is the unique vertex whose deletion preserves full coverage. Its induced colour permutation agrees with its permutation \(f\) of the finite vertices by the edges at \(\infty\), so \(f((x+y)/2)=(f(x)+f(y))/2\). This also holds for \(x=y\). Subtract \(f(0)\) to obtain \(g(0)=0\). Applying the midpoint identity first to \((0,2u)\), then to \((x,y)\), gives \(g(2u)=2g(u)\) and \(g(x+y)=g(x)+g(y)\). Since \(\mathbb F_7\) is prime, \(f(x)=a x+b\) with \(a\ne0\). All such maps preserve the colouring up to colour permutation. This yields order \(7\cdot6=42\) and the asserted vertex orbits.

## Verification

Run `python3 verify.py`. The script enumerates all 105 perfect matchings and 416 one-factorizations containing one fixed matching, tests all triangle triples and pairwise unions, and computes the six isomorphism classes under vertex relabelling. It verifies that exactly one is qualitative and perfect, computes the automorphisms of the affine representative and tests coverage on every induced seven-point subcolouring. `VERIFICATION.md` gives the computed restriction counts. The general extension input is cited in [1], not inferred from the computation.

## Relationship to prior work and limitations

Al-Juaid et al. [1, Lemmas 5.1–5.2 and Theorem 5.3] establish existence, give the affine example, and supply the extension theorem and colouring interpretation. The enumeration of six one-factorization classes of \(K_8\) and the uniqueness of the perfect class are classical [2] and can also be replayed by the accompanying finite enumeration. The retained result is the small-case classification in the qualitative algebra setting: the perfectness criterion and the distinction between restrictions of the unique eight-point class that do and do not preserve the qualitative witnesses. The extension theorem alone does not assert that a restriction to seven vertices is qualitative. The argument concerns only order eight and equivalence allowing colour relabelling; it does not claim a perfectness criterion at larger orders or a census with atom names fixed.

## References

1. B. Al-Juaid, M. Jackson, J. Koussas, T. Kowalski, “Edge colourings and qualitative representations of chromatic algebras”, *Journal of Algebraic Combinatorics* 58 (2023), 157–182, DOI: 10.1007/s10801-023-01251-5, arXiv:2201.03098.
2. E. Seah, D. R. Stinson, “On the Enumeration of One-Factorizations of Complete Graphs Containing Prescribed Automorphism Groups”, *Mathematics of Computation* 50 (1988), 607–618, DOI: 10.1090/S0025-5718-1988-0929557-1.
