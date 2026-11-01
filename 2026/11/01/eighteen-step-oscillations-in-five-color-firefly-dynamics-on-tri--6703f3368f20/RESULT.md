# Eighteen-step oscillations in five-color firefly dynamics on tripartite graphs

## Finding

For the synchronous five-color inhibitory firefly automaton on each labelled complete tripartite graph \(K_{a,b,c}\), \(a,b,c\ge1\), every initial configuration is periodic by time \(40\). Its eventual least period belongs to \(\{5,6,9,18\}\), and all four periods occur for some positive shore sizes. Define
\[
U_3(n)=3^n-3\cdot2^n+3,\qquad U_4(n)=4^n-4\cdot3^n+6\cdot2^n-4.
\]
With \((n_1,n_2,n_3)=(a,b,c)\), the exact number of distinct primitive period-\(18\) orbits is
\[
N_{18}(a,b,c)=\frac{1}{6}\sum_{(i,j,k)\in S_3}2^{n_i}U_3(n_j)U_4(n_k).
\]
Here \(S_3\) means the six ordered permutations of the three shore indices. A primitive period-\(18\) orbit exists if and only if two *different* shores have sizes at least \(3\) and \(4\), respectively. For example, \(N_{18}(1,3,4)=48\) and \(N_{18}(2,2,2)=0\).

## Assumptions and scope

The graph is simple, labelled and complete between three nonempty independent vertex shores; vertices have no self-loops. Colors are \(\{0,1,2,3,4\}\), updated simultaneously. Color \(2\) is the blinking color. A vertex in color \(3\) or \(4\) remains unchanged if at least one neighbor has color \(2\); otherwise it increments modulo \(5\). Vertices of colors \(0,1,2\) always increment modulo \(5\). Periodic-entry time is the least nonnegative update number at which the full labelled state is on a periodic orbit. We count unrooted temporal orbits, not states, without quotienting by vertex or shore relabelings.

## Proof

**1. Finite occupied-support factor.** Encode the set of actually occupied colors on shore \(i\) as a nonempty bit mask \(S_i\in\{1,\ldots,31\}\). A vertex on shore \(i\) encounters a blinking neighbor precisely if \(2\in S_j\cup S_k\), the union of the other shores. Consequently its color map \(\phi_i\) is completely determined by the support triple, and the next support is \(\phi_i(S_i)\). Thus the full microscopic dynamics projects onto a deterministic map \(T\) on the exactly \(31^3=29{,}791\) ordered nonempty support triples, independently of \(a,b,c\).

**2. Complete finite factor enumeration.** The included standalone program `verify_fca5_tripartite.py` explicitly constructs \(T\) for every support triple, follows all directed paths to periodic cycles, and computes all local color permutations along each support cycle. Its complete exhaustive output gives exactly \(89\) directed support cycles, with lengths and counts: \(27\) length-\(1\), one length-\(2\), \(20\) length-\(3\), one length-\(5\), and \(40\) length-\(6\). The largest support preperiod is \(40\), and the numbers of support triples whose eventual support periods are \(1,2,3,5,6\) are respectively \(27,24,60,28684,996\), which sum to \(29791\). The program checks this complete table and the monodromy categories rather than sampling support triples. The entire deterministic algorithm is included, and no unbounded scientific inference is made from a truncated sample.

**3. Lift of cycles to individual vertices.** Along any periodic support cycle, each local map from occupied colors on a shore to occupied colors on that shore at the next support state is surjective. Support sizes can never increase under a function, and returning to the same support size forces equality throughout the cycle. Hence these maps are bijective; composing around a support cycle of length \(L\) produces a permutation \(\pi_i\) on each shore's occupied colors. A labelled state occupying *all* specified colors has least microscopic period exactly \(L\,\operatorname{lcm}(\operatorname{ord}\pi_1,\operatorname{ord}\pi_2,\operatorname{ord}\pi_3)\): the support must return, and surjectivity of the vertex-to-color labelling forces every color permutation to fix every occupied color. These are precisely the monodromy orders calculated in the certificate.

The complete monodromy classification is: the \(27\) length-\(1\) cycles have orders a permutation of \((1,1,5)\); the sole length-\(2\) cycle has \((3,3,3)\); \(18\) length-\(3\) cycles have orders a permutation of \((1,2,3)\) and the other two have \((3,3,3)\); the one length-\(5\) and all \(40\) length-\(6\) cycles have \((1,1,1)\). Therefore the possible microscopic periods are precisely \(5,6,9,18\). Every microscopic state lying above a recurrent support cycle is itself periodic, proving the universal entry-time bound \(40\).

**4. Exact period-\(18\) enumeration.** For any fixed assignment of the monodromy orders \((1,2,3)\) to shores \((i,j,k)\), the complete finite cycle list has three length-\(3\) support cycles. In two of these, shore \(i\) has one occupied color; in the remaining cycle it has two. Shore \(j\) always has four occupied colors and shore \(k\) always has three. For \(n\ge1\), the number of labelled assignments using every color in a specified \(r\)-element support is the surjection count
\[
q_r(n)=\sum_{t=0}^r(-1)^t\binom rt(r-t)^n.
\]
Every such microscopic state has period \(18\). For each of the six permutations, the three support cycles contribute, after weighting their three support phases, exactly \(3[2q_1(n_i)+q_2(n_i)]q_4(n_j)q_3(n_k)\) microscopic period-\(18\) states. Since \(2q_1(n)+q_2(n)=2^n\), summing over the six permutations and dividing by \(18\) states per orbit yields the displayed formula. The surjection factors vanish exactly for \(n_j<4\) or \(n_k<3\), establishing the stated sharp existence condition.

## Verification

`verify_fca5_tripartite.py` uses only the Python standard library. It enumerates every one of \(31^3\) support states, validates the cycle-length census, monodromy classes and maximum preperiod, and independently cross-checks the period-\(18\) formula against direct support-cycle weighting for six shore-size triples. The separate `verify_fca5_micro.py` uses NumPy and advances all \(5^8=390625\) labelled microscopic states on \(K_{1,3,4}\) through \(18\) updates. It finds \(5724\) states fixed by the eighteenth iterate, \(4860\) fixed by the sixth, and none fixed by the ninth or smaller checked divisors; exactly \(864\) states thus have least period \(18\), giving \(48\) orbits. The included `verify_output.txt` records actual runs. These checks establish a finite exhaustive support-factor certificate for the infinite graph family and a direct independent instance test; they are not a substitute for the logical support-factor lifting argument given above.

## Relationship to prior work

Lyu's 2014 finite-state pulse-coupled-oscillator work (arXiv:1407.1103) defines inhibitory firefly updates and studies synchronization and time bounds on paths and related graphs. Lyu's 2016 tree analysis (arXiv:1610.00837) establishes time bounds for trees. Neither inspected account supplies the exact five-color complete-tripartite period spectrum, least-period-\(18\) orbit formula, or exact occupied-support return enumeration shown here. These statements concern graphs with triangles, not the tree models covered by the earlier synchronization theorems. Published exact orbit censuses for *other* update rules, such as binary parity dynamics on complete multipartite graphs, are not equivalent: changing the local rule changes the state map. Searches cannot establish global uniqueness against inaccessible or unindexed literature.

## Limitations

The bound \(40\) is sharp for the abstract support-factor transient but is not claimed optimal for each particular positive shore-size triple. The formula concerns period-\(18\) orbit counts, not complete counts for all other periods, nor any asynchronous or different-color firefly rule. An independent external review has not been carried out. A prior unindexed exact analysis of five-color inhibitory firefly dynamics on complete tripartite graphs could limit the novelty claim.

## References

1. H. Lyu, *Synchronization of finite-state pulse-coupled oscillators*, arXiv:1407.1103 (first public preprint 2014-07-04).
2. H. Lyu, *Time complexity of synchronization of discrete pulse-coupled oscillators on trees*, arXiv:1610.00837 (2016-10-04).
