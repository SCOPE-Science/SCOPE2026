# Minimum 2-rainbow dominating functions of crown graphs
## Finding
For every integer \(n\ge3\), let
\[
\operatorname{Cr}_n=K_{n,n}-\{a_i b_i:1\le i\le n\},
\]
with bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\). A 2-rainbow dominating function is a map
\[
f:V(\operatorname{Cr}_n)\longrightarrow\{\varnothing,\{1\},\{2\},\{1,2\}\}
\]
such that every vertex receiving \(\varnothing\) sees both colors in the union of the labels on its neighbors. Its weight is \(w(f)=\sum_v |f(v)|\).

Then
\[
\gamma_{r2}(\operatorname{Cr}_n)=4.
\]
For every \(n\ge5\), the minimum functions are exactly the following two families.

1. **Matched double-color family.** Choose one index \(i\). Assign \(\{1,2\}\) to both \(a_i\) and \(b_i\), and assign \(\varnothing\) elsewhere. This gives \(n\) functions.
2. **Aligned two-index singleton family.** Choose \(S=\{i,j\}\subseteq[n]\). On the two vertices of \(A\) indexed by \(S\), use the labels \(\{1\}\) and \(\{2\}\) once each; independently do the same on the two vertices of \(B\) indexed by the same set \(S\); assign \(\varnothing\) elsewhere. This gives \(4\binom n2\) functions.

Consequently, for \(n\ge5\), the exact number of minimum functions is
\[
n+4\binom n2=2n^2-n.
\]
For \(n=4\), the two core families contribute \(28\) functions, and there are twelve additional functions: one bipartition class is entirely empty while the other class has four singleton labels, two \(\{1\}\) and two \(\{2\}\). Thus the number of minimum functions is \(40\).

For \(n=3\), the two core families contribute \(15\) functions. There are twelve additional side-weight \((0,4)\) or \((4,0)\) functions, where the nonempty side is a permutation of \(\{1\},\{2\},\{1,2\}\), and twenty-four additional side-weight \((1,3)\) or \((3,1)\) functions. In the latter family, the light side has one singleton at an index \(i\), the heavy side has three singleton labels, and its unique occurrence of one color is at index \(i\). Hence the number of minimum functions is \(51\).

By the standard weight-preserving rainbow/prism correspondence, the same classification counts minimum dominating sets of \(\operatorname{Cr}_n\square K_2\). In particular, for \(n\ge5\),
\[
\gamma(\operatorname{Cr}_n\square K_2)=4
\]
and the prism has exactly \(2n^2-n\) minimum dominating sets.

## Assumptions and scope
Graphs are finite, simple, and undirected. The statement concerns the ordinary 2-rainbow domination parameter with color set \(\{1,2\}\), not total, independent, restrained, or Roman variants. The deleted perfect matching is fixed only to name corresponding indices; all perfect matchings of \(K_{n,n}\) are equivalent under graph automorphisms.

The classification is an all-\(n\) symbolic theorem. The included computation checks finite instances only and is not used to infer the infinite statement.

## Proof
For each side and each color, define the color-support index sets
\[
A_c=\{i:c\in f(a_i)\},\qquad B_c=\{i:c\in f(b_i)\},\qquad c\in\{1,2\}.
\]
Because \(a_i\) is adjacent to every vertex of \(B\) except \(b_i\), an empty \(a_i\) is valid exactly when
\[
B_1\setminus\{i\}\ne\varnothing
\quad\text{and}\quad
B_2\setminus\{i\}\ne\varnothing.
\]
Similarly, an empty \(b_i\) is valid exactly when
\[
A_1\setminus\{i\}\ne\varnothing
\quad\text{and}\quad
A_2\setminus\{i\}\ne\varnothing.
\]
These two conditions are the complete feasibility criterion.

We first prove the lower bound. Suppose \(w(f)\le3\). If one side has weight zero, then every vertex on the opposite side must be nonempty; otherwise an empty vertex would see no color. Since \(n\ge3\), weight at most three forces \(n=3\) and gives exactly one unit of weight per vertex on that opposite side. But then deleting any one corresponding neighbor cannot leave both colors for every empty vertex on the zero-weight side: each color would have to occur at least twice, requiring at least four color occurrences. Thus neither side can have weight zero.

If both sides have positive weight and the total weight is at most three, one side has weight one. A side of weight one carries only one color occurrence, so every vertex on the opposite side must be nonempty. That requires weight at least \(n\ge3\) on the opposite side, making the total weight at least four. Therefore no 2-rainbow dominating function has weight below four.

Conversely, choose any index \(i\) and assign \(\{1,2\}\) to \(a_i\) and \(b_i\), with all other labels empty. Every empty vertex sees the double-colored vertex in the opposite class because its index differs from \(i\). Hence \(\gamma_{r2}(\operatorname{Cr}_n)=4\).

Now classify weight-four functions. For \(n\ge5\), each side contains an empty vertex because four units of total weight cannot make all \(n\) vertices on either side nonempty. Therefore each side must itself contain both colors: otherwise an empty vertex on the opposite side misses a color. Hence both side weights are at least two, and since they sum to four they are exactly two.

A side of weight two containing both colors has only two possible forms: a single vertex labeled \(\{1,2\}\), or two distinct vertices labeled \(\{1\}\) and \(\{2\}\). In the first form, both colors have the same unique support index. The feasibility criterion forces that index to be nonempty on the opposite side. In the second form, each color has a different unique support index, and the criterion forces both of those indices to be nonempty on the opposite side.

If both sides use one \(\{1,2\}\)-vertex, their unique indices must therefore coincide, giving the matched double-color family. If one side uses a double label and the other uses two singleton labels, the two distinct unique-color indices on the singleton side would both have to lie in the one-point support of the double-label side, which is impossible. If both sides use two singleton labels, each two-point support must contain the other, so the two support sets are equal. The color assignments on the common two-set are independent across the two sides, giving four functions per two-set. This proves the classification for \(n\ge5\).

For \(n=4\), the same argument handles all functions whose two side weights are \((2,2)\). A side-weight split \((1,3)\) or \((3,1)\) is impossible because the weight-one side cannot supply both colors to any empty vertex, while weight three cannot make all four vertices on the opposite side nonempty. If one side has weight zero, the other side must have all four vertices nonempty; weight four then makes every label a singleton. Deleting any one neighbor must still leave both colors, so each color must occur at least twice; hence exactly twice. There are \(\binom42=6\) such labelings for each choice of the zero side, adding twelve.

For \(n=3\), the \((2,2)\) analysis is unchanged. In a \((0,4)\) split, the nonzero side must have all three vertices nonempty, so its weights are \((2,1,1)\). The double-labeled vertex supplies both colors whenever it remains, and deleting it must leave both colors, forcing the two singleton labels to be different. Thus that side is a permutation of \(\{1\},\{2\},\{1,2\}\), giving six functions for each orientation. In a \((1,3)\) split, the weight-three side must have all three vertices nonempty, hence all three labels are singletons. Let \(i\) be the support index of the weight-one side. The two empty vertices on that light side correspond to the other two indices, so deleting either of those heavy-side vertices must leave both colors. Therefore the color that occurs only once on the heavy side must occur at index \(i\); conversely this condition is sufficient. There are three choices of \(i\), two choices for the unique heavy-side color, two choices for the light-side singleton color, and two orientations, giving \(24\) functions. Together with the \(15\) core functions and the \(12\) zero-side functions, this gives \(51\).

Finally, the classical correspondence sends a 2-rainbow function \(f\) on \(G\) to the dominating set
\[
D_f=\{(v,c):c\in f(v)\}\subseteq V(G\square K_2),
\]
preserving weight as cardinality. Thus the minimum-function classification is equivalently a classification of minimum dominating sets of the prism.

## Verification
The standalone checker evaluates the literal neighborhood definition and the support-set criterion independently for all labelings of weight at most four for \(3\le n\le12\). It also checks the claimed minimum-family classifier and exact minimum counts. For the exceptional cases \(n=3\) and \(n=4\), it additionally exhausts every possible labeling, not merely low-weight labelings.

Observed output:

`VERIFY_OK n_range=3..12 low_weight_labelings=619907 criterion_checks=619907 minimum_class_checks=1263 count_checks=10 full_small_checks=69632 max_order=24`

The computation is only finite regression evidence. The all-\(n\) conclusion rests on the proof above.

## Relationship to prior work
Brešar, Henning, and Rall introduced rainbow domination in the context of Cartesian products, and their later full treatment gives the weight-preserving correspondence between \(k\)-rainbow domination on \(G\) and ordinary domination on \(G\square K_k\). Their full text records classification 05C69 and develops general bounds and tree algorithms; it does not give a crown-graph theorem. Brešar and Kraner Šumenjak developed 2-rainbow domination further, and Chellali, Haynes, and Hedetniemi established general relations with weak Roman and total domination.

The closest published comparison found is an exact all-function theorem for complete multipartite graphs. It includes \(K_{n,n}\) but does not include \(K_{n,n}-M_n\) for \(n\ge3\). The deleted matching makes feasibility depend on whether a unique color occurs at the same index as an empty vertex, an index-sensitive obstruction absent from complete multipartite graphs. The retained claim is therefore the crown-specific minimum classification and count, not the already known definition, prism correspondence, or complete-multipartite formula.

Searches also covered the aliases “complete bipartite graph minus a perfect matching,” “bipartite Kneser \(H(n,1)\),” “bipartite double cover of \(K_n\),” and “tensor product \(K_n\times K_2\).” No covering theorem was located in the inspected literature or research database. This is evidence for originality, not a proof that no poorly indexed equivalent statement exists.

## Limitations
The theorem classifies minimum functions only; it does not give the full weight enumerator of all 2-rainbow dominating functions on crown graphs. The finite checker extends only through \(n=12\) for low-weight states and through \(n=4\) for exhaustive full-state enumeration. Literature searches cannot rule out an equivalent result hidden under an uncommon alias or in inaccessible older material.

The earliest verified public source date used for the parameter is 2005-10-15, for the paper introducing rainbow domination in the Cartesian-product setting. No earlier publicly dated preprint was located in the inspected sources.

## References
1. B. Brešar, M. A. Henning, and D. F. Rall, “Paired-domination of Cartesian products of graphs and rainbow domination,” *Electronic Notes in Discrete Mathematics* 22 (2005), 233–237. DOI: 10.1016/j.endm.2005.06.059.
2. B. Brešar and T. Kraner Šumenjak, “On the 2-rainbow domination in graphs,” *Discrete Applied Mathematics* 155 (2007), 2394–2400. DOI: 10.1016/j.dam.2007.07.018.
3. B. Brešar, M. A. Henning, and D. F. Rall, “Rainbow domination in graphs,” *Taiwanese Journal of Mathematics* 12 (2008), 213–225. DOI: 10.11650/twjm/1500602498.
4. M. Chellali, T. W. Haynes, and S. T. Hedetniemi, “Bounds on weak Roman and 2-rainbow domination numbers,” *Discrete Applied Mathematics* 178 (2014), 27–32. DOI: 10.1016/j.dam.2014.06.016.
