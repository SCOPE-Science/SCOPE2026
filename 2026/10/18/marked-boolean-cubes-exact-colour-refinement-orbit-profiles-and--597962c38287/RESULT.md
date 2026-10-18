# Marked Boolean cubes: exact colour-refinement orbit profiles and landmark threshold

## Finding

Let \(Q_d\), for every integer \(d\ge1\), be the simple undirected graph on binary \(d\)-tuples with adjacency given by one-coordinate changes. Take an arbitrary nonempty collection of \(r\ge1\) *distinct* marked vertices \(s_0,\ldots,s_{r-1}\), each carrying a unique unary colour. All unmarked vertices share one further colour. For each coordinate \(i\in[d]\), put
\[
t_i=(s_{1i}\oplus s_{0i},\ldots,s_{r-1,i}\oplus s_{0i})\in\{0,1\}^{r-1},\qquad m_t=|\{i:t_i=t\}|.
\]
For any vertex \(x\) and any occurring signature \(t\), put
\[
a_t(x)=|\{i:t_i=t,\ x_i\oplus s_{0i}=1\}|.
\]

**Theorem.** After at most \(d+1\) ordinary one-dimensional Weisfeiler--Leman refinement rounds, the colour classes are exactly the pointwise-mark-stabilizer orbits. Two vertices receive the same stable colour precisely when their complete vectors \((a_t(x))_t\) agree. The number and sizes of these classes are, respectively,
\[
\prod_{t:m_t>0}(m_t+1),\qquad
\#\{x:(a_t(x))_t=(a_t)_t\}=\prod_{t:m_t>0}\binom{m_t}{a_t}.
\]
In particular, the stable colouring is discrete if and only if the coordinate signatures are pairwise distinct. The least possible number of individually coloured vertices making refinement discrete equals
\[
\boxed{1+\lceil\log_2 d\rceil}\qquad(d\ge1).
\]

## Assumptions and scope

All graphs are finite, simple, undirected and unlooped. A refinement round replaces a vertex colour by an injective encoding of its previous colour and the multiset of colours of its neighbours. The initial marked colours are mutually distinct, and are also distinct from the common unmarked colour. The result concerns the **internal stable refinement partition** and its orbits. A colour-refinement *discrete* outcome also identifies the resulting coloured graph among arbitrary finite coloured graphs; the theorem does not say that unmarked hypercubes are identified by colour refinement. Binomial factors for coordinates of multiplicity zero are omitted. The mark set is nonempty, but otherwise unrestricted, including arbitrary positions and all possible cardinalities.

## Proof

**1. Pointwise stabilizers.** Coordinatewise XOR translation takes \(s_0\) to the zero vertex and preserves both adjacency and individuality. After translation, every automorphism fixing zero induces a permutation of its \(d\) neighbours, the unit vectors. This permutation uniquely determines the automorphism: vertices of Hamming weight \(k\) are determined inductively by their neighbours of weight \(k-1\) (for \(k=1\) this is immediate, and for \(k\ge2\) these neighbours jointly determine the support). Conversely, every coordinate permutation is an automorphism. Such a permutation fixes each translated marked vertex precisely when it permutes only coordinates having identical signature \(t_i\). The stabilizer is therefore \(\prod_t\mathfrak S_{m_t}\), acting independently on equal-signature coordinate blocks. Its orbits are precisely the count vectors \((a_t)_t\) and have the advertised binomial product sizes. Since colour refinement is equivariant under colour-preserving automorphisms, a stable colour can never split one of these orbits.

**2. Recovering distances through refinement.** For every integer \(h\ge0\), the colour of a vertex after \(h\) rounds determines whether its distance to each marked vertex is at most \(h\), and, if so, determines that distance exactly. This follows by induction on \(h\): the initial colour identifies each marked vertex, and the new colour records the neighbouring old colours. The shortest path characterization \(\mathrm{dist}(x,s)=1+\min_{y\sim x}\mathrm{dist}(y,s)\) then recovers each new distance layer. The diameter of \(Q_d\) is \(d\), so after \(d\) rounds the colour of every vertex determines the entire \(r\)-component distance vector \((\mathrm{dist}(x,s_j))_{0\le j<r}\).

**3. Recovering every signature count.** From the colour of \(x\) at round \(d+1\), one can read the multiset of complete distance vectors of all its neighbours at round \(d\), as well as its own distance vector. Translate so \(s_0=0\). For a coordinate with signature \(t\), flipping that coordinate changes these \(r\) distances by
\[
v_t=(1,\ 1-2t_1,\ldots,1-2t_{r-1})
\]
if \(x_i=0\), and by \(-v_t\) if \(x_i=1\). Each signed difference vector is distinct from every other signed difference vector with a different signature or sign: its first component identifies the sign, and the remaining components identify \(t\). Consequently, the number of occurrences of \(-v_t\) among the neighbour-minus-centre distance vectors is **exactly** \(a_t(x)\). Hence the \((d+1)\)-round refinement partition separates all distinct stabilizer orbits. Together with step 1, this proves the exact stable partition and its stated round bound.

**4. Sharp number of individualizations.** If \(r\) marks make the stable partition discrete, all \(d\) signatures are distinct in the alphabet \(\{0,1\}^{r-1}\), giving \(d\le2^{r-1}\) and \(r\ge1+\lceil\log_2 d\rceil\). Conversely, choose \(s_0=0\) and \(r=1+\lceil\log_2 d\rceil\). Give the \(i\)-th coordinate the distinct length-\((r-1)\) binary code of the integer \(i-1\), for \(1\le i\le d\). For each positive mark index \(j\), set its bit in coordinate \(i\) equal to the \(j\)-th bit of that code. These \(r\) marked cube vertices are distinct: the first \(r-1\) code bits yield nonzero and mutually distinct mark rows because \(d>2^{r-2}\) whenever \(r>1\); the single-mark case \(d=1\) is immediate. All coordinate signatures are distinct, so refinement is discrete. This proves optimality.

## Verification

The companion `check_hypercube.py` executes ordinary refinement directly on the adjacency list of \(Q_d\), compares stable colour classes against the closed-form orbit count vectors, tests the class-count formula, tests discreteness against signature uniqueness, and checks the \(d+1\) bound. It exhaustively tests all choices of at most four marked vertices for \(1\le d\le4\), uses reproducible random marked sets for \(5\le d\le10\), and checks an explicit optimal construction for \(1\le d\le14\). There are 7030 checked cases and zero observed failures; full output is in `check_output.json`. The infinite theorem is established by the proof above, not inferred from these finite experiments.

## Relationship to prior work

Boutin (2009) established the numerical *determining number* of the binary hypercube as \(1+\lceil\log_2 d\rceil\). Determining sets ask only whether the pointwise stabilizer is trivial; that result by itself does not assert that one-dimensional colour refinement computes pointwise-stabilizer orbits for every marked set. The contribution here is the exact refinement-orbit coincidence for **all** marked sets, with every orbit's cardinality, and a uniform \(d+1\) refinement-depth guarantee. Arvind–Köbler–Rattan–Verbitsky (2015) formalized the broader Tinhofer/refinability hierarchy and proved analogous properties for a different graph family, notably Johnson graphs \(J(n,2)\). Arvind–Fuhlbrück–Köbler–Kuhnert–Rattan (2016) considered individualization and refinement in general graphs. These broad frameworks do not state the specific hypercube result in the inspected material. The earlier determining-number theorem must **not** be represented as newly discovered.

## Limitations

Originality is assessed against the identified sources and available searches, not independently certified. The full text of Boutin's 2009 article was not lawfully obtained in this investigation; its abstract explicitly establishes the numerical minimum, while any additional hypercube-specific refinement discussion beyond the accessible abstract is an unresolved priority risk. A general previously published implication from compactness, Tinhofer graphs, or Cartesian products may also overlap this theorem. The result applies only to the binary hypercube with distinct named marked colours; neither all Hamming graphs nor other product families are claimed. No claim is made that the quantitative upper bound on refinement rounds is always sharp. Independent validation has not been performed.

## References

1. D. L. Boutin, *The determining number of a Cartesian product*, Journal of Graph Theory **61** (2009), 77–87, DOI: `10.1002/jgt.20368` (first online 2009-04-06).
2. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:`1502.01255` (first online 2015-02-04).
3. V. Arvind, S. Fuhlbrück, J. Köbler, S. Kuhnert, G. Rattan, *The Parameterized Complexity of Fixing Number and Vertex Individualization in Graphs*, arXiv:`1606.04383` (first online 2016-06-14).
