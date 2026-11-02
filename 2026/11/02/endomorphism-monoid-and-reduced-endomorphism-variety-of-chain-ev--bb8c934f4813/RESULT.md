# Endomorphism monoid and reduced endomorphism variety of chain evolution algebras

## Finding

For every field \(k\) and integer \(n\ge2\), the chain evolution algebra \(E_n(k)\) has a completely explicit algebra-endomorphism monoid, reduced endomorphism variety, and finite-field rank distribution. With coordinates \(a_1,\ldots,a_n\) for the image of its first basis element, the full set of algebra endomorphisms is exactly
\[
\bigl\{(a_1,\ldots,a_n): a_i a_j=0\text{ for all }1\le i<j\le n-1\bigr\}.
\]
The coordinate \(a_n\) is free. The image of every other basis element is determined uniquely by iterated squaring. The reduced endomorphism variety is
\[
\operatorname{End}_{\rm alg}(E_n)_{\rm red}\cong
\mathbb A_k^1\times\operatorname{Spec}\!\left(k[a_1,\ldots,a_{n-1}]/(a_i a_j: i<j)\right).
\]
For \(n\ge3\), it has \(n-1\) irreducible affine-plane components with common affine-line intersection; at \(n=2\) it is one affine plane. Its dimension is always two.

Over every finite field \(\mathbb F_q\), the numbers \(N_r\) of endomorphisms of rank \(r\) are
\[
N_0=1,\quad N_1=q-1,\quad N_r=q(q-1)\quad(2\le r\le n).
\]
Thus the complete count is \((n-1)q^2-(n-2)q\). Every noninvertible endomorphism is nilpotent under composition. Only the zero map and the identity are idempotent endomorphisms.

## Assumptions and scope

Here an **algebra endomorphism** is any \(k\)-linear map \(f:E_n\to E_n\) preserving multiplication; neither invertibility nor preservation of a natural basis is assumed. Define the commutative, generally nonassociative evolution algebra by its basis \(e_1,\dots,e_n\) and products \(e_i e_j=0\) for \(i\ne j\), \(e_i^2=e_{i+1}\) for \(1\le i<n\), and \(e_n^2=0\). All fields and all integers \(n\ge2\) are allowed. The coordinate variety statement concerns the **reduced** endomorphism scheme, not the unreduced scheme. Rank is ordinary linear-map rank; nilpotency index refers to composition, not nilpotency index of \(E_n\).

## Proof

**1. Determine an endomorphism from one column.** Since \(e_{j+1}=e_j^2\), let
\[
f(e_1)=u=\sum_{s=1}^{n}a_s e_s.
\]
Any multiplicative map must satisfy \(f(e_{j+1})=f(e_j)^2\), so
\[
f(e_j)=\sum_{s=1}^{n-j+1}a_s^{2^{j-1}}e_{s+j-1},\qquad 1\le j\le n.\tag{1}
\]
Conversely the images in (1) preserve every square relation, including \(e_n^2=0\), because squaring shifts support strictly upward. Multiplicativity is therefore equivalent to the remaining relations \(f(e_i)f(e_j)=0\) for all \(i<j\).

**2. Exclude two distinct nonterminal coefficients.** Suppose \(1\le s<t\le n-1\) and \(a_s,a_t\ne0\). Put \(j=t-s+1\), so \(2\le j\le n\). In the coefficient of \(e_{t+1}\) in \(f(e_1)f(e_j)\), only the coordinate \(e_t\) contributes, and that coefficient is
\[
a_t a_s^{2^{t-s}}\ne0.
\]
This contradicts \(e_1e_j=0\). Thus at most one of \(a_1,\ldots,a_{n-1}\) is nonzero. Conversely if there is at most one, then each of the nonterminal images in (1) has one support position and the positions for distinct \(j\) are distinct. Any additional \(e_n\) term in \(f(e_1)\) contributes nothing to multiplication because \(e_n E_n=0\). Consequently all mixed products vanish. This proves the classification over every field without a characteristic assumption.

**3. Reduced algebraic geometry.** In the universal polynomial coordinate ring \(R=k[a_1,\ldots,a_n]\), formula (1) eliminates all other endomorphism-matrix coordinates. Let \(I\subset R\) be the ideal of mixed-product polynomial equations. Set
\[
K=(a_s a_t:1\le s<t\le n-1).
\]
Every coefficient of every mixed product is a sum of monomials divisible by one of the displayed square-free products, hence \(I\subseteq K\). Conversely, the specific mixed-product coefficient in step 2 gives \(a_ta_s^{2^{t-s}}\in I\), so \(a_sa_t\in\sqrt I\) for all \(s<t\le n-1\). The square-free monomial ideal \(K\) is radical. Thus \(\sqrt I=K\), proving the asserted reduced scheme, its geometric irreducible components, and their intersections. The same argument remains valid after any field extension.

**4. Rank spectrum.** If all the first \(n-1\) coefficients vanish, the map is zero when \(a_n=0\) and has rank one otherwise. Otherwise, let \(a_s\ne0\) be the unique nonterminal coefficient and write \(u=a_s e_s+a_ne_n\). The subsequent nonzero images are nonzero multiples of \(e_{s+1},\ldots,e_n\). Therefore the image has dimension exactly \(n-s+1\), independently of \(a_n\). For each \(s\) there are \((q-1)q\) choices over \(\mathbb F_q\); the cases \(s=n-1,n-2,\ldots,1\) produce exactly the ranks \(2,3,\ldots,n\). This yields the full distribution and total count.

**5. Composition structure.** If \(s=1\), the images form a triangular matrix with nonzero diagonal entries, hence the endomorphism is invertible. If \(s\ge2\), each iteration moves every surviving leading support index upward by \(s-1\); starting from \(e_1\), the term at index \(1+j(s-1)\) in \(f^{\circ j}(e_1)\) is nonzero whenever the index is \(\le n\), because its coefficient is a positive power of \(a_s\). Later basis vectors vanish at least as quickly. Thus \(f\) is composition-nilpotent of exact index
\[
1+\left\lfloor\frac{n-1}{s-1}\right\rfloor.
\]
If only \(a_n\) is nonzero, the nonzero rank-one map has square zero; the zero map has index one. Therefore every nonunit is nilpotent. An idempotent endomorphism is either invertible, hence the identity, or nilpotent, hence zero.

## Verification

The accompanying standard-library Python program `verify.py` checks the multiplication relations directly, independently of the symbolic proof. In seven small configurations it enumerates **all** linear maps and selects the multiplicative ones; in four larger configurations it exhaustively enumerates generator images. The tested fields are \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), including a nonprime field. It computes matrix ranks by field elimination and directly composes each classified endomorphism until it reaches zero or is invertible. All eleven configurations passed with final marker `EVOLUTION_CHAIN_ENDOMORPHISM_OK`. Finite checks corroborate but do not establish the uniform theorem; the proof above establishes it for arbitrary fields and dimensions.

## Relationship to prior work

Camacho, Gómez, Omirov and Turdibaev, *Some properties of evolution algebras* (arXiv:1004.1987v1, submitted 2010-04-12), place maximal nilpotency index in the standard evolution-algebra setting. Casas, Ladra, Omirov and Rozikov, *On evolution algebras* (arXiv:1004.1050v1, submitted 2010-04-07), discuss nilpotency and, in §5, **isomorphisms** for a special nonsingular-block family; their term homomorphism imposes a natural-basis condition absent from the unrestricted algebra-endomorphism definition used here. Casas and collaborators (arXiv:1208.1709) and Hegazi–Abdelwahab (arXiv:1508.06860) develop nilpotent classifications. Elduque–Labra (arXiv:1312.4685) connect evolution algebras with graphs. Mukhamedov and collaborators (arXiv:1805.10285) classify **automorphisms** and local automorphisms of maximal-nilindex evolution algebras; this corresponds to the invertible rank-\(n\) portion but does not give the noninvertible rank strata, reduced endomorphism variety or nilpotent composition indices. No full equivalent endomorphism-monoid classification was identified among these inspected relevant sources and targeted bibliographic comparisons. This is a best-knowledge comparison, not a global publication-priority certificate.

## Limitations

The classification is for the pure chain multiplication stated above, not every nilpotent evolution algebra of maximal nilpotency index with arbitrary higher structural constants. The geometric assertion concerns only the reduced endomorphism scheme; possible infinitesimal/nonreduced structure is not classified. The result concerns algebra endomorphisms rather than arbitrary linear operators, and does not determine a full presentation of their composition monoid by generators and relations. Potential specialized prior descriptions not indexed in the checked literature remain a residual originality risk. Independent validation has not been performed.

## References

1. L. M. Camacho, J. R. Gómez, B. A. Omirov and R. M. Turdibaev, *Some properties of evolution algebras*, arXiv:1004.1987v1 (2010-04-12).
2. J. M. Casas, M. Ladra, B. A. Omirov and U. A. Rozikov, *On evolution algebras*, arXiv:1004.1050v1 (2010-04-07).
3. J. M. Casas et al., *On nilpotent index and dibaricity of evolution algebras*, arXiv:1208.1709v1 (2012-08-08).
4. A. Elduque and A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685v1 (2013-12-17).
5. A. S. Hegazi and H. Abdelwahab, *Nilpotent Evolution Algebras over arbitrary fields*, arXiv:1508.06860v1 (2015-08-27).
6. F. Mukhamedov, O. Khakimov, B. A. Omirov and I. Qaralleh, *Derivations and automorphisms of nilpotent evolution algebras with maximal nilindex*, arXiv:1805.10285v1 (2018-05-25).
