# Rigidity of finite cutoff sumset monoids

## Finding

For every integer \(n\ge 1\), define
\[
\mathcal T_n=\{A\subseteq\{0,1,\ldots,n\}:0\in A\},\qquad
A\star_n B=(A+B)\cap\{0,1,\ldots,n\},
\]
where \(A+B=\{a+b:a\in A,\ b\in B\}\). Then
\[
\boxed{\operatorname{Aut}(\mathcal T_n,\star_n)=\{\operatorname{id}\}\quad\text{for every }n\ge1.}
\]
The finite monoid has \(2^n\) elements and is a quotient of the reduced finitary power monoid of the nonnegative integers by truncation at \(n\). The theorem gives a full automorphism classification for every cutoff, not merely a finite census.

## Assumptions and scope

All sums are ordinary integer sums, not addition modulo \(n+1\). The symbol \(A\star_n B\) denotes **discarding** sums exceeding \(n\); it does not mean reducing them modulo \(n+1\). Each set contains zero, so \(\{0\}\) is the identity. This operation is associative: once a nonnegative sum exceeds \(n\), adding another nonnegative integer cannot bring it back below the cutoff.

For \(A\in\mathcal T_n\), define the intrinsic right-multiplication image size
\[
r_n(A)=|\{A\star_n B:B\in\mathcal T_n\}|.
\]
A monoid automorphism preserves \(r_n(A)\) and idempotency. Write \(u_n=\{0,n\}\).

## Proof

**Lemma 1 (terminal element is intrinsic).** For \(n\ge4\), \(u_n\) is the unique nonidentity element having \(r_n(A)=2^{n-1}\). For \(n=2,3\), it is the unique nonidentity *idempotent* having \(r_n(A)=2^{n-1}\).

*Proof.* Because every \(B\) contains zero, each product \(A\star_n B\) contains \(A\). If \(|A\setminus\{0\}|\ge2\), at most \(2^{n-2}\) products are possible. Also,
\[
u_n\star_n B=B\cup\{n\},
\]
so its image is all \(2^{n-1}\) sets containing \(n\).

It remains to examine \(A=\{0,k\}\), with \(1\le k<n\). Every product contains \(k\), and hence \(r_n(A)\le2^{n-1}\). For \(2\le k<n\), the set \(\{0,1,k\}\) is not a product: producing \(1\) requires \(1\in B\), which would also produce \(k+1\le n\). Therefore \(r_n(A)<2^{n-1}\). For \(k=1\) and \(n\ge4\), the set \(\{0,1,3\}\) is impossible: producing \(3\) requires either \(3\in B\), which also produces \(4\), or \(2\in B\), which also produces \(2\). Thus \(r_n(\{0,1\})<2^{n-1}\) when \(n\ge4\).

For \(n=2,3\), the only possible competing singleton at image size \(2^{n-1}\) is \(\{0,1\}\), which is not idempotent because its square contains \(2\). The other multi-positive elements have smaller image sizes. More explicitly, \(r_2(\{0,1\})=2\), \(r_2(\{0,2\})=2\); and \(r_3(\{0,1\})=4\), \(r_3(\{0,2\})=3\), \(r_3(\{0,3\})=4\). This proves the lemma. \(\square\)

**Lemma 2 (characteristic terminal ideal).** The principal ideal \(u_n\star_n\mathcal T_n\) consists of every member of \(\mathcal T_n\) containing \(n\). Under the bijection
\[
A\longmapsto A\setminus\{n\},
\]
it is isomorphic, as a monoid with identity \(u_n\), to \(\mathcal T_{n-1}\) for \(n\ge2\).

*Proof.* The formula \(u_n\star_n B=B\cup\{n\}\) gives the first assertion. For members containing \(n\), every positive sum involving that \(n\) is discarded, so deletion of \(n\) commutes with the respective products, leaving exactly cutoff multiplication at \(n-1\). \(\square\)

**Induction.** The monoid \(\mathcal T_1=\{\{0\},\{0,1\}\}\) has no nontrivial automorphism. Suppose \(n\ge2\) and the result is known for \(n-1\). An automorphism \(f\) of \(\mathcal T_n\) fixes \(u_n\) by Lemma 1, and hence preserves the principal ideal \(u_n\star_n\mathcal T_n\). Lemma 2 and the induction hypothesis imply that \(f\) fixes **every** set containing \(n\). For an arbitrary \(A\in\mathcal T_n\),
\[
f(A)\cup\{n\}=f(A)\star_n u_n=f(A\star_n u_n)=A\cup\{n\}.
\]
If \(n\notin A\), the only possibilities are \(f(A)=A\) and \(f(A)=A\cup\{n\}\). The latter is impossible because \(A\cup\{n\}\) is already fixed and \(f\) is injective. Therefore every \(A\) is fixed. This finishes the induction. \(\square\)

## Verification

The standalone file `verify.py`, runnable with `python verify.py` and requiring only the standard library, implements cutoff sumset multiplication in two independent ways: integer bit masks and explicit set sums. For every \(1\le n\le8\), it calculates the multiplication-image sizes of **all** \(2^n\) elements, checks the intrinsic characterization of \(u_n\), and verifies the terminal-ideal quotient. For \(n\le3\), it also enumerates all identity-preserving permutations and directly confirms that precisely one is an automorphism. Associativity is checked for every triple when \(n\le4\). The executed checker returned `VERIFY_OK`.

These finite computations are corroboration only. The all-cutoff statement is proved by Lemmas 1 and 2 and induction, without an appeal to unbounded computation.

## Relationship to prior work

Bhowmik and Tringali (arXiv:2607.23301, first public 2026-07-25) classify automorphisms of reduced finitary power monoids of numerical monoids. Their result includes the familiar nontrivial reversion automorphism of the **untruncated** reduced monoid over \(\mathbb N\). Wen, He and Liu (arXiv:2608.27292) study convolution realizations and rigidity for the same class of untruncated monoids. Tringali and Yan (arXiv:2312.04439) originally prove the two-element automorphism group of the untruncated reduced monoid. Rago (arXiv:2510.17533) treats power monoids of finite abelian **groups**. None of these statements determines the automorphism group of the cutoff operation \((A+B)\cap[0,n]\): truncation differs both from unrestricted sumsets and from modular addition in a cyclic group.

The distinction is structural. The untruncated reversion \(A\mapsto\max(A)-A\) does not descend to any \(\mathcal T_n\): for \(X=\{0,1\}\) and \(Y=\{0,1,n+2\}\), both have the same truncation \(\{0,1\}\), but their reversions truncate to \(\{0,1\}\) and \(\{0\}\), respectively. The theorem proves that every finite cutoff nevertheless is rigid.

## Limitations

The theorem concerns the specified cutoff monoids, not arbitrary finite quotients of reduced power monoids, Boolean polynomial **semiring** automorphisms, or reduced power monoids of cyclic groups. It does not classify all endomorphisms or automorphisms of the infinite monoid. The literature comparison did not identify an equivalent finite-cutoff theorem, but unpublished or differently described results about Boolean Toeplitz matrix monoids or finite convolution quotients remain a historical-priority risk. No independent review has been performed.

## References

1. A. Bhowmik and S. Tringali, *On the automorphisms of numerical power monoids*, arXiv:2607.23301 (first posted 2026-07-25), https://arxiv.org/abs/2607.23301.
2. H. Wen, J. He and Y.-Z. Liu, *Kleisli convolution representations of power monoids*, arXiv:2608.27292 (first posted 2026-08-27), https://arxiv.org/abs/2608.27292.
3. S. Tringali and W. Yan, *On power monoids and their automorphisms*, arXiv:2312.04439 (first posted 2023-12-07), https://arxiv.org/abs/2312.04439.
4. B. Rago, *The automorphism group of reduced power monoids of finite abelian groups*, arXiv:2510.17533 (first posted 2025-10-20), https://arxiv.org/abs/2510.17533.
5. D. Wong, S. Xu, C. Zhang and J. Zhao, *On automorphism groups of power semigroups over numerical semigroups or over numerical monoids*, arXiv:2512.12606 (first posted 2025-12-14), https://arxiv.org/abs/2512.12606.
6. S. Tringali and K. Wen, *On the automorphisms of the power semigroups of a numerical semigroup*, *Transactions of the London Mathematical Society* 13 (2026), e70030, https://doi.org/10.1112/tlm3.70030.
