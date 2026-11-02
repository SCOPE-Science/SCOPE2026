# The first static–adaptive shattering gap for Boolean Hamming radius-two balls

## Finding

Let \(X_d=\{0,1\}^d\), with Hamming distance \(d_H\). Let \(\mathcal B_d\) be the binary concept class whose concepts are the closed radius-two balls \(B_2(c)=\{x\in X_d:d_H(x,c)\le 2\}\), indexed by centers \(c\in X_d\). Queries are membership questions at arbitrary points \(x\in X_d\). The exact VC and Littlestone dimensions are

\[
(\operatorname{VCdim}(\mathcal B_d),\operatorname{Ldim}(\mathcal B_d))=
\begin{cases}
(0,0)&d=1,2,\\
(1,1)&d=3,\\
(3,3)&d=4,\\
(4,4)&d=5,\\
(4,5)&d\ge6.
\end{cases}
\]

In particular, six is the first ambient dimension with a strict static–adaptive separation. Both dimensions stabilize thereafter, despite the exponentially increasing set of possible centers.

## Assumptions and scope

All spaces and hypotheses are finite. The ambient alphabet is binary; the radius is the **closed metric radius** two, so responses are positive at distances zero, one and two. A static set of queries is shattered when all Boolean traces occur. A complete online tree of depth \(k\) has one point query at each internal node and a different hypothesis consistent with every root-to-leaf response sequence; the Littlestone dimension is the largest such depth. Theorems are for every integer \(d\ge1\), with no probabilistic assumptions.

The radius-two *shell* relation (distance exactly two) is a different concept class and is not used in the statements or certificates here.

## Proof

### 1. Universal VC upper bound four

Suppose five distinct queries \(q_1,\ldots,q_5\) are shattered. An all-positive labeling has a witnessing center \(c\). Translating by bitwise exclusive-or with \(c\), assume \(c=0\). Every \(q_i\) then has weight at most two. Coordinates outside the union of the five query supports are interchangeable. Each occupied coordinate has a nonzero incidence column \(p\in\{1,\ldots,31\}\), recording which queries contain it. Writing \(n_p\) for its multiplicity, the exhaustive list of coordinate-isomorphism types is specified by

\[
n_p\in\mathbb Z_{\ge0},\qquad
\sum_{p:\,p_i=1}n_p\le2\quad(i=1,\ldots,5),
\]

with the five query words pairwise distinct. There are exactly 7,260 such normal forms. This is a finite enumeration of all possible five-query supports in *any* ambient dimension, not a restriction to five- or six-dimensional cubes.

If a center \(z\) makes at least one response positive, then for some \(i\), \(d_H(z,q_i)\le2\), and hence \(|z|\le4\). In particular, at most two nonzero coordinates of \(z\) can be outside the union of the query supports. Therefore every nonzero five-bit trace is obtained by enumerating a subset of occupied coordinates and an outside weight in \(\{0,1,2\}\), keeping total center weight at most four. The bundled independent Python and C++17 exhaustive verifiers each examine every normal form and find at most **26 of the 31 possible nonzero traces**. A shattered five-query set would require all 31 nonzero traces, a contradiction. Thus \(\operatorname{VCdim}(\mathcal B_d)\le4\) for all \(d\).

### 2. Universal Littlestone upper bound five

By translation invariance, the positive branch after any first query is equivalent to restricting the centers to

\[
F_d=\{\varnothing\}\cup\{\{i\}:i\in[d]\}\cup\{\{i,j\}:1\le i<j\le d\}.
\]

Here query \(S\subseteq[d]\) tests \(|C\triangle S|\le2\), and centers \(C\) belong to \(F_d\). We prove \(\operatorname{Ldim}(F_d)\le4\). Queries of weight zero or at least five have constant responses. Queries of weight three or four have at most six positive centers (three singleton centers and three pair centers in the weight-three case; six pair centers in the weight-four case), hence positive-branch Littlestone dimension at most two by hypothesis counting.

For weight-one and weight-two queries, coordinate symmetry reduces the positive branches respectively to

\[
H_1=\{\varnothing\}\cup\{\{i\}:i\in[d]\}\cup\{\{1,j\}:j\ne1\},
\]

\[
H_2=\{\varnothing,\{1\},\{2\}\}\cup\{\{i,j\}:\{i,j\}\cap\{1,2\}\ne\varnothing\}.
\]

We show both have Littlestone dimension at most three. Ignoring constant-response queries, every query not listed below has at most five positive centers; the positive branch then has dimension at most two. This follows by counting intersections: at query weight two with neither distinguished coordinate, the positive-center counts are five in either family; for query weights three or four the count is at most five, and query weights at least five have no positive centers. A weight-one query away from the distinguished coordinates also has at most five positive centers. For \(H_1\), the only exceptional nonconstant queries are \(\{j\}\) with \(j\ne1\), whose negative branch is a subfamily of edges in a fixed star, and \(\{1,j\}\), whose negative branch consists solely of singleton centers. For \(H_2\), exceptional nonconstant queries are \(\{1\},\{2\},\{1,j\},\{2,j\}\) with \(j\notin\{1,2\}\); their negative branches consist of centers \(\{b\}\) and \(\{b,k\}\) for one fixed \(b\in\{1,2\}\) (possibly with the singleton omitted). The query \(\{1,2\}\) is constant positive; the query \(\{1\}\) is constant positive for \(H_1\). All the exceptional negative-branch types have Littlestone dimension at most two: in a singleton-only family, and likewise in a fixed-star family with an optional center singleton, any informative query has at most three positive centers. Their positive-branch dimensions are thus at most one. It follows that each possible query on \(H_1\) or \(H_2\) has at least one branch of Littlestone dimension at most two, so these families have dimension at most three.

Consequently every query on \(F_d\) has at least one branch with dimension at most three, proving \(\operatorname{Ldim}(F_d)\le4\). Every first query on \(\mathcal B_d\) has its positive branch isomorphic to \(F_d\), and therefore \(\operatorname{Ldim}(\mathcal B_d)\le5\) for every \(d\).

### 3. Exact lower bounds and small dimensions

For five coordinates, the four queries encoded by \([0,1,2,4]\) have the following sixteen center witnesses, ordered by the four-bit response string interpreted as a binary integer from zero through fifteen:

`[15,24,25,9,26,10,11,3,28,12,13,5,14,6,7,0]`.

The bundled verifier confirms each witness answers exactly the prescribed response pattern. Appending zero coordinates extends the same shattered set to every \(d\ge5\), proving the VC lower bound four.

For six coordinates, `certificate.json` contains a complete depth-five online tree with 31 internal point queries and 32 distinct terminal center witnesses, each checked against its entire root-to-leaf path. The certificate therefore proves \(\operatorname{Ldim}(\mathcal B_6)\ge5\); zero-padding all queries and centers extends it to every \(d\ge6\).

When \(d\le2\), every radius-two ball is the entire cube, so both dimensions vanish. In dimension three, the balls are complements of singletons; both dimensions are one. In dimension four, each positive root branch has 11 centers and each negative root branch only 5, making depth four impossible (a depth-three branch would require at least 8 centers). Three shattered queries exist, so both dimensions equal three. In dimension five, each positive root branch has 16 centers. Every informative query in this branch splits those centers as 10 versus 6, or 6 versus 10 (all other queries are constant), so the positive branch has dimension at most three, giving full-class dimension at most four. The four-query static witness above proves equality.

## Verification

Run `python3 verify.py` from the directory containing `verify.py` and `certificate.json`. It reconstructs all binary Hamming responses; verifies the static four-query witness, online depth-five tree, exact Littlestone dimensions for dimensions one to six by full version-space recurrence, and universal five-query obstruction over 7,260 incidence normal forms. Run `c++ -std=c++17 -O2 verify_normal_forms.cpp -o verify_normal_forms && ./verify_normal_forms` for an independently implemented exhaustive check of the normal forms. The two enumeration codes agree on 7,260 distinct normal forms and a maximum of 26 realized nonzero traces. The finite certificate uses no third-party library.

The general Littlestone bound rests on the symbolic case analysis in the proof; the verifier corroborates finite cases rather than substituting finite experiments for the universal proof.

## Relationship to prior work

Adler, Benediktsson and Macpherson analyze VC dimension for Johnson and Hamming graph neighborhoods, with the Hamming graph adjacency relation at distance one; that does not imply the closed radius-two ball classification here. Guingona, Kolesnikov, Nierwinski and Soucy establish general VC/Littlestone equality for certain zero-set families, not the metric-ball class here. Ghazi and collaborators provide general composition bounds, without exact values for this cube power. The related exact-distance-two *shell* family is explicitly different: including distances zero and one changes both the static and adaptive dimensions. A literature and research-index search did not locate an equivalent exact classification, although absence from retrieved sources is not a uniqueness proof.

## Limitations

The theorem concerns binary closed balls of radius exactly two, not nonbinary alphabets, varying radii or exact-distance spheres. The finite VC obstruction depends on correct exhaustive normal-form enumeration, for which two independent sources and reproduction commands are provided. No assertion of unconditional historical novelty, peer review or independent scientific validation is made. Possible older terminology includes closed neighborhoods of the square of a hypercube, or fixed-radius Hamming range spaces.

## References

- I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, originally public 2020-07-31, https://arxiv.org/abs/2007.16042.
- V. Guingona, A. Kolesnikov, J. Nierwinski and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805, 2021, https://arxiv.org/abs/2109.04805.
- B. Ghazi et al., *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, Proceedings of Machine Learning Research 132 (2021), https://proceedings.mlr.press/v132/ghazi21a.html.
