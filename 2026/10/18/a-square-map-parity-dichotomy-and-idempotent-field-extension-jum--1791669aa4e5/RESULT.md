# A square-map parity dichotomy and idempotent field-extension jump for cubelike evolution algebras

## Finding

Let \(G=(\mathbb F_2)^d\), \(d\ge1\), and let \(S\subseteq G\setminus\{0\}\) be a nonempty generating set. Over **any field \(K\) of characteristic two**, define the Cayley evolution algebra \(E_K(G,S)\) with natural basis \(\{e_g:g\in G\}\) and products
\[
e_g e_h=0\quad(g\ne h),\qquad e_g^2=\sum_{s\in S}e_{g+s}.
\]
Put \(N=|G|=2^d\), \(t=|S|\), and write \(A\in M_N(\mathbb F_2)\) for the adjacency matrix of the cubelike graph. The quadratic squaring map \(Q(x)=x^2\) has the exact dichotomy
\[
Q(Q(x))=(t\bmod2)\,x^{[4]}
\]
for every \(x\in E_K(G,S)\), where \(x^{[4]}\) denotes coordinatewise fourth powers with respect to the specified basis. In particular, if \(t\) is even then \(Q^2=0\); zero is the only idempotent and every generator has vanishing second iterated square.

If \(t\) is odd, set \(B=A+I_N\), \(r=\operatorname{rank}_{\mathbb F_2}(B)\), and let \(\operatorname{Idem}(E)=\{x\in E:x^2=x\}\). Then \(B^2=0\), and all idempotents have the following **complete explicit descriptions**:
\[
\operatorname{Idem}(E)=
\begin{cases}
\ker_{\mathbb F_2}(B),&\mathbb F_4\not\subseteq K,\\
\{u+\omega Bu:u\in\mathbb F_2^N\},&\mathbb F_4\subseteq K,
\end{cases}
\]
where \(\omega\in\mathbb F_4\setminus\mathbb F_2\) satisfies \(\omega^2+\omega+1=0\). Consequently,
\[
|\operatorname{Idem}(E)|=
\begin{cases}
2^{N-r},&\mathbb F_4\not\subseteq K,\\
2^N,&\mathbb F_4\subseteq K.
\end{cases}
\]
The first set is identified with its natural \(\mathbb F_2\)-coordinate embedding in \(K^N\). The choice of either root \(\omega\) gives the same set. Both counts include zero and remain finite even for infinite fields \(K\). For \(K=\mathbb F_{2^m}\), containment of \(\mathbb F_4\) is equivalent to \(m\) being even.

For the \(d\)-dimensional hypercube, \(S\) is the set of \(d\) standard unit vectors. The number of idempotents is exactly one for even \(d\); for odd \(d\) it is \(2^{2^{d-1}}\) when \(\mathbb F_4\not\subseteq K\), and \(2^{2^d}\) when \(\mathbb F_4\subseteq K\). At the other rank extreme, the complete cubelike graph obtained from \(S=G\setminus\{0\}\) has \(r=1\), hence \(2^{N-1}\) or \(2^N\) idempotents.

## Assumptions and scope

All algebras in the theorem are *unweighted*, loopless cubelike Cayley evolution algebras, with characteristic-two coefficient field. The assumption that \(S\) generates \(G\) ensures that the underlying undirected graph is connected and has positive Cheeger constant; no uniform expansion lower bound across dimensions is asserted. The integer \(t\) is the graph valency. The notation \(Q^2\) means composition \(Q\circ Q\), and \(x^{[4]}\) means the vector with \(g\)-coordinate \(x_g^4\), not an arbitrary association of four algebra factors. An idempotent is an **element** with \(x^2=x\); this is distinct from calling an evolution algebra perfect when \(E^2=E\).

## Proof

**(1) Adjacency-square identity.** For every \(s\in S\), let \(P_s\) be translation by \(s\) on coordinate vectors. Because \(G\) is elementary abelian of exponent two, the translation matrices commute and \(P_s^2=I_N\). The binary adjacency matrix is \(A=\sum_{s\in S}P_s\). Squaring over a ring of characteristic two cancels all mixed terms, so
\[
A^2=\sum_{s\in S}P_s^2=(t\bmod2)I_N.
\]
Here the same binary matrix identity holds after scalar extension from \(\mathbb F_2\) to \(K\).

**(2) Plenary dynamics.** The definition of an evolution algebra makes the coordinate equation for squaring
\[
Q(x)=A(x_g^2)_{g\in G}.
\]
Since the entries of \(A\) lie in the prime subfield, raising its action to the second coordinatewise power commutes with \(A\). Thus
\[
Q(Q(x))=A^2(x_g^4)_{g\in G}=(t\bmod2)(x_g^4)_{g\in G}.
\]
For even \(t\), this equals zero identically. If \(Q(x)=x\), applying \(Q\) again gives \(x=0\). For a basis vector \(e_g\), \(Q(e_g)\) is the nonzero sum of its neighbours but \(Q^2(e_g)=0\). For odd \(t\), \(Q^2(e_g)=e_g\) and \(Q(e_g)\ne e_g\), producing an exact two-cycle of plenary iterates. These are statements about a map on elements; \(Q^2=0\) does not claim that every ordinary nonassociative product of four elements vanishes.

**(3) Fields of definition of idempotents.** Assume \(t\) is odd. Then \(A^2=I_N\) and \(B=A+I_N\) has \(B^2=0\). If \(x\) is idempotent, the dynamics identity yields \(x_g^4=x_g\) for every coordinate \(g\). The roots of \(z^4-z\) in an algebraic closure are exactly \(\mathbb F_4\). Hence all coordinates lie in \(K\cap\mathbb F_4\), equal to \(\mathbb F_2\) when \(K\) lacks \(\mathbb F_4\), and to \(\mathbb F_4\) when it contains that subfield. This is valid even if \(K\) is infinite or imperfect.

**(4) No quadratic subfield.** When \(\mathbb F_4\not\subseteq K\), any fixed point is a binary vector \(u\in\mathbb F_2^N\); since \(u_g^2=u_g\), its idempotent equation is \(Au=u\), equivalent to \(Bu=0\). Conversely all such vectors are idempotent. Rank–nullity gives \(2^{N-r}\) points.

**(5) Quadratic subfield.** When \(\mathbb F_4\subseteq K\), choose \(\omega^2+\omega+1=0\). Every possible idempotent has a unique decomposition \(x=u+\omega v\), with \(u,v\in\mathbb F_2^N\). Equating components of
\[
u+\omega v=A(u+\omega^2v)=A(u+v)+\omega Av
\]
shows \(v=Av\) and \(u=A(u+v)\). Because \(B=A+I_N\), these are equivalent to \(v=Bu\) and \(Bv=0\). The second condition follows automatically from \(B^2u=0\). Therefore each of the \(2^N\) binary vectors \(u\) yields exactly one idempotent \(u+\omega Bu\), and all idempotents occur. Replacing \(\omega\) by \(\omega+1\) changes the parameter from \(u\) to \(u+Bu\), an involutory bijection since \(B^2=0\).

**(6) Hypercube and complete graph ranks.** For the hypercube \(S=\{v_1,\ldots,v_d\}\), identify the group algebra over \(\mathbb F_2\) with
\[
\mathbb F_2[y_1,\ldots,y_d]/(y_1^2,\ldots,y_d^2),\qquad v_i\longleftrightarrow1+y_i.
\]
When \(d\) is odd, multiplication by \(B=I_N+A\) corresponds to multiplication by \(y_1+\cdots+y_d\). An invertible linear change of the square-zero variables carries this nonzero linear form to \(y_1\), whose multiplication map has rank \(2^{d-1}\) (monomials not containing \(y_1\) map bijectively to those containing it). In the complete cubelike case, \(A=J+I_N\), so \(B=J\), the all-ones matrix of rank one. Substitute these ranks in the already established formula. \(\square\)

## Verification

The accompanying standalone `verify.py` rebuilds the cubelike adjacency matrices, checks \(A^2=(t\bmod2)I_N\) by exact binary arithmetic, evaluates actual algebra squares using finite-field arithmetic, and independently exhausts every potential idempotent in 17 finite cases over \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\). The \(\mathbb F_4\) and \(\mathbb F_8\) computations use irreducible binary polynomials, not integer arithmetic modulo four or eight. It also checks the explicit \(\mathbb F_4\) parametrization and four odd-dimensional hypercube ranks through dimension seven (21 checks total). Running `python3 verify.py` produced `VERIFY_OK 21 cases`. The general theorem for arbitrary characteristic-two fields follows from the symbolic proof above, not the finite experiments.

## Relationship to prior work

Giacomelli's *Expander Evolution Algebras* (arXiv:2605.12672v1, first posted 12 May 2026), especially Definition 9.1 and Theorems 4.3 and 4.5, supplies the motivating Cayley family, expansion framework, and plenary-persistence assertions. The actual binary-coefficient cancellation in the present construction shows why a graph-neighbourhood union cannot universally be substituted for the support of an algebraic sum. Already the square/cycle on four vertices is a connected symmetric example for which \(Q^2=0\), in contrast to the unconditional persistence/cover-time assertions in that preprint. This is a specific mathematical implication comparison, not a claim about all properties of its other constructions.

Costoya, Muñoz, Tocino, and Viruel (arXiv:2207.01335; published 2023) study Cayley evolution algebras with emphasis on their automorphism groups. García-Martínez and Pérez-Rodríguez (2026) study existence of idempotents and complete evolution algebras over \(\mathbb C\); their result is not a characteristic-two cubelike count. A previous finite-binary general census of idempotent *elements* in perfect evolution algebras covers the \(K=\mathbb F_2\) perfect-algebra subcase, and this subcase is **not** presented as independently new. The distinction established here is the full cubelike plenary-square parity law, field-independent exact parametrization, and sharp \(\mathbb F_4\)-extension jump in *all* characteristic-two fields. Literature searches did not locate an equivalent theorem, but absence of search hits does not establish priority.

## Limitations

The theorem is restricted to the all-ones unweighted Cayley multiplication on elementary-abelian two-groups in characteristic two; it does not address other finite groups, odd characteristic, or nonconstant edge weights. The complete binary rank \(r\) is an explicit computable invariant of the chosen generating set; no closed expression for \(r\) for *every* generating set is claimed. Connection to a graph with positive Cheeger constant is pointwise in each finite dimension, not a uniform spectral-expander assertion. The theorem classifies idempotent **elements** and iterative squares, not ideals, algebra isomorphism classes, or the full nonassociative ideal structure. Its finite computations are corroboration only. Possible older equivalent formulations through Frobenius-semilinear maps or truncated group algebras remain a residual literature risk; no independent originality or correctness audit has been performed.

## References

1. P. Giacomelli, *Expander Evolution Algebras*, arXiv:2605.12672v1 (12 May 2026), especially Sections 4 and 9.1. https://arxiv.org/html/2605.12672v1
2. C. Costoya, V. Muñoz, A. Tocino, A. Viruel, *Automorphism groups of Cayley evolution algebras*, arXiv:2207.01335; Rev. R. Acad. Cienc. Exactas Fis. Nat. Ser. A Mat. **117** (2023), art. 82. https://doi.org/10.1007/s13398-023-01414-w
3. X. García-Martínez, A. Pérez-Rodríguez, *A note on complete evolution algebras*, Archiv der Mathematik **126** (2026), 597–604, Section 3.3. https://doi.org/10.1007/s00013-026-02251-0
4. A. Elduque, A. Labra, *Evolution algebras and graphs*, Journal of Algebra and Its Applications **14** (2015), 1550103. https://doi.org/10.1142/S0219498815501030
