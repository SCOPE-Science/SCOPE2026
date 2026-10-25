# Minority-controlled critical fluctuations in an imbalanced bipartite Ising ferromagnet

## Finding
Let \(m\ge n\ge1\). Put spins \(\sigma_i,\tau_j\in\{-1,1\}\) on the two classes of the complete bipartite graph \(K_{m,n}\) and write \(S_A=\sum_{i=1}^m\sigma_i\), \(S_B=\sum_{j=1}^n\tau_j\). At inverse coupling \(\beta>0\) assign Gibbs weights proportional to
\[
\exp\!\left(\frac{\beta S_A S_B}{\sqrt{mn}}\right).
\]
Write \(Q_{n,q}\) for the ordinary zero-field \(n\)-spin Curie–Weiss law, with configuration weights proportional to \(\exp(q S_B^2/(2n))\).

**Quantitative minority reduction.** For each finite \(L>0\) there are constants \(C_L,n_L\) such that, for every \(n\ge n_L\), \(m\ge n\) and \(|\lambda|\le L\), upon setting \(\beta=1+\lambda/\sqrt n\),
\[
\left\|\mathcal L_{m,n,\beta}(S_B)-\mathcal L_{Q_{n,\beta^2}}(S_B)\right\|_{\rm TV}
\le C_L\frac nm.
\]
This holds for the entire minority magnetization distribution, not merely a finite set of moments. The finite-size marginal is exactly
\[
\mathbb P_{m,n,\beta}(S_B=s)
=\frac{\binom n{(n+s)/2}\cosh\!\left(\beta s/\sqrt{mn}\right)^m}
{\sum_{u\equiv n\;(\mathrm{mod}\;2),\ |u|\le n}\binom n{(n+u)/2}\cosh\!\left(\beta u/\sqrt{mn}\right)^m},
\quad s=-n,-n+2,\ldots,n.
\]

**Singular-size critical window.** Suppose \(n\to\infty\), \(n/m\to0\) and \(\beta=1+\lambda/\sqrt n\), where \(\lambda\in\mathbb R\) is fixed. Then
\[
\left(\frac{S_B}{n^{3/4}},\ \frac{S_A}{\sqrt m}-\frac{\beta S_B}{\sqrt n}\right)
\ \Longrightarrow\ (X_\lambda,Z),
\]
where \(Z\) is standard normal and is independent of \(X_\lambda\), whose density is
\[
\frac{\exp(\lambda x^2-x^4/12)}{\int_{\mathbb R}\exp(\lambda u^2-u^4/12)\,du}.
\]
Consequently \(S_A/(\sqrt m\,n^{1/4})\Rightarrow X_\lambda\). The limiting scaled variances of both communities are \(v(\lambda)=\mathbb E X_\lambda^2>0\):
\[
\frac{\operatorname{Var}(S_B)}{n^{3/2}}\longrightarrow v(\lambda),\qquad
\frac{\operatorname{Var}(S_A)}{m\sqrt n}\longrightarrow v(\lambda).
\]
In particular, the critical window has width \(n^{-1/2}\), governed by the *smaller* class, and the majority magnetization scale is \(\sqrt m\,n^{1/4}\) rather than a power determined by the total population alone.

## Assumptions and scope
Every spin takes values \(\pm1\); there are no magnetic fields or within-class couplings. The cross-class Hamiltonian is exactly \(H=-\beta S_A S_B/\sqrt{mn}\) in dimensionless units. The factor \(1/\sqrt{mn}\) is essential: it keeps the linearized bipartite mean-field instability at \(\beta=1\) for unequal class sizes. The two classes are labelled, with \(A\) the larger one. Total variation means \(\frac12\sum_s|p(s)-q(s)|\). Constants \(C_L,n_L\) do not depend on \(m,n,\lambda\) within the stated ranges. Convergence statements use the thermodynamic limit along arbitrary integer sequences satisfying the assumptions; no rate of divergence of \(m/n\) beyond \(n/m\to0\) is required.

## Proof
**1. Exact elimination and comparison.** Fix \(S_B=s\). Summing independently over the \(m\) majority spins gives \((2\cosh(\beta s/\sqrt{mn}))^m\), proving the displayed finite marginal. Put \(h(x)=x^2/2-\log\cosh x\). The inequalities
\[
0\le h(x)\le x^4/12\qquad(x\in\mathbb R)
\]
follow from \(\tanh x\le x\) and, for \(x\ge0\), \(\tanh x\ge x-x^3/3\); the latter follows by differentiating, since \(x^2-\tanh^2x\ge0\). By symmetry the inequalities also hold for negative \(x\). Hence the marginal on \(s\) is the critical-window Curie–Weiss law \(Q=Q_{n,\beta^2}\) reweighted by
\[
w(s)=\exp\!\left[-m h\!\left(\frac{\beta s}{\sqrt{mn}}\right)\right],\qquad
0<w(s)\le1,\qquad
1-w(s)\le\frac{\beta^4s^4}{12mn^2}.
\]
The proof of the required uniform Curie–Weiss fourth-moment bound is given next.

**2. Critical-window moment lemma.** Uniformly for \(|\lambda|\le L\), \(\beta=1+\lambda/\sqrt n\), and sufficiently large \(n\),
\[
\mathbb E_{Q_{n,\beta^2}}|S_B|^k\le C_{k,L}n^{3k/4}
\]
for each fixed positive even integer \(k\). To see this, use the exact Hubbard–Stratonovich identity \(\exp(\beta^2s^2/(2n))=\mathbb E_G\exp(\beta Gs/\sqrt n)\), with \(G\) standard normal. The induced mixing density of \(G=z\) is proportional to
\[
\exp\!\left(\frac{\beta^2-1}{2}z^2-nh(\beta z/\sqrt n)\right).
\]
Elementary calculus gives a universal \(c>0\) for which \(h(x)\ge c\min(x^4,x^2)\): indeed \(h''(x)=\tanh^2 x\), which grows quadratically near zero and is bounded away from zero outside a fixed neighborhood. With \(\beta\in[1/2,2]\), the displayed density is bounded, up to an \(L\)-dependent multiplier, by \(\exp(-c'z^4/n)\) on \(|z|\le\sqrt n\) and \(\exp(-c'z^2)\) outside, after absorbing its \(O_L(z^2/\sqrt n)\) positive term. Its normalizing integral is at least \(c_Ln^{1/4}\), as follows by restricting to \(|z|\le n^{1/4}\), where the exponent is bounded below by an \(L\)-dependent constant. Therefore its fixed absolute moments satisfy \(\mathbb E|G|^k=O_{k,L}(n^{k/4})\). Conditional on \(G=z\), the spins are independent with mean \(\tanh(\beta z/\sqrt n)\); their centered sum has \(k\)-th absolute moment \(O_k(n^{k/2})\), while the conditional mean has magnitude at most \(2\sqrt n|z|\). Taking expectations proves the lemma. (The centered-sum bound follows, for example, by expanding products and retaining terms whose factors each appear at least twice.)

For \(\delta=\mathbb E_Q(1-w)\) the lemma gives \(0\le\delta\le C_Ln/m\). If \(\delta<1/2\), the identity \(dP/dQ=w/(1-\delta)\) yields \(\|P-Q\|_{\rm TV}\le\delta/(1-\delta)\le2\delta\). If \(\delta\ge1/2\), use \(\|P-Q\|_{\rm TV}\le1\le2\delta\). After enlarging \(C_L\), this establishes the claimed uniform bound.

**3. Quartic minority law.** The Curie–Weiss magnetization mass at \(s\equiv n\pmod2\) is proportional to \(\binom n{(n+s)/2}\exp(\beta^2s^2/(2n))\). For \(s=xn^{3/4}+O(1)\) with bounded \(x\), Stirling's formula uniformly on compact \(x\)-sets gives
\[
\log\!\left(2^{-n}\binom n{(n+s)/2}e^{\beta^2s^2/(2n)}\right)
=-\tfrac12\log(\pi n/2)+\lambda x^2-x^4/12+o(1).
\]
Indeed the binomial rate function has expansion \(I(y)=y^2/2+y^4/12+O(y^6)\), and \(\beta^2-1=2\lambda/\sqrt n+O_L(n^{-1})\). The global entropy inequality \(I(y)\ge y^2/2+y^4/12\), together with Stirling bounds away from \(|y|=1\), supplies integrable quartic tails after the same quadratic tilt, while the region \(|s|>n/2\) is exponentially negligible. The lattice spacing after scaling is \(2n^{-3/4}\), so the normalized mass converges to the displayed quartic density. Uniform higher moments follow from the preceding lemma. Since the bipartite minority law differs from \(Q\) by a weighting \(w\le1\) whose \(Q\)-mean tends to one, its weak limit and all fixed scaled moments agree with those of \(Q\).

**4. Gaussian transverse fluctuation.** Given \(S_B=s\), the majority spins are independent with mean \(t_s=\tanh(\beta s/\sqrt{mn})\). In the typical range \(|s|\le Rn^{3/4}\), this mean tends uniformly to zero because \(n/m\to0\). Their centered normalized sum thus tends uniformly in conditional characteristic functions to a standard normal. Also
\[
\left|\sqrt m\,t_s-\frac{\beta s}{\sqrt n}\right|
\le C\frac{|s|^3}{mn^{3/2}}
=O_R\left(\frac{n^{3/4}}m\right)\longrightarrow0.
\]
Tightness of \(S_B/n^{3/4}\) permits removal of the typical-range restriction. Integrating conditional characteristic functions proves joint convergence to the product of the quartic and standard Gaussian laws. It also gives \(S_A/(\sqrt m n^{1/4})\Rightarrow X_\lambda\). To establish the variance claim, use the uniform scaled moment bounds from Step 2, conditional independent-spin moment bounds, and the displayed conditional mean error to obtain uniform integrability of the squared normalized magnetizations. Spin-flip symmetry makes both means zero. This completes the proof.

## Verification
Run `python verify.py` with Python 3, NumPy, and SciPy. The program enumerates labelled spin configurations independently for \(2\le m\le7\), \(2\le n\le6\) and three coupling values; compares that enumeration with both grouped exact sums and the analytic marginal; checks finite-window total variation against the Curie–Weiss measure on four imbalanced-size pairs; and compares three finite-size critical-window second moments with the derived quartic integrals. Its current run passed 921 numerical assertions. This finite computation is a consistency check, not a proof of the infinite-size statements; Steps 1–4 provide that proof.

## Relationship to prior work
Gallo and Contucci (2007) introduced the broad two-population mean-field setting and solved its thermodynamic free-energy problem. Fedele and Contucci (2010) proved general multispecies magnetization scaling under a convex interaction matrix and fixed positive population proportions. Fedele (2013) proved a Gaussian–quartic decomposition for bipartite critical models under a positive-definite interaction matrix, and Kirsch and Toth (2018) addressed two positively proportioned groups. The present cross-only interaction matrix is indefinite, its cross coupling is scaled with \(\sqrt{mn}\), and its minority fraction tends to zero; the cited results do not directly yield the stated quantitative total-variation reduction or singular-size critical window. The classical one-species Curie–Weiss quartic limit and Hubbard–Stratonovich identity are used as established background, not claimed as inventions. A broader unlocated critical spin-system approximation theorem could still cover aspects of the result.

## Limitations
Only zero-field Ising spins, pure ferromagnetic cross-class interactions, the specified normalization, and the asymptotic regime \(n/m\to0\) are treated. The quantitative reduction is uniform in bounded critical windows but is **not** asserted for temperatures a fixed positive distance into the ordered phase. It does not establish kinetic mixing, metastable dynamics, quenched disorder, or arbitrary within-class interactions. Historical priority is not certified and independent scientific validation has not occurred.

## References
1. I. Gallo and P. Contucci, *Bipartite Mean Field Spin Systems: Existence and Solution*, arXiv:0710.0800, first public 2007-10-03. https://arxiv.org/abs/0710.0800
2. M. Fedele and P. Contucci, *Scaling Limits for Multispecies Statistical Mechanics Mean-Field Models*, arXiv:1011.3216, first public 2010-11-14. https://arxiv.org/abs/1011.3216
3. M. Fedele, *Rescaled Magnetization for Critical Bipartite Mean-Fields Models*, arXiv:1310.7615, first public 2013-10-28. https://arxiv.org/abs/1310.7615
4. W. Kirsch and G. Toth, *Critical Regime in a Curie-Weiss Model with Two Groups and Heterogeneous Coupling*, arXiv:1807.05020, first public 2018-07-13. https://arxiv.org/abs/1807.05020
