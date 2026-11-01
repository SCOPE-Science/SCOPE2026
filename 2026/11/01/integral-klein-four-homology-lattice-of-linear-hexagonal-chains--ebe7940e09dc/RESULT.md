# Integral Klein-four homology lattice of linear hexagonal chains

## Finding
For every integer \(n\geq 1\), let \(G_n\) be the graph of a linear chain of \(n\) hexagons defined below, and let \(K_n=\operatorname{Ind}(G_n)\). Let \(h\) exchange its two horizontal rows and let \(v\) reverse its columns. The previously known homotopy equivalence \(K_n\simeq S^n\vee S^n\) gives a free rank-two lattice \(L_n=\widetilde H_n(K_n;\mathbb Z)\).

**Integral equivariant classification.** There is an integral basis \((e_1,e_2)\) of \(L_n\) such that
\[
[h]_{L_n}=J=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
[v]_{L_n}=\begin{cases}
(-1)^{n/2}I_2,& n\text{ even},\\
(-1)^{(n+1)/2}J,& n\text{ odd}.
\end{cases}
\]
Consequently \(L_n\cong\mathbb Z[C_2]\) as an integral row-exchange module, not the direct sum of its rational \(+1\)- and \(-1\)-eigenlines. Those two primitive eigenlines generate a sublattice of **index exactly two**. Modulo two, row exchange acts by the single Jordan block \(J_2(1)\). The entire \(C_2\times C_2\) integral action, rather than just its rational character, is thereby determined.

## Assumptions and scope
Use vertices \((r,j)\) with \(r\in\{0,1\}\), \(1\leq j\leq 2n+1\). On each row connect consecutive columns, and add a vertical rung between \((0,j)\) and \((1,j)\) at every odd \(j\). The independence complex \(K_n\) contains exactly the graph-independent vertex subsets. The commuting involutions are \(h(r,j)=(1-r,j)\) and \(v(r,j)=(r,2n+2-j)\). All homology is reduced when a tilde appears; integral homology is intended unless a coefficient field is specified.

The one imported topological premise is Chandrakar--Singh's theorem \(K_n\simeq S^n\vee S^n\) for all \(n\geq1\) [1, Theorem 3.1]. In particular, \(L_n\) is torsion-free of rank two and all other reduced homology vanishes. No equivariant wedge decomposition is assumed.

## Proof
**1. The row-exchange fixed set.** A point in a simplicial realization fixed by an involution must have equal barycentric weights along each exchanged vertex orbit; its support must therefore be a union of complete vertex orbits. Under \(h\), the orbit joining two vertices of any odd column contains a rung and cannot occur in an independent face. For each even column, the two exchanged vertices are nonadjacent. The \(n\) even-column orbits are pairwise independent of one another. Therefore the geometric fixed-point space \(|K_n|^{\langle h\rangle}\) is precisely a full \((n-1)\)-simplex with its orbit barycenters as vertices. Denote this contractible nonempty space by \(F\). The \(C_2\)-action on \(|K_n|\setminus F\) is free.

**2. An integral lattice obstruction from the free relative action.** Work first over \(k=\mathbb F_2\), put \(R=k[C_2]\), and let \(M=H_n(|K_n|,F;k)\cong H_n(K_n;k)\cong k^2\). These are the only nonzero relative homology groups: \(F\) is contractible, \(K_n\) is connected, and its reduced homology is concentrated in degree \(n\). After an equivariant barycentric subdivision, \(F\) is a subcomplex and the relative cellular chain complex \(C_*=C_*(|K_n|,F;k)\) is bounded and consists of free finite-rank \(R\)-modules, since all cells outside \(F\) have trivial stabilizer.

Tensor a projective resolution of the trivial \(R\)-module \(k\) with \(C_*\). One spectral sequence has
\[
E^2_{p,q}=\operatorname{Tor}^{R}_p(k,H_q(C_*))
\Longrightarrow H_{p+q}(k\otimes_R C_*).
\]
The \(E^2\)-page has just the row \(q=n\), so no differentials can affect it, and
\[
\operatorname{Tor}^{R}_p(k,M)\cong H_{n+p}(|K_n|/C_2,F;k).
\]
Here the target identification uses the free relative cell action. The quotient pair is finite dimensional, so the right side vanishes for all sufficiently large \(p\).

For \(C_2=\langle h\rangle\) in characteristic two, the standard periodic resolution has every differential \(1+h\). Thus for every \(p\geq1\),
\[
\operatorname{Tor}^{R}_p(k,M)=\ker(1+h:M\to M)/\operatorname{im}(1+h:M\to M).
\]
Since \((1+h)^2=0\) and \(\dim_k M=2\), its eventual vanishing forces \(\operatorname{rank}_k(1+h)=1\). In particular, \(h\) is **not** the identity modulo two: it is the unique nontrivial two-dimensional unipotent Jordan block.

The reduced Lefschetz number of \(h\) is \(\widetilde\chi(F)=0\); the only nonzero rational reduced homology has degree \(n\). Hence \(h\) has rational trace zero on \(L_n\), with one positive and one negative rational eigenvalue. Choose a primitive positive integral eigenvector \(u\). Then \(L_n/\mathbb Zu\cong\mathbb Z\), and \(h\) acts by \(-1\) on this quotient. Choose a lift \(e\) of a quotient generator. We have \(h(e)=-e+a u\) for an integer \(a\). The mod-two nonidentity condition proved above says \(a\) is odd. Replacing \(e\) by \(e+ku\) replaces \(a\) by \(a+2k\); choose \(k\) so that \(a=1\). Since \(u=e+h(e)\), the pair \((e,h(e))\) is an integral basis and \(h\) exchanges it. In this basis, \([h]=J\). The primitive eigenvectors \(e+h(e)\) and \(e-h(e)\) have determinant of absolute value two, proving the index-two obstruction.

**3. All possible longitudinal actions.** Since \(v\) commutes with \(h\), its matrix in the integral swap basis must be \(\begin{pmatrix}a&b\\b&a\end{pmatrix}\) with \(a,b\in\mathbb Z\). Invertibility forces \((a-b)(a+b)=\pm1\). Thus \([v]\) is one of \(\pm I_2,\pm J\). It remains to determine which one occurs at each \(n\).

**4. A parity-sensitive end-reversal Lefschetz calculation.** Folding columns under \(v\) yields the graph \(Q_n\) on two rails of \(n+1\) columns, with horizontal edges between consecutive columns and a vertical rung at every *even* zero-indexed column. Every vertex orbit is independent internally, and the conflict graph of the orbits is exactly \(Q_n\). Hence \(|K_n|^{\langle v\rangle}\) is the independence complex of \(Q_n\), realized by orbit barycenters.

Write \(Z_n=I(Q_n;-1)\), where the independence polynomial includes the empty set. Process its columns from left to right and let \((a,b,c)\) be the signed totals for the last-column states \(\varnothing\), either one of the two singleton choices (they are symmetric), and the two-vertex choice. Initially \((a,b,c)=(1,0,0)\). Appending column \(j\), counted from zero, gives
\[
(a',b',c')=(a+2b+c,\,-a-b,\,\epsilon_j a),\qquad
\epsilon_j=\begin{cases}0&j\text{ even},\\1&j\text{ odd}.
\end{cases}
\]
After columns \(0,1\), the state is \((-1,0,1)\); after column \(2\), it is \((0,1,0)\). Every subsequent odd-even column pair transforms \((0,b,0)\mapsto(0,-b,0)\), with the intervening odd-column state \((2b,-b,0)\). Therefore
\[
Z_n=\begin{cases}2(-1)^{n/2+1}&n\text{ even},\\0&n\text{ odd}.
\end{cases}
\]
For any finite complex \(X\), \(\widetilde\chi(X)=-I(Q;-1)\) when \(X=\operatorname{Ind}(Q)\). Equivariant Lefschetz gives
\[
\operatorname{tr}(v\mid L_n\otimes\mathbb Q)=(-1)^{n+1}Z_n.
\]
Thus for \(n=2k\), the trace is \(2(-1)^k\). Among \(\pm I_2,\pm J\) this forces \([v]=(-1)^k I_2\). For odd \(n\), the trace is zero and so \([v]=\pm J\).

**5. Resolve the remaining odd sign with a primitive cycle.** At each of the \(n+1\) odd columns form the zero-cycle \(c_i=[(0,2i+1)]-[(1,2i+1)]\), \(0\le i\le n\). Different rungs have no edges between their endpoints, so their oriented simplicial join
\[
z=c_0*c_1*\cdots*c_n
\]
is an integral \(n\)-cycle in \(K_n\). Choosing the upper rung endpoint for even \(i\) and the lower endpoint for odd \(i\) gives a maximal independent face: all unused rung endpoints are blocked by the chosen ones, and each intermediate even-column vertex meets a selected neighbor. Its top-dimensional facet cochain is a cocycle pairing \(\pm1\) with \(z\). Thus \([z]\) is nonzero and primitive in \(L_n\).

The row exchange negates all \(n+1\) factors, while end reversal reverses their order. Accordingly
\[
h[z]=(-1)^{n+1}[z],\qquad
v[z]=(-1)^{\binom{n+1}{2}}[z].
\]
For odd \(n\), the first sign is \(+1\); the second is \((-1)^{(n+1)/2}\). Since \([v]=\pm J\) and \(J\) fixes the positive \(h\)-eigenline, the nonzero class \([z]\) forces \([v]=(-1)^{(n+1)/2}J\). This proves the integral equivariant classification for every \(n\ge1\).

## Verification
The standalone Python 3 program `verify_hex_lattice.py` uses only standard-library integer arithmetic. It independently constructs graph-independent faces, boundary matrices over \(\mathbb F_2\), representatives of degree-\(n\) homology, and actions of both graph reflections for \(1\le n\le5\). In every case the top homology has dimension two; \(h-I\) has rank one, and \(v-I\) has rank zero for even \(n\) and one for odd \(n\). It also checks forty transfer-recurrence instances, seven complete independent-set orbit evaluations, and fourteen maximal alternating rung selections. Execute from the package directory with `python3 verify_hex_lattice.py`.

These finite computations do not establish the universal assertion; Steps 1--5 do. In particular, the free-relative-cell and group-homology argument, not extrapolation from small cases, proves the nonsplitting for arbitrary \(n\).

## Relationship to prior work
Chandrakar--Singh [1] establish the **nonequivariant** homotopy type \(S^n\vee S^n\), hence rank two of the integral homology, without classifying automorphism actions. The closest published symmetry computation [2] gives the exact **rational** character of \(\langle h,v\rangle\): it agrees with the rationalization of the matrices above and explicitly leaves integral lattice splitting open. Rational characters cannot tell \(\operatorname{diag}(1,-1)\) apart from the integral swap matrix \(J\), since both have trace zero and square to the identity. The new fixed-point/free-relative argument eliminates the split lattice, and the integer centralizer plus primitive cross-cycle argument specifies the full integral group action. It is therefore not a restatement of either the wedge theorem or the rational character formula.

The standard two-periodic group resolution and the ordinary simplicial Lefschetz formula are proof techniques, not new claims of general theory. No uniqueness in all unindexed literature is asserted.

## Limitations
This result concerns the natural two-reflection action on the integral homology of the *linear* hexagon chain; it does not claim an equivariant homotopy equivalence, wider honeycomb-grid classifications, or an explicit chain-level integral basis independent of existence arguments. It relies on the published nonequivariant homotopy theorem [1]. An equivalent unindexed integral result may exist. No independent audit or validation is claimed.

## References
[1] H. Chandrakar and A. Singh, *Independence Complexes of Hexagonal Grid Graphs*, arXiv:2512.21318v1, first public 2025-12-24, Theorem 3.1 and Sections 2--3. https://arxiv.org/pdf/2512.21318

[2] *Reflection characters of linear hexagonal-chain independence complexes*, published mathematical record dated 2026-10-11, especially its Finding, Proof, and Limitations. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-reflection-characters-of-linear-hexagonal-chain-independence-com--db3e42fb7a57
