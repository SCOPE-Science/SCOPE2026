# Strict endpoint entropy concavity throughout the log-concave binary-Gaussian location family

## Finding

For every \(0<\alpha\le\tfrac12\), let \(R\) be equiprobable on \(\{-1,+1\}\) and let \(G_0,G_1\) be independent standard Gaussian variables, all mutually independent. Define the variance-one prethermal state and half-thermalized state by
\[
X_\alpha=\sqrt\alpha\,R+\sqrt{1-\alpha}\,G_0,\qquad
U_\alpha=\frac{X_\alpha+G_1}{\sqrt2}.
\]
For two independent copies of the latter, define differential entropy (natural logarithm) along the normalized independent mixing path:
\[
F_\alpha(t)=h\!\left(\sqrt{1-t}\,U_\alpha^{(1)}+\sqrt t\,U_\alpha^{(2)}\right),\qquad 0\le t\le1.
\]
Then \(X_\alpha\) is log-concave if and only if \(\alpha\le\tfrac12\) (within \(0\le\alpha<1\)); and for every non-Gaussian member in that maximal log-concave range,
\[
F_\alpha''(0^+)=F_\alpha''(1^-)<0.
\]
The endpoint curvature has the **sharp small-signal asymptotic**
\[
\boxed{F_\alpha''(0^+)=-\frac{\alpha^4}{12}+o(\alpha^4)\quad (\alpha\downarrow0).}
\]
Thus the entire natural two-location Gaussian family, up to and including the exact threshold at which its initial mixture ceases to be log-concave, has strictly concave entropy near both mixing endpoints. This does not assert concavity across every interior mixing fraction.

## Assumptions and scope

All variables are real-valued. The two copies used in \(F_\alpha\) are independent, not merely uncorrelated. For \(0<\alpha\le\tfrac12\), every density appearing here is smooth, strictly positive, even, variance-one, and has Gaussian tails. This guarantees the required differentiations and integrations by parts, and yields an ordinary smooth one-sided second derivative at both endpoints. The limiting case \(\alpha=0\) is the standard Gaussian with zero entropy curvature. The claim does not concern \(\alpha>\tfrac12\), where the prethermal distribution is not log-concave.

Write \(S=2-\alpha\), \(\sigma^2=S/2\), \(\mu=\sqrt{\alpha/2}\), \(c=\mu/\sigma^2=\sqrt{2\alpha}/S\), and \(v=c^2\sigma^2=\alpha/S\). Thus \(0<v\le1/3\). If \(\phi_s\) is the centered Gaussian density of variance \(s\), then the density of \(U_\alpha\) is
\[
f(u)=\tfrac12\phi_{\sigma^2}(u-\mu)+\tfrac12\phi_{\sigma^2}(u+\mu)
=\phi_{\sigma^2}(u)e^{-v/2}\cosh(cu).
\]

## Proof

**1. Exact initial log-concavity boundary.** The density of \(X_\alpha\) equals a centered Gaussian factor times \(\cosh(\sqrt\alpha\,x/(1-\alpha))\). Consequently
\[
(\log p_{X_\alpha})''(x)=-\frac{1}{1-\alpha}+\frac{\alpha}{(1-\alpha)^2}\operatorname{sech}^2\!\left(\frac{\sqrt\alpha\,x}{1-\alpha}\right).
\]
This is nonpositive for every \(x\) exactly when \(\alpha\le1/2\); for larger \(\alpha\) it is positive at \(x=0\). Hence the family covers precisely its maximal log-concave parameter interval.

**2. The non-Gaussian term in the endpoint identity is strictly negative.** Let \(\rho=f'/f\) be the score. Direct differentiation gives
\[
\rho(u)=-\frac{2u}{S}+c\tanh(cu),\quad
\rho'(u)=-\frac2S+c^2\operatorname{sech}^2(cu),\quad
\rho^{(3)}(u)=c^4\bigl(4\operatorname{sech}^2(cu)-6\operatorname{sech}^4(cu)\bigr).
\]
Set
\[
A=\mathbb E_f[(\rho'(U_\alpha)+1)^2],\qquad
B=\mathbb E_f[(\rho'(U_\alpha))^2]-\tfrac13\mathbb E_f[\rho(U_\alpha)^4].
\]
Integrating by parts, \(\mathbb E_f[\rho^4]=-3\mathbb E_f[\rho^2\rho']\), and therefore
\[
B=\int\rho' f''\,du=-\int\rho'' f'\,du=\mathbb E_f[\rho^{(3)}(U_\alpha)].
\]
For \(Z\sim N(0,v)\), changing the Gaussian-mixture density to the centered reference measure gives the exact formula
\[
B=c^4e^{-v/2}\left(4\mathbb E\operatorname{sech}(Z)-6\mathbb E\operatorname{sech}^3(Z)\right).
\]
Tilt the \(N(0,v)\) measure by the strictly positive weight \(w(z)=\operatorname{sech}(z)\), and denote its expectation by \(\mathbb E_w\). Because \(z\mapsto z^2\) is strictly increasing in \(|z|\), while \(w(z)\) strictly decreases in \(|z|\), their covariance is negative and \(\mathbb E_w[Z^2]<v\). Also \(\operatorname{sech}^2 z=1-\tanh^2z\ge1-z^2\), with strict inequality for \(z\ne0\). Thus
\[
\frac{\mathbb E[\operatorname{sech}^3 Z]}{\mathbb E[\operatorname{sech} Z]}
=\mathbb E_w[\operatorname{sech}^2 Z]
>1-\mathbb E_w[Z^2]>1-v\ge\frac23.
\]
It follows that \(4\mathbb E\operatorname{sech}Z-6\mathbb E\operatorname{sech}^3Z<0\), so \(B<0\), with strictness even at \(\alpha=1/2\).

**3. Endpoint strictness.** Gaussian variables have vanishing fourth cumulant, while a Rademacher variable has fourth cumulant \(-2\). Hence
\[
\kappa_4(U_\alpha)=-2\mu^4=-\alpha^2/2<0.
\]
The established smooth symmetric endpoint-curvature identity [1, Theorem 3.1] is
\[
F_\alpha''(0^+)=-\frac12A-\frac{\kappa_4(U_\alpha)}{12}B.
\]
Since \(A\ge0\) and \(\kappa_4(U_\alpha)B>0\), the right-hand side is strictly negative for every \(0<\alpha\le\tfrac12\). Independence and exchangeability of the two identically distributed inputs give \(F_\alpha(t)=F_\alpha(1-t)\), so the right endpoint has the same strict one-sided curvature.

**4. Sharp fourth-order onset.** The exact score derivative identity simplifies to
\[
\rho'(u)+1=\frac{\alpha}{S^2}\bigl(\alpha-2\tanh^2(cu)\bigr).
\]
As \(\alpha\downarrow0\), \(U_\alpha\) converges with bounded Gaussian-dominated moments to a standard Gaussian \(G\) and \(c^2/\alpha\to1/2\). Using \(|\tanh z|\le |z|\) for dominated convergence, in \(L^2\) one obtains
\[
\frac{\rho'(U_\alpha)+1}{\alpha^2}\ \longrightarrow\ \frac{1-G^2}{4},\qquad
\frac{A}{\alpha^4}\longrightarrow\frac18.
\]
The explicit expression for \(B\), together with \(c^4/\alpha^2\to1/4\) and \(\operatorname{sech}Z\to1\), gives \(B/\alpha^2\to-1/2\). With \(\kappa_4(U_\alpha)/\alpha^2=-1/2\), the endpoint identity yields
\[
\lim_{\alpha\downarrow0}\frac{F_\alpha''(0^+)}{\alpha^4}
=-\frac12\cdot\frac18-\frac1{12}\cdot\frac14=-\frac1{12}.
\]
This completes the proof.

## Verification

The standalone file `verify.py` implements deterministic Gauss–Hermite quadrature on the exact two-component normal mixture. Running `python verify.py` checks the score integration-by-parts identity by two independent integral expressions, the strict \(B<0\) comparison and endpoint curvature for ten parameter values, the fourth-order limiting coefficient, and a second numerical route using four-Gaussian entropy mixtures and finite differences at five moderate parameters. Its bounded numerical checks passed (57 checks). This is a diagnostic cross-check, not a substitute for the quantified analytic proof.

## Relationship to prior work

Abu-Ajamieh [1] proves the general smooth endpoint-curvature identity and a conditional sign criterion, as well as results for generalized-Gaussian and leading Hermite perturbation families. We do not claim that identity or those conditional criteria as new. The present theorem verifies the missing sign for the full, naturally bounded, *Gaussian location-mixture* family by an exact positive-weight inequality, including the boundary parameter and its sharp small-signal coefficient. The Gaussian mixture theorem of Eskenazis–Gavalakis [3] concerns *centered Gaussian scale mixtures*; it does not cover separated-mean mixtures, which here have strictly negative fourth cumulant, whereas every centered Gaussian scale mixture has nonnegative fourth cumulant. Luo's asymmetric counterexample [2] does not settle this even log-concave family. These claim-level distinctions do not establish exhaustive publication priority.

## Limitations

Only the strict endpoint second derivative, and hence sufficiently local endpoint concavity, is proved; full concavity on the whole mixing interval is not established. No result beyond the maximal log-concave interval \(0<\alpha\le1/2\) is asserted. The basic endpoint identity is prior work; the new work is this family's strict sign proof and its fourth-order boundary. A potentially broader, previously unlocated Gaussian location-mixture result could subsume the theorem. Numerical finite differences alone do not prove any universal claim. No independent mathematical or publication-priority validation has been performed.

## References

[1] Fayez Abu-Ajamieh, *Noise-Induced Restoration of Entropy Concavity Near Gaussian Equilibrium*, arXiv:2610.22386v1, first posted 2026-10-12, https://arxiv.org/abs/2610.22386 . Theorem 3.1 and Sections 4–8.

[2] Congyi Luo, *Entropy concavity for log-concave random variables: an asymmetric counterexample*, arXiv:2609.11418, https://arxiv.org/abs/2609.11418 .

[3] Alexandros Eskenazis and Lampros Gavalakis, *On the entropy and information of Gaussian mixtures*, arXiv:2308.15997 (first posted 2023-08-30), https://arxiv.org/abs/2308.15997 ; *Mathematika* 70 (2024), e12246.
