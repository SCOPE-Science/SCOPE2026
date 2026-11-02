# Exact first-entry layer laws for Greenberg–Hastings excitation on bridged cliques

## Finding
Let \(B_{a,b}\), for integers \(a,b\ge2\), be the graph obtained by joining a distinguished vertex of \(K_a\) to a distinguished vertex of a vertex-disjoint \(K_b\) by a single edge. Under synchronous three-state threshold-one Greenberg–Hastings evolution, every initial state reaches a periodic configuration by time six. The only eventual periods are one and three; the only fixed state is all resting. The bound is sharp for every \((a,b)\ne(2,2)\), and is five for \((a,b)=(2,2)\).

The exact number \(N_{p,t}(a,b)\) of labelled initial configurations having least eventual period \(p\) and first periodic-entry time \(t\) is as follows. Write
\[
X=2^a,\quad Y=2^b,\quad U=3^a,\quad V=3^b,\quad A=3^{a-1}-2^a+1,\quad B=3^{b-1}-2^b+1.
\]
The extinction layers are
\[
\begin{array}{c|l}
t&N_{1,t}\\\hline
0&1\\
1&XY-1\\
2&(5XY-4X-4Y+2)/2\\
3&(6XY-9X-9Y+12)/2\\
4&(2XY-X-Y)/2\\
5&(3XY-4X-4Y+4)/2
\end{array}
\]
with \(N_{1,t}=0\) for \(t\ge6\). The recurrent three-cycle layer is \(N_{3,0}=9AB+3(A+B)\). For \(1\le t\le6\), writing \(j=\min\{t,7-t\}\),
\[
N_{3,t}=\frac{2j-1}{6}(UY+XV)-\frac j3(U+V)-(2j-1)XY+\frac{4j-1}{2}(X+Y)-2j,
\]
and all other layers vanish. In particular \(N_{3,t}=N_{3,7-t}\) for \(1\le t\le6\).

The exact number of primitive three-cycle orbits is
\[
3AB+A+B.
\]
The basin of the unique fixed state has size \(9(X-1)(Y-1)\), and its probability from an independent uniform initial three-coloring is
\[
9(1-2^{-a})(1-2^{-b})(2/3)^{a+b}.
\]
Every remaining initial configuration reaches a three-cycle; thus the period-three attraction probability tends to one exponentially when both clique sizes tend to infinity.

## Assumptions and scope
Vertices carry colors \(0\) (resting), \(1\) (excited), \(2\) (refractory). All vertices update simultaneously. Colors \(1\) and \(2\) change unconditionally to \(2\) and \(0\), respectively; a resting vertex changes to \(1\) precisely when it has at least one neighbor of color \(1\), otherwise remains \(0\). The neighborhood is open and the interclique connection is a single undirected edge. All colors and vertices are labelled; every one of the \(3^{a+b}\) initial states is counted once. First-entry time is the smallest nonnegative \(t\) for which the configuration at time \(t\) is periodic. A cycle of length three counts three distinct recurrent configurations but one orbit.

## Proof
**Finite-universe reduction.** Denote bridge endpoints by \(h\) and \(k\). In each clique record the numbers of nonbridge vertices in colors \(0,1,2\), but truncate each number by \(c(r)=\min(2,r)\). Each compressed state consists of two hub colors and two triples of values in \(\{0,1,2\}\). A nonbridge resting vertex sees an excited neighbor if and only if its hub is excited or some other nonbridge vertex is excited. Since the vertex itself is resting, it does not affect the color-one count. A resting bridge endpoint additionally sees the other bridge endpoint. Thus, for a hub \(h\in\{0,1,2\}\), opposite hub \(k\), and capped nonbridge counts \((z,o,r)\), the next capped nonbridge triple is
\[
\begin{cases}(r,z,o),&o>0\ \text{or}\ h=1,\\
(\min\{2,r+z\},0,o),&o=0\ \text{and}\ h\ne1,
\end{cases}
\]
where the first line also caps \(r\) if needed. The hub changes from \(h=0\) to \(1\) iff \(o>0\) or \(k=1\), and otherwise follows \(1\to2\to0\). This finite transition preserves the exact class of every labelled state because truncation commutes with addition of disjoint color classes.

There are exactly \(9(3^3-1)^2=6084\) compressed states with at least one nonbridge vertex on each side. The standalone `finite_certificate.py` exhaustively evaluates their explicit transition and verifies that the sixth iterate is either all resting or satisfies the **rotation condition**: every zero-colored vertex sees a one-colored neighbor. Once that condition holds, all vertices advance through \(0\to1\to2\to0\) every round, and the condition persists. Hence there are no other periods, and the first-entry bound is six. The same finite computation verifies that the compressed first-entry time equals the labelled first-entry time: each compressed periodic state is either all resting or rotation-compatible. Because an actual periodic state necessarily has periodic compressed data, no earlier hidden periodicity is possible.

**Recurrent configurations.** A nonzero recurrent configuration rotates every color globally. For a clique whose distinguished hub has color \(h\), every nonhub vertex of color \(c\) requires a neighbor of color \(c+1\) modulo three. Its nonhub color-pattern is therefore either (i) contains both \(h+1\) and \(h-1\), or (ii) consists entirely of \(h-1\), with the opposite hub of color \(h+1\). Both sides cannot be of type (ii), because the demanded hub-color differences are incompatible. For \(a-1\) labelled nonhubs, type (i) has \(A=3^{a-1}-2^a+1\) patterns; similarly the other side has \(B\). Thus the recurrent three-cycle configurations number \(9AB+3A+3B\), and dividing by three gives \(3AB+A+B\) orbits.

**Exact first-entry counts.** For each capped triple \(c=(c_0,c_1,c_2)\), its exponential generating function for labelled nonhub colorings is
\[
W_c(z)=\prod_{i=0}^{2}e_{c_i}(z),\qquad e_0(z)=1,\quad e_1(z)=z,\quad e_2(z)=e^z-1-z.
\]
Thus the number of nonhub assignments with \(r\) vertices and cap triple \(c\) is \(r![z^r]W_c(z)\). For each of the 6084 compressed hub/triple classes, let \(p(c)\) and \(t(c)\) be its exact least eventual period and first-entry time, found by the explicit finite transition. Then the bivariate generating function for each layer is the **finite, size-independent identity**
\[
\mathcal W_{p,t}(z,w)=\sum_{\substack{h,k\in\{0,1,2\}\\c,d\in\{0,1,2\}^{3}\\(h,k,c,d)\text{ admissible}\\p(c,d,h,k)=p,\ t(c,d,h,k)=t}}W_c(z)W_d(w),
\]
and \(N_{p,t}(a,b)=(a-1)!(b-1)![z^{a-1}w^{b-1}]\mathcal W_{p,t}\). `finite_certificate.py` establishes all thirteen displayed layer formulas by *exact formal polynomial equality* after substituting \(E=e^z\), \(F=e^w\). Specifically, all terms involving \(z\) and \(w\) cancel, leaving only the exponential bases corresponding to \(1\), \(2^a\), and \(3^a\) on each shore. This verifies the identities for **all** positive nonhub sizes, not merely for sampled graph orders. Summing the six extinction layers yields \(9(2^a-1)(2^b-1)\), consistent with subtracting all period-three layers from \(3^{a+b}\).

**Sharpness.** If \(a\ge2\) and \(b\ge3\), initially color hub \(h\) zero, hub \(k\) two, all first-clique nonhubs one, and the second-clique nonhubs with at least one zero and at least one one. Their capped transition has first-entry time exactly six, irrespective of the nonzero multiplicities. The symmetric construction applies if \(a\ge3,b=2\). For \(a=b=2\), the initial colors \((h,\text{nonhub A},k,\text{nonhub B})=(0,0,0,1)\) reach the fixed configuration for the first time at time five. The finite certificate also establishes no first-entry times above five in this smallest graph.

## Verification
The standalone `finite_certificate.py` uses only the Python standard library. It enumerates 6084 compressed classes, checks the global six-step bound and period classification, and verifies thirteen layer generating functions as **formal polynomial identities** using exact rational arithmetic. Run with `python3 finite_certificate.py`; its reproduced standard output is provided in `finite_output.txt`.

`independent_direct.cpp` does not use capped counts or formal generating functions. It directly updates individual vertex colors, enumerates complete state spaces for twelve pairs of clique orders up to \((6,6)\), and checks all exact layer counts, periods and first-entry times. Run with `g++ -O3 -std=c++17 independent_direct.cpp -o check && ./check`; its reproduced output is `direct_output.txt`. Both computations completed successfully. Direct finite enumeration is corroboration; the all-size formulas follow from the symbolic generating-function identity.

## Relationship to prior work
Gravner, Lyu and Sivakoff (2016), Theorem 3, characterize synchronization for arbitrary finite graphs through the initial coloring's cycle integrals and give a general diameter-scale synchronization statement. For bridged cliques, that theorem already implies the basic criterion that extinction occurs exactly when neither clique initially contains all three colors, and the corresponding aggregate extinction probability. **Those implications are not claimed as new.** Doba (2018) also establishes a general maximum-cycle-density criterion for deterministic Greenberg–Hastings dynamics. The contribution here is the **complete first-periodic-entry layer distribution**, the exact count and structural description of bridge-supported recurrent three-cycles, the six-step sharp bound, and the non-obvious palindromic period-three entry profile. The family differs from matched-clique Cartesian products and complete bipartite graphs, for which other specialized dynamical counts exist.

## Limitations
The claim is restricted to threshold one, three colors, synchronous updates, and exactly one bridge between two cliques of orders at least two. It neither addresses thresholds above one nor irregular intracluster edges. Prior general theorems explain the extinction-versus-survival dichotomy; novelty concerns refined finite-time and orbit counts. The generating-function proof uses a finite exhaustive symbolic computation whose source is provided and is independently checked on finite labelled graphs, not an external formal proof assistant. The source searches performed are not a proof of universal priority.

## References
1. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, first public version 2016-10-24, especially Theorem 3 and Sections 2 and 4. https://arxiv.org/abs/1610.07320.
2. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems **27** (2018), 101–126, DOI:10.25088/ComplexSystems.27.2.101, especially Sections 3, 6–8. https://wpmedia.wolfram.com/sites/13/2018/09/27-2-1.pdf.
3. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, first public version 1993-03-22. https://arxiv.org/abs/patt-sol/9303002.
