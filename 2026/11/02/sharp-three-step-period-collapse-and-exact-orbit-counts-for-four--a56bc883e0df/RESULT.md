# Sharp three-step period collapse and exact orbit counts for four-color cyclic dynamics on tripartite graphs

## Finding

Let \(a,b,c\) be arbitrary positive integers and \(F\) the synchronous four-color cyclic cellular automaton on the labelled loopless complete tripartite graph \(K_{a,b,c}\). A vertex of color \(j\in\mathbb Z/4\mathbb Z\) moves to \(j+1\) modulo four if a neighbor currently has color \(j+1\), and otherwise stays at \(j\).

**Sharp universal iterate identity.** For every initial coloring,
\[
F^{7}=F^{3}.
\]
Every orbit reaches a fixed point or a primitive four-cycle within at most three updates, and no primitive two-cycle (or any other period) exists. The three-update bound is attained already on \(K_{1,1,2}\). A primitive four-cycle exists if and only if \(\max(a,b,c)\ge2\).

**Exact primitive-orbit census.** Define the surjection polynomial evaluations
\[
S_j(n)=\sum_{r=0}^{j}(-1)^r\binom jr(j-r)^n
\qquad(1\le j\le4,\ n\ge1).
\]
In particular \(S_1(n)=1\) and \(S_2(n)=2^n-2\). Let \(P_1(a,b,c)\) and \(P_4(a,b,c)\) be the respective numbers of *labelled configurations* with exact temporal periods one and four. Then
\[
P_1(a,b,c)=2\bigl(S_2(a)+2\bigr)\bigl(S_2(b)+2\bigr)\bigl(S_2(c)+2\bigr).
\]
To state the four-period formula compactly, for any sorted triple \(1\le i\le j\le k\le4\) set
\[
M_{ijk}(a,b,c)=\sum_{(r,s,t)\in\operatorname{DistinctPerm}(i,j,k)}S_r(a)S_s(b)S_t(c),
\]
where the sum contains every **distinct ordered permutation** of the multiset \(\{i,j,k\}\) exactly once. Then
\[
P_4(a,b,c)=\sum_{1\le i\le j\le k\le4} c_{ijk}M_{ijk}(a,b,c),
\]
with all nonzero coefficients displayed here (every unlisted coefficient is zero):

| \((i,j,k)\) | \(c_{ijk}\) | \((i,j,k)\) | \(c_{ijk}\) |
|:--|--:|:--|--:|
| \((1,1,2)\) | 4 | \((1,2,2)\) | 16 |
| \((1,2,3)\) | 8 | \((1,3,3)\) | 12 |
| \((1,3,4)\) | 4 | \((1,4,4)\) | 4 |
| \((2,2,2)\) | 42 | \((2,2,3)\) | 32 |
| \((2,2,4)\) | 6 | \((2,3,3)\) | 36 |
| \((2,3,4)\) | 12 | \((2,4,4)\) | 6 |
| \((3,3,3)\) | 36 | \((3,3,4)\) | 12 |
| \((3,4,4)\) | 4 | \((4,4,4)\) | 1 |

The number of distinct labelled primitive four-cycle orbits is precisely \(N_4(a,b,c)=P_4(a,b,c)/4\), and the number of fixed configurations is \(N_1(a,b,c)=P_1(a,b,c)\). For instance, \(N_4(1,1,2)=2\) and \(N_4(2,2,2)=138\). For balanced shore sizes tending to infinity, a uniformly random initial coloring is already in a primitive four-cycle with probability tending to one.

## Assumptions and scope

The graph has three specified nonempty labelled independent shores of sizes \(a,b,c\), all possible edges between different shores, and no edges within a shore or loops. Updates are simultaneous; the successor-contact rule uses exactly four cyclically ordered colors and excitation threshold one. A 'primitive four-cycle' refers to the least *temporal* period of a configuration under this fixed graph map, not a support-set cycle. Different choices of phase in the same four-cycle are counted once in \(N_4\). The result is not asserted for other alphabets, general graphs, or asynchronous updating.

## Proof

**1. Complete finite support reduction.** For an arbitrary state \(x\), let \(A_i(x)\subseteq\{0,1,2,3\}\) be the nonempty set of colors present on shore \(i\), for \(i=1,2,3\). Put \(B_i=A_j\cup A_k\), where \(\{i,j,k\}=\{1,2,3\}\). Each vertex of shore \(i\) and color \(u\) follows the same deterministic color map
\[
h_{i,A}(u)=\begin{cases}u+1\pmod4,&u+1\pmod4\in B_i,\\u,&\text{otherwise}.\end{cases}
\]
The successor support on that shore is exactly \(A'_i=h_{i,A}(A_i)\). Crucially, the update depends on the **sets of occupied colors**, never their multiplicities. Thus the dynamics for all positive \(a,b,c\) are governed by the \((2^4-1)^3=3375\) nonempty ordered support triples. To verify identities between full-state iterates, it suffices to track one distinguishable representative for every occupied color in every shore: vertices with the same initial shore/color have identical complete trajectories. A possible collision of two representatives must be retained, rather than incorrectly interpreting the subsequent support dynamics as reversible.

**2. All-depth iterate identity and sharpness.** The accompanying pure-Python verifier traverses every one of the \(3375\) possible support triples. For each it constructs all representative trajectories through step seven via the displayed successor rule and checks equality at steps three and seven **for every original representative**, not merely equality of the final support sets. The full finite enumeration thereby proves \(F^7(x)=F^3(x)\) for *every* microscopic coloring \(x\), regardless of shore cardinalities. The calculation is a finite proof of an infinite family because the reduction in Step 1 is exact, and the program's bounds include every nonempty support triple and every initial color therein. It also verifies that three is the largest minimal periodic-entry time. For a concrete sharp example, on \(K_{1,1,2}\) begin with shore color sets \((\{0\},\{0\},\{1,2\})\). Its successive sets are
\[
(\{0\},\{0\},\{1,2\})\to(\{1\},\{1\},\{1,2\})\to(\{2\},\{2\},\{1,2\})\to(\{2\},\{2\},\{2\}),
\]
and the last configuration is fixed. Neither earlier state is periodic.

**3. True microscopic periods, not merely support periods.** Exhaustive functional-graph enumeration of the \(3375\)-node support map finds \(55\) fixed support cycles, \(9\) support cycles of length two, and \(150\) of length four. This support data alone would *not* identify microscopic periods: for example, the support two-cycle
\[
(\{0,2\},\{1,3\},\{0,2\})\longleftrightarrow(\{1,3\},\{0,2\},\{1,3\})
\]
shifts every represented vertex by two colors after two steps, so it lifts to a genuine four-cycle, never a two-cycle. Tracking all original colored representatives shows that exactly \(54\) recurrent support triples yield fixed microscopic configurations and the other \(619\) recurrent support triples yield primitive four-cycle configurations. No recurrent support triple yields period two. The full preperiod/least-microperiod support-triple histogram is: time 0: \((54,619)\); time 1: \((112,702)\); time 2: \((856,384)\); time 3: \((552,96)\), with entries ordered (fixed, four-cycle). These eight counts sum to \(3375\).

**4. Exact counting.** A fixed occupied support set of size \(j\) on a labelled shore with \(n\) vertices has exactly \(S_j(n)\) surjective assignments of the four named colors to the shore, by inclusion-exclusion. Hence each recurrent support triple \((A_1,A_2,A_3)\) contributes exactly \(\prod_{i=1}^3 S_{|A_i|}(n_i)\) labelled periodic configurations. Grouping the \(54\) fixed supports by their shore support cardinalities gives the coefficients \(16\), \(8\), \(4\), and \(2\) on the respective sorted triples \((1,1,1)\), \((1,1,2)\), \((1,2,2)\), and \((2,2,2)\), which factor as stated. Grouping the other \(619\) periodic support triples gives exactly the sixteen rows of the \(c_{ijk}\) table. Dividing the latter count by four gives the primitive orbit count because each four-cycle has exactly four distinct configurations.

The \((1,1,2)\) coefficient in the four-cycle table is positive, so a four-cycle exists whenever any shore contains at least two vertices (and the other shores are nonempty). Conversely, if all three shore sizes equal one, only singleton supports can occur and no four-cycle supports exist. Finally, as \(n\to\infty\), the probability that every color appears on each shore of \(K_{n,n,n}\) tends to one; all such states advance every vertex at every step and have least period four. This proves the asymptotic statement.

## Verification

Run `python3 verify.py` in the extracted package directory. The standard-library verifier checks every support state, proves the decorated representative identity at times three and seven, independently enumerates all recurrent support cycles, checks the exact sorted-support coefficient table, and directly simulates the original vertex-based process on nine small but nontrivial shore-size triples. In total the direct microscopic tests cover \(173376\) labelled configurations, while the exact quotient calculation covers all \(3375\) possible support triples and does not impose any upper bound on graph sizes. The saved `verify_output.txt` was generated by running this program. `support_classes.tsv` records the exact preperiod and least microscopic period for each support triple and can be regenerated from the verifier. Direct finite microscopic tests are cross-checks; the universal argument relies on the exact support reduction and exhaustive finite certificate.

## Relationship to prior work

Fisch, Gravner, and Griffeath (1991; arXiv posting 1993) formulate the general multi-color successor-contact cyclic automaton and study spatially distributed waves and threshold-range behavior predominantly on planar lattices. Gravner, Lyu, and Sivakoff (arXiv:1610.07320, 2016) analyze **three-color** excitable dynamics on arbitrary graphs. Neither paper states an exact four-color complete-tripartite temporal iterate identity or an orbit census parameterized by all three shore sizes. The distinction is genuinely graph-topological: a direct four-color complete-bipartite example on \(K_{3,3}\), with initial shore words \((0,1,2)\) and \((0,2,3)\), has primitive temporal period six (its six iterates are pairwise distinct), a period prohibited by the three-shore theorem. The presented exact enumeration is therefore not a formal consequence of simply allowing different shore sizes in a two-shore result or of the three-color winding theory.

## Limitations

Originality is assessed against the identified primary literature and mathematical-record searches, not established by a formal exhaustive survey of all historical literature; an unindexed equivalent remains possible. The theorem supplies recurrent-state and orbit counts, not complete attraction-basin cardinalities by entry time. A finite exact computation is an essential proof step; the independent code is supplied so that the entire bounded certificate can be checked directly. Independent scientific audit has not been performed.

## References

1. R. Fisch, J. Gravner and D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing **1** (1991), 23–39, DOI: 10.1007/BF01890834; public preprint arXiv:patt-sol/9304001 (1993-04-02).
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320 (2016-10-24).
