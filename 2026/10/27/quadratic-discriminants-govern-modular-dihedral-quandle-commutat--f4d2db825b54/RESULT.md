# Quadratic discriminants govern modular dihedral quandle commutators

## Finding

Let \(K\) be any field of characteristic \(5\). In the five-element dihedral quandle algebra \(A=K[R_5]\), let the natural basis satisfy \(e_i e_j=e_{2j-i}\), with subscripts in \(\mathbb Z/5\mathbb Z\), and let \([f,g]=fg-gf\). Identify the underlying vector space of \(A\) with the ordinary group algebra \(K[X]/(X^5-1)\), by sending \(e_i\) to \(X^i\). Set \(t=X-1\) and
\[
w=\sum_{j=1}^{4}(-1)^{j+1}t^j/j.
\]
Since \(t^5=0\), this defines a coordinate \(w\) with \(w^5=0\). The augmentation ideal is \(J=wK[w]/(w^5)\), and each \(z\in J\) has unique coordinates
\[
z=z_1w+z_2w^2+z_3w^3+z_4w^4.
\]

**Complete single-commutator criterion.** The element \(z\) equals \([f,g]\) for some \(f,g\in A\) if and only if
\[
z_1\ne0\quad\text{or}\quad z_3^2-2z_2z_4\text{ is a square in }K,
\]
where zero counts as a square. Every element of \(J\) is a sum of at most two commutators, and the commutator-generated subalgebra is exactly \(J\). Thus its commutator width is \(1\) if every element of \(K\) is a square, and \(2\) otherwise.

For every finite field \(K=\mathbb F_q\) with \(q=5^m\), \(m\ge1\), precisely
\[
\frac{q(q-1)^2}{2}
\]
elements of \(J\) have commutator length exactly \(2\). Precisely \(q^4-1-q(q-1)^2/2\) nonzero elements have length \(1\), while zero has length \(0\). Consequently, the fraction of all derived elements requiring two commutators is exactly \((q-1)^2/(2q^3)\). The values for \(q=5\) and \(q=25\) are respectively \(40\) and \(7200\).

## Assumptions and scope

The algebra is the native, generally nonassociative, nonunital quandle algebra, not the associative group algebra. The group algebra is used solely as a vector-space model; its ordinary multiplication is invoked to express the native multiplication. All equations are in characteristic five. Commutator length counts sums of commutators of arbitrary elements; scalar coefficients can be absorbed into either factor. No claim is made for other characteristics, other dihedral orders, or commutator lengths in ordinary associative group algebras.

## Proof

**1. Coordinates.** Let \(R=K[X]/(X^5-1)=K[t]/(t^5)\). The quandle multiplication translates to
\[
f\ast g=f(X^{-1})g(X^2),
\]
where the multiplication on the right is the ordinary associative multiplication in \(R\). Define the truncated exponential \(\operatorname{Exp}(s)=\sum_{j=0}^4s^j/j!\). Truncated exponential and logarithm are inverse polynomial maps in nilpotence degree five; thus \(X=\operatorname{Exp}(w)\), and the two substitutions \(X\mapsto X^{-1}\) and \(X\mapsto X^2\) send \(w\) respectively to \(-w\) and \(2w\). Consequently
\[
f\ast g=f(-w)g(2w),\qquad [f,g]=f(-w)g(2w)-g(-w)f(2w).
\]

**2. Alternating-coordinate formula.** Write \(f=\sum_{i=0}^4 f_iw^i\), \(g=\sum_{i=0}^4 g_iw^i\), and \(p_{ij}=f_ig_j-f_jg_i\) for \(0\le i<j\le3\). Only pairs with \(i+j<5\) contribute. In characteristic five, direct expansion gives
\[
[f,g]=3p_{01}w+3p_{02}w^2+4(p_{03}+p_{12})w^3+4p_{13}w^4.
\]
In particular, all commutators have augmentation zero; the coefficient \(f_4\) or \(g_4\) does not influence the result. The four basis elements of \(J\) belong to the linear span of commutators: choose respectively the pairs \((1,w)\), \((1,w^2)\), \((1,w^3)\), \((w,w^3)\). Thus the linear span is exactly \(J\); because \(J\) is an ideal closed under the quandle product, the commutator-generated subalgebra is also \(J\).

**3. Plücker obstruction.** Given a target \(z\), put
\[
a=z_1/3,\quad b=z_2/3,\quad s=z_3/4,\quad d=z_4/4.
\]
Its realization as a single commutator is equivalent to finding six \(p_{ij}\) which arise as minors of a \(2\)-by-\(4\) matrix and satisfy \(p_{01}=a\), \(p_{02}=b\), \(p_{03}+p_{12}=s\), \(p_{13}=d\). The unique Plücker relation for such minors is
\[
p_{01}p_{23}-p_{02}p_{13}+p_{03}p_{12}=0.
\]
It is also sufficient: an alternating \(4\)-by-\(4\) matrix with this zero Pfaffian has rank at most two, hence represents a decomposable bivector over \(K\). If \(a\ne0\), take \(p_{03}=0\), \(p_{12}=s\) and \(p_{23}=bd/a\); this satisfies the relation. If \(a=0\), writing \(p_{03}=u\), \(p_{12}=s-u\) reduces the relation to
\[
u^2-su+bd=0.
\]
This equation has a root in \(K\) precisely when \(s^2-4bd\) is a square, including zero. Since \(3^{-1}=2\) and \(4^{-1}=4\) in characteristic five,
\[
s^2-4bd=z_3^2-2z_2z_4.
\]
This proves the criterion for all fields of characteristic five.

**4. Width and finite-field count.** Every target with \(z_1\ne0\) is one commutator; every target with \(z_1=0\) is the sum of one commutator with first coordinate \(1\) and another with first coordinate \(-1\). Therefore the width is at most two. If some \(\delta\in K\) is nonsquare, the target \(z_1=z_3=0\), \(z_2=1\), \(z_4=-\delta/2\) has discriminant \(\delta\), and so has length two. Conversely, if every field element is a square, every target is one commutator. For \(K=\mathbb F_q\) of odd cardinality, a nonsquare discriminant forces \(z_2\ne0\). Choose \(z_2\in K^\times\) in \(q-1\) ways and \(z_3\in K\) in \(q\) ways; for each of the \((q-1)/2\) nonsquares \(\delta\), the equation \(\delta=z_3^2-2z_2z_4\) determines exactly one \(z_4\). The result is \(q(q-1)^2/2\) length-two elements, as claimed.

## Verification

The included `verify.py` is a standard-library-only checker, run using `python verify.py`. It independently forms every ordered pair of four-coordinate inputs over \(\mathbb F_5\) (\(625^2=390625\) pairs), compares the complete image with the stated quadratic criterion, and confirms \(585\) single-commutator values and \(40\) obstructions. It separately checks all \(25\) natural quandle basis products against the truncated-logarithm formula. Over \(\mathbb F_{25}\), represented using a root of \(Y^2-3\), it checks all \(25^3\) discriminant triples by independent quadratic-root enumeration, obtaining \(7200\) nonsquare obstructions, and tests \(5000\) seeded random commutators against the criterion. All checks complete with `VERIFY_OK`.

## Relationship to prior work

Bardakov, Passi and Singh introduced quandle commutator width and gave general estimates and selected exact computations in their 2022 paper. Sangare and Ta's 2026 paper, Theorem 5.4 and discussion following Theorem 5.6, explicitly reports that \(\mathbb F_5[R_5]\) has a four-dimensional commutator subalgebra and exactly \(40\) elements of commutator length two. That finite datum is **not** presented as new here. What is added is a necessary-and-sufficient criterion for **each** potential commutator over **any** characteristic-five field, its geometric explanation by a Plücker quadric, the extension-field census for every \(q=5^m\), and the arbitrary-field dichotomy for commutator width. These do not follow merely from the previously enumerated \(q=5\) case.

## Limitations

No assertion of first discovery independent of unpublished or unindexed literature is made. The derivation covers only the five-element dihedral quandle in coefficient characteristic five. The experiment in the extension field tests the quadratic criterion and constructed instances, not all ordered pairs there; the complete statement for arbitrary fields follows from the algebraic proof. There is no independent external mathematical audit.

## References

1. V. G. Bardakov, I. B. S. Passi, M. Singh, *Zero-divisors and idempotents in quandle rings*, Osaka J. Math. **59** (2022), 611–637, doi:10.18910/88489. Open-access full text: https://ir.library.osaka-u.ac.jp/repo/ouka/all/88489/ojm59_03_611.pdf. First arXiv posting: January 19, 2020, arXiv:2001.06843.
2. B. Sangare, L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550, first posted August 3, 2026, especially Section 5.1 and Theorem 5.4.
