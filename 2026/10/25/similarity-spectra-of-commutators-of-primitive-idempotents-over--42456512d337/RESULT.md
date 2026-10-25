# Similarity spectra of commutators of primitive idempotents over finite fields

## Finding

Let \(q\) be any prime power, \(n\ge 2\), and \(E\) a fixed rank-one idempotent in \(M_n(\mathbb F_q)\). Let \(F\) range through all rank-one idempotents, and set \(C=[E,F]=EF-FE\). Put
\[
 d=n-1,\qquad B=(q^d-1)q^{d-1},\qquad T=q^d\frac{q^{d+1}-1}{q-1}.
\]
There are exactly \(T\) choices of \(F\). The following list is the complete *similarity-type distribution* of \(C\), with numbers of \(F\) shown for each type:

| Similarity type | Exact multiplicity |
| --- | ---: |
| Zero matrix \(0_n\) | \(1+B/(q-1)\) |
| \(J_2(0)\oplus0_{n-2}\) | \(2B+2(q^d-1)\) |
| \(J_3(0)\oplus0_{n-3}\), only \(n\ge3\) | \((q^d-1)(q^{d-1}-1)\) |
| \(\operatorname{Comp}(t^2-\delta)\oplus0_{n-2}\), each \(\delta\ne0\) of the form \(\delta=c(c-1)\) | \(m_q(\delta)B\) |

Here \(J_k(0)\) is a nilpotent Jordan block, \(\operatorname{Comp}(t^2-\delta)\) is the cyclic \(2\times2\) companion block, and \(m_q(\delta)=|\{c\in\mathbb F_q:c(c-1)=\delta\}|\). A row with zero multiplicity is omitted; in particular the length-three nilpotent block never appears when \(n=2\). No other similarity type occurs. Equivalently, every such commutator obeys
\[
 [E,F]^3=c(c-1)[E,F],\qquad c=\operatorname{tr}(EF),
\]
and the table distinguishes the different nilpotent types left unresolved by this cubic identity alone.

When \(q\) is odd, there are \((q-1)/2\) nonzero values of \(\delta\): the distinguished value \(-1/4\) has \(m_q(\delta)=1\), and every other attained nonzero value has \(m_q(\delta)=2\). When \(q\) is even, the attained nonzero values are the nonzero elements with absolute field trace zero; there are \(q/2-1\) such values and each has \(m_q(\delta)=2\). In characteristic two the nonzero companion blocks have a repeated eigenvalue and are not scalar: they are cyclic, hence nontrivial Jordan blocks over the finite field.

The exact joint distribution of ordered pairs \((E,F)\) is obtained by multiplying every displayed multiplicity by \(T\), because conjugation acts transitively on rank-one idempotents. In particular, at fixed \(q\), the probabilities of the zero, length-two nilpotent, length-three nilpotent, and nonnilpotent classes converge, respectively, to
\[
 \frac1{q^2},\qquad \frac{2(q-1)}{q^2},\qquad
 \frac{q-1}{q^2},\qquad \frac{(q-1)(q-2)}{q^2}
\]
as \(n\to\infty\). Thus nilpotency of index three persists with positive limiting probability for every finite field, despite both inputs being idempotent.

## Assumptions and scope

All linear algebra is over the finite field \(\mathbb F_q\), without a restriction on characteristic. Matrix multiplication is ordinary associative multiplication. A rank-one idempotent is a matrix \(P\) with \(P^2=P\) and rank exactly one; it is not the zero idempotent. Similarity types are over the base field, not merely over an algebraic closure. The two-element cases and the field of two elements are included. Counts concern an ordered pair, with \(E\) fixed and \(F\) varying, unless expressly multiplied by \(T\).

## Proof

**Normalization and parametrization.** Any rank-one idempotent is conjugate to \(E=\operatorname{diag}(1,0_d)\). Every rank-one idempotent \(F\) has a representation \(F=uv^{\mathsf T}\), with nonzero \(u,v\in\mathbb F_q^n\) satisfying \(v^{\mathsf T}u=1\). Exactly \(q-1\) representations give each \(F\), via \((u,v)\mapsto(\lambda u,\lambda^{-1}v)\). Choosing \(u\ne0\) and then an affine hyperplane of \(q^{n-1}\) choices for \(v\) gives \(T=q^{n-1}(q^n-1)/(q-1)\).

Write \(u=(a,x)^{\mathsf T}\) and \(v=(b,y)^{\mathsf T}\), where \(x\in\mathbb F_q^d\), \(y\in(\mathbb F_q^d)^*\), so \(ab+yx=1\). Put \(c=ab=\operatorname{tr}(EF)\). Direct multiplication gives
\[
 C=\begin{pmatrix}0&ay\\-bx&0_d\end{pmatrix},\quad
 C^2=\begin{pmatrix}-ab\,yx&0\\0&-ab\,xy\end{pmatrix},\quad
 C^3=c(c-1)C.
\]

**Nonzero pairing count.** For each nonzero \(t\in\mathbb F_q\), the number of \((x,y)\in\mathbb F_q^d\times(\mathbb F_q^d)^*\) satisfying \(yx=t\) is \(B=(q^d-1)q^{d-1}\): choose nonzero \(x\), then choose \(y\) in an affine hyperplane. For \(yx=0\) with both vectors nonzero, the count is \((q^d-1)(q^{d-1}-1)\).

**Case \(c=0\).** If \(a=b=0\), then \(yx=1\) and \(C=0\), contributing \(B/(q-1)\) distinct idempotents. If exactly one of \(a,b\) is nonzero, then \(yx=1\), \(C\ne0\), \(C^2=0\), and \(\operatorname{rank}C=1\). The \(2(q-1)B\) vector-pair representations contribute \(2B\) idempotents. No other case with \(c=0\) is possible.

**Case \(c=1\).** Here \(a,b\ne0\) and \(yx=0\). The case \(x=y=0\) gives the unique \(F=E\), adding one zero commutator. Exactly one of \(x,y\) nonzero contributes \(2(q^d-1)\) distinct rank-one square-zero commutators. With both nonzero, \(C\) has rank two, \(C^2\ne0\), and \(C^3=0\), so its nilpotent Jordan type is exactly \(J_3(0)\oplus0_{n-3}\). The zero-pairing count above gives \((q^d-1)(q^{d-1}-1)\) such idempotents. This count vanishes when \(d=1\).

**Case \(c\notin\{0,1\}\).** Now \(a,b\ne0\), \(yx=1-c\ne0\), and there are precisely \(B\) distinct \(F\) for each value of \(c\). The commutator has rank two. Its two-dimensional image is the invariant subspace spanned by the first basis vector and \((0,x)^{\mathsf T}\); on this subspace it has an invertible cyclic off-diagonal matrix with characteristic and minimal polynomial \(t^2-c(c-1)\). The complement is annihilated by \(C\), yielding the asserted companion block and zero blocks. Grouping the values of \(c\) by \(\delta=c(c-1)\) proves the fourth row, including multiplicity \(m_q(\delta)B\).

**Field-dependent parameter fibers.** If the characteristic is odd, the discriminant of \(c^2-c-\delta\) is \(1+4\delta\). Its zero value occurs once (at \(\delta=-1/4\)); the remaining attained values are paired by \(c\leftrightarrow1-c\). If the characteristic is two, \(c\mapsto c^2+c\) is an \(\mathbb F_2\)-linear map with kernel \(\{0,1\}\) and image the absolute-trace-zero subspace. This proves the parameter claims.

**Exhaustion and asymptotics.** The cases \(c=0\), \(c=1\), and \(c\notin\{0,1\}\) partition all idempotents. Their multiplicities sum to \(T\). Conjugation preserves brackets and transits on rank-one idempotents, establishing the ordered-pair multiplier \(T\). Dividing each total class count by \(T\) and taking fixed-field limits yields the four proportions.

## Verification

A standalone checker is included as `verify_rank_one_idempotent_commutators.py`, with recorded output `verify_rank_one_idempotent_commutators.out`. It enumerates every matrix over fields of orders \(2,3,4,5\) in the tested dimensions, identifies rank-one idempotents by direct rank and multiplication tests, and independently classifies each commutator by its rank, nilpotency, cubic relation, and parameter \(\delta\). The degree-two extension field is implemented using the polynomial \(X^2+X+1\). All eight finite configurations passed, inspecting 348,853 matrices and finding 669 rank-one idempotents. These checks support but do not replace the all-dimension proof above.

## Relationship to prior work

Ferraz, Polcino Milies and Taufer (2017) establish structural rank-one idempotent facts and counts in finite matrix rings; their normalization supports the setting, but their examined results do not give a similarity distribution for brackets of two rank-one idempotents. Brešar, Gardella and Thiel (2024) study products of general commutators, and in particular arbitrary trace-zero commutators, without the two rank-one-idempotent restriction or these exact fibers. Hoopes-Boyd (2020) addresses representations of nilpotent matrices as arbitrary single commutators; its publicly accessible abstract does not give this constrained full spectrum. Related counting of zero-products or opposite-product ranks is also weaker than a determination of the entire Jordan/rational canonical class of the commutator. The novelty assessment is bounded to sources actually checked; a negative search is not proof of precedence.

## Limitations

The result concerns *two rank-one idempotents* in full finite-field matrix rings, not higher-rank idempotents, arbitrary products or distributions of individual matrices \(C\) within their similarity conjugacy classes. The fourth row counts input pairs by *similarity type*, not by every fixed output matrix. Some specialist historical sources were only abstract-accessible, so an equivalent implicit result elsewhere cannot be excluded. Computational tests cover finitely many small fields and dimensions. Independent assessment of originality and correctness has not been performed.

## References

1. R. A. Ferraz, C. Polcino Milies and E. Taufer, *Left ideals in matrix rings over finite fields*, arXiv:1711.09289v1 (2017), especially Section 3 and its rank-one idempotent counting framework. https://arxiv.org/pdf/1711.09289
2. M. Brešar, E. Gardella and H. Thiel, *Products of commutators in matrix rings*, arXiv:2404.18116v1 (2024), especially Section 4. https://arxiv.org/pdf/2404.18116
3. E. Hoopes-Boyd, *Representing nilpotent matrices as single commutators*, Communications in Algebra (2020), DOI:10.1080/00927872.2020.1791900. Abstract available; full text not verified.
