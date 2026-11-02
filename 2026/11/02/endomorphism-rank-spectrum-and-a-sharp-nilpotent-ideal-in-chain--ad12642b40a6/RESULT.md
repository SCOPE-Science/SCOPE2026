# Endomorphism rank spectrum and a sharp nilpotent ideal in chain evolution algebras

## Finding

For every integer \(n\ge2\) and finite field \(K=\mathbb F_q\), let \(E_n(K)\) be the evolution algebra with basis \(e_1,\ldots,e_n\) and multiplication \(e_i e_j=0\) for \(i\ne j\), \(e_i^2=e_{i+1}\) for \(1\le i<n\), and \(e_n^2=0\). This is the standard unweighted chain model in the literature on maximal-nilindex evolution algebras.

Every \(K\)-linear algebra endomorphism is uniquely one of the following maps (the images on all other basis vectors are prescribed by the squaring rule):

* \(Z_b\), for \(b\in K\): \(Z_b(e_1)=b e_n\), and \(Z_b(e_r)=0\) for \(2\le r\le n\).
* \(F_{j,a,b}\), for \(1\le j<n\), \(a\in K^\times\), and \(b\in K\):
  \[
  F_{j,a,b}(e_1)=a e_j+b e_n,\qquad
  F_{j,a,b}(e_r)=\begin{cases}a^{2^{r-1}}e_{j+r-1},&2\le r\le n-j+1,\\0,&n-j+2\le r\le n.\end{cases}
  \]
  The second range may be empty. For \(r=1\), the displayed first formula takes precedence, including the parameter \(b\).

Let \(R_{n,q}(z)=\sum_{f\in\operatorname{End}_K(E_n(K))}z^{\operatorname{rank}_K f}\). Then
\[
\boxed{R_{n,q}(z)=1+(q-1)z+q(q-1)\sum_{r=2}^{n}z^r.}
\]
In particular, \(\lvert\operatorname{End}_K(E_n(K))\rvert=q[1+(n-1)(q-1)]\), and \(\lvert\operatorname{Aut}_K(E_n(K))\rvert=q(q-1)\).

Under composition, the set \(I\) of nonautomorphisms, together with the zero endomorphism, is a two-sided nilpotent ideal with **sharp nilpotency index** \(n\): \(I^n=\{0\}\) while \(I^{n-1}\ne\{0\}\). The only idempotent endomorphisms are \(0\) and \(1\). The regular elements of the endomorphism monoid (those \(f\) for which some \(g\) satisfies \(fgf=f\)) are exactly \(0\) and the automorphisms.

## Assumptions and scope

The field is any finite field \(\mathbb F_q\) (all characteristics, including two). Endomorphisms are \(K\)-linear multiplication-preserving maps of this nonunital, commutative, generally nonassociative algebra. The theorem covers exactly the displayed chain multiplication table for every \(n\ge2\); it does not assert the same formulas for arbitrary weighted or branched evolution algebras.

The rank is the dimension of the linear image. Products of endomorphisms mean functional composition. If \(J\) is a subset of the endomorphism monoid, \(J^k\) denotes the set of all products of \(k\) members of \(J\); this is a semigroup nilpotency assertion, not an assertion of additive-ring structure.

## Proof

**1. A single generator image and its iterated squares.** For every endomorphism \(f\), put \(f(e_1)=\sum_{j=1}^{n}a_j e_j\). The defining identities recursively force \(f(e_{r+1})=f(e_r)^2\). Since mixed basis products vanish, repeated squaring gives, for every \(1\le r\le n\),
\[
 f(e_r)=\sum_{j=1}^{n-r+1}a_j^{2^{r-1}}e_{j+r-1}.
\]
For \(r=n\), this is just \(a_1^{2^{n-1}}e_n\). The expression automatically respects all prescribed basis squares, including the zero square of \(e_n\).

**2. Cross-product rigidity.** The relations \(e_1e_{d+1}=0\), with \(1\le d\le n-2\), imply
\[
 0=f(e_1)f(e_{d+1})=\sum_{k=d+1}^{n-1}a_k a_{k-d}^{2^d}e_{k+1}.
\]
Each basis coefficient vanishes separately. If two coefficients \(a_i\), \(a_j\) with \(1\le i<j<n\) were nonzero, taking \(d=j-i\) would force \(a_j a_i^{2^d}=0\), a contradiction in a field. Thus at most one among \(a_1,\ldots,a_{n-1}\) is nonzero; \(a_n\) remains unrestricted.

Conversely, if all of \(a_1,\ldots,a_{n-1}\) vanish, the resulting map is \(Z_b\). Otherwise there are unique \(j<n\), \(a\in K^\times\) and \(b\in K\) with \(f(e_1)=a e_j+b e_n\). The iterated-square formula gives the stated \(F_{j,a,b}\). In these maps the possible nonzero components of distinct \(f(e_r)\) occur in distinct basis positions, apart from the annihilating \(e_n\) component of \(f(e_1)\). Hence all mixed products \(f(e_r)f(e_s)\) for \(r\ne s\) vanish. The displayed formulas are therefore sufficient for multiplicativity. Every permitted parameter tuple yields one endomorphism, and uniqueness follows from the image of \(e_1\).

**3. Exact ranks and cardinalities.** The zero map is \(Z_0\), and every \(Z_b\) with \(b\ne0\) has rank one. For fixed \(j<n\), the images of \(e_1,\ldots,e_{n-j+1}\) are linearly independent: their first possible nonzero coordinates are \(j,j+1,\ldots,n\), respectively, each with a nonzero coefficient. All later images vanish, so \(\operatorname{rank}F_{j,a,b}=n-j+1\). Thus each rank from two through \(n\) has exactly \(q(q-1)\) representatives; this establishes the polynomial and total. Precisely the rank-\(n\) maps (\(j=1\)) are automorphisms.

**4. The sharp nilpotent ideal.** Let \(V_r=\operatorname{span}_K\{e_r,\ldots,e_n\}\) and \(V_{n+1}=0\). Every nonunit is either \(Z_b\) or \(F_{j,a,b}\) with \(j\ge2\). The explicit formulas give \(f(V_r)\subseteq V_{r+1}\) for all \(1\le r\le n\). The nonunits form a two-sided ideal in the endomorphism monoid: a composition containing a noninvertible linear map is again noninvertible. Every composition of \(n\) nonunits maps \(V_1\) into \(V_{n+1}=0\), so \(I^n=\{0\}\). The shift \(T(e_r)=e_{r+1}\) for \(r<n\), \(T(e_n)=0\), is itself a nonunit endomorphism: it equals \(Z_1\) when \(n=2\), and \(F_{2,1,0}\) when \(n\ge3\). Its \((n-1)\)-st power is nonzero, as \(T^{n-1}(e_1)=e_n\). Hence the index is exactly \(n\).

**5. Idempotents and regularity.** If a nonunit \(f\) is idempotent, then \(f=f^n=0\) by the ideal nilpotency. A unit satisfying \(f^2=f\) is the identity. Thus the idempotents are exactly \(0\) and \(1\). If \(fgf=f\), then \(h=fg\) is an idempotent, since \(h^2=(fgf)g=fg=h\). If \(h=0\), then \(f=fgf=0\). If \(h=1\), then \(f\) has a right inverse as a linear map of a finite-dimensional vector space and hence is an automorphism. Conversely zero and all units are regular. This completes the proof.

## Verification

The self-contained accompanying program `verify.py` enumerates all \(q^n\) candidate first-column images, derives the remaining images using actual finite-field squaring, independently tests every mixed basis product, and computes ranks by finite-field Gaussian elimination. It checks the rank polynomial, number of maps, normal-form restriction, and actual composition idempotents in 19 configurations: prime fields of orders two, three and five, and the nonprime field of order four; the tested dimensions range from two through eight depending on field size. The program returns `VERIFY_OK`. These finite checks supplement and do not replace the unrestricted proof above.

## Relationship to prior work

The chain basis and maximal-nilindex setting are classical. Mukhamedov, Khakimov, Omirov and Qaralleh (2018), especially Sections 2 and 5, classify derivations and automorphisms of maximal-nilindex evolution algebras in characteristic zero; their automorphism theorem is prior structural work, not part of the novelty claim here. The 2020 classification paper studies invariants, associative enveloping algebras, and extension of derivations. The present claim instead gives the full **finite-field endomorphism monoid**, including singular maps, with its complete rank multiplicities, sharp nilpotent nonunit ideal, and regular-element spectrum.

The 2018 preprint's Section 2 was inspected in full-text HTML for its canonical chain reduction and Section 5 for its automorphism scope. The 2020 journal paper was inspected through its complete 16-page open-access PDF, including its Sections 3–7 on classification, associative enveloping algebras, derivations, and derivation extensions; these sections do not claim the complete endomorphism rank distribution or the sharp nonunit ideal theorem. Broader online searches for maximal-nilindex evolution-algebra endomorphism monoids did not locate a statement equivalent to the combined normal form and nilpotent ideal result, but this is not a proof of novelty.

## Limitations

The proof is self-contained for the specified chain algebra and does not extend automatically to all maximal-nilindex structural matrices. An earlier result using terminology such as endomorphism monoids of monogenic or chain-type evolution algebras may exist. The related 2020 article was read in full; a possible equivalent result under other terminology in other older literature remains a residual originality risk. The finite computational tests do not certify any infinite quantifier; the proof supplies those quantifiers. No independent external mathematical audit has been conducted.

## References

1. F. Mukhamedov, O. Khakimov, B. Omirov, I. Qaralleh, *Derivations and automorphisms of nilpotent evolution algebras with maximal nilindex*, arXiv:1805.10285, first posted 25 May 2018; https://arxiv.org/abs/1805.10285 .
2. F. Mukhamedov, O. Khakimov, I. Qaralleh, *Classification of nilpotent evolution algebras and extensions of their derivations*, Communications in Algebra 48 (2020), 4155–4169; https://doi.org/10.1080/00927872.2020.1757688 .
3. J. M. Casas, M. Ladra, B. A. Omirov, U. A. Rozikov, *On nilpotent index and dibaricity of evolution algebras*, arXiv:1208.1709, first posted 8 August 2012; https://arxiv.org/abs/1208.1709 .
