# Finite-characteristic phase diagram of quadratic four-square polynomial triples

## Finding

A **quadratic four-square triple** over a field \(K\) is an ordered triple \((a,b,c)\) of pairwise distinct degree-two polynomials in \(K[X]\) such that
\[
ab+1,\qquad ac+1,\qquad bc+1,\qquad abc+1
\]
are squares in \(K[X]\). In odd characteristic the center of \(AX^2+BX+C\), where \(A\ne0\), is \(-B/(2A)\).

**Theorem (exceptional characteristics and splitting).** Let \(K\) be a field of characteristic \(p\ge5\).

1. Every quadratic four-square triple over \(K\) has a common center unless \(p=5\) or \(p=13\). Exactly two equal centers cannot occur. Each exceptional characteristic admits an explicit triple with all three centers different, even over its prime field.
2. Put \(G(T)=16T^3+55T^2-64T+16\). For every rational prime \(p\ge17\), every integer \(m\ge1\), and \(K=\mathbb F_{p^m}\), a quadratic four-square triple exists if and only if either \(G\) has a root in \(\mathbb F_p\) or \(3\mid m\).
3. The primes \(p\ge17\) admitting a quadratic four-square triple over \(\mathbb F_p\) have natural density \(1/3\). For the complementary density \(2/3\), the smallest positive extension degree over which such a triple exists is three.

Here natural density means limiting proportion among primes up to \(x\) as \(x\to\infty\).

## Assumptions and scope

All statements about centers require odd characteristic and nonzero quadratic leading coefficients. Statement 1 covers arbitrary fields in characteristic at least five, not only prime fields. The splitting and density statements concern primes at least seventeen and do not assert a corresponding extension-degree classification in characteristics two, three, five, seven, eleven or thirteen. Polynomial square means equality in the polynomial ring, not merely pointwise quadratic residuosity. No positivity or ordering on \(K\) is assumed.

## Proof

**1. A pairwise square lemma.** The leading coefficient of every entry is a square in \(K\): for example, the leading coefficients of \(abc+1\) and \(bc+1\) are squares, and their quotient is the leading coefficient of \(a\). Thus each quadratic can be written \(P^2+\lambda\) for a nonconstant linear \(P\). Write \(f=P^2+\lambda\), \(g=Q^2+\mu\), and let \(Q=uP+v\), with \(u\ne0\). If \(fg+1\) is a square, its square root has the form \(PQ+d\) with \(d\in K\): a nonconstant difference from \(PQ\) would create an uncancellable cubic coefficient, since \(2\ne0\). Comparing coefficients gives two cases.

If \(v\ne0\), then
\[
\lambda=-1/v^2,\qquad \mu=-u^2/v^2,\qquad d=\lambda u.
\]
If \(v=0\), then \(g=t^2 f+2t\) for some \(t\in K^\times\). The latter follows on solving \(d-\lambda u=\pm1\) and writing \(t=\pm u\). The two quadratics have the same center exactly when \(v=0\).

**2. Mixed centers are impossible.** Suppose \(a,b\) have a common center and \(c\) has a different one. By the pair lemma, write \(a=P^2+\lambda\) and \(b=t^2a+2t=(tP)^2+(t^2\lambda+2t)\), where \(t\ne0\). Apply the distinct-center case to the pairs \((a,c)\) and \((b,c)\). Because the change of slope from \(P\) to \(tP\) multiplies the required constant \(\lambda\) by \(t^2\), it forces \(t^2\lambda+2t=t^2\lambda\), hence \(2t=0\), a contradiction. Thus any non-common-center triple must have all three centers different.

**3. The exceptional-characteristic obstruction.** Suppose all centers are different. A common invertible affine change of variable, and independent changes of sign in the linear square roots, put the triple in the form
\[
a=X^2-n^{-2},\quad
b=(uX+n)^2-u^2n^{-2},\quad
c=(vX+n)^2-v^2n^{-2},
\]
where \(n,u,v\in K^\times\). The pair \((b,c)\) satisfies the pair lemma if and only if \((u-v)^2=1\). Set \(S=u+v\) and \(w=uv\), so \(S^2=4w+1\). If \(abc+1\) is a square, matching the four highest coefficients of its degree-six square root, with a choice of positive leading coefficient \(w\), forces that root to be
\[
U=X(uX+n)(vX+n)-\frac{3w}{2n^2}X-\frac S{2n}.
\]
The coefficients of \(X^2\), \(X\), and \(1\) in \(abc+1-U^2\), after using \((u-v)^2=1\), vanish exactly when
\[
3w^2=4n^4(w+1),\qquad S(w-2n^4)=0,
\]
\[
4n^8-4n^6-4n^4w-3n^4+4w^2=0.\tag{1}
\]
If \(S=0\), then \(w=-1/4\). Since \(p\ge5\), the first equation gives \(n^4=1/16\), and so \(n^2=\pm1/4\). The last equation becomes \(5/64=0\) or \(13/64=0\), which requires \(p=5\) or \(p=13\). If \(S\ne0\), the middle equation gives \(w=2n^4\). The first then forces \(n^4=1\), so \(n^2=\pm1\). The last equation becomes \(9-4n^2=0\), again requiring \(p=5\) or \(p=13\). This proves the obstruction uniformly over all fields of characteristic at least five.

Both exceptions are realized by the following explicit polynomial identities; coefficients are reduced in the indicated fields. Over \(\mathbb F_5\), take
\[
(a,b,c)=(X^2+4,\ X^2+3X,\ 4X^2+X+2).
\]
Then the four square roots, ordered as \(ab+1,ac+1,bc+1,abc+1\), are
\[
(4X^2+X+1,\ 3X^2+X+2,\ 2X^2+2X+4,\ 2X^3+2X^2+3X+4).
\]
Over \(\mathbb F_{13}\), take
\[
(a,b,c)=(X^2+4,\ 10X^2+4X+4,\ 10X^2+9X+4),
\]
with corresponding roots
\[
(7X^2+4X+2,\ 6X^2+4X+11,\ 3X^2+2,\ 3X^3+8X).
\]
Direct multiplication confirms all eight square identities, and calculating \(-B/(2A)\) shows three distinct centers in each field. The standalone exact-arithmetic checker reproduces these identities.

**4. The common-center parameter.** Now assume \(p\ge17\). The preceding argument forces all three centers equal. After an affine change of \(X\), write \(a=X^2+\lambda\). Applying the same-center part of the pair lemma to \((a,b)\) and \((a,c)\) gives
\[
b=P^2a+2P,\qquad c=Q^2a+2Q,
\]
where \(P,Q\in K^\times\) are distinct. The condition that \(bc+1\) be a square is \((P-Q)^2=1\). Reorder \(b,c\) if necessary to arrange \(P-Q=1\). Put \(\pi=PQ\), \(\sigma=P+Q\). Since \(abc+1\) is an even degree-six polynomial in \(X\), its square root is odd (any polynomial square with even exponents and odd characteristic has root either even or odd); hence its square root can be written
\[
X(\pi a+k)
\]
for some \(k\in K\), after choosing the leading sign. Comparing coefficients in the polynomial identity
\[
\pi^2a^3+2\pi\sigma a^2+4\pi a+1=(a-\lambda)(\pi a+k)^2
\]
gives
\[
\lambda=-k^{-2},\quad
\pi=\frac{k^3}{2(2k-1)},\quad
\sigma=\frac{k(8k-3)}{4(2k-1)}.
\]
Here \(k\ne0\) and \(2k-1\ne0\) are forced by the equations. The identity \((P-Q)^2=\sigma^2-4\pi=1\) is exactly
\[
\sigma^2-4\pi-1=-\frac{G(k)}{16(2k-1)^2}=0,
\qquad G(T)=16T^3+55T^2-64T+16.
\]
Conversely, any root \(k\in K\) of \(G\) is nonzero and satisfies \(2k-1\ne0\), since \(G(0)=16\) and \(G(1/2)=-1/4\) in odd characteristic at least seventeen. Define \(\pi,\sigma\) by the displayed formulas and \(P=(\sigma+1)/2\), \(Q=(\sigma-1)/2\). Then \(P-Q=1\), \(PQ=\pi\ne0\). Take
\[
a=X^2-k^{-2},\quad b=P^2a+2P,\quad c=Q^2a+2Q.
\]
The four polynomial square roots are explicitly
\[
Pa+1,\qquad Qa+1,\qquad P Qa+P+Q,\qquad X(PQa+k).
\]
This proves that for any field of characteristic at least seventeen a triple exists **if and only if** \(G\) has a root in the field. The entries all have degree two and are pairwise distinct, because \(P,Q,P-Q\) are nonzero and the respective nonconstant and constant coefficients preclude equality.

**5. Arithmetic splitting and density.** The integer cubic \(G\) has discriminant
\[
\operatorname{disc}(G)=529984=728^2,
\]
and modulo three its values at \(0,1,2\) are \(1,2,2\). Thus it is irreducible over \(\mathbb Q\) and its Galois group is the transitive subgroup \(A_3\), cyclic of order three. Every prime \(p\ge17\) is unramified for the corresponding splitting field and gives a separable reduction of \(G\). Frobenius in this cyclic cubic group is either the identity (so \(G\) splits into three linear factors over \(\mathbb F_p\)) or a three-cycle (so \(G\) is irreducible over \(\mathbb F_p\)). In the latter case its roots belong to \(\mathbb F_{p^m}\) exactly when \(3\mid m\). The common-center criterion then proves statement 2. By the Chebotarev density theorem, the identity conjugacy class in the cyclic cubic extension has density \(1/3\), while the two nonidentity classes have total density \(2/3\). Removing finitely many small primes does not affect natural density, proving statement 3.

## Verification

The standalone file `verify.py` uses only Python's standard library. Execute `python verify.py` in a directory containing that file. It checks the two explicit exceptional triples and distinct centers; computes the integer cubic discriminant and the no-root statement modulo three; exhaustively checks the reduction \(G\) for the 103 primes between seventeen and six hundred, confirming zero or three distinct roots; and verifies all four square identities in each of the 99 resulting root-parametrized triples (396 identities). It prints `VERIFY_OK` on success. The finite checks do not replace the coefficient-comparison proofs, the finite-field Frobenius argument, or Chebotarev.

## Relationship to prior work

Jukić Bokun and Jurasić, *Four-square polynomial triples: quadratic classification and equal-degree obstructions* (arXiv:2610.05565v1, publicly submitted October 4, 2026), give the characteristic-zero quadratic classification and its real/rational consequences. Their work does not assert a finite-characteristic phase diagram, prime-field existence density, or exceptional non-common-center examples. The current result uses the same motivating four-square property but derives a field-valid pair lemma and analyzes reduction, including the additional characteristic-thirteen branch where a square of a field element may equal the negative of another square. Jurasić's earlier real construction is context; finite-field Diophantine tuple results counting sets of field elements concern different objects, not polynomial triples. A prior mathematical note already identifies the same cubic as a cyclic cubic field, determines its field discriminant as \(91^2\), and gives an explicit Galois generator. That cyclicity, and the generic Chebotarev density of splitting primes which follows from it, are acknowledged as covered antecedents. The new contribution is the all-good-prime equivalence between polynomial triple existence and splitting, alongside the sharp characteristic-five/thirteen center exceptions. The splitting theorem is an application of classical discriminant, Frobenius and Chebotarev facts, not independently claimed as new.

## Limitations

The theorem does not classify quadratic triples up to affine equivalence within each finite characteristic, does not address characteristic two or three, and gives no extension-degree statement for the excluded small odd primes. Prime-density assertions rely on the standard unconditional Chebotarev theorem. Literature searches cannot rule out an implicit earlier specialization of classical polynomial-Diophantine or Chebotarev constructions. No independent audit has been performed.

## References

1. Mirela Jukić Bokun and Ana Jurasić, *Four-square polynomial triples: quadratic classification and equal-degree obstructions*, arXiv:2610.05565v1 (2026-10-04), https://arxiv.org/abs/2610.05565 .
2. Ana Jurasić, real four-square polynomial-triple construction, arXiv:2607.06586v1 (2026), https://arxiv.org/abs/2607.06586 .
3. Seoyoung Kim, Chi Hoi Yip, and Semin Yoo, *Explicit constructions of Diophantine tuples over finite fields* (2024), cited for a contrasting scalar-tuple setting, not for polynomial triples.
4. Classical discriminant criterion for cubics, finite-field Frobenius factorization, and the Chebotarev density theorem.
