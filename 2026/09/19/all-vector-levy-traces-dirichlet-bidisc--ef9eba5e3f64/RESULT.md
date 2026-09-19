# All-vector Levy measures and measure tomography in bidisc Dirichlet spaces

## Theorem

Let
\[
H=\mathcal D(\rho^{(1)},\rho^{(2)})
\]
be the Dirichlet-type space on the bidisc associated with finite positive Borel
measures on \(\overline{\mathbb D}\), and let
\(\mathscr M_z=(M_1,M_2)\) be the coordinate-multiplication pair. Write \(m\)
for normalized Haar measure on \(\mathbb T\) and set
\[
S(a)=|a|^2.
\]

There are bounded linear trace maps
\[
\Gamma_1:H\to
L^2(\overline{\mathbb D}\times\mathbb T,\rho^{(1)}\otimes m),
\qquad
\Gamma_2:H\to
L^2(\mathbb T\times\overline{\mathbb D},m\otimes\rho^{(2)})
\]
whose values on polynomials are
\[
(\Gamma_1p)(a,\zeta)=p(a,\zeta),\qquad
(\Gamma_2p)(\zeta,a)=p(\zeta,a).
\]
For every \(h\in H\),
\[
\|\Gamma_i h\|_2^2=\|M_i h\|_H^2-\|h\|_H^2,
\]
and
\[
\Gamma_1M_1=M_a\Gamma_1,\qquad
\Gamma_2M_2=M_a\Gamma_2.
\]

Define finite positive measures on \(\overline{\mathbb D}\) by
\[
\eta_{1,h}(E)=
\int_{E\times\mathbb T}|\Gamma_1h(a,\zeta)|^2\,
d\rho^{(1)}(a)\,dm(\zeta),
\]
\[
\eta_{2,h}(E)=
\int_{\mathbb T\times E}|\Gamma_2h(\zeta,a)|^2\,
dm(\zeta)\,d\rho^{(2)}(a),
\]
and put
\[
\mu_{i,h}=S_*\eta_{i,h}.
\]
Then
\[
\boxed{
\|M_i^{n+1}h\|_H^2-\|M_i^nh\|_H^2
=
\int_{[0,1]}t^n\,d\mu_{i,h}(t)
\qquad(n\ge0).
}
\]
Thus \(\mu_{i,h}\) is exactly the Hausdorff representing measure of the
coordinate forward-difference sequence.

Define
\[
d\lambda_{i,h}(t)=
\mathbf 1_{[0,1)}(t)\frac{1}{1-t}\,d\mu_{i,h}(t),
\qquad
\beta_i(h)=\mu_{i,h}(\{1\}).
\]
Then the complete Levy--Khinchin data of \((\mathscr M_z,h)\) are
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
This gives an explicit answer to Question 1.3 of Bera--Sequeira,
arXiv:2609.20346v1, for every vector \(h\).

## Polynomial specialization

For a polynomial \(p\), set
\[
w_{1,p}(a)=\int_{\mathbb T}|p(a,\zeta)|^2\,dm(\zeta),
\qquad
w_{2,p}(a)=\int_{\mathbb T}|p(\zeta,a)|^2\,dm(\zeta).
\]
Then
\[
\boxed{\mu_{i,p}=S_*(w_{i,p}\rho^{(i)}).}
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
The case \(m=n=0\) is the \(h=1\) formula in Theorem 1.4 of
arXiv:2609.20346v1.

## Countable tomography and the information boundary

For each coordinate \(i\), let
\[
\mathcal P_i=
\{1\}\cup\{1+z_i^k,\ 1-i z_i^k:k\ge1\}.
\]
The Levy measures
\[
\{\nu_{(\mathscr M_z,p)}:p\in\mathcal P_i\}
\]
determine the interior restriction
\[
\rho^{(i)}|_{\mathbb D}
\]
uniquely. The corresponding drift values
\[
\{b_{(\mathscr M_z,p)}(e_i):p\in\mathcal P_i\}
\]
determine the boundary restriction
\[
\rho^{(i)}|_{\mathbb T}
\]
uniquely. Hence the full Levy triples for the countable probe family
\(\mathcal P_1\cup\mathcal P_2\) determine both defining measures.

To see this, fix one coordinate and write \(\rho=\rho^{(i)}\). From the face
Levy measure one recovers
\[
S_*(|p|^2\rho|_{\mathbb D})
\]
for every \(p\in\mathcal P_i\). Put
\[
\sigma_0=S_*(\rho|_{\mathbb D}),\qquad
\sigma_k=S_*(a^k\rho|_{\mathbb D}).
\]
The identities
\[
|1+a^k|^2=1+|a|^{2k}+2\operatorname{Re}(a^k),
\]
\[
|1-i a^k|^2=1+|a|^{2k}+2\operatorname{Im}(a^k)
\]
recover the real and imaginary parts of every \(\sigma_k\).

Disintegrate \(\rho|_{\mathbb D}\) over \(t=|a|^2\). For
\(\sigma_0\)-almost every \(t>0\), let \(\kappa_t\) be the conditional
probability measure on the circle \(|a|=\sqrt t\). Then
\[
\frac{d\sigma_k}{d\sigma_0}(t)
=
t^{k/2}\int_{\mathbb T}\zeta^k\,d\kappa_t(\zeta).
\]
Thus the recovered \(\sigma_k\) give all Fourier coefficients of
\(\kappa_t\), so Fourier uniqueness determines the interior measure. The
fiber \(t=0\) consists only of the origin and is already determined by
\(\sigma_0\).

For the boundary part,
\[
b_{(\mathscr M_z,p)}(e_i)
=
\int_{\mathbb T}|p(\zeta)|^2\,d\rho(\zeta).
\]
The same probes recover all Fourier coefficients of
\(\rho|_{\mathbb T}\), hence the boundary measure by Fourier uniqueness.

Therefore the loss of information is exact: for polynomial probes,
interior mass is encoded in the Levy measure, while mass on \(\mathbb T\)
is sent to the \(t=1\) atom of the forward-difference representing measure
and appears in the drift rather than in the Levy measure.

## Angular sensitivity beyond the cyclic vector

Fix \(0<r<1\), take \(\rho^{(2)}=0\), and compare
\[
\rho^{(1)}_+=\delta_r,\qquad
\rho^{(1)}_-=\delta_{-r}.
\]
Their radial pushforwards are both \(\delta_{r^2}\), so the \(h=1\) Levy
measures coincide. For \(h(z)=1+z_1\), however, the first-face Levy atom at
\((r^2,1)\) has weight
\[
\frac{(1+r)^2}{1-r^2}
\]
for \(\rho^{(1)}_+\), and
\[
\frac{(1-r)^2}{1-r^2}
\]
for \(\rho^{(1)}_-\). Thus the radial pushforward alone cannot determine
the arbitrary-vector Levy measure.

## Proof of the all-vector formula

Equation (31) in S. Bera, *New York J. Math.* 32 (2026), gives for every
two-variable polynomial \(p\)
\[
\|M_1p\|_H^2-\|p\|_H^2
=
\int_{\overline{\mathbb D}\times\mathbb T}
|p(a,\zeta)|^2\,d\rho^{(1)}(a)\,dm(\zeta),
\]
and analogously for \(M_2\). Since \(M_i\) is bounded,
\[
\|\Gamma_i p\|_2^2
\le
\|M_i^*M_i-I\|\,\|p\|_H^2.
\]
Polynomials are dense, so the literal restriction maps extend uniquely to
bounded maps \(\Gamma_i\). Their polynomial intertwining with multiplication
by \(a\) extends by continuity.

Hence
\[
\begin{aligned}
\|M_i^{n+1}h\|_H^2-\|M_i^nh\|_H^2
&=\|\Gamma_iM_i^nh\|_2^2\\
&=\int_{\overline{\mathbb D}}|a|^{2n}\,d\eta_{i,h}(a)\\
&=\int_{[0,1]}t^n\,d(S_*\eta_{i,h})(t).
\end{aligned}
\]
Hausdorff uniqueness identifies \(S_*\eta_{i,h}\) with the representing
measure. In one variable the Levy--Khinchin relation is
\[
d\mu(t)=(1-t)d\nu(t)\quad(0\le t<1),
\qquad
b(1)=\mu(\{1\}),
\]
which gives \(\lambda_{i,h}\) and \(\beta_i(h)\).

Finally, the bidisc multiplication pair has vanishing pair defect.
Theorem 2.4 of Bera--Sequeira states that for every vector, this condition
is equivalent to the joint Levy measure being the sum of the two coordinate
face measures. This proves the joint formula and the additive drift.

## Originality boundary and limitations

Bera--Sequeira, arXiv:2609.20346v1, explicitly asks for the relation between
the arbitrary-vector Levy measure and the defining measures, but its
explicit defining-measure computation is for \(h=1\). Its Theorem 2.4
provides the abstract all-vector face decomposition. Bera's 2026 model
paper provides the polynomial defect identity used above.

The defect identity, the zero-defect decomposition, Hausdorff moment
uniqueness, disintegration, and Fourier uniqueness are not claimed as new.
The contribution is the explicit all-vector trace-map synthesis, the
weighted-pushforward formula, the exact interior-Levy/boundary-drift
information split, and the countable tomography consequence. Originality
is to the best of our knowledge.

For general \(h\), the trace maps are \(L^2\) traces defined by completion;
no pointwise boundary values are asserted. The tomography theorem uses a
countable family of probes. No claim is made for higher polydiscs or for
tuples without the vanishing pair-defect hypothesis.

## References

1. S. Bera and S. S. Sequeira, *Levy measures for Dirichlet-type spaces on
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
