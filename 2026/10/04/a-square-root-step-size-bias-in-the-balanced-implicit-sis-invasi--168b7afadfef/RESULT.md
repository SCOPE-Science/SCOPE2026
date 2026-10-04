# A square-root step-size bias in the balanced implicit SIS invasion threshold
## Finding
For the Schurz–Tosun stochastic SIS model and its balanced implicit method (BIM) (39)–(40), specialize to \(F_1\equiv0\), \(F_2(S,I)=\sigma S/K\) with \(\sigma>0\), and a uniform step \(h>0\). Writing \(c=\alpha+\gamma+\mu\) and \(a=\beta K-c\), the disease-free transverse SDE has almost-sure Lyapunov exponent \(\lambda=a-\sigma^2/2\). The linearized BIM has iid multiplier \(M_h(Z)=[1+(c+a)h+\sigma\sqrt{h}(|Z|-Z)]/[1+ch+\sigma\sqrt{h}|Z|]\), where \(Z\sim N(0,1)\), and hence transverse exponent \(\lambda_h=h^{-1}\mathbb E\log M_h(Z)\). As \(h\downarrow0\), \(\lambda_h=a-\sigma^2/2+\sqrt{2/\pi}\,\sigma(2\sigma^2-a)\sqrt{h}+O(h)\). Therefore the unique zero \(a_h\) near the continuous threshold satisfies \(a_h=\sigma^2/2-(3/2)\sqrt{2/\pi}\,\sigma^3\sqrt{h}+O(h)\), so for every sufficiently small positive \(h\) there is a nonempty interval \(a_h<a<\sigma^2/2\) on which the exact disease-free transverse linearization is almost-surely stable while the BIM transverse linearization is almost-surely unstable. This is a local linear threshold statement; it does not contradict the paper's fixed-finite-time mean-square convergence theorem or assert nonlinear/global instability.

## Assumptions and scope
Consider the stochastic SIS system of Schurz and Tosun with positive \\(\\alpha,\\beta,\\gamma,\\mu,K\\) on \\(\\mathbb D=\\{{(S,I):S>0,\\ I\\ge0,\\ S+I\\le K\\}}\\), and its BIM (39)–(40). Use the admissible diffusion specialization
\\[
F_1(S,I)=0,\\qquad F_2(S,I)=\\sigma S/K,\\qquad \\sigma>0.
\\]
Then \\(F_2/S=\\sigma/K\\) is bounded, so this specialization satisfies the source's hypothesis (45) for its mean-square convergence theorem. Fix a uniform step \\(h\\). The finding concerns only the transverse linearization at the disease-free state \\((K,0)\\).

Set \\(c=\\alpha+\\gamma+\\mu\\), \\(B=\\beta K\\), and \\(a=B-c\\). No assertion is made about nonlinear global disease extinction or persistence away from the disease-free state.

## Proof
At \\((K,0)\\), the infected component of the exact SDE linearizes to
\\[
dJ=aJ\\,dt-\\sigma J\\,dW.
\\]
Its explicit solution gives
\\[
\\lim_{t\\to\\infty}t^{-1}\\log|J(t)|=a-\\sigma^2/2
\\]
almost surely whenever \\(J(0)\\ne0\\). Thus the exact transverse exponent is \\(\\lambda=a-\\sigma^2/2\\).

For the BIM, the balancing weight at the disease-free state is
\\[
A=ch+\\sigma|\\Delta W|.
\\]
Writing \\(\\Delta W=\\sqrt h\\,Z\\) with \\(Z\\sim N(0,1)\\), differentiation of the infected update with respect to \\(I\\) at \\((K,0)\\) gives the positive multiplier
\\[
M_h(Z)=\\frac{1+Bh+\\sigma\\sqrt h(|Z|-Z)}{1+ch+\\sigma\\sqrt h|Z|}.
\\]
The multipliers are iid and \\(\\mathbb E|\\log M_h(Z)|<\\infty\\), so the strong law of large numbers gives the discrete transverse exponent
\\[
\\lambda_h=\\frac1h\\mathbb E[\\log M_h(Z)].
\\]

Put \\(\\varepsilon=\\sqrt h\\), \\(n=\\sigma(|Z|-Z)=2\\sigma(-Z)_+\\), and \\(d=\\sigma|Z|\\). Then
\\[
\\log M_h=\\log(1+n\\varepsilon+B\\varepsilon^2)-\\log(1+d\\varepsilon+c\\varepsilon^2).
\\]
The needed Gaussian moments are
\\[
\\mathbb E n=\\mathbb E d=\\sigma\\sqrt{2/\\pi},\\quad
\\mathbb E n^2=2\\sigma^2,\\quad \\mathbb E d^2=\\sigma^2,
\\]
\\[
\\mathbb E n^3=8\\sigma^3\\sqrt{2/\\pi},\\quad
\\mathbb E d^3=2\\sigma^3\\sqrt{2/\\pi}.
\\]
Taylor expansion through order \\(\\varepsilon^3\\) therefore yields
\\[
\\mathbb E\\log M_h=
\\left(a-\\frac{\\sigma^2}{2}\\right)\\varepsilon^2+
\\sqrt{\\frac{2}{\\pi}}\\,\\sigma(2\\sigma^2-a)\\varepsilon^3+O(\\varepsilon^4).
\\]
The remainder is justified by domination: for \\(\\varepsilon\\) in a fixed small interval and \\(a\\) in a compact neighborhood of \\(\\sigma^2/2\\), the fourth derivatives of both logarithms are bounded by a polynomial in \\(|Z|\\), which has finite Gaussian expectation. Division by \\(h=\\varepsilon^2\\) proves
\\[
\\lambda_h=a-\\frac{\\sigma^2}{2}+
\\sqrt{\\frac{2}{\\pi}}\\,\\sigma(2\\sigma^2-a)\\sqrt h+O(h).
\\]

At \\(a=\\sigma^2/2\\), the leading discrete exponent is
\\[
\\lambda_h=\\frac32\\sqrt{\\frac{2}{\\pi}}\\,\\sigma^3\\sqrt h+O(h)>0
\\]
for all sufficiently small positive \\(h\\). Moreover, for fixed \\(h\\), \\(\\lambda_h\\) is strictly increasing in \\(a\\), because
\\[
\\frac{\\partial\\lambda_h}{\\partial a}=
\\mathbb E\\left[\\frac{1}{1+(c+a)h+\\sigma\\sqrt h(|Z|-Z)}\\right]>0.
\\]
Consequently there is a unique zero \\(a_h\\) near \\(\\sigma^2/2\\), and substitution into the expansion gives
\\[
a_h=\\frac{\\sigma^2}{2}-\\frac32\\sqrt{\\frac{2}{\\pi}}\\,\\sigma^3\\sqrt h+O(h).
\\]
This places the BIM threshold strictly below the exact linear threshold for all sufficiently small \\(h>0\\), producing the stated mismatch interval.

## Verification
The accompanying `verify.py` replays the exact multiplier algebra at representative inputs and checks, from the half-normal Gaussian moments above, the coefficients \\(a-\\sigma^2/2\\), \\(\\sqrt{2/\\pi}\\,\\sigma(2\\sigma^2-a)\\), and the critical coefficient \\((3/2)\\sqrt{2/\\pi}\\,\\sigma^3\\). It also checks the sign of the leading threshold displacement.

The argument itself is analytic; no finite experiment is used as an infinite-time proof.

## Relationship to prior work
Schurz and Tosun define the SIS model and BIM used here, prove invariance for arbitrary step sizes, and prove mean-square convergence of order \\(1/2\\) on every fixed finite time interval under condition (45). Their conclusion describes dynamic consistency as coincidence of qualitative properties of exact and numerical solutions. The present calculation isolates a distinct long-time local question: at fixed \\(h\\), the almost-sure transverse Lyapunov threshold need not coincide exactly with the SDE threshold, even within the paper's convergence class.

The 2019 Schurz–Tosun paper analyzes stochastic asymptotic stability for the same SIS family and already uses the same BIM form for simulations, but it does not derive the finite-step transverse exponent above. Liu, Wang, and Dai construct a different SIS discretization that is explicitly designed to reproduce extinction and persistence for every step size; this shows that exact long-time threshold preservation is a substantive numerical property rather than a consequence of finite-time strong convergence alone.

## Limitations
The result is restricted to \\(F_1\\equiv0\\), \\(F_2(S,I)=\\sigma S/K\\), the disease-free transverse linearization, and the small-step asymptotic regime. It does not determine the nonlinear basin of attraction, global stochastic persistence, stationary distributions, or the behavior for general diffusion functions. The literature search found no equivalent source-specific BIM threshold expansion, but search coverage cannot prove universal absence from the literature.

## References
1. H. Schurz and K. Tosun, “Numerical Analysis of BIMs for Stochastic SIR and SIS Models with Variable Contact Diffusion Rates,” *Journal of Mathematical Biology* 92, 88 (2026). DOI: 10.1007/s00285-026-02392-4.
2. H. Schurz and K. Tosun, “Stability of stochastic SIS model with disease deaths and variable diffusion rates,” *Electronic Journal of Qualitative Theory of Differential Equations* 2019(14), 1–24. DOI: 10.14232/ejqtde.2019.1.14.
3. R. Liu, X. Wang, and L. Dai, “An unconditional boundary and dynamics preserving scheme for the stochastic epidemic model,” *Calcolo* 61 (2024). DOI: 10.1007/s10092-024-00606-z; arXiv:2308.05287.
