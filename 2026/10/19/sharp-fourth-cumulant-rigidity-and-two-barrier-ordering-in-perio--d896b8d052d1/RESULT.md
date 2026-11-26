# The harmonic-coordinate variance gives the exact fourth-cumulant excess on a periodic bond walk

## Finding

Let \(X_t\) be the continuous-time nearest-neighbor walk on \(\mathbb Z\) with rate \(c_j>0\) in either direction across edge \((j,j+1)\), repeated with integer period \(n\ge3\). Write \(r_j=1/c_j\), \(R=\sum_{j=0}^{n-1}r_j\), and \(\pi\) for the uniform law on the residue classes. Let \(\chi\) be the unique mean-zero periodic corrector for which \(x+\chi(x\bmod n)\) is harmonic. Equivalently,
\[
\chi(j+1)-\chi(j)=\frac{n}{R}r_j-1,\qquad \sum_j\chi(j)=0.
\]
For the cumulant rates \(\kappa_m=\lim_{t\to\infty}t^{-1}\operatorname{cum}_m(X_t-X_0)\), the exact excess over the homogeneous fourth-to-second ratio is
\[
\boxed{\frac{\kappa_4}{\kappa_2}-1=12\operatorname{Var}_\pi(\chi).}
\]
In particular, if \(S_j=\sum_{i<j}(r_i-R/n)\) for \(0\le j<n\) and \(\bar S=n^{-1}\sum_jS_j\), the right-hand side is \(12nR^{-2}\sum_j(S_j-\bar S)^2\). This gives the exact profile-dependent deviation, not just an envelope for it, without computing any eigenvalues or using a small-contrast approximation.

## Assumptions and scope

All rates are finite and strictly positive, and symmetry is across each undirected bond, not just the absence of a net steady-state current. Displacement is unwrapped and lattice steps have length one. The ratio uses rates of cumulants, not finite-time kurtosis. The initial site may be arbitrary and fixed. No analogous claim is made about biased walks, random nonperiodic environments, higher cumulants or other geometries.

## Proof

**Corrector.** Across an edge the positive oriented increment of \(x+\chi(x)\) is \((n/R)r_j\). Multiplication by the local rate gives the same flux \(n/R\) across every edge; right and left contributions cancel at each site. Conversely, harmonicity forces a constant flux, and the sum of the increments across a period is \(n\). This proves the expression and uniqueness with the mean-zero convention. The residue generator is symmetric, so the stationary law \(\pi\) is uniform.

**Spectral reduction to an effective-resistance sum.** Let \(L_k\) be the tilted residue generator with forward and backward off-diagonal factors \(e^k,e^{-k}\), respectively, and the unchanged escape-rate diagonal. Its analytic eigenvalue \(\lambda(k)\) issuing from zero gives the cumulant rates. Indeed the simple eigenvalue is separated from the rest at zero. For \(k\) near zero the dominant spectral term in the moment generating function at any starting site is \(a(k)e^{t\lambda(k)}\), with \(a\) analytic, \(a(0)=1\), and a remainder exponentially smaller on a sufficiently small neighborhood of zero. Thus the derivatives per unit time converge to those of \(\lambda\).

Write \(C=\prod_jc_j\) and \(P(z)=\det(zI-L_0)\). The established unicyclic characteristic-polynomial relation of Pietzonka, Barato and Seifert [1, Appendix C, Eqs. (C5)–(C6)] gives
\[
P(\lambda(k))=2C[\cosh(nk)-1].
\]
Here products of a forward and backward traversal cancel the tilt, and the only tilt-dependent permutation terms are the two directed full circuits. This also verifies the normalization \(nk\) for lattice displacement rather than the winding number.

Let \(\mu_1,\ldots,\mu_{n-1}>0\) be the nonzero eigenvalues of \(-L_0\). The matrix-tree identity gives \(P'(0)=nCR\): deleting edge \(i\) gives a tree of weight \(Cr_i\), with \(n\) choices of root. Thus, with \(T=\sum_j\mu_j^{-1}\),
\[
P(z)=nCR\bigl(z+Tz^2+O(z^3)\bigr).
\]
Comparing powers at zero gives \(\lambda(k)=(n/R)k^2+[n^3/(12R)-Tn^2/R^2]k^4+O(k^6)\). If \(K=\sum_{i<j}R_{\rm eff}(i,j)\) on the weighted residue cycle, then \(K=nT\): sum \((e_i-e_j)^\mathsf T(-L_0)^+(e_i-e_j)\) over \(i<j\), using \(\sum_{i<j}(e_i-e_j)(e_i-e_j)^\mathsf T=nI-\mathbf1\mathbf1^\mathsf T\). In particular,
\[
\kappa_2=2n/R,\qquad \frac{\kappa_4}{\kappa_2}=n^2-\frac{12K}{R}.
\]
This spectral expression is an application of the known winding determinant, not the new identity by itself.

**Exact variance deficit.** For \(d\in\{1,\ldots,n-1\}\), the forward arc from \(i\) to \(i+d\) has resistance
\[
A_{i,d}=\frac{R}{n}\bigl(d+\chi(i+d)-\chi(i)\bigr),
\]
and the two parallel arcs have effective resistance \(A_{i,d}(R-A_{i,d})/R\). Expanding this product and summing over \(i\) for each \(d\), the linear term cancels by periodicity. Each unordered pair of vertices appears twice. The homogeneous reference at total resistance \(R\) contributes \(\frac{R}{2n}\sum_{d=1}^{n-1}d(n-d)=R(n^2-1)/12\), and
\[
\begin{aligned}
K&=\frac{R(n^2-1)}{12}-\frac{R}{2n^2}\sum_{i=0}^{n-1}\sum_{d=1}^{n-1}[\chi(i+d)-\chi(i)]^2\\
 &=\frac{R(n^2-1)}{12}-R\operatorname{Var}_\pi(\chi).
\end{aligned}
\]
The second line uses the ordered pair identity \(\sum_{i,j}(\chi_j-\chi_i)^2=2n^2\operatorname{Var}_\pi(\chi)\). Substitution gives the claimed exact excess. It vanishes precisely for a constant corrector, which by its increment formula means a homogeneous bond profile.

## Verification

Run `python verify.py` with SymPy. It compares the identity with exact rational perturbation of the full tilted generator through order four, checks harmonicity and the effective-resistance deficit independently on the same finite profiles, and includes homogeneous and nonhomogeneous cases. This is supporting arithmetic; the proof above applies to all stated periods and profiles.

## Relationship to prior work

Pietzonka, Barato and Seifert [1, Eq. (53)] bound the equilibrium winding generating function by two hyperbolic cosine functions sharing its second-order coefficient. Since lattice displacement is \(n\) times winding up to a bounded residue term, comparing fourth-order coefficients already yields the enclosing inequalities \(1\le\kappa_4/\kappa_2\le n^2\) in lattice units. That bound is prior coverage, not a new contribution here. The winding determinant is likewise prior [1, Appendix C]. Ptaszyński [2, Sec. III E] compares skewness and normalized fourth cumulant in more general unicyclic models. Gerry and Segal [3, Eq. (16)] give an exact alternating two-bond fourth cumulant and longer-period numerics. The exact two-bond placement dependence on the cycle is an effective-resistance calculation, covered at that level by the weighted-ring spacing identity in [4]; no separate spacing result is claimed here. The distinct statement studied above is the positive corrector-variance expression for the exact excess for arbitrary profiles, not the hyperbolic cosine bounds, the determinant method, or the effective-resistance definition. Historical priority cannot be ruled out for uninspected work on fourth-order transport in disordered or periodic media, including [5].

## References

1. P. Pietzonka, A. C. Barato and U. Seifert, *Universal bounds on current fluctuations*, Phys. Rev. E **93**, 052145 (2016), DOI:10.1103/PhysRevE.93.052145, arXiv:1512.01221.
2. K. Ptaszyński, *Bounds on skewness and kurtosis of steady state currents*, arXiv:2204.08421.
3. M. Gerry and D. Segal, *Random walks on modular chains: Detecting structure through statistics*, arXiv:2305.09759.
4. *Sharp defect-spacing laws for continuous-time diffusion on weighted rings*, [published record](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-sharp-defect-spacing-laws-for-continuous-time-diffusion-on-weigh--962eb926e664), edge-pair expansion.
5. E. Hernández-García et al., *Transport properties for random walks in disordered one-dimensional media*, Phys. Rev. B **42**, 10653 (1990), DOI:10.1103/PhysRevB.42.10653 (abstract comparison only).
