# Three-state excitation on complete bipartite graphs: a five-step cutoff and exact period basins

## Finding
For every pair of integers \(a,b\ge2\), consider synchronous three-state Greenberg–Hastings excitation with contact threshold two on the labelled complete bipartite graph \(K_{a,b}\). Let \(B_d(a,b)\) be the number of labelled initial states whose eventual least temporal period equals \(d\). Define, for \(n\ge4\),
\[
\begin{aligned}
P_n&=(n+2)2^{n-1}-2n^2-2n-2,\\
Q_n&=n(n-1),\\
H_n&=3^n-3\cdot2^n-3n2^{n-1}+3(n^2+n+1),\\
U_n&=2^n-2n-2.
\end{aligned}
\]
For \(n=2,3\), set \(P_n=Q_n=H_n=U_n=0\). Then every initial state is periodic after at most five updates, the only eventual least periods are \(1,3,4\), and the complete period-stratified basin sizes are
\[
\begin{aligned}
B_3(a,b)&=H_aH_b,\\
B_4(a,b)&=6P_aP_b+3(P_aQ_b+Q_aP_b)+2Q_aQ_b\\
 &\quad +(3P_a+Q_a)H_b+H_a(3P_b+Q_b),\\
B_1(a,b)&=3^{a+b}-B_3(a,b)-B_4(a,b).
\end{aligned}
\]
The only fixed point is the all-rest state. A primitive four-cycle exists if and only if \(a,b\ge4\), while a primitive three-cycle exists if and only if \(a,b\ge6\). The exact numbers of primitive cycle **orbits** are \(H_aH_b/3\) of period three and \(U_aU_b/2\) of period four.

The sharp maximum first entry time into a periodic orbit is three for \((a,b)=(2,2)\), four when \(\min(a,b)=2\) and \(\max(a,b)\ge3\) or when \((a,b)=(3,3)\), and five in all remaining cases. In particular the full map satisfies \(F^{17}=F^5\). Under independent uniform initial colors, \(B_3(a,b)/3^{a+b}\to1\) as \(\min(a,b)\to\infty\).

## Assumptions and scope
Every vertex has a state in \(\{0,1,2\}\), with \(0\) resting, \(1\) excited and \(2\) refractory. In each simultaneous update, \(1\mapsto2\) and \(2\mapsto0\); a resting vertex becomes excited if and only if at least **two distinct neighbors** were excited in the preceding configuration, and otherwise stays resting. There are no loops, randomness, external stimuli or asynchronous steps. Vertices within a shore are individually labelled. The first-entry time of an initial configuration is the smallest nonnegative \(t\) at which its configuration is already periodic. A period basin counts initial configurations, not primitive orbit objects. Both shores must have at least two vertices.

## Proof
**Exact capped-state factor.** For one shore, let \(p=(p_0,p_1,p_2)\in\{0,1,2\}^3\) record the multiplicities of its *initial* colors, clipped at two: \(0\) means absent, \(1\) means exactly one, \(2\) means at least two. Because the shore has at least two vertices, exactly 23 profiles (those with \(p_0+p_1+p_2\ge2\)) are possible across all shore sizes. Vertices starting with a given color on the same shore remain synchronized with one another forever. Track the present colors \(c_{L,i}(t),c_{R,i}(t)\) of the three initial color classes on the left and right, initially \(c_{L,i}(0)=c_{R,i}(0)=i\). Unoccupied classes are omitted from state comparisons.

The capped current excited count on the left is exactly
\[
r_L(t)=\min\left\{2,\sum_{i=0}^{2}p_i\mathbf1_{\{c_{L,i}(t)=1\}}\right\};
\]
likewise \(r_R(t)\) using profile \(q\). For every occupied class, the next color is \(c+1\pmod3\) when \(c\in\{1,2\}\), and is \(\mathbf1_{\{r_{\mathrm{opposite}}(t)=2\}}\) when \(c=0\). Replacing any actual multiplicity at least two by two does not affect these tests, so the tagged evolution is **exact**, not an approximation. It contains \(23^2=529\) possible initial profile pairs and determines actual labelled temporal periods and transients, rather than merely periods of aggregate color counts.

**Exhaustive finite classification.** Apply the explicit tagged recurrence to all 529 pairs until the full occupied-class color signature repeats. Of these pairs, 476 have eventual period one, one has period three, and 52 have period four; their maximum first-entry times are respectively five, zero, and four. The unique period-three profile pair is \((222,222)\). All other profile pairs not in the period-four table below lead to the all-rest fixed configuration. The complete period-four table lists the possible right profiles against each left profile; a profile such as \(122\) means one initial vertex of color zero and at least two vertices of each of colors one and two.

| Left profile | Right profiles giving eventual period four |
| --- | --- |
| 022 | 202, 211, 212, 220, 221, 222 |
| 121 | 202, 211, 212 |
| 122 | 202, 211, 212, 220, 221, 222 |
| 202 | 022, 121, 122, 220, 221, 222 |
| 211 | 022, 121, 122, 220, 221, 222 |
| 212 | 022, 121, 122, 220, 221, 222 |
| 220 | 022, 122, 202, 211, 212, 222 |
| 221 | 022, 122, 202, 211, 212, 222 |
| 222 | 022, 122, 202, 211, 212, 220, 221 |

The accompanying `verify_symbolic.py` is a transparent exhaustive certificate for this exact 529-case recurrence: it generates the profiles, updates tagged colors, compares complete occupied-class signatures, tests the period-four list implicitly, and checks the coefficient matrix below. The finiteness of this *complete quotient* proves the uniform assertions for arbitrary shore sizes; no extrapolation from small labelled graphs occurs. The first-entry maximum five is realized by profiles \((201,022)\), already feasible on \(K_{3,4}\). The sharp lesser bounds are realized respectively by \((020,101)\) on \(K_{2,2}\), \((200,021)\) on \(K_{2,3}\), and \((021,200)\) on \(K_{3,3}\). Extra vertices can be added to an already capped color class without altering the tagged trajectories. The 529-case recurrence also shows that the period-three signatures are already periodic initially, and the only initially period-four signatures are \((202,220)\) and \((220,202)\). The least common multiple of all eventual periods is twelve, giving \(F^{17}=F^5\).

**Exact labelled weighting.** For a fixed shore size \(n\ge4\), a specified capped profile with one absent color and two colors present at least twice has weight \(U_n=2^n-2n-2\); one singleton color and two colors present at least twice has weight \(A_n=n(2^{n-1}-2n)\); two singleton colors and one color present at least twice has weight \(Q_n=n(n-1)\); and three colors present at least twice has weight \(H_n=n![z^n](e^z-1-z)^3\), which expands by inclusion–exclusion as displayed above. Hence \(P_n=U_n+A_n\). Each weight is zero if its required minimum multiplicities exceed \(n\).

Classify each period-four profile as type \(U,A,Q,H\), using the four weights above. Counting the table's profile pairs gives the exact coefficient matrix
\[
M=\begin{pmatrix}
6&6&3&3\\
6&6&3&3\\
3&3&2&1\\
3&3&1&0
\end{pmatrix}.
\]
Thus \(B_4(a,b)=(U_a,A_a,Q_a,H_a)M(U_b,A_b,Q_b,H_b)^{\mathsf T}\), which simplifies to the announced formula. The sole three-cycle profile yields \(B_3=H_aH_b\); subtraction from the \(3^{a+b}\) labelled initial states gives \(B_1\). The only initially period-four profiles each have weight \(U_aU_b\), yielding \(2U_aU_b/4=U_aU_b/2\) distinct period-four orbits. The initially period-three states are exactly the \(H_aH_b\) states of profile \((222,222)\), yielding \(H_aH_b/3\) distinct period-three orbits.

**Existence thresholds and concentration.** \(U_n>0\) precisely when \(n\ge4\), and \(H_n>0\) precisely when \(n\ge6\). The nonnegative basin polynomial therefore proves the two sharp recurrence thresholds. If \(X_n\) is a uniform ternary word, a union bound over the three colors gives
\[
0\le1-\Pr\{\text{each color appears at least twice in }X_n\}
\le3\left(1+\frac n2\right)\left(\frac23\right)^n.
\]
Independence of the shores then shows \(B_3(a,b)/3^{a+b}\to1\) as \(\min(a,b)\to\infty\), with the explicit error bounded by the sum of the two right-hand terms.

## Verification
Run `python3 verify_symbolic.py`. It checks all 529 exact tagged profile pairs, verifies the 52 period-four profile pairs and their type matrix, establishes the five-update bound and sharp witnesses, and independently sums their labelled multinomial weights over all 81 ordered pairs \(2\le a,b\le10\). This is an exhaustive *symbolic factor* verification, not a claim that a finite sample proves arbitrary graph sizes without the exact factor argument.

Separately compile and run `c++ -std=c++17 -O2 verify_microscopic.cpp -o verify_microscopic && ./verify_microscopic`. That checker evolves individual vertex colors directly, without using the capped-state recurrence. It checks eight graph sizes, including \(K_{6,6}\) and \(K_{4,8}\), for a total of 1,327,590 labelled initial states. Full outputs from both commands are included as standalone files. These finite independent checks corroborate the infinite-family theorem but are not substitutes for the exact finite-factor proof.

## Relationship to prior work
The Greenberg–Hastings and cyclic excitation models, including thresholds above one, are classical; see Durrett and Griffeath (1993). Doba (2018) proves a qualitative periodicity criterion for three-state graph excitation under the **one-excited-neighbor** rule; the paper's Section 2 explicitly defines that rule and therefore its conclusions do not directly give this threshold-two census. Bello and Sivakoff (2021) study thresholds at least two on infinite regular trees, a different graph and probabilistic regime. Related established exact classifications for complete bipartite graphs involve three-state *cyclic-contact* updates or a **four-state** threshold-two refractory process. Neither update is dynamically equivalent to the three-state threshold-two rule here: changing the excitation condition or refractory duration changes both periods and entrance times. The contribution assessed here is the five-step cutoff, complete three-way basin census, period thresholds and exact orbit counts on all \(K_{a,b}\).

## Limitations
The result assumes fully synchronous updates, threshold exactly two, three colors, complete bipartite adjacency and shore sizes at least two. It does not classify arbitrary thresholds, other graph families, asynchronous dynamics, stochastic external excitation, or individual attraction basins of each distinct recurrent orbit. The finite symbolic certificate is part of the proof and should be executed as provided. Historical mathematical priority outside the inspected sources, including unindexed formulations, remains possible; this is not independent certification.

## References
1. R. Durrett and D. Griffeath, “Asymptotic Behavior of Excitable Cellular Automata,” *Experimental Mathematics* **2** (1993), 183–208. Earliest public arXiv submission: 1993-03-22, https://arxiv.org/abs/patt-sol/9303002 . DOI: 10.1080/10586458.1993.10504277.
2. N. Doba, “The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph,” *Complex Systems* **27** (2018), 101–126. https://wpmedia.wolfram.com/sites/13/2018/09/27-2-1.pdf . DOI: 10.25088/ComplexSystems.27.2.101.
3. J. Bello and D. Sivakoff, “Cyclic Cellular Automata and Greenberg-Hastings Models on Regular Trees,” arXiv:2108.06404 (2021), https://arxiv.org/abs/2108.06404 .
