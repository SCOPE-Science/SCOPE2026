# Optimal proper conflict-free colouring census for cycle prisms

## Finding

Let \(G_n=C_n\square K_2\) be the simple, vertex-labelled two-row prism with \(n\ge3\). A *proper conflict-free* colouring is a proper vertex colouring in which every vertex has a colour appearing exactly once among its open neighbours. For an available palette of \(q\) named colours, let \(A_q(n)\) be the number of such colourings, allowing some names to be unused.

For every \(n\ge3\),
\[
A_3(n)=\begin{cases}12,&3\mid n,\\0,&3\nmid n.\end{cases}
\]
Define the integer polynomial
\[
\begin{aligned}
R(t)={}&(1-2t)(1-t)^6(1+t)^2(1+t+2t^2)^3\\
&\cdot(1-t-2t^3)^2(1-4t-6t^2+4t^3)\\
&\cdot(1+3t+6t^2-2t^3+4t^4)^3.
\end{aligned}
\]
Then the **complete four-colour census** is the formal-power-series identity
\[
\boxed{\sum_{n\ge3}A_4(n)t^n=-t\frac{R'(t)}{R(t)}.}
\]
In particular \(A_4(3)=264\), \(A_4(4)=384\), \(A_4(5)=3600\), and \(A_4(6)=17472\). Consequently the minimum proper conflict-free palette size equals \(3\) when \(3\mid n\) and \(4\) otherwise; there are exactly \(12\) named optimal three-colourings when \(3\mid n\), and exactly \(A_4(n)\) named optimal four-colourings otherwise. The number of *surjective* four-colourings is \(A_4(n)-4A_3(n)\).

Let \(\rho\) be the unique real zero in \((5,6)\) of \(x^3-4x^2-6x+4\). There is also the asymptotic refinement
\[
A_4(n)=\rho^n+O(5^n),\qquad
\Pr(\text{proper conflict-free}\mid\text{uniform proper four-colouring})\sim (\rho/7)^n.
\]
Numerically \(\rho\approx5.03404184\). The probability is over all proper colourings of the labelled prism using colours from the fixed palette of four.

## Assumptions and scope

The two cycles have vertices \(u_i\) and \(v_i\), with \(i\in\mathbb Z/n\mathbb Z\), and the edges are \(u_iu_{i+1}\), \(v_iv_{i+1}\), and \(u_iv_i\). All colour names and all vertex positions are distinguished. There is no quotient by rotations, reflections, or colour permutations. The graph is cubic for every stated \(n\). Open neighbourhoods, rather than closed neighbourhoods, are used. This is ordinary proper conflict-free colouring; no list or weighted constraint is imposed.

For a cubic graph, a proper colouring is proper conflict-free precisely when its three neighbours are not monochromatic: a multiset of three colours has a singleton if and only if it is not constant. This is also called proper \(2\)-dynamic colouring on cubic graphs. An assignment can use either two or three distinct colours in a neighbourhood, not necessarily a uniform number at every vertex.

## Proof

**1. A bijective transfer representation.** For \(q\ge2\), let \(S_q=\{(a,b)\in\{0,\ldots,q-1\}^2:a\ne b\}\). A column has state \(s_i=(c(u_i),c(v_i))\in S_q\). Write \(s\sim t\) when their first entries differ and their second entries differ. The state set \(E_q\) consists of ordered pairs \((s,t)\in S_q^2\) for which \(s\sim t\). Its sizes are \(|E_3|=18\) and \(|E_4|=84\).

Define a zero-one matrix \(T_q\), indexed by \(E_q\), with the entry from \((s,t)\) to \((t',r)\) equal to one precisely when \(t=t'\), \(t\sim r\), and
\[
\left|\{s_1,r_1,t_2\}\right|\ge2,
\qquad \left|\{s_2,r_2,t_1\}\right|\ge2.
\]
Here the subscripts 1 and 2 mean the upper and lower colour coordinates. The two inequalities are exactly the nonmonochromatic open-neighbourhood conditions at the middle column \(t\). Thus, for every \(n\ge3\), the map from a colouring to its consecutive ordered-column pairs is a bijection with length-\(n\) closed walks whose initial pair corresponds to the distinguished column boundary. Hence
\[
A_q(n)=\operatorname{tr}(T_q^n).
\]
The finite matrices are defined completely by the displayed conditions; no undisclosed table is required.

**2. Exact finite characteristic-polynomial identities.** Writing \(x\) for a characteristic variable, exact integer arithmetic gives
\[
\det(xI-T_3)=x^6(x^3-1)^4
\]
and
\[
\begin{aligned}
\det(xI-T_4)={}&x^{48}(x-2)(x-1)^6(x+1)^2(x^2+x+2)^3\\
&\cdot(x^3-x^2-2)^2(x^3-4x^2-6x+4)\\
&\cdot(x^4+3x^3+6x^2-2x+4)^3.
\end{aligned}
\]
These are finite identities, not guesses from initial terms. The accompanying `verify.py` independently constructs both matrices and checks **every characteristic coefficient** by exact Newton identities from traces through degrees \(18\) and \(84\), respectively. This gives a complete reproducible finite-arithmetic certificate for the required nonstandard computation.

For any finite matrix \(T\), the formal trace identity
\[
-t\frac{d}{dt}\log\det(I-tT)=\sum_{n\ge1}\operatorname{tr}(T^n)t^n
\]
follows formally by the power-series identity for the matrix logarithm, or Newton's identities. The displayed characteristic polynomials give \(\det(I-tT_3)=(1-t^3)^4\) and \(\det(I-tT_4)=R(t)\). For \(q=3\) this yields \(12t^3/(1-t^3)\), proving the first formula. For \(q=4\) it gives the second. Both sequences have zero terms in degrees one and two.

**3. Sharp palette and actual existence.** No proper conflict-free colouring of any cubic prism uses just two colours: a connected proper two-colouring, when one exists, makes every open neighbourhood monochromatic. The three-colour count above proves the divisibility obstruction. Four colours suffice for all \(n\ge3\), independently of the positivity of the formula: the following three cyclic lists of upper/lower column states, with four named colours \(0,1,2,3\), satisfy every transition condition:
\[
\begin{aligned}
&(0,1),(1,0),(2,3);\\
&(0,1),(1,0),(2,3),(3,2);\\
&(0,1),(1,0),(2,3),(0,1),(2,3).
\end{aligned}
\]
They give closed walks of lengths \(3,4,5\) all based at the same two-column state \(((0,1),(1,0))\). Concatenating the closed walks produces every length \(n\ge3\), since every such integer is a nonnegative sum of \(3,4,5\). Thus the minimum palette sizes and optimal multiplicities follow. Any valid assignment on fewer than four colours uses exactly three, since two colours never suffice; selecting its three colour names from four gives exactly \(4A_3(n)\) nonsurjective assignments.

**4. Asymptotics.** The cubic factor \(x^3-4x^2-6x+4\) has three real roots in \((-2,-1)\), \((0,1)\), and \((5,6)\), as certified by endpoint signs. All roots of \(x^4+3x^3+6x^2-2x+4\) have modulus less than \(5\), since on \(|x|=5\) the leading \(|x^4|=625\) exceeds \(3|x|^3+6|x|^2+2|x|+4=539\) (Rouché's theorem). The other nontrivial factors also have every root of modulus below \(5\), by the analogous leading-term comparison or direct quadratic bounds. The isolated dominant eigenvalue \(\rho>5\) has multiplicity one, so the exact trace formula gives \(A_4(n)=\rho^n+O(5^n)\). The ordinary proper four-colouring transfer on single columns has simple dominant eigenvalue \(7\), all others of modulus at most \(3\), so its total number of proper colourings is \(7^n+O(3^n)\). Dividing the two estimates gives the probability formula.

## Verification

Run `python3 verify.py` from the extracted package directory; only the Python standard library is required. This script reconstructs the transfer matrices, checks their dimensions and entries, obtains the entire stated characteristic polynomials using integer traces and Newton identities, verifies the rational generating-series coefficients, and independently enumerates all four-colour assignments for cycle lengths three through five and all three-colour assignments for lengths three through seven. It also checks the claimed three-, four-, and five-column constructive cycles and a separate three-distinct-neighbour transition count. The actual replay yields `VERIFY_OK` after `CHARPOLY_OK`, `RATIONAL_SERIES_OK`, `TRANSFER_OK`, `DIRECT_OK assignments 6498957`, `HOMOGENEOUS_OK`, and `CONSTRUCTIVE_OK`.

This fixed-size exact computation proves the finite determinant identities used in the universal proof. The direct enumerations test smaller graphs only; they are not used as an infinite extrapolation. The universal step is the trace identity applied to the finite transfer matrices.

## Relationship to prior work

The September 2026 work of Qi, Song and Cao motivates proper conflict-free colouring via general list-colouring guarantees for sparse graphs of large girth. It does not supply a prism colour-count formula. The prism-specific 2023 theorem of Madaras and Šurimová proves the existence ranges of uniform \(2\)-homogeneous prism colourings, including the three-colour divisibility condition. Its Theorem 3 reports allowable palette sizes, not the present exact named-colouring counts, and the present proper conflict-free class also allows mixed neighbourhood colour degrees. The 2026 analysis by Allagan, Voloshin, Deriglazov and Lopez-Bonilla determines the ordinary prism chromatic polynomial and its spectral branches. Ordinary proper colourings are a larger class, so that enumeration does not determine this constrained four-colour census. The present result does not claim novelty for the concept of conflict-free colouring, the existence threshold alone, or the general transfer-matrix method.

## Limitations

The exact enumerator concerns only available palettes of three and four named colours and simple labelled prisms of length at least three. It is not a full polynomial in arbitrary palette size, a list-colouring theorem, or a classification modulo symmetry. A published general dynamic-colouring enumeration not located during the literature comparison could have an implicit specialization to these counts. An independent mathematical assessment and comprehensive historical-priority review have not been performed.

## References

1. X. Qi, H. Song, Z. Cao, *Proper conflict-free choosability of sparse graphs with girth at least seven*, arXiv:2609.11249v1, publicly submitted 2026-09-10, https://arxiv.org/abs/2609.11249.
2. T. Madaras, M. Šurimová, *Homogeneous colourings of graphs*, Mathematica Bohemica 148 (2023), 105–115, Theorem 3, doi:10.21136/MB.2022.0007-21, https://dml.cz/dmlcz/151530.
3. J. Allagan, V. Voloshin, V. Deriglazov, R. N. Lopez-Bonilla, *Explicit Equimodular Curves for Prism-Graph Chromatic Polynomials and the Beraha-Kahane-Weiss Limit Set*, American Journal of Computational Mathematics 16 (2026), 14–26, doi:10.4236/ajcm.2026.161002, https://www.scirp.org/journal/paperinformation?paperid=150405.
4. E.-K. Cho, I. Choi, H. Kwon, B. Park, *Proper conflict-free coloring of sparse graphs*, arXiv:2203.16390, https://arxiv.org/abs/2203.16390 (foundational terminology).
