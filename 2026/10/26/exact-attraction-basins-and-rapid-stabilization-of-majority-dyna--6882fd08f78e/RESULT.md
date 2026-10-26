# Exact attraction basins and rapid stabilization of majority dynamics on friendship graphs

## Finding

Let \(F_m\), for an arbitrary integer \(m\geq1\), be the friendship graph consisting of \(m\) edge-disjoint triangles with a single common hub and no other edges. Run synchronous binary majority dynamics on *open* neighborhoods: each vertex adopts the strict majority of its neighbors and retains its current color when its neighbors are tied. All \(2^{2m+1}\) initial binary colorings are distinguished by vertex labels.

**Complete basin theorem.** Every orbit reaches a fixed coloring after at most two simultaneous updates; this bound is attained if and only if \(m\geq3\). A coloring is fixed precisely when (i) each peripheral pair is monochromatic and (ii) the number \(j\) of peripheral pairs opposite the hub satisfies \(0\leq j\leq m/2\). Thus the number of fixed colorings is
\[
E_m=2\sum_{j=0}^{\lfloor m/2\rfloor}\binom mj
=\begin{cases}2^m,&m\text{ odd},\\2^m+\binom m{m/2},&m\text{ even}.\end{cases}
\]
For each *individual* fixed coloring with \(j\) pairs opposite its hub, its full attraction-basin cardinality is
\[
B_m(j)=\begin{cases}
3^{m-j}+3^j,&2j<m,\\
3^j,&2j=m.
\end{cases}
\]
In particular, the **complete terminal-blue-count polynomial** is
\[
H_m(z)=\sum_{j=0}^{\lfloor(m-1)/2\rfloor}\binom mj
(3^{m-j}+3^j)(z^{2j}+z^{2m-2j+1})
+\mathbf1_{2\mid m}\binom m{m/2}3^{m/2}(z^m+z^{m+1}).
\]
The coefficient of \(z^k\) is the number of initial colorings whose eventual fixed coloring has exactly \(k\) blue vertices; it is not merely the number of fixed colorings with that population.

When the initial coloring is uniformly random, the exact probability of eventual monochromatic consensus is
\[
\Pr(\mathrm{consensus})=\frac{3^m+1}{4^m},
\]
which tends to zero exponentially even though the hub is adjacent to every other vertex. Conversely, the probability that the hub retains its *initial* opinion in the terminal configuration tends to one. The exact number of initial colorings that require two rounds (rather than zero or one) is
\[
N_2(m)=2\sum_{b=1}^{\lfloor(m-1)/2\rfloor}\binom mb
\sum_{a=0}^{b-1}\binom{m-b}{a}2^{m-b-a},
\]
and \(N_2(m)/2^{2m+1}\to1/2\) as \(m\to\infty\).

## Assumptions and scope

Each of the \(m\) peripheral pairs \(\{u_i,w_i\}\) has edges \(u_iw_i\), \(u_ih\), and \(w_ih\) to the common hub \(h\); different pairs have no interconnections. There are exactly two opinions, labelled \(0\) and \(1\). Every vertex updates simultaneously from the preceding configuration. The vertex does not count itself in the neighborhood majority, and a tied vote causes it to keep its own opinion. There are no random update choices. Basin size counts *every labelled initial configuration* that eventually reaches a specified fixed configuration, including the fixed configuration itself. The probability assertions use independent fair initial opinions on all vertices.

## Proof

Fix an initial hub color \(s\), and write \(\bar s\) for the opposite color. Each peripheral pair begins in exactly one of the following three types: \(A=(s,s)\), \(B=(\bar s,\bar s)\), and \(C\), comprising the two mixed orientations. Write \(a,b,c\) for the numbers of pairs of these types, with \(a+b+c=m\). The two members of an \(A\) pair stay at \(s\); the two members of a \(B\) pair stay at \(\bar s\), because each sees one neighbor of each color; and any mixed \(C\) pair becomes \((s,s)\) in a single update. Thereafter *every* peripheral pair is monochromatic. A monochromatic pair can never change, regardless of later changes of the hub: both peripheral vertices always see at least one neighbor matching themselves, and at most one opposite neighbor. Thus all peripheral colors freeze after the first update.

At the first update, the hub compares \(2a+c\) neighbors of color \(s\) with \(2b+c\) of color \(\bar s\), and consequently keeps \(s\) if and only if \(a\geq b\). After that update, the hub has exactly \(2(m-b)\) peripheral neighbors of color \(s\) and \(2b\) of the opposite color. Its next update chooses the strict peripheral majority, or keeps its first-update opinion in case of equality. That second-update hub color then remains unchanged forever. This proves stabilization by round two and excludes all nontrivial periodic orbits.

For a coloring to be fixed, no pair can be mixed: its member opposing the hub would see two neighbors of the hub color and change. With every pair monochromatic, no peripheral vertex can change. The hub is stable exactly when the number \(j\) of pairs opposing its color is at most \(m/2\). Choosing the hub color and these \(j\) pairs proves the formula for \(E_m\); binomial symmetry yields its two parity expressions.

Fix a specified terminal fixed coloring whose hub color is \(s\) and whose \(j\) opposing pairs satisfy \(2j<m\). If the initial hub already has color \(s\), those \(j\) opposing pairs were necessarily both \(\bar s\), while each of the other \(m-j\) pairs could initially be both \(s\) or mixed in either orientation: exactly \(3^{m-j}\) possibilities. If the initial hub has color \(\bar s\), the \(m-j\) terminal pairs of color \(s\) must have been both \(s\) initially; each of the other \(j\) terminal pairs admits the three possibilities of being both \(\bar s\) or mixed. Since \(m-j>m/2\) initial pairs oppose the initial hub, its final color must be \(s\), giving \(3^j\) possibilities. The two cases are disjoint, proving \(B_m(j)=3^{m-j}+3^j\).

At the tie boundary \(2j=m\), the second hub update retains its first-update color. If initially the hub has its final color \(s\), the first-update hub remains \(s\) only when all \(j\) initially non-opposing peripheral pairs were of type \(A\); there is one possibility. If initially it has \(\bar s\), of the \(3^j\) possibilities for the remaining pairs, exactly one (all type \(A\) relative to \(\bar s\)) keeps that initial hub color, so \(3^j-1\) yield final hub color \(s\). Adding gives the tie-boundary basin size \(B_m(j)=3^j\). These arguments exhaust every initial state and assign it to exactly one fixed point.

For terminal-blue counts, a fixed state with hub color \(0\) and \(j\) opposing pairs has exactly \(2j\) blue vertices, while its color-swapped state has \(2m-2j+1\) blue vertices. There are \(\binom mj\) fixed states with either chosen hub color and each has basin size \(B_m(j)\). Summation proves the displayed polynomial. The two monochromatic fixed states, each with \(j=0\), have basin size \(3^m+1\). Dividing their combined basin weight by \(2^{2m+1}=2\cdot4^m\) gives the consensus probability.

For exact two-round stabilization, the first hub must switch away from \(s\) and the second must switch back, because the peripheral vertices already freeze at round one. The first switch requires \(a<b\). The second switch back requires \(2b<m\); when \(2b=m\), the hub is tied and holds its first-update color, and when \(2b>m\), that opposite color is the strict majority. Fixing \(b\geq1\), choosing the \(b\) opposite monochromatic pairs, choosing \(a<b\) matching monochromatic pairs among the rest, assigning either mixed orientation to each remaining pair, and choosing either initial hub color gives exactly the displayed \(N_2(m)\). Such configurations exist exactly when \(m\geq3\), proving the sharp two-round threshold.

Finally, conditional on the initial hub color under a uniform initial coloring, the category of each peripheral pair is independent, with \(\Pr(A)=\Pr(B)=1/4\) and \(\Pr(C)=1/2\). Therefore \(b\sim\mathrm{Binomial}(m,1/4)\), and \(\Pr(b\geq m/2)\to0\), which proves persistence of the initial hub with probability tending to one. Moreover, \(\Pr(a=b)=\binom{2m}{m}/4^m\to0\): this follows by taking the constant coefficient of \((z+2+z^{-1})^m/4^m\). Symmetry between \(a\) and \(b\) gives \(\Pr(a<b)\to1/2\). The two-round condition differs from \(a<b\) only when \(b\geq m/2\), an event of vanishing probability. Thus \(N_2(m)/2^{2m+1}\to1/2\).

## Verification

The included standalone `verify.py` constructs the labelled friendship graph directly via index arithmetic and applies the synchronous open-neighborhood majority rule to each vertex. It exhaustively checks all \(2^{2m+1}\) initial colorings for every integer \(1\leq m\leq8\), totaling \(174{,}760\) states. For each input it independently iterates the actual update map, proves computationally that round two is fixed for the tested instances, records its exact absorption time and terminal-blue count, and compares the resulting individual basin sizes against \(B_m(j)\), the fixed-point total against \(E_m\), the terminal polynomial against \(H_m(z)\), consensus counts, and two-round counts against \(N_2(m)\). All assertions pass. The exhaustive finite check tests the implementation and boundary conventions; the above elementary argument, not the enumeration, proves the statements for all \(m\).

At \(m=3\), the terminal-blue-count polynomial is \(28+36z^2+36z^5+28z^7\), and exactly \(24\) of \(128\) initial colorings need both updates. At \(m=8\), the fixed-point count is \(326\) and exactly \(37{,}888\) of \(131{,}072\) inputs require two rounds.

Reproduce with `python3 verify.py` (Python standard library only).

## Relationship to prior work

Zehmakan's majority-diffusion work gives the synchronous majority-with-tie-retention model, general periodicity context, and quantitative results on cycles, but does not give this friendship-graph fixed-point and individual attraction-basin classification. Out and Zehmakan study majority opinion diffusion, elite influence, and modifications of updating on social networks; their graph-wide results do not specify the present exact three-type paired-neighborhood basin structure. Auletta, Ferraioli and Greco consider consensus and coexistence complexity in an asynchronous majority setting rather than these synchronous exact basins. General theorems allowing eventual periods one or two do not imply that all friendship-graph trajectories fix within two rounds. Friendship-graph generating polynomials for unrelated static invariants do not imply dynamical basin counts. The known majority model and general graph facts are not claimed as new here.

## Limitations

This result concerns the deterministic synchronous majority model with tie *retention*, not independent-random tie resolution; changing that rule destroys the pair-freezing argument. It is specific to triangles sharing a single hub, with no edges between distinct peripheral pairs. A probability law for uniformly random *initial* states is not the same as uniform sampling over equilibrium states. The claimed novelty is the explicit fixed-state basin decomposition and its consequences, not a generic stabilization theorem or the definition of friendship graphs. Equivalent formulations in broader Boolean-network or cellular-automaton literature may exist; the comparison cannot establish absolute uniqueness.

## References

1. A. N. Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes*, arXiv:2302.06760v1 (first public version February 14, 2023), https://arxiv.org/abs/2302.06760 .
2. C. Out and A. N. Zehmakan, *Majority Vote in Social Networks: Make Random Friends or Be Stubborn to Overpower Elites*, IJCAI 2021, DOI:10.24963/ijcai.2021/49, https://www.ijcai.org/proceedings/2021/49 .
3. V. Auletta, D. Ferraioli and G. Greco, *Reasoning about Consensus when Opinions Diffuse through Majority Dynamics*, IJCAI 2018, DOI:10.24963/ijcai.2018/7, https://www.ijcai.org/proceedings/2018/7 .
4. American Mathematical Society and zbMATH Open, MSC2020 code 91D30: Social networks; opinion dynamics, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=91D10 .
