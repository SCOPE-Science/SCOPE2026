# Matroidal cycle convexity on cactus graphs

## Finding

Let \(G\) be any finite connected simple **cactus graph**: every edge lies in at most one simple cycle. Write \(V=V(G)\), let \(n=|V|\), and let \(\mathcal C\) be the family of vertex sets of its distinct simple cycles, with \(c=|\mathcal C|\). In cycle convexity, a vertex outside a set is generated when it is the sole omitted vertex of some simple cycle; iterating this rule defines the hull \(\operatorname{Hull}_{cc}\).

Let \(\mathbf e_v\) denote the standard basis of \(\mathbb F_2^V\), and form the subspace
\[
W_G=\operatorname{span}_{\mathbb F_2}\left\{\sum_{v\in C}\mathbf e_v:C\in\mathcal C\right\}.
\]
For every \(S\subseteq V\), there is the exact closure identity
\[
\boxed{\operatorname{Hull}_{cc}(S)=\{v\in V:\mathbf e_v+W_G\in\operatorname{span}_{\mathbb F_2}\{\mathbf e_s+W_G:s\in S\}\}.}
\]
Thus cycle convexity on a cactus is the closure operator of a **loopless binary-representable matroid** on the vertex set. Its rank is \(n-c\); consequently the cycle-convex Helly number, Radon number and rank, defined below as maximum sizes of their respective independent sets, are all
\[
\boxed{\operatorname{hel}_{cc}(G)=\operatorname{rad}_{cc}(G)=\operatorname{rk}_{cc}(G)=n-c.}
\]
In particular, every inclusion-maximal convexly independent vertex set has exactly \(n-c\) members (the basis property), and these sets obey the matroid basis-exchange axiom. This identifies the three parameters for cacti with arbitrarily many cycles, not only the previously characterized forest, unicyclic and bicyclic cases.

The cactus assumption is substantive: the four-vertex diamond (two triangles sharing an edge) already fails the matroid exchange axiom for cycle-convex closure.

## Assumptions and scope

All graphs are finite, simple, undirected and connected, including the single-vertex graph. A cactus is characterized equivalently by a block decomposition into bridge edges and chordless cycle blocks. Its incidence graph between cycle blocks and their vertices, restricted to vertices belonging to cycles, is a forest. Different cycle blocks have at most one common vertex; an alternating cycle in this incidence graph would create a distinct simple graph cycle, contradicting the cactus assumption.

For any \(S\subseteq V\), set
\[
I_{cc}(S)=S\cup\{v\in V\setminus S:\exists C\in\mathcal C\text{ with }C\setminus S=\{v\}\}.
\]
The finite fixed point of repeatedly applying \(I_{cc}\) is \(\operatorname{Hull}_{cc}(S)\). A set \(S\) is convexly independent if \(v\notin\operatorname{Hull}_{cc}(S\setminus\{v\})\) for each \(v\in S\). It is Helly-independent if \(\bigcap_{v\in S}\operatorname{Hull}_{cc}(S\setminus\{v\})=\varnothing\), and Radon-independent if no partition of \(S\) into two disjoint nonempty subsets has intersecting hulls. The three invariants are the maximum sizes of these sets. Under the usual empty-intersection convention the empty set is not Helly-independent (although it is convexly and Radon-independent); this has no effect on the maximum sizes. For the one-vertex graph all three invariants equal one.

The quotient notation \(\mathbf e_v+W_G\) is an element of \(\mathbb F_2^V/W_G\). No claim is made for general noncactus graphs.

## Proof

**1. Cycle relations are independent and contain no unit vector.** Associate to each \(C\in\mathcal C\) its characteristic vector \(\mathbf 1_C=\sum_{v\in C}\mathbf e_v\). Consider any nonempty subset \(\mathcal J\subseteq\mathcal C\). In the bipartite incidence forest of the selected cycles and their vertices, pick a cycle node that is a leaf after suppressing vertices incident with only one selected cycle. Such a leaf cycle has at least \(|C|-1\ge2\) vertices that belong to no other cycle of \(\mathcal J\). These coordinates are all one in \(\sum_{C\in\mathcal J}\mathbf 1_C\). Hence every nonempty sum of distinct cycle relations is nonzero and has Hamming weight at least two. Therefore \(\dim W_G=c\), and no standard basis vector \(\mathbf e_v\) lies in \(W_G\). The quotient representation is loopless and has dimension \(n-c\).

**2. Every cycle-convex hull lies in the represented matroid closure.** In the quotient, \(\sum_{v\in C}(\mathbf e_v+W_G)=0\) for each cycle \(C\). Therefore, if all but one vertex of a cycle lie in the linear span of selected quotient vectors, the remaining vertex does too. Starting from \(S\), every step of the cycle-convex closure stays inside the represented matroid closure. This gives one inclusion.

**3. Every cycle-closed set is a matroid flat.** Let \(T\subseteq V\) satisfy \(I_{cc}(T)=T\). Suppose that \(v\notin T\) but \(\mathbf e_v+W_G\) is spanned by the quotient vectors of \(T\). Over \(\mathbb F_2\), this means that for some nonempty subset \(\mathcal J\subseteq\mathcal C\), the symmetric-difference vector
\[
r=\sum_{C\in\mathcal J}\mathbf1_C
\]
has exactly one nonzero coordinate outside \(T\), namely \(v\). In the cycle–vertex incidence forest of \(\mathcal J\), discard every connected component not containing \(v\). This discards only coordinates inside \(T\), so the unique outside coordinate remains \(v\).

Root the remaining incidence tree at vertex \(v\). If there is a selected cycle node at distance greater than one from \(v\), choose one farthest from \(v\). It is a leaf among selected cycle nodes: all of its vertices except its possible parent articulation vertex \(a\) occur in exactly one selected cycle. Since they are not \(v\), they all lie in \(T\). If \(a\notin T\), then this cycle has exactly one vertex outside \(T\), contradicting \(I_{cc}(T)=T\). Thus the entire leaf cycle lies inside \(T\). Remove its characteristic vector from the sum: only coordinates inside \(T\) change, and the unique outside coordinate remains \(v\). Repeating this pruning eventually leaves only selected cycles adjacent to \(v\).

At least one cycle remains, since the sum still has a nonzero coordinate \(v\). Every other vertex of each remaining cycle occurs in exactly one selected cycle and is therefore in \(T\). Hence such a cycle has \(v\) as its sole omitted vertex, contradicting cycle-closedness. This contradiction shows that every cycle-closed \(T\) is a flat of the quotient representation.

Apply this to \(T=\operatorname{Hull}_{cc}(S)\), which is cycle-closed. The represented matroid closure of \(S\) is contained in every represented flat containing \(S\), hence in \(T\). Together with Step 2 this proves the boxed closure identity for **every** subset \(S\subseteq V\).

**4. The three independence notions coincide for nonempty sets.** The proven closure is linear-span closure of a loopless vector matroid. Its convexly independent sets are exactly the linearly independent sets. If \(S\) is linearly independent, the spans of \(S\setminus\{v\}\), as \(v\) runs through \(S\), have intersection equal to the zero subspace; no represented vertex is zero. Thus \(S\) is Helly-independent. Likewise, any two disjoint subsets of a linearly independent \(S\) span subspaces intersecting only at zero, making \(S\) Radon-independent. Conversely, if \(v\in\operatorname{Hull}_{cc}(S\setminus\{v\})\), then \(v\) belongs to all the one-point-deletion hulls (so \(S\) is Helly-dependent), and the partition \(\{v\},S\setminus\{v\}\) has intersecting hulls (so \(S\) is Radon-dependent). Therefore the three nonempty independence families coincide, and their maximum size is the matroid rank \(n-c\). Matroid basis exchange and the common cardinality of all maximal independent sets follow.

**5. A sharp noncactus boundary.** Let the diamond have edge set \(\{01,02,12,03,13\}\), where \(01\) is the shared edge. Put \(S=\{2\}\), \(x=0\), and \(y=3\). Starting from \(S\cup\{0\}=\{0,2\}\), the triangle on \(0,1,2\) generates \(1\), after which the triangle on \(0,1,3\) generates \(3\). But \(\operatorname{Hull}_{cc}(\{2,3\})=\{2,3\}\), so \(0\) is not generated in the reverse direction. This violates the Steinitz exchange axiom, a necessary property of matroid closure. Thus the theorem does not extend unchanged even to the smallest overlapping-cycle example.

## Verification

The accompanying standard-library Python program `verify.py` implements two independent closure calculations: iterative generation from every simple cycle and the binary quotient test through the full span of the corresponding cycle-characteristic vectors. It exhaustively checks every **labelled connected cactus graph** on at most six vertices, using all its vertex subsets and directly enumerating the three independence maxima. Counts by order \(1,2,3,4,5,6\) are \(1,1,4,31,362,5676\). It also checks 200 generated 15-vertex cacti, comparing 64 sampled subsets per graph, and exhibits the diamond exchange failure. The recorded output is in `verify_output.txt`. These computations corroborate, but do not replace, the proof for arbitrary graph orders.

## Relationship to prior work

Araújo et al. (2020, arXiv:2012.05656) introduced the cycle-interval operator. Nair et al. (2026, arXiv:2609.34236, first submitted 28 September 2026) studied the cycle-convex Helly, Radon and rank parameters and characterized the maximum values \(n-1\) and \(n-2\), including the unicyclic and bicyclic cases. The present claim extends the parameter identity to arbitrarily many cactus cycles and explains it by an explicit matroid representation and exchange property; the first two nontrivial cycle counts are compatible with those prior results. Aráujo et al. (2026, DOI:10.1007/978-3-032-27732-9_6) gave rank algorithms for several graph classes, including chordal graphs, but the available preview does not supply this all-cactus representation or the three-parameter result.

## Limitations

The theorem is restricted to cactus graphs; cycles sharing an edge can break matroid exchange. Its contribution is an exact structural representation and invariant classification, not a general complexity bound and not a solution of the proposed Helly–Radon coincidence question for arbitrary graphs. Although the closest accessible primary sources were inspected, an equivalent result in less accessible technical material cannot be excluded. In particular, the full technical report corresponding to the earlier rank paper was unavailable for a complete text comparison. No independent audit has been performed.

## References

1. J. Araújo, V. Campos, D. Girão, J. Nogueira, A. Salgueiro, A. Silva. *Cycle convexity and the tunnel number of links*. arXiv:2012.05656 (first submitted 10 December 2020). https://arxiv.org/abs/2012.05656
2. R. S. Nair, B. S. Anand, U. Chandran S. V., J. R. Nascimento, A. Anil. *Computing the Helly Number, Radon Number and Rank in Cycle Convexity*. arXiv:2609.34236 (first submitted 28 September 2026). https://arxiv.org/html/2609.34236
3. J. Aráujo, S. N. Aráujo, P. P. Medeiros, N. Nisse, C. Silva. *On the Rank and the General Position Number in Cycle Convexity*. IWOCA 2026, pp. 73–87. DOI:10.1007/978-3-032-27732-9_6. https://link.springer.com/chapter/10.1007/978-3-032-27732-9_6
