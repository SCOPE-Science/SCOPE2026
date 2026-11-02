# Exact topology and critical-volume scaling for simultaneous coherent-state localization

## Finding

Let \(q\ge1\) be an integer, let \(a\ge0\), and work in the probability-normalized Bargmann--Fock space on \(\mathbb C^q\). The unit coherent states at \(\pm a e_1\) are
\[
k_{\pm a}(z)=\exp(\pm a z_1-a^2/2).
\]
For each normalized Euclidean observation volume \(A>0\), define
\[
R_q(a,A)=\sup_{|\Omega|=\pi^q A}\min_{\sigma\in\{-1,+1\}}\int_\Omega |k_{\sigma a}(z)|^2\pi^{-q}e^{-|z|^2}\,dV(z),
\]
where \(\Omega\subset\mathbb C^q\) ranges over measurable sets. The optimizer is unique up to null sets and is the superlevel set of the **average** coherent-state energy density
\[
h_a(z)=\pi^{-q}e^{-(|z|^2+a^2)}\cosh(2a\operatorname{Re}z_1).
\]
If \(a\le1/\sqrt2\), the canonical open optimal region is connected for every \(A>0\). If \(a>1/\sqrt2\), there is a unique critical volume \(A_c(a)>0\): the canonical optimal region has exactly two connected components for \(0<A\le A_c(a)\), and is connected for \(A>A_c(a)\). At equality the two open components have the midpoint saddle in their common closure. Topology is stated for the canonical open superlevel representative, not for arbitrary null-set modifications.

Set \(m=2q\), \(v_j=\pi^{j/2}/\Gamma(j/2+1)\), and \(g_a(x)=\log\cosh(2ax)-x^2\). For \(a>1/\sqrt2\), there is a unique positive root \(r_a\) of \(g_a(r_a)=0\). The **exact** critical normalized volume is
\[
A_c(a)=\frac{2v_{m-1}}{\pi^q}\int_0^{r_a}[g_a(x)]^{(m-1)/2}\,dx.
\]
The function \(a\mapsto A_c(a)\) is strictly increasing on \((1/\sqrt2,\infty)\). With \(\mu=2a^2-1\downarrow0\), its dimension-dependent onset is
\[
\boxed{A_c(a)=\frac{3^q\Gamma(q)}{\sqrt\pi\,\Gamma(2q+\tfrac12)}\,\mu^{2q-1/2}(1+O_q(\mu)).}
\]
In particular, the coefficient is \(4/\pi\) for \(q=1\) and \(48/(35\pi)\) for \(q=2\). At large separation,
\[
\boxed{A_c(a)\sim\frac{2}{q!}\,a^{2q}\qquad(a\to\infty).}
\]
Thus the transition volume grows with exponent \(2q-1/2\) at the symmetry-breaking threshold and with exponent \(2q\) at large separation.

## Assumptions and scope

The Fock norm is \(\|F\|^2=\pi^{-q}\int_{\mathbb C^q}|F(z)|^2e^{-|z|^2}\,dV(z)\). The states and both captured energies are individually normalized to one on all of \(\mathbb C^q\). The optimization is over all Lebesgue-measurable regions of **exact** Euclidean volume \(\pi^q A\), with no convexity or connectedness constraint. The two targets have identical Gaussian width and equal minimax importance; \(q\) is any fixed positive integer. The canonical representative is \(\Omega_{a,A}=\{z:h_a(z)>\lambda_{a,A}\}\), with the unique threshold giving the requested volume.

## Proof

**Exact reduction to one symmetric density.** The reproducing-kernel normalization gives
\[
|k_{\pm a}(z)|^2\pi^{-q}e^{-|z|^2}=\pi^{-q}e^{-|z\mp a e_1|^2}=:p_\pm(z).
\]
For any admissible \(\Omega\),
\[
\min\{\int_\Omega p_+,\int_\Omega p_-\}\le\int_\Omega(p_++p_-)/2\le\sup_{|E|=\pi^q A}\int_E h_a.
\]
Since \(h_a\) is continuous, positive, tends to zero at infinity, and is nonconstant real analytic, the standard exchange argument for fixed-volume integration shows that the unique maximizing set up to null sets is \(\Omega_{a,A}=\{h_a>\lambda_{a,A}\}\). Its volume is a strictly decreasing, continuous function of \(\lambda\) from infinity to zero on \((0,\max h_a)\): between distinct levels lie open sets of positive measure, while every level surface has zero Lebesgue measure. Reflection \(\operatorname{Re}z_1\mapsto-\operatorname{Re}z_1\) interchanges \(p_+\) and \(p_-\) and preserves \(\Omega_{a,A}\). Hence the two captured energies are equal on that set, both inequalities are equalities, and the same set uniquely attains \(R_q(a,A)\).

**Connectedness classification.** Write \(z=(x+iu,w)\), where \(x\in\mathbb R\) and \(y=(u,\operatorname{Re}w,\operatorname{Im}w)\in\mathbb R^{m-1}\). For a threshold \(\lambda>0\), put \(c=-\log(\pi^q e^{a^2}\lambda)\). Then
\[
\{h_a>\lambda\}=\{(x,y):|y|^2<g_a(x)+c\}.
\]
For \(x>0\), the derivative is \(g_a'(x)=2a\tanh(2ax)-2x\). If \(2a^2\le1\), the strict inequality \(\tanh t<t\) for \(t>0\) gives \(g_a'(x)<0\), so every nonempty superlevel has connected interval support in \(x\) and ball cross-sections containing \(y=0\). If \(2a^2>1\), the function \(a\tanh(2ax)-x\) has positive derivative at zero, strictly decreasing derivative for \(x>0\), and tends to minus infinity; it has exactly one positive zero. Accordingly \(g_a\) increases from zero to one positive maximum, then decreases to minus infinity and has exactly one positive nonzero root \(r_a\). The midpoint \((x,y)=(0,0)\) has density \(h_a(0)=\pi^{-q}e^{-a^2}\). Above this density threshold the positive \(x\)-support has exactly two disjoint intervals, at the threshold it has two intervals separated by \(x=0\), and below it is a single interval. Each cross-section is a ball, and its \(y=0\) spine establishes the corresponding path-connectedness. Thus topology switches exactly when the threshold crosses \(h_a(0)\). Integrating the radial \(\mathbb R^{m-1}\) cross-section at this level gives the stated critical-volume integral. The canonical open superlevel remains disconnected at the equality level.

**Strict monotonicity.** For every \(x>0\), \(\partial_a g_a(x)=2x\tanh(2ax)>0\). As \(a\) increases beyond \(1/\sqrt2\), the positive-cross-section set \(\{(x,y):|y|^2<g_a(x)\}\) strictly expands on an open set of positive volume, proving strict increase of \(A_c(a)\).

**Threshold asymptotic.** Put \(\mu=2a^2-1\). The Taylor expansion around \((\mu,x)=(0,0)\) is
\[
g_a(x)=\mu x^2-\frac{(1+\mu)^2}{3}x^4+O(x^6),
\]
where the remainder is uniform for small nonnegative \(\mu\). The positive root therefore obeys \(r_a=\sqrt{3\mu}(1+O(\mu))\). With \(x=\sqrt{3\mu}\,u\), the leading integrand is \([3\mu^2u^2(1-u^2)]^{(m-1)/2}\). Rescaling by the exact root (to control the vanishing endpoint) gives a uniform relative \(O_q(\mu)\) remainder after integration. Thus
\[
A_c(a)=\frac{2v_{m-1}3^{m/2}}{\pi^q}\mu^{m-1/2}\int_0^1u^{m-1}(1-u^2)^{(m-1)/2}\,du\,(1+O_q(\mu)).
\]
The integral equals \(\tfrac12 B(m/2,(m+1)/2)\). Using \(m=2q\), \(v_{m-1}=\pi^{q-1/2}/\Gamma(q+1/2)\), and the beta-gamma identity produces the claimed coefficient \(3^q\Gamma(q)/(\sqrt\pi\Gamma(2q+1/2))\).

**Large-separation asymptotic.** Scale \((x,y)=a(s,v)\). Pointwise for \(s\ne0\),
\[
a^{-2}g_a(as)=a^{-2}\log\cosh(2a^2s)-s^2\longrightarrow 2|s|-s^2.
\]
The scaled positive-cross-section regions are uniformly bounded (since \(\log\cosh t\le|t|\)), and their indicator functions converge almost everywhere to the union of two unit balls in \(\mathbb R^m\), centered at \((\pm1,0)\). Dominated convergence gives \(A_c(a)/a^m\to 2v_m/\pi^q=2/q!\).

## Verification

The accompanying `check_coherent_phase.py` uses only the Python standard library. It verifies the existence/order of the positive saddle root, the critical-volume integral by deterministic numerical quadrature, strict sample-point monotonicity, the near-critical power and constants in complex dimensions one to three, and the large-separation limit. The independent numerical tests passed 44 deterministic assertions. These checks corroborate calculations; they do not replace the above proofs for all dimensions and parameters.

## Relationship to prior work

Nicola and Tilli (first public version 2021) characterize the globally optimal *single, freely chosen signal* and observation region for Gaussian short-time Fourier energy concentration: a ball and a corresponding coherent state. Their supremum over all signals does not determine the distinct problem of guaranteeing concentration for **both prescribed** coherent states, nor the observation-set topology as their separation varies. Galbis (2021) proves operator-norm estimates for radial Fock Toeplitz symbols; it does not address two displaced coherent-state target intensities or connectedness thresholds. The well-known two-Gaussian-mixture mode transition is mathematical background and does not by itself supply the dimension-dependent critical observation volume and its two sharp asymptotic regimes. The result is a direct geometric localization problem, not a claim that Gaussian mixture modes or bathtub rearrangement are new.

## Limitations

This result is confined to two equal-width, equally prioritized coherent states. It does not classify asymmetric target weights, three or more states, anisotropic windows, or stability under perturbations. The connectedness theorem concerns canonical open superlevel representatives; null-set changes to a measurable optimum may alter point-set topology. No independent audit has been performed, and historical priority of the exact critical-volume law is not conclusively established.

## References

1. F. Nicola and P. Tilli, *The Faber–Krahn inequality for the short-time Fourier transform*, arXiv:2106.03423 (first public 7 June 2021), Invent. Math. 230 (2022), 1–30. https://arxiv.org/abs/2106.03423
2. A. Galbis, *Norm estimates for selfadjoint Toeplitz operators on the Fock space*, arXiv:2102.02031 (first public 3 February 2021). https://arxiv.org/abs/2102.02031
3. C. Améndola, A. Engström and C. Haase, *Maximum Number of Modes of Gaussian Mixtures*, arXiv:1702.05066 (first public 16 February 2017). https://arxiv.org/abs/1702.05066
4. M. Á. Carreira-Perpiñán and C. K. I. Williams, *On the Number of Modes of a Gaussian Mixture*, Scale Space Methods in Computer Vision (2003), 625–640. https://doi.org/10.1007/3-540-44935-3_44
