# Rank-free mixed Schatten commutator cost for finite-rank normal operators

## Statement

Let \(H\) be a separable infinite-dimensional complex Hilbert space, let \(1\le p,q<\infty\), and assume
\[
\frac1p+\frac1q<\frac12.
\]
Put \(r>2\) by
\[
\frac1r=\frac1p+\frac1q.
\]
For \(T\in S_r(H)\), define the mixed Schatten commutator cost
\[
\Gamma_{p,q}(T)
:=\inf\{\|A\|_p\,\|B\|_q:\ A\in S_p(H),\ B\in S_q(H),\ [A,B]=T\},
\tag{1}
\]
with \(\Gamma_{p,q}(T)=\infty\) if no such factorization exists. If \(P\) is a rank-one projection, set
\[
c_{p,q}:=\Gamma_{p,q}(P).
\tag{2}
\]
The Brown--Anderson theory implies \(c_{p,q}<\infty\) precisely in the strict region above.

Then every finite-rank normal operator \(T\) satisfies
\[
\boxed{
\frac12\|T\|_r\le \Gamma_{p,q}(T)\le c_{p,q}\|T\|_r.
}
\tag{3}
\]
Thus, for fixed \((p,q)\) in the admissible region, the optimal product of the two Schatten factor norms is equivalent to the \(S_r\)-norm of a finite-rank normal target, with constants independent of the rank and of the distribution of its nonzero eigenvalues.

More generally, (3) holds for every normal compact \(T\in S_r(H)\) whose kernel is infinite-dimensional.

For every nonzero positive finite-rank operator \(T\), the existence threshold is exact:
\[
\boxed{
\Gamma_{p,q}(T)<\infty
\quad\Longleftrightarrow\quad
\frac1p+\frac1q<\frac12.
}
\tag{4}
\]
Consequently, in the symmetric case \(p=q=s\), a nonzero positive finite-rank target admits a commutator factorization by two \(S_s\) operators exactly when \(s>4\), and throughout that region
\[
\Gamma_{s,s}(T)\asymp_s \|T\|_{s/2}.
\tag{5}
\]

## Context

Two recent results make the quantitative gap particularly visible. Tran (2026) introduced a homogeneous operator-norm commutator cost for finite matrices and proved a dimension-free bound for traceless matrices. Liu (2026) proved that every compact operator is a commutator of compact operators and obtained a universal operator-norm factor bound; for finite-rank targets, Liu also uses tensorization of Anderson's rank-one commutator.

The classical Schatten-ideal picture is different. Anderson's rank-one construction and Brown's obstruction, as summarized explicitly by Dykema--Figiel--Weiss--Wodzicki, show that a finite-rank operator of nonzero trace can occur in a single commutator \([S_p,S_q]\) exactly on the strict side of the hyperbola
\[
\frac1p+\frac1q=\frac12.
\]
Those results determine existence, but they do not provide the mixed factorization gauge (1) for a general target. The theorem above supplies a rank-free quantitative form on finite-rank normal operators and identifies the natural target norm \(S_r\).

## Proof

### 1. Universal lower bound

Let \(T=[A,B]\) with \(A\in S_p\) and \(B\in S_q\). Schatten Hölder gives \(AB,BA\in S_r\) and
\[
\|AB\|_r\le \|A\|_p\|B\|_q,
\qquad
\|BA\|_r\le \|B\|_q\|A\|_p.
\]
Hence
\[
\|T\|_r
\le \|AB\|_r+\|BA\|_r
\le 2\|A\|_p\|B\|_q.
\]
Taking the infimum over all factorizations gives
\[
\Gamma_{p,q}(T)\ge \frac12\|T\|_r.
\tag{6}
\]
This part does not require normality.

### 2. A tensor transfer lemma

Let \(P=[C,Z]\) be a rank-one projection with \(C\in S_p\) and \(Z\in S_q\). Suppose an operator \(T\) admits commuting factors
\[
T=XY=YX,
\qquad X\in S_p,
\qquad Y\in S_q.
\tag{7}
\]
On the Hilbert tensor product, set
\[
A=X\otimes C,
\qquad
B=Y\otimes Z.
\]
Then
\[
[A,B]
=XY\otimes CZ-YX\otimes ZC
=T\otimes [C,Z]
=T\otimes P.
\tag{8}
\]
Moreover, multiplicativity of Schatten norms under tensor products yields
\[
\|A\|_p\|B\|_q
=\|X\|_p\|Y\|_q\,\|C\|_p\|Z\|_q.
\tag{9}
\]

### 3. Normal targets have an optimal commuting Schatten split

Let \(T\) be normal and write its polar decomposition as
\[
T=U|T|.
\]
Normality implies that \(U\) commutes with \(|T|\) on the support of \(T\). Put
\[
\alpha=\frac rp,
\qquad
\beta=\frac rq.
\]
Since \(1/r=1/p+1/q\),
\[
\alpha+\beta=1.
\tag{10}
\]
Define
\[
X=U|T|^{\alpha},
\qquad
Y=|T|^{\beta}.
\tag{11}
\]
Then \(XY=YX=T\). Also \(\alpha p=\beta q=r\), so
\[
\|X\|_p
=\bigl(\operatorname{Tr}|T|^r\bigr)^{1/p}
=\|T\|_r^{r/p},
\tag{12}
\]
and similarly
\[
\|Y\|_q=\|T\|_r^{r/q}.
\tag{13}
\]
Multiplying and using \(r/p+r/q=1\),
\[
\|X\|_p\|Y\|_q=\|T\|_r.
\tag{14}
\]

### 4. Transfer the rank-one commutator

If \(T\) is finite rank on infinite-dimensional \(H\), then \(T\otimes P\) has exactly the same nonzero normal spectral data as \(T\) and an infinite-dimensional zero eigenspace. Hence \(T\otimes P\) is unitarily equivalent to \(T\). The same observation applies to any compact normal \(T\) with infinite-dimensional kernel.

Applying (8)--(14), and then conjugating the factors by a unitary implementing this equivalence, gives
\[
\Gamma_{p,q}(T)
\le \|T\|_r\,\|C\|_p\|Z\|_q.
\]
Taking the infimum over all rank-one factorizations \(P=[C,Z]\) proves
\[
\Gamma_{p,q}(T)\le c_{p,q}\|T\|_r.
\tag{15}
\]
Together with (6), this proves (3).

### 5. Exact phase transition for positive finite-rank targets

Let \(T\ge0\) be nonzero and finite rank. Then
\[
\operatorname{Tr}T>0.
\]
Brown proved that when
\[
\frac1p+\frac1q\ge\frac12,
\]
a finite-rank commutator \([A,B]\) with \(A\in S_p\), \(B\in S_q\) must have trace zero. Thus no such factorization of \(T\) exists in that region.

Conversely, when \(1/p+1/q<1/2\), Anderson's rank-one construction gives \(c_{p,q}<\infty\), and (15) gives a factorization of every finite-rank positive \(T\). This proves (4).

## Consequences and mechanism

The proof isolates a reusable principle. A single rank-one commutator serves as a universal infinite-dimensional carrier, while the target is encoded entirely in a commuting factorization \(T=XY=YX\). For normal \(T\), the polar/spectral calculus chooses the factor powers so that the product of the factor norms is exactly \(\|T\|_r\). This is why no rank factor appears.

By contrast, the elementary decomposition \(T=T I\) on the finite-dimensional support produces a factor involving the identity on that support and therefore generally introduces a rank-dependent Schatten norm. Normality removes that loss through the balanced spectral split (11).

## Limitations

The constants are not claimed sharp. In particular, the rank-one constant \(c_{p,q}\) is left implicit; only its finiteness in the Brown--Anderson admissible region is used. No claim is made that \(1/2\) is the optimal lower constant in (3).

The extension from finite rank to infinite-rank normal compact operators is stated only when the kernel is infinite-dimensional. The tensor model \(T\otimes P\) introduces an infinite-dimensional kernel, so it is not unitarily equivalent to an injective compact operator. No factorization theorem for injective normal compact targets is asserted here.

The exact nonexistence statement (4) uses the nonzero trace of a positive finite-rank target. Trace-zero finite-rank targets can behave differently outside the strict Brown--Anderson region, and no phase transition is claimed for them.

Originality is claimed only to the best of our knowledge. Anderson and Brown already established the existence/nonexistence threshold for nonzero-trace finite-rank targets, and Dykema--Figiel--Weiss--Wodzicki developed the surrounding operator-ideal commutator theory. Liu's recent finite-rank tensorization supplies a closely related operator-norm mechanism. The contribution claimed here is specifically the mixed Schatten factorization gauge, the rank-independent \(S_r\) two-sided estimate for normal targets, and the resulting quantitative formulation of the classical threshold. Older operator-ideal literature may contain an equivalent norm estimate under different terminology; this remains the main originality risk. Salinas's 1974 ideal-theoretic treatment was inspected as a nearby source, while Anderson's 1986 sequel on trace-class ideals remains a specific full-text access gap noted in the review.

## References

1. T. Tran, *Quantum expanders and dimension-free commutator bounds*, arXiv:2609.20161v1 (2026). https://arxiv.org/abs/2609.20161
2. Z. Liu, *Every compact operator is a commutator of compact operators*, arXiv:2609.20672v1 (2026). https://arxiv.org/abs/2609.20672
3. J. H. Anderson, *Commutators of compact operators*, J. Reine Angew. Math. 291 (1977), 128--132. https://doi.org/10.1515/crll.1977.291.128
4. L. G. Brown, *Traces of commutators of Schatten-von Neumann class operators*, J. Reine Angew. Math. 451 (1994), 171--174.
5. K. Dykema, T. Figiel, G. Weiss, and M. Wodzicki, *The commutator structure of operator ideals*, Adv. Math. 185 (2004), 1--79. https://doi.org/10.1016/S0001-8708(03)00141-5
6. J. Loreaux, S. Patnaik, S. Petrovic, and G. Weiss, *On Commutators of Compact Operators: Generalizations and Limitations of Anderson's Approach*, Integral Equations Operator Theory 96 (2024), Paper 16. https://doi.org/10.1007/s00020-024-02764-9
7. N. Salinas, *Ideals of commutators of compact operators*, Acta Sci. Math. (Szeged) 36 (1974), 131--144. https://acta.bibl.u-szeged.hu/14468/
8. J. H. Anderson, *Commutators in ideals of trace class operators II*, Indiana Univ. Math. J. 35 (1986), 373--378, MR 833400, Zbl 0602.47033. https://iumj.org/article/3231/
