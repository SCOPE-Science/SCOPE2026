# A four-frequency sextic normal form near sharp Chang–Marshall extremizers

## Finding
For an analytic polynomial \(f(z)=\sum_{j\ge1}a_jz^j\), define its normalized Dirichlet energy and boundary exponential moment by
\[
D(f)=\sum_{j\ge1}j|a_j|^2,\qquad J(f)=\frac1{2\pi}\int_0^{2\pi}e^{|f(e^{i\theta})|^2}\,d\theta.
\]
The sharp Chang–Marshall theorem of Frank–Ivanisvili states \(J(f)\le e^{D(f)/m}\) when \(f\) vanishes to order \(m\ge1\) and \(0<D(f)\le1\), with equality precisely for monomials. Here is a quantitative, finite-jet refinement of its equality geometry.

Fix any integer \(m\ge1\), any real \(\kappa,\lambda\), and sufficiently small real \(t\). Set
\[
\begin{aligned}
a(t)&=\left[\frac{1-(m+1)t^2-(m+2)\kappa^2t^4-(m+3)\lambda^2t^6}{m}\right]^{1/2},\\
f_{m,t;\kappa,\lambda}(z)&=a(t)z^m+t z^{m+1}+\kappa t^2z^{m+2}+\lambda t^3z^{m+3}.
\end{aligned}
\]
Then \(D(f_{m,t;\kappa,\lambda})=1\) exactly. Write
\[
\kappa_m=\frac{2m+1}{2\sqrt m},\qquad \lambda_m=\frac{12m^2+15m+4}{12m},\qquad
\Delta(f)=\frac1m-\log J(f).
\]
There are **two successive, uniquely optimized resonant cancellations**:
\[
\boxed{\Delta(f_{m,t;\kappa,\lambda})=\frac{(\kappa-\kappa_m)^2}{m}t^4+O_{m,\kappa,\lambda}(t^6).}
\]
For the unique quartic-cancelling value \(\kappa=\kappa_m\),
\[
\boxed{\Delta(f_{m,t;\kappa_m,\lambda})=\left[\frac{2(\lambda-\lambda_m)^2}{m}+\frac1{24m}\right]t^6+O_{m,\lambda}(t^8).}
\]
Consequently, the **smallest sextic coefficient within this normalized four-frequency jet family** is exactly \(1/(24m)\), uniquely realized by \(\lambda=\lambda_m\). For \(m=1\), the optimizing coefficients are \(\kappa_1=3/2\) and \(\lambda_1=31/12\), and the sixth-order coefficient is \(1/24\).

## Assumptions and scope
The parameter \(m\) is any positive integer; \(\kappa,\lambda\in\mathbb R\) are fixed independently of \(t\), and \(t\to0\) through real values small enough that \(a(t)>0\). The claims concern exactly the displayed four adjacent Fourier modes. The minimizations are over the two real jet parameters \(\kappa\) and then \(\lambda\); no global sixth-order stability assertion is made for unrestricted Dirichlet functions or for differently scaled higher-mode perturbations.

For \(\mathcal E_m=\{e^{i\phi}z^m/\sqrt m:\phi\in\mathbb R\}\), the Dirichlet distance obeys
\[
\operatorname{dist}_{D}(f_{m,t;\kappa_m,\lambda_m},\mathcal E_m)=\sqrt{m+1}\,|t|+O_m(|t|^3).
\]
Therefore neither a local quadratic nor a local quartic lower bound in this Dirichlet distance can hold for the normalized Chang–Marshall deficit, even though the published theorem has strict equality rigidity. The value \(1/(24m)\) is **not** asserted to be the best coefficient over arbitrary infinite-dimensional perturbations.

## Proof
Writing \(a=a(t)\), the Fourier expansion of the boundary square is
\[
|f_{m,t;\kappa,\lambda}(e^{i\theta})|^2=S+2U\cos\theta+2V\cos2\theta+2W\cos3\theta,
\]
where the coefficients are real and exactly
\[
\begin{aligned}
S&=a^2+t^2+\kappa^2t^4+\lambda^2t^6,\\
U&=at+\kappa t^3+\kappa\lambda t^5,\\
V&=a\kappa t^2+\lambda t^4,\\
W&=a\lambda t^3.
\end{aligned}
\]
Thus \(\log J(f)=S+\Phi(U,V,W)\), where \(\Phi\) is the logarithm of the mean of \(\exp(2U\cos\theta+2V\cos2\theta+2W\cos3\theta)\). Extracting the constant Laurent coefficient of the exponential, then applying the power series for the logarithm, gives, with weights \(\deg U=1\), \(\deg V=2\), \(\deg W=3\),
\[
\begin{aligned}
\Phi(U,V,W)={}&U^2+\bigl(V^2+U^2V-\tfrac14U^4\bigr)\\
&+\bigl(W^2+2UVW+\tfrac13U^3W-\tfrac23U^4V+\tfrac19U^6\bigr)
+O_{\mathrm{wt}}(8).
\end{aligned}
\]
The omitted constant Laurent coefficients have weighted degree at least eight: odd weighted degrees vanish under \(\theta\mapsto\theta+\pi\) and simultaneous \((U,W)\mapsto(-U,-W)\). This identity can also be reconstructed by enumerating the finitely many zero-frequency terms of the exponential through weighted degree six.

Next, the positive square root defining \(a\) has the expansion
\[
a(t)=m^{-1/2}\left[1-\frac{m+1}{2}t^2-\left(\frac{m+2}{2}\kappa^2+\frac{(m+1)^2}{8}\right)t^4+O_{m,\kappa,\lambda}(t^6)\right].
\]
Substitution into \(\Delta=1/m-S-\Phi\) cancels the quadratic coefficient identically. Its quartic coefficient is the **perfect square** \((\kappa-\kappa_m)^2/m\), independent of \(\lambda\). Hence quartic cancellation is unique. With \(\kappa=\kappa_m\), the sextic coefficient simplifies to
\[
\frac{36m^2\lambda^2-(72m^3+90m^2+24m)\lambda+36m^4+90m^3+81m^2+30m+4}{18m^3}
=\frac{2(\lambda-\lambda_m)^2}{m}+\frac1{24m}.
\]
The second displayed normal form and unique sextic minimizer follow. For real \(t\), the boundary moment and Dirichlet normalization are even analytic functions of \(t\), which justifies the \(O(t^8)\) remainder after the sextic term. Positivity of the leading minimum is immediate since \(m\ge1\). Finally, orthogonality of the Dirichlet Fourier basis gives the stated distance to \(\mathcal E_m\): the nearest phase is zero for small real \(t\), and the first transverse coefficient has norm \(\sqrt{m+1}|t|\). This proves the failure of any local lower bound with a positive multiple of the second or fourth power of that distance.

## Verification
The accompanying `verify.py` reconstructs the weighted-degree-six Laurent constant-term expansion using exact rational/symbolic arithmetic. It verifies both the perfect-square quartic coefficient and the completed-square sextic coefficient for symbolic \(m\), and checks positivity for sample positive integer parameters. Execute `python3 verify.py` with Python 3 and SymPy installed. The actual checked execution returned `VERIFY_OK exact Fourier expansion; unique quartic cancellation; sharp four-mode sextic coefficient 1/(24m)`.

The symbolic check is a reproducibility aid. The universal conclusion follows from the displayed analytic Taylor derivation, not from finitely many numerical experiments.

## Relationship to prior work
Frank and Ivanisvili, *The sharp constant in the Chang–Marshall inequality* (first arXiv version dated 2026-10-11), prove the global inequality and characterize monomial equality, but do not give this nonlinear four-mode local normal form. Andreev and Matheson, *Extremal functions and the Chang–Marshall inequality* (1994), treat local maximality including the exceptional first higher Fourier mode along **fixed-direction** normalized curves. Their calculation does not incorporate the second- and third-order mode corrections yielding the quartic and sextic cancellations above. The global inequality and those local maximality statements are credited as established premises. This result concerns the distinct quantitative geometry of approaching their equality cases.

## Limitations
The normal form is exact for a specified four-mode polynomial family and fixed real jet parameters; no claim of a sharp infinite-dimensional stability exponent or of a global stability lower bound is made. Complex phases or higher-frequency modes may alter the best unrestricted coefficient. Historical priority of higher-order Chang–Marshall stability expansions remains a risk despite targeted literature and database searches. The review is not an independent mathematical audit.

## References
1. R. L. Frank and P. Ivanisvili, *The sharp constant in the Chang–Marshall inequality*, arXiv:2610.15378 (first posted 2026-10-11; inspected complete HTML of revised version), https://arxiv.org/html/2610.15378v2 .
2. V. V. Andreev and A. Matheson, *Extremal functions and the Chang–Marshall inequality*, Pacific J. Math. **162** (1994), 233–246, https://msp.org/pjm/1994/162-2/pjm-v162-n2-p02-p.pdf .
