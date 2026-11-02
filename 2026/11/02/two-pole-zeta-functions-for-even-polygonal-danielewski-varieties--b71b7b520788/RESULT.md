# Two-pole zeta functions for even polygonal Danielewski varieties

## Finding

Fix a prime power \(q\) and an even integer \(m\ge4\). Let \(\mathcal F^{(m)}=(F_1,\ldots,F_n)\) be the specific associated polynomial family over \(\mathbb F_q\) defined by the four seeds (4.4), the lift \(L\), the extension operator \(E\), and the recursion in Definition 4.25 of Gupta, Kuckian and Sengupta [1]. Consider **any** triangular affine system
\[
G_i=X^{d_i}Y_i-H_i(X,Y_0,\ldots,Y_{i-1})=0,\qquad 1\le i\le n,
\]
with \(d_i\) positive integers and \(H_i(0,Y_0,\ldots,Y_{i-1})=F_i\). Its zero scheme over \(\mathbb F_q\) is denoted \(V_{m,q}\); point counts depend only on the associated family, not on the unspecified extension terms.

**Theorem.** For every integer \(r\ge1\), write \(Q=q^r\). The complete extension-field point count is
\[
\#V_{m,q}(\mathbb F_Q)=
\begin{cases}
Q^2+\dfrac{m-4}{2}(q-1)Q,&m\equiv4,6\pmod8,\\[3pt]
2Q^2+\bigl(\dfrac{m-6}{2}(q-1)-1\bigr)Q,&m\equiv0,2\pmod8.
\end{cases}
\]
Consequently the local zeta function, defined by
\[
Z(V_{m,q},t)=\exp\!\left(\sum_{r\ge1}\frac{\#V_{m,q}(\mathbb F_{q^r})}{r}t^r\right),
\]
has the exact two-pole factorization
\[
Z(V_{m,q},t)=
\begin{cases}
\dfrac{1}{(1-q^2t)(1-qt)^{(m-4)(q-1)/2}},&m\equiv4,6\pmod8,\\[6pt]
\dfrac{1}{(1-q^2t)^2(1-qt)^{(m-6)(q-1)/2-1}},&m\equiv0,2\pmod8.
\end{cases}
\]
All the displayed exponents are nonnegative integers for the specified ranges. Thus the full zeta functions of the entire infinite even-polygonal family exhibit exactly two arithmetic types, according to the seed of the parent chain.

## Assumptions and scope

The integer \(q\) is **fixed in the coefficients** of the defining polynomials when evaluating their points over \(\mathbb F_{q^r}\). In particular, the polynomial \(Y^q-Y\) is not replaced by \(Y^{q^r}-Y\). The associated family is the exact recursive one in [1]; arbitrary polynomial families with the same single base-field count need not have the same zeta function. No smoothness or reducedness is assumed. The proof works in every characteristic, including two. The variables in the defining system are \(X,Y_0,\ldots,Y_n\).

## Proof

**Triangular fiber count over every extension.** Since the equations can be solved successively for \(Y_1,\ldots,Y_n\) whenever \(X\ne0\), there are precisely \(Q(Q-1)\) points with \(X\ne0\). When \(X=0\), the equations become \(F_i(Y_0,\ldots,Y_{i-1})=0\), and \(Y_n\) is free. Let \(N_m(Q)\) be the number of common zeros of \(\mathcal F^{(m)}\) in \(\mathbb F_Q^n\). Then
\[
\#V_{m,q}(\mathbb F_Q)=Q(Q-1)+Q N_m(Q).\tag{1}
\]
This elementary count is valid for any choice of the nonconstant-in-\(X\) terms and for every extension field.

**Base families over extension fields.** In [1, equations (4.1)--(4.4)] the seeds are \((Y_0^q-Y_0,\sigma_m)\), where
\[
\Delta(u)=u^{q-1},\qquad
\Omega(u,v)=\Delta(u)+\Delta(v)-\Delta(u)\Delta(v)
\]
and \(\sigma_4=\Omega\), \(\sigma_6=\Omega v\), \(\sigma_8=\Omega uv\), \(\sigma_{10}=\Omega uv(u+v)\). Over \(\mathbb F_Q\), the equation \(u^q-u=0\) has exactly the roots \(u\in\mathbb F_q\). For nonzero such \(u\), \(\Delta(u)=1\) and \(\Omega(u,v)=1\); for \(u=0\), \(\Omega(0,v)=v^{q-1}\), whose sole zero is \(v=0\). Counting the zeros of the displayed four products gives, **for all** \(Q=q^r\),
\[
N_4(Q)=1,\qquad N_6(Q)=q,\qquad
N_8(Q)=Q+q-1,\qquad N_{10}(Q)=Q+2(q-1).\tag{2}
\]
Note especially that the large \(Q\)-term occurs only for the last two seeds; base-field values alone do not reveal this distinction.

**Extension-field lift lemma.** Let \(\mathcal F=(F_1,\ldots,F_s)\) be any associated family over \(\mathbb F_q\), with \(N_{\mathcal F}(Q)\) common zeros over \(\mathbb F_Q\). The operator \(L\) of [1, Definition 4.18] prepends \(Y_0^q-Y_0\) and uses \(\alpha(u,v)=u^{q-1}v(v+u)\), \(\gamma(u)=1-u^{q-1}\). The operator \(E\) of [1, Definition 4.21] appends \(\beta(u,v)=\alpha(u,v)+\gamma(u)v\). We assert
\[
N_{E^\ell L(\mathcal F)}(Q)=N_{\mathcal F}(Q)+2^{s+\ell}(q-1)\qquad(\ell\ge0).\tag{3}
\]
Indeed, the first equation forces \(u\in\mathbb F_q\) even though the ambient field has \(Q\) elements. For \(u=0\), the shifted old equations reappear and every appended \(E\)-coordinate is forced to zero, yielding exactly \(N_{\mathcal F}(Q)\) solutions. For each of the \(q-1\) choices of \(u\in\mathbb F_q^\times\), \(\gamma(u)=0\); each of the \(s+\ell\) remaining equations becomes \(v(v+u)=0\), with two distinct roots \(v=0,-u\). This yields \(2^{s+\ell}(q-1)\) further solutions. The argument is valid in every characteristic and requires no claim about arbitrary \(u\in\mathbb F_Q\).

**Parent-chain telescope.** The construction [1, Definition 4.25] starts at the unique seed \(m_0\in\{4,6,8,10\}\) congruent to \(m\) modulo eight and repeatedly applies \(E^{\nu(m)}L\), where the previous family has \(s=n(\mathrm{Par}(m))\) equations and \(s+\nu(m)=n(m)-1\). As \(m-\mathrm{Par}(m)=2^{n(m)}\), equation (3) adds precisely \((q-1)(m-\mathrm{Par}(m))/2\) to \(N\), **independent of the extension degree**. All parent differences are divisible by eight, so the last seed is the one with the same residue modulo eight. Telescoping gives
\[
N_m(Q)=N_{m_0}(Q)+\frac{m-m_0}{2}(q-1).\tag{4}
\]
Substituting (2) into (4) yields
\[
N_m(Q)=
\begin{cases}
1+\dfrac{m-4}{2}(q-1),&m\equiv4,6\pmod8,\\[3pt]
Q+\dfrac{m-6}{2}(q-1),&m\equiv0,2\pmod8.
\end{cases}\tag{5}
\]
Equations (1) and (5) give the asserted extension counts. Finally \(\exp(\sum_{r\ge1}q^{jr}t^r/r)=(1-q^jt)^{-1}\) for \(j=1,2\), and linearity of the exponent gives the zeta formula. This concludes the proof.

## Verification

The standalone `verify.py` constructs the actual seed and recursive associated polynomial functions, performs direct finite-field operations in polynomial residue fields, and enumerates the zeros over extensions, rather than using equation (3) to predict the enumerated totals. It checks \(q=2,3,4,9\), their available extensions, and even polygonal indices including the initial seeds and later parent-chain cases, subject to a finite enumeration cap. A successful run reports `VERIFY_OK direct_extension_field_cases=124 associated_tuples_checked=172556`. The verifier also independently checks that the \(r=1\) counts equal the polygonal values from [1]. The infinite assertions follow from the proof, not from this finite test.

For a concrete base-change distinction, at \(q=2\) and \(m=8\), the fixed variety has \(\#V_{8,2}(\mathbb F_4)=32\), whereas rebuilding the defining polynomial family with \(q=4\) yields the octagonal value \(P_8(4)=40\). Changing the base field is not the same operation as extending scalars of a fixed polynomial system.

## Relationship to prior work

Gupta--Kuckian--Sengupta [1, Theorem 3.1] give the triangular count only over the original base field; [1, Lemma 4.23] prove the recursive increment for that field, and [1, Theorem 4.27] obtain \(P_m(q)\) as a base-field count. Their paper does not state extension-degree point counts or a zeta formula. Formula (3) is the key extension-field refinement: the newly forced root \(u^q=u\) stays in \(\mathbb F_q\), while old free coordinates can range over \(\mathbb F_{q^r}\).

The earlier paper [2, Section 7, Theorem 7.2] deals with four particular double Danielewski surfaces and their \(\mathbb F_q\)-points; it does not give the present zeta function for every recursively constructed even polygonal variety. Classical local zeta-function formalism supplies the generating-function definition but does not calculate the specific extension counts. Exact earlier implicit or unindexed coverage remains a priority risk.

## Limitations

The theorem applies **only** to the precise even-index recursive associated families from [1] and their triangular realizations. It does not cover the odd or centered polygonal constructions, arbitrary associated families sharing the same \(\mathbb F_q\)-count, or any statement about smoothness, cohomology, or geometric irreducibility. The elementary proof makes no independent-audit claim. The finite verifier covers selected small fields and indices, not an exhaustive set of all prime powers or all polygonal indices. Priority remains subject to independent expert comparison.

## References

[1] Sakshi Gupta, Anit Kuckian, Indranath Sengupta, *Rational Points on Affine Varieties over Finite Fields and Polygonal Number Sequences*, arXiv:2610.32930v1 (first posted 2026-10-23), https://arxiv.org/html/2610.32930v1; Sections 3 and 4, specifically Theorem 3.1, equations (4.1)--(4.4), Definitions 4.18, 4.21, 4.25, Lemma 4.23, and Theorem 4.27.

[2] Sakshi Gupta, Anit Kuckian, Indranath Sengupta, *Counting Rational Points on Danielewski and Double Danielewski Surfaces over Finite Fields*, arXiv:2605.24821v1 (2026-05-24), https://arxiv.org/html/2605.24821v1; Section 7, Theorem 7.2.
