# Sharp smallness threshold for a \(K\)-fusion perturbation theorem
## Finding
Theorem 9 of Xu--Li--Leng, arXiv:1801.02785v2, asserts that a family \(\{(V_i,w_i)\}_{i\in I}\) is a \(K\)-fusion frame whenever a weighted quadratic perturbation inequality holds with \(0\leq\lambda_1,\lambda_2<1/2\) and arbitrary \(\mu>0\). That conclusion is false without a smallness condition on \(\mu\).

Let
\[
a_-:=\inf_i a_i,\qquad a_+:=\sup_i a_i,\qquad b_-:=\inf_i b_i,\qquad b_+:=\sup_i b_i,
\]
which are positive and finite because the two coefficient sequences are positively confined. Define
\[
p:=\lambda_1+\frac{\mu}{Aa_-^2},\qquad q:=\lambda_2,\qquad \Delta:=\sqrt{p+q-pq},
\]
and, when \(p<1\),
\[
r_-:=\frac{1-\Delta}{1-q},\qquad r_+:=\frac{1+\Delta}{1-q}.
\]
The exact universal missing smallness condition, in terms of the theorem's stated data, is
\[
\mu<(1-\lambda_1)Aa_-^2.
\]
Under this condition the perturbation hypothesis implies that \(\{(V_i,w_i)\}\) is a \(K\)-fusion frame with valid bounds
\[
\frac{Aa_-^2r_-^2}{b_+^2}
\quad\text{and}\quad
\frac{Ba_+^2r_+^2}{b_-^2}.
\]
The threshold is sharp as a universal parameter-only guarantee.

## Assumptions and scope
Let \(H\) be a Hilbert space, let \(K\in\mathcal L(H)\), and let \(\{(W_i,w_i)\}_{i\in I}\) be a \(K\)-fusion frame with certified bounds \(A,B>0\):
\[
A\|K^*f\|^2\leq \sum_i w_i^2\|\pi_{W_i}f\|^2\leq B\|f\|^2
\quad\text{for every }f\in H.
\]
Assume \(a_i,b_i>0\) are positively confined, \(0\leq\lambda_1,\lambda_2<1/2\), \(\mu>0\), and closed subspaces \(V_i\subset H\) satisfy
\[
\sum_i w_i^2\|(a_i\pi_{W_i}-b_i\pi_{V_i})f\|^2
\leq
\lambda_1\sum_i a_i^2w_i^2\|\pi_{W_i}f\|^2
+\lambda_2\sum_i b_i^2w_i^2\|\pi_{V_i}f\|^2
+\mu\|K^*f\|^2
\]
for every \(f\in H\). The claim concerns what follows uniformly from exactly these data. It does not claim that an individual perturbed family must fail whenever the sharp universal threshold is violated.

## Proof
First, the published statement fails in dimension one. Take \(H=\mathbb C\), \(K=I\), \(I=\{1\}\), \(W_1=H\), \(V_1=\{0\}\), and \(w_1=a_1=b_1=1\). The original family is a Parseval \(K\)-fusion frame, so \(A=B=1\). With \(\lambda_1=\lambda_2=0\) and \(\mu=1\), the perturbation hypothesis becomes
\[
\|f\|^2\leq\|f\|^2,
\]
so every hypothesis is satisfied. But the perturbed energy is identically zero, hence no positive lower \(K\)-fusion-frame bound exists.

For the repair, introduce the nonnegative quantities
\[
X(f)^2:=\sum_i a_i^2w_i^2\|\pi_{W_i}f\|^2,
\qquad
Y(f)^2:=\sum_i b_i^2w_i^2\|\pi_{V_i}f\|^2,
\]
and
\[
D(f)^2:=\sum_i w_i^2\|(a_i\pi_{W_i}-b_i\pi_{V_i})f\|^2.
\]
Since \(X(f)^2\geq a_-^2A\|K^*f\|^2\), the perturbation hypothesis gives
\[
D(f)^2\leq pX(f)^2+qY(f)^2.
\]
The three quantities are norms of vectors in the same Hilbert direct sum, so the triangle inequality gives
\[
X(f)\leq Y(f)+D(f),
\qquad
Y(f)\leq X(f)+D(f).
\]
If \(X(f)>0\), put \(r:=Y(f)/X(f)\). Then
\[
1\leq r+\sqrt{p+qr^2},
\qquad
r\leq1+\sqrt{p+qr^2}.
\]
When \(p<1\) and \(q<1\), solving the boundary equation
\[
(1-r)^2=p+qr^2
\]
gives the two roots
\[
r_\pm=\frac{1\pm\sqrt{p+q-pq}}{1-q}.
\]
The preceding inequalities therefore imply
\[
r_-X(f)\leq Y(f)\leq r_+X(f).
\]
If \(X(f)=0\), the original lower frame inequality forces \(K^*f=0\), so the lower \(K\)-frame estimate is automatic; the upper estimate follows directly from the perturbation inequality and the triangle inequality.

Finally,
\[
Y(f)^2\leq b_+^2\sum_iw_i^2\|\pi_{V_i}f\|^2,
\qquad
X(f)^2\geq a_-^2A\|K^*f\|^2,
\]
so
\[
\sum_iw_i^2\|\pi_{V_i}f\|^2
\geq
\frac{Aa_-^2r_-^2}{b_+^2}\|K^*f\|^2.
\]
Similarly,
\[
Y(f)^2\geq b_-^2\sum_iw_i^2\|\pi_{V_i}f\|^2,
\qquad
X(f)^2\leq a_+^2B\|f\|^2,
\]
which yields
\[
\sum_iw_i^2\|\pi_{V_i}f\|^2
\leq
\frac{Ba_+^2r_+^2}{b_-^2}\|f\|^2.
\]
Thus the repaired family is a \(K\)-fusion frame.

The condition \(p<1\) is exactly
\[
\mu<(1-\lambda_1)Aa_-^2.
\]
It is sharp for universal guarantees from these parameters. For any boundary or supercritical choice \(\mu\geq(1-\lambda_1)Aa_-^2\), take a one-dimensional one-index system with \(K=I\), \(W_1=H\), \(V_1=\{0\}\), \(a_1=a_-\), and choose the weight so that the original fusion-frame energy is exactly \(A\|f\|^2\). Then
\[
D(f)^2=Aa_-^2\|f\|^2
\leq
\lambda_1Aa_-^2\|f\|^2+\mu\|f\|^2,
\]
while the perturbed lower frame energy remains zero.

## Verification
The counterexample was checked by direct substitution into every hypothesis. The repaired inequalities were reconstructed from the direct-sum triangle inequality and the scalar quadratic equation above. A separate symbolic stress test sampled \(100000\) random pairs \((p,q)\) with \(0\leq p<1\) and \(0\leq q<1/2\); whenever the scalar perturbation constraint held, the computed ratio lay inside \([r_-,r_+]\). This numerical check is only a consistency check; the proof is the exact quadratic calculation.

## Relationship to prior work
The source's Theorem 9 contains no smallness condition on \(\mu\), while its immediately following Theorem 10 uses a different norm-form perturbation and explicitly imposes a smallness condition involving \(\lambda_1\), \(\lambda_2\), \(\mu\), and the lower frame bound. The source therefore does not itself imply the repaired Theorem 9 statement.

Related perturbation results also impose an additive-error threshold. For ordinary \(g\)-frames, Lemma 4.1 of the 2018 Journal of Inequalities and Applications paper below assumes a condition of the form \(\lambda_1+\mu/\sqrt A<1\). For \(K\)-\(g\)-fusion frames, Theorem 3.17 of the 2020 paper below assumes \(c/(1-a)<\sqrt A\). Those theorems concern different perturbation inequalities and do not state the coefficient-weighted threshold \(\mu<(1-\lambda_1)Aa_-^2\), the explicit \(r_\pm\) bounds, or the scalar sharpness boundary proved here.

## Limitations
The threshold is claimed to be sharp only as a universal guarantee determined by the source theorem's parameters. An individual family can remain a \(K\)-fusion frame beyond that threshold because additional geometry can improve stability. The later journal publication associated with the preprint was identified bibliographically; the mathematical statement verified here is the openly available arXiv v2 Theorem 9. No independent audit has been performed.

## References
1. Y. Xu, D. Li, J. Leng, *Fusion frames for operators and atomic systems*, arXiv:1801.02785v2, Theorem 9; first public version 2018-01-09.
2. Y. Xu, J. Leng, *Fusion frames for operators and atomic systems*, Journal of Pseudo-Differential Operators and Applications 13 (2022), Article 17, doi:10.1007/s11868-022-00451-0.
3. *Characterization and stability of approximately dual g-frames in Hilbert spaces*, Journal of Inequalities and Applications (2018), doi:10.1186/s13660-018-1779-7, Lemma 4.1.
4. *K-g-fusion frames in Hilbert spaces*, Journal of Inequalities and Applications (2020), doi:10.1186/s13660-020-02320-0, Theorem 3.17.
