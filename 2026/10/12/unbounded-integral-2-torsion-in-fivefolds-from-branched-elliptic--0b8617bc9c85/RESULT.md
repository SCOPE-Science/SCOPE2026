# Unbounded integral \(2\)-torsion in fivefolds from branched elliptic covers

## Finding
Fix any even integer \(r\geq 2\). For the smooth projective fivefold \(X_r\) defined below, the integral cohomology has free ranks
\[
(b_0,b_1,\ldots,b_{10})=(1,2,3,6,9,10,9,6,3,2,1).
\]
Its entire torsion is
\[
\operatorname{Tor} H^k(X_r;\mathbb Z)\cong
\begin{cases}
(\mathbb Z/2\mathbb Z)^{r-2},& k\in\{4,5,6,7\},\\
0,& k\notin\{4,5,6,7\}.
\end{cases}
\]
These formulas hold for every allowable choice of curves, branch points, nonzero two-torsion translation, and embedding. Thus the fivefold construction admits arbitrarily large integral two-primary torsion while all rational Betti numbers stay fixed.

## Assumptions and scope
Work over \(\mathbb C\). Let \(E\) and \(F\) be arbitrary elliptic curves. Choose a connected smooth double cover \(\rho:C\to E\) simply branched over \(r\) distinct points, where \(r\) is even and at least two. Such covers exist for all these \(r\): take an effective reduced divisor of even degree on \(E\), choose a square root of its associated line bundle, and form the associated double cover. By Riemann–Hurwitz, \(g(C)=1+r/2\). Let \(\iota\) be the covering involution. Pick \(0\ne a\in F[2]\) and let \(\tau_a\) be translation by \(a\). Define the smooth complex surface
\[
S=(F\times C)/\langle\tau_a\times\iota\rangle.
\]
The action is free because \(\tau_a\) has no fixed points. Its natural morphism \(p:S\to E\) admits a closed embedding \(j:S\hookrightarrow\mathbb P^4\times E\) over \(E\) by the generic-projection lemma for relative embeddings of surfaces. Set
\[
X_r=\operatorname{Bl}_{j(S)}(\mathbb P^4\times E).
\]
This is a smooth projective complex fivefold. The assertion concerns integral singular cohomology, not étale cohomology or the full integral cup-product ring.

## Proof
**1. Coinvariants of the covering involution.** Let \(\Gamma\) be the orbifold fundamental group of the elliptic curve with the \(r\) branch points of order two. It has the standard presentation
\[
\Gamma=\langle a_0,b_0,c_1,\ldots,c_r\mid
[a_0,b_0]c_1\cdots c_r=1,\ c_i^2=1\rangle.
\]
The branched double cover determines a surjective homomorphism \(\phi:\Gamma\to\mathbb Z/2\mathbb Z\), sending every \(c_i\) to the nontrivial element. Orbifold covering theory identifies its kernel with \(\pi_1(C)\). The associated conjugation action on \(H_1(C;\mathbb Z)\) is the action of \(\iota\).

Abelianizing the presentation gives
\[
H_1(\Gamma;\mathbb Z)\cong\mathbb Z^2\oplus(\mathbb Z/2\mathbb Z)^{r-1},
\]
since the only relation among the order-two branch generators is \(c_1+\cdots+c_r=0\). Because \(r\) is even, sending every branch generator to one is compatible with this relation. On the torsion summand the map induced by \(\phi\) is surjective, and its kernel has dimension \(r-2\) over \(\mathbb F_2\).

The five-term integral group-homology exact sequence for \(1\to\pi_1(C)\to\Gamma\to\mathbb Z/2\mathbb Z\to1\) and the equality \(H_2(\mathbb Z/2\mathbb Z;\mathbb Z)=0\) identify
\[
H_1(C;\mathbb Z)_{\iota}=\ker\bigl(H_1(\Gamma;\mathbb Z)\to\mathbb Z/2\mathbb Z\bigr)
\cong\mathbb Z^2\oplus(\mathbb Z/2\mathbb Z)^{r-2}.
\tag{1}
\]
The invariants \(H_1(C;\mathbb Z)^{\iota}\) have free rank two: over \(\mathbb Q\), the invariant subspace is the pullback of \(H_1(E;\mathbb Q)\), and integral invariants are a subgroup of a free abelian group.

**2. Integral homology of the surface.** The unramified double cover \(F\to F/\langle\tau_a\rangle\) is, topologically, the double cover of a two-torus classified by a nonzero class in \(H^1(T^2;\mathbb Z/2\mathbb Z)\). Choose a lattice basis making that class \((1,0)\). Then the associated bundle \(S\to F/\langle\tau_a\rangle\) with fiber \(C\) has involution monodromy along the first circle and trivial monodromy along the second. Hence
\[
S\cong S^1\times M_{\iota}
\]
as differentiable manifolds, where \(M_{\iota}\) is the mapping torus of the orientation-preserving surface homeomorphism \(\iota:C\to C\).

The integral Wang sequence of this mapping torus and (1) yield
\[
H_1(M_{\iota};\mathbb Z)\cong
\mathbb Z^3\oplus T_r,
\qquad H_2(M_{\iota};\mathbb Z)\cong\mathbb Z^3,
\qquad H_3(M_{\iota};\mathbb Z)\cong\mathbb Z,
\]
where \(T_r=(\mathbb Z/2\mathbb Z)^{r-2}\). In particular, the first is the direct sum of a circle and the coinvariants (1); the second fits into an exact sequence with kernel \(H_2(C)_{\iota}\cong\mathbb Z\) and quotient \(H_1(C)^{\iota}\cong\mathbb Z^2\), which splits since the quotient is free. The Künneth formula (with no new Tor terms from the free circle homology) gives
\[
\begin{array}{c|ccccc}
k&0&1&2&3&4\\\hline
H_k(S;\mathbb Z)&\mathbb Z&\mathbb Z^4\oplus T_r&\mathbb Z^6\oplus T_r&\mathbb Z^4&\mathbb Z
\end{array}.
\]
The universal coefficient theorem therefore gives
\[
\begin{array}{c|ccccc}
k&0&1&2&3&4\\\hline
H^k(S;\mathbb Z)&\mathbb Z&\mathbb Z^4&\mathbb Z^6\oplus T_r&\mathbb Z^4\oplus T_r&\mathbb Z
\end{array}.
\tag{2}
\]

**3. Blow-up and all integral cohomology groups.** The surface has complex codimension three in \(\mathbb P^4\times E\). The integral blow-up decomposition therefore gives, additively and without extension ambiguity,
\[
H^k(X_r;\mathbb Z)\cong H^k(\mathbb P^4\times E;\mathbb Z)
\oplus H^{k-2}(S;\mathbb Z)\oplus H^{k-4}(S;\mathbb Z),
\tag{3}
\]
where cohomology in negative degrees is zero. All cohomology of \(\mathbb P^4\times E\) is free. Equation (2) puts \(T_r\) in degrees two and three of \(S\), so (3) places one copy in each of degrees four through seven of \(X_r\), and nowhere else. The free-rank generating function from (3) is
\[
(1+t^2+t^4+t^6+t^8)(1+2t+t^2)
+(t^2+t^4)(1+4t+6t^2+4t^3+t^4),
\]
which expands to the displayed Betti vector. This proves the theorem for every \(r\) and every allowable embedding.

## Verification
Run \(\texttt{python3 artifacts/verify_target.py}\) in the extracted package. The script replays the branch-generator parity count for each even \(r\) from two through sixteen, the cohomological degree shifts, Poincaré-duality compatibility, and the exact Betti-polynomial arithmetic; it prints \(\texttt{VERIFY_OK}\). The infinite family is established by the group-homology, Wang, universal-coefficient, and blow-up arguments above, not by those finite checks.

## Relationship to prior work
Debarre, Jiang and Lahoz introduced the quotient surface as an Iitaka torus tower (Example 1.11), emphasizing its rational cohomology. Schreieder and Wang's July 2026 work introduced the fivefold blow-up application to Aomoto complexes. Corrêa, Kollár, Schreieder and Wang's October 2026 work supplies the relative embedding, the integral blow-up formula, and the strengthened semisimple Aomoto property (Sections 4.1–4.5). The exact finite integral torsion groups of the compact fivefolds, their dependence on the branch-point count, and the fixed Betti vector are not given in the inspected relevant passages. Classical orbifold-cover and Wang-sequence tools make the computation possible; novelty is the resulting exact family-specific integral invariant, rather than any claim of a new general homological tool.

## Limitations
The theorem determines additive integral cohomology only; it does not describe the integral ring multiplication or individual torsion-cycle representatives. The examples require a simply branched double cover with an even positive number of branch points and the stated free diagonal action. The computation does not claim that finite verification enumerates all covers. A July 2026 precursor could not be read beyond its abstract and independent summary during bibliographic review; possible implicit earlier equivalent calculations remain a limitation on originality assessment.

## References
1. O. Debarre, Z. Jiang and M. Lahoz, *Rational cohomology tori*, Geom. Topol. 21 (2017), 1095–1130; arXiv:1509.01043, Example 1.11. https://arxiv.org/pdf/1509.01043
2. S. Schreieder and B. Wang, *Zeros of one-forms and the topology of algebraic maps*, arXiv:2607.15102v1 (first public 2026-07-16). https://arxiv.org/abs/2607.15102
3. M. Corrêa, J. Kollár, S. Schreieder and B. Wang, *The topology of Kähler manifolds and 1-forms without zeros*, arXiv:2610.04314v1 (first public 2026-10-03), Sections 4.1–4.5. https://arxiv.org/html/2610.04314v1
4. Standard ingredients: the integral five-term Lyndon–Hochschild–Serre sequence for group extensions, the integral Wang sequence of a mapping torus, the Künneth and universal coefficient theorems, and the integral blow-up formula.
