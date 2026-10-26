# Sharp circular diameter of nonpolygonal minimal vanishing sums at order \(2pq\)

## Finding
Fix odd primes \(3\le p<q\), let \(N=2pq\) and \(\zeta=\exp(2\pi i/N)\). A finite subset \(S\subseteq\mathbb Z/N\mathbb Z\) is **minimal vanishing** if \(\sum_{e\in S}\zeta^e=0\) but \(\sum_{e\in T}\zeta^e\ne0\) for every nonempty proper \(T\subset S\). We exclude the rotated regular polygons (cycles of lengths \(2\), \(p\), and \(q\)). For the circularly sorted elements of \(S\), define \(G(S)\) as the largest clockwise distance between consecutive elements and define the circular support diameter \(D(S)=N-G(S)\), the length of a shortest arc containing \(S\).

**Theorem.** Among all nonpolygonal minimal vanishing subsets of \(\mathbb Z/N\mathbb Z\),
\[
\max G(S)=q+2p-1,\qquad \min D(S)=(2p-1)(q-1).
\]
Both extrema are attained for every pair of distinct odd primes \(p<q\). Moreover, all nonpolygonal minimal sets have the exact checkerboard parametrization described below.

## Assumptions and scope
The coefficients are exactly zero or one and each chosen root appears once. The cyclic positions are modulo \(N\); the diameter is minimized over rotations of the cyclic exponents, not the ordinary diameter of an arbitrarily fixed representative. Primality and oddness of \(p<q\) are essential to the proof. We make no classification at orders with four or more distinct prime factors or for multiplicities greater than one.

For nonempty proper \(A\subset\mathbb Z/p\mathbb Z\) and \(B\subset\mathbb Z/q\mathbb Z\), put
\[
S(A,B)=\{e\bmod N:e\equiv0\ (\mathrm{mod}\ 2),\ e\bmod p\in A,\ e\bmod q\in B\}
\cup
\{e\bmod N:e\equiv1\ (\mathrm{mod}\ 2),\ e\bmod p\notin A,\ e\bmod q\notin B\}.
\]
The checkerboard assertion says every nonpolygonal minimal vanishing set is some \(S(A,B)\), and every such \(S(A,B)\) is minimal vanishing. Reversing the parity sign or rotating a set is already encompassed by appropriate choices and rotations of \(A,B\).

## Proof
**1. Rational kernel and classification.** Because \(N/2=pq\) is odd, each pair of antipodal positions has sum zero. A minimal vanishing set with more than two members therefore contains at most one position in each antipodal pair. Identify an even selected exponent \(e\) with a coefficient \(+1\), and an odd selected exponent with \(-1\), for the primitive \(pq\)-th roots under the identity \(\zeta^e=(-1)^e\zeta_{pq}^{k(e)}\), where \(k(e)\equiv 2^{-1}e\pmod{pq}\). The invertible scaling of the two residue coordinates can be absorbed into their labels. Thus the signed coefficient matrix \(c_{ij}\), indexed by residues modulo \(p,q\), has values in \(\{-1,0,1\}\) and records vanishing exactly when
\[
\sum_{i\in\mathbb Z/p}\sum_{j\in\mathbb Z/q}c_{ij}\zeta_p^i\zeta_q^j=0.
\]
(Here the roots may have been independently replaced by primitive powers; this leaves the kernel unchanged.) The two cyclotomic fields have coprime conductors and linearly disjoint degrees. Since the sole relation among the \(p\)-th roots is their full sum, and similarly for the \(q\)-th roots, tensoring the two rational quotient spaces gives the **exact** kernel description
\[
c_{ij}=u_i+v_j\qquad(u_i,v_j\in\mathbb Q).
\]
In particular, every additive \(2\times2\) minor of \(c\) is zero.

If \(u\) or \(v\) is constant, any nonzero signed row or column is a complete prime polygon and violates nonpolygonal minimality. Otherwise both ranges are positive integers (the differences are differences of entries in \(\{-1,0,1\}\)). Since the range of \(u_i+v_j\) is at most two, both ranges must equal one and the matrix attains both values \(-1\) and \(+1\). Consequently the matrix equals \(+1\) on a nonempty proper rectangle \(A\times B\), equals \(-1\) on \(A^c\times B^c\), and vanishes on the mixed rectangles. Undoing the invertible coordinate scalings yields the stated parity checkerboard.

Conversely a checkerboard gives zero because the two signed rectangle sums are equal: \(\sum_{i\in A}\zeta_p^i=-\sum_{i\notin A}\zeta_p^i\) and likewise for \(B\). For minimality, suppose a sub-sum vanishes. Its signed matrix \(c'\) is still additive and zero on \(A\times B^c\) and \(A^c\times B\). These cross-rectangle equalities force \(c'\) to be constant on each diagonal rectangle and force the two diagonal constants to be negatives of each other. Because their allowed entries are respectively \(0,1\) and \(0,-1\), the sub-sum is either empty or the entire checkerboard. This also proves that all checkerboards are nonpolygonal.

**2. Universal gap bound.** Translation of \(S\) by one exponent preserves minimality and the value of \(G(S)\), so assume there is an empty circular interval containing exponents \(1,2,\ldots,L\), with \(L=q+2p-1\). For the checkerboard labels put \(a_r={\boldsymbol1}_A(r)\), \(b_t={\boldsymbol1}_B(t)\). If \(e\) is even, its absence forbids \(a_{e\bmod p}=b_{e\bmod q}=1\); if \(e\) is odd, its absence forbids both variables being zero. For each \(e\in\{1,\ldots,2p-1\}\), both \(e\) and \(e+q\) lie in this interval. They have opposite parity but the same residue modulo \(q\). Hence
\[
e\ \text{even}\implies a_{e\bmod p}\le a_{(e+q)\bmod p},\qquad
 e\ \text{odd}\implies a_{e\bmod p}\ge a_{(e+q)\bmod p}.
\]
For each residue \(r=1,\ldots,p-1\) the two integers \(e=r\) and \(e=r+p\) both occur in \(1,\ldots,2p-1\), with opposite parity. Therefore \(a_r=a_{r+q}\). Since \(q\) is invertible modulo \(p\), the directed cycle \(r\mapsto r+q\) stays connected even if its single edge outgoing from zero is deleted; the equations for the remaining \(p-1\) edges imply that \(a\) is constant. This contradicts nonemptiness and properness of \(A\). Thus no \(q+2p-1\) consecutive positions can be missing and \(G(S)\le q+2p-1\).

**3. Attainment.** Set \(L_0=q+2p-2\). We construct \(A,B\) for which every exponent \(1,\ldots,L_0\) is absent. For \(e=1,\ldots,2p-2\), the pair \(e,e+q\) imposes the same displayed weak inequalities. They imply equality on all directed edges \(r\mapsto r+q\) of \(\mathbb Z/p\mathbb Z\) except the edges outgoing from \(0\) and \(p-1\). The edge from \(p-1\) (appearing at the even exponent \(p-1\)) requires \(a_{p-1}\le a_{p-1+q}\), while the edge from \(0\) (appearing at the odd exponent \(p\)) requires \(a_0\ge a_q\). Deleting the two edges splits the directed prime cycle into two paths. Set \(a=0\) on the path from \(q\) to \(p-1\), and \(a=1\) on the path from \(p-1+q\) to \(0\). All inequalities hold; \(A=\{r:a_r=1\}\) is nonempty and proper.

For every column \(t\bmod q\), at most three exponents in \(1,\ldots,L_0\) have that column, because \(L_0<3q\). Consecutive such exponents differ by \(q\), hence alternate parity. Two restrictions on the single variable \(b_t\) could conflict only if one comes from an even exponent and the other from an odd exponent. Among at most three consecutive occurrences, every opposite-parity pair is adjacent, and the established inequalities for adjacent occurrences exclude exactly these conflicts. Thus a compatible \(b_t\) exists. Choose each \(b_t\in\{0,1\}\) accordingly (arbitrarily if unconstrained). Since the interval contains a full even and a full odd traversal of every residue modulo \(p\), some even exponent with \(a_e=1\) forces \(b=0\), and some odd exponent with \(a_e=0\) forces \(b=1\). Thus \(B\) too is nonempty and proper. The resulting minimal checkerboard omits \(1,\ldots,L_0\), so its consecutive gap between zero and \(L_0+1\) has length at least \(L_0+1=q+2p-1\). The universal upper bound forces equality and proves the theorem.

## Verification
An independent standard-library integer verifier, `verify.py`, enumerates all \(16{,}992\) nonempty proper checkerboard pairs for \((p,q)=(3,5),(3,7),(3,11),(5,7)\). It checks the exact rational cyclotomic-kernel identities, the absence of antipodal pairs, the maximum circular gap for every enumerated set, attainment of the asserted bound for each pair, and all proper subsums of selected small extremizers. Its expected final output begins with `CERTIFICATE_OK`. Such finite verification cannot certify the infinite family: that follows from the proof.

## Relationship to prior work
Lam and Leung (arXiv:math/9511209; *Journal of Algebra* 2000) analyze minimal vanishing sums and their weights, including the smallest asymmetric weight and its equality case. Christie, Dykema and Klep (arXiv:2008.11268) classify low-weight minimal vanishing sums and their types. These results explain the signed prime-cycle phenomena but do not, in the inspected statements, determine the exact maximal circular gap for every \(2pq\) or construct gap extremizers for all prime pairs. Tan and Zhang (arXiv:2609.07646v1, first posted 2026-09-07) prove a sharp general support-diameter inequality for nonnegative cyclotomic multiples, with polygonal equality cases; the present theorem determines a distinct exact threshold inside the nonpolygonal **minimal zero-one** class. The general bound gives \(D\ge pq\) here, whereas the new threshold equals \((2p-1)(q-1)\), which is strictly larger. Earlier implicit coverage cannot be ruled out, and this work has not undergone independent audit.

## Limitations
No result is claimed for repeated roots, signed arbitrary-height coefficients, nonminimal vanishing sums, higher-prime-factor indices, or other gap statistics. The novelty assessment depends on the sources and comparisons listed in the accompanying review; absence of a search hit is not a mathematical proof of originality.

## References
- H. Tan and Y. Zhang, *Sharp Diameter Bounds for Nonnegative Cyclotomic Multiples*, arXiv:2609.07646v1, submitted 2026-09-07.
- T. Y. Lam and K. H. Leung, *On Vanishing Sums of Roots of Unity*, *Journal of Algebra* **224** (2000), 91–109, DOI:10.1006/jabr.1999.8089; arXiv:math/9511209v1.
- L. Christie, K. J. Dykema and I. Klep, *Classifying Minimal Vanishing Sums of Roots of Unity*, arXiv:2008.11268v2.
