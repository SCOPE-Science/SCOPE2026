# Exact period-three and period-four attractor spectrum of three-color cyclic competition on complete bipartite graphs

## Finding
Let \(a,b\geq 1\) be integers. Run the synchronous three-color **cyclic cellular automaton** (CCA) on the simple, loopless complete bipartite graph \(K_{a,b}\): a vertex of color \(i\in\mathbb Z/3\mathbb Z\) increases its color to \(i+1\) modulo three if and only if it has a neighbor of color \(i+1\); otherwise it retains \(i\). Write \(F\) for the global map. Define the number of onto colorings using \(k\) specified colors by
\[
U_k(n)=\sum_{j=0}^{k}(-1)^j\binom{k}{j}(k-j)^n,\qquad k\in\{1,2,3\},\ n\ge1.
\]
In particular, \(U_1(n)=1\), \(U_2(n)=2^n-2\), and \(U_3(n)=3^n-3\cdot2^n+3\).

**Complete recurrent census.** Every orbit has exact eventual period one, three, or four; there are no other eventual periods. The numbers of labeled configurations *already* on cycles of those exact periods are respectively
\[
R_1=3,\qquad R_3=U_3(a)U_3(b),\qquad R_4=6U_2(a)U_2(b).
\]
Thus the numbers of distinct primitive three-cycles and four-cycles are \(U_3(a)U_3(b)/3\) and \(3U_2(a)U_2(b)/2\), and the dynamical zeta function is
\[
\zeta_F(t)=(1-t)^{-3}(1-t^3)^{-U_3(a)U_3(b)/3}(1-t^4)^{-3U_2(a)U_2(b)/2}.
\]
Four-cycles exist precisely when \(\min(a,b)\ge2\); three-cycles exist precisely when \(\min(a,b)\ge3\). In particular, three colors can generate primitive period four on a bipartite graph.

**Exact transient-depth census.** Let \(D_r\) count initial labeled configurations whose least time of entry into their eventual periodic orbit equals \(r\). Abbreviating \(u=U_2(a)\), \(v=U_2(b)\), \(s=U_3(a)\), and \(w=U_3(b)\), one has
\[
\begin{aligned}
D_0&=3+6uv+sw,\\
D_1&=6+3(u+v)+3uv+3(uw+sv),\\
D_2&=6(u+v)+3(s+w),\\
D_r&=0\qquad(r\ge3).
\end{aligned}
\]
Hence \(F^{14}=F^2\) as maps on all configurations, and two updates are necessary for some initial condition whenever \(\max(a,b)\ge2\). If \(a=b=1\), the sharp bound is one update. The probability of already lying on a three-cycle under independent uniform initial colors tends to one as \(\min(a,b)\to\infty\), because \(R_3/3^{a+b}\to1\).

## Assumptions and scope
All vertices are labeled, so the counts are for actual configurations rather than quotient classes under graph automorphisms. Both bipartition classes are nonempty, the three colors are distinguished, the update is parallel and synchronous, and no state is automatically advanced. In particular this is the cyclic cellular automaton, **not** the Greenberg–Hastings update rule. A periodic configuration is one for which some positive iterate of \(F\) returns it; transient depth is the least nonnegative iterate at which the configuration is periodic.

## Proof
**1. A finite support quotient valid for every \(a,b\).** For each configuration \(x\), let \(A(x),B(x)\) be the nonempty sets of colors occurring on its first and second parts. For any nonempty \(S\subseteq\mathbb Z/3\mathbb Z\), define
\[
f_S(i)=\begin{cases}i+1\pmod3,&i+1\pmod3\in S,\\i,&\text{otherwise.}\end{cases}
\]
Every vertex in a given part with color \(i\) updates by the same map, so the support dynamics closes exactly as
\[
T(A,B)=\bigl(f_B(A),f_A(B)\bigr).
\]
There are only seven choices of nonempty support on each side, hence exactly \(49\) support pairs. This quotient is exact: there is no approximation or dependence on multiplicities of colors inside their supports.

**2. Exhaustive symbolic support classification.** On the \(49\) support pairs, the periodic pairs are precisely the following \(10\): the three equal singleton pairs \((\{i\},\{i\})\); the six ordered pairs of *different* two-color subsets; and the full/full pair \((\{0,1,2\},\{0,1,2\})\). Every other support pair maps to one of these within at most two steps. More precisely, the number of support pairs with initial support sizes \((i,j)\) and first periodic support at depth \(r\) is the \((i,j)\)-entry of the following three matrices, with row and column sizes ordered \(1,2,3\):
\[
H_0=\begin{pmatrix}3&0&0\\0&6&0\\0&0&1\end{pmatrix},\qquad
H_1=\begin{pmatrix}6&3&0\\3&3&3\\0&3&0\end{pmatrix},\qquad
H_2=\begin{pmatrix}0&6&3\\6&0&0\\3&0&0\end{pmatrix}.
\]
This is a finite exact computation, with a short direct case check: unequal singleton pairs collapse to equal singleton pairs after one step; identical two-color supports collapse to a singleton pair after one step; distinct two-color supports form three two-cycles of support pairs; full/full is fixed; supports of sizes \((1,3)\) or \((3,1)\) always need two steps; those of sizes \((2,3)\) or \((3,2)\) need one; and for \((1,2)\) or \((2,1)\) exactly three of the nine ordered choices need one step and the other six need two. A representative of the last case is \((\{0\},\{0,2\})\), which needs one step, whereas \((\{0\},\{0,1\})\) needs two. These symmetry classes account for all \(49\) possibilities; the standalone enumerator also reproduces all entries by evaluating their definitions.

**3. Lifting periods back to labeled configurations.** If an orbit of support pairs closes, the induced color map between consecutive supports on each side must be a bijection: the supports in a cycle return to the same finite cardinalities, while each image is the full successor support. Hence every labeled configuration above a periodic support pair is periodic. For an equal singleton support pair the dynamics is fixed. For full/full supports every vertex advances by one each step, with exact period three. For distinct two-color supports the support pairs alternate, and the two-step return map swaps the two color classes on each side; thus every such configuration has exact period four. For example, starting at \((\{0,1\},\{0,2\})\), the first support update gives \((\{0,2\},\{0,1\})\), and the second returns the supports but interchanges the two actual colors within each part. Conversely, if a configuration is recurrent its support pair must be recurrent, so there are no other recurrent states or periods. This also shows that first entry of the support pair into the periodic support set is exactly first entry of the complete configuration into its periodic orbit.

**4. Counting labels and transient depths.** With a prescribed support of size \(k\) on a part of \(n\) labeled vertices, there are exactly \(U_k(n)\) colorings by inclusion–exclusion. Multiplying the counts for the two parts and weighting by the appropriate entry in \(H_r\) yields \(D_0,D_1,D_2\). The \(H_0\) entries and exact return periods yield \(R_1,R_3,R_4\). The identities \(D_0+D_1+D_2=3^{a+b}\) and \(F^{14}=F^2\) follow, since every periodic orbit has length dividing twelve. For sharpness of transient two, place color \(0\) on one singleton-support part and both colors \(0,1\) on the other: the support sequence is
\[
(\{0\},\{0,1\})\longrightarrow(\{1\},\{0,1\})\longrightarrow(\{1\},\{1\}).
\]
The same construction works with additional vertices of either color in either part and with the bipartition reversed.

## Verification
The supplied `verify.py` independently implements the \(49\)-state support map and the vertex-level update on labeled graphs. It computes the entire periodic-support set, the three exact depth matrices, and the color-class return permutations. Separately, a direct state-graph enumeration over \(22\) parameter pairs and \(24,606\) labeled configurations confirms the predicted periods, depths and enumerations. The reproducible output is included in `verification_output.txt`. These experiments check the finite quotient and small instances; the all-size conclusion follows from the exact support-factor proof, not from extrapolating finite graph sizes.

## Relationship to prior work
Durrett and Griffeath's 1993 study introduced and analyzed cyclic excitable automata with lattice geometries and thresholds. Gravner, Lyu and Sivakoff's 2016 preprint establishes a general finite-graph criterion for synchronization of three-color CCA, together with an activity formula from cycle circulations. Applied to a complete bipartite graph, that general result constrains synchronization and activity but does not directly enumerate all labeled periodic configurations, distinguish their primitive periods and individual orbit counts, or give this complete first-entry-depth distribution. The exact full-support and two-support orbit classification above supplies those finer invariants. Prior exact counts for the Greenberg–Hastings rule or binary parity/majority rules do not imply these formulas, because the local update operators differ: the present CCA has three monochromatic fixed points, whereas the three-state Greenberg–Hastings rule has only the all-rest fixed point. They are not conjugate dynamical systems. The present work does not claim discovery of the general synchronization criterion or of the CCA rule itself.

## Limitations
The result is restricted to three colors, threshold-one cyclic consumption, two nonempty complete bipartition classes, deterministic synchronous updates, and labeled states. No claim is made for general graph families, more colors, asynchronous dynamics or the Greenberg–Hastings rule. The literature comparison cannot rule out an unindexed equivalent enumeration, although no direct covering statement was identified among the examined sources. No independent external audit has been performed.

## References
1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, initial arXiv release 1993-03-22, arXiv:patt-sol/9303002, https://arxiv.org/abs/patt-sol/9303002.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, initial arXiv release 2016-10-24, arXiv:1610.07320, https://arxiv.org/abs/1610.07320; *Annals of Applied Probability* **28** (2018), DOI 10.1214/17-AAP1350.
3. M. Matamala and E. Moreno, *Dynamic of cyclic automata over \(\mathbb Z^2\)*, *Theoretical Computer Science* **322** (2004), 369–381, DOI 10.1016/j.tcs.2004.03.018 (two-dimensional infinite-grid rather than complete-bipartite finite-volume behavior).
