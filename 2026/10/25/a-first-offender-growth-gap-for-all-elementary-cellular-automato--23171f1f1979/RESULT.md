# A first-offender growth gap for all elementary cellular-automaton images

## Finding

Consider the 256 binary radius-one elementary cellular automata \(F_r\), indexed by their Wolfram rule numbers \(0\le r\le255\), acting on the bilateral full shift \(\{0,1\}^{\mathbb Z}\). Let \(Y_r=F_r(\{0,1\}^{\mathbb Z})\). A finite binary word is **minimally forbidden** for \(Y_r\) if it does not appear in any point of \(Y_r\), although every proper contiguous factor does. Let \(m_r(n)\) count such words of length \(n\ge1\).

**Classification theorem.** Exactly 176 rules have an eventually zero sequence \(m_r(n)\); their image shifts are of finite type. Exactly 28 rules have an infinite, uniformly bounded first-offender sequence. Exactly 52 rules have positive exponential first-offender growth, in the precise sense
\[
\limsup_{n\to\infty}m_r(n)^{1/n}>1.
\]
No elementary rule has unbounded subexponential first-offender growth (including polynomial growth). Thus the minimal-forbidden-word growth invariant of these images has a genuine gap between bounded and exponential behavior.

For the 28 bounded-infinite cases one has the stronger sharp bound \(m_r(n)\le2\) for every \(n\), and exactly four forms, with the following rule groups (all unlisted values are zero):

* For `27,39,53,83,172,202,216,228`, \(m_r(n)=1\) exactly when \(n=4\) or \(n\ge7\).
* For `38,44,52,100,155,203,211,217`, \(m_r(n)=1\) exactly when \(n\ge4\) is even.
* For `46,116,139,209`, \(m_r(n)=1\) exactly when \(n\ge3\) is odd.
* For `58,78,92,114,141,163,177,197`, \(m_r(4)=1\) and \(m_r(n)=2\) for all \(n\ge7\).

Among the 176 finite-type cases, the maximal length of a minimally forbidden word is at most ten, and this cutoff is attained precisely by Rules `57,99,156,198`. The complete per-rule classification and the finite-type cutoff are in `classification.csv`; `verify.py` is a standalone finite-graph certificate.

## Assumptions and scope

All configurations are bilateral and indexed by \(\mathbb Z\). The local rule is \((F_r x)_i=f_r(x_{i-1},x_i,x_{i+1})\), with \(f_r(a,b,c)\) equal to bit number \(4a+2b+c\) of the nonnegative integer \(r\). A finite word belongs to the spatial image language if and only if it labels a path in the four-vertex de Bruijn graph whose vertices are the input pairs \((a,b)\) and whose edges \((a,b)\to(b,c)\) are labelled by \(f_r(a,b,c)\). This concerns the one-step spatial image, not the temporal limit set or entropy of a trajectory.

Let \(I\) be the set of all four input pairs, and let \(\delta_r(S,w)\) be the set of vertices attainable from some vertex in \(S\) along paths labelled by the binary word \(w\). Then \(w\) belongs to the image language if and only if \(\delta_r(I,w)\ne\varnothing\). Finite paths can be extended to bilateral input configurations by arbitrary bits on both sides; no periodic-boundary assumption is made.

## Proof

**1. A deterministic first-offender graph.** Because the image language is factorial, a word \(w\) of length \(n\ge2\) is minimally forbidden if and only if its length-\(n-1\) prefix and suffix are allowed but \(w\) is forbidden. Write \(w=a v b\) with \(a,b\in\{0,1\}\). Define
\[
q=\delta_r(I,av),\qquad s=\delta_r(I,v).
\]
The conditions are exactly \(q\ne\varnothing\), \(\delta_r(q,b)=\varnothing\), and \(\delta_r(s,b)\ne\varnothing\). For fixed first letter \(a\), build a finite labelled graph whose starting state is \((\delta_r(I,a),I)\). On reading a middle letter \(c\), the state \((q,s)\) moves to \((\delta_r(q,c),\delta_r(s,c))\) provided the first component stays nonempty. A state is terminal when at least one final letter \(b\) empties its first component but not the corresponding successor of its second component. Distinct final letters count separately. Empty-prefix letters account for the length-one first offenders.

Consequently, every length-\(n\) minimal forbidden word corresponds *uniquely* to a first-letter choice, an accepted path of length \(n-2\), and a valid final-letter choice. The states are pairs of subsets of a four-element set; they can be computed exactly by bit operations. Discard all states which either cannot be reached from a start or cannot reach a terminal state. This productive graph recognizes the complete infinite first-offender language, not a finite sample.

**2. Growth classification for any productive graph.** Contract the strongly connected components. If there is no directed cycle, the number of accepted paths vanishes at all sufficiently large lengths. If some strongly connected component has more than one internal outgoing labelled edge at a vertex, it contains at least two genuinely different closed walks: by strong connectivity, this yields exponentially many distinct labelled paths along an infinite subsequence of lengths, with fixed paths from the initial state and to a terminal state. This criterion includes parallel edges carrying different letters.

Otherwise every cyclic component is a single directed cycle, with precisely one internal labelled edge leaving each vertex. If an accepted path can traverse two distinct cyclic components, independent numbers of laps around their cycles produce unbounded counts of accepted words of selected lengths (at least linear along an arithmetic progression), but only subexponential growth. If every accepted path visits at most one cyclic component, then for each length there are only uniformly finitely many accepted labelled paths: outside the unique cycle, the path choices and lengths are bounded; the required number of laps is fixed by its total length. These criteria are exhaustive and depend only on finite directed-graph structure.

**3. Complete exact evaluation.** The script `verify.py` constructs both binary de Bruijn transitions for every \(r\in\{0,\ldots,255\}\), takes the two initial-letter graphs, removes nonproductive states, computes their strongly connected components with Tarjan's algorithm, detects branching cycles and directed paths through multiple cyclic components, and independently computes the longest accepting path in every acyclic case. The 256 output rows in `classification.csv` encode the resulting exact classification. The counts are 176 finite, 28 bounded, zero polynomial and 52 exponential. For the finite cases the graph's longest-path calculation proves the sharp length-ten bound and its four extremizers.

In the bounded cases an additional exact transfer-vector calculation starts with one path at each initial state, advances the integer path-count vector, and records its first *identical* repeated vector. Since subsequent vectors are deterministic linear updates, such equality certifies eventual periodicity for **all** lengths. Combining the two first-letter contributions with their exact preperiods and cycle lengths verifies all four displayed formula families and the universal upper bound two. This is an all-length finite-state argument, not extrapolation.

**4. Dynamical significance.** The number \(\limsup_{n\to\infty}m_r(n)^{1/n}\) is the exponential growth invariant of minimal forbidden words discussed in the symbolic-dynamics literature. In the present family it is zero for the 176 finite cases, one for the 28 bounded-infinite cases, and strictly greater than one for the remaining 52; hence the theorem separates types of sofic images that cannot be distinguished by the finite-type/proper-sofic dichotomy alone.

## Verification

Place `verify.py` and `classification.csv` in the same directory and run `python verify.py` with Python 3.10 or newer; no third-party packages are required. All 256 graphs are recomputed from local truth tables and checked against the independent CSV. For each rule, a second enumerator constructs the output words directly from **all** binary input blocks of length \(n+2\) for every \(1\le n\le9\), and checks first-offender counts against the product-automaton calculation. There are exactly \(256\cdot9=2304\) such complete finite output-language comparisons.

The verifier also checks exactly the four finite-type length-ten extremizers and gives an all-length periodic-transfer certificate for every bounded-infinite case. The complete finite-state argument, rather than tests at nine lengths, proves the unrestricted classification.

## Relationship to prior work

Béal, Mignosi, Restivo and Sciortino developed minimal forbidden words as a symbolic-dynamical complexity invariant; subsequent work with Crochemore provided algorithms for factorial regular languages. Abram and Lagarias constructed deterministic presentations for path sets and studied their relation to sofic shifts. Salo's work on von Neumann regularity of cellular automata identifies image finite-typeness and gives explicit first-offender sets for particular elementary rules, including Rule 9, as well as proper-soficity witnesses for Rules 27, 41 and 58.

Those sources provide the foundational constructions and several individual first-offender results. The present theorem instead separates **all 256 elementary one-step images** by asymptotic first-offender growth, proves that no intermediate unbounded polynomial class occurs, supplies exact class sizes, and classifies the 28 bounded-infinite sequences. These conclusions are not consequences of the cited individual examples without the complete productive-graph analysis.

## Limitations

This result does not classify the full rational generating function or exact positive exponential growth constant for each of the 52 exponential cases, although every such constant is computable from the certified graph. It does not assert an analogous trichotomy for larger neighborhoods, larger alphabets, iterated images or limit sets. Historical priority is not independently certified; an older unindexed enumeration or equivalent presentation remains possible. One older minimal-forbidden-word article could be checked only through accessible indexed material, not a complete downloaded text. The claim is supported by an exhaustive finite structural certificate and exact finite-word cross-checks, not by an external independent audit.

## References

1. William Abram and Jeffrey C. Lagarias, *Path sets in one-sided symbolic dynamics*, first public arXiv submission 20 July 2012, arXiv:1207.5004, https://arxiv.org/abs/1207.5004.
2. Marie-Pierre Béal, Filippo Mignosi, Antonio Restivo and Marinella Sciortino, *Forbidden Words in Symbolic Dynamics*, Advances in Applied Mathematics 25 (2000), 163–193, DOI:10.1006/aama.2000.0682.
3. Marie-Pierre Béal, Maxime Crochemore, Filippo Mignosi, Antonio Restivo and Marinella Sciortino, *Computing forbidden words of regular languages*, Fundamenta Informaticae 56 (2003), 121–135.
4. Ville Salo, *On von Neumann regularity of cellular automata*, Natural Computing, DOI:10.1007/s11047-022-09935-w (first arXiv submission 2022), https://link.springer.com/article/10.1007/s11047-022-09935-w.
