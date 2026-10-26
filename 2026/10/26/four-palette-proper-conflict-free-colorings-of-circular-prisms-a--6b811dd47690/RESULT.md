# Four-palette proper conflict-free colorings of circular prisms: an exact rational census

## Finding
Let \(P_n=C_n\square K_2\), with \(n\ge 3\), and let \(F_4(n)\) be the number of proper vertex colorings of \(P_n\) from a fixed palette of four **named** colors in which every open neighborhood contains a color appearing exactly once. A coloring need not use every available color. Define
\[
\begin{aligned}
D(t)={}&(1-t)^6(1+t)^2(1-2t)(1+t+2t^2)^3\\
&\cdot(1-t-2t^3)^2(1-4t-6t^2+4t^3)\\
&\cdot(1+3t+6t^2-2t^3+4t^4)^3.
\end{aligned}
\]
Then the **complete four-palette census**, for all circumferences, is the rational series
\[
\boxed{\displaystyle\sum_{n\ge 3}F_4(n)t^n=-t\frac{D'(t)}{D(t)}-24t^2.}
\]
Its initial coefficients for circumferences \(3\) through \(11\) are
\[
264,\ 384,\ 3600,\ 17472,\ 75936,\ 427152,\ 2071632,\ 10365504,\ 52961568.
\]
The minimum palette size is \(3\) when \(3\mid n\) and \(4\) otherwise. More sharply, the number \(U(n)\) of partitions of the **labeled vertices** into unlabeled color classes arising from minimum-palette proper conflict-free colorings is
\[
\boxed{\displaystyle U(n)=\begin{cases}2,&3\mid n,\\ F_4(n)/24,&3\nmid n.\end{cases}}
\]
For circumferences not divisible by three, these optimum counts grow as \(\lambda^n/24\), where \(\lambda=5.03404183580349\ldots\) is the largest real root of \(x^3-4x^2-6x+4\). For circumferences divisible by three, the optimum partition count remains exactly two.

## Assumptions and scope
All graphs are finite and simple. The prism has vertices \((i,s)\) with \(i\in\mathbb Z/n\mathbb Z\), \(s\in\{0,1\}\); two vertices are adjacent if their first coordinates agree and second coordinates differ, or their second coordinates agree and first coordinates differ by one cyclic step. For a proper coloring, a vertex's three neighbor colors contain a uniquely occurring color if and only if they are not all identical. Thus on these cubic graphs proper conflict-free coloring is exactly proper two-dynamic coloring. The four colors are distinguishable names, and a palette coloring is a map to the palette, not necessarily a surjection. Counts of unlabeled class partitions quotient a surjective named-color count by the factorial of the number of used colors.

## Proof
**Three colors and optimality.** Under a proper three-coloring every vertex's neighborhood can use at most the two colors different from its own; the conflict-free condition forces both to occur. A column is an ordered rung pair \((a,b)\) with \(a\ne b\). After renaming colors, take one column to be \((0,1)\). Properness limits the next column to \((1,0)\), \((1,2)\), or \((2,0)\). The swap \((1,0)\) cannot be followed by a valid third column: the two local neighborhood requirements would force both entries to equal \(2\). In the second possibility the next column is uniquely forced to \((2,0)\), and in the third it is forced to \((1,2)\). Iterating gives one of the two three-periodic rung patterns. The cyclic closure requires \(3\mid n\). There are six choices of the first ordered pair and two orientations, hence exactly \(12\) named three-colorings when \(3\mid n\), and none otherwise. Proper two-colorings cannot satisfy the conflict-free property because all neighbors of a vertex would share the opposite color.

**Four colors exist for every circumference.** Write each column as its top and bottom colors. The following three valid periodic sequences of columns have lengths \(3\), \(4\), and \(5\), respectively:
\[
\begin{aligned}
&((0,1),(1,0),(2,3)),\\
&((0,1),(1,0),(2,3),(3,2)),\\
&((0,1),(1,0),(2,3),(0,1),(2,3)).
\end{aligned}
\]
Each sequence has the same initial two columns \(((0,1),(1,0))\); viewed as a closed walk of ordered consecutive-column states, each also ends at that state. Concatenating these closed walks preserves every triple-column constraint. Since every integer \(n\ge3\) is a nonnegative sum of \(3\), \(4\), and \(5\), a four-palette valid coloring exists for every \(n\ge3\). Together with the preceding paragraph this proves the palette-size assertion.

**A finite transfer matrix counts all four-palette colorings.** Let \(Q\) be the set of ordered pairs \((a,b)\) of different colors in \(\{0,1,2,3\}\); it has \(12\) elements. Let \(S\) consist of ordered column pairs \((u,v)\in Q^2\) satisfying \(u_0\ne v_0\) and \(u_1\ne v_1\). Direct counting gives \(|S|=84\). Define the \(84\)-square zero-one matrix \(A\), indexed by \(S\), by
\[
A_{(u,v),(v,w)}=1
\]
precisely when \(v_0\ne w_0\), \(v_1\ne w_1\), \(|\{u_0,w_0,v_1\}|\ge2\), and \(|\{u_1,w_1,v_0\}|\ge2\); all other entries vanish. The two cardinality conditions are exactly the conflict-free constraints at the middle column. Consequently each valid coloring of an indexed \(n\)-column cyclic prism corresponds bijectively to one length-\(n\) closed walk with indexed starting state in this graph. Therefore \(F_4(n)=\operatorname{tr}(A^n)\) for every \(n\ge3\).

**Exact characteristic polynomial.** The finite integer identity
\[
\det(I-tA)=D(t)
\]
is verified by the standalone, dependency-free program `verify.py`. Specifically, it constructs all \(84\) states and \(384\) transitions from the above formula; computes the exact traces \(\operatorname{tr}(A^j)\) for \(1\le j\le84\); and uses the Newton determinant identities to recover **every** coefficient of \(\det(I-tA)\). It independently multiplies the seven displayed factors of \(D(t)\) and checks all \(85\) coefficients, including the high-degree zeros. This is an exhaustive **finite exact-arithmetic certificate** for the polynomial identity, not a numerical extrapolation about large circumferences. The formal identity
\[
-t\frac{d}{dt}\log\det(I-tA)=\sum_{j\ge1}\operatorname{tr}(A^j)t^j
\]
then proves the generating function. Its first two traces are \(0\) and \(24\); subtracting \(24t^2\) removes the non-prism two-column term (simple cycle graphs here start at length three).

**Optimum census and asymptotics.** For \(3\mid n\), the twelve three-named-colorings yield precisely \(12/3!=2\) unlabeled optimum partitions. Otherwise every valid four-palette coloring must use all four colors, giving \(U(n)=F_4(n)/4!\). The transfer digraph is strongly connected, as verified by exact forward and reverse reachability, and is aperiodic because its initial state supports closed walks of coprime lengths \(3\) and \(4\). Perron–Frobenius therefore gives a simple dominant positive eigenvalue \(\lambda\). From the factored characteristic polynomial, the unique eigenvalue of greatest modulus is the real root \(\lambda=5.03404183580349\ldots\) of \(x^3-4x^2-6x+4\). Hence \(F_4(n)=\lambda^n+o(\lambda^n)\), proving the stated asymptotic along circumferences not divisible by three.

## Verification
Run `python3 verify.py` using Python 3 standard library. Expected marker: `VERIFY_OK: transfer, exact determinant, direct counts, constructions`. It independently counts colorings by vertex-level backtracking for circumferences \(3\), \(4\), and \(5\) (four colors) and \(3\) through \(6\) (three colors). Those small checks are diagnostic; the proof for all \(n\) is the transfer bijection, exact finite characteristic identity, and the color-pattern argument. The checker also establishes strong connectivity and the stated short closed walks.

## Relationship to prior work
Proper conflict-free open-neighborhood coloring was developed by Fabrici, Lužar, Rindošová, and Soták (2022) and by Caro, Petruševski, and Škrekovski (2022). On cubic graphs this condition is identical to proper two-dynamic coloring, a previously studied invariant. Madaras and Šurimová's *Homogeneous colourings of graphs* (first published 2022) investigates homogeneous colorings of prism graphs; in particular its three-color analysis establishes the period-three obstruction, so the **three-color existence criterion is background rather than the new enumerative contribution**. Work on crossed or stacked prism graphs concerns different graph families. The new claim here is the explicitly factored **complete four-palette generating function**, yielding every four-palette count, the full minimum-class-partition census, and the resulting constant-versus-exponential counting transition. General upper bounds and scalar chromatic-number results do not supply that generating function.

## Limitations
The determinant factorization is a finite exact-arithmetic certificate requiring the accompanying source program for efficient independent replay. No claim about every possible palette size or other graph products is made. Literature-indexing gaps and the inability to inspect every potentially relevant legacy full text leave a residual priority risk.

## References
- I. Fabrici, B. Lužar, S. Rindošová, R. Soták, *Proper conflict-free and unique-maximum colorings of planar graphs with respect to neighborhoods* (2022), arXiv:2202.02570, https://arxiv.org/abs/2202.02570 .
- Y. Caro, M. Petruševski, R. Škrekovski, *Remarks on proper conflict-free colorings of graphs* (2022), arXiv:2203.01088, https://arxiv.org/html/2203.01088v1 .
- T. Madaras, M. Šurimová, *Homogeneous colourings of graphs*, published online April 28, 2022; Mathematica Bohemica 148 (2023), 105–115, https://doi.org/10.21136/MB.2022.0007-21 .
- A. Jiménez, K. Knauer, C. Lintzmayer, J. Zamora, *Boundedness for proper conflict-free and odd colorings* (2023), arXiv:2308.00170, https://arxiv.org/html/2308.00170v4 .
