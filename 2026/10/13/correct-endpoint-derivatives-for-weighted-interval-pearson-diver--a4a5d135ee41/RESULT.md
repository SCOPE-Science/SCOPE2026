# Correct endpoint derivatives for weighted interval Pearson divergence
## Finding
Let \(0<a<b<\infty\). For two nonnegative absolutely continuous distributions with densities \(f,g\) and distribution functions \(F,G\), define
\[
\Delta_F=F(b)-F(a),\qquad \Delta_G=G(b)-G(a),
\]
and the conditional densities on \((a,b)\)
\[
p(x)=\frac{f(x)}{\Delta_F},\qquad q(x)=\frac{g(x)}{\Delta_G}.
\]
The weighted interval Pearson divergence considered by Akila and Moharana is
\[
D(a,b)=\int_a^b xq(x)\left(1-\frac{p(x)}{q(x)}\right)^2\,dx.
\]
Write
\[
\mu_X=\int_a^b xp(x)\,dx,\qquad \mu_Y=\int_a^b xq(x)\,dx,
\]
with endpoint generalized failure rates
\[
h_{1X}=p(a),\quad h_{1Y}=q(a),\quad h_{2X}=p(b),\quad h_{2Y}=q(b).
\]
Whenever the indicated endpoint values and differentiations exist and \(q(a),q(b)>0\), the correct endpoint identities are
\[
\frac{\partial D}{\partial a}=(2h_{1X}-h_{1Y})D+2(h_{1X}-h_{1Y})(\mu_X-\mu_Y)-a\frac{(h_{1X}-h_{1Y})^2}{h_{1Y}},
\]
and
\[
\frac{\partial D}{\partial b}=(h_{2Y}-2h_{2X})D+2(h_{2Y}-h_{2X})(\mu_X-\mu_Y)+b\frac{(h_{2X}-h_{2Y})^2}{h_{2Y}}.
\]
Equations (14) and (15) in the 2026 article are therefore incorrect as stated.

## Assumptions and scope
The claim concerns the weight \(w(x)=x\) used in the cited article. It assumes \(0<a<b<\infty\), positive truncation masses \(\Delta_F,\Delta_G\), positive \(q(a),q(b)\), and sufficient regularity for Leibniz differentiation. No assertion is made about endpoint cases where these quantities are undefined.

The conclusion about later results is deliberately limited: when a proof explicitly uses equations (14) or (15), that published proof route is not valid until the calculation is replaced by the correct identities. The present result does not by itself prove that every theorem depending on those equations has a false conclusion.

## Proof
Expand the divergence as
\[
D=\mu_Y-2\mu_X+A,\qquad A=\int_a^b x\frac{p(x)^2}{q(x)}\,dx.
\]
For the lower endpoint, normalization gives
\[
\frac{\partial p(x)}{\partial a}=h_{1X}p(x),\qquad
\frac{\partial q(x)}{\partial a}=h_{1Y}q(x).
\]
Hence
\[
\frac{\partial\mu_X}{\partial a}=h_{1X}(\mu_X-a),\qquad
\frac{\partial\mu_Y}{\partial a}=h_{1Y}(\mu_Y-a),
\]
and Leibniz differentiation yields
\[
\frac{\partial A}{\partial a}=(2h_{1X}-h_{1Y})A-a\frac{h_{1X}^2}{h_{1Y}}.
\]
Substituting \(A=D-\mu_Y+2\mu_X\) and collecting terms gives
\[
\frac{\partial D}{\partial a}=(2h_{1X}-h_{1Y})D+2(h_{1X}-h_{1Y})(\mu_X-\mu_Y)-a\frac{(h_{1X}-h_{1Y})^2}{h_{1Y}}.
\]

For the upper endpoint,
\[
\frac{\partial p(x)}{\partial b}=-h_{2X}p(x),\qquad
\frac{\partial q(x)}{\partial b}=-h_{2Y}q(x),
\]
so
\[
\frac{\partial\mu_X}{\partial b}=h_{2X}(b-\mu_X),\qquad
\frac{\partial\mu_Y}{\partial b}=h_{2Y}(b-\mu_Y),
\]
and
\[
\frac{\partial A}{\partial b}=(h_{2Y}-2h_{2X})A+b\frac{h_{2X}^2}{h_{2Y}}.
\]
Again substituting \(A=D-\mu_Y+2\mu_X\) gives
\[
\frac{\partial D}{\partial b}=(h_{2Y}-2h_{2X})D+2(h_{2Y}-h_{2X})(\mu_X-\mu_Y)+b\frac{(h_{2X}-h_{2Y})^2}{h_{2Y}}.
\]

There is also an immediate exact stress test. If \(X=Y\), then \(p=q\), \(D\equiv0\), \(\mu_X=\mu_Y\), and corresponding endpoint rates agree. Both corrected derivatives are therefore zero. By contrast, the published equations (14) and (15) reduce respectively to
\[
h_1(1-a),\qquad h_2(b-1),
\]
which are nonzero for generic \(a,b\) whenever the common endpoint density is positive. For example, any common exponential law with \(a=1/2\) and \(b=2\) gives a contradiction to the published identities.

## Verification
A supplementary checker evaluates the defining integral for two unequal exponential laws, evaluates the corrected analytic derivatives, and compares them against centered finite differences. At \(\lambda_X=1.3\), \(\lambda_Y=0.7\), \(a=0.5\), and \(b=2\), it obtains
\[
D\approx0.0685069764342913,
\]
\[
\frac{\partial D}{\partial a}\approx-0.0438771832996392,
\qquad
\frac{\partial D}{\partial b}\approx0.101706512193270.
\]
Centered finite differences agree to better than \(10^{-10}\) in the checker. This numerical replay is supplementary only; the proof above is symbolic.

## Relationship to prior work
Akila and Moharana define the weighted interval Pearson divergence in equation (5), introduce the endpoint generalized failure rates and generalized conditional means in equations (9)--(13), and print endpoint derivative formulas as equations (14) and (15). Their proofs of Theorems 2.4 and 2.5 substitute these formulas directly, Theorem 2.6 explicitly simplifies equation (14), Theorem 2.7 refers to the same reasoning, and Theorem 3.1 states that its bounds are deduced from equations (14) and (15).

The authors' 2025 predecessor gives the corresponding unweighted endpoint derivative formulas. Those formulas are consistent with the corrected calculation: when the weight is constant, the conditional weighted means coincide and the extra moment term collapses, recovering the unweighted identities. The 2019 weighted Kullback--Leibler paper concerns a different divergence; its endpoint calculus contains conditional-moment terms, but it does not state the Pearson correction proved here.

Focused searches for the exact 2026 article, its DOI, endpoint-derivative corrections, doubly truncated weighted Pearson divergence, generalized failure-rate formulations, and broader weighted-divergence endpoint calculus located no published correction or equivalent statement covering the identities above.

## Limitations
The result is a correction of two analytic identities and of proof routes that rely on them. It does not re-prove or refute every later theorem in the 2026 article. A later corrigendum or an equivalent formula in literature not surfaced by the searches could reduce originality; none was located in the checked sources.

## References
P. Akila and R. Moharana, “On weighted interval Pearson \(\chi^2\)-divergence measure,” Journal of Dynamics and Games, early access 25 June 2026, DOI 10.3934/jdg.2026044.

P. Akila and R. Moharana, “The Pearson \(\chi^2\)-Divergence Measure for Doubly Truncated Random Variables,” IEEE Access 13 (2025), 88905--88916, DOI 10.1109/ACCESS.2025.3571188.

R. Moharana and S. Kayal, “On Weighted Kullback--Leibler Divergence for Doubly Truncated Random Variables,” REVSTAT Statistical Journal 17(3) (2019), 297--320, DOI 10.57805/revstat.v17i3.269.
