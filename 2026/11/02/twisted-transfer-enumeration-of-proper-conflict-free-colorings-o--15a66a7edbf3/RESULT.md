# Twisted transfer enumeration of proper conflict-free colorings of Möbius ladders

## Finding

For every integer \(m\ge 3\), let \(M_{2m}\) be the simple Möbius ladder, namely the cycle on \(2m\) vertices with chords joining antipodal vertices. A proper conflict-free (PCF) coloring is a proper vertex coloring in which every open neighborhood contains a color appearing exactly once. Write \(a_4(m)\) for the number of PCF colorings of \(M_{2m}\) from the **named** palette \(\{0,1,2,3\}\), allowing unused colors. Then

\[
\boxed{\chi_{\mathrm{pcf}}(M_{2m})=4 \qquad(m\ge3).}
\]

There is also an exact rational generating function for **all** named four-palette colorings. Define

\[
\begin{aligned}
P_+(t)&=(1-t)^3(1-t-2t^3)^2(1-4t-6t^2+4t^3)
             (1+3t+6t^2-2t^3+4t^4)^3,\\
P_-(t)&=(1-t)^3(1+t)^2(1-2t)(1+t+2t^2)^3.
\end{aligned}
\]

Then, as an identity of formal power series,

\[
\boxed{\sum_{m\ge3}a_4(m)t^m
   =-t\frac{d}{dt}\log\!\left(\frac{P_+(t)}{P_-(t)}\right)-24t^2.}
\]

The first five terms are \(216t^3+336t^4+3600t^5+17280t^6+75600t^7\). In particular, every PCF four-palette coloring of \(M_{2m}\) uses all four colors (since no PCF three-coloring exists), so these coefficients enumerate the labeled optimal colorings.

There is a quantitative twist comparison. If \(b_4(m)\) denotes the same named four-palette count on the untwisted prism \(C_m\square K_2\), and \(L_0=2\), \(L_1=-1\), \(L_{j+2}=-L_{j+1}-2L_j\), then

\[
\boxed{b_4(m)-a_4(m)=2^{m+1}+6+4(-1)^m+6L_m,\quad m\ge3.}
\]

The difference is strictly positive except at \(m=5\), where it is zero. This comparison is an outcome of the same twisted enumerator, not a separate claim of a new prism enumerator.

## Assumptions and scope

All graphs are finite, simple, and undirected. The Möbius ladder has a two-row strip presentation with vertices \(a_i,b_i\), for \(0\le i<m\). It has rungs \(a_ib_i\), horizontal edges \(a_ia_{i+1},b_ib_{i+1}\) for \(0\le i<m-1\), and crosswise closing edges \(a_{m-1}b_0,b_{m-1}a_0\). This is isomorphic to the antipodal-chord definition. The *prism* used for comparison instead closes with \(a_{m-1}a_0,b_{m-1}b_0\). Each vertex has exactly three neighbors. A named coloring distinguishes fixed color labels and fixed labelled vertices; no quotient by graph automorphisms or color permutations is taken.

## Proof

**1. No coloring with fewer than four colors.** A proper two-coloring of any cubic graph cannot be conflict-free: all three neighbors of a vertex would have the opposite color. Suppose a proper PCF coloring used the three colors \(\{\alpha,\beta,\gamma\}\). Represent each column by the ordered pair of its top and bottom colors. Each column contains distinct colors. From a column \((\alpha,\beta)\), the next column must be one of \((\beta,\alpha)\), \((\beta,\gamma)\), \((\gamma,\alpha)\). The swap \((\beta,\alpha)\) is impossible: at that middle column the PCF condition at the top forces the next top entry to be \(\gamma\), while at the bottom it forces the next bottom entry to be \(\gamma\), contradicting properness of its rung. Thus each transition has either forward form \((\alpha,\beta)\mapsto(\beta,\gamma)\) or reverse form \((\alpha,\beta)\mapsto(\gamma,\alpha)\). A change of direction also fails: the three consecutive columns would be \((\alpha,\beta),(\beta,\gamma),(\alpha,\beta)\) or \((\alpha,\beta),(\gamma,\alpha),(\alpha,\beta)\), and one middle vertex would have three neighbors of one color. Hence the direction is constant and every three columns the same ordered pair recurs. The three ordered pairs in either periodic orbit never include the row swap \((\beta,\alpha)\) of the initial pair. But the Möbius closing rule requires the column after \(m\) steps to be the row swap of the first. This is impossible, proving \(\chi_{\mathrm{pcf}}(M_{2m})\ge4\).

**2. A four-color construction.** With colors \(0,1,2,3\), set column symbols \(A=(0,1)\), \(B=(1,0)\), \(C=(2,3)\), \(D=(3,2)\). For \(m=3q+r\), \(q\ge1\), \(0\le r\le2\), take the column word \((ABC)^q\), \((ABC)^qD\), or \((ABC)^qAC\), respectively. Along each edge the endpoint colors differ. At a middle column \(v\) with predecessor \(u\) and successor \(w\), failure of conflict-freeness at the top is exactly \(u_0=w_0=v_1\); failure at the bottom is exactly \(u_1=w_1=v_0\). For each of the three endings, these two forbidden equalities and both properness inequalities can be checked at every triple for \(q=1,2\), with the last column joined crosswise to the first. Additional copies of \(ABC\) introduce only the already checked interior triples \(ABC,BCA,CAB\) and leave the boundary triples unchanged. Thus the construction works for all \(q\ge1\), proving the upper bound \(4\).

**3. The exact transfer.** Let \(\mathcal C\) be the 12 ordered pairs of distinct colors from the named four-color palette. Let \(\mathcal S\) be the 84 ordered pairs \((u,v)\in\mathcal C^2\) satisfying \(u_0\ne v_0\) and \(u_1\ne v_1\). Define the integer \(84\)-by-\(84\) transfer matrix \(T\) by

\[
T_{(u,v),(v,w)}=
\begin{cases}
1,&v_0\ne w_0,\ v_1\ne w_1,\
    \neg(u_0=w_0=v_1),\ \neg(u_1=w_1=v_0),\\
0,&\text{otherwise},
\end{cases}
\]

and set all other entries to zero. Write \(J(u,v)=((u_1,u_0),(v_1,v_0))\) for simultaneous row exchange. It is an involution without fixed states and commutes with \(T\). The transfer conditions are precisely properness on two adjacent column boundaries plus PCF at the middle column. Therefore for every \(m\ge3\),

\[
a_4(m)=\operatorname{tr}(JT^m),\qquad
b_4(m)=\operatorname{tr}(T^m).
\]

There are 42 row-swap orbits in \(\mathcal S\). Select the lexicographically smaller representative \(r\) in each orbit and define \(42\)-by-\(42\) integer matrices \(T_+,T_-\) by \((T_\pm)_{r,s}=T_{r,s}\pm T_{r,Js}\). These represent the invariant and anti-invariant subspaces of \(J\), respectively. Consequently,

\[
a_4(m)=\operatorname{tr}(T_+^m)-\operatorname{tr}(T_-^m),\qquad
b_4(m)-a_4(m)=2\operatorname{tr}(T_-^m).
\]

The following **exact finite algebra identities** hold:

\[
\begin{aligned}
\det(xI-T_+)&=x^{18}(x-1)^3(x^3-x^2-2)^2
 (x^3-4x^2-6x+4)(x^4+3x^3+6x^2-2x+4)^3,\\
\det(xI-T_-)&=x^{30}(x-2)(x-1)^3(x+1)^2(x^2+x+2)^3.
\end{aligned}
\]

They are reproducible from the definitions of all 84 states by the integer Faddeev–LeVerrier characteristic-polynomial recurrence, implemented in `verify.py`. In particular, \(P_\pm(t)=\det(I-tT_\pm)\) are the two polynomials displayed in the finding. For any finite square matrix \(B\), the formal identity \(\sum_{m\ge1}\operatorname{tr}(B^m)t^m=-t\frac{d}{dt}\log\det(I-tB)\) holds. The first two twisted trace coefficients are \(0\) and \(24\). Subtracting these non-graph terms gives the announced generating function for \(m\ge3\).

For the comparison, the nonzero eigenvalues of \(T_-\) are \(2\) once, \(1\) three times, \(-1\) twice, and both roots of \(x^2+x+2\) each three times. The stated recurrence defines the sum of the last two eigenvalue powers. Thus \(2\operatorname{tr}(T_-^m)=2^{m+1}+6+4(-1)^m+6L_m\). Since the two conjugate roots have modulus \(\sqrt2\), \(|L_m|\le2^{1+m/2}\), which gives strict positivity from \(m\ge6\); direct substitution gives differences \(48,48,0\) at \(m=3,4,5\). This completes the proof.

## Verification

The supplied standalone standard-library script `verify.py` constructs the 84-state transfer directly, builds both 42-state blocks, and computes their **full characteristic polynomials** by exact integer arithmetic. It independently reconstructs the original graph edge sets and directly enumerates all named three- and four-color assignments for the smallest two orders. It also checks the explicit constructions for all widths from 3 through 300 and compares the transfer trace to the closed twist correction through width 30. The replay produces `VERIFY_OK`. Finite checks validate the exact certificate and examples; the universal statements follow from the proved transfer identities, characteristic-polynomial certificate, and explicit periodic construction, not from guessing a pattern in sample counts.

## Relationship to prior work

The 2026 result of Lu, Ying, and Song establishes proper conflict-free four-choosability for connected subcubic graphs, a broader existence upper bound that also applies here. That bound does not establish the *absence* of three-colorings or count all optimal named four-colorings. Caro, Petruševski, and Škrekovski establish general bounds and basic-family results; examination of their accessible complete preprint found no Möbius-ladder enumeration. The established prism case concerns the **untwisted** closure and does not imply the row-exchange trace or its new spectral correction. The present theorem is an exact enumerative and structural classification for the twisted family, rather than an improvement to the general subcubic choosability theorem.

## Limitations

The theorem counts named colors for the standard antipodal-chord Möbius ladders only. It does not address arbitrary cubic graphs, additional palette sizes, or quotienting colorings by automorphisms. The full 2026 subcubic-list-coloring preprint was not accessible for a complete text comparison; its publicly available statement of the general upper bound was checked. Historical priority remains provisional, and no independent mathematical audit has been performed.

## References

- Zhijun Lu, Qirui Ying, Huimin Song, *Proper Conflict-Free Choosability for Graphs with Bounded Average Degree*, arXiv:2608.29375v1, first submitted August 29, 2026, https://arxiv.org/abs/2608.29375.
- Yair Caro, Mirko Petruševski, Riste Škrekovski, *Remarks on proper conflict-free colorings of graphs*, arXiv:2203.01088v1, March 2, 2022, https://arxiv.org/abs/2203.01088.
- Igor Fabrici, Borut Lužar, Simona Rindošová, Roman Soták, *Proper conflict-free and unique-maximum colorings of planar graphs with respect to neighborhoods*, arXiv:2202.02570v1, February 5, 2022, https://arxiv.org/abs/2202.02570.
