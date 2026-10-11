# A \(K\)-rescaling counterexample to a woven \(K\)-\(g\)-frame perturbation theorem

## Finding
Theorem 3.10 of Faraj--Derouich--Rossafi gives a perturbation criterion intended to imply that two \(K\)-\(g\)-frames are woven. The criterion is false as stated.

Take
\[
H=\mathbb C^2,\qquad
I=\{1,2\},\qquad
V_1=V_2=\mathbb C,
\qquad
K=\frac14 I_H.
\]
Define
\[
\Lambda_1 f=\langle f,e_1\rangle,\qquad
\Lambda_2 f=\langle f,e_2\rangle,
\]
and
\[
\Gamma_1 f=\langle f,e_2\rangle,\qquad
\Gamma_2 f=\langle f,e_1\rangle.
\]
Each family is an ordinary Parseval \(g\)-frame. Since
\[
\|K^*f\|^2=\frac1{16}\|f\|^2,
\]
both families satisfy the \(K\)-\(g\)-frame inequalities with
\[
A_1=A_2=16,\qquad B_1=B_2=1.
\]

Set
\[
\alpha=\beta=\mu=\frac34.
\]
The scalar smallness condition printed in the theorem becomes
\[
\frac94<4.
\]
For an arbitrary coefficient vector \(c=(c_1,c_2)\),
\[
\left(
\sum_{i=1}^2
\|(\Lambda_i^*-\Gamma_i^*)c_i\|^2
\right)^{1/2}
=
\sqrt2\,\|c\|,
\]
whereas the right side of the theorem's perturbation inequality equals
\[
\frac94\|c\|.
\]
Hence all displayed perturbation hypotheses hold.

However, the weave using \(\Lambda_1\) and \(\Gamma_2\) consists twice of the \(e_1\)-coordinate functional. It has zero energy on \(e_2\), while
\[
\|K^*e_2\|^2=\frac1{16}.
\]
That weave is not a \(K\)-\(g\)-frame. Thus the theorem's wovenness conclusion fails.

## Assumptions and scope
A Hilbert space is a Hilbert \(C^*\)-module over the scalar algebra \(\mathbb C\), so this example lies inside the source's stated setting.

The index set and all coefficient spaces are finite-dimensional. Every operator is adjointable, every relevant range is closed, and the Moore--Penrose inverse exists:
\[
K^\dagger=4I_H.
\]

The counterexample addresses Theorem 3.10 exactly as printed, including its displayed scalar threshold
\[
\alpha\sqrt{B_1}+\beta\sqrt{B_2}+\mu
<
\frac{A_1}{2(\sqrt{B_1}+\sqrt{B_1})}.
\]
No claim is made here about a differently normalized perturbation theorem.

## Proof
For \(\Lambda\),
\[
\sum_{i=1}^2\|\Lambda_i f\|^2=\|f\|^2,
\]
and the same identity holds for \(\Gamma\). Therefore
\[
16\|K^*f\|^2=\|f\|^2
\]
gives the admissible lower bound \(16\), while \(1\) is an admissible upper bound.

For coefficients \(c_1,c_2\in\mathbb C\),
\[
(\Lambda_1^*-\Gamma_1^*)c_1=c_1(e_1-e_2)
\]
and
\[
(\Lambda_2^*-\Gamma_2^*)c_2=c_2(e_2-e_1).
\]
Consequently,
\[
\sum_{i=1}^2
\|(\Lambda_i^*-\Gamma_i^*)c_i\|^2
=
2(|c_1|^2+|c_2|^2).
\]
Meanwhile,
\[
\left(\sum_i\|\Lambda_i^*c_i\|^2\right)^{1/2}
=
\left(\sum_i\|\Gamma_i^*c_i\|^2\right)^{1/2}
=
\|c\|.
\]
With
\[
\alpha=\beta=\mu=\frac34,
\]
the required perturbation estimate is therefore
\[
\sqrt2\,\|c\|
\le
\frac94\|c\|,
\]
which holds.

The scalar threshold also holds:
\[
\alpha\sqrt{B_1}+\beta\sqrt{B_2}+\mu
=
\frac94
<
4
=
\frac{A_1}{2(\sqrt{B_1}+\sqrt{B_1})}.
\]

Now choose the partition with index \(1\) taken from \(\Lambda\) and index \(2\) taken from \(\Gamma\). The woven energy at \(f=e_2\) is
\[
|\Lambda_1e_2|^2+|\Gamma_2e_2|^2=0.
\]
But
\[
\|K^*e_2\|^2=\frac1{16}.
\]
No positive lower \(K\)-\(g\)-frame bound exists for this weave.

The reason the hypothesis can coexist with failure is its scaling. Replacing an invertible \(K_0\) by \(\varepsilon K_0\) changes a legal lower \(K\)-frame bound by the factor \(\varepsilon^{-2}\), but it does not change the woven analysis families. A threshold whose right side grows with that lower bound and does not compensate for the scale of \(K\) can therefore certify nonwoven pairs after sufficiently strong rescaling.

## Verification
The open publisher PDF was inspected at the definition of woven \(K\)-\(g\)-frames, Theorem 3.10, and the complete proof. The statement uses the displayed threshold above and concludes wovenness. In the proof, the estimate later acquires the factor
\[
\|K^\dagger\|\|K^*f\|,
\]
and the stated lower bound is
\[
A_1-\frac{A_1}{2}\|K^\dagger\|.
\]
For the present example,
\[
\|K^\dagger\|=4,
\]
so even the proof's final coefficient is nonpositive. More importantly, the explicit weave above proves that the theorem's main wovenness conclusion itself is false.

Every calculation in the counterexample is exact; no numerical experiment is used.

## Relationship to prior work
Earlier woven \(K\)-fusion perturbation results use hypotheses that compare the removed or perturbed energy directly with \(K\)-scaled quantities. A later continuous controlled \(K\)-\(g\)-fusion perturbation theorem likewise imposes a positivity condition on a coefficient multiplying the \(K\)-energy. Those formulations do not imply the non-scale-invariant criterion in Theorem 3.10.

Targeted searches using the exact title, DOI, theorem number, perturbation constants, Moore--Penrose scaling, and correction terminology did not locate an indexed erratum or a source containing this two-dimensional counterexample.

The closest checked frame-theoretic results concern range compression, diagonal scaling, reconstruction families, or other perturbation mechanisms. None implies the present theorem-specific failure.

## Limitations
The finding refutes Theorem 3.10 as printed and identifies a scale-invariance obstruction. It does not provide a complete replacement theorem for arbitrary Hilbert \(C^*\)-modules.

A corrected perturbation theorem may be possible after reformulating the hypothesis with a genuinely \(K\)-scaled error quantity or otherwise compensating for \(K\mapsto\varepsilon K\).

An unindexed erratum, thesis remark, or informal author correction may contain the same counterexample or scaling observation.

## References
1. H. Faraj, M. Derouich and M. Rossafi, *Woven \(K\)-\(g\)-frames in Hilbert \(C^*\)-modules*, Journal of Mathematical and Computational Science 12 (2022), Article 89, DOI 10.28919/jmcs/6907.
2. V. Sadri, G. Rahimlou and R. Ahmadi, *K-G-Fusion Woven in Hilbert Spaces*, TWMS Journal of Applied and Engineering Mathematics 11(3) (2021), 947--958.
3. P. Ghosh and T. K. Samanta, *Weaving continuous controlled \(K\)-\(g\)-fusion frames in Hilbert spaces*, arXiv:2111.03389v1.
