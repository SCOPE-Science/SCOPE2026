# All-vector Lévy measures and measure tomography in bidisc Dirichlet spaces

## Statement

Let
\[
H=\mathcal D(\rho^{(1)},\rho^{(2)})
\]
be the Dirichlet-type space on the bidisc associated with finite positive Borel
measures \(\rho^{(1)},\rho^{(2)}\) on \(\overline{\mathbb D}\), and let
\(\mathscr M_z=(M_1,M_2)\) be the coordinate-multiplication pair.  Write \(m\)
for normalized Haar measure on \(\mathbb T\) and
\[
S:\overline{\mathbb D}\to[0,1],\qquad S(a)=|a|^2.
\]

There are bounded linear trace maps
\[
\Gamma_1:H\longrightarrow
L^2(\overline{\mathbb D}\times\mathbb T,\rho^{(1)}\otimes m),
\qquad
\Gamma_2:H\longrightarrow
L^2(\mathbb T\times\overline{\mathbb D},m\otimes\rho^{(2)})
\]
uniquely determined on polynomials by
\[
(\Gamma_1p)(a,\zeta)=p(a,\zeta),\qquad
(\Gamma_2p)(\zeta,a)=p(\zeta,a).
\]
They satisfy, for every \(h\in H\),
\[
\|\Gamma_i h\|_2^2=\|M_i h\|_H^2-\|h\|_H^2,
\]
and the intertwining relations
\[
\Gamma_1M_1=M_a\Gamma_1,\qquad
\Gamma_2M_2=M_a\Gamma_2,
\]
where \(M_a\) denotes multiplication by the \(\overline{\mathbb D}\)-coordinate.

For \(h\in H\), define finite positive measures on \(\overline{\mathbb D}\) by
\[
\eta_{1,h}(E)
=
\int_{E\times\mathbb T}|\Gamma_1h(a,\zeta)|^2\,
d\rho^{(1)}(a)\,dm(\zeta),
\]
\[
\eta_{2,h}(E)
=
\int_{\mathbb T\times E}|\Gamma_2h(\zeta,a)|^2\,
dm(\zeta)\,d\rho^{(2)}(a),
\]
and put
\[
\mu_{i,h}=S_*\eta_{i,h}.
\]
Then \(\mu_{i,h}\) is exactly the Hausdorff representing measure of the
forward-difference sequence
\[
\|M_i^{n+1}h\|_H^2-\|M_i^nh\|_H^2,\qquad n\ge0.
\]
Equivalently,
\[
\|M_i^{n+1}h\|_H^2-\|M_i^nh\|_H^2
=
\int_{[0,1]}t^n\,d\mu_{i,h}(t).
\]

Define
\[
d\lambda_{i,h}(t)
=
\mathbf 1_{[0,1)}(t)\frac{1}{1-t}\,d\mu_{i,h}(t),
\qquad
\beta_i(h)=\mu_{i,h}(\{1\}).
\]
Then the complete Lévy--Khinchin data of \((\mathscr M_z,h)\) are
\[
\boxed{
\nu_{(\mathscr M_z,h)}
=
\lambda_{1,h}\times\delta_1+
\delta_1\times\lambda_{2,h}
}
\]
and
\[
\boxed{
b_{(\mathscr M_z,h)}(\alpha_1,\alpha_2)
=
\alpha_1\beta_1(h)+\alpha_2\beta_2(h).
}
\]
Thus Question 1.3 of Bera--Sequeira, arXiv:2609.20346v1, has an explicit
answer for every vector \(h\), not only for the cyclic vector \(1\).

## Polynomial formula

For a polynomial \(p\), the trace maps are literal restrictions, so
\[
d\eta_{1,p}(a)
=
\left(\int_{\mathbb T}|p(a,\zeta)|^2\,dm(\zeta)\right)d\rho^{(1)}(a),
\]
\[
d\eta_{2,p}(a)
=
\left(\int_{\mathbb T}|p(\zeta,a)|^2\,dm(\zeta)\right)d\rho^{(2)}(a).
\]
Consequently, if
\[
w_{1,p}(a)=\int_{\mathbb T}|p(a,\zeta)|^2\,dm(\zeta),\qquad
w_{2,p}(a)=\int_{\mathbb T}|p(\zeta,a)|^2\,dm(\zeta),
\]
then
\[
\mu_{i,p}=S_*(w_{i,p}\rho^{(i)}).
\]

In particular, for \(p(z)=z_1^mz_2^n\),
\[
d\nu_{(\mathscr M_z,p)}(x)
=
\mathbf 1_{\{x_1<1\}}\frac{x_1^m}{1-x_1}\,
d\big((S_*\rho^{(1)})\times\delta_1\big)(x)
+
\mathbf 1_{\{x_2<1\}}\frac{x_2^n}{1-x_2}\,
d\big(\delta_1\times(S_*\rho^{(2)})\big)(x).
\]
The case \(m=n=0\) is the formula proved in Theorem 1.4 of
arXiv:2609.20346v1.

## A sharp information boundary and a countable tomography theorem

The vector \(h=1\) sees only the radial pushforwards \(S_*\rho^{(i)}\).
Nonconstant vectors recover angular information.

More precisely, for each coordinate \(i\), consider the countable family
\[
\mathcal P_i=
\{1\}\cup
\{\,1+z_i^k,\ 1-i z_i^k: k\ge1\,\}.
\]
The Lévy measures
\[
\{\nu_{(\mathscr M_z,p)}:p\in\mathcal P_i\}
\]
determine the interior part
\[
\rho^{(i)}\!\restriction_{\mathbb D}
\]
uniquely.  The corresponding drift values
\[
\{b_{(\mathscr M_z,p)}(e_i):p\in\mathcal P_i\}
\]
determine the boundary part
\[
\rho^{(i)}\!\restriction_{\mathbb T}
\]
uniquely.  Hence the full Lévy triples for the countable probe family
\(\mathcal P_1\cup\mathcal P_2\) determine both defining measures
\(\rho^{(1)},\rho^{(2)}\).

This also identifies the exact information loss in the Lévy measure alone:
for polynomial probes, mass of \(\rho^{(i)}\) on \(\mathbb T\) is sent to the
atom \(t=1\) of the forward-difference representing measure and therefore
appears in the drift, not in the Lévy measure.

### Proof of tomography

Fix one coordinate and abbreviate \(\rho=\rho^{(i)}\).
From the corresponding face of the Lévy measure one recovers
\[
\mu_p\!\restriction_{[0,1)}
=
(1-t)\lambda_p(dt)
=
S_*\big(|p|^2\,\rho\!\restriction_{\mathbb D}\big)
\]
for all one-variable probes \(p\in\mathcal P_i\).
Let
\[
\sigma_0=S_*(\rho\!\restriction_{\mathbb D}),
\qquad
\sigma_k=S_*(a^k\,\rho\!\restriction_{\mathbb D}),\quad k\ge1,
\]
where \(\sigma_k\) is a finite complex measure on \([0,1)\).
The identities
\[
|1+a^k|^2=1+|a|^{2k}+2\operatorname{Re}(a^k),
\]
\[
|1-i a^k|^2=1+|a|^{2k}+2\operatorname{Im}(a^k)
\]
show that the data from \(1,1+z_i^k,1-i z_i^k\) recover
\(\operatorname{Re}\sigma_k\) and \(\operatorname{Im}\sigma_k\), hence
\(\sigma_k\), for every \(k\ge1\).

Disintegrate \(\rho\!\restriction_{\mathbb D}\) over
\(t=|a|^2\).  For \(\sigma_0\)-almost every \(t>0\), let
\(\kappa_t\) be the conditional probability measure on the circle
\(\{|a|=\sqrt t\}\), identified with \(\mathbb T\).  Then
\[
\frac{d\sigma_k}{d\sigma_0}(t)
=
t^{k/2}\int_{\mathbb T}\zeta^k\,d\kappa_t(\zeta).
\]
Thus the recovered measures \(\sigma_k\) give all Fourier coefficients of
\(\kappa_t\) for almost every \(t>0\).  Fourier uniqueness on \(\mathbb T\)
determines \(\kappa_t\); the fiber \(t=0\) consists only of the origin and is
already determined by \(\sigma_0\).  Hence the interior measure is recovered.

For the boundary part, the drift values are
\[
b_{(\mathscr M_z,p)}(e_i)
=
\int_{\mathbb T}|p(\zeta)|^2\,d\rho(\zeta).
\]
Using the same probes gives the real and imaginary parts of all Fourier
coefficients \(\int_{\mathbb T}\zeta^k\,d\rho(\zeta)\).  Fourier uniqueness
therefore recovers \(\rho\!\restriction_{\mathbb T}\).

## Angular sensitivity already at one interior atom

Fix \(0<r<1\), take \(\rho^{(2)}=0\), and compare
\[
\rho^{(1)}_+=\delta_r,\qquad
\rho^{(1)}_-=\delta_{-r}.
\]
They have the same radial pushforward
\[
S_*\rho^{(1)}_+=S_*\rho^{(1)}_-=\delta_{r^2},
\]
so Theorem 1.4 of arXiv:2609.20346v1 gives the same Lévy measure for
\(h=1\).  But for the polynomial \(h(z)=1+z_1\), the first-face Lévy atom at
\((r^2,1)\) has weight
\[
\frac{(1+r)^2}{1-r^2}
\]
for \(\rho^{(1)}_+\), and
\[
\frac{(1-r)^2}{1-r^2}
\]
for \(\rho^{(1)}_-\).
Hence the radial pushforward alone cannot determine the arbitrary-vector
Lévy measure.

## Proof of the all-vector formula

Bera, *New York J. Math.* 32 (2026), equation (31), proves for every
two-variable polynomial \(p\)
\[
\|M_1p\|_H^2-\|p\|_H^2
=
\int_{\overline{\mathbb D}\times\mathbb T}|p(a,\zeta)|^2\,
d\rho^{(1)}(a)\,dm(\zeta),
\]
with the analogous formula for \(M_2\).  Since \(M_i\) is bounded,
\[
\|\Gamma_i p\|_2^2
\le
\|M_i^*M_i-I\|\,\|p\|_H^2.
\]
Polynomials are dense in \(H\), so the literal restriction maps extend
uniquely to bounded maps \(\Gamma_i\).  The norm identity survives by
continuity.  The polynomial identity
\[
\Gamma_iM_i=M_a\Gamma_i
\]
also extends by continuity.

Therefore
\[
\begin{aligned}
\|M_i^{n+1}h\|_H^2-\|M_i^nh\|_H^2
&=\|\Gamma_iM_i^nh\|_2^2\\
&=\int_{\overline{\mathbb D}}|a|^{2n}\,d\eta_{i,h}(a)\\
&=\int_{[0,1]}t^n\,d(S_*\eta_{i,h})(t).
\end{aligned}
\]
Hausdorff uniqueness identifies \(S_*\eta_{i,h}\) with the representing
measure of the forward difference.  In one variable, the
Lévy--Khinchin relation is
\[
d\mu(t)=(1-t)d\nu(t)\quad (0\le t<1),
\qquad
b(1)=\mu(\{1\}).
\]
This yields \(\lambda_{i,h}\) and \(\beta_i(h)\) above.

Finally, \(\mathscr M_z\) has vanishing pair defect.  Theorem 2.4 of
Bera--Sequeira proves that for every vector \(h\), vanishing pair defect is
equivalent to the joint Lévy measure being the sum of the coordinate face
measures.  This gives the asserted joint formula and the additive drift.

## Context and originality boundary

Bera--Sequeira, arXiv:2609.20346v1, explicitly asks in Question 1.3 how
\(\nu_{(\mathscr M_z,h)}\) for arbitrary \(h\) is related to the defining
measures, but its stated main theorem and Section 3 computation specialize
to \(h=1\).  Their Theorem 2.4 supplies the abstract face decomposition for
all \(h\).  Bera's 2026 model paper supplies the polynomial defect identity
used above.  The earlier Bera--Chavan--Ghara bidisc paper contains the
boundary-measure predecessor of this defect formula.

Accordingly, neither the defect identity, the zero-defect face
decomposition, the Hausdorff moment theorem, nor Fourier uniqueness is
claimed as new.  The contribution here is their all-vector synthesis into
an explicit bounded trace-map formula, the polynomial weighted-pushforward
specialization, the exact separation of interior information into the
Lévy part and boundary information into the drift, and the countable
tomography consequence answering the current arbitrary-vector question.

Originality is to the best of our knowledge.  Older one-variable
completely-hyperexpansive model literature may contain equivalent trace or
operator-valued measure formulations under different terminology; no source
located in the literature search stated the all-vector bidisc formula or the
countable tomography/information-boundary consequences above.

## Limitations

The trace maps for a general \(h\in H\) are \(L^2\)-boundary/interior traces
defined by completion; no pointwise boundary values are asserted.
The tomography statement uses a countable family of polynomial probes, not
a single vector.  Lévy measures alone do not recover boundary-supported
defining mass; the drift is essential there.  No claim is made here for
Dirichlet-type spaces on higher polydiscs or for completely hyperexpansive
tuples lacking the vanishing pair-defect hypothesis.

## References

1. S. Bera and S. S. Sequeira, *Lévy measures for Dirichlet-type spaces on
   the unit bidisc*, arXiv:2609.20346v1 (2026).
   https://arxiv.org/abs/2609.20346
2. S. Bera, *Dirichlet-type spaces of the unit bidisc and toral completely
   hyperexpansive operators*, New York J. Math. 32 (2026), 99--117.
   https://nyjm.albany.edu/j/2026/32-4.html
3. S. Bera, S. Chavan and S. Ghara, *Dirichlet-type spaces of the unit
   bidisc and toral 2-isometries*, Canad. J. Math. 77 (2025), 1271--1293.
   https://doi.org/10.4153/S0008414X24000300
4. A. Athavale and V. M. Sholapurkar, *Completely hyperexpansive operator
   tuples*, Positivity 3 (1999), 245--257.
   https://doi.org/10.1023/A:1009719803199
