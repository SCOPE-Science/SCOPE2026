# The Klein-four homology character of \(\operatorname{Ind}(K_2\times K_q\times K_q)\)

## Finding

For every integer \(q\ge 2\), put
\[
X_q=\operatorname{Ind}(K_2\times K_q\times K_q).
\]
The two simplicial involutions
\[
s(a,i,j)=(1-a,i,j),\qquad t(a,i,j)=(a,j,i)
\]
commute and generate \(V_4\cong C_2\times C_2\). Their rational third-homology character, in the order \((1,s,t,st)\), is
\[
\boxed{\chi_q=\left(\frac{(q-1)^2(q^2-2)}{2},\ (q-1)^2,\ -(q-1)^2,\ 1-q\right).}
\]
Every other reduced rational homology group vanishes. Writing \(B_q=(q-1)^2(q^2-2)/2\), the one-dimensional \(V_4\) character taking values \(\epsilon\) on \(s\) and \(\delta\) on \(t\), where \(\epsilon,\delta\in\{\pm1\}\), occurs with multiplicity
\[
\boxed{m_{\epsilon,\delta}=\frac{B_q+\epsilon(q-1)^2-\delta(q-1)^2+\epsilon\delta(1-q)}4.}
\]
In particular,
\[
\boxed{\widetilde H_3(|X_q|/V_4;\mathbb Q)\cong
\mathbb Q^{\frac{(q-1)^2(q^2-2)-2(q-1)}8},}
\]
and the other reduced rational homology groups of the orbit space vanish.

## Assumptions and scope

All complete graphs \(K_q\) have \(q\) vertices and no loops. The *categorical* product of simple graphs has an edge between distinct tuples exactly when all corresponding coordinates differ. Thus the vertices of the underlying graph are \((a,i,j)\) with \(a\in\{0,1\}\) and \(i,j\in\{1,\ldots,q\}\); two vertices are adjacent precisely when \(a\ne b\), \(i\ne k\), and \(j\ne l\). A face of its independence complex is an edge-free vertex set. The involutions \(s,t\) are actual graph automorphisms; no action of the larger automorphism group is asserted. Homology is reduced rational singular/simplicial homology. The claim is for *all* integers \(q\ge2\).

## Proof

**1. Concentration.** Antolín Camarena and Carnero Bravo [1, Proposition 25], treating exactly the categorical products in question, prove
\[
X_q\simeq\bigvee^{B_q}S^3,
\qquad B_q=\frac{(q-1)^2(q^2-2)}2.
\]
This published nonequivariant theorem establishes the homology concentration and the identity trace, but does not determine the involution actions.

**2. Signed fixed-face principle.** For a finite simplicial automorphism \(g\) of \(X_q\), the Lefschetz number equals the Euler characteristic of the fixed-point realization, after barycentric subdivision if needed. Since the only nonzero reduced homology is in degree three,
\[
\chi(|X_q|^g)=1-\operatorname{tr}(g_*|\widetilde H_3(X_q;\mathbb Q)).
\]
Alternatively, let \(F\) range over all \(g\)-invariant independent vertex sets, including the empty face, and let \(r_g(F)\) be their number of \(g\)-orbits of vertices. The sign of \(g\) on the oriented simplex \(F\) is \((-1)^{|F|-r_g(F)}\), so the augmented simplicial chain trace gives the useful exact identity
\[
\operatorname{tr}(g_*|\widetilde H_3(X_q;\mathbb Q))
=\sum_{F\,\text{invariant, independent}}(-1)^{r_g(F)}.
\]
These two expressions agree, including the empty-face convention.

**3. Sheet interchange \(s\).** An orbit of \(s\) is a pair \(\{(0,i,j),(1,i,j)\}\), which is independent. The union of such pairs is independent if and only if the index pairs \((i,j)\) form an independent set of the graph \(K_q\times K_q\). Thus the fixed-point realization is the independence complex of that product. By Goyal–Shukla–Singh [2], also restated as [1, Proposition 8], it is a wedge of \((q-1)^2\) circles. Therefore
\[
1-\chi_q(s)=1-(q-1)^2,
\qquad \chi_q(s)=(q-1)^2.
\]

**4. Combined interchange \(st\).** An orbit based at \((0,i,j)\) consists of \((0,i,j)\) and \((1,j,i)\). If \(i\ne j\) these two are adjacent, so no invariant independent set may contain that orbit. When \(i=j\), the orbit is independently allowable. Two distinct diagonal orbits are mutually incompatible, so the fixed-point realization consists of \(q\) isolated points. Hence
\[
1-\chi_q(st)=q,
\qquad\chi_q(st)=1-q.
\]

**5. Equal-coordinate interchange \(t\).** Orbits of \(t\) remain within a sheet, and each orbit is independent. Index orbits are the \(q\) diagonal symbols \(d_i=\{(i,i)\}\) and \(h=\binom q2\) off-diagonal symbols \(e_{ij}=\{(i,j),(j,i)\}\) for \(i<j\). Denote their sets by \(D\) and \(E\). There are two copies of \(D\cup E\), one per sheet, with no incompatibilities within either sheet. Cross-sheet incompatibility is as follows:

- \(d_i\) conflicts with \(d_j\) precisely when \(i\ne j\).
- \(d_i\) conflicts with \(e_{jk}\) precisely when \(i\notin\{j,k\}\).
- **Every** \(e_{ij}\) conflicts with **every** \(e_{kl}\), including itself; choose opposite ordered representatives to witness an edge.

By the signed fixed-face identity, \(\chi_q(t)\) is the independence polynomial of this bipartite incompatibility graph at \(-1\). Sum first over selected orbit vertices \(U=S_D\cup S_E\) in sheet zero. The signed sum over compatible selections on sheet one is zero unless \(U\) conflicts with **every** orbit on sheet one (in which case that sum is one). We thus add \((-1)^{|U|}\) only over such fully dominating \(U\).

If \(S_E=\varnothing\), exactly \(|S_D|\ge3\) works; the signed contribution is
\[
A=\sum_{k=3}^q(-1)^k\binom qk=-1+q-\binom q2.
\]
If \(S_E\ne\varnothing\) and \(|S_D|\ge2\), all second-sheet vertices are blocked, giving
\[
B=\Big(\sum_{k=2}^q(-1)^k\binom qk\Big)
\Big(\sum_{r=1}^{h}(-1)^r\binom hr\Big)=-(q-1).
\]
If \(|S_D|=1\), say \(S_D=\{d_i\}\), domination requires at least one chosen \(e_{jk}\) not containing \(i\). Its signed contribution cancels to zero: the total signed sum over nonempty subsets of \(E\) is \(-1\), as is the sum over nonempty subsets of the \(q-1\) off-diagonal symbols containing \(i\).

Finally, if \(S_D=\varnothing\), a nonempty \(S_E\) dominates the opposite diagonal vertices precisely when its selected unordered pairs have empty common intersection. The signed sum over *all* nonempty subsets of \(E\) is \(-1\). For any given index \(i\), the nonempty subsets made only of edges containing \(i\) have signed sum \(-1\). Inclusion–exclusion over these \(q\) stars has only nonempty one-star and two-star intersections (two stars share the single symbol \(e_{ij}\)); hence the signed sum for **nonempty common intersection** is \(-q+\binom q2\). Subtracting gives
\[
C=-1+q-\binom q2.
\]
These arguments and binomial sums remain valid at the boundary \(q=2\). Thus
\[
\boxed{\chi_q(t)=A+B+C=-(q-1)^2.}
\]

**6. Decomposition and quotient.** The four irreducible rational characters of \(V_4\) are the one-dimensional sign choices \((\epsilon,\delta)\). Their multiplicities are the inner products with \(\chi_q\), yielding the displayed formula. Rational homology of a finite-group quotient is the invariant homology of a barycentrically subdivided simplicial complex: over \(\mathbb Q\), averaging is exact, and the orbit cellular chains are the invariant chains. Hence the quotient has the displayed third reduced Betti rank \(m_{+,+}\) and no other reduced homology.

## Verification

The complete finite checker `check_klein_character.py` enumerates **every** independent face for \(q=2,3\), directly computes all four signed invariant-simplex traces, and agrees with the theorem: respectively \((1,1,-1,-1)\) and \((14,4,-4,-2)\). Independently within that program, its second algorithm enumerates subsets of coordinate-swap orbit-vertices and confirms \(\chi_q(t)=-(q-1)^2\) for \(q=2,3,4,5\). Character orthogonality, nonnegative integral multiplicities, and their sum are checked for every integer \(2\le q\le100\). Exact stdout is in `klein_character_checks.txt`. These finite tests support the proof but **do not** replace the all-parameter argument above.

## Relationship to prior work

The **nonequivariant** sphere-wedge classification for the full graph family is [1, Proposition 25] (first public July 23, 2023), so neither its dimension nor Betti count is claimed as new. The two-factor fixed-point homotopy calculation is [2] and [1, Proposition 8]. The new result computes three involution traces and the resulting complete \(V_4\)-module and quotient homology, which nonequivariant homotopy equivalences cannot imply. The full relevant sections of [1] and the relevant product-complex results in [2] were checked; no claim of exhaustive global literature indexing is made.

## Limitations

Only rational homology and the displayed natural four-element symmetry subgroup are determined; this does not give integral homology or the homotopy type of the quotient, nor the representation under all coordinate permutations. The argument relies on the previously published nonequivariant homotopy theorem. Searches and inspection of relevant primary sources did not identify an equivalent equivariant classification, but an unindexed equivalent statement remains possible. There is no independent external review or certification.

## References

[1] Omar Antolín Camarena and Andrés Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401 (first public 2023-07-23), Proposition 25 and Proposition 8; https://arxiv.org/html/2307.12401v2 .

[2] Shuchita Goyal, Samir Shukla, and Anurag Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926 (first public 2019-05-16), categorical two-factor product result; https://arxiv.org/abs/1905.06926 .
