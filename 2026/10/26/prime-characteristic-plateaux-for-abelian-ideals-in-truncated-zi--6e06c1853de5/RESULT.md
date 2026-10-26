# Prime-characteristic plateaux for abelian ideals in truncated Zinbiel algebras

## Finding

Let \(K\) be any field of characteristic \(p>0\), where \(p\) is prime. On the \(n\)-dimensional \(K\)-vector space with basis \(e_1,\ldots,e_n\), define the truncated half-shuffle Zinbiel product
\[
e_i\circ e_j = \begin{cases}\binom{i+j-1}{j}e_{i+j},&i+j\le n,\\0,&i+j>n.\end{cases}
\]
Call this algebra \(Z_n(K)\), and let \(\beta(Z_n(K))\) denote the largest dimension of a two-sided ideal \(J\) with \(J\circ J=0\).

**Theorem.** For every integer \(k\ge0\), put \(P=p^k\), and let \(n\) be any integer satisfying
\[
\bigl(p+\lceil p/2\rceil\bigr)P\le n\le (2p-1)P.
\]
Then
\[
\beta(Z_n(K))=pP=p^{k+1}.
\]
Moreover, the unique abelian ideal of this maximal dimension is
\[
J=\operatorname{span}_K\{e_{n-pP+1},\ldots,e_n\}.
\]
In particular, in characteristic \(2\), the algebra of dimension \(3\cdot2^k\) has a unique maximal abelian ideal of dimension \(2^{k+1}\). This is an exact infinite sequence of characteristic-dependent deviations from the complex null-filiform formula \(\beta(Z_n(\mathbb C))=n-\lfloor n/2\rfloor\).

## Assumptions and scope

The prime \(p\) may be \(2\). The field \(K\) need not be finite or algebraically closed; only its characteristic matters. The integer \(k\) is any nonnegative integer; \(P\) is a positive integral power of \(p\). The theorem covers exactly the displayed family of intervals in \(n\), not all dimensions. An **abelian ideal** here means a two-sided ideal with identically zero internal multiplication; the result is about \(\beta\), not the maximal dimension \(\alpha\) of an arbitrary abelian subalgebra.

The multiplication is well-defined over any \(K\) by reducing integer binomial coefficients modulo \(p\). It satisfies the Zinbiel identity \((x\circ y)\circ z=x\circ(y\circ z)+x\circ(z\circ y)\), by the elementary integer identity
\[
\binom{i+j-1}{j}\binom{i+j+\ell-1}{\ell}
=\left(\binom{j+\ell-1}{\ell}+\binom{j+\ell-1}{j}\right)\binom{i+j+\ell-1}{j+\ell}.
\]
The truncated versions also satisfy the identity, because each term has total degree \(i+j+\ell\).

## Proof

**1. Every two-sided ideal is a suffix space.** For \(1\le r\le n\) set \(I_r=\operatorname{span}_K\{e_r,\ldots,e_n\}\). Every \(I_r\) is a two-sided ideal, since a nonzero product of basis elements has index equal to the sum of their indices. Conversely, left multiplication by \(e_1\) obeys \(e_1\circ e_j=e_{j+1}\) for \(j<n\), and sends \(e_n\) to zero. It is therefore a single nilpotent Jordan shift. A nonzero ideal \(I\) is invariant under this shift. Choose the least \(r\) appearing as the first nonzero coordinate of an element of \(I\), and let \(v\in I\) have first nonzero coordinate \(r\). The \(n-r+1\) vectors \(v,L(v),\ldots,L^{n-r}(v)\), where \(L(x)=e_1\circ x\), are linearly independent and belong to \(I_r\). Since \(I\subseteq I_r\), equality holds. Thus all nonzero ideals form the chain \(I_1\supset I_2\supset\cdots\supset I_n\), with \(\dim I_r=n-r+1\).

**2. A square-zero suffix of dimension \(pP\).** Let \(a=\lceil p/2\rceil\) and \(r=n-pP+1\). The interval assumptions yield \(aP\le r-1\le(p-1)P\). Suppose \(i,j\ge r\) and \(i+j\le n\). Then
\[
aP\le i-1<pP,\qquad aP<j<pP.
\]
In their base-\(p\) expansions, the coefficients at the \(P=p^k\) digit of \(i-1\) and \(j\) are therefore both at least \(a\). Since \(2a\ge p\), adding \(i-1\) and \(j\) has a carry at that digit. The standard Lucas binomial criterion gives
\[
\binom{i+j-1}{j}\equiv0\pmod p.
\]
Every product of two elements of \(I_r\) vanishes. Hence \(I_r\circ I_r=0\) and \(\dim I_r=n-r+1=pP\).

**3. Sharpness and uniqueness.** The preceding suffix \(I_{r-1}\) contains \(e_{r-1}\) and \(e_{pP}\), because \(r-1=n-pP\le(p-1)P<pP\le n\). Their product has total degree \(n\):
\[
e_{r-1}\circ e_{pP}=\binom{n-1}{pP}e_n.
\]
Write \(n-1=pP+s\) with \(0\le s<pP\). Lucas's theorem, or the coefficient of \(T^{pP}\) in \((1+T)^{pP+s}\equiv(1+T^{pP})(1+T)^s\pmod p\), shows \(\binom{n-1}{pP}\equiv1\pmod p\). Thus \(I_{r-1}\) is not abelian. Every larger ideal contains it, and every smaller ideal is contained in \(I_r\). The chain classification proves both the maximality and uniqueness of \(I_r\).

## Verification

The accompanying standalone `verify.py` uses integer binomial coefficients and independent base-\(p\) carry tests. It checks the Zinbiel identity and carry criterion for all ordered basis triples or pairs of total degree at most \(13\) for primes \(2,3,5,7,11\). It also exhaustively enumerates square-zero conditions for all suffix ideals on \(40\) admissible parameter triples with dimension up to \(96\). All checks passed. Illustrative values are \((p,k,n,\beta)=(2,3,24,16),(3,1,15,9),(5,1,40,25),(7,1,77,49)\). These finite checks are not the general proof, which is the digit-carry argument above.

## Relationship to prior work

Ceballos and Towers, *Abelian subalgebras and ideals of maximal dimension in Zinbiel algebras* (arXiv:2202.03214, 2022), Proposition 4.2, prove for **complex** null-filiform Zinbiel algebras that \(\alpha=\beta=n-\lfloor n/2\rfloor\) and identify a unique maximal abelian ideal. They use the same binomial multiplication table. Their complex-field conclusion does not extend by reduction of coefficients to characteristic \(p\): Lucas carries make additional products vanish. The present theorem gives sharp positive-characteristic intervals where the maximal abelian ideal is larger, with an explicit different suffix location. Towers, *Zinbiel algebras are nilpotent* (arXiv:2202.12026, 2022), proves nilpotence over arbitrary fields, but does not determine this invariant.

## Limitations

No formula is asserted for arbitrary dimensions outside the stated intervals, nor for the largest abelian subalgebra not required to be an ideal. The theorem is a field-characteristic statement about this explicit half-shuffle family, not a classification of all null-filiform Zinbiel algebras in positive characteristic. Closely related unindexed modular adaptations of the complex invariant remain a possible priority risk; the mathematical proof itself does not depend on priority.

## References

1. M. Ceballos and D. A. Towers, *Abelian subalgebras and ideals of maximal dimension in Zinbiel algebras*, arXiv:2202.03214v2 (2022), Proposition 4.2, https://arxiv.org/abs/2202.03214 . First preprint submitted February 7, 2022.
2. D. A. Towers, *Zinbiel algebras are nilpotent*, arXiv:2202.12026v1 (2022), https://arxiv.org/abs/2202.12026 .
3. M. Ceballos, J. Núñez, and A. F. Tenorio, *Finite-dimensional Zinbiel algebras and combinatorial structures*, An. Ştiinţ. Univ. Ovidius Constanţa Ser. Mat. 30 (2022), 67–96, https://doi.org/10.2478/auom-2022-0035 .
