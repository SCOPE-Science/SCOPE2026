# Compact recurrent words upgrade weak projection products to strong convergence

## Statement

Let \(H\) be a Hilbert space, let \(\{P_j\}_{j\in J}\) be orthogonal
projections, and let
\[
M=\bigcap_{j\in J}\mathcal R(P_j),\qquad P=P_M.
\]
For a selection \(\sigma:\mathbb N\to J\), write
\[
T_n=P_{\sigma(n)}P_{\sigma(n-1)}\cdots P_{\sigma(1)}.
\]

### Theorem (compact recurrent-word upgrade)

Assume that
\[
T_nx\rightharpoonup Px\qquad(x\in H).
\]
Suppose that a finite word
\[
\omega=(i_1,\ldots,i_m)
\]
occurs as a consecutive block of \(\sigma\) infinitely often, and put
\[
W=P_{i_m}\cdots P_{i_1}.
\]
If
\[
W-P\in\mathcal K(H),
\]
then
\[
T_nx\longrightarrow Px
\]
in norm for every \(x\in H\).

Equivalently, the extra hypothesis is that the recurrent word and the
common-intersection projection have the same image in the Calkin algebra:
\[
\pi(W)=\pi(P)\quad\text{in }B(H)/\mathcal K(H).
\]

## Proof

Because \(M\subseteq\mathcal R(P_j)\) for every \(j\),
\[
P_jP=P=PP_j.
\]
Thus \(M^\perp\) is invariant under every \(P_j\), and
\[
PT_n=P=T_nP.
\]
Fix \(x\in H\) and set \(y=(I-P)x\). Then
\[
T_nx-Px=T_ny,\qquad T_ny\rightharpoonup0,
\]
and the contraction property of orthogonal projections gives the monotonicity
\[
\|T_{n+1}y\|\le \|T_ny\|.
\]

Choose infinitely many occurrences of \(\omega\), with starting positions
\(a_k+1\) and ending positions \(b_k=a_k+m\), where \(a_k\to\infty\). At each
such endpoint,
\[
T_{b_k}y=WT_{a_k}y.
\]
Since \(PT_{a_k}y=0\),
\[
T_{b_k}y=(W-P)T_{a_k}y.
\]
The sequence \(T_{a_k}y\) is bounded and weakly null. Compact operators map
bounded weakly null sequences to norm-null sequences, hence
\[
\|T_{b_k}y\|\longrightarrow0.
\]
As \(\|T_ny\|\) is nonincreasing, the full sequence satisfies
\[
\|T_ny\|\longrightarrow0.
\]
Therefore \(T_nx\to Px\) for every \(x\in H\).

This last monotonicity step is also consistent with Eskandari--Moslehian's
earlier weak-plus-strong-subsequence principle for projection products
(arXiv:2405.04848, Lemma 2.14).

## Infinite-periodic consequence

Eskandari and Moslehian proved in 2026 that if
\(\sigma:\mathbb N\to\mathbb N\) is infinite-periodic, then
\[
T_nx\rightharpoonup Px
\]
for every \(x\in H\), where \(P\) projects onto
\(\bigcap_{j\ge1}\mathcal R(P_j)\) (arXiv:2609.13957, Theorem 2.12).

Their definition requires every index \(j\) to occur infinitely often.
Consequently the theorem above gives:

### Corollary (finite excess above the common intersection)

Let \(\sigma\) be infinite-periodic in the sense of arXiv:2609.13957. If for
some \(j\)
\[
\dim\bigl(\mathcal M_j\ominus M\bigr)<\infty,
\qquad \mathcal M_j=\mathcal R(P_j),
\]
then
\[
T_nx\longrightarrow Px
\]
strongly for every \(x\in H\).

Indeed,
\[
P_j-P=P_{\mathcal M_j\cap M^\perp}
\]
is finite rank, hence compact, and the one-letter word \(j\) recurs
infinitely often.

This gives a strong-convergence criterion for the countably infinite
infinite-periodic setting without the positivity hypothesis used in
Corollary 3.3 of arXiv:2609.13957 and without the finite-angle plus
monotone-tail hypotheses of Theorem 2.16 in arXiv:2405.04848.

## A genuinely multi-letter compact gate

The compact-word condition can hold even when no individual reduced
projection \(P_j-P\) is compact.

Let
\[
H=M\oplus K,\qquad
K=\bigoplus_{n\ge1}\mathbb C^2,
\]
where \(M\) is any infinite-dimensional Hilbert space. In the \(n\)-th copy
of \(\mathbb C^2\), choose an orthonormal basis \(e_n,f_n\), put
\[
c_n=\frac1{n+1},\qquad s_n=(1-c_n^2)^{1/2},
\]
and define
\[
E=\overline{\operatorname{span}}\{e_n:n\ge1\},
\qquad
F=\overline{\operatorname{span}}\{c_ne_n+s_nf_n:n\ge1\}.
\]
Then \(E\cap F=\{0\}\). Let \(P_1,P_2\) be the orthogonal projections onto
\(M\oplus E\) and \(M\oplus F\), respectively, and let \(P\) be the
projection onto \(M\).

Both
\[
P_1-P,\qquad P_2-P
\]
are infinite-rank orthogonal projections and therefore are noncompact.
However,
\[
P_1P_2-P=0_M\oplus Q_EQ_F,
\]
where \(Q_E,Q_F\) are the projections onto \(E,F\). On the \(n\)-th
two-dimensional block, \(Q_EQ_F\) has the single nonzero singular value
\(c_n\). Since \(c_n\to0\),
\[
P_1P_2-P\in\mathcal K(H).
\]

Thus any weakly \(P\)-convergent control in which the ordered two-letter
word "apply \(P_2\), then \(P_1\)" recurs infinitely often converges
strongly, although neither factor is compact modulo \(P\).

This phenomenon also occurs inside the countably infinite
infinite-periodic framework. For example, set \(P_j=P_1\) for \(j\ge3\) and
take
\[
\sigma(n)=1+v_2(n),
\]
where \(v_2(n)\) is the exponent of \(2\) in \(n\). Every index occurs
infinitely often with bounded gaps, and the block \(2,1\) occurs
infinitely often. Hence the products converge strongly even though every
individual \(P_j-P\) is noncompact.

## Relation to prior literature

The recent paper of Eskandari and Moslehian,
*Convergence of Random Products of Projections Under Infinite-Periodic
Selections* (arXiv:2609.13957v1, submitted 12 September 2026), proves weak
convergence for arbitrary infinite-periodic selections. Its additional
strong-convergence result, Corollary 3.3, assumes a subsequence of positive
partial products. The paper contains no compactness, finite-dimensional
excess, or Calkin-algebra criterion.

Their earlier paper *Convergence of Random Products of Countably Infinitely
Many Projections* (arXiv:2405.04848v2; J. Approx. Theory 317 (2026))
contains Lemma 2.14, which upgrades weak convergence to strong convergence
once a strongly convergent subsequence is already available, and Theorem
2.16, which obtains strong convergence for a pseudo-periodic class under a
finite-family angle condition together with a monotonically decreasing
tail. The compact recurrent-word mechanism above supplies the strongly
convergent subsequence from a different, operator-ideal hypothesis.

Compactness mechanisms are classical for finite families. Dye, Khamsi and
Reich proved in 1991 that a random product of a finite number of suitable
contractions converges weakly, and that if one contraction is compact the
convergence is uniform. Dye's 1989 work treats finite sets of compact
contractions. These results are close precedents, but their stated setting
is a finite generating family and compact generators, whereas the theorem
above only requires one recurrent finite product to equal \(P\) modulo
compacts and applies after any independently established weak convergence,
including the countably infinite infinite-periodic theorem of 2026.

Pustylnik, Reich and Zaslavski obtained strong and uniform convergence
criteria for nonperiodic products using inclination/angle geometry of
finite tuples. Kopecká later characterized convergence phenomena for
finite families of projections. Those results provide important nearby
finite-family theory but do not, in the inspected statements, give the
countable recurrent-word/Calkin criterion above.

## Limitations

The theorem is a sufficient criterion, not a characterization. For words
of length greater than one, actual consecutive recurrence of that ordered
word is required. No operator-norm convergence or convergence rate is
claimed. The argument is for orthogonal projections (or, more abstractly,
for contraction products with the same fixed projection identities); no
claim is made for arbitrary idempotents or nonlinear projections.

Originality is asserted only to the best of our knowledge. Older
finite-family random-product literature contains related compactness and
geometric mechanisms, and some full texts were not exhaustively checked
for differently phrased special cases.

## References

1. R. Eskandari and M. S. Moslehian, *Convergence of Random Products of
   Projections Under Infinite-Periodic Selections*, arXiv:2609.13957v1
   (2026), to appear in Proc. Amer. Math. Soc.
   https://arxiv.org/abs/2609.13957
2. R. Eskandari and M. S. Moslehian, *Convergence of Random Products of
   Countably Infinitely Many Projections*, J. Approx. Theory 317 (2026);
   arXiv:2405.04848v2.
   https://arxiv.org/abs/2405.04848
3. J. Dye, M. A. Khamsi and S. Reich, *Random Products of Contractions in
   Banach Spaces*, Trans. Amer. Math. Soc. 325 (1991), 87--99.
   https://doi.org/10.1090/S0002-9947-1991-0989572-5
4. J. M. Dye, *Convergence of Random Products of Compact Contractions in
   Hilbert Space*, Integral Equations Operator Theory 12 (1989), 12--22.
   https://doi.org/10.1007/BF01199754
5. E. Pustylnik, S. Reich and A. J. Zaslavski, *Convergence of
   Non-Periodic Infinite Products of Orthogonal Projections and
   Nonexpansive Operators in Hilbert Space*, J. Approx. Theory 164 (2012),
   611--624. https://doi.org/10.1016/j.jat.2012.01.001
6. E. Kopecká, *When Products of Projections Diverge*, J. London Math. Soc.
   102 (2020), 279--292; arXiv:1901.01921.
   https://arxiv.org/abs/1901.01921
