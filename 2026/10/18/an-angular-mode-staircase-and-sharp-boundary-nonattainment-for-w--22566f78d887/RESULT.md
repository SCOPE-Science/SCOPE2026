# An angular-mode staircase and sharp boundary nonattainment for weighted Forelli–Rudin operators

## Finding
On the disk with normalized area measure \(d\mu(z)=dA(z)/\pi\), consider the complex weighted integral operator
\[
(T_{a,b,c}f)(z)=(1-|z|^2)^a\int_{\mathbb D}\frac{(1-|w|^2)^b f(w)}{(1-z\overline w)^c}\,d\mu(w).
\]
For \(a,b>-1/2\), \(c>0\), define \(L=a+b+2\). Its exact unsorted nonzero singular sequence is
\[
s_n=\frac{(c)_n}{n!}\sqrt{B(n+1,2a+1)B(n+1,2b+1)},\qquad n=0,1,2,\dots.
\]
The operator is bounded precisely for \(c\le L\), compact precisely for \(c<L\), and in the compact regime belongs to Schatten \(S_p\) exactly when \(p(L-c)>1\) for \(p>0\).

When \(a\ne b\), put
\[
h_n=\sqrt{(n+2a+2)(n+2b+2)}-n,\qquad n\ge0.
\]
The numbers \(h_n\) strictly increase from \(h_0=2\sqrt{(a+1)(b+1)}\) to \(L\). In the compact regime, the exact norm is \(\max_{n\ge0}s_n\), attained on one angular mode except at any \(c=h_n\), where the two adjacent modes \(n\) and \(n+1\) tie. More precisely, mode zero wins for \(c<h_0\), mode \(m\ge1\) wins for \(h_{m-1}<c<h_m\), and at \(c=h_m\) exactly modes \(m,m+1\) win. The selected frequency escapes to infinity according to
\[
m(c)\sim\frac{(a-b)^2}{2(L-c)}\qquad(c\uparrow L).
\]
At \(c=L\), the operator is bounded but noncompact, with norm
\[
\|T_{a,b,L}\|=\frac{\sqrt{\Gamma(2a+1)\Gamma(2b+1)}}{\Gamma(a+b+2)},
\]
which is **not attained by any nonzero input** when \(a\ne b\). In the symmetric case \(a=b\), mode zero wins uniquely for \(c<L\), while at \(c=L=2a+2\) every nonzero singular value is \(1/(2a+1)\); the norm is then attained by all nonzero inputs in the closed span of the right singular modes.

## Assumptions and scope
Throughout \(a,b>-1/2\), so the radial factors \((1-|z|^2)^a\), \((1-|w|^2)^b\) lie in area \(L^2\). The kernel uses the analytic branch of \((1-z\overline w)^{-c}\), well defined for \(|z\overline w|<1\). The operator acts between copies of the full area Hilbert space, not merely its holomorphic subspace. Singular values are listed by angular index before decreasing rearrangement. The words 'attains its norm' refer to a unit-vector input of the full area Hilbert space. If \(c>L\), the integral formula defines an unbounded densely defined operator; a bounded extension is impossible.

## Proof
Expand the kernel absolutely for fixed interior \(z\):
\[
(1-z\overline w)^{-c}=\sum_{n\ge0}\frac{(c)_n}{n!}z^n\overline w^n.
\]
For each \(n\ge0\), set \(v_n(w)=w^n(1-|w|^2)^b\) and \(u_n(z)=z^n(1-|z|^2)^a\). Different \(n\) have orthogonal angular dependence, and the normalized-area beta identity gives
\[
\|u_n\|_2^2=B(n+1,2a+1),\quad \|v_n\|_2^2=B(n+1,2b+1).
\]
Thus
\[
Tf=\sum_{n\ge0}\frac{(c)_n}{n!}u_n\langle f,v_n\rangle,
\]
with the convention that the inner product is linear in the first argument. This is an orthogonal rank-one decomposition; normalized \(u_n\), \(v_n\) form mutually orthogonal systems. On finite combinations it is an exact singular decomposition, extending boundedly precisely if the displayed coefficients \(s_n\) are uniformly bounded. The orthogonal complement of the closed span of the input vectors is the kernel.

The gamma-ratio formula implies
\[
s_n\sim Cn^{c-L},\quad C=\frac{\sqrt{\Gamma(2a+1)\Gamma(2b+1)}}{\Gamma(c)}.
\]
Consequently boundedness, compactness and the Schatten criterion follow, with the strict critical case handled below.

An exact consecutive-index calculation yields
\[
\frac{s_{n+1}}{s_n}=\frac{n+c}{\sqrt{(n+2a+2)(n+2b+2)}}.
\]
For \(a\ne b\), the threshold \(h(x)=\sqrt{(x+2a+2)(x+2b+2)}-x\) has derivative
\[
h'(x)=\frac{2x+2a+2b+4}{2\sqrt{(x+2a+2)(x+2b+2)}}-1>0,
\]
by strict arithmetic-geometric mean. Moreover \(h(x)\uparrow L\), and
\[
L-h(x)=\frac{(a-b)^2}{2x}+O(x^{-2}).
\]
Hence \(s_{n+1}>s_n\) exactly when \(c>h_n\). Below criticality there are finitely many rising steps followed by strict decay, giving the complete maximizing-mode and equality classifications. The threshold asymptotic gives the stated angular-index escape law.

At \(c=L\) and \(a\ne b\), all ratios are strictly greater than one, but the gamma asymptotic yields the displayed finite limit \(C\). No singular vector has singular value \(C\), and for any nonzero input in the right-mode span the weighted average of strictly smaller squared singular values is strictly smaller than \(C^2\). Thus the norm is not attained. When \(a=b\), the ratio simplifies to \((n+c)/(n+2a+2)\), decreasing below criticality and equal to one at \(c=L\). The beta identity then gives \(s_n=1/(2a+1)\) for all \(n\), proving the symmetric exceptional case.

## Verification
The accompanying `forelli_spectrum_checker.py` computes beta moments from log-gamma identities and verifies the exact consecutive ratio, monotone thresholds, symmetric critical identity and selected asymmetric boundary limits on reproducibly seeded parameter collections. Its `VERIFY_OK` output reports 18,023 finite comparisons. These are checks of implementation and boundary normalization; the proof of the infinite family is the analytic orthogonal decomposition above. Reproduce with `python forelli_spectrum_checker.py` using Python's standard library only.

## Relationship to prior work
Hu, Wang, Zhang and Zhou (2026) study weak and restricted weak \(L^p\)-to-\(L^q\) mapping, explicitly in the hypersingular range \(p>q\), for the same complex Forelli–Rudin kernel; the Hilbert operator-norm angular switching at \(p=q=2\) is a different problem. Kures and Zhu (2006) and Zhao and Zhou (2022) characterize boundedness regimes for Forelli–Rudin operators, but the statements accessible for comparison do not provide the full singular sequence, angular optimizer transitions, or norm nonattainment claimed here. The inspected Theorems 1–4 of Songxiao Li (2007) concern mixed-norm boundedness conditions rather than exact singular values or norm-maximizing angular degrees; uninspected auxiliary passages remain a priority risk. These distinctions are claims about inspected material only, not proof of comprehensive historical uniqueness.

## Limitations
The explicit mode staircase assumes \(a\ne b\); the symmetric case is treated separately. The theorem concerns the complex analytic kernel with normalized disk area and Hilbert input/output, not its absolute-value positive-kernel analogue or non-Hilbert endpoint norms. Priority uncertainty remains for older unindexed exact-norm calculations and parts of relevant papers not available for full-text comparison. No independent review or external verification has been performed.

## References
- B. Hu, Z. Wang, K. Zhang, X. Zhou, *Cancellation of complex kernels and sharp critical lines and endpoint theory for the Forelli–Rudin operators I*, arXiv:2609.14552 (first posted 2026-09-13), https://arxiv.org/abs/2609.14552.
- O. Kures and K. Zhu, *A class of integral operators on the unit ball of complex \(n\)-space*, Integral Equations Operator Theory 56 (2006), 71–82, https://doi.org/10.1007/s00020-005-1411-3.
- S. Li, *A class of integral operators on mixed norm spaces in the unit ball*, Czechoslovak Mathematical Journal 57 (2007), 1013–1023, https://dml.cz/dmlcz/128222.
- R. Zhao and L. Zhou, *L-p–L-q boundedness of Forelli–Rudin type operators on the unit ball*, Journal of Functional Analysis 282 (2022), article 109345, https://doi.org/10.1016/j.jfa.2021.109345.
