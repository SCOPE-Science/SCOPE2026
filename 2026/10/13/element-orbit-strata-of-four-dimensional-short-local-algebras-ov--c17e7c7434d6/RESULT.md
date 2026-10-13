# Element-orbit strata of four-dimensional short local algebras over finite fields

## Finding
Let \(k=\mathbb F_q\) for any prime power \(q\). Consider every commutative unital \(k\)-algebra \(A\) satisfying
\[
\dim_k A=4,\qquad A/J(A)\cong k,\qquad
\dim_k J/J^2=2,\quad\dim_k J^2=1,\quad J^3=0.
\]
These hypotheses specify the entire split local Hilbert type \((1,2,1)\). Choose a vector-space complement \(V\) to \(J^2\) in \(J\) and a nonzero \(z\in J^2\). The product is specified by a nonzero symmetric bilinear form \(B\) on \(V\) via \(vw=B(v,w)z\).

**Complete orbit-size table.** For each fixed residue \(r\in k\), the affine fiber \(r+J\) is invariant under \(\operatorname{Aut}_{k\text{-alg}}(A)\). The following are the full multisets of orbit sizes inside that fiber, including repeated sizes as separate orbits:

| Characteristic | Bilinear type | Orbit-size multiset in \(r+J\) | Orbit count in \(r+J\) |
|---|---|---|---|
| odd | rank one | \(1,\ (q-1)/2,\ (q-1)/2,\ q(q-1),\ q^2(q-1)\) | \(5\) |
| odd | rank two, split | \(1,\ q-1,\ 2q(q-1),\ q(q-1)^2\) | \(4\) |
| odd | rank two, anisotropic | \(1,\ q-1,\ q(q^2-1)\) | \(3\) |
| even | rank one | \(1,\ q-1,\ q(q-1),\ q^2(q-1)\) | \(4\) |
| even | rank two, nonalternating | \(1,\ q-1,\ q(q-1),\ q^2(q-1)\) | \(4\) |
| even | rank two, alternating | \(1,\ q-1,\ q(q^2-1)\) | \(3\) |

The total number of element-orbits on \(A\) is \(q\) times the final column. In particular, the rank-one and nonsingular nonalternating even-characteristic algebras have the same complete element-orbit-size multiset despite different socle dimensions, hence are nonisomorphic.

## Assumptions and scope
The finite field is part of the algebra structure; automorphisms are \(k\)-linear unital algebra automorphisms, not arbitrary ring or semilinear automorphisms. The residue field is identified with the given coefficient field \(k\). Each orbit is on the underlying **elements** of \(A\), not on algebras, ideals, or dual generators. Multiplication is associative because \(J^3=0\), so a product on \(V\times V\) into \(kz\) determines the algebra. Every nonzero symmetric \(2\times2\) form occurs.

## Proof
**1. Universal normal form.** With \(A=k1\oplus V\oplus kz\), the radical and its square are characteristic. Every automorphism has precisely the form
\[
\phi(r+v+sz)=r+gv+(\tau(v)+cs)z,
\quad g\in\operatorname{GL}(V),\quad \tau\in V^*,\quad c\in k^\times,
\]
where \(B(gv,gw)=cB(v,w)\) for all \(v,w\in V\). Conversely these conditions preserve all products and make \(\phi\) invertible. Thus the linear quotient action is the similarity group \(\operatorname{GO}(B)\), while \(\tau\) is unrestricted.

**2. Reduction of element orbits.** The coefficient \(r\) is fixed. On \(v=0\), the zero socle coordinate gives a singleton and nonzero socle coordinates have orbits under the multiplier subgroup \(\{c:\exists g\ B(g\cdot,g\cdot)=cB\}\subset k^\times\). When \(v\ne0\), arbitrary \(\tau\) moves its socle coordinate to any other value; consequently each \(\operatorname{GO}(B)\)-orbit \(\mathcal O\) on \(V\setminus\{0\}\) lifts to one element orbit of size \(q|\mathcal O|\). This reduction is exact, not an asymptotic count.

**3. Rank-one form.** Choose \(B((x,y),(x',y'))=xx'\). Its similarities are \(g=\bigl(\begin{smallmatrix}a&0\\b&d\end{smallmatrix}\bigr)\) with \(ad\ne0\) and multiplier \(a^2\). The nonzero-vector orbits are the punctured radical line, size \(q-1\), and its complement, size \(q(q-1)\). The multiplier subgroup is all of \(k^\times\) if \(q\) is even; if \(q\) is odd it is the subgroup of squares, yielding two socle orbits of size \((q-1)/2\). This produces the rank-one rows.

**4. Odd-characteristic nonsingular forms.** There are exactly two similarity classes of nondegenerate symmetric binary forms. For split \(B\), use \(B((x,y),(x',y'))=xy'+yx'\). Diagonal similarities act transitively on vectors with \(xy\ne0\) (there are \((q-1)^2\)); swapping axes joins the two punctured isotropic axes (there are \(2(q-1)\)). Every nonzero scalar occurs as a multiplier. For anisotropic \(B\), identify \(V\) with \(\mathbb F_{q^2}\) and take a scalar multiple of the norm-polarization form. Multiplication by \(h\in\mathbb F_{q^2}^\times\) gives a similarity with multiplier \(N_{\mathbb F_{q^2}/k}(h)\), which is surjective onto \(k^\times\); it is transitive on nonzero vectors. This proves both nonsingular odd rows.

**5. Even-characteristic nonsingular forms.** Every nonsingular symmetric binary form over a finite perfect field of characteristic two is either alternating or nonalternating. In the alternating case take \(B((x,y),(x',y'))=xy'+yx'\). All of \(\operatorname{GL}_2(k)\) acts by similarities, with multiplier the determinant; it is transitive on \(V\setminus\{0\}\). In the nonalternating case choose \(B=\operatorname{diag}(1,1)\). The isotropic vectors \(\{(x,x)\}\) form a single invariant line. Scalar matrices are similarities, and the isometries
\[
h_b=\begin{pmatrix}1+b&b\\b&1+b\end{pmatrix},\qquad b\in k,
\]
act transitively on any affine line \(x+y=t\ne0\), since \(h_b(x,y)=(x+bt,y+bt)\). Hence the nonzero-vector orbits have sizes \(q-1\) and \(q(q-1)\). Scalar similarities have multipliers \(\lambda^2\), and the square map is surjective on \(k^\times\). The remaining table entries follow.

**6. Socle comparison.** The annihilator of \(J\) inside \(J\) is \(J^2\oplus\operatorname{rad}(B)\); hence it has dimension two in the rank-one case and one in the nonsingular case. This certifies nonisomorphism even when the even-characteristic element-orbit multisets agree. The table exhausts the rank-one, split/anisotropic odd-rank-two, and alternating/nonalternating even-rank-two similarity classes.

## Verification
Run \(\texttt{python3 verify.py}\) from the extracted directory. The standalone standard-library checker exhaustively visits **every nonzero symmetric binary multiplication form** and every invertible linear similarity over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\), and computes the exact induced orbits on \(J\) by a union-find reduction justified in Proof step 2. It checks all orbit sizes, not only the orbit counts. The verified form totals are \(7,26,63,124\), respectively, and the output ends in \(\texttt{VERIFY_OK}\). These are finite checks; the theorem for every prime power follows from the uniform proof above.

## Relationship to prior work
Jelisiejew's *Classifying local Artinian Gorenstein algebras* (first publicly deposited 2015) gives the inverse-system approach to isomorphism classes of local Artinian Gorenstein algebras; its stated classification examples have different Hilbert functions, and its general orbit action is on **dual generators of algebras**, not on the elements of a fixed finite-field algebra. The separately published *Segre-quadric monomiality criterion for two-generated short local algebras* treats the full two-generator short-local tensor set-up and explicitly distinguishes rank-one multiplication from rank-two multiplication when \(\dim J^2=1\); its theorem decides **monomializability**, not the sizes of element orbits under full algebra automorphisms. Casnati studies isomorphism types of small Gorenstein algebras over algebraically closed characteristic-zero fields. None of these statements implies the complete finite-field element-orbit-size table without an additional similarity-group and multiplier-orbit calculation.

## Limitations
The result is restricted to commutative split four-dimensional local algebras with radical Hilbert type \((1,2,1)\). It does not cover nonsplit residue extensions, noncommutative multiplications, longer Loewy length, or group actions on modules/ideals. Originality is based on the inspected statements and searches, not a proof that no equivalent unpublished or differently indexed enumeration exists; the full text of Casnati's article was not accessible in this check.

## References
1. J. Jelisiejew, *Classifying local Artinian Gorenstein algebras*, arXiv:1511.08007, initial public version 25 November 2015; revised full text inspected: https://arxiv.org/pdf/1511.08007 .
2. *Segre-quadric monomiality criterion for two-generated short local algebras*, published scientific record (2026): https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-segre-quadric-monomiality-two-generated-short-local-algebras--0eb926948571 .
3. G. Casnati, *Isomorphism Types of Artinian Gorenstein Local Algebras of Multiplicity at Most 9*, Communications in Algebra 38 (2010), 2738--2761, https://doi.org/10.1080/00927870903059513 .
