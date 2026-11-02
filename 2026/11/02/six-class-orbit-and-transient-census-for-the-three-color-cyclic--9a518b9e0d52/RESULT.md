# Six-class orbit and transient census for the three-color cyclic automaton on wheels

## Finding

Let \(W_n=K_1\vee C_n\), where \(n\ge3\), and apply synchronous three-color cyclic cellular automaton (CCA): a vertex of color \(a\in\mathbb Z/3\mathbb Z\) changes to \(a+1\) precisely when a neighbor already has color \(a+1\); otherwise it retains \(a\). Let \(\tau(x)\) be the least nonnegative time at which the trajectory of \(x\) has become periodic. Every trajectory is ultimately monochromatic and fixed, or belongs to a primitive three-cycle of configurations, and the exact uniform identity is
\[
F^5=F^2.
\]
For \(n=3\), the maximum \(\tau\) is one; for every \(n\ge4\), the maximum is two.

Define the monic polynomials
\[
\begin{aligned}
p_A(t)&=(t-1)(t^2-2t-1),\\
p_B(t)&=(t^2+t+1)(t^3-2t^2-1),\\
p_C(t)&=t^3-t^2-t-1,\\
p_M(t)&=t^6-2t^5-t^4-2t^3-t^2-2t+3.
\end{aligned}
\]
For \(X\in\{A,B,C,M\}\), let \(X_n\) be the sum of the \(n\)-th powers of all complex roots (with algebraic multiplicity) of \(p_X\). The following is the **complete six-class census** of labelled initial states, where \(S_j\) counts trajectories whose first periodic state occurs at time \(j\) and is fixed, and \(O_j\) counts those whose first periodic state occurs at time \(j\) and belongs to a primitive three-cycle:
\[
\begin{array}{rlrl}
S_0&=3,&O_0&=3(B_n-1),\\
S_1&=3(2^n+C_n)-3,&O_1&=3(M_n-2^n-B_n+1),\\
S_2&=3A_n-3(2^n+C_n),&O_2&=3^{n+1}-3A_n-3(M_n-2^n).
\end{array}
\]
Every other class is empty. In particular, there are exactly \(B_n-1\) distinct primitive three-cycle orbits, and the number of monochromatic-attraction-basin configurations is \(3A_n\), where
\[
A_n=1+(1+\sqrt2)^n+(1-\sqrt2)^n.
\]
For uniformly random labelled initial colors, the probability that the first periodic state occurs at the *second* update tends to one as \(n\to\infty\). The nonfixating basin instead has probability \(1-A_n/3^n\), also tending to one.

## Assumptions and scope

The graph is the simple, undirected wheel with one hub and a labelled rim of length \(n\ge3\). Updates occur simultaneously with threshold one; there are exactly three cyclically ordered colors. Configurations are **not** identified under graph automorphisms or cyclic rotation of color labels. A primitive temporal three-cycle orbit is counted once, whereas \(O_j\) counts initial *configurations*. The first-entry time uses exact periodicity of the whole configuration, not merely persistent activity at one vertex. No claim is made for higher color counts or other thresholds.

## Proof

**(1) Sharp universal entry time.** Normalize the initial hub color to zero by global color rotation. If some rim edge has endpoints colored one and two, the hub and those endpoints form a rainbow triangle. Every vertex of that triangle has a neighbor of successor color, so the triangle rotates one color forward at every update; in particular the hub color equals its initial color plus time modulo three. Write \(d_i(t)\) for a rim vertex's color minus the hub color. Its local update is
\[
2\mapsto2;\qquad
1\mapsto\begin{cases}1&\text{if a rim neighbor has difference }2,\\0&\text{otherwise};\end{cases}\qquad
0\mapsto\begin{cases}0&\text{if a rim neighbor has difference }1,\\2&\text{otherwise}.\end{cases}
\]
A site with difference two is permanently locked. Any site with difference one at time one must have had a difference-two neighbor at time zero, which persists, so it is permanently locked. Any site still of difference zero at time two has a difference-one neighbor at time one, also permanently locked; all other sites have become difference two. Thus every difference is constant after time two. The hub rotates every step, proving \(F^5(x)=F^2(x)\) and eventual primitive period three for these states.

If there is no rim edge colored one--two, two cases cover all initial states. If there is no rim one, at time one the hub stays zero, every two becomes zero using the hub, and every zero stays zero: the entire state is fixed. If some rim one occurs, the hub becomes one. No rim one has a two-neighbor, so those ones remain one. Every rim two becomes zero via the hub, while rim zeros either become one (next to an initial one) or remain zero. At time one every rim entry is zero or one. At time two the hub remains one and all rim zeros advance to one using the hub, so the state is monochromatic. This proves that the basin dichotomy is exactly the presence or absence of a rainbow hub triangle. A state with hub zero and a single rim one, all other rim entries zero, attains first-entry time two for every \(n\ge4\). When \(n=3\), the wheel is complete and every state enters by time one.

**(2) Synchronizing basin and its first layer.** With fixed hub color zero, forbidding a rainbow hub triangle is equivalent to forbidding adjacent rim colors one and two in either order. The three-by-three cyclic-word transition matrix is
\[
A=\begin{pmatrix}1&1&1\\1&1&0\\1&0&1\end{pmatrix}.
\]
Its cyclic-word count is \(\operatorname{tr}(A^n)=A_n\), yielding \(3A_n\) ultimately fixed initial states. To be fixed after at most one update, either the rim initially has no ones (\(2^n\) words over zero and two), or it uses only zero and one and every zero has a neighboring one. The latter are cyclic binary words avoiding the triple `000`; their number is \(C_n\), the trace of the four-state binary de Bruijn matrix that admits transitions \((a,b)\to(b,c)\) unless \((a,b,c)=(0,0,0)\). Its nonzero characteristic polynomial is \(p_C\). The two types are disjoint for \(n\ge3\), so the fixed cumulative counts at times zero, one and two are \(3\), \(3(2^n+C_n)\), and \(3A_n\), respectively.

**(3) Primitive three-cycle configurations.** In a state that advances globally at every step, fix the hub color zero. A rim vertex of color two automatically has its required successor (the hub); a rim one needs a neighboring two, and a rim zero needs a neighboring one. Define the nine-state matrix indexed by ordered pairs \((a,b)\in\{0,1,2\}^2\) whose entry from \((a,b)\) to \((b,c)\) equals one exactly when \(b=2\) or \(b+1\pmod3\in\{a,c\}\). Its trace \(B_n\) counts these cyclic rim words. The single all-two rim word has no successor for the hub and must be excluded. Every remaining word contains a rim one, which excites the hub of color zero, and is a globally rotating three-cycle state. Adding the one monochromatic fixed state for the hub's specified color gives exactly \(B_n\) recurrent states per hub color, and \(3(B_n-1)\) periodic states of primitive period three. Exact characteristic-polynomial computation gives \(\det(tI-B)=t^4p_B(t)\).

**(4) One-update entry into a primitive three-cycle.** Let
\[
f(a,b,c)=\begin{cases}b+1\pmod3&\text{if }b+1\pmod3\in\{0,a,c\},\\b&\text{otherwise}.\end{cases}
\]
This is the rim output at one update when the initial hub is zero. Index an 81-state transfer matrix \(M\) by four-letter words \((a,b,c,d)\in\{0,1,2\}^4\). Admit the transition from \((a,b,c,d)\) to \((b,c,d,e)\) precisely when, for \(L=f(a,b,c)\), \(V=f(b,c,d)\), and \(R=f(c,d,e)\), one has either \(V=0\), or \(V+1\pmod3\in\{L,R\}\). This is exactly the condition that the output rim vertex has its successor, *assuming* the updated hub is one. The cyclic trace \(M_n=\operatorname{tr}(M^n)\) counts all input rim words satisfying these local conditions. Inputs without any one, of which there are exactly \(2^n\), are the only spurious words: their true updated hub is zero, and all outputs are zero. If an input has a one, the conditions force at least one updated rim two, so the actual updated hub has a successor and the output rotates globally. Hence precisely \(3(M_n-2^n)\) configurations enter a primitive three-cycle no later than one update. Subtracting the time-zero count yields \(O_1\); subtracting from the total nonfixating basin \(3^{n+1}-3A_n\) yields \(O_2\).

**(5) The exact six-degree spectral identity.** The matrices above are explicit finite integer matrices, not numerically inferred recurrences. Their characteristic polynomials are
\[
\det(tI-A)=p_A(t),\quad
\det(tI-B)=t^4p_B(t),\quad
\det(tI-C)=t\,p_C(t),\quad
\det(tI-M)=t^{75}p_M(t).
\]
The last identity has a compact exact certificate: rational ranks of \(M^5\) and \(M^6\) are both six; the integer matrix identity \(M^5p_M(M)=0\) holds; and the first six traces of \(M\) are \((2,6,20,54,152,390)\). Equal ranks give a six-dimensional invertible stable image, and Newton's identities for these six power sums give its characteristic polynomial \(p_M\). All other eigenvalues are zero, proving the factor \(t^{75}\). The standalone verifier constructs every entry from the definitions, checks this finite certificate over exact arithmetic, and separately enumerates all labelled states for \(3\le n\le10\). These finite checks reinforce, but do not replace, the general structural argument.

Finally, each of the four polynomials has all roots strictly within the circle of radius three: this is immediate for \(p_A\); for the cubic factors and \(p_M\) it follows by comparing the leading term with the sum of absolute lower-order terms when \(|t|\ge3\) (and the quadratic factor of \(p_B\) has unit-modulus roots). Thus \(A_n,B_n,C_n,M_n=o(3^n)\). The six formulas imply \(O_2/3^{n+1}\to1\), as asserted.

## Verification

Execute `python3 wheel_cca_verifier.py` using Python 3 and its standard library. It constructs transfer matrices of dimensions 3, 9, 4 and 81, checks the integer-matrix polynomial and exact rational ranks, and independently simulates all \(265680\) labelled initial states on wheels with \(3\le n\le10\). The recorded reference output is `verification_output.txt`, whose final marker is `WHEEL_CCA_EXACT_VERIFY_OK`. The exact six-class counts for \(n=4\) are \((3,78,24;66,48,24)\), and for \(n=5\) they are \((3,156,90;150,210,120)\), ordered as fixed-then-period-three classes at entry times zero, one and two. The proof applies to every \(n\ge3\); brute force alone is not used to extrapolate.

## Relationship to prior work

Gravner, Lyu and Sivakoff established the general 3-color CCA/GHM criterion in terms of vanishing cycle integrals, including an upper bound of the graph diameter for synchronization. Their characterization supplies relevant background for the fixed/oscillatory basin division, but it does not state this wheel-family six-class first-entry census, the exact spectral polynomials, the finite algebraic trace identities, or the two-step periodic-entry classification of oscillatory states. The proof above is independent of their cycle-integral theorem and uses direct wheel dynamics for the two-step bound. Bello's subsequent dissertation discusses cyclic particle systems on finite graphs with random *discordant voting* and deterministic CCA/GHM on infinite trees; the different update models should not be identified with synchronous finite-wheel CCA. The relevant comparison is by statements and mechanisms, not by matching titles.

## Limitations

The result concerns labelled, loopless wheels and exactly three colors with threshold one. The recurrence sequences count labelled initial states, not spatial symmetry classes. The six-degree transfer computation is reproducibly certified by the included exact-arithmetic program, but there has been no independent mathematical audit. Searches and inspections cannot exclude an unindexed historical equivalent or a result formulated in terms of a stronger general graph enumeration; this residual originality risk is explicit.

## References

1. J. Gravner, H. Lyu, and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, first submitted October 24, 2016, https://arxiv.org/abs/1610.07320 (especially the model definitions and Theorem 3; subsequently published in *Annals of Applied Probability*).
2. J. Bello, *Cyclic Particle Systems on Finite Graphs and Cellular Automata on Rooted, Regular Trees and Galton-Watson Trees*, Ohio State University PhD dissertation, 2021, https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=osu1618833498993715&disposition=inline (abstract, introduction, and contents examined).
