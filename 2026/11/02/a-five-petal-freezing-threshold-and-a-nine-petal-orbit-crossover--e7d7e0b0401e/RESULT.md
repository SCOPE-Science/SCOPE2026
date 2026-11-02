# A five-petal freezing threshold and a nine-petal orbit crossover in firefly friendship graphs

## Finding
For every integer \(m\ge1\), let \(F_m=K_1\vee(mK_2)\) be the labelled friendship graph consisting of \(m\) triangles with one common hub. In the synchronous five-color firefly cellular automaton, the only eventual least periods are five and six. Writing
\[
U_m=\sum_{j=0}^{5}(-1)^j\binom5j(5-j)^m,
\]
where \(U_m\) is the number of onto maps from \(m\) labelled petals to five prescribed colors, the exact number of primitive periodic orbits modulo temporal rotation is
\[
\boxed{N_5(m)=1+\frac25U_m,\qquad N_6(m)=4^m-2^m.}
\]
An additional, nonsynchronous period-five orbit exists if and only if \(m\ge5\). For \(1\le m\le8\), six-cycles outnumber five-cycles; for every \(m\ge9\), five-cycles outnumber six-cycles.

Every initial condition first becomes periodic within exactly the sharp size-dependent worst-case bound
\[
T_m=\begin{cases}10,&m=1,\\28,&m=2,3,\\32,&m=4,\\33,&m\ge5.\end{cases}
\]
Consequently the update map \(F\) obeys \(F^{T_m+30}=F^{T_m}\), and no smaller first-entry bound is valid.

## Assumptions and scope
The graph has one hub \(h\) and \(m\) labelled disjoint pairs \((u_i,v_i)\). Each pair is an edge, and both endpoints connect to \(h\); distinct petals have no edges between them. Vertex colors belong to \(\{0,1,2,3,4\}\). All vertices update simultaneously. A vertex advances by one modulo five unless its color is \(3\) or \(4\) and it has a neighbor colored \(2\), in which case it holds. Every finite coloring is allowed, including the nonsynchronous ones. A primitive orbit is counted once under cyclic shifts in time, never modulo graph automorphisms.

## Proof
**1. Exact finite-support factor.** The unordered color type of a petal is one of the fifteen pairs \((a,b)\), \(0\le a\le b\le4\). Let \(S\) be the nonempty set of petal types currently present; let \(H\in\{0,1,2,3,4\}\) be the hub color. There are exactly \(5(2^{15}-1)=163835\) possible reduced states. Define \(g(c,e)=c\) when \(c>2\) and \(e\) is true, and \(g(c,e)=c+1\pmod5\) otherwise. The exact update is
\[
H'=g(H,\exists(a,b)\in S:\ a=2\ \text{or}\ b=2),
\]
\[
S'=\left\{\operatorname{sort}\big(g(a,H=2\ \text{or}\ b=2),g(b,H=2\ \text{or}\ a=2)\big):(a,b)\in S\right\}.
\]
This is a factor of the fully labelled graph dynamics: each petal changes according to its own two colors and the hub color, and the hub sees blinking exactly when one represented type contains color two. Thus the factor is valid for arbitrarily many petals and no petal multiplicity can alter the transition.

**2. Exhaustive finite lemma.** The attached self-contained program `verify_fca5_friend.py` constructs each of the \(163835\) nonempty reduced states and exhaustively resolves the finite functional graph. Its complete recurrent-state classification is:

| Reduced least period | Number of reduced recurrent states | Number of present petal types |
|---|---:|---:|
| \(1\) | \(2\) | \(5\) |
| \(5\) | \(5\) | \(1\) |
| \(6\) | \(6\) | \(1\) |
| \(6\) | \(12\) | \(2\) |
| \(6\) | \(6\) | \(3\) |

The two reduced fixed states have hub color three or four and support precisely the five monochromatic petal types \((c,c)\). The reduced period-five orbit has equal colors at every vertex. The twenty-four reduced six-cycle states consist of four distinct reduced six-cycles. The program verifies that each *ordered* petal pair returns to its original orientation after six updates along every reduced six-cycle. This last check is essential: using unordered types alone could otherwise conceal a doubled microscopic period. The two reduced fixed states instead rotate every monochromatic petal color through the five colors while the hub remains fixed. Therefore every full configuration above a reduced recurrent state is already periodic, with actual period five or six as specified. No full coloring can become periodic earlier than its projected reduced coloring does.

**3. Counts by weighted surjections.** A reduced support of unordered petal types \(S\) has \(\sum_{T\subseteq S}(-1)^{|S|-|T|}(\sum_{p\in T}w_p)^m\) fully labelled realizations, where \(w_{(a,a)}=1\) and \(w_{(a,b)}=2\) when \(a<b\), counting endpoint orientation. For reduced six-cycle states, the exact complete list of weight multisets is \(6\) copies of \((2)\), \(12\) copies of \((1,2)\), and \(6\) copies of \((1,1,2)\). Inclusion–exclusion consequently yields \(6(4^m-2^m)\) recurrent microscopic states, each with least period six, giving \(N_6(m)=4^m-2^m\).

The five synchronous periodic configurations contribute one period-five orbit. In each of the two reduced fixed states, every petal has equal endpoint colors, and all five colors must occur. There are \(U_m\) choices of the labelled petal colors for each hub value, giving \(2U_m\) further period-five states and \(2U_m/5\) orbits. Such orbits exist precisely when \(m\ge5\). They are nonsynchronous because the hub is permanently held and the page colors circulate.

**4. Crossover and sharp entry time.** The exact formulas give \(N_6(m)>N_5(m)\) for \(1\le m\le8\), and \(N_5(9)=333649>261632=N_6(9)\). Every surjective coloring extends to at least five surjective colorings by adjoining another labelled petal, so \(U_{m+1}\ge5U_m\). Meanwhile \(N_6(m+1)<5N_6(m)\) for \(m\ge2\). This proves that the crossover persists for every \(m\ge9\).

The finite factor's maximum first-periodic-entry time among support sets of at most \(m\) petal types is \(10,28,28,32,33\) for \(m=1,2,3,4,5\), and it is \(33\) thereafter. Every allowed reduced support can be realized by \(m\) labelled petals whenever its cardinality is at most \(m\). Since exact periodic entry lifts between the factor and the full states, these are attained bounds, not merely upper bounds. The standalone program exhaustively verifies both the maxima and the finite functional graph.

## Verification
Run `python3 verify_fca5_friend.py` with standard Python. The program independently updates fully labelled graphs with one, two and three petals, checking \(81375\) microscopic initial colorings against the reduced dynamics, return times and eventual periods. It also classifies the entire \(163835\)-state nonempty support factor and checks each recurring six-cycle's ordered-petal monodromy. The recorded successful output appears in `verify_fca5_friend.out`. Finite microscopic tests corroborate the general proof; the infinite-family conclusion follows from the exact finite factor, not from extrapolating the small cases.

## Relationship to prior work
Lyu's 2014 preprint introduces and investigates finite-state pulse-coupled inhibitory oscillators, with synchronization theorems on paths and trees. His 2016 work gives sharp synchronization-time and non-synchronization structure on trees. These establish the model and motivating dynamical question but do not state the present exact friendship-graph recurrent orbit census in the accessible material. Complete multipartite network results concern a different graph family: \(F_m\) for \(m\ge2\) is not complete multipartite, because nonadjacency is not transitive between distinct petals and the ends of a single petal. The triangle \(F_1\) alone is a previously studied special graph; novelty is not asserted for that isolated instance.

## Limitations
The conclusion is for five colors with blinking color two, synchronous updates, labelled petals and the stated graph family. It does not classify other color counts or other triangular cacti. Historical full-text coverage remains a residual risk: attempts to obtain the two most relevant early papers through open preprint routes did not yield readable full texts, and authorized institutional retrieval reported disconnected access. Their accessible abstracts and summaries were inspected, but those snippets do not justify any whole-paper exclusion. 

## References
1. Hanbaek Lyu, *Synchronization of finite-state pulse-coupled oscillators*, arXiv:1407.1103, first public 2014-07-04. https://arxiv.org/abs/1407.1103
2. Hanbaek Lyu, *Time complexity of synchronization of discrete pulse-coupled oscillators on trees*, arXiv:1610.00837, first public 2016-10-04. https://arxiv.org/abs/1610.00837
