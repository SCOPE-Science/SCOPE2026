# Dihedral quotient Euler characteristics of squared-cycle independence complexes

## Finding
For every integer \(n\ge6\), let \(C_n^2\) be the graph on \(\mathbb Z/n\mathbb Z\) in which two different vertices are adjacent exactly when their circular distance is at most two. Set \(K_n=\operatorname{Ind}(C_n^2)\), and let \(D_n=\langle r,s:r^n=s^2=1,\ srs=r^{-1}\rangle\), where \(r(i)=i+1\) and \(s(i)=-i\). Define the integer sequences
\[
A_j=1\quad(j\le0),\qquad A_1=0,\quad A_2=-1,\qquad A_j=A_{j-1}-A_{j-3}\quad(j\ge3),
\]
\[
W_1=W_2=1,\quad W_3=-2,\quad W_4=-3,\quad W_5=-4,\qquad W_j=W_{j-1}-W_{j-3}\quad(j\ge6).
\]
Put \(F(d)=1\) for \(d=1,2\), and \(F(d)=W_d\) for \(d\ge3\). For an element \(g\in D_n\), let \(\mathcal L_n(g)=\sum_{q\ge0}(-1)^q\operatorname{tr}(g_*\mid\widetilde H_q(K_n;\mathbb Q))\) denote its reduced Lefschetz character. Then
\[
\mathcal L_n(r^a)=-F(\gcd(n,a)).
\]
For odd \(n=2h+1\), every reflection has
\[
\mathcal L_n(r^as)=-(A_{h-2}-A_{h-3}).
\]
For even \(n=2h\),
\[
\mathcal L_n(r^as)=
\begin{cases}
-(A_{h-3}-2A_{h-4}+A_{h-5}),&a\text{ even (two fixed vertices)},\\
-A_{h-2},&a\text{ odd (no fixed vertices)}.
\end{cases}
\]
Consequently the **ordinary topological quotient** of the geometric realization has the exact reduced Euler characteristic
\[
\boxed{\displaystyle
\widetilde\chi(|K_n|/D_n)=-\frac{1}{2n}\left(\sum_{d\mid n}\varphi(n/d)F(d)+R_n\right),
}
\]
where \(\varphi\) is Euler's totient and
\[
R_n=\begin{cases}
n(A_{(n-5)/2}-A_{(n-7)/2}),&n\text{ odd},\\
\frac n2(A_{n/2-3}-2A_{n/2-4}+A_{n/2-5}+A_{n/2-2}),&n\text{ even}.
\end{cases}
\]
The value is an integer for every \(n\ge6\). Furthermore **the absolute values of these quotient Euler characteristics are unbounded** as \(n\to\infty\); thus infinitely many of the dihedral quotients have nonzero reduced rational homology.

## Assumptions and scope
All faces of \(K_n\) are sets of vertices having pairwise circular distance at least three. The empty face is included for chain-level alternating traces. The dihedral quotient refers to the topological orbit space of the geometric realization, not to the generally incorrect naive quotient of the un-subdivided vertex labels. All Lefschetz traces and the inferred nonvanishing homology are rational; the Euler characteristic is integral. No claim is made about individual Betti numbers, integral quotient torsion, equivariant homotopy type, or geometric contractibility.

## Proof
**1. Signed fixed-orbit lemma.** Let \(g\) be any simplicial permutation of a finite independence complex \(\operatorname{Ind}(G)\). If an independent set \(S\) is fixed setwise and comprises \(u\) cycles of the permutation induced by \(g\) on its elements, its oriented simplex contributes \((-1)^{|S|-1}(-1)^{|S|-u}=(-1)^{u-1}\) to the reduced chain Lefschetz trace; the empty face contributes \(-1\). Discard each orbit of \(g\) that contains an edge of \(G\), and construct the conflict graph \(B_g\) on the remaining vertex orbits, joining two orbits if any original graph edge connects them. Setwise invariant independent sets are exactly unions of independent collections of vertices in \(B_g\). Thus
\[
\mathcal L(g)=-I(B_g,-1),\qquad I(B,z)=\sum_{T\text{ independent in }B}z^{|T|}.
\]
The reduced homology equality follows from the Hopf trace theorem applied to the augmented oriented simplicial chain complex. This explicitly accounts for orientation reversals of invariant simplices.

**2. Rotations.** If \(g=r^a\), put \(d=\gcd(n,a)\) with \(\gcd(n,0)=n\). Each orbit is a congruence class modulo \(d\). If \(d=1\) or \(d=2\), every orbit contains a pair at circular distance one or two and is therefore inadmissible, so \(I(B_g,-1)=1\). For \(d\ge3\), the orbits are internally independent, and their pairwise conflict graph is exactly \(C_d^2\), including the complete-graph conventions at \(d=3,4,5\). Write \(W_d=I(C_d^2,-1)\). A cyclic binary word recording selected vertices is admissible exactly when every selected \(1\) is followed cyclically by at least two zeros. A three-state transfer counts these weighted cyclic words: the states record whether zero, one, or at least two zeros have followed the last selected vertex. Reading rows as source states, its signed transition matrix is \(T=\begin{pmatrix}0&1&0\\0&0&1\\-1&0&1\end{pmatrix}\). Closing the state path gives \(W_d=\operatorname{tr}(T^d)\), for every \(d\ge3\). Since \(\det(\lambda I-T)=\lambda^3-\lambda^2+1\), the trace sequence satisfies \(W_d=W_{d-1}-W_{d-3}\). Direct counts give \(W_3=-2,W_4=-3,W_5=-4\), proving the prescribed \(F\) and the rotational formula. Alternatively, for all \(d\ge3\) this transfer can be checked against the explicit count
\[
W_d=\sum_{k=0}^{\lfloor d/3\rfloor}(-1)^k\frac{d}{d-2k}\binom{d-2k}{k}.
\]
The displayed binomial count follows by assigning at least two intervening unselected vertices to each of the \(k\) cyclic selected positions.

**3. Reflections.** For odd \(n=2h+1\), the representative \(s(i)=-i\) fixes vertex \(0\) and has paired orbits \(\{i,n-i\}\) for \(1\le i\le h\). Precisely the terminal pairs \(i=1\) (internally at distance two) and \(i=h\) (internally adjacent) are inadmissible. The remaining \(h-2\) paired orbits, indexed \(2,\ldots,h-1\), have mutual conflicts at index distance one or two; the fixed vertex conflicts only with the first pair. Hence \(B_s\) is a square of a path on \(h-2\) vertices with one pendant vertex at its first vertex. If \(A_m=I(P_m^2,-1)\), conditioning on the pendant shows \(I(B_s,-1)=A_{h-2}-A_{h-3}\).

For even \(n=2h\), the reflection \(s(i)=-i\) fixes vertices \(0,h\), and its terminal paired orbits \(i=1,h-1\) are inadmissible. The remaining \(h-3\) pairs form \(P_{h-3}^2\), while each fixed vertex is a pendant at a different end (when the path has one vertex, both attach there; when it is empty, the fixed vertices are independent). Conditioning on the two pendants gives \(A_{h-3}-2A_{h-4}+A_{h-5}\). The reflection \(rs(i)=1-i\) has no fixed vertices; the two terminal pairs are internally adjacent and inadmissible. The remaining \(h-2\) pairs have conflict graph \(P_{h-2}^2\), contributing \(A_{h-2}\). This classification includes the boundary cases \(n=6,7,8\), with \(A_j=1\) for \(j\le0\). Conditioning on the final vertex of \(P_m^2\) proves \(A_m=A_{m-1}-A_{m-3}\), with the stated initial values. Reflection conjugacy gives all exponents \(a\).

**4. Quotient formula.** Passing to barycentric subdivision makes the action without inversions. Over \(\mathbb Q\), chain averaging and exactness of taking invariants identify reduced homology of the topological quotient with invariant reduced homology of \(K_n\). Therefore
\[
\widetilde\chi(|K_n|/D_n)=\frac{1}{2n}\sum_{g\in D_n}\mathcal L_n(g).
\]
Exactly \(\varphi(n/d)\) rotations have \(\gcd(n,a)=d\). There are \(n\) reflections of the single odd type, or \(n/2\) of each even type. Substitution proves the boxed formula and its integrality.

**5. Infinitely many non-acyclic quotients.** The roots of \(x^3-x^2+1\) consist of one real \(\mu\in(-1,0)\) and a complex conjugate pair \(\rho e^{\pm i\theta}\), where \(\rho^2=1/|\mu|>1\). Newton's identities give \(W_n=\mu^n+2\rho^n\cos(n\theta)\). There are arbitrarily large integers \(n\) with \(\cos(n\theta)\ge1/2\), by elementary rational rotation if \(\theta/(2\pi)\) is rational and by simultaneous-approximation/rotation recurrence otherwise. Along these \(n\), \(|W_n|\ge \rho^n-o(\rho^n)\). Every proper divisor \(d<n\) is at most \(n/2\); the other rotational terms and all reflection terms together are \(O(n^2\rho^{n/2})\), since \(A_m\) satisfies the same characteristic recurrence. Their contribution is exponentially smaller than \(W_n\). Therefore \(|\widetilde\chi(|K_n|/D_n)|\) grows without bound along this subsequence. A nonzero reduced Euler characteristic forces at least one nonzero reduced rational homology group.

## Verification
The included `verify.py` implements the displayed recurrences **and** an independent enumeration of every invariant independent simplex as a union of permutation orbits with signed weight \((-1)^{\#\mathrm{orbits}}\). It compares all \(2n\) actions for every \(6\le n\le22\) and verifies integer-valued quotient arithmetic through \(n=500\), printing `CHECKS_OK`. These finite computations corroborate the orbit-graph proof but do not establish the infinite claim alone. Run `python3 verify.py` with Python 3 standard library; no downloads or external dependencies are required.

## Relationship to prior work
Adamaszek, *Splittings of independence complexes and the powers of cycles* (arXiv:1106.6250, first public 2011-06-30), proves nonequivariant homotopy splittings for \(\operatorname{Ind}(C_n^r)\) and specifically for \(r=2\). Those splittings do not specify the natural dihedral action or the orbit-space reduced Euler characteristic. Rinaldo and Romeo, *On the reduced Euler characteristic of independence complexes of circulant graphs* (arXiv:1706.00863, first public 2017-06-02), consider ordinary reduced Euler characteristics of circulants, not Euler characteristics of these dihedral quotients. The published dihedral formulas for **ordinary cycle matching complexes** concern \(\operatorname{Ind}(C_n)\), not \(\operatorname{Ind}(C_n^2)\); the full strong Morse cycle complex is another, distinct simplicial complex. Adamaszek, Adams, Frick, Peterson and Previte-Johnson, *Nerve complexes of circular arcs* (arXiv:1410.4336), Section 7 computes dihedral representations for circular-arc **nerve complexes**, while Section 8 treats cycle-power **clique complexes**; those are not the squared-cycle **independence complexes** considered here, and the cited results give no identification of the natural action or the present quotient formula. The present finding does not claim a new nonequivariant homotopy decomposition or individual rational homology representation.

## Limitations
The conclusion is an all-length formula for a reduced **alternating** homology invariant and a nonvanishing corollary. It does not determine individual rational Betti numbers, quotient homotopy types, or integral torsion. A related formula in unindexed work cannot be excluded. The finite verifier tests selected bounds; all-length validity rests on the orbit classification and recurrence proof. In particular, zero Euler characteristic does not imply acyclicity.

## References
1. M. Adamaszek, *Splittings of independence complexes and the powers of cycles*, arXiv:1106.6250 (first posted 2011-06-30), Theorem 1.1, Section 6, https://arxiv.org/pdf/1106.6250.
2. G. Rinaldo and F. Romeo, *On the reduced Euler characteristic of independence complexes of circulant graphs*, arXiv:1706.00863 (first posted 2017-06-02), Sections 1–2, https://arxiv.org/pdf/1706.00863.
3. *Dihedral homology characters and quotient congruences for cycle matching complexes*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-dihedral-homology-characters-and-quotient-congruences-for-cycle--6d9fbe47cba0.
4. *Dihedral Euler characters of full strong Morse complexes of cycles*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-dihedral-euler-characters-of-full-strong-morse-complexes-of-cycl--4819a9d67705.

5. M. Adamaszek, H. Adams, F. Frick, C. Peterson and C. Previte-Johnson, *Nerve complexes of circular arcs*, arXiv:1410.4336 (2014), Sections 7–8, https://arxiv.org/pdf/1410.4336.
