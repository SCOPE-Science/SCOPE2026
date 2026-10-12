# Strong-odd color-count spectrum of friendship graphs
## Finding
For the friendship graph \(F_k\) formed from \(k\ge2\) triangles sharing one center, define \(\Sigma_{\mathrm{so}}(F_k)\) to be the set of numbers of colors that occur in strong odd colorings. Then
\[
\Sigma_{\mathrm{so}}(F_k)=
\begin{cases}
\{3,5,7,\ldots,2k+1\},&k\text{ odd},\\
\{5,7,9,\ldots,2k+1\},&k\text{ even}.
\end{cases}
\]
In particular,
\[
\chi_{\mathrm{so}}(F_k)=
\begin{cases}3,&k\text{ odd},\\5,&k\text{ even}.\end{cases}
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. A strong odd coloring is a proper vertex coloring in which, for every vertex, every color appearing in its open neighborhood occurs there an odd number of times. The friendship graph \(F_k\) has center \(c\) and outer pairs \(\{a_i,b_i\}\) for \(1\le i\le k\), with each \(c a_i b_i c\) a triangle and no other edges. The theorem is stated for \(k\ge2\); the trivial endpoint \(F_1=K_3\) has the same odd-\(k\) minimum but is not part of the new family claim.

## Proof
Because \(c\) is adjacent to every outer vertex, properness forces its color to be absent from all \(2k\) outer vertices. Each pair \(a_i,b_i\) is adjacent, so its two colors are distinct. For an outer vertex, say \(a_i\), the open neighborhood is exactly \(\{c,b_i\}\), whose two vertices have distinct colors; each therefore occurs once. Thus every outer vertex automatically satisfies the strong odd condition in every proper coloring.

The only remaining condition is at \(c\). Its neighborhood is the set of all \(2k\) outer vertices, so a proper coloring is strong odd exactly when every color used on those outer vertices occurs an odd number of times. Let \(q\) be the number of outer colors. Since \(2k\) is a sum of \(q\) positive odd integers, \(q\) is even and \(2\le q\le2k\). Also, a single outer color can occur at most once on each of the \(k\) outer edges, so every outer color class has size at most \(k\).

If \(q=2\), both positive odd class sizes sum to \(2k\) and are at most \(k\); hence both must equal \(k\). This is possible exactly when \(k\) is odd. Therefore a three-color strong odd coloring exists exactly for odd \(k\).

Now fix any even \(q\) with \(4\le q\le2k\). We construct positive odd integers \(d_1,\ldots,d_q\le k\) with sum \(2k\). Write \(d_i=1+2x_i\). It is enough to choose nonnegative integers \(x_i\) with
\[
\sum_i x_i=k-q/2
\]
and \(x_i\le\lfloor(k-1)/2\rfloor\). Such a choice always exists: the required sum is at most \(k-2\), while the total available capacity of the \(q\ge4\) coordinates is at least \(4\lfloor(k-1)/2\rfloor\ge k-2\); fill coordinates greedily up to their capacities.

Consider the complete multipartite graph \(K_{d_1,\ldots,d_q}\). It has \(2k\) vertices and largest part at most \(k\), so it has a perfect matching. This is the standard complete-multipartite perfect-matching criterion: an even-order complete multipartite graph has a perfect matching exactly when no part contains more than half of all vertices. Use the \(k\) matched pairs as the \(k\) outer edges of \(F_k\), and color each matched vertex by its multipartite part. Matched endpoints have distinct colors and color \(i\) occurs exactly \(d_i\), which is odd. Giving the center a fresh color therefore produces a strong odd coloring with \(q+1\) colors.

Thus every even \(q\in\{4,6,\ldots,2k\}\) occurs, and \(q=2\) occurs exactly when \(k\) is odd. Adding the center color gives precisely the asserted spectra and minima.

## Verification
The standalone verifier independently enumerates canonical set partitions of the \(2k\) outer vertices for \(2\le k\le5\). It filters only by the defining properness constraint on each outer edge and by odd cardinality of every used outer color class, then compares the realized color counts with the theorem. It does not use the constructive proof or the multipartite matching criterion. Its replay output is stored in `verification_output.txt`.

The finite enumeration is corroborative only. The theorem for every \(k\ge2\) follows from the structural reduction and the perfect-matching construction above.

## Relationship to prior work
Manattu, Vinay, and Lakshmanan study the same strong odd coloring invariant, give exact results for joins of cycles with empty graphs, and use one-point unions of specially constructed graphs in their planar examples. Their full text introduces general one-point-union notation but does not state a friendship-graph or windmill theorem; full-text searches for those names returned no occurrence. Their arXiv record lists MSC \(05C15\) first, followed by \(05C10\) and \(05C76\), and the first version was public on 2026-02-03.

Pradhan, Sharma, and Verma prove in 2026 that an optimal strong odd coloring can be computed in linear time for every block graph. Friendship graphs are block graphs, so that algorithm is broader coverage for the minimum-value computation in principle. It does not classify all feasible numbers of colors. The new content here is the exact color-count spectrum and its parity mechanism; the displayed minimum follows as a corollary of that stronger structural classification.

Targeted semantic-index searches using friendship, windmill, strong odd coloring, color-count spectrum, feasible color counts, and center-neighborhood odd multiplicities found no statement giving this spectrum. The closest friendship/windmill hit concerned the general-position polynomial, a different invariant, while the closest strong-odd hits concerned other graph classes.

## Limitations
The theorem is specific to friendship graphs. It does not classify generalized windmills with larger clique blocks or arbitrary block graphs. The 2026 block-graph algorithm already supplies a general computational route to the minimum strong odd chromatic number; originality here therefore rests on the closed spectrum and structural characterization, not on mere computability of the minimum. Very recent or poorly indexed concurrent work remains a residual bibliographic risk.

## References
1. Arun J. Manattu, Athira Vinay, Aparna Lakshmanan S, “On a conjecture about the strong odd chromatic number of planar graphs,” arXiv:2602.03259v1, first public 2026-02-03.
2. Dinabandhu Pradhan, Vaishali Sharma, Shaily Verma, “On the Classical and Parameterized Complexity of Strong Odd Coloring,” arXiv:2610.01441v1, first public 2026-10-01.
