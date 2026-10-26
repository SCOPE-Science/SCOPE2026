# An exact separation principle and macroscopic thermal peak for two antiferromagnetic bonds on an Ising ring

## Finding
Fix a zero-field periodic nearest-neighbor classical Ising chain with \(n\ge4\) spins \(\sigma_i\in\{-1,+1\}\), two exchange bonds equal to \(-J\), and all other exchange bonds equal to \(+J\), where \(J>0\). If the two negative bonds cut the ring into arcs of \(\ell\) and \(n-\ell\) edges, define \(M=\sum_{i=0}^{n-1}\sigma_i\), \(t=\tanh(\beta J)\), and the temperature-rescaled, zero-field susceptibility \(X_{n,\ell}(t)=\operatorname{Var}_\beta(M)/n\). For \(0<t<1\), the exact expression is
\[
X_{n,\ell}(t)=
\frac{(1+t)(1-t^n)}{(1-t)(1+t^n)}-
\frac{8t(1-t^\ell)(1-t^{n-\ell})}{n(1-t)^2(1+t^n)}.
\]
At every positive finite temperature, and for fixed \(n,J\), the susceptibility is **strictly greatest when the negative bonds are adjacent** (\(\ell=1\) or \(n-1\)) and **strictly least when the bonds are as far apart as possible** (\(\ell=\lfloor n/2\rfloor\) or \(\lceil n/2\rceil\)). The extrema are unique up to dihedral symmetries of the ring.

For even \(n\ge6\) with antipodal negative bonds, \(X_{n,n/2}(0)=1\) and \(X_{n,n/2}(1)=0\), yet \(X_{n,n/2}(t)>1\) for all sufficiently small positive \(t\). Thus it has a strictly interior temperature peak, exceeding the infinite-temperature fluctuation level although the zero-temperature magnetization is identically zero.

Moreover, for \(x>0\) and \(t_n=\exp(-x/n)\),
\[
\lim_{\substack{n\to\infty\\n\ \mathrm{even}}}\frac{X_{n,n/2}(t_n)}{n}
=\Phi(x):=\frac{2\tanh(x/2)}{x}
-\frac{8\bigl(1-\operatorname{sech}(x/2)\bigr)}{x^2}.
\]
The limiting profile is strictly positive for \(x>0\), tends to zero at both ends of \((0,\infty)\), and determines the **globally optimized peak**, not just a selected scaling regime:
\[
\lim_{\substack{n\to\infty\\n\ \mathrm{even}}}
\frac1n\max_{0\le t\le1}X_{n,n/2}(t)
= c_*:=\max_{x>0}\Phi(x)>0.
\]
A numerical orientation value is \(c_*\approx0.13208531749\), realized near \(x\approx6.55065436\). No exact uniqueness assertion about the maximizer of \(\Phi\) is required or claimed. Every sequence of finite-size maximizers has \(-n\log t\) in a compact subset of \((0,\infty)\) for sufficiently large even \(n\).

## Assumptions and scope
The Hamiltonian is \(H(\sigma)=-J\sum_{i=0}^{n-1}\epsilon_i\sigma_i\sigma_{i+1}\), with \(\sigma_n=\sigma_0\), \(\epsilon_{\ell-1}=\epsilon_{n-1}=-1\) and \(\epsilon_i=1\) otherwise. Inverse temperature \(\beta\) is nonnegative, and the thermodynamic susceptibility to a physical field coupled as \(-hM\) is \(\chi=\beta X\). This theorem concerns \(X=\chi/\beta\), not a claim about the optimizer of \(\chi\) itself. Endpoints \(t=0,1\) mean limits \(\beta=0,\infty\), respectively. The quantity \(X\) is invariant under rotation and reflection, which interchange \(\ell\) and \(n-\ell\).

## Proof
**Gauge and covariance.** Since the product of the two negative edge signs is \(+1\), put \(g_i=1\) for \(0\le i<\ell\), \(g_i=-1\) for \(\ell\le i<n\), and \(\tau_i=g_i\sigma_i\). The transformed Hamiltonian is the standard zero-field ferromagnetic cycle, while \(M=\sum_i g_i\tau_i\). The high-temperature expansion gives partition function \(Z=2^n(\cosh\beta J)^n(1+t^n)\) and, for cyclic forward distance \(d\in\{0,\ldots,n\}\),
\[
\langle\tau_i\tau_{i+d}\rangle
=\frac{t^d+t^{n-d}}{1+t^n}=:C_d.
\]
Indeed a pair of insertion vertices can be joined by either one of the two complementary arcs; in the partition expansion the only even subgraphs are the empty set and the full cycle. Symmetry gives \(\langle M\rangle=0\), hence \(X=n^{-1}\sum_{i,j}g_i g_j C_{j-i}\).

**Exact finite formula.** The all-plus variance equals \(\sum_{d=0}^{n-1}C_d=(1+t)(1-t^n)/[(1-t)(1+t^n)]\). Changing signs across the two blocks subtracts four times the block-crossing unordered correlation sum divided by \(n\). Since
\[
\sum_{i=0}^{\ell-1}\sum_{j=\ell}^{n-1}t^{j-i}
=\frac{t(1-t^\ell)(1-t^{n-\ell})}{(1-t)^2},
\]
with the complementary-distance sum identical, the subtraction is exactly the second displayed term. This proves the finite formula for all stated parameters.

**Strict placement extrema and endpoints.** For fixed \(t\in(0,1)\), the arrangement-dependent factor is \((1-t^\ell)(1-t^{n-\ell})=1+t^n-(t^\ell+t^{n-\ell})\). Its discrete increment is
\[
(1-t^{\ell+1})(1-t^{n-\ell-1})-(1-t^\ell)(1-t^{n-\ell})
=(1-t)(t^\ell-t^{n-\ell-1})>0
\]
for \(1\le\ell<(n-1)/2\). Thus \(X\) strictly decreases until the midpoint, establishing every equality case. As \(t\uparrow1\), the transformed spins become perfectly aligned, so \(X_{n,\ell}(1)=(n-2\ell)^2/n\). In particular, the antipodal even case has zero variance. At \(t=0\), spins are independent and \(X=1\). From the exact formula, \(\frac{d}{dt}X_{n,n/2}(0)=2-8/n>0\) for even \(n\ge6\); by continuity and the zero low-temperature limit, an interior global maximum exceeds one.

**Scaling and global optimization.** With even \(n\) and \(t=e^{-x/n}\), substitute into the exact formula and use \(n(1-e^{-x/n})\to x\). Straight simplification gives \(\Phi\), uniformly on every compact positive \(x\)-interval. For positivity, in continuum coordinates \(u,v\in[0,1)\) the limiting covariance kernel is \(K_x(d)=(e^{-xd}+e^{-x(1-d)})/(1+e^{-x})\) at circular distance \(d\in[0,1]\). Its Fourier coefficients are \(2x\tanh(x/2)/(x^2+4\pi^2k^2)>0\). The two-block sign function has a nonzero odd-frequency Fourier coefficient, so its quadratic form \(\Phi(x)\) is strictly positive. Direct expansion gives \(\Phi(x)=x^2/48+O(x^4)\) as \(x\downarrow0\) and \(\Phi(x)=2/x+O(x^{-2})\) as \(x\to\infty\).

It remains to show that the maximum cannot escape the scaling window. Put \(x=-n\log t\), for \(0<t<1\). The antiphase sign function has zero sum. As \(\operatorname{sech}(x/2)\le C_d\le1\),
\[
0\le\frac{X_{n,n/2}(t)}n\le1-\operatorname{sech}(x/2),
\]
which tends uniformly to zero for \(x\downarrow0\). At the other end, the ferromagnetic covariance dominates the signed quadratic form by positivity of each entry, so
\[
0\le\frac{X_{n,n/2}(t)}n
\le\frac{1+t}{n(1-t)}\le\frac2x+\frac2n.
\]
The last bound follows from \(1-e^{-u}\ge u/(1+u)\). Thus for any fixed positive candidate \(x\) with \(\Phi(x)>0\), all maximizing \(x\)-values eventually stay away from zero and infinity. Uniform convergence on this compact interval yields the full asymptotic maximum formula and compactness of optimizer sequences. The endpoints \(t=0,1\) cannot maximize when even \(n\ge6\). This completes the proof.

## Verification
The included standard-library program `verify_two_defect_ising.py` exhaustively enumerates spin configurations for all \(4\le n\le12\), all defect separations, and three independent exactly representable positive temperatures. It made 189 exact-rational variance-to-formula comparisons, checked strict separation order and rotation symmetry, checked the high-temperature endpoint and interior overshoot, and tested convergence of six increasing even ring sizes to the displayed profile. These finite tests corroborate the formula but do not substitute for the analytical all-size proof or establish uniqueness of a limiting profile maximizer.

## Relationship to prior work
The zero-field transfer-matrix and spin-correlation methods are classical. Turban (2016) treats more general contiguous multispin interactions, deriving partition functions and correlations, but the inspected paper does not study two localized negative two-spin exchanges, their spacing extremum, or the present macroscopic peak coefficient. Karl'ová and Strečka (2026) derive magnetic response curves of homogeneous antiferromagnetic chains under open and periodic boundaries, including compensated even rings; their uniform negative-exchange model has a different bond inventory and does not imply the two-defect placement formula or its \(n\)-order fluctuation peak. The novelty claim is the combined two-bond spacing classification and proved global finite-size scaling of the optimized fluctuation susceptibility; it is not a claim to have invented the transfer-matrix method or all finite-temperature susceptibility peaks. A broader historical inhomogeneous-bond calculation might encompass the result, and independent originality checking has not been performed.

## Limitations
Only exactly two negative bonds of the same magnitude as the positive bonds, zero applied field, and equilibrium classical Ising spins are covered. The thermodynamic field-response susceptibility differs by the factor \(\beta\); its maximizing temperature is not classified here. The coefficient \(c_*\) is characterized by a one-variable maximum, with only an illustrative numerical evaluation, and uniqueness of its optimizer is left unproved. No claim is made about disordered bond strengths, higher-dimensional lattices, dynamical mixing, or phase transitions at positive temperature.

## References
1. L. Turban, "One-dimensional Ising model with multispin interactions," *Journal of Physics A* **49**, 355002 (2016); first preprint 2016-05-17, arXiv:1605.05199, https://arxiv.org/abs/1605.05199.
2. K. Karl'ová and J. Strečka, "Open and Periodic Boundary Conditions in Statistical Mechanics: A Case Study of the Antiferromagnetic Ising Chain," *Entropy* **28**, 727 (2026), DOI 10.3390/e28070727; open preprint https://www.preprints.org/manuscript/202606.0271.
