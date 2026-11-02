# A nonmonotone twelve-cycle window for threshold-two excitable dynamics on tripartite graphs

## Finding

Consider the three-state synchronous Greenberg–Hastings rule on the complete tripartite graph \(K_{a,b,c}\) with positive shore sizes \(a\le b\le c\). States are \(0\) (resting), \(1\) (excited), and \(2\) (refractory). Every \(1\) advances to \(2\), every \(2\) to \(0\), and a \(0\) advances to \(1\) exactly when at least **two** vertices in the other shores are excited.

**Theorem.** Every labelled configuration is eventually periodic, its primitive period belongs to \(\{1,3,4,12\}\), and every trajectory enters its eventual orbit by time \(11\). The exact existence conditions are:

- Period \(1\): always (the all-resting fixed point is the only fixed state).
- Period \(3\): exactly when \(a\ge2\), or when \(a=1\) and \(b\ge5\).
- Period \(4\): exactly when \(a=b=2\) and \(c\ge4\).
- Period \(12\): exactly when \(a\le3\) and \(b\ge4\).

Moreover, first-periodic-entry time \(11\) occurs **exactly when** \(a=2\), \(b\ge3\), and \(c\ge5\); it is the sharp global maximum. For the family of all complete tripartite graphs, \(F^{23}=F^{11}\) holds with minimal universal transient exponent \(11\) and minimal universal eventual period \(12\). Here \(F\) denotes the relevant graph's global update map.

This is a nonmonotone persistence phenomenon: twelve-cycles exist on \(K_{1,4,4}\) and on all triples with \(a\le3\le b\) and \(b\ge4\), but disappear entirely as soon as the *smallest* shore has at least four vertices. Four-cycles likewise disappear as soon as either of the two smaller shores has more than two vertices.

The theorem also supplies an exact labelled first-entry/period census for **every** positive \(a,b,c\). Put \(g_0(z)=1\), \(g_1(z)=z\), and \(g_2(z)=e^z-1-z\). Let \(S_{t,p}\) be the finite set of nine-coordinate signatures from `certificates/tripartite_signatures.csv` with recorded first-entry time \(t\) and primitive period \(p\). For \((Z_1,Z_2,Z_3)=(X,Y,Z)\), define

\[
P_{t,p}(X,Y,Z)=\sum_{\sigma\in S_{t,p}}\prod_{i=1}^3\prod_{j=0}^2g_{\sigma_{ij}}(Z_i).
\]

Then the **exact number of labelled initial configurations** with first entry \(t\) and period \(p\) is

\[
N_{a,b,c}(t,p)=a!b!c!\,[X^aY^bZ^c]P_{t,p}(X,Y,Z).
\]

The number of primitive period-\(p\) orbits is \(N_{a,b,c}(0,p)/p\), and all other first-entry/period populations follow from the same finite formula.

## Assumptions and scope

There are three **nonempty labelled shores** and no within-shore edges. The excitation threshold is two and excludes a vertex itself. All updates are simultaneous; the refractory dynamics are deterministic \(1\to2\to0\). First-periodic-entry time is the least \(t\ge0\) such that \(F^t(x)\) lies on a periodic orbit. Primitive period is the least positive return period after that time. The theorem holds for all positive integer shore sizes, without randomness or asymptotic assumptions.

## Proof

**Exact finite factor.** Partition each shore by each of its three *initial* colors. The nine initial cohorts remain internally homogeneous forever, because every vertex in a shore sees exactly the same neighbors and has the same update rule. A cohort of size zero is absent; a nonzero cohort's color evolves as one tagged state. Every future excitation test depends only on whether the total number of excited vertices in the two other shores is at least two. Therefore the initial cohort sizes can each be replaced by their truncations \(\min(2,m)\), without changing any future excitation decision. Since a cohort's being nonempty is also preserved by this truncation, equality of global labelled states at two times is equivalent to equality of the colors of all nonempty cohorts. Hence *both* the first-entry time and the primitive period are unchanged by truncation.

Each shore has \(3^3-1=26\) nonempty truncated count triples. Thus there are exactly \(26^3=17{,}576\) signatures, independent of the original shore sizes. For each signature the deterministic factor has nine cohort slots, with a distinguished absent marker on zero-sized cohorts, and updates each occupied cohort using the threshold-two excited count of the two other shores.

**Finite exhaustive step.** The attached standalone verifier enumerates all \(17{,}576\) signatures, follows each state until repetition, and records the exact tail and primitive cycle lengths in `certificates/tripartite_signatures.csv`. It **independently** constructs the actual labelled graph with the minimal representative number (zero, one, or two) of vertices in each initial cohort, evolves it vertex-by-vertex, and checks agreement of the two stopping times for *every* signature. The resulting exhaustive record has maximal first-entry time \(11\), with primitive periods precisely \(1,3,4,12\). The verifier asserts the entire joint histogram of signature stopping times and primitive periods; the certificate has a header and exactly \(17{,}576\) data rows.

**Sharp conditions and unbounded shore sizes.** A capped initial-color triple \((u_0,u_1,u_2)\in\{0,1,2\}^3\setminus\{(0,0,0)\}\) occurs in a shore of size \(m\) exactly when \(u_0+u_1+u_2\le m\), and either equality holds or at least one coordinate equals \(2\). Indeed, extra vertices can be added to any already-size-at-least-two cohort and cannot be added to cohorts of exact capped size zero or one. Consequently, for **every** \(m\ge7\), exactly the same capped shore triples are feasible: those containing a \(2\). Checking all sorted triples of sizes in \(\{1,\ldots,7\}\) therefore establishes the stated period-existence and sharp time-\(11\) criteria for **all** positive shore sizes. The verifier performs precisely this exhaustive check, including the boundary values.

For sharpness, the capped signature \(((0,0,1),(0,2,2),(2,0,2))\) is realized on \(K_{1,4,4}\) and has primitive period \(12\), first entered at time \(1\). The signature \(((1,0,1),(1,2,0),(1,2,2))\) on \(K_{2,3,5}\) reaches its fixed orbit first at time \(11\). These signatures are part of the exact finite certificate, not statistical examples. The existence conditions are verified directly against the full exhaustive table.

**Counting.** For a labelled shore of size \(m\), the number of ways to realize a given truncated count triple \((u_0,u_1,u_2)\) is \(m![z^m]\prod_jg_{u_j}(z)\): the exponential generating functions describe empty, singleton, and size-at-least-two initial color classes. Multiplying over the independent shores and summing exactly the signatures of stopping-time type \((t,p)\) gives the stated coefficient formula. Every period-\(p\) orbit contains exactly \(p\) configurations with \(t=0\), proving the orbit formula.

## Verification

Run `python3 verification/verify_tripartite.py certificates/tripartite_signatures.csv` from the artifact root. The verifier uses only the Python standard library, checks all \(17{,}576\) signatures by two distinct implementations, checks the cutoff-based all-size classifications in all \(84\) sorted size triples up to size seven, and independently enumerates labelled configurations for shore sizes \((1,1,1)\), \((1,2,3)\), \((2,2,2)\), and \((2,2,4)\). Recorded output is in `verification/run_output.txt`. Exhaustive finite computation proves a uniform infinite-family theorem **only because** the preceding cohort truncation and size-seven cutoff arguments are exact.

## Relationship to prior work

Fisch, Gravner, and Griffeath introduced and investigated threshold Greenberg–Hastings excitation, emphasizing two-dimensional lattices, waves, and stable periodic objects (1991; dated public preprint 1993-04-02). Gravner, Lyu, and Sivakoff studied threshold-one three-color dynamics on arbitrary graphs (arXiv:1610.07320, first posted 2016-10-24). Previously established exact threshold-two biclique results cover only two shores and permit periods \(1,3,4\), with maximal entry time five. The present third shore creates a genuine period-twelve window, and the precise disappearance of that period on balanced large tripartite graphs is not implied by those results. Prior four-state and threshold-one tripartite models use different update rules and are not substitutions. The inspected 1991 paper does not state the exact tripartite size windows or the finite exact census.

## Limitations

This is a computer-assisted finite-quotient classification, not a symbolic list of all \(17{,}576\) trajectories. Its proof depends on the supplied exhaustive standard-library checker and its mathematically established finite reduction. The census is specified as an exact coefficient extraction rather than a short elementary closed form for each size. The published literature comparison cannot exclude unindexed historical equivalents; independent audit has not been performed. No claim concerns unequal thresholds, more than three shores, or different refractory lengths.

## References

1. R. Fisch, J. Gravner, D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing **1** (1991), 23–39, doi:10.1007/BF01890834; dated preprint arXiv:patt-sol/9304001, 1993-04-02. Full text: https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf.
2. R. Durrett, D. Griffeath, *Asymptotic behavior of excitable cellular automata*, Experimental Mathematics **2** (1993), 183–208, arXiv:patt-sol/9303002, posted 1993-03-22.
3. J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, posted 2016-10-24, doi:10.1214/17-AAP1350.
