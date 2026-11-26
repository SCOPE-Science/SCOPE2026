# Exact first-entry layer laws for Greenberg–Hastings excitation on bridged cliques

## Finding

Let \(B_{a,b}\), for integers \(a,b\ge2\), be the graph obtained by joining a distinguished vertex of \(K_a\) to a distinguished vertex of a vertex-disjoint \(K_b\) by a single edge. Under synchronous three-state threshold-one Greenberg–Hastings evolution, every initial state reaches a periodic configuration by time six. The only eventual periods are one and three; the only fixed state is all resting. The maximum entry time is six for every \((a,b)\ne(2,2)\) and five for \((2,2)\).

Write \(N_{p,t}(a,b)\) for the number of labelled initial configurations whose eventual least period is \(p\) and whose first periodic-entry time is \(t\). Set
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
5&(3XY-4X-4Y+4)/2 .
\end{array}
\]
The recurrent three-cycle layer is \(N_{3,0}=9AB+3(A+B)\). For \(1\le t\le6\), with \(j=\min\{t,7-t\}\),
\[
 N_{3,t}=\frac{2j-1}{6}(UY+XV)-\frac j3(U+V)-(2j-1)XY+\frac{4j-1}{2}(X+Y)-2j.
\]
All other layers vanish. In particular \(N_{3,t}=N_{3,7-t}\) for \(1\le t\le6\). There are \(3AB+A+B\) primitive three-cycle orbits. The basin of the unique fixed state has size \(9(X-1)(Y-1)\). Under independent uniform initial colors its probability is \(9(1-2^{-a})(1-2^{-b})(2/3)^{a+b}\); the complementary period-three attraction probability tends to one exponentially as both orders tend to infinity.

## Assumptions and scope

Vertices carry colors \(0\) (resting), \(1\) (excited), \(2\) (refractory), with all vertices updating simultaneously. Colors \(1\) and \(2\) change unconditionally to \(2\) and \(0\); a resting vertex changes to \(1\) precisely when it has an excited neighbor, and otherwise stays at \(0\). The neighborhood is open. Vertices and colors are labelled. First-entry time is the least nonnegative time at which the state is periodic. A three-cycle counts as one orbit but consists of three recurrent configurations.

## Proof

**Presence masks.** Keep the colors \(h,k\) of the bridge endpoints and the sets \(S,T\) of colors present among the nonbridge vertices on each side. For the shore with hub \(h\), the nonhub set updates by \(1\mapsto2\), \(2\mapsto0\), and \(0\mapsto1\) if \(1\in S\) or \(h=1\), and \(0\mapsto0\) otherwise. Apply these rules to the colors in \(S\) and take the union of the images. The hub updates with the same unconditional rules at 1 and 2, and goes from \(0\) to \(1\) precisely if \(1\in S\) or \(k=1\). The other shore is symmetric. These are exact projected dynamics: any resting vertex is not itself excited, so the presence tests respect open neighborhoods. There are \(9\cdot 7^2=441\) states in this projection, independent of clique orders.

**Period and first entry.** Let \(R\) add one modulo three to the two hub colors and to all colors in both masks. For a projected state \(s\), the test that its next state equals \(R(s)\) is equivalent to every vertex advancing by one modulo three in the labelled state. In fact a blocked resting hub leaves its hub coordinate at zero, and a mask with a blocked resting class contains zero but its next mask lacks one, whereas the rotated mask contains one. A successful test at a single time does not imply repetition (for example, it holds for all excited). The test must succeed at all three phases of a rotating cycle, or equivalently every vertex of color \(c\) must have a neighbor of color \(c+1\) modulo three in the initial phase.

The finite computation in `support_certificate.py` follows each projected state until its first repetition. It verifies that its period and entry time are either 1 and at most 5, or 3 and at most 6. The only recurrent period-one mask state is all resting, and for every period-three orbit it checks the rotation test at each of its three states. The projected periodic entry thus lifts to periodic entry of the labelled dynamics: all vertices either are resting, or advance through all three colors in the verified cycle. Conversely an earlier labelled periodic state would project to an earlier periodic mask state, so the computed first entries are exact. The lifted period is the same as the projected one, since the all-resting state is fixed and all colors change in a rotating cycle.

**Recurrent counts.** In a rotating configuration, a clique with hub color \(h\) either contains both colors \(h+1\) and \(h-1\) among its nonhubs, or all its nonhubs are \(h-1\) and the opposite hub has color \(h+1\). This follows from the three-phase neighbor condition: if there is a nonhub of color \(h+1\), it requires \(h-1\), and if there is no \(h+1\) in the clique, no nonhub can be \(h\). The first case provides all three colors and requires no bridge support. In the second case the hub needs its missing successor color across the bridge. Both shores cannot be of the second type, since the demanded hub-color differences are incompatible. Inclusion–exclusion over the two required colors gives \(A\) patterns in the first case on the first shore, and \(B\) on the second. The three choices for each hub in the first–first case, and the three choices for the lone independent hub color in each mixed case, give \(9AB+3(A+B)\). Divide by three for the number of orbits.

**Exact layers.** For a nonempty mask \(S\), exactly the colors in \(S\) occur, each at least once. The exponential generating function of its assignments to labelled nonhubs is \((e^z-1)^{|S|}\). The series for a layer is the sum of \((e^z-1)^{|S|}(e^w-1)^{|T|}\) over its projected states (including each hub pair). The finite computation compares these expressions as polynomials in \(E=e^z\), \(F=e^w\), clearing denominators by six. At positive nonhub sizes, \(E-1\), \(2(E^2-1)\) and \(3(E^3-1)\) represent \(1,2^a,3^a\) under extraction of \((a-1)![z^{a-1}]\); use the same basis in \(F\) for the other shore. The thirteen polynomial identities give the displayed layer formulas for every order, without graph-size extrapolation. Summing the six extinction layers gives \(9(X-1)(Y-1)\).

**Sharpness.** If \(a\ge2\) and \(b\ge3\), set hub colors \(h=0,k=2\) and take masks \(S=\{1\},T=\{0,1\}\). The projected state has period three and first-entry time six. These masks are realized for all such sizes; exchanging shores handles \(a\ge3,b=2\). For \(a=b=2\), both masks are singletons, and the largest entry time over this restricted projected space is five. The initial colors \((h,\text{nonhub A},k,\text{nonhub B})=(0,0,0,1)\) attain five.

## Verification

Run `python3 support_certificate.py` (Python 3.10 or newer, without `-O`). It checks the recurrent lifting at all three phases, all thirteen all-size polynomial identities and sharpness. The original capped-count computation and direct labelled enumeration on twelve pairs of orders are supplementary checks. The direct enumeration does not establish formulas outside the tested orders.

## Relationship to prior work

Gravner, Lyu and Sivakoff's Theorem 3 gives a general cycle-integral criterion for synchronization of finite graphs. Here all cycles lie within the cliques, with a nonzero integral exactly when a rainbow triangle occurs. Extinction therefore occurs exactly when neither clique initially contains all three colors; counting those initial conditions gives the aggregate extinction basin directly. The graph has diameter three, so their synchronization bound followed by at most two updates to all resting also gives the five-step upper bound for extinction cases. Doba's maximum cycle-density result implies the period classification here: a rainbow triangle attains density \(1/3\), so every vertex has eventual excitation rate \(1/3\); its gaps between excitations are at least three and thus equal three on the eventual cycle. The rotating clock mechanism also appears in Durrett and Griffeath's lattice setting. The contributions here are the full first-entry layers, the sharp cutoff in the surviving cases, and the count and description of recurrent three-cycle orbits, not the aggregate extinction criterion or the list of possible periods.

## Limitations

The result is for three colors, threshold one, synchronous updates, and a single bridge between two cliques of orders at least two. The all-size proof uses a finite symbolic certificate, not a formal proof assistant. Priority is relative to the available literature.

## References

1. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, https://arxiv.org/abs/1610.07320.
2. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems **27** (2018), 101–126, https://doi.org/10.25088/ComplexSystems.27.2.101.
3. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, Theorem 1.1 and proof outline. Author copy: https://sites.math.duke.edu/~rtd/reprints/paper79.pdf.
