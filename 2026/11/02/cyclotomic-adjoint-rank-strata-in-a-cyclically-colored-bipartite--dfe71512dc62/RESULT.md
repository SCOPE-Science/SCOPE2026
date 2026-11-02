# Cyclotomic adjoint-rank strata in a cyclically colored bipartite Lie algebra

## Finding

**Theorem.** Fix any integer \(n\ge 4\) and any prime power \(q\). Let \(L_n(q)\) be the Lie algebra described below, and define its adjoint-rank enumerator by
\[
F_{n,q}(t)=\sum_{x\in L_n(q)}t^{\operatorname{rank}_{\mathbb F_q}(\operatorname{ad}_x)}.
\]
Put \(g=\gcd(n,q-1)\). Then
\[
\boxed{\begin{aligned}
F_{n,q}(t)=q^n\big[&1+g(q-1)t+(q^n-1-g(q-1))t^2\\
&+g(q-1)q^{n-1}t^{n-1}\\
&+((q^2-1)q^n-g(q-1)q^{n-1})t^n\big].
\end{aligned}}
\]
The only possible adjoint ranks are \(0,1,2,n-1,n\); all five occur for the stated parameters. In particular, in the fixed dimension-eight case \(n=4\), the number of elements of adjoint rank three is
\[
\boxed{q^7(q-1)\gcd(4,q-1),}
\]
which is **not the evaluation of any single polynomial with rational coefficients in \(q\)** across all prime powers. The obstruction occurs already along powers of the single prime \(3\).

## Assumptions and scope

The field \(k=\mathbb F_q\) may have arbitrary characteristic. The vector space \(L_n(q)\) has basis
\[
u_0,u_1,v_0,\ldots,v_{n-1},z_0,\ldots,z_{n-1}.
\]
All subscripts on \(v\) and \(z\) are read modulo \(n\). Its only nonzero basic brackets, apart from their alternating and skew-symmetric partners, are
\[
[u_0,v_j]=z_j,\qquad [u_1,v_j]=z_{j+1}\quad(0\le j<n).
\]
Here \([x,x]=0\) is stipulated in characteristic two. The span \(Z=\langle z_0,\ldots,z_{n-1}\rangle\) is central, and every double bracket vanishes; hence the Jacobi identity holds over every finite field. In graph terms, this is the complete bipartite graph \(K_{2,n}\), with its \(2n\) edges colored by \(n\) colors, each color used on two disjoint edges. The coloring is proper and equifrequent; for \(n>2\) the graph is not regular, so this is not a 'uniform graph' in the more restrictive regular-graph terminology.

The statement counts **all** elements of the Lie algebra, not central cosets or isomorphism classes. The exponent records linear rank over \(\mathbb F_q\) of the adjoint endomorphism; it is not a group conjugacy-class count or an adjoint orbit dimension over a different field. The dimension is \(2n+2\) and \(|L_n(q)|=q^{2n+2}\).

## Proof

**1. Exact image of an adjoint.** Let \(U=\langle u_0,u_1\rangle\), \(V=\langle v_0,\ldots,v_{n-1}\rangle\), so \(L=U\oplus V\oplus Z\). Identify both \(V\) and \(Z\) with
\[
R=k[T]/(T^n-1)
\]
using their listed bases, and let multiplication by \(T\) denote the cyclic shift. For each \(x=a u_0+b u_1+w+z\) with \(a,b\in k\), \(w\in V\), and \(z\in Z\), direct evaluation of the defining brackets gives
\[
\operatorname{im}(\operatorname{ad}_x)
=(a+bT)R+\operatorname{span}_k\{w,Tw\}\subseteq Z.
\tag{1}
\]
The minus signs on \([w,u_i]\) do not change the generated subspace; the central coordinate \(z\) does not affect the rank. Therefore every count of triples \((a,b,w)\) must be multiplied by \(q^n\).

**2. Zero pencil.** If \(a=b=0\), equation (1) is \(\operatorname{span}\{w,Tw\}\). It has rank zero only for \(w=0\). For nonzero \(w\), it has rank one precisely when \(Tw=\lambda w\) for some \(\lambda\in k^\times\). Since \(T^n=I\), necessarily \(\lambda^n=1\). Conversely, for every \(n\)-th root of unity \(\lambda\in k\), the cyclic-shift eigenspace is exactly one-dimensional: choosing one coordinate fixes all others. The cyclic multiplicative group \(k^\times\) contains exactly \(g=\gcd(n,q-1)\) such roots. Hence there are \(g(q-1)\) vectors giving rank one and \(q^n-1-g(q-1)\) giving rank two. No diagonalizability of \(T\) is presumed, so this remains valid when the characteristic divides \(n\).

**3. Nonzero pencil.** Assume \((a,b)\ne(0,0)\). A degree-at-most-one polynomial \(a+bT\) is a unit in \(R\) unless \(b\ne0\) and \(a+bT=b(T-\lambda)\) for some \(\lambda\in k^\times\) with \(\lambda^n=1\). Thus exactly \(g(q-1)\) nonzero pencil parameters are nonunits, while \(q^2-1-g(q-1)\) are units. For a unit, equation (1) has rank \(n\) for all \(q^n\) choices of \(w\). For a nonunit, multiplication by \(a+bT\) has image of dimension \(n-1\) (the quotient by \(T-\lambda\) is a one-dimensional \(k\)-space). The images of \(w,Tw\) in that quotient are proportional because \(T=\lambda\) there. Consequently the rank is \(n-1\) for the exactly \(q^{n-1}\) vectors \(w\in(a+bT)R\), and otherwise the rank is \(n\). The resulting counts are \(g(q-1)q^{n-1}\) at rank \(n-1\) and \((q^2-1)q^n-g(q-1)q^{n-1}\) at rank \(n\).

**4. Combine, boundaries and polynomiality.** Combine the mutually exclusive cases and multiply by \(q^n\) for the arbitrary central coordinate. Since \(n\ge4\), the five displayed exponents are distinct. Every coefficient is positive: \(g\ge1\), \(g(q-1)\le q^n-1\), and unit pencils exist (take \(a=1,b=0\)); likewise nonzero non-eigenvectors exist because \(n\ge4\). Substituting \(t=1\) yields \(F_{n,q}(1)=q^{2n+2}\), providing an independent total-count consistency check.

When \(n=4\), the rank-three coefficient is \(q^n\cdot g(q-1)q^{n-1}=q^7(q-1)g\). For \(q=3^k\), this has \(g=2\) when \(k\) is odd and \(g=4\) when \(k\) is even. If a rational polynomial \(P(q)\) matched it at every prime power, the infinitely many odd \(k\) would force the polynomial identity \(P(q)=2q^7(q-1)\), contradicting the infinitely many even \(k\). This proves the claimed arithmetic failure of polynomiality.

## Verification

The standalone Python 3 file `verify.py` constructs the matrix columns of \(\operatorname{ad}_x\) directly from the Lie brackets, performs finite-field Gaussian elimination, and exhaustively enumerates all noncentral parameters \((a,b,w)\). It does **not** use the quotient-ring image formula from the proof to calculate ranks. It checks the predicted multiplicities for \((n,q)=(4,2),(4,3),(4,4),(4,5),(4,7),(5,2),(5,3),(6,2)\), including \(\mathbb F_4\) as a nonprime field. It also checks the fixed-prime parity cycle \(q\in\{3,9,27,81\}\) in the exact coefficient formula. Run from the package directory with `python3 verify.py`; success ends with `VERIFY_OK`.

Illustratively, for \(n=4,q=3\), the noncentral rank multiplicities at ranks \(0,1,2,3,4\) are \((1,4,76,108,540)\). Multiplying each by \(q^4=81\) gives the full Lie-algebra counts. Exhaustive examples and formula checks are consistency evidence; the infinite statement is proved above independently of computation.

## Relationship to prior work

Godoy Molina and Lagos introduced the general labeled-directed-graph Lie construction, and in Sections 5.1–5.2 of their 2023 preprint analyzed graded derivations of complete bipartite graphs colored with a **single** label or with **one distinct label per edge**. The present intermediate proper coloring uses \(n\) labels on \(2n\) edges and instead counts adjoint ranks. The method and numerical invariant are different.

Rossmann (2022) proves a class-size polynomial for graphical groups attached to simple graphs with **independent central generators on distinct edges**. That theorem covers the distinct-edge specialization, not the present quotient which identifies pairs of edge labels. The current rank-three stratum's dependence on \(\gcd(4,q-1)\) shows precisely why naïvely extending polynomiality to such label identifications is impossible. The familiar linear-algebra criterion for invertibility of a cyclic pencil is used here, not claimed as independently new.

Chakrabarti, Mainkar and Swiatlowski study graph symmetries and automorphisms for a different, odd-order complete-graph coloring; Payne and Schroeder develop the uniform-colored-graph framework for regular graphs. Neither inspected paper gives this complete-bipartite adjoint-rank formula. The graph \(K_{2,n}\) is nonregular for \(n>2\), so the latter's regularity-dependent results cannot be mechanically applied.

## Limitations

The formula applies to the precisely defined cyclic matching coloring, not arbitrary proper edge colorings, general complete bipartite graph sizes, or arbitrary finite rings. The rank is a Lie adjoint rank, and group-theoretic consequences in small characteristic are not asserted. The odd/even exponent of field size in the polynomiality argument refers to powers of the prime \(3\), not parity of \(q\). The published-priority comparison is a best-knowledge assessment: an older general matrix-pencil or colored-Lie-algebra enumeration may imply this result without using its terminology. The supplied finite checks alone would not prove its unbounded range, and independent mathematical audit has not been performed.

## References

1. Mauricio Godoy Molina and Diego Lagos, *Lie algebras associated with labeled directed graphs*, arXiv:2308.00272, first publicly posted 2023-08-01; *Communications in Algebra* 52 (2024), 3115–3125. https://arxiv.org/abs/2308.00272 ; https://doi.org/10.1080/00927872.2024.2315306 .
2. Tobias Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, *Bulletin of the London Mathematical Society* 54 (2022), 1923–1943. https://doi.org/10.1112/blms.12665 .
3. Debraj Chakrabarti, Meera Mainkar and Savannah Swiatlowski, *Automorphism groups of nilpotent Lie algebras associated to certain graphs*, arXiv:1812.09439; *Communications in Algebra* 48 (2020), 263–273. https://arxiv.org/abs/1812.09439 .
4. Tracy L. Payne and Matthew Schroeder, *Uniform Lie algebras and uniformly colored graphs*, arXiv:1603.00803; *Advances in Geometry* 17 (2017), 507–524. https://arxiv.org/abs/1603.00803 .
