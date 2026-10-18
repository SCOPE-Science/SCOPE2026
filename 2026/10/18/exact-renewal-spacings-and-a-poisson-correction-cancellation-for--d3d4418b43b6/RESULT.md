# Exact renewal spacings and a Poisson-correction cancellation for isolated-point thinning

## Finding
Let \(\lambda,\tau>0\) and let \(n\ge1\) be an integer. Superpose \(n\) independent stationary Poisson processes of intensity \(\lambda\) on the real line. Retain any point without another original point at distance at most \(r_n=\tau/(2n)\) with probability \(1/n\), independently of all other surviving isolation decisions; discard all other points. Write \(Y_n\) for the resulting process and \(T_n\) for the distance between consecutive points under its Palm law.

**Exact finite-\(n\) law.** The retained process \(Y_n\) is a stationary renewal point process for every \(n\). For \(s\ge0\), put \(\mu=n\lambda\), \(r=\tau/(2n)\) and
\[
 A_n(s)=\frac{\mu}{\mu+s}e^{-(\mu+s)r},\qquad
 B_n(s)=\frac{\mu}{\mu+s}\bigl(1-e^{-(\mu+s)r}\bigr).
\]
Its Palm interarrival Laplace transform is exactly
\[
 \mathbb E e^{-sT_n}=\frac{\phi_n(s)}{n-(n-1)\phi_n(s)},\qquad
 \phi_n(s)=\frac{A_n(s)(1-B_n(s))}{1-B_n(s)-A_n(s)B_n(s)}.
\]
The mean interarrival distance is exactly \(\mathbb ET_n=e^{\lambda\tau}/\lambda\), independent of \(n\).

**Sharp first correction to Poisson spacing.** Write \(t=\lambda\tau\), \(m=e^t/\lambda\). For each fixed \(s\ge0\), as \(n\to\infty\),
\[
\begin{aligned}
\mathbb E e^{-sT_n}
&=\frac1{1+ms}
+\frac1n\frac{e^t}{\lambda^2}\bigl(e^{t/2}-1-t\bigr)
\frac{s^2}{(1+ms)^2}+O_{\lambda,\tau,s}(n^{-2}).
\end{aligned}
\]
There is a unique positive \(t_*\) solving \(e^{t_*/2}=1+t_*\), with \(t_*\approx2.51286241725234\). For every \(s>0\), the first-order difference from the Poisson interarrival transform is negative for \(0<t<t_*\) and positive for \(t>t_*\). At the nonzero critical value \(t=t_*\), the entire order-\(1/n\) term cancels simultaneously for every fixed \(s\ge0\), so the Laplace transform approaches the exponential law with error \(O_{\lambda,\tau,s}(n^{-2})\). This is a fixed-transform statement, not a total-variation or uniform-in-\(s\) estimate.

## Assumptions and scope
All point processes are defined on the full real line, eliminating artificial finite-window boundary effects. A Poisson point is isolated precisely when both adjacent Poisson gaps exceed \(r_n\). Strict versus weak inequalities is immaterial because exponential gaps have no atoms. Retention coins for distinct isolated points are mutually independent and independent of the original process. Palm interarrival refers to the rightward gap beginning at a typical retained point, not the length-biased gap containing a fixed deterministic spatial location.

## Proof
**1. Isolation regenerates in dimension one.** For a homogeneous Poisson input of intensity \(\mu>0\), enumerate its points from left to right and let their successive gaps be independent \(\operatorname{Exp}(\mu)\) variables. Write a gap \(L\) if its length exceeds \(r\), and \(S\) otherwise. A point is isolated exactly when its left and right gaps have labels \(LL\). At an isolated point the outgoing gap is \(L\), and, conditional on this label, its positive length has the exponential law conditioned to exceed \(r\). The event that the point is isolated tests the outgoing gap only through this label and does not test its excess length. Thus the next rightward cycle can begin from the same conditional law, independently of everything up to the current isolated point. Iterating shows that Palm intervals between isolated points are independent and identically distributed. The process is stationary by translation invariance, and isolated points have strictly positive intensity \(\mu e^{-2\mu r}\).

**2. Exact transform by a two-state gap recursion.** For an independent \(G\sim\operatorname{Exp}(\mu)\), define
\[
 a(s)=\mathbb E[e^{-sG};G>r],\quad b(s)=\mathbb E[e^{-sG};G\le r],\quad p=\Pr(G>r)=e^{-\mu r}.
\]
They equal the displayed \(A_n,B_n\) when \(\mu=n\lambda\) and \(r=r_n\). Define \(F_L(s)\) and \(F_S(s)\) as the transforms of the distance *after* a gap of known long or short label has just been counted, until the next isolated point, counting the subsequent gap only when required to travel farther. If the known previous gap is long, the very next gap is long with probability \(p\), in which case the current point is isolated and no further displacement is required; otherwise that short next gap must be traversed. If the previous gap is short, the next gap must be traversed regardless of its label. Hence
\[
 F_L=p+bF_S,\qquad F_S=aF_L+bF_S,
\]
and therefore \(F_L=p(1-b)/(1-b-ab)\). Starting from an isolated point, first traverse an outgoing gap distributed as \(G\mid\{G>r\}\), whose transform is \(a/p\), to obtain
\[
 \phi(s)=\frac apF_L(s)=\frac{a(1-b)}{1-b-ab}.
\]
The denominator is positive for \(s\ge0\): since \(0\le a\le p\), \(0\le b\le1-p\), \(1-b-ab\ge1-(1-p)(1+p)=p^2>0\). Independent retention with probability \(q=1/n\) selects geometric numbers of consecutive isolated-point gaps; if \(K\) has \(\Pr(K=k)=q(1-q)^{k-1}\), then the retained gap is \(T_n=\sum_{j=1}^KT^{\mathrm{iso}}_j\) in law. The geometric sum gives \(\mathbb E e^{-sT_n}=q\phi_n(s)/(1-(1-q)\phi_n(s))\), as claimed. Consecutive retained gaps are again independent by regeneration and independence of coins.

**3. Moments of the isolated-point gap.** Put \(c=\mu r>0\), \(u=s/\mu\). Direct simplification gives the scale-free transform
\[
 \phi(s)=\frac{1+u e^{c(1+u)}}{1+u e^{c(1+u)}+u(1+u)e^{2c(1+u)}}.
\]
Differentiating this explicit analytic quotient at \(s=0\) yields
\[
 \mathbb E T^{\mathrm{iso}}=\frac{e^{2c}}\mu,\qquad
 \mathbb E[(T^{\mathrm{iso}})^2]-2(\mathbb E T^{\mathrm{iso}})^2
 =\frac{2e^{2c}}{\mu^2}(e^c-1-2c).
\]
The mean also agrees with the reciprocal isolation intensity, an independent normalization check. Geometric compounding multiplies the mean by \(n\), giving \(\mathbb E T_n=e^{2c}/\lambda=e^t/\lambda\).

**4. Order-\(1/n\) correction and unique cancellation.** Here \(c=t/2\) is constant, while \(\mu=n\lambda\). Set \(m=e^t/\lambda\) and \(C=e^t(e^{t/2}-1-t)/\lambda^2\). By the moment identity and analyticity near zero,
\[
 \phi_n(s)=1-\frac{ms}{n}+\frac{(m^2+C)s^2}{n^2}+O_s(n^{-3}).
\]
Substituting into \(\phi_n/[n-(n-1)\phi_n]\) and expanding about the nonzero denominator \(1+ms\) yields
\[
 \mathbb E e^{-sT_n}=\frac1{1+ms}+\frac{Cs^2}{n(1+ms)^2}+O_s(n^{-2}).
\]
The function \(h(t)=e^{t/2}-1-t\) has \(h(0)=0\), \(h'(0)=-1/2\), \(h''(t)=e^{t/2}/4>0\), and \(h(t)\to\infty\). Consequently it is strictly negative immediately to the right of zero and has exactly one further positive zero, establishing all sign statements. The leading term is the transform of \(\operatorname{Exp}(1/m)\); Laplace-transform uniqueness gives convergence of Palm interarrival distributions to that law. Stationary renewal structure additionally identifies the associated limiting stationary Poisson point process.

## Verification
The accompanying standalone `verify.py` calculates the exact transform in two algebraically distinct representations, checks the two-state recursion and moment identities by symbolic differentiation, tests the geometric-thinning identity over a grid of parameters, numerically checks finite-\(n\) coefficients at several rates and frequencies, and simulates independent Poisson gaps to check both the predicted renewal means and near-zero lag-one correlations. All numerical experiments are finite illustrations; the proof of the theorem is analytical in the four steps above. To reproduce: run `python verify.py` with Python 3 and installed NumPy and SymPy.

## Relationship to prior work
Hlyniana, *A law of thin processes with neighbour-count thinning* (arXiv:2609.25733v1, September 22, 2026), proves the general first-order Poisson process limit under the critical spatial scaling; it motivates looking for a sharp higher-order law in the exact-one-dimensional Matérn-I specialization. The present statement identifies an exact regenerative structure, all finite-\(n\) Palm spacing transforms and a signed order-\(1/n\) correction with a distinguished cancellation parameter, none stated in the inspected source. Hlyniana, *Neighbour-count dependent thinning of Poisson processes: correlation structure and Poisson approximation* (arXiv:2511.10083, first available November 13, 2025), already supplies intensity and pair correlation for general local thinning, including Matérn I. These determine second-order count information but do not explicitly give the regenerative interarrival identity or its geometric-compounding transform. Spinka (arXiv:1912.03786v1) proves regeneration for a *one-sided* simple-selection Poisson process (requiring a left empty interval), not the present two-sided isolation rule. Rao, Adams, and Dunson (arXiv:1308.1136v2) distinguish Matérn types and focus on inference for type III rather than the present law.

## Limitations
The sharp correction is proved only in one spatial dimension, for Poisson inputs with exact intensity \(n\lambda\), exact radius \(\tau/(2n)\), and Bernoulli retention \(1/n\) *after* isolation. It concerns Palm nearest-neighbor distances, not the forward-recurrence distance from a deterministic location. The \(O(n^{-2})\) statement is pointwise in the Laplace variable and should not be read as a total-variation rate or as an estimate uniformly over growing \(s\). Extension to general input point processes, non-Poisson superpositions, or general neighbor-dependent retention is not proved. A related classical one-dimensional isolation result may exist under an alternate renewal/scan-statistic terminology; the literature comparison is not an independence certification.

## References
1. K. Hlyniana, *A law of thin processes with neighbour-count thinning*, arXiv:2609.25733v1 (2026-09-22), https://arxiv.org/html/2609.25733v1.
2. K. Hlyniana, *Neighbour-count dependent thinning of Poisson processes: correlation structure and Poisson approximation*, arXiv:2511.10083 (2025-11-13), https://arxiv.org/abs/2511.10083.
3. Y. Spinka, *Finitary isomorphisms of renewal point processes and continuous-time regenerative processes*, arXiv:1912.03786v1, https://arxiv.org/html/1912.03786v1.
4. V. Rao, R. P. Adams, D. B. Dunson, *Bayesian inference for Matérn repulsive processes*, arXiv:1308.1136v2, https://arxiv.org/html/1308.1136v2.
