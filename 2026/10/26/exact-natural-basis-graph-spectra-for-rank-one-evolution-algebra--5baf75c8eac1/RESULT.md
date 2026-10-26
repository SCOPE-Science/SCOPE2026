# Exact natural-basis graph spectra for rank-one evolution algebras in characteristic two

## Finding

Let \(q=2^e\) with \(e\ge 2\) and let \(d\ge2\). Every \(d\)-dimensional evolution algebra \(E\) over \(\mathbb F_q\) with \(\dim E^2=1\) and zero annihilator has a natural basis in which its multiplication is
\[
xy=\left(\sum_{i=1}^d x_i y_i\right)u,\qquad
u=(u_1,\ldots,u_d)\ne0.
\]
Here a *natural basis* is a vector-space basis whose distinct elements multiply to zero. Two natural bases are identified if they differ by permuting their elements and multiplying them individually by nonzero scalars. The directed graph of such a basis has an arc \(i\to j\) if the coefficient of the \(j\)-th basis vector in the square of the \(i\)-th is nonzero. Every normalized natural basis therefore has a graph with all rows of its adjacency matrix equal, and its graph-isomorphism type depends only on the number \(k\) of nonzero coordinates of \(u\) in that basis.

The following formulas determine, simultaneously, which graph types occur and **exactly how many equivalence classes of natural bases** produce each graph type. Put \(t=(1,\ldots,1)\), \(c=\sum_i u_i\), and, for \(1\le k\le d\),
\[
A_k(c)=
\begin{cases}
\displaystyle\frac{(q-1)^k+(q-1)(-1)^k}{q},&c=0,\\[5pt]
\displaystyle\frac{(q-1)^k-(-1)^k}{q},&c\ne0.
\end{cases}
\]
Define \(G_d\) by
\[
G_{2m+1}=q^{m^2}\prod_{j=1}^{m}(q^{2j}-1),\qquad
G_{2m}=q^{m^2}\prod_{j=1}^{m-1}(q^{2j}-1),
\]
with the empty product equal to one. Define a positive integer \(T\) and integers \(H_k\) according to the following mutually exclusive cases:

1. **Fixed line:** if \(u\in\mathbb F_q^\times t\), let \(T=1\), \(H_d=1\), and \(H_k=0\) for \(k<d\).
2. **Odd dimension, moving vector:** if \(d\) is odd and \(u\notin\mathbb F_qt\), let \(T=q^{d-1}-1\) and \(H_k=\binom dk A_k(c)-\mathbf1_{\{k=d,\ c\ne0\}}\).
3. **Even dimension, nonzero coordinate sum:** if \(d\) is even and \(c\ne0\), let \(T=q^{d-1}\) and \(H_k=\binom dk A_k(c)\).
4. **Even dimension, zero coordinate sum outside the fixed line:** if \(d\) is even, \(c=0\), and \(u\notin\mathbb F_qt\), let \(T=q^{d-1}-q\) and \(H_k=\binom dk A_k(0)-(q-1)\mathbf1_{\{k=d\}}\). This fourth case requires \(d\ge4\).

**Theorem.** In each case, the number \(C_k\) of scaling-and-reordering classes of natural bases of \(E\) whose associated directed graph has exactly \(k\) common out-neighbors is
\[
\boxed{C_k=\frac{G_d H_k}{d!\,T}.}
\]
All these values are nonnegative integers, and \(\sum_{k=1}^d C_k=G_d/d!\). For \(q\ge4\), the graph spectrum is exactly \(\{d\}\) on the fixed line, \(\{1,2,\ldots,d\}\) when \(c\ne0\) away from that line, and \(\{2,3,\ldots,d\}\) when \(c=0\) away from that line. Thus there are precisely one, \(d\), or \(d-1\) distinct graph-isomorphism types according to the case, and their multiplicities are explicit.

## Assumptions and scope

All fields have order \(q=2^e\) with \(e\ge2\), all dimensions satisfy \(d\ge2\), and all algebras are finite-dimensional commutative, generally nonassociative evolution algebras with \(\dim E^2=1\) and \(\operatorname{Ann}(E)=0\). A normalized natural basis for a fixed choice of nonzero generator \(u\) of \(E^2\) is one in which every basis element squares to that same generator. The zero-annihilator assumption is essential: it ensures no diagonal coefficient vanishes. The preceding numbers classify natural bases of a *fixed* algebra, not isomorphism types of algebras. The displayed \(c\) and fixed-line case are computed after choosing any normalized natural frame. Changing the generator rescales all normalized coordinates by a common nonzero factor, leaving the case and counts unchanged.

## Proof

**1. Bilinear realization and normalization.** Choose any \(0\ne u\in E^2\). Since \(E^2=\mathbb F_qu\), there is a symmetric bilinear form \(B\) satisfying \(xy=B(x,y)u\). Its radical is precisely \(\operatorname{Ann}(E)\), hence is zero. In any natural basis \((f_i)\), the form is diagonal with \(B(f_i,f_i)=a_i\ne0\). Because squaring is an automorphism of every finite field of characteristic two, each \(a_i\) has a unique nonzero square root. Rescaling \(f_i\) by its inverse makes \(B(f_i,f_i)=1\). This yields the stated dot-product form and a normalized basis \((e_i)\) with \(e_i^2=u\). Each equivalence class modulo individual rescalings has a unique representative up to reordering among normalized bases.

**2. Orthogonal frames and the characteristic vector.** Let \(V=\mathbb F_q^d\), endowed with \(B(x,y)=\sum_i x_i y_i\). The ordered normalized natural bases are precisely the orthonormal frames, parametrized freely by \(O(B)=\{g\in\mathrm{GL}_d(q):g^{\mathsf T}g=I\}\). If the columns of \(g\) give the new frame, the coordinates of the product generator are \(w=g^{-1}u\). Their support determines the graph because every frame vector squares to \(u\). The symmetric group on the \(d\) frame positions acts freely by reordering, so each unordered frame has exactly \(d!\) ordered representatives.

For every \(x\in V\),
\[
B(x,x)=\left(\sum_i x_i\right)^2=B(x,t)^2.
\]
An isometry preserves the left-hand side; injectivity of squaring implies it preserves the linear functional \(x\mapsto B(x,t)\), hence **fixes \(t\)**. Therefore \(c=B(u,t)\) is constant across the orbit, and every orbit lies in the affine hyperplane \(\sum_i w_i=c\).

**3. Odd-dimensional orthogonal group and orbits.** If \(d=2m+1\), then \(B(t,t)=1\). There is an orthogonal decomposition \(V=\mathbb F_qt\perp H\), where \(H=t^\perp\) is a nondegenerate alternating space of dimension \(2m\) (for \(x\in H\), \(B(x,x)=B(x,t)^2=0\)). Every isometry fixes \(t\), and restriction gives \(O(B)\cong\operatorname{Sp}(H)\). The symplectic group is transitive on nonzero vectors: each can be extended to a symplectic basis. The orbit of \(u=ct+x\), with \(x\in H\), is therefore a singleton if \(x=0\), or all \(ct+y\) with \(0\ne y\in H\) if \(x\ne0\). The latter has size \(q^{d-1}-1\).

**4. Even-dimensional orthogonal group and orbits.** If \(d=2m\), then \(B(t,t)=0\). Choose \(s=e_1\), so \(B(s,t)=B(s,s)=1\), and put \(H=\langle s,t\rangle^\perp\). This is a nondegenerate alternating space of dimension \(2m-2\). Every isometry fixes \(t\) and is uniquely described by \(S\in\operatorname{Sp}(H)\), \(z\in H\), and \(a\in\mathbb F_q\), acting as
\[
g(t)=t,\qquad g(s)=s+z+at,\qquad
 g(x)=Sx+B(z,Sx)t\quad(x\in H).
\]
Conversely these formulas preserve all pairings on \(\langle s,t\rangle\oplus H\), so give **all** isometries. Thus \(|O(B)|=q^{d-1}|\operatorname{Sp}_{d-2}(q)|\). Writing \(u=cs+x+bt\), if \(c\ne0\), choices of \(z,a\) move \(x,b\) arbitrarily and the orbit is the entire affine hyperplane with coordinate sum \(c\), of size \(q^{d-1}\). If \(c=0\) and \(x\ne0\), the symplectic group moves \(x\) through all of \(H\setminus\{0\}\), and varying \(z\) moves \(b\) arbitrarily; the orbit is the zero-sum hyperplane with the line \(\mathbb F_qt\) removed, of size \(q^{d-1}-q\). Nonzero vectors on this line are fixed.

**5. Group order.** Counting ordered symplectic bases of a nondegenerate alternating space of dimension \(2m\) gives
\[
|\operatorname{Sp}_{2m}(q)|=q^{m^2}\prod_{j=1}^{m}(q^{2j}-1).
\]
For example, after choosing any nonzero first vector and one partner with pairing one, their orthogonal complement is symplectic of dimension \(2m-2\), yielding the recursion \(|\operatorname{Sp}_{2m}(q)|=(q^{2m}-1)q^{2m-1}|\operatorname{Sp}_{2m-2}(q)|\), with initial value one. Together with Steps 3–4 this yields the displayed \(G_d=|O(B)|\).

**6. Hamming-weight distribution.** Let \(A_k(c)\) count \(k\)-tuples of nonzero field elements summing to \(c\). Choosing the final entry gives \(A_{k+1}(c)=(q-1)^k-A_k(c)\), initialized by \(A_1(0)=0\), \(A_1(c)=1\) when \(c\ne0\). Solving this recursion yields the formulas in the Finding section. Choosing the \(k\) nonzero coordinates among \(d\) positions gives \(\binom dk A_k(c)\) vectors of weight \(k\) and coordinate sum \(c\). In odd dimension the moving orbit excludes the unique point \(ct\), which has weight \(d\) exactly when \(c\ne0\); when \(c=0\) the omitted point is zero and has weight zero. In even dimension the nonzero-sum orbit includes the entire hyperplane, while the moving zero-sum orbit omits \(q-1\) nonzero multiples of \(t\), all of weight \(d\). These are exactly the displayed \(H_k\), and their sum equals the orbit size \(T\).

**7. From orbit frequencies to graph counts.** Since \(O(B)\) acts transitively on the orbit of \(u\), each vector \(w\) in that orbit is obtained from exactly \(G_d/T\) ordered normalized frames. Thus exactly \(G_dH_k/T\) ordered frames give graph support \(k\). Division by the free reordering factor \(d!\) gives \(C_k\); in particular it is an integer and its sum is \(G_d/d!\). A graph with every row identical and a nonempty target set has exactly \(k\) nonzero columns and is classified up to vertex permutation by \(k\), since the number of loops equals \(k\). For \(q\ge4\), if \(c\ne0\), one constructs all-nonzero tuples summing to \(c\): use one entry \(c\) and pairs of equal nonzero entries when \(k\) is odd, or entries \(a,c+a\) with \(a\notin\{0,c\}\), followed by equal pairs, when \(k\) is even. If \(c=0\), equal pairs provide every even \(k\ge2\), and the triple \(a,b,a+b\) with distinct nonzero \(a,b\), followed by equal pairs, provides every odd \(k\ge3\). In the odd-dimensional moving orbit with \(c\ne0\), choose \(a\notin\{0,c\}\) and use \(c\) plus pairs of \(a\) to ensure full support while avoiding the excluded scalar point \(ct\). In the even-dimensional moving zero-sum orbit, full support can be obtained using distinct nonzero pairs \(a,a,b,b\), followed by equal pairs, avoiding the excluded scalar line. These constructions establish precisely the asserted graph spectra, including the full-support boundaries, and complete the proof.

## Verification

A standalone standard-library checker in `verify.py` implements arithmetic in \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\); it enumerates the full finite orthogonal group and independently compares orbit cardinalities, complete graph-support histograms and all asserted natural-basis counts. Tested pairs \((q,d)\) are \((2,2),(2,3),(2,4),(2,5),(4,2),(4,3),(4,4),(8,2),(8,3)\). The characteristic-two prime field is included only as a computational boundary check, **not** in the claimed new domain. The checker returns `VERIFY_OK`. In particular, for \(q=4\) and \(d=4\), an anisotropic moving vector has counts \((C_1,C_2,C_3,C_4)=(10,30,70,50)\), while an isotropic moving vector has \((0,48,64,48)\), and a fixed-line vector has \((0,0,0,160)\). Every histogram sums to \(160\).

The symbolic proof covers all dimensions and extension degrees. Finite enumeration cannot establish the infinite-domain theorem and is used only to catch implementation or normalization errors.

## Relationship to prior work

Kaygorodov, Martín González and Viruel (arXiv:2610.22248v1, posted 2026-10-15) survey evolution algebras, their natural bases, automorphisms, graph dependence, and explicitly ask for the enumeration of natural bases modulo reordering and scaling and for understanding basis-dependent graph invariants. Their rank-one orthogonal-group example does not state an exact graph-support spectrum and natural-basis multiplicities for characteristic-two extension fields. Martín Barquero, Martín González and Sánchez-Ortega (2025, DOI below) classify commutative algebras having one-dimensional square through bilinear forms and establish an isometry description; that foundational classification does not enumerate the basis graphs and their frequencies. Boudi, Cabrera Casado and Siles Molina (arXiv:2006.14460v1, 2020) analyze natural families and orthogonal change-of-basis structures, without the present exact finite-field distribution.

Related computations in characteristic two at \(q=2\) and in odd-characteristic finite fields give distinct field domains and do not directly imply the \(q\ge4\) support-frequency classification. The results here draw on standard finite symplectic-group theory; priority for the explicit coupled support and basis-count formulas is qualified by possible older unindexed combinatorial treatments of orthonormal frames.

## Limitations

No classification is asserted for odd-characteristic fields, the prime field \(\mathbb F_2\), algebras with nonzero annihilator, algebras whose square has dimension greater than one, or higher-dimensional graph-isomorphism structures outside the common-row family. The theorem counts natural-basis classes of a fixed algebra, not nonisomorphic algebras. The proof uses classical symplectic transitivity and order formulas, independently justified above; its computational tests are finite only. Search-based originality assessment cannot establish absolute priority, and no independent audit has been performed.

## References

1. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first public 2026-10-15), https://arxiv.org/abs/2610.22248.
2. D. Martín Barquero, C. Martín González and J. Sánchez-Ortega, *Commutative Algebras with One-Dimensional Square*, Mediterranean Journal of Mathematics 22, article 48 (2025), https://doi.org/10.1007/s00009-025-02812-7.
3. N. Boudi, Y. Cabrera Casado and M. Siles Molina, *Natural families in evolution algebras*, arXiv:2006.14460v1 (2020), https://arxiv.org/abs/2006.14460.
