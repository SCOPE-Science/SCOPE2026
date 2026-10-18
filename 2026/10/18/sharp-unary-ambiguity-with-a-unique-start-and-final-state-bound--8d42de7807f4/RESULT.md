# Sharp unary ambiguity with a unique start and final state: bound and extremizer rigidity

## Finding
For every integer \(n\ge3\), an \(n\)-state, trim, epsilon-free, finitely ambiguous nondeterministic automaton over the unary alphabet \(\{a\}\), with exactly one initial state and exactly one accepting state, has degree of ambiguity at most \(2^{n-2}\). This is attained.

More precisely, equality holds **if and only if**, after renaming the states, there is a total order \(q_0<q_1<\cdots<q_{n-1}\), with the unique start \(q_0\) and unique final state \(q_{n-1}\), in which the transition relation consists of every forward arc \(q_i\xrightarrow{a}q_j\) for \(i<j\), together with **exactly one** self-loop, either at \(q_0\) or at \(q_{n-1}\). No other transitions occur. For a fixed labeled set with distinct designated start and final states, there are exactly \(2(n-2)!\) extremizers.

In either extremizer, exactly \(2^{n-2}\) runs accept \(a^m\) for every \(m\ge n-1\), and no word has more accepting runs.

## Assumptions and scope
An automaton is a directed graph with at most one edge per ordered pair of states, all edges labeled \(a\). A run is a directed walk; the empty run is allowed. "Trim" means every state is reachable from the unique initial state \(s\) and can reach the unique final state \(t\). The degree of ambiguity is \(\sup_{m\ge0}r_m\), where \(r_m\) counts directed walks of length \(m\) from \(s\) to \(t\). Finite ambiguity means this supremum is finite. The endpoints may a priori coincide; the conclusion determines that extremizers necessarily have distinct endpoints. All graph edges are ordinary Boolean transitions, not parallel transitions, weights, or epsilon transitions.

## Proof
**Lemma 1 (cyclic-component structure).** In the trim graph of a finitely ambiguous unary automaton, every strongly connected component containing a directed cycle is exactly a directed simple cycle (a singleton with its self-loop is allowed). Moreover, no accepted walk visits two different cyclic components.

Indeed, if a strongly connected component had two distinct internal outgoing edges at a state, one could complete each to a nonempty closed walk based at that state. Their lengths have a common positive multiple, producing two different closed walks of the same length. Iterating this equal-length choice yields arbitrarily many accepted walks at a common length, using trim access and exit paths. Thus each vertex in a cyclic component has exactly one outgoing edge internal to that component. Strong connectivity forces a single directed cycle. If a path passes through two cyclic components with respective cycle lengths \(p,q\), an extra length \(hpq\) can be distributed between the cycles in \(h+1\) ways, again contradicting bounded ambiguity. This proves the lemma.

Consequently a successful run passes through either no cyclic component or exactly one such component. The condensation graph is a directed acyclic graph, and the run visits each noncyclic (singleton) component at most once.

**Case A: neither \(s\) nor \(t\) is cyclic.** Let \(a\) denote the number of states in all cyclic components, and let \(r=n-a-2\) be the number of other noncyclic states apart from \(s,t\). Associate to each successful run the subset \(S\) of these \(r\) states that it visits. Within a fixed \(S\), there is at most one run avoiding all cyclic components: the condensation order fixes every visited vertex. For a fixed cyclic component \(C\) of size \(c\), and fixed input length \(m\), there are at most \(c\) runs through \(C\) visiting exactly \(S\): the position of \(C\) among the ordered noncyclic vertices is forced by the condensation order; after choosing an entry state in \(C\), the unique internal directed cycle determines the entire segment because its length is \(m-(|S|+2)\), counting a single visit through \(C\). Thus there are at most \(1+\sum_C |C|=1+a\) runs for each subset \(S\), and hence
\[
r_m\le(1+a)2^{n-a-2}\le 2^{n-2},
\]
using \(1+a\le2^a\) for nonnegative integers \(a\).

Equality is impossible in this case for \(n\ge3\). If \(a\ge2\), the last inequality is strict. If \(a=1\), equality would require, for every subset \(S\), both the run avoiding the unique looped vertex and the run visiting it, but these have different minimum lengths: respectively \(|S|+1\) and \(|S|+2\). More directly, any run through the looped vertex has length at least \(|S|+2\), while the unique path avoiding it has length exactly \(|S|+1\); they cannot both occur for one fixed \(m\). If \(a=0\), any successful run of length \(m\) visits exactly \(m-1\) internal vertices; the count is at most \(\binom{n-2}{m-1}<2^{n-2}\), with the usual zero convention. The strict inequality holds because \(n-2\ge1\).

**Case B: at least one of \(s,t\) lies in a cyclic component.** They cannot lie in distinct cyclic components by Lemma 1. If both lie in the same cyclic component, every accepted run stays in it; for each length there is at most one run because a directed cycle is deterministic. This is below \(2^{n-2}\).

Otherwise exactly one endpoint lies in a cyclic component \(C\) of size \(c\). By trimness and Lemma 1, there is no other cyclic component. All other \(r=n-c-1\) states are noncyclic vertices distinct from the opposite endpoint. Fix a subset \(S\) of these vertices and a length \(m\). There is at most one accepted run that visits exactly \(S\): the noncyclic vertices are traversed in condensation order, and the number of steps within \(C\) is fixed by \(m\) and \(|S|\); a directed cycle then forces the entire internal segment from its known initial endpoint (if \(s\in C\)) or known terminal endpoint (if \(t\in C\)). Hence
\[
r_m\le 2^{n-c-1}\le 2^{n-2}.
\]
If \(c\ge2\), the last inequality is strict. Thus equality forces \(c=1\), so exactly one endpoint has a self-loop.

**Rigidity in the equality case.** Let \(c=1\). Equality at some input length means every one of the \(2^{n-2}\) subsets of the remaining noncyclic internal states occurs as the visited set of a successful run. In particular, for each pair of different internal states the run visiting both fixes a common strict order in the condensation DAG; it cannot reverse that order in another run, since the condensation graph is acyclic. Thus all internal vertices have one common total order. Every subset must be achievable, including the empty subset and all one- and two-element subsets. Therefore every forward edge between consecutive or nonconsecutive vertices in the combined order \(s<\cdots<t\) is present: selecting precisely the intervening subset of length zero between any two ordered vertices requires their direct edge. No backward edge or additional loop can occur, since it would create a further cyclic component or a larger cyclic component, contradicting Lemma 1 and the singleton endpoint component. The only possible graph is the full strict ordered DAG with the unique loop at \(s\) or \(t\).

**Attainment and enumeration.** Conversely take this graph and choose a subset \(S\) of the \(n-2\) internal vertices. It specifies precisely one increasing path from \(s\) to \(t\), of length \(|S|+1\). For each \(m\ge n-1\), padding at the unique endpoint loop for \(m-(|S|+1)\) steps produces exactly one accepting run of length \(m\). All accepting runs arise this way, so their number is \(2^{n-2}\) for every such \(m\). Choosing the looped endpoint in two ways and ordering the \(n-2\) internally labeled vertices in \((n-2)!\) ways yields exactly \(2(n-2)!\) distinct labeled extremizers. This completes the proof.

## Verification
The standalone `verify.py` enumerates **every** Boolean transition graph on \(2\), \(3\), and \(4\) labeled vertices with start state \(0\) and final state \(n-1\). The finite-ambiguity check independently computes useful vertices, cyclic strongly connected components, and comparability of cyclic components. For finitely ambiguous graphs, dynamic programming counts accepting walks through length \(30\). It obtains maxima \(1,2,4\) and precisely \(2,4\) labeled extremizers at \(n=3,4\), matching the theorem. It separately enumerates every labeled extremizer through \(n=10\) and checks its ambiguity. These computations support the stated boundary cases, but the bound and rigidity for every \(n\ge3\) follow from the preceding proof, not from the finite experiment.

Reproduce with the standard Python interpreter: `python verify.py`. The included `computation.txt` contains the output observed when the packaged checker was executed.

## Relationship to prior work
Kiefer, Mazowiecki, Ryzhikov, and Wiśniewski (2026) establish a general exponential bound for finite ambiguity of NFAs and explicitly mention the unary lower bound \(2^{n-2}\). That lower bound alone does not provide a matching universal upper bound within the **single-initial, single-final unary** model, nor any equality classification. Their full paper has been examined for these implications.

Weber and Seidl (1991), particularly the numerical comparison in their Table 1 and their discussion of ambiguity growth, provide foundational bounds for unary finite automata with more general choices of initial and final states; Table 1 records the larger worst-case \(2^{n-1}\) in that broader model. The broader-model upper bound neither implies the sharper singleton-endpoint bound nor forces a unique extremal directed graph. Their full article was inspected. Earlier equivalent treatments may remain undetected.

Drabik, Ganardi, and collaborators (2025) address algorithmic ambiguity detection and related complexity rather than the exact equality structure identified here.

## Limitations
The result concerns unary epsilon-free **Boolean** NFAs, one start and one final state, trimness, and finite ambiguity. It does not apply to weighted or multigraph transitions, arbitrary alphabets, multiple initial/final states, or polynomially/inherently ambiguous machines. A source with an equivalent formulation under finite digraph path counting remains a possible priority risk. Independent scientific validation has not been performed.

## References
1. S. Kiefer, F. Mazowiecki, A. Ryzhikov, and A. Wiśniewski, *Stronger bounds on the degree of ambiguity of finite automata*, arXiv:2610.08525 (first submitted 2026-10-06). https://arxiv.org/abs/2610.08525
2. A. Weber and H. Seidl, *On the degree of ambiguity of finite automata*, Theoretical Computer Science 88 (1991), 325–349. https://doi.org/10.1016/0304-3975(91)90381-B ; lawful author-posted full text: https://fmazowiecki.github.io/course/WS91.pdf
3. Drabik and collaborators, *Fine-Grained Complexity of Ambiguity Problems on Automata and Directed Graphs* (2025), arXiv:2501.14725. https://arxiv.org/abs/2501.14725
