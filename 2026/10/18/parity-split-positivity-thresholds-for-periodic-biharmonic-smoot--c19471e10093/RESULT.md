# Parity-split positivity thresholds for periodic biharmonic smoothing

## Finding

Let \(n\ge5\), let \(S_n\) cyclically shift the coordinates of \(\mathbb R^n\), and set \(L_n=2I-S_n-S_n^{-1}\). The periodic second-difference least-squares smoother is
\[
T_n(t)=(I+tL_n^2)^{-1},\qquad t\ge0.
\]
It fixes constants, and thus is range-preserving on every bounded real input precisely when its matrix is entrywise nonnegative. Define the *eventual positivity threshold*
\[
t_n^*=\inf\{b\ge0:T_n(t)\text{ is entrywise nonnegative for every }t\ge b\}.
\]
Every \(t_n^*\) is finite and strictly positive. Let \(\rho\in(\pi/2,\pi)\) be the unique zero of \(\tan\rho+\tanh\rho\), and put
\[
c_*={1\over64\rho^4}=0.00049943673351347\ldots,\qquad D_m=1+c_*(2\pi m)^4.
\]
The following absolutely convergent sums define three real constants:
\[
\Gamma=-2\sum_{m=1}^{\infty}{(-1)^m(2\pi m)^4\over D_m^2}>0,\quad
H={64c_*\pi^6\over3}\sum_{m=1}^{\infty}{(-1)^m m^6\over D_m^2}<0,\quad
K=-2\sum_{m=1}^{\infty}{(-1)^m(2\pi m)^2\over D_m}>0.
\]
Then, as \(n\to\infty\) **within the indicated parity class**,
\[
\boxed{\quad t_n^*=c_*n^4+\begin{cases}-H\,n^2/\Gamma+o(n^2),&n\text{ even},\\[-2pt]-(H+K/8)\,n^2/\Gamma+o(n^2),&n\text{ odd}.\end{cases}\quad}
\]
In fact, the coefficients have the additional **closed expressions**
\[
\boxed{\beta_{\mathrm{even}}=\frac{\tanh\rho(3-\rho\tanh\rho)}{48\rho^3}>0,\qquad
\beta_{\mathrm{odd}}=-\frac{\tanh^2\rho}{48\rho^2}<0.}
\]
Their difference is \(K/(8\Gamma)=\tanh\rho/(16\rho^3)>0\). Numerically they are approximately \(0.00104656691\) and \(-0.00359547329\), respectively. The leading constant is a classical *continuous* fourth-order positivity threshold; the finding is the **finite-cycle parity correction** and its sharp interpretation for periodic penalized smoothing, not the first appearance of \(\rho\).

## Assumptions and scope

The cycle carries the unnormalized nearest-neighbor Laplacian \(L_n\). Both the squared-difference penalty and the quadratic data-fidelity term have unit lattice weights; an arbitrary coefficient is absorbed into \(t\). The finite operator is a real symmetric circulant matrix, and \(t\) is nonnegative. Positivity always means entrywise nonnegativity of the inverse and is stronger than positive semidefiniteness. The assertion concerns the eventual threshold, not uniqueness of every individual zero of a finite matrix entry. No claim is made for open-ended smoothing or for general irregular weighted cycles.

## Proof

**1. Finite resolvent and nontriviality.** The Fourier eigenvalues of \(L_n\) are \(4\sin^2(\pi m/n)\) for \(0\le m<n\). Thus its cyclic convolution kernel is
\[
k_{n,t}(j)={1\over n}\sum_{m=0}^{n-1}{\cos(2\pi mj/n)\over1+16t\sin^4(\pi m/n)},\qquad 0\le j<n.
\]
Every row sums to one. For \(n\ge5\), the distance-two entry of \(L_n^2\) is \(1\), so \(k_{n,t}(2)=-t+O_n(t^2)<0\) for small positive \(t\). Conversely, \(T_n(t)\to\mathbf 1\mathbf 1^{\mathsf T}/n\) as \(t\to\infty\). Hence \(0<t_n^*<\infty\). For any real matrix with row sum one, entrywise nonnegativity is equivalent to \(\ell^\infty\)-contraction; by the same observation it is equivalent to preservation of all intervals \([a,b]\).

**2. Periodic continuum Green kernel and its known threshold.** For \(c>0\) define
\[
G_c(x)=\sum_{m\in\mathbb Z}{e^{2\pi imx}\over1+c(2\pi m)^4},\qquad x\in\mathbb R/\mathbb Z.
\]
It solves \(cG_c^{(4)}+G_c=\delta_0\) periodically and has integral one. Put \(s=1/(\sqrt2\,c^{1/4})\), \(a=s/2\), \(z=s(1/2-x)\) for \(0\le x\le1/2\), and
\[
U(z)=\sinh z\cos z-\cosh z\sin z,\qquad V(z)=\sinh z\cos z+\cosh z\sin z.
\]
Solving the homogeneous equation on the half circle with \(G'_c(1/2)=G'''_c(1/2)=G'_c(0)=0\) and the jump condition \(2cG_c'''(0+)=1\) gives
\[
G_c(x)=s\,{V(a)\cosh z\cos z-U(a)\sinh z\sin z\over U(a)^2+V(a)^2}.
\]
In particular \(G_c(1/2)=sV(a)/(U(a)^2+V(a)^2)\). The first positive root of \(V\) is \(\rho\), characterized by \(\tan\rho=-\tanh\rho\), and it lies between \(\pi/2\) and \(\pi\). On \((0,\rho)\) one has \(V>0\) and
\[
\big(U/V\big)'=-{\sinh(2z)-\sin(2z)\over V(z)^2}<0.
\]
Consequently the displayed kernel is positive and strictly decreasing in \(x\in(0,1/2)\) for \(a<\rho\), and at \(a=\rho\) its only zero occurs at the antipode \(x=1/2\). To see that no later positivity interval is possible, suppose \(a>\rho\) and \(G_c\ge0\). Since \(G_c^{(4)}=-G_c/c\) away from the origin and \(G_c'''(1/2)=0\), \(G_c'\) is strictly convex with zero endpoint values; hence the derivative with respect to \(z\) must be positive for \(0<z<a\). But \(G_c(1/2)\ge0\) implies \(V(a)\ge0\), and at \(z=\rho\) the exact derivative equals \(sV(a)U(\rho)/(U(a)^2+V(a)^2)\le0\), a contradiction. Therefore
\[
G_c(x)\ge0\text{ for all }x\quad\Longleftrightarrow\quad c\ge c_*=1/(64\rho^4).
\]
This continuum threshold is included to identify the correct scaling and is acknowledged as previously known.

**3. Uniform discrete-to-continuum expansion.** Put \(F_n(c,j)=n k_{n,cn^4}(j)\). Uniformly for \(c\) in a compact subinterval of \((0,\infty)\) and \(0\le j<n\),
\[
F_n(c,j)=G_c(j/n)+n^{-2}H_c(j/n)+o(n^{-2}),\qquad
H_c(x)={32c\pi^6\over3}\sum_{m\ne0}{m^6 e^{2\pi imx}\over[1+c(2\pi m)^4]^2}.
\]
Indeed, for each fixed integer \(m\), the discrete fourth-power symbol has the expansion
\[
16n^4\sin^4(\pi m/n)=(2\pi m)^4-{32\pi^6m^6\over3n^2}+O(m^8n^{-4}).
\]
Grouping \(m\) and \(-m\) in the discrete Fourier sum gives the indicated correction. To justify its uniformity, for \(1\le|m|\le n/2\) use \(\sin(\pi|m|/n)\ge2|m|/n\) to bound the scaled difference of reciprocal symbols by \(C|m|^{-2}\), uniformly on the chosen \(c\)-compact set. Dominated convergence controls its sum and permits termwise parameter differentiation. The omitted continuum modes have total size \(O(n^{-3})\). The same estimate, applied to derivatives in \(c\), holds locally uniformly.

**4. Nondegenerate antipodal minimum.** At \(c=c_*\) the unique minimum of \(G_c\) is the quadratic zero at \(x=1/2\). Denote
\[
\Gamma=\partial_cG_c(1/2)|_{c=c_*},\qquad
H=H_{c_*}(1/2),\qquad K=\partial_x^2G_{c_*}(1/2).
\]
The Fourier definitions in the finding follow by absolute differentiation. The closed expression gives \(\Gamma>0\): since \(V'(\rho)=2\cosh\rho\cos\rho<0\) and \(da/dc<0\), the antipodal Green value increases with \(c\) at its first zero. Also \(K>0\) because \(G_{c_*}\) is positive away from its symmetric, nondegenerate antipodal minimum: more explicitly the small-\(z\) expansion at \(V(\rho)=0\) yields a positive quadratic coefficient proportional to \(-U(\rho)>0\). There are useful exact relations. First the symbol expansion gives \(H_c=(c/6)\,\partial_c\partial_x^2G_c\). At the critical parameter, \(s=2\rho\), \(U(\rho)=-2\cosh\rho\sin\rho\), and \(U'(\rho)/U(\rho)=\tanh\rho\). Consequently differentiating \(G_c''(1/2)=-2s^3U(a)/(U(a)^2+V(a)^2)\) yields
\[
H=-\frac K{24}(3-\rho\tanh\rho)<0.
\]
Direct differentiation of \(G_c(1/2)=sV(a)/(U(a)^2+V(a)^2)\) gives
\[
\frac K\Gamma=\frac{\tanh\rho}{2\rho^3}.
\]
These identities prove both signs in the finding and reduce the second-order coefficients to the displayed elementary expressions in \(\rho\).

**5. Discrete grid parity and eventual positivity.** Fix bounded \(\tau\) and write \(c=c_*+\tau/n^2\). For lattice indices with bounded \(\ell=j-n/2\), the uniform expansion and Taylor's theorem give
\[
n^2 F_n(c,j)=\Gamma\tau+H+{K\over2}\ell^2+o(1).
\]
The allowed \(\ell\)'s are integers for even \(n\) and half-integers for odd \(n\), yielding respective lowest quadratic penalties \(0\) and \(K/8\). To pass from this local formula to the minimum over all \(j\), use the strict positivity of \(G_{c_*}\) away from the antipode, the lower quadratic bound near it, and boundedness of \(H_c\). This first excludes all lattice points outside an arbitrarily fixed antipodal neighborhood and then excludes \(|\ell|\to\infty\) on the critical scale. Thus the minimum has the stated two parity profiles, uniformly for bounded \(\tau\).

For \(c\) in any compact interval strictly above \(c_*\), the continuum kernel has a positive minimum, so all sufficiently fine discretizations are entrywise positive. For all sufficiently large \(c\), the nonconstant Fourier contribution to \(F_n\) is bounded by \(C/c\) uniformly in \(n\): pair modes around zero and use \(n\sin(\pi m/n)\ge2\min(m,n-m)\). Hence large \(c\) are uniformly positive as well. Conversely any fixed \(c<c_*\) with a negative continuum kernel value yields negative discrete entries for large \(n\). The local asymptotics therefore locate the *last* loss of positivity, not merely a sampled zero, and imply the displayed expansion of \(t_n^*=n^4 c\).

## Verification

Run `python3 CHECK.py` from the same directory as this document. The standard-library checker reconstructs the cyclic matrix and its inverse by Gauss–Jordan elimination, compares it to the independent Fourier formula, checks the closed periodic Green expression against rapidly convergent Fourier sums, and tests finite positivity windows and both parity asymptotics. It reports `CHECK_OK 1604 assertions` in the recorded execution. These finite computations support but do not replace the infinite-dimensional uniform estimates and local perturbation proof.

## Relationship to prior work

The positive Green-kernel parameter \(\rho\) is **not new**. Cabada's periodic fourth-order inverse-positivity interval (reported explicitly by Lu, Ma and Chen, 2019, Lemma 2) contains the identical continuous threshold after reparameterization. Cabada and Saavedra's 2017 spectral analysis independently displays the same transcendental root for another fourth-order boundary setup. Ulm's earlier work examines resolvent positivity of the biharmonic operator, and Grunau–Robert–Sweers examine lower estimates for continuous biharmonic Green functions. None of the inspected full texts states the finite cyclic discrete parity splitting or the \(n^2\) correction. The related published result on open-end Whittaker–Henderson smoothing concerns a different boundary geometry and establishes a contrasting failure of universal range preservation at all smoothing strengths; it does not supply a threshold for periodic closure. This comparison does not establish exhaustive historical priority.

## Limitations

The statement treats the uniform periodic second-difference penalty, not arbitrary graphs or boundary conditions. It establishes a two-term asymptotic for the *eventual* positivity threshold; it does not classify every positivity interval of a fixed \(n\), nor give an exact finite-\(n\) closed form for that threshold. The classical continuous threshold has prior art. Numerical checking is finite. Full historical priority remains uncertain, especially because not all older biharmonic resolvent publications could be read in full; the cited period-fourth-order primary paper could be examined in full.

## References

1. Michael Ulm, *The interval of resolvent-positivity for the biharmonic operator*, Proceedings of the American Mathematical Society, DOI: 10.1090/S0002-9939-99-04556-6; bibliographic first-public date recorded as 1998-11-18, https://portal.mardi4nfdi.de/wiki/The_interval_of_resolvent-positivity_for_the_biharmonic_operator.
2. Yanqiong Lu, Ruyun Ma, Tianlan Chen, *Global Bifurcation for Fourth-Order Differential Equations with Periodic Boundary-Value Conditions*, Mathematical Notes **106** (2019), 248–257, DOI: 10.1134/S0001434619070289; full text https://www.researchgate.net/publication/335446103_Global_Bifurcation_for_Fourth-Order_Differential_Equations_with_Periodic_Boundary-Value_Conditions.
3. Alberto Cabada and Lorena Saavedra, *Characterization of constant sign Green's function of a two point boundary value problem by means of spectral theory*, arXiv:1704.00644v1 (2017), https://arxiv.org/html/1704.00644v1.
4. Hans-Christoph Grunau, Frédéric Robert, Guido Sweers, *Optimal estimates from below for biharmonic Green functions*, arXiv:1103.0651v1 (2011), https://arxiv.org/abs/1103.0651.
5. Ahlème Bouakkaz and collaborators, *Green's functions for the fourth-order differential equations* (2019), accessible paper in the examined literature; its real-characteristic-root setting is distinct from the present oscillatory kernel.
