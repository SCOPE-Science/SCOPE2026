# Exact second-coordinate marginals and equivalence classes of rational Nevanlinna extremals

## Finding

Let \(\varphi\) be a nonconstant, real rational Herglotz--Nevanlinna function on the upper half-plane, written uniquely as
\[
\varphi(z)=a z+b+\sum_{j=1}^{N}\frac{r_j}{\tau_j-z},
\quad a\ge0,\quad b\in\mathbb R,\quad r_j>0,\quad \tau_j\in\mathbb R,
\]
with distinct poles, and either \(a>0\) or \(N\ge1\). Put \(\Gamma=\sum_{j=1}^{N}r_j\). Let \(\mu_\varphi\) denote the unique representing Nevanlinna measure of the two-variable function
\[
h_\varphi(z,w)=-\frac1{\varphi(z)+w-1/w},
\]
under the normalization of Fagrell--Luger [1]. That measure is extremal in the full positive cone of Nevanlinna measures by [1, Theorem 3.1]. Let \(P_1(t,y)=t\), \(P_2(t,y)=y\), \(J(y)=y-1/y\) for \(y\ne0\), and let \(\lambda\) denote Lebesgue measure on \(\mathbb R\).

**Theorem (complete marginal phase diagram).** The projections, as positive Borel measures (not assumed locally finite), satisfy
\[
(P_1)_*\mu_\varphi=\pi\lambda,
\]
and
\[
(P_2)_*\mu_\varphi=\begin{cases}
\displaystyle \frac\pi a\lambda,&a>0,\\
\displaystyle \pi\frac{\Gamma}{(b+J(y))^2}\,dy,&a=0\ \text{and}\ N\ge1.
\end{cases}
\]
The second density is understood away from its finitely many exceptional arguments; these points have no atoms. In the zero-slope case there are precisely two second-coordinate singular locations, the simple roots
\[
y_\pm=\frac{-b\pm\sqrt{b^2+4}}2
\]
of \(b+J(y)=0\). The second marginal is \(\sigma\)-finite but **not locally finite** at either location; for positive slope it is a constant multiple of Lebesgue measure and is locally finite.

Moreover, for two nonconstant rational Herglotz--Nevanlinna functions \(\varphi,\psi\), their ordered pairs of coordinate marginals agree **if and only if** either both have positive linear coefficients with \(a_\varphi=a_\psi\), or both have zero linear coefficients with \(b_\varphi=b_\psi\) and \(\Gamma_\varphi=\Gamma_\psi\). Whenever \(\varphi\ne\psi\), the underlying two-dimensional measures are mutually singular:
\[
\mu_\varphi\perp\mu_\psi.
\]
In particular, the functions \(\varphi_c(z)=z+(c-z)^{-1}\), \(c\in\mathbb R\), yield uncountably many mutually singular, nonlinear-supported, extreme Nevanlinna measures **with both marginals exactly \(\pi\lambda\)**. This is a statement about \(\sigma\)-finite measures, not probability couplings.

## Assumptions and scope

The representing-measure normalization and the assertion of extremality are taken from the full-text theorem of Fagrell--Luger [1], not re-proved here. Explicitly, their two-variable Herglotz representation has coefficient \(\pi^{-2}\) in front of the Nevanlinna-kernel integral. In their structure formula [1, Section 3.2], outside the finitely many real poles of \(\varphi\), the measure is
\[
\mu_\varphi=\pi\sum_{\epsilon\in\{+,-\}}
(t\mapsto(t,g_\epsilon(t)))_*(\alpha_\epsilon(t)\,dt),
\]
where
\[
g_\pm(t)=\frac{-\varphi(t)\pm\sqrt{\varphi(t)^2+4}}2,
\qquad
\alpha_\pm(t)=\frac{g_\pm(t)^2}{1+g_\pm(t)^2}.
\]
All formulas involving \(\varphi(t)\) exclude its finite pole set. No assertion is made for nonrational or constant functions \(\varphi\), or for arbitrary two-variable Nevanlinna measures outside this family. One-coordinate projection of an infinite, locally finite measure may fail to be locally finite, so all projection equalities concern Borel measures with values in \([0,\infty]\).

## Proof

**1. Exact first marginal.** The two roots \(g_\pm(t)\) solve \(y^2+\varphi(t)y-1=0\), hence \(g_+(t)g_-(t)=-1\). Since \(\alpha_\epsilon(t)=1/J'(g_\epsilon(t))\), where \(J'(y)=1+y^{-2}\), one has \(\alpha_+(t)+\alpha_-(t)=1\). The graph representation immediately gives \((P_1)_*\mu_\varphi=\pi\,dt\). This first-projection identity follows already from the identities established in [1]; the new classification concerns the second projection and cross-parameter equivalence.

**2. Inverse-branch Jacobian.** On every interval between poles of \(\varphi\),
\[
\varphi'(t)=a+\sum_{j=1}^{N}\frac{r_j}{(\tau_j-t)^2}>0.
\]
Both graphs are smooth on that interval. Their defining relation is \(J(g_\epsilon(t))=-\varphi(t)\), so implicit differentiation gives
\[
|g_\epsilon'(t)|=\frac{\varphi'(t)}{J'(g_\epsilon(t))}=\varphi'(t)\alpha_\epsilon(t).
\]
Consequently, changing variables from \(t\) to \(y\) in every monotonic graph piece yields, for every \(y\ne0\) outside the finite exceptional set,
\[
\frac{d(P_2)_*\mu_\varphi}{dy}(y)
=\pi\sum_{\substack{t\in\mathbb R:\ \varphi(t)=-J(y)}}\frac{1}{\varphi'(t)}. \tag{1}
\]
Each real solution enters exactly one of the two graphs (the positive one when \(y>0\), the negative one when \(y<0\)). Thus there is neither a missing multiplicity nor an extra Jacobian factor. Singletons of \(y\), including \(y=0\) and the exceptional roots, have zero projected mass: each graph is strictly monotone on every one of finitely many intervals, so its preimage of a point is finite, and the graph measure is absolutely continuous in \(t\).

**3. Evaluate the inverse-root trace exactly.** Define the monic polynomial \(Q(t)=\prod_{j=1}^{N}(t-\tau_j)\), with \(Q=1\) for \(N=0\), and set \(s=-J(y)\). The finite solutions of \(\varphi(t)=s\) are precisely the roots of
\[
F_s(t)=(a t+b-s)Q(t)-\sum_{j=1}^{N}r_j\frac{Q(t)}{t-\tau_j}.
\]
There is no spurious root at a pole because \(F_s(\tau_j)=-r_jQ'(\tau_j)\ne0\). For \(a>0\), strict monotonicity and the opposite infinite limits at endpoints give exactly \(N+1\) distinct real solutions for every \(s\in\mathbb R\). The leading two polynomial coefficients, followed by Vieta, yield
\[
\sum_{\varphi(t)=s}t=\sum_{j=1}^{N}\tau_j+\frac{s-b}{a}.
\]
Each inverse root is differentiable with derivative \(dt/ds=1/\varphi'(t)\). Differentiating the finite root sum therefore proves
\[
\sum_{\varphi(t)=s}\frac1{\varphi'(t)}=\frac1a.
\]
Combined with (1), this proves the constant-density case, independently of pole locations and residues.

For \(a=0\) and \(N\ge1\), fix \(s\ne b\). The polynomial \(F_s\) has degree \(N\), with exactly \(N\) distinct real roots: the \(N-1\) intervals between adjacent poles each contribute a root, and exactly one exterior interval contributes the last. Vieta now gives
\[
\sum_{\varphi(t)=s}t=\sum_{j=1}^{N}\tau_j+\frac{\Gamma}{b-s}.
\]
Differentiation yields \(\sum1/\varphi'(t)=\Gamma/(b-s)^2\). Substituting \(s=-J(y)\) gives the second displayed density. The special value \(s=b\) corresponds to one inverse branch escaping to infinity, not to a point mass of the projected measure, so the almost-everywhere density determines the measure completely.

**4. The sharp local-finiteness transition.** For \(a>0\) the density is the finite constant \(\pi/a\). For \(a=0\), \(J'(y)=1+y^{-2}>0\), and the equation \(b+J(y)=0\) has precisely the two nonzero simple real roots \(y_\pm\) stated above. Thus locally near either root,
\[
\frac{\pi\Gamma}{(b+J(y))^2}
\sim \frac{\pi\Gamma}{(1+y_\pm^{-2})^2(y-y_\pm)^2}.
\]
Its integral diverges on any interval containing that root. On the complement of these two points the density is finite and continuous, and the two-point set is null, proving \(\sigma\)-finiteness and non-local-finiteness exactly as asserted.

**5. Classify common marginal pairs.** Every first marginal is \(\pi\lambda\). In the positive-slope family, equality of second marginals is equivalent to equality of \(a\). A zero-slope marginal has nonlocally finite neighborhoods and cannot coincide with any positive-slope marginal. Within the zero-slope family, \(J\) maps each of \((0,\infty)\) and \(( -\infty,0)\) bijectively onto \(\mathbb R\). Hence equality of the densities is the rational identity \(\Gamma/(b-s)^2=\Gamma'/(b'-s)^2\) in real \(s\). Equality of poles forces \(b=b'\), then equality of numerators forces \(\Gamma=\Gamma'\). The converse in each case follows from the density formulas.

**6. Mutual singularity and fibers.** Define the full-measure graph set \(E_\varphi=\{(t,y):t\ \text{is not a pole of}\ \varphi,\ y\ne0,\ \varphi(t)+J(y)=0\}\). If \(\varphi\ne\psi\) are rational functions, then \(\varphi(t)=\psi(t)\) at only finitely many finite real values \(t\), and these values have zero mass under the first marginal \(\pi\lambda\). Hence \(\mu_\varphi(E_\varphi^c)=0\) and \(\mu_\psi(E_\varphi)=0\), proving \(\mu_\varphi\perp\mu_\psi\). For \(\varphi_c(z)=z+1/(c-z)\) the slope is always \(1\), while distinct \(c\) give distinct rational functions. The positive supporting branch satisfies \(g_+(t)>0\) and \(g_+(t)\to0\) as \(t\to+\infty\); it cannot be an affine line. Thus the common-marginal continuum genuinely contains curved support, not merely affine graph rearrangements. The family \(\varphi_c(z)=1/(c-z)\) similarly supplies continuum-sized mutually singular fibers on the zero-slope side, all with \(b=0\), \(\Gamma=1\).

## Verification

The decisive steps are analytic and finite-parameter exact: (1) the source graph weights; (2) the inverse-graph Jacobian cancellation; (3) Vieta applied in the \(t\)-variable rather than the \(y\)-variable; and (4) the rational pole comparison for complete marginal equivalence. The included standalone `CHECK.py` (standard library only) numerically verifies the identity \(\sum_{\varphi(t)=s}1/\varphi'(t)=1/a\) for positive slopes and \(\Gamma/(b-s)^2\) for zero slope at fifteen nonexceptional sample pairs. Its successful run is a consistency check only; it does not replace the proof for arbitrary pole counts and real parameters. Execute with `python3 CHECK.py`.

## Relationship to prior work

Fagrell--Luger [1, Theorem 3.1 and equations (20)--(24)] proves the extremality of the two-graph measures and computes their weights, including the identity that immediately gives the first marginal. Their text does not identify or classify second-coordinate marginals, the slope-zero non-local-finiteness transition, or the equivalence classes of different parameters under the two projections. The present statement does not claim their structure formula or extremality as new. Nedic--Saksman [2, Section 3] classifies measures supported on hyperplanes (including their extremal densities), a different support geometry; it does not provide the inverse-root trace of this nonlinear two-graph family. Anderson--Bergqvist--Bickel--Cima--Sola [3] gives a general two-torus Clark-measure structure formula under Cayley-related geometry, but its stated results are weight and support formulas, not the specific rational-family two-projection equivalence theorem above. These are substantive mathematical comparisons, not proofs of universal literature uniqueness.

## Limitations

The classification concerns exactly the one-variable real rational input family of [1], not every extreme Nevanlinna measure, and does not generalize the marginal formula to arbitrary nonrational Pick functions. Extremality is a published input, while the marginal equivalence theorem is proved here. The two marginals do not reconstruct the joint measure: in fact the fibers can contain mutually singular continuum families. In the zero-slope regime the second marginal is not Radon despite the original planar measure being locally finite; the indicated density has no atoms even where it diverges. Earlier analyses of two-variable Clark measures could contain equivalent formulations not exposed by accessible indexing; no independent external audit has yet been performed.

## References

[1] L. Fagrell and A. Luger, *Real rational Herglotz-Nevanlinna functions in two variables and a class of extremals*, arXiv:2610.02476v1 (first public posting 2026-10-01), especially Theorem 3.1, equations (20)--(24), and Proposition 3.4. https://arxiv.org/abs/2610.02476

[2] M. Nedic and E. Saksman, *On the structure of Nevanlinna measures*, Mathematische Nachrichten 297 (2024), 2488--2516, particularly Theorem 3.7 and Corollary 3.9. https://doi.org/10.1002/mana.202200135

[3] J. T. Anderson, L. Bergqvist, K. Bickel, J. A. Cima and A. A. Sola, *Clark measures for rational inner functions II: General bidegrees and higher dimensions*, arXiv:2303.11248v1 (2023), especially Sections 1 and 3. https://arxiv.org/abs/2303.11248
