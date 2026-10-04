# Exact fibers of idempotent–nilpotent factorizations in two dimensions
## Finding
Let \(q\) be a prime power and let \(A\in M_2(\mathbb F_q)\). Define
\[
\nu_{IN}(A)=\#\{(E,N):E^2=E,\ N\text{ nilpotent},\ EN=A\}
\]
and define \(\nu_{NI}(A)\) analogously by \(NE=A\). Then \(\nu_{IN}(A)=\nu_{NI}(A)\), and the common value is
\[
\nu(A)=
\begin{cases}
q^3+2q^2+1,&A=0,\\
q+1,&A\ne0\text{ and }A\text{ is nilpotent},\\
q-1,&\det A=0\text{ and }\operatorname{tr}A\ne0,\\
0,&\det A\ne0.
\end{cases}
\]
Thus every singular \(2\times2\) matrix over \(\mathbb F_q\) is both an idempotent–nilpotent product and a nilpotent–idempotent product, but the factorization map is not fiber-uniform: nonzero nilpotents have two more ordered factorizations than the nonnilpotent rank-one matrices.

## Assumptions and scope
The field is an arbitrary finite field \(\mathbb F_q\), with no restriction on the characteristic. Idempotents and nilpotents are taken in \(M_2(\mathbb F_q)\), and ordered pairs of factors are counted. The result concerns one idempotent and one nilpotent factor; it does not count longer alternating products or identify factorizations modulo conjugation.

The motivating recent result of Dolžan proves, for finite commutative local principal rings, that the IN- and NI-classes in \(M_2(R)\) coincide and gives their total cardinality. In the field specialization, that cardinality equals the number of singular matrices. The present result refines that image-size statement by determining every fiber of the two factorization maps.

## Proof
Write \(V=\mathbb F_q^2\). A nonzero nilpotent endomorphism of \(V\) has rank one and satisfies \(\operatorname{im}N=\ker N\), which is a line. Hence there are \((q+1)(q-1)=q^2-1\) nonzero nilpotents: choose the common line \(K\), then choose a nonzero map \(V/K\to K\). Including zero gives exactly \(q^2\) nilpotent matrices.

A nontrivial idempotent has rank one and is the projection onto a line \(L\) along a distinct line \(K\). Therefore there are \((q+1)q\) nontrivial idempotents, one for each ordered pair \((L,K)\) of distinct lines.

Assume first that \(A\ne0\) and \(A=EN\). Since \(N\) is singular, \(A\) is singular. If \(E=I\), then \(N=A\), so this contributes exactly one factorization when \(A\) is nilpotent and none otherwise. If \(E\) is nontrivial, then
\[
\operatorname{im}A\subseteq\operatorname{im}E.
\]
Both spaces are one-dimensional, so \(\operatorname{im}E=L:=\operatorname{im}A\). Thus the possible nontrivial idempotents are indexed by the \(q\) complement lines \(K\) of \(L\).

Fix such a complement and choose a basis \((u,v)\) with \(u\) spanning \(L\) and \(v\) spanning \(K\). In this basis
\[
E=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
A=\begin{pmatrix}t&s\\0&0\end{pmatrix},
\]
where \(t=\operatorname{tr}A\). Every solution of \(EN=A\) has the form
\[
N=\begin{pmatrix}t&s\\x&y\end{pmatrix}.
\]
For a \(2\times2\) matrix over a field, nilpotency is equivalent to zero trace and zero determinant. Therefore \(N\) is nilpotent exactly when
\[
y=-t,\qquad sx=-t^2.
\]
If \(t=0\), then \(A\ne0\) forces \(s\ne0\) for every complement \(K\), so there is exactly one value \(x=0\) for each of the \(q\) nontrivial idempotents. Together with \(E=I\), this gives \(q+1\) factorizations.

If \(t\ne0\), then exactly one complement has \(s=0\), namely \(K=\ker A\); for this complement the equation \(sx=-t^2\) is impossible. For each of the other \(q-1\) complements, \(s\ne0\) and there is a unique \(x\). Hence \(\nu_{IN}(A)=q-1\).

It remains to count the zero fiber. If \(E=0\), any of the \(q^2\) nilpotents is allowed. If \(E=I\), only \(N=0\) is allowed. For a fixed nontrivial idempotent with kernel line \(K\), the condition \(EN=0\) is equivalent to \(\operatorname{im}N\subseteq K\). There are exactly \(q\) such nilpotents: zero, together with the \(q-1\) nonzero maps whose image and kernel both equal \(K\). Since there are \(q(q+1)\) nontrivial idempotents,
\[
\nu_{IN}(0)=q^2+1+q\,q(q+1)=q^3+2q^2+1.
\]
An invertible \(A\) has no factorization because a product containing a nilpotent factor is singular.

Finally, transposition is a bijection from IN-factorizations of \(A\) to NI-factorizations of \(A^T\). The preceding formula for \(\nu_{IN}\) depends only on whether \(A\) is zero and on \(\det A\) and \(\operatorname{tr}A\), all of which are unchanged by transposition. Hence \(\nu_{NI}(A)=\nu_{IN}(A)\) for every \(A\).

## Verification
A standalone exact checker enumerates all matrices, idempotents, and nilpotents over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), \(\mathbb F_5\), and \(\mathbb F_7\). It groups outputs of \((E,N)\mapsto EN\) by the four cases in the theorem and verifies that every matrix in a given case has the asserted fiber size. The replay returns `VERIFY_OK` and gives, for example, fiber sizes \((17,3,1,0)\) over \(\mathbb F_2\) and \((97,5,3,0)\) over \(\mathbb F_4\), in the order zero, nonzero nilpotent, nonnilpotent rank one, invertible.

As a global consistency check, the theorem's fibers sum to
\[
(q^3+2q^2+1)+(q^2-1)(q+1)+q(q^2-1)(q-1)
=q^2(q^2+q+2),
\]
which is exactly the number of ordered pairs \((E,N)\), because there are \(q^2+q+2\) idempotents and \(q^2\) nilpotents.

## Relationship to prior work
Dolžan, *Products of Nilpotent and Idempotent Matrices over Finite Local Rings* (arXiv:2608.20934, first posted 21 August 2026), proves that IN and NI matrices coincide in \(M_2(R)\) for finite commutative local principal rings and gives the total number of matrices in this class. Its Theorem 3.6 is an image characterization and Theorem 3.10 is a cardinality formula; neither gives the number of ordered factorizations above a fixed target. In the field case, its formula specializes to \(q(q^2+q-1)\), the number of singular \(2\times2\) matrices.

Călugăreanu and Pop, *2-Products of Idempotent by Nilpotent Matrices* (Bulletin of the Iranian Mathematical Society 50 (2024), article 61, DOI 10.1007/s41980-024-00883-y), characterize existence of IN and NI decompositions for \(2\times2\) zero-determinant matrices over Prüfer and related domains. Their statements are solvability criteria, not fiber cardinalities.

Searches of published-finding corpus and the indexed primary literature using the terms “ordered factorizations”, “fiber cardinality”, “IN factorization”, “NI factorization”, and the candidate formulas found no statement implying the four exact fiber sizes above.

## Limitations
The proof is specific to dimension two: it uses that every nonzero nilpotent has rank one with equal image and kernel and that every nontrivial idempotent is a projection between two lines. The formula therefore does not automatically extend to \(M_n(\mathbb F_q)\) for \(n\ge3\), nor to finite local rings with nonzero radical. The literature search supports originality but cannot prove absence from every unpublished or unindexed source. Independent audit has not been performed.

## References
1. D. Dolžan, *Products of Nilpotent and Idempotent Matrices over Finite Local Rings*, arXiv:2608.20934v1, 21 August 2026. Primary MSC 15B33.
2. G. Călugăreanu and H. F. Pop, *2-Products of Idempotent by Nilpotent Matrices*, Bulletin of the Iranian Mathematical Society 50 (2024), article 61, DOI 10.1007/s41980-024-00883-y.
