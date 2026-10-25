# A sharp sign transition for nested zero counts in the hyperbolic Gaussian analytic function

## Finding

Let \(f_L(z)=\sum_{n\ge0}\sqrt{\Gamma(n+L)/(n!\Gamma(L))}\,\xi_n z^n\) be the hyperbolic Gaussian analytic function, where \(L>1\) and the \(\xi_n\) are independent standard circular complex Gaussians. Write \(N_L(r)\) for its number of zeros in \(\{|z|<r\}\), counted with multiplicity. For fixed \(\alpha,\beta>0\), put \(p=\alpha+\beta\) and \(v=|\alpha-\beta|/p\). Then

\[
\lim_{\epsilon\downarrow0}\epsilon\,\operatorname{Cov}\left(N_L(1-\alpha\epsilon),N_L(1-\beta\epsilon)\right)
=H_L(\alpha,\beta),
\]
\[
H_L(\alpha,\beta)=\frac{1}{4\sqrt\pi\,p}\sum_{k=1}^{\infty}\frac{L}{k}\frac{\Gamma(Lk-\tfrac12)}{\Gamma(Lk)}(1-v^2)^{Lk-1}\bigl[1-(2Lk-1)v^2\bigr]. \tag{1}
\]

The series is absolutely convergent. Its value is strictly positive at \(v=0\), while it is strictly negative whenever \(v^2\ge 1/(2L-1)\). In particular, sufficiently separated *nested* hyperbolic Gaussian zero counts can have **negative covariance** for every \(L>1\).

When \(L=2\), the complete sign diagram admits an elementary closed form:
\[
H_2(\alpha,\beta)=\frac{2}{p(1-v^2)}\left(1+v^2-v-\frac{1}{\sqrt{2-v^2}}\right). \tag{2}
\]
There is exactly one threshold \(v_*\in(0,1)\), the unique positive root of
\[
v_*^4+2v_*-1=0,\qquad v_*=0.4746266175626055503294\ldots, \tag{3}
\]
such that \(H_2>0\) for \(0\le v<v_*\), \(H_2=0\) for \(v=v_*\), and \(H_2<0\) for \(v_*<v<1\). In terms of the ratio of the two distances to the unit circle, the exact transition is
\[
\frac{\min(\alpha,\beta)}{\max(\alpha,\beta)}=\frac{1-v_*}{1+v_*}=0.35627553183990293999\ldots. \tag{4}
\]
For each fixed pair on either strict side of this threshold, the *finite-radius* covariance has the same sign for all sufficiently small positive \(\epsilon\).

## Assumptions and scope

The covariance kernel of \(f_L\) is \(\mathbb E[f_L(z)\overline{f_L(w)}]=(1-z\overline w)^{-L}\), and \(N_L(r)\) counts its zeros in a centered Euclidean disk within the unit disk. The boundary limit concerns \(r_\epsilon=1-\alpha\epsilon\) and \(s_\epsilon=1-\beta\epsilon\) with fixed strictly positive \(\alpha,\beta\) as \(\epsilon\downarrow0\). Equation (1) holds for every real \(L>1\), including equal radii. The claimed unique sign crossing, explicit quartic and precise critical boundary-gap ratio are for \(L=2\) only. The point \(v=1\) is not included, because it would require one distance parameter to vanish. All limits concern expectations/covariances; no almost-sure convergence is asserted.

## Proof

**Gaussian logarithms and Jensen circles.** Set \(J_L(r)=(2\pi)^{-1}\int_0^{2\pi}\log|f_L(re^{i\theta})|\,d\theta\). Jensen's formula gives \(N_L(r)=rJ_L'(r)\) for every radius avoiding a zero on its circle. The normalized complex-Gaussian logarithm identity gives
\[
\operatorname{Cov}(\log|Z|,\log|W|)=\tfrac14\operatorname{Li}_2(|\operatorname{Corr}(Z,W)|^2).
\]
Consequently, with
\[
Q(r,s,\theta)=\frac{(1-r^2)(1-s^2)}{1+r^2s^2-2rs\cos\theta},
\]
\[
\operatorname{Cov}(J_L(r),J_L(s))=\frac1{8\pi}\int_{-\pi}^{\pi}\operatorname{Li}_2\left(Q(r,s,\theta)^L\right)\,d\theta, \quad
\operatorname{Cov}(N_L(r),N_L(s))=rs\,\partial_r\partial_s\operatorname{Cov}(J_L(r),J_L(s)). \tag{5}
\]
For unequal radii, the logarithm correlation stays strictly below one uniformly in \(\theta\), so differentiation under the integral is classical.

**Boundary scaling and controlled derivatives.** Put \(r=1-\alpha\epsilon\), \(s=1-\beta\epsilon\) and \(\theta=\epsilon p t\). Then
\[
Q(r,s,\epsilon pt)\longrightarrow\frac{1-v^2}{1+t^2}.
\]
If \(\alpha\ne\beta\), restrict \((\alpha,\beta)\) to a compact neighborhood away from equality and zero. There \(Q\) is bounded uniformly below one, and each scaled mixed radial derivative of the integrand in (5) is bounded by an integrable linear combination of \((1+t^2)^{-L}\), \((1+t^2)^{-L-1}\), and \((1+t^2)^{-L-2}\). Here \(L>1\) ensures domination (in fact a wider range suffices). The tails \(|\theta|\ge\delta\) contribute \(o(\epsilon^{-1})\) to the differentiated covariance. Thus dominated convergence applies directly to the mixed derivative, not merely to an undifferentiated asymptotic expansion. Define
\[
I_L(v)=\int_{\mathbb R}\operatorname{Li}_2\left(\left(\frac{1-v^2}{1+t^2}\right)^L\right)dt.
\]
The leading circle-log covariance is \(\epsilon p I_L(v)/(8\pi)\), and the controlled mixed derivative in (5) gives
\[
\lim_{\epsilon\downarrow0}\epsilon\operatorname{Cov}(N_L(1-\alpha\epsilon),N_L(1-\beta\epsilon))=
\frac1{8\pi}\partial_\alpha\partial_\beta\bigl[pI_L(v)\bigr]
=-\frac{1-v^2}{8\pi p}I_L''(v). \tag{6}
\]
Here one can initially use the signed variable \((\alpha-\beta)/p\); evenness of \(I_L\) gives the displayed formula for \(v\ge0\).

**The convergent series.** Expand \(\operatorname{Li}_2(x)=\sum_{k\ge1}x^k/k^2\). Positivity of terms and the beta integral yield
\[
I_L(v)=\sqrt\pi\sum_{k=1}^{\infty}\frac{\Gamma(Lk-\tfrac12)}{k^2\Gamma(Lk)}(1-v^2)^{Lk}.
\]
Its second derivative converges locally uniformly for \(0\le v<1\) (at \(v=0\), the relevant summands are \(O(k^{-3/2})\)). Substitution into (6) proves (1) whenever \(\alpha\ne\beta\). If \(\alpha=\beta\), apply the known one-radius hyperbolic Gaussian variance asymptotic from Buckley (2013): its coefficient matches (1) at \(v=0\), by the same gamma series. Thus (1) also covers equal radii. At \(v=0\) each summand is positive. For \(L>1\) and \(v^2\ge 1/(2L-1)\), all square-bracket factors in (1) are nonpositive and those for \(k\ge2\) are strictly negative, proving the general signed claim.

**Elementary evaluation at intensity two.** Write \(q=1-v^2\). An elementary binomial-series summation gives
\[
\sum_{k\ge1}\frac{\Gamma(2k-\tfrac12)}{k\Gamma(2k)}z^k=2\sqrt\pi\left(2-\sqrt{1-\sqrt z}-\sqrt{1+\sqrt z}\right),\qquad 0\le z<1. \tag{7}
\]
Differentiate (7), set \(z=q^2\), and substitute the resulting series and derivative into (1). The radical terms simplify to (2) for \(v>0\), and continuity supplies \(v=0\). In particular, \(H_2(\alpha,\alpha)=(1-1/\sqrt2)/\alpha\), consistent with Buckley's exact variance.

**Unique sign crossing.** The prefactor in (2) is positive, as is \(1+v^2-v\). The identity
\[
(1+v^2-v)^2(2-v^2)-1=-(1-v)^2(v^4+2v-1) \tag{8}
\]
shows that the sign of the parenthesis in (2) is the sign of \(1-2v-v^4\). This polynomial is strictly decreasing on \([0,1]\), changes sign between its endpoints, and has only one zero. This proves (3)–(4), including the sign classification. Pointwise convergence in (1) then transfers either strict sign to all sufficiently small positive \(\epsilon\).

## Verification

An included standalone Python checker evaluates the exact finite-radius, doubly differentiated dilogarithmic integral, the convergent boundary series and the elementary closed form separately. It checks the quartic factorization and isolates the unique positive root, compares finite-radius boundary rescalings at three values of \(\epsilon\), tests the general-intensity sign prediction, and checks the determinantal intensity-one covariance and Buckley's intensity-two variance formula. On Python with SciPy and SymPy it reports **43 passing numerical and symbolic assertions**. These tests corroborate but do not replace the analytic proof. Run locally as `python check_hyperbolic_covariance.py`.

## Relationship to prior work

Buckley (2013, arXiv:1307.6674) established the one-disk zero-count variance of the same hyperbolic GAF, including an exact formula at \(L=2\), and records the Gaussian-logarithm identity used here. Buckley and Nishry (2021, arXiv:2104.12598) study single-disk limit laws and fluctuations, not the claimed two-disk boundary-layer covariance sign diagram. Their methods and fixed-radius formulas provide context and ingredients but do not directly state (2)–(4). The Peres–Virág intensity-one case has determinantal positive nested-disk covariance, demonstrating the structural distinction. Related work on large deviations for hyperbolic Gaussian zeros concerns one-disk tails, not this sharp cross-covariance threshold. Independently recorded research on planar Gaussian entire-function two-disk covariance concerns a different kernel and different scaling and does not imply this hyperbolic sign law.

## Limitations

This theorem does not assert a sign formula at finite radii for every \(r,s\), nor the finite-radius sign when the leading coefficient is zero at \(v=v_*\). No uniqueness of a sign crossing is claimed for general \(L>1\). The asymptotic concerns fixed positive \(\alpha,\beta\) and does not cover a parameter tending to zero along with \(\epsilon\). Although the compared sources did not state the quartic threshold, an equivalent extraction from more general pair-correlation or variance machinery is a residual historical-priority risk. Independent mathematical audit has not been performed.

## References

1. Jeremiah Buckley, *Fluctuations in the zero set of the hyperbolic Gaussian analytic function*, arXiv:1307.6674 (first public 2013-07-25), especially the Gaussian logarithm identity and the disk variance formula.
2. Jeremiah Buckley and Alon Nishry, *Gaussian complex zeroes are not always normal: limit theorems on the disc*, arXiv:2104.12598 (first public 2021-04-26), especially the introductory definition of the hyperbolic GAF and single-radius limit theorems.
3. Keren Mor Waknin, *Overcrowding for zeros of hyperbolic Gaussian analytic functions*, arXiv:2209.05854 (first public 2022-09-13), on a different single-disk fluctuation question.
4. Yuval Peres and Bálint Virág, *Zeros of the i.i.d. Gaussian power series: a conformally invariant determinantal process*, Acta Math. 194 (2005), 1–35, concerning the distinct intensity-one determinantal case.
