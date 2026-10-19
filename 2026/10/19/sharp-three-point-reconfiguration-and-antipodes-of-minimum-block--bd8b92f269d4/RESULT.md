# Sharp three-point reconfiguration and antipodes of minimum blocking sets in \(\operatorname{PG}(2,4)\)

## Finding

Let \(\Pi=\operatorname{PG}(2,4)\), with its \(21\) points and \(21\) lines. A **nontrivial blocking set** is a point set meeting every line but containing no entire line. The minimum size of such a set is \(7\). Form a reconfiguration graph \(\mathcal R_t\) on all minimum nontrivial blocking sets by joining two distinct sets when at most \(t\) points of the first can be replaced, at once, to obtain the second. All intermediary configurations are required to remain minimum nontrivial blocking sets; there is no requirement on intermediate states within a simultaneous replacement.

There are exactly \(360\) vertices. Each is the point set of a Baer subplane \(\operatorname{PG}(2,2)\). The graphs \(\mathcal R_1\) and \(\mathcal R_2\) have no edges. The first connected graph is \(\mathcal R_3\), with \(10080\) edges, degree \(56\), and radius and diameter both \(3\). For any two distinct minimum sets \(B,C\), its graph distance is

\[
 d_{\mathcal R_3}(B,C)=\begin{cases}
 1,&|B\cap C|=4,\\
 2,&|B\cap C|\in\{1,2,3\},\\
 3,&B\cap C=\varnothing.
 \end{cases}
\]

In particular, **the configurations at maximum distance are exactly the disjoint Baer subplanes**. The distance distribution from every vertex is \((1,56,287,16)\); there are \(2880\) unordered diametral pairs.

## Assumptions and scope

The ambient plane is the Desarguesian \(\operatorname{PG}(2,4)\), not an arbitrary projective plane or a larger extension field. Points are one-dimensional subspaces of \(\mathbb F_4^3\), where \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\). Lines are the kernels of nonzero linear functionals up to scalar multiples. Vertex labels are the actual ambient seven-point subsets; configurations are **not** identified under projective or semilinear symmetries. All claims are finite and exact. A \(t\)-exchange changes at most \(t\) of the seven chosen points, hence for distinct size-seven sets the relevant quantity is \(7-|B\cap C|\). We require the endpoints, not transient halfway states, to be nontrivial blocking sets.

## Proof

**Finite incidence lemma.** Represent each nonzero triple over \(\mathbb F_4\) by its unique normalization with first nonzero coordinate equal to one. There are exactly \((4^3-1)/(4-1)=21\) normalized points, and the same number of normalized nonzero linear functionals. Construct the \(21\) five-point lines by vanishing of their dot products. The first standalone verifier checks that all line sizes are five, each point lies on five lines, and any two distinct lines meet in exactly one point. These checks establish that this explicitly generated incidence system is \(\operatorname{PG}(2,4)\).

**Complete minimum-set enumeration.** Examine, in lexicographic order, every point subset of size \(0,1,\ldots,7\). Retain it if and only if its intersection with each generated line is nonempty and is not the entire line. No size below seven survives; exactly \(360\) size-seven subsets survive. For each surviving subset, all its line-intersection sizes are \(1\) or \(3\). Thus it is a seven-point copy of \(\operatorname{PG}(2,2)\): the seven three-secants each contain three points, every pair of points determines one of these lines, and each point lies on three such lines. It follows that the minimum nontrivial blocking sets are precisely the \(360\) Baer subplanes. The independently written second verifier generates these by completing all ordered-independent four-point projective quadrangles to seven-point Fano planes, removing duplicates. The resulting set of incidence masks coincides *exactly*, as checked by the shared ordered-mask SHA-256 digest.

**Intersection and exchange certificates.** For each of the \(\binom{360}{2}\) pairs, compute the bitwise intersection cardinality. The complete unordered intersection histogram is

\[
\begin{array}{c|rrrrr}
|B\cap C|&0&1&2&3&4\\\hline
\#\{\{B,C\}\}&2880&7560&30240&13860&10080.
\end{array}
\]

The displayed histogram is a known geometric fact; it is included to make the subsequent computation independently checkable, **not** as a novelty claim. Since every distinct pair intersects in at most four points, an exchange of fewer than three points is impossible. A three-point exchange is legal exactly when the pair intersects in four points, giving \(10080\) undirected edges and degree \(2(10080)/360=56\), with the degree verified vertex by vertex.

**Complete shortest-path certificate.** Construct the entire \(360\)-vertex adjacency list by the intersection-four test, then run ordinary breadth-first search from **each** of its \(360\) vertices. Both included, independently structured verifiers confirm that all vertices are reached from each source, that each search has distance layers \((1,56,287,16)\), and that the joint distribution of unordered pairs by (intersection size, shortest-path distance) is exactly

\[
 (0,3):2880,\quad(1,2):7560,\quad(2,2):30240,\quad
 (3,2):13860,\quad(4,1):10080.
\]

Because the two programs generate the plane and its subplanes by different finite constructions and independently build and traverse their own adjacency lists, these finite checks reconstruct both upper and lower distance bounds: each visited shortest-path layer is generated from the preceding layer, and every possible adjacency is tested. The joint histogram proves the displayed distance formula, sharp connectivity threshold, eccentricity three for each vertex and identification of all antipodal pairs. This uses **complete** enumeration of the specified finite objects, not sampled paths or an extrapolation to other projective planes.

## Verification

The included `verify_incidence.py` uses characteristic-two polynomial multiplication in \(\mathbb F_4\) and exhaustive combinations of \(21\) points. The independent `verify_quadrangles.py` uses an explicitly tabulated field and projective cross-product completion of quadrangles. Run each from any directory using Python 3.10 or newer, without installing packages or supplying external data. Their accompanying `verify_incidence_output.json` and `verify_quadrangles_output.json` record the exact expected output; the programs terminate with assertion failure on a discrepancy. They agree on the common sorted set of \(360\) incidence masks, identified by SHA-256 digest `e569b1b4979da37812f549b11900b52f0981e899e280688543b6626cca930d96`, as well as the graph's degree, distance layers and distance/intersection histogram.

## Relationship to prior work

The lower bound \(q+\sqrt q+1\) and the characterization of equality by Baer subplanes are classical, as summarized in work on blocking sets in finite planes and the small-plane classification of Coolsaet, Botteldoorn and Fack. The count of \(360\) Baer subplanes and the complete pairwise intersection histogram in \(\operatorname{PG}(2,4)\) also appear in earlier finite-geometry references, including the accessible monograph by Brouwer and Haemers; these are *not claimed to be new*. The 1984 projective-plane treatment of J. H. van Lint gives related constructions and incidence counts. De Beule, Héger, Szőnyi and Van de Voorde (2016-04-01) use Baer planes to construct blocking sets in larger finite planes, not this exact finite optimum-set exchange graph.

Gottschalk's *On the Geometry of Baer Subplanes in PG(2,4)* defines a graph on **one** projective-linear-group orbit of Baer subplanes, connecting planes with intersection of size **one**. The present graph uses all \(360\) subplanes and a size-**four** intersection rule. Its accessible abstract therefore does not imply the claimed all-vertex shortest-path characterization, although full-text overlap could not be completely ruled out. A later classification of minimal blocking sets documents the objects but does not, in the inspected material, give the complete three-point replacement metric.

## Limitations

Only this specific order-four plane and the exact simultaneous point-exchange rule are covered. There is no statement about replacements through nonoptimal intermediate configurations, optimal mixing or sampling, or all prime-power squares. The known intersection statistics alone do not automatically certify the all-pairs shortest paths; the full adjacency reconstruction and every-source breadth-first-search checks are necessary for the distance claim. The novelty review is limited by inaccessible full text of a geometrically relevant Gottschalk article and potential unindexed finite-geometry datasets. Publication priority and independent scientific verification have not been established.

## References

- J. De Beule, T. Héger, T. Szőnyi and G. Van de Voorde, *Blocking and Double Blocking Sets in Finite Planes*, Electronic Journal of Combinatorics **23** (2016), P2.5, publicly dated 2016-04-01, DOI:10.37236/5717.
- A. A. Bruen, *Blocking sets in finite projective planes*, SIAM Journal on Applied Mathematics **21** (1971), 380–392.
- J. H. van Lint, *On Ovals in PG(2,4) and the McLaughlin Graph*, in *Finite Geometries*, 1984, available in the freely accessible proceedings volume.
- A. E. Brouwer and W. H. Haemers, *Spectra of Graphs*, finite-geometries subsection on \(\operatorname{PG}(2,4)\), publicly available at https://homepages.cwi.nl/~aeb/math/srg/rk3/srgw.pdf.
- H. Gottschalk, *On the Geometry of Baer Subplanes in PG(2,4)*, European Journal of Combinatorics **21** (2000), 899–912, DOI:10.1006/eujc.1999.0391.
- K. Coolsaet, A. Botteldoorn, V. Fack, *Classification of minimal blocking sets in small Desarguesian projective planes*, Journal of Combinatorial Designs **30** (2022), 561–580, DOI:10.1002/jcd.21842.
- *Small maximal partial t-spreads in PG(2t+1,q)*, European Journal of Combinatorics, DOI:10.1016/j.ejc.2014.10.004 (publicly available online in 2015); its cited blocking-set theorem states the general classical sharp bound and equality characterization.
