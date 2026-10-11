# Exact norms and flat approximation numbers for scale-critical Hardy–Steklov windows

## Finding
Fix real or complex scalars, \(1<p_1,p_2<\infty\), \(0<q<\infty\) with \(1/q=1/p_1+1/p_2\), and \(\lambda_1,\lambda_2>1\). Consider the moving-window bilinear operator
\[
\mathcal B(f,g)(x)=\frac{1}{x^2}\left(\int_x^{\lambda_1 x} f(t)\,dt\right)\left(\int_x^{\lambda_2 x} g(t)\,dt\right),\quad x>0,
\]
from \(L^{p_1}(0,\infty)\times L^{p_2}(0,\infty)\) into \(L^q(0,\infty)\). For \(i\in\{1,2\}\) define
\[
A_i=\int_0^{\log\lambda_i} e^{(1-1/p_i)v}\,dv
=\frac{\lambda_i^{1-1/p_i}-1}{1-1/p_i}.
\]
Then the exact operator norm, compact-bilinear distance, and finite-rank-bilinear distance coincide:
\[
\boxed{\|\mathcal B\|=\operatorname{dist}(\mathcal B,\mathcal K_2)
=\operatorname{dist}(\mathcal B,\mathcal F_2)=A_1 A_2.}
\]
Every finite-rank approximation number in the range-dimension convention is flat:
\[
a_n^{(2)}(\mathcal B)=A_1A_2\qquad(n=1,2,\ldots).
\]
No pair of nonzero inputs attains the full operator norm. In particular, for the equality-boundary model of Kanjilal's Example 11.2, where \(p_1=p_2=2\), \(q=1\), and \(\lambda_1=\lambda_2=2\), the exact value is
\[
12-8\sqrt2=0.686291501015\ldots<\log2.
\]
The asymmetric model \(\lambda_1=2\), \(\lambda_2=4\), \(p_1=p_2=2\) from its Example 11.4 similarly has exact norm \(4(\sqrt2-1)\).

## Assumptions and scope
All integrations use Lebesgue measure on \((0,\infty)\). The bilinear operator norm is the supremum of the output \(L^q\) quasi-norm over the product of the input unit balls. Compact bilinear maps are bounded bilinear maps whose product-unit-ball images are relatively compact in \(L^q\). Finite-rank bilinear maps have finite-dimensional linear span of their range, and
\[
a_n^{(2)}(T)=\inf\{\|T-R\|:\operatorname{rank}R<n\}\qquad(n\ge1).
\]
When \(q<1\), the target topology is given by the complete metric \(d_q(u,v)=\|u-v\|_q^q\); distances displayed above are in the unpowered operator quasi-norm. The theorem does not include endpoint input exponents \(p_i=1\) or \(p_i=\infty\), or arbitrary weights or moving-window functions.

## Proof
**Logarithmic conjugation.** Set \(u=\log x\) and, for each input, \(h_i(u)=e^{u/p_i}f_i(e^u)\). The substitution \(x=e^u\) shows \(\|h_i\|_{L^{p_i}(\mathbb R)}=\|f_i\|_{L^{p_i}(0,\infty)}\). Put
\[
(C_i h)(u)=\int_0^{\log\lambda_i}e^{(1-1/p_i)v}h(u+v)\,dv.
\]
Substitution \(t=e^{u+v}\) yields
\[
\int_{e^u}^{\lambda_i e^u}f_i(t)\,dt=e^{(1-1/p_i)u}(C_i h_i)(u),
\]
so the critical identity \(1/q=1/p_1+1/p_2\) gives
\[
\mathcal B(f_1,f_2)(e^u)=e^{-u/q}(C_1h_1)(u)(C_2h_2)(u).
\]
Since \(dx=e^u du\), the output quasi-norm is exactly
\[
\|\mathcal B(f_1,f_2)\|_{L^q(dx)}
=\|(C_1h_1)(C_2h_2)\|_{L^q(du)}.
\]

**Sharp boundedness.** Minkowski's integral inequality and translation isometries, valid because \(p_i>1\), give \(\|C_i h_i\|_{p_i}\le A_i\|h_i\|_{p_i}\). Hölder's inequality with conjugate exponents \(p_1/q\) and \(p_2/q\), both strictly greater than one, gives
\[
\|(C_1h_1)(C_2h_2)\|_q\le \|C_1h_1\|_{p_1}\|C_2h_2\|_{p_2}
\le A_1A_2\|h_1\|_{p_1}\|h_2\|_{p_2}.
\]
This step remains valid when \(q<1\), since Hölder is applied to the integrable powers of the factors. For the reverse bound choose \(L>R=\max\{\log\lambda_1,\log\lambda_2\}\) and
\[
h_{i,L}(u)=L^{-1/p_i}\mathbf1_{[0,L]}(u).
\]
Each input has unit norm. For every \(u\in[0,L-R]\), one has \((C_i h_{i,L})(u)=A_i L^{-1/p_i}\). Hence
\[
\|\mathcal B(f_{1,L},f_{2,L})\|_q
\ge A_1A_2\left(\frac{L-R}{L}\right)^{1/q}\longrightarrow A_1A_2.
\]
Thus the upper bound is exactly sharp. These are valid explicit near-extremizers: \(f_{i,L}(t)=L^{-1/p_i}t^{-1/p_i}\mathbf1_{[1,e^L]}(t)\).

**No norm attainment.** Fix any nonzero \(h\in L^p(\mathbb R)\), \(1<p<\infty\), and let \(C\) be a positive weighted average of translates over an interval of positive length. If \(\|Ch\|_p=\|h\|_p\int k\), strict convexity of \(L^p\) makes the normalized translates \(h(\cdot+v)\) equal for almost every pair of shifts \(v\) in that interval: equality in the integral triangle inequality forces equality of the unit vectors. Two distinct shifts therefore differ by a nonzero period. A nonzero periodic function cannot belong to \(L^p(\mathbb R)\), contradiction. Thus \(\|C_i h\|_{p_i}<A_i\|h\|_{p_i}\) for every nonzero \(h\). Equality in the bilinear bound would require equality in each of the two linear bounds, which is impossible.

**Compact distance.** For each \(r>0\) define the isometric input dilations \(f_{i,r}(t)=r^{1/p_i}f_i(rt)\). Direct substitution gives
\[
\mathcal B(f_{1,r},f_{2,r})(x)=r^{1/q}\mathcal B(f_1,f_2)(rx).
\]
Hence the output \(L^q\) quasi-norm is unchanged, while for every fixed \(c>0\)
\[
\|\mathbf1_{(0,c)}\mathcal B(f_{1,r},f_{2,r})\|_q
\xrightarrow[r\to\infty]{}\|\mathcal B(f_1,f_2)\|_q.
\]
Let \(K\) be any compact bilinear map on the same input and output spaces. Relative compactness of its product-unit-ball image gives uniform small-set tails:
\[
\lim_{c\downarrow0}\sup_{\|f\|_{p_1},\|g\|_{p_2}\le1}
\|\mathbf1_{(0,c)}K(f,g)\|_q=0.
\]
Indeed, first prove this for one \(L^q\) function by absolute continuity of its integral; a finite net then gives uniformity. For \(q<1\) use the metric power \(\theta=q\), and otherwise take \(\theta=1\). The indicator is contractive, and the \(\theta\)-triangle inequality gives
\[
\|(\mathcal B-K)(f_{1,r},f_{2,r})\|_q^\theta
\ge \|\mathbf1_{(0,c)}\mathcal B(f_{1,r},f_{2,r})\|_q^\theta
-\|\mathbf1_{(0,c)}K(f_{1,r},f_{2,r})\|_q^\theta.
\]
First send \(r\to\infty\), then \(c\downarrow0\), and finally take the supremum over normalized input pairs: \(\|\mathcal B-K\|\ge\|\mathcal B\|\). The zero map is compact, so equality follows. Every finite-rank map is compact, while the zero map has rank zero; consequently the finite-rank distance and every \(a_n^{(2)}\) equal the same full norm.

## Verification
The logarithmic conjugation is an isometry for each input, and its output Jacobian cancels precisely at the harmonic exponent equality. The explicit normalized logarithmic interval tests verify sharpness without numerical extrapolation. The compactness argument uses a finite-net uniform-integrability fact valid also for \(0<q<1\), with powered metric exponent \(\theta=\min\{1,q\}\). All limits are ordinary dominated/monotone tail limits of integrable functions. Direct arithmetic at the symmetric Hilbert point gives \(A_i=2(\sqrt2-1)\), hence \(A_1A_2=12-8\sqrt2\).

## Relationship to prior work
Kanjilal's weighted bilinear Hardy–Steklov paper, arXiv:2610.02937v1, develops exact output-tail formulas and identifies bounded noncompact critical models. Its Example 11.2 gives a valid \(\log2\) upper bound in the symmetric Hilbert case, and its dilation argument already shows that the essential distance there equals the full but uncomputed operator norm. The present result computes that norm exactly, does so simultaneously for every critical harmonic pair of exponents and every two multiplicative window widths, and supplies explicit nonattainment and flat approximation conclusions. Its asymmetric Example 11.4 motivates treating distinct window widths. The same author's arXiv:2609.37998v1 treats instead product Hardy primitives with a fixed left endpoint; arXiv:2610.02649v1 treats input endpoints for that different primitive geometry. The logarithmic-convolution upper estimate uses classical Minkowski and Hölder inequalities; these standard ingredients are not claimed as discoveries.

## Limitations
The proof does not determine sharp norms beyond the exact dilation-critical relation, with genuinely variable windows, or with other input/output weights. Sharpness is attained only in the limit of increasingly long logarithmic intervals, not by any nonzero input pair. The flat approximation-number conclusion is restricted to the specified range-dimension convention for bilinear maps. The qualitative compactness obstruction and localization mechanism were established in the motivating source; what is added here is their exact quantitative calibration over this canonical parameter family.

## References
1. S. Kanjilal, *Compactness and Essential Distances of Weighted Bilinear Hardy–Steklov Operators*, arXiv:2610.02937v1 (2026), Sections 2–3 and 9–11, especially Examples 11.2 and 11.4; https://arxiv.org/abs/2610.02937.
2. S. Kanjilal, *Compactness and Essential Norms of Weighted Bilinear Hardy Operators on General Intervals*, arXiv:2609.37998v1 (2026), Introduction and Sections 1–2; https://arxiv.org/abs/2609.37998.
3. S. Kanjilal, *Input-Endpoint Compactness and Essential Norms for Weighted Bilinear Hardy Operators*, arXiv:2610.02649v1 (2026), Introduction and Sections 1–2; https://arxiv.org/abs/2610.02649.
