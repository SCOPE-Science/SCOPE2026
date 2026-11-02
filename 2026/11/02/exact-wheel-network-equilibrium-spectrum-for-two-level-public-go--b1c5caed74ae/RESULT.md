# Exact wheel-network equilibrium spectrum for two-level public-goods responses

## Finding

For integers \(m\ge3\) and \(r\ge2\), let \(W_{m+1}\) be the wheel with a rim cycle of \(m\) labeled vertices and one universal hub. Each agent chooses activity \(0\) or \(1\), with the homogeneous strict best response \(1\) precisely when the number of active **open** neighbors belongs to \(\{0,r\}\). Let \(E(m,r)\) be the number of labeled pure Nash equilibria.

For \(k\ge1\), define
\[
M_m(k)=\begin{cases}
\dfrac{m}{k}\binom{k}{m-2k},& 0\le m-2k\le k,\\
0,&\text{otherwise},
\end{cases}
\qquad P_m=\sum_{k=1}^{m}M_m(k).
\]
Then the **complete exact spectrum** is
\[
E(m,r)=\begin{cases}
2+3\mathbf1_{\{3\mid m,\ m\ne6\}}+3\mathbf1_{\{m=3\}},&r=2,\\
1+P_m-M_m(r)+\mathbf1_{\{m=r=3\}},&r\ge3.
\end{cases}
\]
The unique-equilibrium case across the entire family is exactly \((m,r)=(7,3)\), corresponding to the eight-vertex wheel. For every fixed \(r\ge3\) and \(m>3r\), the formula simplifies to \(E(m,r)=1+P_m\). Here \(P_m\) is the Perrin number satisfying \(P_m=P_{m-2}+P_{m-3}\), \(P_3=3,P_4=2,P_5=5\). Thus if \(\alpha\approx1.324717957\) is the positive root of \(z^3-z-1=0\),
\[
E(m,r)\sim\alpha^m\quad(m\longrightarrow\infty,\ r\ge3\text{ fixed}),
\]
whereas \(E(m,2)\le8\) for every \(m\). This is a sharp change from bounded to exponentially growing equilibrium multiplicity when the second favored active-neighbor count increases from two to three.

## Assumptions and scope

The wheel is simple, undirected and unweighted. Its rim \(C_m\) has \(m\ge3\) vertices, each adjacent to its two cyclic neighbors and the hub; the hub is adjacent to every rim vertex. The action \(x_v\in\{0,1\}\) must equal \(\mathbf1_{\{d_x(v)\in\{0,r\}\}}\), where \(d_x(v)=\sum_{w\sim v}x_w\) counts other active agents, not the agent itself. This is a strict best-response pattern without indifference. The integer \(r\ge2\) may exceed the hub degree; such responses are still well-defined. Vertices are labeled; rotations or reflections are not identified. Pure Nash equilibrium means every agent is responding optimally to the others' current actions.

## Proof

**1. Hub inactive, \(r\ge3\).** The rim vertex has at most two active rim neighbors, so it is active if and only if neither cyclic neighbor is active. This is exactly the condition that the active rim vertices form a maximal independent set of the cycle. If there are \(k\) such vertices, write the cyclic distances between consecutive selected vertices. Independence requires each distance at least two, while domination of all unselected vertices requires each distance at most three. Hence all \(k\) distances are either two or three, and exactly \(m-2k\) of them are three. Choose a starting labeled selected vertex in \(m\) ways and then one of \(\binom{k}{m-2k}\) ordered gap words. Each selected configuration is counted exactly \(k\) times, proving the formula \(M_m(k)\). An inactive hub is best responding precisely if \(k\notin\{0,r\}\), and maximal independent sets are nonempty. This case contributes \(P_m-M_m(r)\).

**2. Hub active, \(r\ge3\).** Every rim vertex sees at least one active neighbor, namely the hub. If \(r\ge4\), its total active-neighbor count is at most three, so every rim vertex must be inactive. This configuration is an equilibrium because the active hub sees zero active neighbors. If \(r=3\), a rim vertex is active exactly when its two cyclic neighbors are both active. On a connected rim cycle, the only solutions are the all-inactive and the all-active rim. The all-inactive rim permits the active hub. The all-active rim permits it only when the hub sees exactly three active neighbors, namely \(m=3\). This case contributes \(1+\mathbf1_{\{m=r=3\}}\). Adding to Step 1 proves the second formula.

**3. The resonant case \(r=2\).** Let \(h\) be the hub action and \(x_i\) the rim actions, with cyclic indices. If \(h=0\), the rim response equals one precisely when its two cyclic neighbors agree; equivalently, over \(\mathbb F_2\),
\[
x_{i-1}+x_i+x_{i+1}=1.
\]
If \(h=1\), the rim response equals one precisely when the two cyclic neighbors disagree, giving
\[
x_{i-1}+x_i+x_{i+1}=0.
\]
Subtracting consecutive equations gives \(x_{i+3}=x_i\). If \(3\nmid m\), periodicity forces constant rim actions: all one for \(h=0\), all zero for \(h=1\). Both satisfy the respective hub conditions. If \(3\mid m\), each equation has four admissible period-three words: for \(h=0\), the word \(111\) and three rotations of \(100\); for \(h=1\), the word \(000\) and three rotations of \(110\). The three nonconstant \(h=0\) words have \(m/3\) active rim agents, so the inactive hub permits them exactly when \(m/3\ne2\). The three nonconstant \(h=1\) words have \(2m/3\) active rim agents; the active hub permits them only when \(2m/3=2\), or \(m=3\). This proves the first formula, including the exceptional lengths three and six.

**4. Uniqueness.** For \(r=2\), the formula is always at least two. For \(r\ge3\), the active-hub/all-inactive-rim profile always exists. It is the only equilibrium exactly when the extra \(m=r=3\) case is absent and all maximal independent sets of \(C_m\) have size exactly \(r\). The possible sizes are precisely all integers in \([\lceil m/3\rceil,\lfloor m/2\rfloor]\), by the gap argument in Step 1. This interval has a single integer exactly when \(m\in\{3,4,5,7\}\), with respective sizes \(1,2,2,3\). The constraint \(r\ge3\) leaves only \(m=7,r=3\).

**5. Growth.** The known cyclic maximal-independent-set count \(P_m\) satisfies the Perrin recurrence, also following by the standard transfer-count recurrence for cyclic gap words of lengths two and three. Its characteristic polynomial is \(z^3-z-1\), and the initial values identify \(P_m\) as the sum of the \(m\)-th powers of its three roots. The unique positive real root is \(\alpha>1\), and the other two roots have modulus \(\alpha^{-1/2}<1\); hence \(P_m=\alpha^m+O(\alpha^{-m/2})\). For fixed \(r\ge3\) and \(m>3r\), no maximal independent set can have only \(r\) vertices, so \(M_m(r)=0\) and the claimed asymptotic follows.

## Verification

Run the standard-library-only program with `python3 verify_wheels.py`. It tests the formula directly against all binary action profiles for wheel rim lengths \(3\) through \(13\) and response values \(2\) through \(m+2\), and independently enumerates maximal independent sets of cycles of lengths \(3\) through \(18\). It also checks \(98\) exact recurrence values through rim length \(100\). The completed run reported \(99\) wheel parameter combinations and \(425{,}952\) fully evaluated action profiles, all matching the theorem. These finite checks corroborate the proof but do not establish the infinite statement by exhaustion.

## Relationship to prior work

Klimm and Stahlberg (2023, arXiv:2301.11849) establish hardness for the homogeneous nonmonotone or *picky* rule that activates at zero or a specified other number of active neighbors. Gilboa and Nisan (2022, arXiv:2207.04238), and Gilboa (2023, arXiv:2301.11580), study general complexity boundaries, including the zero-or-two-neighbor pattern. Their general hardness statements neither give a labeled wheel equilibrium count nor imply that a particular wheel has a unique equilibrium. The Perrin enumeration of maximal independent sets on cycles is classical, including the work of Bisdorff and Marichal (2008); it is explicitly used, not claimed as new. The new statement concerns the hub-dependent strategic compatibility of those configurations, the exceptional modular case \(r=2\), and their uniform sharp comparison across all wheel sizes and all \(r\ge2\).

## Limitations

The classification assumes a homogeneous strict response on a wheel. It does not describe convergence of best-response paths, stochastic dynamics, welfare, arbitrary networks, vertex-specific response patterns, or different interpretations of the number of active neighbors. The uniqueness result does not assert uniqueness in other graph families. The complete prior-publication priority question warrants independent specialist review; a literature search alone cannot establish it absolutely.

## References

- M. Klimm and M. J. Stahlberg, *Complexity of Equilibria in Binary Public Goods Games on Undirected Graphs* (2023), arXiv:2301.11849, https://arxiv.org/abs/2301.11849 (initial public release 2023-01-27).
- M. Gilboa and N. Nisan, *Complexity of Public Goods Games on Graphs* (2022), arXiv:2207.04238, https://arxiv.org/abs/2207.04238.
- M. Gilboa, *A Characterization of Complexity in Public Goods Games* (2023), arXiv:2301.11580, https://arxiv.org/abs/2301.11580.
- R. Bisdorff and J.-L. Marichal, *Counting Non-Isomorphic Maximal Independent Sets of the n-Cycle Graph*, Journal of Integer Sequences 11 (2008), Article 08.5.7, https://cs.uwaterloo.ca/journals/JIS/VOL11/Marichal/marichal.html.
