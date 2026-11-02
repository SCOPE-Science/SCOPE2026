# Exact three- and four-phase excitation on quadrilateral books

## Finding

For each integer \(k\geq1\), form the labelled quadrilateral book \(B_k\) from two common vertices \(u,v\) and \(k\) disjoint ordered page pairs \((a_i,b_i)\). Its edges are exactly \(uv\), \(ua_i\), \(a_ib_i\), and \(b_iv\), for \(1\leq i\leq k\). Thus \(k\) four-cycles share precisely their common edge \(uv\). Apply synchronous three-state, threshold-one Greenberg–Hastings dynamics: state \(1\) goes to \(2\), state \(2\) goes to \(0\), and state \(0\) goes to \(1\) if and only if some neighbor is in state \(1\).

**Complete recurrence theorem.** Every initial configuration has eventual least period \(1\), \(3\), or \(4\), and reaches its first periodic state by update \(5\). The bound is sharp for every \(k\geq2\); for \(k=1\) the sharp bound is \(4\). The global update map satisfies
\[
F_k^{17}=F_k^5\qquad(k\geq1).
\]

The only fixed configuration is all zero. With labelled vertices and temporal shifts identified but graph automorphisms **not** identified, the exact numbers of primitive period-three and period-four orbits are
\[
Q_3(k)=3^k-2^{k+1}+1,\qquad Q_4(k)=2^{k+1}-2.
\]
Period three first occurs at \(k=2\), and three-cycles first outnumber four-cycles at \(k=4\).

Write \(B_d(k)\) for the number of initial labelled configurations eventually attracted to a cycle of least period \(d\). These attraction-basin populations are exactly
\[
\begin{aligned}
B_1(k)&=3\cdot7^k+6\cdot6^k,\\
B_3(k)&=3\bigl(9^k-2\cdot8^k+7^k\bigr),\\
B_4(k)&=6\bigl(9^k+8^k-7^k-6^k\bigr).
\end{aligned}
\]
They sum to the full configuration-space size \(3^{2k+2}=9^{k+1}\). Consequently, a uniformly random initial configuration has limiting attraction probabilities \(1/3\) for three-cycles and \(2/3\) for four-cycles, while the extinction probability tends to zero as \(k\to\infty\). Although three-cycle **orbits** eventually outnumber four-cycle orbits exponentially, four-cycle **basins** retain twice the limiting mass.

There is also a direct, initial-data decision rule. Define the antisymmetric edge weight
\[
d_X(r,s)=\begin{cases}
1,&X(r)=0,\ X(s)=1,\\
-1,&X(r)=1,\ X(s)=0,\\
0,&\text{otherwise},
\end{cases}
\]
and for each page define its oriented initial circulation
\[
c_i=d_X(u,a_i)+d_X(a_i,b_i)+d_X(b_i,v)+d_X(v,u).
\]
Every \(c_i\) belongs to \(\{-1,0,1\}\). The least eventual period is \(3\) if both a positive and a negative \(c_i\) occur; otherwise it is \(4\) if at least one \(c_i\) is nonzero; otherwise it is \(1\).

## Assumptions and scope

The result concerns deterministic simultaneous updates of the three states \(\{0,1,2\}\), with the open graph neighborhood and excitation threshold exactly one. Every page is labelled and distinct, with no edges beyond those defined above; \(k\ge1\) is arbitrary. The first periodic-entry time of a state \(x\) is the least integer \(t\ge0\) such that \(F_k^t(x)\) lies on a periodic orbit. The period of an orbit is its **least positive** return time. Counts of orbits are divided by their temporal periods, without quotienting any graph symmetry.

## Proof

**1. A finite, parameter-independent recurrence certificate.** Set \(\mathcal A=\{0,1,2\}^2\), the nine possible page-pair states. Given the two hub states \((u,v)\) and the nonempty support \(S\subseteq\mathcal A\) of the initially occurring page types, track a single current image of each initially occurring type. Equal initial page types always evolve identically because each page sees the same two hubs. The next two hubs depend only on whether some tracked page's first coordinate is excited and whether some tracked page's second coordinate is excited; they do not depend on multiplicities. Thus the tracked evolution represents **exactly**, for every \(k\), the evolution of every labelled configuration with initial support \(S\). Explicitly, for each current page pair \((a,b)\), its update is
\[
a'=\begin{cases}2,&a=1,\\0,&a=2,\\\mathbf1_{\{u=1\}\cup\{b=1\}},&a=0,\end{cases}
\qquad
b'=\begin{cases}2,&b=1,\\0,&b=2,\\\mathbf1_{\{v=1\}\cup\{a=1\}},&b=0.\end{cases}
\]
The hubs follow the same rule, using the other hub and the existence of excited first or second page coordinates respectively.

There are exactly \(3^2(2^9-1)=4599\) possible initial triples \((u,v,S)\). The standalone exact-integer checker `code/verify_symbolic.py` enumerates **every** triple, stores the hub states together with the nine-or-fewer tracked page images, and detects exact recurrence of that combined state. It verifies for all \(4599\) cases that the first periodic-entry time is at most \(5\), the least period lies in \(\{1,3,4\}\), and the least period agrees with the stated circulation-sign rule. No arbitrary bound on \(k\) enters this enumeration. In particular, all full configurations satisfy \(F_k^{17}=F_k^5\).

The checker also supplies the complete support-class certificate in `evidence/support_classes.csv`. The numbers of initial triples of support size \(s=1,\ldots,9\), separated by eventual least period, are

| Least period | \(s=1\) | \(s=2\) | \(s=3\) | \(s=4\) | \(s=5\) | \(s=6\) | \(s=7\) | \(s=8\) | \(s=9\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(1\) | 57 | 153 | 225 | 195 | 99 | 27 | 3 | 0 | 0 |
| \(3\) | 0 | 3 | 21 | 63 | 105 | 105 | 63 | 21 | 3 |
| \(4\) | 24 | 168 | 510 | 876 | 930 | 624 | 258 | 60 | 6 |

Their sum is \(4599\). The all-size state count follows also by giving every support \(S\) of size \(s\) the exact labelled-word weight \(\sum_{j=0}^{s}(-1)^{s-j}\binom{s}{j}j^k\); this independent inclusion–exclusion check reproduces all basin formulas. To show sharpness, for one page the four-state trajectory (vertex order \(u,v,a_1,b_1\)) begins \(0001\to0112\to1220\to2000\to0000\), with entry time \(4\). For two pages, the six-state trajectory (order \(u,v,a_1,b_1,a_2,b_2\)) is \(000001\to010012\to120120\to201200\to002000\to000000\), with entry time \(5\). Adding further pages initially of type \((0,0)\) preserves this second support-level trajectory and its entry time, so \(5\) is attained for every \(k\ge2\).

**2. Structural enumeration of periodic orbits.** In a connected graph, no nonzero periodic excitation orbit can leave any vertex permanently resting: a resting vertex next to an infinitely excited vertex would itself become excited. In a primitive period-three or period-four orbit, every vertex is therefore excited exactly once per period, because the local refractory sequence prevents two excitations closer than three updates. Assign each vertex its phase, the time residue at which it is excited. Every vertex must have a neighbor whose phase precedes its own by one unit. In period four, additionally no graph edge can connect phases differing by two, which would cause an excitation one update too early.

For period three, rotate all phases so the common vertex \(u\) has phase \(0\). The local page constraints and the two hub requirements force \(v\) also to have phase \(0\). Every page pair then belongs to exactly the phase list \((1,1),(1,2),(2,1)\); at least one page of type \((1,2)\) and at least one of type \((2,1)\) are required to excite both hubs. The number of such words is \(3^k-2\cdot2^k+1\). There are three global phase shifts and each primitive three-cycle has three states, giving the stated \(Q_3(k)\).

For period four, rotate phases so \(u=0\). The phase of \(v\) cannot be \(2\) by the no-opposite-edge rule. If \(v=0\), the only locally allowed page pair is \((1,1)\), which leaves both hubs unsupported. If \(v=1\), the page pairs are \((1,2)\) and \((3,2)\), with at least one \((3,2)\) needed. If \(v=3\), the page pairs are \((1,0)\) and \((1,2)\), with at least one \((1,2)\) needed. There are two orientation choices, \(2^k-1\) words each, and four global phase shifts. Dividing the resulting periodic-state count by four yields \(Q_4(k)=2(2^k-1)\). Fixed configurations contain no excited or refractory vertex and hence consist only of all zero. The finite certificate in step 1 excludes all other recurrent periods.

**3. Exact basins from the initial circulations.** With hub states fixed, the nine page-pair states divide by their initial face circulation into three classes. For each of the three assignments \(u=v\), exactly one page type has circulation \(+1\), one has \(-1\), and seven have \(0\). For each of the other six hub assignments, three page types have the same nonzero sign, none has the opposite sign, and six have circulation \(0\). The sign decision established in step 1 therefore gives \(B_1(k)=3\cdot7^k+6\cdot6^k\) and \(B_3(k)=3(9^k-2\cdot8^k+7^k)\). Subtracting both from \(9^{k+1}\) gives the displayed \(B_4(k)\). The probability limits follow by dividing by \(9^{k+1}\). The orbit-count crossover follows from \(Q_3(k)-Q_4(k)=3^k-4\cdot2^k+3\): it is negative for \(k=1,2,3\) and positive for every \(k\ge4\).

## Verification

The general, exact certificate uses only Python's standard library. From the package root, run `python3 code/verify_symbolic.py --csv evidence/support_classes.csv`. Its output (also supplied as `evidence/symbolic_output.txt`) checks all \(4599\) support cases, the circulation-sign classification, the uniform entrance bound, and the support-size tally for immediate periodic states and eventual periods. Every line of the CSV is generated deterministically from the displayed transition rule. All assertions passed.

A separate vertex-by-vertex implementation in `code/verify_direct.cpp` constructs the actual labelled graph, evaluates the full configuration map, and decomposes its finite functional graph. Compile with `g++ -std=c++17 -O3 code/verify_direct.cpp -o verify_direct` and run `./verify_direct`. It exhaustively checks all initial states for \(1\le k\le6\), a total of \(5{,}380{,}830\) labelled configurations, against the orbit, basin, and sharp entrance formulas. The six exact outputs are in `evidence/direct_output.txt`. These finite full-state tests corroborate, but do not replace, the all-size support-certificate argument.

## Relationship to prior work

Gravner, Lyu and Sivakoff (arXiv:1610.07320v1, posted 2016-10-24), Theorem 3 and its proof, establish the general cycle-circulation criterion for synchronization and the maximal normalized initial circulation for asymptotic excitation rate on finite connected graphs. This previously established principle is consistent with the present sign rule: the only simple cycles in a quadrilateral book are page cycles of length four (circulation \(c_i\)) and two-page cycles of length six (circulation \(c_i-c_j\)). Thus the maximal excitation rates are \(0\), \(1/4\), and \(1/3\), depending on the sign pattern. The known general theorem alone does not enumerate labelled primitive orbits, prove the global iterate identity, or give the sharp uniform entrance time. The present classification and counting formulas are the additional specific claims.

Doba (2018) likewise gives general asymptotic excitation-rate and winding criteria for deterministic three-state graph excitation, but not the quadrilateral-book orbit enumeration or its basin transition. Work concerning squares glued at a **single vertex**, and work on books whose pages are **triangles**, has different graph structure and does not imply the stated result for edge-glued square pages when \(k\ge2\).

## Limitations

All claims are for the defined edge-glued quadrilateral-book family and the exact three-state synchronous threshold-one rule. No inference about arbitrary finite graphs, higher excitation thresholds, asynchronous updating, or longer refractory chains is asserted. The classification is supported by a fully specified finite-state certificate rather than a purely hand-reduced proof of the bounded-transient assertion. Independent external validation has not been performed. Searches cannot exclude equivalent results in unindexed historical publications.

## References

1. J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, first posted 2016-10-24, especially Theorem 3 and its proof. https://arxiv.org/abs/1610.07320 ; journal version: *Annals of Applied Probability* 28 (2018), 3324–3357, https://doi.org/10.1214/17-AAP1350.
2. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, *Complex Systems* 27 (2018), 101–126, especially Sections 6–7. https://doi.org/10.25088/ComplexSystems.27.2.101 ; lawful full text: https://content.wolfram.com/uploads/sites/13/2018/09/27-2-1.pdf.
3. J. M. Greenberg and S. P. Hastings, *Spatial Patterns for Discrete Models of Diffusion in Excitable Media*, *SIAM Journal on Applied Mathematics* 34 (1978), 515–523, https://doi.org/10.1137/0134040 (model origin).
