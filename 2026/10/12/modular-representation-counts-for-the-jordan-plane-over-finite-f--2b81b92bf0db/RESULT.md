# Modular representation counts for the Jordan plane over finite fields

## Finding

For a finite field \(k=\mathbb F_q\) of characteristic \(p\), let the Jordan plane be the associative algebra
\[
R=k\langle x,y\rangle/(xy-yx-y^2).
\]
Its \(n\)-dimensional representations with chosen basis are precisely the ordered matrix pairs \((X,Y)\in M_n(k)^2\) with \([X,Y]=Y^2\). We determine the exact number \(N_{n,q}\) of such pairs in every dimension, and characterize every possible second matrix \(Y\).

**Solvable rational-canonical types.** Let \(\lambda_f(Y)\) be the partition of sizes of the cyclic \(f\)-primary blocks in the rational canonical decomposition of \(Y\), for every monic irreducible \(f\in k[t]\). There exists \(X\) satisfying \([X,Y]=Y^2\) if and only if, for every \(f\ne t\), every part of \(\lambda_f(Y)\) is divisible by \(p\). The nilpotent \(t\)-primary part is unrestricted. Every feasible \(Y\) has exactly \(q^{\dim_k C(Y)}\) partners \(X\), where \(C(Y)\) is its full matrix centralizer.

For \(n\ge0\), set \(N_{0,q}=1\) and \(g_{n,q}=|\mathrm{GL}_n(k)|\) (with \(g_{0,q}=1\)). Let
\[
I_q(d)=\frac1d\sum_{e\mid d}\mu(e)q^{d/e}
\]
be the number of monic irreducible polynomials of degree \(d\). The **complete normalized representation count** is
\[
\boxed{\displaystyle
\sum_{n\ge0}\frac{N_{n,q}}{g_{n,q}}u^n
=\left[\prod_{r\ge1}\prod_{j\ge0}\frac1{1-u^r q^{-j}}\right]
\left[\prod_{d\ge1}\prod_{r\ge1}\prod_{j\ge0}
\frac1{(1-u^{dpr}q^{-dj})^{I_q(d)-\mathbf 1_{d=1}}}\right].}
\]
Each coefficient is finite and exact. The first factor counts the unrestricted nilpotent part; the second accounts for all nonzero spectral primary parts, whose cyclic lengths must be multiples of the characteristic.

**Sharp modular onset.** If \(n<p\), every feasible \(Y\) is nilpotent. At \(n=p\), exactly the nonnilpotent similarity classes \(Y\sim aI+J_p\), with \(a\in k^\times\) and \(J_p\) a single nilpotent Jordan block, become feasible; together these contribute \(qg_{p,q}\) ordered pairs. Consequently,
\[
N_{2,q}=\begin{cases}2q^4-q^2,&p\ne2,\\ q^5+q^4-q^3,&p=2.\end{cases}
\]
For example, \(N_{2,2}=40\), \(N_{2,3}=153\), \(N_{2,4}=1216\), and \(N_{3,2}=2192\).

## Assumptions and scope

The field \(k\) may be any finite field, including extension fields and characteristic two. The integer \(n\) is arbitrary and nonnegative. The polynomial \(t\) denotes the zero-eigenvalue primary component; \(f\ne t\) includes all other monic irreducibles, not just linear polynomials. In each \(f\)-primary block \(k[t]/(f^\ell)\), a part \(\ell\) records the exponent of \(f\), not its full \(k\)-dimension \(d\ell\). Products of infinitely many factors are understood coefficientwise in \(u\): for a fixed coefficient of degree \(n\), only finitely many pairs of positive integers \((d,r)\) contribute; each internal geometric series over \(j\ge0\) converges as a rational number for \(q\ge2\).

## Proof

**1. Linear solvability and fiber cardinality.** For fixed \(Y\), the linear map \(\delta_Y:M_n(k)\to M_n(k)\), \(X\mapsto XY-YX\), has kernel \(C(Y)\). The trace pairing \((A,B)\mapsto\operatorname{tr}(AB)\) is nondegenerate in every characteristic. Cyclicity of trace gives
\[
\operatorname{im}\delta_Y=C(Y)^\perp.
\]
Therefore \([X,Y]=Y^2\) is solvable exactly when \(\operatorname{tr}(Y^2Z)=0\) for all \(Z\in C(Y)\). If solvable, the affine solution space is a translate of \(C(Y)\), hence contains exactly \(q^{\dim_k C(Y)}\) points.

**2. The blockwise criterion.** Extend scalars to an algebraic closure. Solvability of the finite linear system is unchanged by extension, so it suffices to test the trace condition over the closure. Conjugate \(Y\) into Jordan blocks \(J_\ell(a)=aI+N_\ell\). Projecting to any individual block commutes with the direct-sum \(Y\). Thus, using a block projection as \(Z\), the condition implies \(\ell a^2=0\). Conversely, an arbitrary matrix commuting with the direct-sum \(Y\) has diagonal block restrictions commuting with each Jordan block. The commutant of one Jordan block consists of polynomials in that block. Such a polynomial has constant diagonal value \(c\); the product with \(J_\ell(a)^2\) therefore has trace \(\ell a^2c\). If every block satisfies \(\ell a^2=0\), all diagonal block traces vanish, proving sufficiency. For \(a=0\) the condition is automatic. For \(a\ne0\), it is exactly \(p\mid\ell\). Because finite fields are perfect, an \(f\)-primary rational cyclic summand with exponent \(\ell\) splits over the closure into \(\deg(f)\) Jordan blocks of size \(\ell\), one for each distinct root of \(f\). The asserted rational-canonical test follows.

**3. Centralizer-weighted orbit enumeration.** For each irreducible polynomial \(f\) of degree \(d\), a primary partition \(\lambda\) contributes \(d|\lambda|\) to dimension. Let \(m_r(\lambda)\) be the multiplicity of part \(r\), and let \(\lambda'\) be the conjugate partition. The standard centralizer formulas are
\[
\dim_k C_f=d\sum_i(\lambda'_i)^2,
\qquad
|C_f^\times|=q^{d\sum_i(\lambda'_i)^2}\prod_{r\ge1}\prod_{j=1}^{m_r(\lambda)}(1-q^{-dj}).
\]
One \(\mathrm{GL}_n(k)\)-orbit of type \((\lambda_f)_f\) has size \(g_{n,q}/\prod_f|C_f^\times|\). Multiplying its orbit size by its prescribed-commutator fiber size \(q^{\dim C(Y)}\), and dividing by \(g_{n,q}\), leaves exactly
\[
\prod_f\prod_{r\ge1}\prod_{j=1}^{m_r(\lambda_f)}(1-q^{-\deg(f)j})^{-1},
\]
with no other weights. The sum is over the admissible partitions described in Step 2.

**4. Euler products.** For a fixed degree \(d\), a part size \(r\) with multiplicity \(m\) has weight \(u^{drm}/\prod_{j=1}^m(1-q^{-dj})\). The elementary \(q\)-binomial identity
\[
\sum_{m\ge0}\frac{z^m}{\prod_{j=1}^{m}(1-Q^j)}
=\prod_{j\ge0}(1-zQ^j)^{-1}
\]
then gives the factor \(\prod_{j\ge0}(1-u^{dr}q^{-dj})^{-1}\). The zero polynomial \(f=t\) permits all \(r\ge1\), giving the first Euler product. Each nonzero \(f\) permits only \(r\in p\mathbb Z_{>0}\), giving a factor with \(u^{dpr}\). There are exactly \(I_q(d)-\mathbf1_{d=1}\) such irreducible polynomials of degree \(d\), proving the full formula.

**5. Threshold and first counts.** A nonnilpotent \(Y\) requires a nonzero primary part with cyclic length at least \(p\), hence \(n\ge p\). When \(n=p\), its only possible type is one degree-one block \((t-a)^p\), \(a\ne0\). Its centralizer algebra has dimension \(p\), and its invertible centralizer has order \((q-1)q^{p-1}\). The \(q-1\) corresponding similarity classes contribute
\[
(q-1)\frac{g_{p,q}}{(q-1)q^{p-1}}q^p=qg_{p,q}.
\]
In dimension two, the nilpotent classes are \(Y=0\), contributing \(q^4\), and the single nonzero nilpotent similarity class, comprising \(q^2-1\) matrices with \(q^2\) partners each. In characteristic two, the additional \(q-1\) nonnilpotent classes contribute \(q^2(q-1)(q^2-1)\). The stated dimension-two formulas follow by summing these contributions.

## Verification

The standalone program `verification/jordan_plane_verify.py` independently constructs \([X,Y]-Y^2\) by matrix multiplication over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), counts all ordered solutions in dimensions two (all three fields) and three (\(\mathbb F_2\)), and separately computes solution fibers by Gaussian elimination. It also tests eligibility in sampled dimension-three matrices over \(\mathbb F_3\) and \(\mathbb F_4\), expands the rational Euler products through degree five for four fields, and checks integrality after multiplying by \(g_{n,q}\). Run with `python verification/jordan_plane_verify.py`; the final success marker is `VERIFY_OK_JORDAN_PLANE`. These finite tests corroborate the proof but do not establish an arbitrary-dimension theorem.

## Relationship to prior work

Iyudu's 2008 work studies representations of the same Jordan plane, including the nilpotence of \(Y\) in the stated characteristic-zero setting and its Jordan forms. Iyudu's later representation-space paper likewise treats characteristic zero. These precedents cover important structure of the nilpotent branch and are not claimed as new here. The present theorem addresses **positive-characteristic finite fields** and explicitly counts the nonnilpotent branches beginning in dimension \(p\). The rational-canonical centralizer formulas and cycle-index identities underlying the Euler product are classical and recorded, for example, by Fulman. Positive-characteristic work on the **restricted** Jordan plane studies a further quotient with truncation relations; it does not, by itself, supply the point counts for the unrestricted algebra here. Novelty is claimed only for the joint modular block admissibility and the resulting all-dimensional finite-field point-count refinement, not for the standard ingredients.

## Limitations

This theorem enumerates framed finite-field representations, not isomorphism classes of indecomposable modules or geometric irreducible components. It does not provide closed single-polynomial expressions for \(N_{n,q}\) at arbitrary fixed \(n\) independent of characteristic, though each coefficient can be extracted effectively. The characteristic-zero analysis is prior work, not an extension proved here. Historical equivalent finite-field enumerations under other terminology remain a bibliographic possibility; no independent mathematical audit is asserted.

## References

1. N. K. Iyudu, *Representation theory of Jordanian algebra* (2008), arXiv:0802.1545v1, first posted 12 February 2008, https://arxiv.org/abs/0802.1545.
2. N. K. Iyudu, *Representation spaces of the Jordan plane* (2012 preprint; 2014 journal article), arXiv:1209.0746v1, https://arxiv.org/abs/1209.0746.
3. J. Fulman, *Random matrix theory over finite fields* (2000), arXiv:math/0003195, https://arxiv.org/abs/math/0003195, including the finite-field matrix cycle-index and rational-canonical centralizer factors.
4. N. Andruskiewitsch and H. Peña Pollastri, *On the restricted Jordan plane in odd characteristic* (2020), arXiv:2002.02514, https://arxiv.org/abs/2002.02514.
