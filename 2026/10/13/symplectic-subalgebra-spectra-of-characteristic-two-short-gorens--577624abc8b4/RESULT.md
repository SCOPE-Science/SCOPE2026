# Symplectic subalgebra spectra of characteristic-two short Gorenstein algebras

## Finding
Let \(k=\mathbb F_q\), with \(q=2^e\), \(e\ge1\), and let \(m\ge1\). Let \(V\) be a \(2m\)-dimensional symplectic space with nondegenerate alternating form \(\omega\). Define the commutative unital \(k\)-algebra
\[
A=k\oplus V\oplus kz,\qquad vw=\omega(v,w)z,\quad zV=z^2=0.
\]
Its radical is \(J=V\oplus kz\), \(J^2=kz\), \(J^3=0\), and its socle is \(kz\). Thus it is an Artinian local Gorenstein algebra with Hilbert function \((1,2m,1)\). We classify all unital \(k\)-subalgebras (with the same identity), under its full \(k\)-algebra automorphism group.

Put \(S_n(q)=q^{n^2}\prod_{i=1}^n(q^{2i}-1)\), including \(S_0(q)=1\), and
\[
I_{m,r}(q)=\prod_{j=0}^{r-1}\frac{q^{2(m-j)}-1}{q^{r-j}-1}\quad(0\le r\le m),\qquad I_{m,0}(q)=1.
\]
For each \(r,s\ge0\) with \(r+s\le m\), there is exactly one orbit of subalgebras containing \(z\), with orbit size
\[
C_{m;r,s}(q)=I_{m,r}(q)\frac{S_{m-r}(q)}{S_s(q)S_{m-r-s}(q)}.
\]
Its representative is \(k\oplus kz\oplus L\), where \(L\le V\) has dimension \(r+2s\) and restriction-radical dimension \(r\). For each \(0\le d\le m\), there is exactly one orbit of subalgebras \(k\oplus U\) with \(z\notin U\), of size \(q^d I_{m,d}(q)\); here \(U\) projects isomorphically to a totally isotropic \(d\)-space in \(V\). These are all orbits, and none coincide. Hence
\[
\boxed{\#\bigl(\operatorname{Sub}_{k,1}(A)/\operatorname{Aut}_k(A)\bigr)=\frac{(m+1)(m+4)}2.}
\]
The dimension-generating polynomial of *all* unital subalgebras, including the unit subalgebra \(k\), is
\[
P_{m,q}(t)=\sum_{d=0}^{2m}{2m\brack d}_q\,t^{d+2}+\sum_{d=0}^m q^d I_{m,d}(q)\,t^{d+1},
\]
where \({n\brack d}_q=\prod_{i=0}^{d-1}(q^{n-i}-1)/(q^{d-i}-1)\) is a Gaussian coefficient. In particular,
\[
\#\operatorname{Sub}_{k,1}(A)=\sum_{d=0}^{2m}{2m\brack d}_q+\sum_{d=0}^m q^d I_{m,d}(q).
\]
Exactly \(\sum_{d=0}^{2m}{2m\brack d}_q+1\) of these subalgebras are \(k\)-vector-space translates \(k\oplus I\) of ideals \(I\subseteq J\): the ideals are \(0\) and precisely the subspaces containing \(kz\). The additional nonideal unital subalgebras, parameterized by nonzero isotropic spaces and graph maps, are counted by \(\sum_{d=1}^{m}q^d I_{m,d}(q)\).

For \(m=1\) the total is \(q^2+2q+4\), in five orbits of sizes \(1,1,1,q+1,q(q+1)\). For \(m=2,q=2\), the total is \(158\), in nine orbits of sizes \(1,1,1,15,15,15,20,30,60\).

## Assumptions and scope
The result applies to all powers of two \(q\) and all integers \(m\ge1\). The alternating form \(\omega\) is nondegenerate; this excludes both degenerate and nonalternating symmetric bilinear products. The algebra is not the full exterior algebra except for the four-dimensional case in characteristic two. All automorphisms and subalgebras are \(k\)-linear and unital. A subalgebra is not assumed to be an ideal.

## Proof
**1. Structure and automorphisms.** Since \(\omega\) is alternating and \(\operatorname{char}k=2\), it is symmetric; consequently the displayed multiplication is commutative and associative, since every product of two elements of \(J\) lies in \(kz\) and \(zJ=0\). Its unique maximal ideal is \(J\), and nondegeneracy gives \(\operatorname{Ann}_A(J)=kz\). Any algebra automorphism induces an invertible linear map \(g\) on \(J/J^2\cong V\), a nonzero scalar \(c\) on \(J^2=kz\), and an arbitrary linear correction \(\ell:V\to k\). Multiplicativity is equivalent to \(\omega(gv,gw)=c\omega(v,w)\). Conversely each \((g,c,\ell)\) satisfying this equation defines an automorphism by \(v\mapsto gv+\ell(v)z\), \(z\mapsto cz\). Thus the automorphism group acts through all symplectic similitudes together with every central shear \(\ell\).

**2. Dichotomy for subalgebras.** A unital subalgebra is uniquely \(k\oplus U\) with a vector subspace \(U\le J\) satisfying \(U^2\subseteq U\). If \(z\in U\), this closure condition is automatic. Then \(U=\pi^{-1}(L)\) for a unique \(L\le V\), where \(\pi:J\to V=J/kz\). If \(z\notin U\), \(\pi|_U\) identifies \(U\) with a subspace \(L\le V\) and \(U\) is the graph of a unique linear map \(\lambda:L\to kz\). Since \(U\cap kz=0\), the closure condition holds exactly when \(\omega|_{L\times L}=0\), i.e., \(L\) is totally isotropic. The arbitrary central shears act transitively on graph maps over a fixed \(L\).

**3. Orbit parameters.** Symplectic Witt extension and the symplectic Gram--Schmidt decomposition show that symplectic transformations act transitively on subspaces \(L\le V\) with a given dimension \(d\) and given \(r=\dim(L\cap L^\perp)\). The quotient \(L/(L\cap L^\perp)\) has rank \(2s=d-r\), and such subspaces exist precisely when \(r,s\ge0\) and \(r+s\le m\). Therefore subalgebras containing \(z\) have one orbit for each \((r,s)\). On totally isotropic \(d\)-spaces the symplectic group is transitive for \(0\le d\le m\); shear transitivity then gives one orbit for each \(d\) among subalgebras not containing \(z\). These orbit systems cannot meet, since containing \(J^2\) is automorphism-invariant.

**4. Fiber sizes.** The number of totally isotropic \(r\)-spaces in \(V\) is \(I_{m,r}(q)\): count ordered bases by selecting successive vectors in the orthogonals of the previously selected isotropic vectors, then divide by \(|\mathrm{GL}_r(q)|\). For a fixed isotropic \(r\)-space \(R\), any \(L\) having \(L\cap L^\perp=R\) is uniquely the inverse image of a nondegenerate symplectic \(2s\)-subspace of \(R^\perp/R\), a \(2(m-r)\)-dimensional symplectic space. The symplectic group acts transitively on these nondegenerate subspaces; their number is \(S_{m-r}/(S_sS_{m-r-s})\), by the orthogonal direct-sum decomposition into complementary symplectic spaces. Multiplication gives \(C_{m;r,s}\). A totally isotropic \(d\)-space has exactly \(q^d\) graph maps to \(kz\), giving the second orbit-size formula.

**5. Totals and ideals.** There are \(\sum_{r=0}^m(m-r+1)=(m+1)(m+2)/2\) containing-socle orbits and \(m+1\) disjoint-socle orbits. To count individual subalgebras, the containing-socle choices correspond bijectively to all subspaces of the \(2m\)-space \(V\), and the disjoint-socle choices are the isotropic graphs counted above. For an ideal \(I\subseteq J\), nonzero \(v\in\pi(I)\) has \(vJ=kz\) by nondegeneracy, so either \(I=0\) or \(z\in I\). Conversely every \(I\) containing \(kz\) is an ideal. This proves all formulas.

## Verification
Run `python3 artifacts/verify.py` with Python 3, requiring only its standard library. The checker enumerates every vector subspace of \(J\) in reduced row-echelon form, tests multiplicative closure, independently identifies orbit invariants and predicted cardinalities, and reconstructs group orbits using central shears and symplectic transvections over the tested fields. Complete subalgebra counts were checked for \((m,q)=(1,2),(1,4),(1,8),(2,2),(2,4),(3,2)\), yielding respectively \(12,28,84,158,2230,5292\). Group orbit sizes were reconstructed for \((1,2),(1,4),(2,2),(3,2)\); the checker terminates `VERIFY_OK`. Finite tests are corroboration, not a replacement for the proof in arbitrary dimension.

## Relationship to prior work
Jelisiejew's *Classifying local Artinian Gorenstein algebras* (arXiv:1511.08007; first posted 25 November 2015; primary MSC 13H10) studies isomorphism classification and local inverse systems; its main results do not enumerate embedded unital subalgebras over finite fields of characteristic two. The symplectic subspace stratification used above is classical; in particular Liu's 2013 paper on lattices generated by singular-symplectic subspace orbits describes the analogous rank-and-intersection types. The claim here is not a new form of Witt's lemma or a new formula for symplectic Grassmannians: it is their precise translation into all subalgebras of this family of local Gorenstein rings, including the graph-map fibers, the complete automorphism-orbit decomposition, and the ideal/nonideal separation.

## Limitations
No classification is asserted for odd characteristic, nonalternating or degenerate multiplication tensors, nonunital subrings, or arbitrary short Gorenstein algebras. The full uniqueness/novelty of the combination against all potentially equivalent ring-enumeration terminology is not independently certified. All computational checks are finite; the unbounded statement follows from the symbolic proof. Independent review has not been performed.

## References
1. J. Jelisiejew, *Classifying local Artinian Gorenstein algebras*, arXiv:1511.08007 (first public 2015-11-25), https://arxiv.org/abs/1511.08007.
2. X. Liu, *Lattices Generated by Two Orbits of Subspaces under Finite Singular Symplectic Groups*, Journal of Applied Mathematics 2013, Article 732808, https://doi.org/10.1155/2013/732808.
3. *Lattices Generated by Subspaces under Symplectic Group over a Finite Field*, Ars Combinatoria 96 (2010), 459--467, https://combinatorialpress.com/ars-articles/volume-096-ars-articles/lattices-generated-by-subspaces-under-symplectic-group-over-a-finite-field/ (abstract consulted).
