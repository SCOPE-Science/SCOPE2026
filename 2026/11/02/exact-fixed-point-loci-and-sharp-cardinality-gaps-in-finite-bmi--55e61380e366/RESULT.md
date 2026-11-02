# Exact fixed-point loci and sharp cardinality gaps in finite BMI algebras

## Finding

For any finite nonempty BMI algebra \(S\) with application written by juxtaposition, define the *uniform semantic fixed-point locus*
\[
Y(S)=\{y\in S:\ \forall x\in S,\ yx=x(yx)\}.
\]
The following statements hold.

1. \(Y(S)\) is a nonempty **right-regular subband**: it is closed under application and satisfies \(uvu=vu\) for all \(u,v\in Y(S)\).
2. If \(S\setminus Y(S)\) is nonempty, it contains at least two elements. This is sharp.
3. Every nonempty finite right-regular band \(R\) with a left identity can occur, unchanged as an induced subband, as the exact locus \(Y(S)=R\) of some finite BMI algebra \(S\) of order \(|R|+2\). No proper realization with only one additional element exists.
4. Consequently, writing \(\Sigma_n\) for the possible values of \(|Y(S)|\) among all \(n\)-element BMI algebras (the distinguished combinators are permitted to coincide),
\[
\Sigma_1=\{1\},\qquad \Sigma_2=\{2\},\qquad
\Sigma_n=\{1,2,\ldots,n-2,n\}\quad(n\ge3).
\]
In particular, exactly one missing semantic fixed-point element is impossible, while every other positive cardinality is achievable.

## Assumptions and scope

A BMI algebra is a nonempty set \(S\) with an application operation and distinguished elements \(B,M,I\), obeying
\[
((Bx)y)z=x(yz),\qquad Mx=xx,\qquad Ix=x
\]
for all inputs. The distinguished elements need not be distinct. For *finite* BMI algebras, the band characterization of Imamura (2026, Theorems 3.3--3.4) gives the exact equivalence with an associative idempotent semigroup having \(B,M,I\) as left identities. A *band* is such an associative idempotent semigroup, and a *right-regular band* additionally satisfies \(uvu=vu\) for all its elements. None of the conclusions asserts that a syntactic term in the free BMI system is a fixed-point combinator. The source first publicly submitted September 18, 2026 motivates the semantic question; the explicit finite band characterization first appeared October 27, 2026 and is used with credit.

## Proof

**Reduction and nonemptiness.** By the finite BMI characterization cited above, \(S\) is a band with at least one left identity \(e\). For any left identity \(e\) and any \(x\in S\),
\[
ex=x=x^2=x(ex),
\]
so \(e\in Y(S)\). In particular, the designated \(B,M,I\) belong to \(Y(S)\).

**Closure.** Let \(y,z\in Y(S)\) and let \(x\in S\). Associativity, first the defining equation for \(z\) and then for \(y\), gives
\[
(yz)x=y(zx)=y\bigl(x(zx)\bigr)=(yx)(zx)
=\bigl(x(yx)\bigr)(zx)=x\bigl(y(zx)\bigr)=x\bigl((yz)x\bigr).
\]
Thus \(yz\in Y(S)\). Moreover, since \(z\in Y(S)\), substituting \(x=y\) gives \(zy=y(zy)=yzy\). Hence \(yzy=zy\), the right-regular identity on this subband.

**Symmetric failure and the gap.** For arbitrary \(x,y\in S\), the two equations
\[
yx=xyx\qquad\text{and}\qquad xy=yxy
\]
are equivalent. Indeed, multiply the first on the right by \(y\) and use idempotence of the element \(xy\): \(yxy=xyxy=xy\). Conversely, multiply the second on the right by \(x\) and use idempotence of \(yx\): \(xyx=yxyx=yx\). If \(y\notin Y(S)\), some \(x\in S\) witnesses \(yx\ne xyx\). The equivalent failure \(xy\ne yxy\) makes \(x\notin Y(S)\) as well. Necessarily \(x\ne y\), since each idempotent satisfies its own fixed-point test. Therefore the complement of \(Y(S)\) cannot be a singleton.

**A universal sharp extension.** Let \(R\) be any nonempty right-regular band with left identity \(e\), and let \(U\) be a disjoint set of \(t\ge2\) elements. On \(S=R\sqcup U\) retain the product of \(R\), and set for \(r\in R\) and \(u,v\in U\)
\[
ru=ur=u,\qquad uv=u.
\]
This defines an associative operation: words involving a member of \(U\) evaluate to their **leftmost** such member, while words entirely in \(R\) evaluate by the associative product of \(R\). Every element is idempotent, and \(e\) is a left identity of \(S\). Choosing \(B=M=I=e\) therefore makes \(S\) a BMI algebra by the finite band characterization (or by checking the defining axioms directly).

For \(r\in R\) and \(x\in R\), right-regularity gives \(rx=xrx\); and for \(u\in U\), \(ru=u=u(ru)\). Thus \(R\subseteq Y(S)\). If \(u,v\in U\) are distinct, \(uv=u\ne v=v(uv)\), so \(u\notin Y(S)\). Hence \(Y(S)=R\). With \(t=2\), the gap just proved shows that this proper enlargement is minimum possible.

**Exact cardinality spectrum.** For any \(n\ge3\) and \(1\le k\le n-2\), let \(R\) be the \(k\)-element chain semilattice with product its minimum and left identity the greatest element. Take \(|U|=n-k\ge2\) in the construction above; the resulting BMI algebra has exactly \(k\) Y-elements. For \(k=n\), the \(n\)-element chain semilattice itself has \(Y(S)=S\). The nonemptiness and singleton-complement obstruction exclude all other possibilities. The same argument with \(n=1,2\) gives the stated small cases.

## Verification

The accompanying standalone `checker.py` checks the theorem using literal multiplication tables. It exhaustively generates every labelled band with element zero prescribed as a left identity, for universe sizes \(1\) through \(4\). The counts are respectively \(1,2,9,84\), and the observed fixed-point-locus size spectra are \(\{1\},\{2\},\{1,3\},\{1,2,4\}\). Every tested locus is closed and right-regular; every tested failure is symmetric. It also verifies the chain-semilattice extensions for orders through \(13\), and extends every right-regular unital band on up to four points by the universal two-point construction. The script prints `ALL_CHECKS_OK` on success. These finite tests are ancillary; the preceding algebraic proof handles every finite order and every admissible \(R\).

Reproduce using `python3 checker.py` from the directory containing the file; no third-party modules are required.

## Relationship to prior work

Imamura's earlier paper, *Bluebirds and mockingbirds cannot produce a fixed-point combinator* (first submitted September 18, 2026), concerns failure of a **uniform syntactic term** in the free BMI calculus, not the number of semantic Y-elements in finite models. His *Finite BM-algebras and fixed-point combinators* (October 27, 2026), Section 3, proves that finite BMI algebras are exactly bands with specified left identities and consequently possess at least one Y-element. Both the band reduction and existence are already known; the new contribution here is the characterization of the entire Y-locus as a right-regular subband, the symmetric two-obstruction theorem, the minimal realization of any unital right-regular band and the exact cardinality spectrum. General references on right-regular bands define the identity but do not, in the inspected material, formulate this semantic fixed-point-locus theorem.

The argument does **not** claim an extension to arbitrary finite BM algebras without an I-element: Imamura supplies a nonassociative BM example. Nor does it assert novelty of the right-regular band identity itself.

## Limitations

The result depends on the full BMI axioms and on finiteness for the reduction to bands. The elementary closure/gap/extension lemmas hold for any band with a left identity, even if it is infinite; an arbitrary infinite BMI algebra need not be a band and may have an empty Y-locus. The distinguished constants may coincide in the extremal constructions. Exact historical priority of related semigroup lemmas remains an open bibliographic risk; a semantic similarity search is not proof of uniqueness. The result does not count isomorphism classes of all BMI models at each Y-size, nor does it classify the relative embedding of every possible locus in an arbitrary band.

## References

1. Takuma Imamura, *Bluebirds and mockingbirds cannot produce a fixed-point combinator*, arXiv:2609.21765v1 (first submitted 2026-09-18), https://arxiv.org/abs/2609.21765.
2. Takuma Imamura, *Finite BM-algebras and fixed-point combinators*, arXiv:2610.37108v1 (first submitted 2026-10-27), especially Definition 0.2 and Theorems 3.3--3.4 and Corollary 3.5, https://arxiv.org/html/2610.37108v1.
3. Clemens Berger and Mai Gehrke, *Stone duality for spectral sheaves and the patch monad*, arXiv:2202.00084v2, preliminaries on right-regular bands, https://arxiv.org/abs/2202.00084.
