# Crown-graph firefly dynamics: sharp transient cutoff and exact period basins

## Finding
For each integer \(n\ge3\), run the synchronous three-color inhibitory firefly map on the crown graph \(\operatorname{Cr}_n=K_{n,n}-M\), formed by deleting a fixed perfect matching from a complete bipartite graph. Every initial state reaches a periodic orbit after at most \(13\) updates. The sharp maximal first-entry time is \(9\) for \(n=3,4\), and \(13\) for every \(n\ge5\). For \(n=3\), the only eventual least periods are \(3\) and \(18\); exactly \(144\) of the \(729\) initial states reach a primitive eighteen-cycle, and there are exactly four such cycles. For every \(n\ge4\), the only eventual least periods are \(3\) and \(4\), both occur, and the exact four-cycle attraction-basin size is

\[
B_4(n)=\frac{(n^2+7n+16)4^n}{8}-(n^2+5n+8)2^n-n(n-1)(n-2)(n-3)+4n(n-1)+8.
\]

All other configurations at \(n\ge4\) eventually have least period three, so \(B_3(n)=9^n-B_4(n)\). In particular \(B_4(n)/9^n\sim (n^2/8)(4/9)^n\). Under uniform independent initial colors, first synchronization at update two has probability tending to one exponentially as \(n\to\infty\).

## Assumptions and scope
The graph has labelled vertex pairs \((u_i,v_i)\), \(1\le i\le n\). Each \(u_i\) is adjacent to each \(v_j\) except \(v_i\); there are no edges within a shore. The state of each vertex is an element of \(\{0,1,2\}\). At each simultaneous update, an element in state \(2\) stays at \(2\) if at least one neighbor is in blinking state \(1\); every other vertex advances by one modulo three. This is the three-color firefly rule in Lyu's original model, not Greenberg–Hastings excitation, cyclic cellular automata, or asynchronous updates.

For an initial labelled state \(x\), let \(\tau(x)\) be the smallest \(t\ge0\) for which \(F^t(x)\) belongs to a periodic orbit of the full labelled-state map. Write \(p(x)\) for its eventual least period. Let \(B_p(n)=|\{x:p(x)=p\}|\), and let \(R_p(n)\) be the number of already periodic labelled states of least period \(p\). Thus each primitive orbit of least period \(p\) has exactly \(p\) states; basin counts include periodic initial states. Synchronization means all vertices share the same color, and its periodic orbit has least period three.

## Proof
**Exact pair-count quotient.** Each matched vertex pair has an ordered color type \((a,b)\in\{0,1,2\}^2\), with \(a\) on the first shore and \(b\) on the second. Let \(c_{ab}\) be the number of pairs of type \((a,b)\), and let \(s_{ab}=\min(c_{ab},2)\). Define \(A=\min(2,\sum_b c_{1b})\) and \(B=\min(2,\sum_a c_{a1})\). A pair of type \((a,b)\) changes as follows: its first color stays at two exactly if \(a=2\) and \(B-\mathbf 1_{b=1}>0\); otherwise it advances modulo three. Its second color stays at two exactly if \(b=2\) and \(A-\mathbf 1_{a=1}>0\); otherwise it advances. The update of the full capped vector \(s\) is determined by this rule: move all occupied pair types to their target types, add their capped multiplicities, and cap each sum at two. The two-capping is exact because a vertex excludes only its own matched partner from the opposite-shore blinking count. Hence the dynamics of \(s\) is a deterministic map on precisely \(3^9=19683\) possible capped vectors (including the empty vector, used solely as an algebraic bookkeeping state).

**Why the finite quotient proves the labelled claim.** Every occupied pair type maps to one pair type at each step. Consequently, the number of occupied types cannot increase. Once the capped vector is on a periodic orbit, this number is constant along the orbit and the mapping of occupied types at each step is bijective. After one complete period of the capped vector, the occupied types are permuted. Every individually labelled pair therefore returns after finitely many further repeats; the full labelled configuration is periodic from the first entry time of the capped vector. Conversely, periodicity of the full labelled configuration implies periodicity of its capped image. Thus the first periodic-entry times agree. The least full period equals the capped period multiplied by the order of the induced permutation after one capped period. This statement remains exact for arbitrarily large multiplicities within a capped type.

**Exhaustive, independently replayable finite certificate.** The included `verify_support.py` defines the capped map and, for each of its \(19683\) states, follows its complete finite orbit to first repetition, then computes the induced permutation on the occupied types. Its complete enumeration gives \(33\) distinct recurrent capped cycles, maximum first-entry time \(13\), and only full periods \(1,3,4,18\), with period one occurring only for the algebraically empty vector. Among nonempty capped states, there are exactly \(19209\) that eventually have full period three, \(449\) with full period four, and \(24\) with full period eighteen. All period-eighteen capped states have three singleton occupied types and no multiply occupied types, so they correspond only to \(n=3\). The program also checks the exact maximal feasible first-entry times \(9\) for \(n=3,4\), and the explicit capped vector \((0,0,2,1,0,0,0,0,2)\) has entry time thirteen and is realizable for all \(n\ge5\) by putting \(n-3\) pairs of color type \((2,2)\). A complete period-four capped orbit exists already at \(n=4\). A full period-eighteen orbit occurs at \(n=3\), with four distinct primitive eighteen-cycles.

**Exact enumeration by exponential generating functions.** For a specified capped vector with exactly \(a\) singleton types and \(b\) types appearing at least twice, the exponential generating function for labelled assignments of the \(n\) matched pairs is \(z^a(e^z-1-z)^b\), since the pair types are distinct labelled boxes. Let \(y=e^z-1-z\). The exhaustive capped-state computation gives this *complete* period-four coefficient polynomial:

\[
\begin{aligned}
P_4(z,y)={}&2(1+z)^2y^4+8(1+z)^3y^3\\
&+(4+36z+68z^2+48z^3+12z^4)y^2\\
&+(52z^2+72z^3+39z^4+8z^5)y\\
&+25z^4+11z^5+2z^6.
\end{aligned}
\]

The standalone `verify_egf.py` checks the following identity *as an identity of integer polynomials in independent indeterminates* \(z\) and \(E\), substituting \(y=E-1-z\), rather than by sampling coefficients:

\[
\begin{aligned}
P_4(z,e^z-1-z)={}&2e^{4z}(1+z)^2-4e^{2z}(1+z)(2+z)\\
&+e^z(8+4z^2-z^4)-2(3z-1)(4z^2+z-1).
\end{aligned}
\]

Extracting \(n![z^n]\) gives the displayed \(B_4(n)\) for every \(n\ge4\). For period eighteen the complete generating polynomial is \(24z^3\), so \(B_{18}(3)=3!\cdot24=144\), with no other sizes possible. The remaining states have period three by the finite certificate. The count \(R_{18}(3)=72\) yields precisely \(72/18=4\) primitive eighteen-cycles. For completeness, the recurrent labelled-state counts for \(n\ge4\) are

\[
\begin{aligned}
R_3(n)&=2\cdot3^n-(3n+6)2^n+6n^2+6n+9,\\
R_4(n)&=2\cdot4^n-(4n+8)2^n+n(n-1)(n-2)(n-3)+8n+8.
\end{aligned}
\]

These are obtained from the recurrent capped coefficient tables in `verify_support.py` and their exact polynomial identities in `verify_egf.py`; the primitive orbit counts are \(R_3(n)/3\) and \(R_4(n)/4\). The exceptional size three has \(R_3(3)=3\), not the extension of the displayed first expression.

**Generic two-step synchronization.** If every one of the nine ordered pair types occurs at least twice initially, every vertex has at least one blinking neighbor unless that same vertex is blinking; hence the first update changes all type-two vertices to type two and all others to their successors, and the second update places every vertex at two. In more direct terms, each shore has multiple blinking vertices after both the initial and first step; both shore updates yield the constant color-two state at time two. (This property is also checked by the exact quotient.) Such a configuration is not synchronized at times zero or one. Under independent uniform initial pair colors, a union bound gives

\[
\Pr(\tau_{\mathrm{sync}}\ne2)\le 9\bigl[(8/9)^n+(n/9)(8/9)^{n-1}\bigr],
\]

which tends to zero exponentially. The period-four basin fraction follows directly from the exact formula, since every other term is exponentially smaller than \(n^2 4^n/8\).

## Verification
Run `python3 verify_support.py` and `python3 verify_egf.py` with the Python standard library, and `g++ -O2 -std=c++17 verify_vertices.cpp -o verify_vertices && ./verify_vertices`. The first script exhausts all \(19683\) capped states, including their eventual full labelled periods, first-entry times, symbolic counting weights, and size constraints. The second checks the full period-four generating-function identity with integer coefficients. The independent C++ checker implements the rule on individual vertices without using the capped-state representation and exhausts all labelled configurations for \(2\le n\le7\), a total of \(5,380,830\) states. Embedded text outputs record the actual successful executions.

The finite quotient is a size-uniform exact reduction, not a sample of graph sizes. Direct vertex enumeration is an additional cross-check and is not the reason the statements hold for arbitrary \(n\).

## Relationship to prior work
The underlying inhibitory firefly map and general synchronization questions are due to Lyu's 2014 preprint, whose publicly accessible full text states the precise update rule and proves results mainly for paths and trees. The 2016 tree analysis addresses time complexity on trees. Neither inspected theorem yields the period-eighteen exception or exact period-basin formulas on the matched-deleted complete bipartite family. General results about three-state Greenberg–Hastings excitation, cyclic cellular automata, and binary parity dynamics employ different transition maps and cannot be substituted into this claim. General finite-state periodicity alone supplies no size-independent bound, exact basin count, or orbit census.

## Limitations
The classification applies only to the stated synchronous three-color inhibitory rule, with exact deletion of a perfect matching and \(n\ge3\). The time \(\tau\) means first entry to any periodic orbit; it is not time to synchronization for a nonsynchronizing trajectory. The probability estimate uses uniform independent initial colors. The proof relies on a finite exhaustive certificate with independently readable code and an algebraic identity. No claim is made about other graph families, different firefly periods, stochastic versions, or priority against inaccessible or unindexed literature. Independent expert audit has not been performed.

## References
1. Hanbaek Lyu, *Synchronization of finite-state pulse-coupled oscillators*, initial arXiv release 2014-07-04, arXiv:1407.1103, https://arxiv.org/abs/1407.1103 . The author's full manuscript is also accessible at https://www.researchgate.net/publication/263699436_A_Self-stablizing_Cellular_Automata_Model_For_Pulse-coupled_Biological_Oscillators .
2. Hanbaek Lyu, *Time complexity of Synchronization of discrete pulse-coupled oscillators on trees*, arXiv:1610.00837, 2016-10-04, https://arxiv.org/abs/1610.00837 .
3. `verify_support.py`, `verify_egf.py`, and `verify_vertices.cpp`, included here as standalone exact finite-state, symbolic algebra, and direct-dynamics checks, respectively.
