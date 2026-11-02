# Exact generating function for uniquely reconstructible ternary circular 2-gram profiles

## Finding
For a nonempty cyclic word \(w=w_0\cdots w_{n-1}\in\{0,1,2\}^n\), record \(m_{ij}=\#\{k\bmod n:(w_k,w_{k+1})=(i,j)\}\). Two words are equivalent under cyclic rotation, **not** under renaming alphabet symbols. Let \(U_n\) count the realizable matrices \(M=(m_{ij})\) for which all realizing cyclic words form one rotation class. Then
\[
\sum_{n\ge1}U_nz^n=\frac{z(6z^{10}-10z^8-14z^7-2z^6+4z^5+13z^4+7z^3+2z^2+3z+3)}{(1-z)^3(1+z)(1+z+z^2)}.
\]
The coefficients for \(n=1,\ldots,12\) are \(3,6,11,24,45,64,93,114,139,168,201,226\). Consequently \(U_n=n^2+O(n)\), with a degree-two quasipolynomial and period dividing six. The support of any such matrix has at most four positive off-diagonal entries.

## Assumptions and scope
All words are finite, nonempty, ternary, and circular. The cyclic pair count includes the wraparound pair from the last symbol to the first. A profile may use one, two, or three alphabet symbols. Multiplicities count parallel directed edges, whereas words identify parallel edges of the same label. The adjacency matrix is balanced and the positive-edge directed support is connected on its positive-degree vertices exactly when it arises from a cyclic word.

## Proof
**Rooted-count lemma.** Write \(d_i=\sum_jm_{ij}\), and let \(S\) be the set of vertices of positive degree. Let \(\tau(M)\) denote the number of directed spanning in-arborescences toward any fixed vertex of \(S\), with parallel-edge multiplicity (the value is independent of the root for balanced graphs). For a connected balanced \(M\) of total mass \(n\), the number \(T(M)\) of labeled *rooted* cyclic words realizing it is
\[
T(M)=n\tau(M)\frac{\prod_{i\in S}(d_i-1)!}{\prod_{i,j}m_{ij}!}.
\]
This is the Euler-tour/Markov-type formula, obtained by ordering outgoing arcs and dividing by parallel-edge permutations. A one-vertex loop-only graph has \(T(M)=1\). Each necklace contributes at most \(n\) rooted words, so \(T(M)>n\) proves ambiguity.

For positive-degree support of at least two vertices, write \(F(M)=T(M)/n\). Loops at vertex \(i\) multiply the loop-free \(F\) by \(\binom{r_i+a_i-1}{a_i}\), where \(r_i\) is its non-loop outdegree and \(a_i=m_{ii}\). This follows by cancelling factorials in the displayed formula. For a directed two-cycle, with each cross-edge multiplicity \(k\), or a directed three-cycle with all three cross-edge multiplicities \(k\), the loop-free \(F\) is \(1/k\); in each case adding loops gives
\[
F(M)=\frac1k\prod_{i\in S}\binom{k+a_i-1}{a_i}.
\]
Therefore \(F\le1\) exactly if either \(k=1\) (arbitrary loops) or \(k\ge2\) with at most one loop in total.

For exactly four positive cross-arcs there are two possible supports. First, two reciprocal pairs share a hub (a *bowtie*). Let their positive multiplicities be \(x,y\), and let \(a_0\) be the hub loop count, \(a_1,a_2\) the two leaf loop counts. Direct substitution gives
\[
F(M)=\frac1{x+y}\binom{x+y}{x}\binom{x+y+a_0-1}{a_0}\binom{x+a_1-1}{a_1}\binom{y+a_2-1}{a_2}.
\]
The factor \(\binom{x+y}{x}/(x+y)\) is one iff \(\min(x,y)=1\), and is greater than one otherwise. Thus \(F\le1\) exactly when the hub has no loops and loops at a leaf are allowed only if its pair multiplicity equals one. Second, the four cross-arcs form two directed simple cycles of lengths two and three sharing one directed edge (a *theta*). With respective cycle multiplicities \(x,y\), the base factor is the same; the two vertices on the shared edge have non-loop outdegree \(x+y\), while the third vertex has non-loop outdegree \(y\). Thus \(F\le1\) exactly when \(\min(x,y)=1\), no loops occur at either shared-edge vertex, and loops at the exclusive third vertex are allowed only when \(y=1\).

To rule out all remaining supports, suppose five positive cross-arcs occur. Up to vertex relabeling and reversing all arrows, the missing cross-arc is \(0\to2\); the five positive multiplicities are \(m_{01}=x+t,m_{10}=x,m_{12}=y+t,m_{21}=y,m_{20}=t\), with \(x,y,t\ge1\). The in-arborescence count is \((x+t)(y+t)\). In the loop-free formula the single-exit vertex contributes \(1/(x+t)\); the other two vertices yield
\[
F(M)=\frac{\binom{x+y+t}{x}}{x+y+t}\binom{y+t}{y}\ge y+t\ge2.
\]
Any additional loops only increase \(F\). If all six cross-arcs are positive, each row has two positive exits, hence its row multinomial is at least its non-loop outdegree; the arborescence count \(\tau\) is at least three, so \(F\ge3\). Thus none are unique. The only remaining cross-support possibility is zero cross-arcs, necessarily the loop-only one-letter word.

The cases with \(F=1\) always contain an arc of multiplicity one, so their cyclic words are primitive, each contributes exactly \(n\) distinct rooted rotations, and \(F=1\) means exactly one necklace. The cases with \(F<1\) are pure repeated two- or three-cycles, clearly giving a single periodic necklace. Therefore the conditions above are both necessary and sufficient, without assuming primitive words.

**Generating function.** Partitioning the complete classification into five disjoint support types, their positive-length series are:
\[
\begin{aligned}
L(z)&=\frac{3z}{1-z},\\
P(z)&=\frac{3z^2}{(1-z)^2}+\frac{3z^4+6z^5}{1-z^2},\\
R(z)&=\frac{2z^3}{(1-z)^3}+\frac{2z^6+6z^7}{1-z^3},\\
B(z)&=\frac{3z^4}{(1-z)^2}+\frac{6z^6}{(1-z^2)(1-z)},\\
H(z)&=\frac{6z^5}{(1-z^2)(1-z)}+\frac{6z^8}{1-z^3}.
\end{aligned}
\]
Here \(L\) is one-vertex loops, \(P\) is one reciprocal pair, \(R\) is one directed triangle, \(B\) is the bowtie, and \(H\) the shared-edge theta. The factors 3, 2, 3, and 6 count labeled choices of pair, triangle orientation, hub, and theta orientation respectively. For example, \(B\) has either two pairs used once with arbitrary loops at the leaves, or one pair used once and the other at least twice, with loops confined to the once-used leaf. The same counting proves the displayed formulas in the other cases. Summing the five rational series and reducing to a common denominator gives the theorem. Evaluating the numerator at \(z=1\) gives dominant singular part \(2/(1-z)^3\), proving \(U_n=n^2+O(n)\).

## Verification
The standalone standard-library Python program `verify.py` independently enumerates all circular ternary words through length nine, canonicalizes rotations, and checks their exact profile fibers. It separately enumerates every balanced three-state integer matrix through total mass 26, tests directed connectivity, calculates the number of necklaces by Euler rooted counts and Burnside's lemma, checks the five-family classification and all 26 coefficients. Burnside uses \(N(M)=\frac1n\sum_{d\mid\gcd(m_{ij})}\varphi(d)T(M/d)\). Recorded output appears in `verification_output.txt`. The proof above is all-length; these finite checks are corroboration, not a substitute.

## Relationship to prior work
Jacquet, Knessl and Szpankowski study enumeration of Markov types and asymptotics. Drmota and Szpankowski give the rational generating function for all balanced ternary transition matrices and distinguish balanced matrices from cyclically realizable profiles, but do not give the present **single-necklace-fiber** generating function or its five-family reconstruction classification. Bals, Pissis and Tinca develop efficient Euler-trail enumeration in directed graphs (first public 2026), focusing on enumerating trails for given inputs rather than uniquely reconstructible ternary cyclic profiles over all lengths. The present distinction is counting *profiles whose fiber contains exactly one necklace*, not counting arbitrary balanced profiles, cyclic necklaces, or individual Euler trails.

## Limitations
The exact classification is for a labeled three-symbol alphabet and cyclic adjacent-pair counts only, not linear words, longer windows, four or more symbols, or uniqueness under arbitrary alphabet permutation. The result uses classical Euler-tour enumeration and makes no claim that these classical ingredients are new. Bibliographic coverage can miss unindexed equivalent statements; independent mathematical audit is not yet performed.

## References
- Bals, Pissis and Tinca, *Optimal Enumeration of Eulerian Trails in Directed Graphs*, arXiv:2603.12894 (first public March 13, 2026), https://arxiv.org/abs/2603.12894.
- Jacquet, Knessl and Szpankowski, *Counting Markov Types* (2010), https://www.cs.purdue.edu/homes/spa/papers/aofa10.pdf.
- Drmota and Szpankowski, *Analytic Information Theory: From Compression to Learning*, draft (2022), Chapter 11.2, https://www.cs.purdue.edu/homes/spa/temp/ait22.pdf.
