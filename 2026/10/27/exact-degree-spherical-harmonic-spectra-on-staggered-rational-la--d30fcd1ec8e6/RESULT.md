# Exact-degree spherical harmonic spectra on staggered rational-latitude double rings

## Finding
Let \(N\ge3\) be an integer and let \(c=p/q\in(0,1)\) be reduced, with \(q\) a positive even integer. On \(S^2\), consider the two staggered latitude rings
\[
 X_{N,c}=\left\{\left(\sqrt{1-c^2}\cos\frac{2\pi j}{N},\sqrt{1-c^2}\sin\frac{2\pi j}{N},c\right):0\le j<N\right\}
 \cup\left\{\left(\sqrt{1-c^2}\cos\frac{(2j+1)\pi}{N},\sqrt{1-c^2}\sin\frac{(2j+1)\pi}{N},-c\right):0\le j<N\right\}.
\]
Let \(\mathcal H_\ell\) be the complex degree-exactly-\(\ell\) spherical harmonics, orthonormalized in \(L^2(S^2,d\sigma)\) for probability surface measure, and let \(E_\ell:\mathcal H_\ell\to\mathbb C^{2N}\) be point evaluation divided by \(\sqrt{2\ell+1}\). The eigenvalues of \(G_\ell=E_\ell E_\ell^*\), including all zeros, are as follows.

For every integer \(m\) with \(|m|\le\ell\), define the strictly positive rational number
\[
 a_{\ell,m}(c)=\frac{(\ell-|m|)!}{(\ell+|m|)!}(1-c^2)^{|m|}\left(\frac{d^{|m|}}{dt^{|m|}}P_\ell(t)\bigg|_{t=c}\right)^2,
\]
where \(P_\ell\) is the Legendre polynomial with \(P_\ell(1)=1\).

* If \(N\) is odd, the spectrum is
\[
 \left\{2N\sum_{\substack{-\ell\le m\le\ell\\m\equiv r\ (\mathrm{mod}\ N)}}a_{\ell,m}(c):r=0,\ldots,N-1\right\}\ \cup\ \{0\}^{N}.
\]
* If \(N\) is even, the spectrum consists of the \(2N\) (possibly zero) numbers
\[
 \left\{2N\sum_{\substack{-\ell\le m\le\ell\\ m=r+kN\text{ for some }k\equiv h\ (\mathrm{mod}\ 2)}} a_{\ell,m}(c):r=0,\ldots,N-1,\ h=0,1\right\}.
\]
In these formulas an empty sum is zero; each displayed entry contributes its multiplicity.

In particular, the *exact rank at every degree* is
\[
 \boxed{\operatorname{rank}E_\ell=\begin{cases}\min(2\ell+1,N),&N\text{ odd},\\\min(2\ell+1,2N),&N\text{ even}.\end{cases}}
\]
For odd \(N\), the antipodal-parity-compatible output space has dimension \(N\), and full rank holds from the sharp degree \(\ell=(N-1)/2\) onward. For even \(N\), the full \(2N\)-dimensional output becomes attainable precisely from the sharp degree \(\ell=N\) onward. Hence changing the parity of \(N\) doubles the ultimate sampled-data dimension and changes the full-rank onset. All strictly positive Gram eigenvalues are rational; the normalization gives \(\operatorname{tr}G_\ell=2N\). The eligible rational heights are dense in \((0,1)\), giving explicit *fixed configurations* with maximal attainable rank simultaneously for infinitely many degrees, not merely a generic-position statement. For instance, \(N=3\), \(c=1/2\), and \(\ell=1\) produce eigenvalues \(3/2,9/4,9/4,0,0,0\).

## Assumptions and scope
The two rings have nonzero opposite heights \(\pm c\) and a relative rotation of exactly \(\pi/N\). No generic-position assumption is made. The reduced rational height has even denominator, so its numerator is odd. \(N\ge3\) and \(\ell\ge0\). Singular-value squares refer to normalized evaluation \(E_\ell\) with unweighted counting norm on \(\mathbb C^{2N}\); changing that normalization rescales all eigenvalues. For odd \(N\), the point set is antipodal; the rank assertion concerns its parity-compatible data, not arbitrary independent data at all \(2N\) points. The theorem neither promises a degree-independent lower positive eigenvalue nor stable interpolation uniformly in degree.

## Proof
**1. Fourier columns.** For the standard orthonormal basis \(Y_\ell^m\) with \(-\ell\le m\le\ell\), write the upper-ring azimuths as \(\phi_j=2\pi j/N\). The column of \(E_\ell\) indexed by \(m\), up to an irrelevant unit scalar, has entries
\[
 \sqrt{a_{\ell,m}(c)}e^{im\phi_j},\qquad \sqrt{a_{\ell,m}(c)}q_m e^{im\phi_j},\quad q_m=(-1)^{\ell+m}e^{im\pi/N},
\]
respectively on the upper and lower rings. This follows from the standard associated-Legendre normalization and \(P_\ell^{|m|}(-c)=(-1)^{\ell+|m|}P_\ell^{|m|}(c)\), with \(m\) and \(|m|\) having the same parity. The columns have squared norm \(2N a_{\ell,m}(c)\).

**2. Cyclic diagonalization.** The \(N\)-point discrete Fourier transform in \(j\), applied independently to each ring, separates the Gram matrix into \(N\) Hermitian blocks of size \(2\times2\), indexed by \(r=m\bmod N\). In the \(r\)-th block the column of order \(m\equiv r\) becomes \(\sqrt{Na_{\ell,m}}(1,q_m)^\mathsf T\). Its phase changes under the next alias according to
\[
 q_{m+N}=(-1)^{N+1}q_m.
\]
For odd \(N\), all aliases in the same residue have the same phase, giving a rank-one block whose eigenvalues are \(2N\sum_{m\equiv r}a_{\ell,m}\) and zero. For even \(N\), consecutive aliases have opposite phases; the vectors \((1,q_r)^\mathsf T\) and \((1,-q_r)^\mathsf T\) are orthogonal, with eigenvalues \(2N\) times the separate even- and odd-alias sums. This gives the exact spectral lists, including multiplicity.

**3. Arithmetic nonvanishing at every degree.** Put \(s=\nu_2(q)\ge1\). We prove \(P_\ell^{(k)}(c)\ne0\) for every \(0\le k\le\ell\). The standard derivative identity gives
\[
 P_\ell^{(k)}(t)=(2k-1)!!\,C_{\ell-k}^{k+1/2}(t),
\]
with \((-1)!!=1\), where \(C_n^\alpha\) is a Gegenbauer polynomial. For \(n=\ell-k\), its leading coefficient is
\[
 L_{n,k}=\frac{\prod_{u=0}^{n-1}(2k+2u+1)}{n!}.
\]
All factors in the numerator are odd. For \(j\ge1\), the coefficient of \(t^{n-2j}\), divided by \(L_{n,k}\), equals
\[
 (-1)^j\binom n{2j}\frac{(2j-1)!!}{\prod_{u=n-j}^{n-1}(2k+2u+1)},
\]
which has nonnegative two-adic valuation. Since \(\nu_2(c)=-s\), the leading monomial at \(c\) has valuation \(-\nu_2(n!)-ns\), strictly smaller than every lower monomial by at least \(2s\). Uniqueness of the least two-adic valuation proves that the Gegenbauer value, and hence every derivative, is nonzero. Consequently all \(a_{\ell,m}(c)\) are strictly positive, with no appeal to finite testing.

**4. Rank and sharpness.** An alias sum is positive precisely when its congruence class contains an integer \(m\in[-\ell,\ell]\). If \(N\) is odd, the consecutive interval contains \(\min(2\ell+1,N)\) residues modulo \(N\). If \(N\) is even, each of the two alias-parity classes is one residue modulo \(2N\), and the same interval meets exactly \(\min(2\ell+1,2N)\) such residues. This proves the ranks and shows strictly smaller rank one degree below each stated threshold. Finally, the addition theorem gives \(\sum_{m=-\ell}^{\ell}a_{\ell,m}(c)=1\), so the full Gram trace equals \(2N\). The eigenvalues are finite sums of rational \(a_{\ell,m}(c)\).

## Verification
The accompanying standalone `check.py` computes all predicted eigenvalues with exact rational arithmetic, independently constructs the normalized complex evaluation matrix using associated Legendre functions and finite Fourier phases, and compares the numerical Gram eigenvalues. It checks \(130\) pairs \((N,\ell)\) for \(3\le N\le12\), \(0\le\ell\le12\), with largest absolute eigenvalue discrepancy below \(1.6\times10^{-14}\); it also checks \(2520\) exact derivative-amplitude nonvanishing cases for four eligible rational heights and degrees through \(34\). Sample sharp thresholds are checked at \(N=11\) and \(N=10\). See `check_output.txt`. These finite tests do not establish the all-degree assertion; Step 3 and the block decomposition do.

## Relationship to prior work
Zu Castell, Lain Fernández and Xu (arXiv:math/0407448, first public July 27, 2004) prove interpolation results for polynomial spaces of all degrees at most a cutoff on collections of several latitude circles, using rotations and factorization. Their Theorem 3.1 does not state a two-ring, *exact-degree*, complete all-degree Gram spectrum or the parity-sharp thresholds here. McEwen and Wiaux (arXiv:1110.6298, October 28, 2011) and Khalid, Kennedy and McEwen (arXiv:1403.4661, March 19, 2014) study full bandlimited spherical sampling and fast transform schemes; neither result directly implies the spectral lists for this fixed two-ring point set. The separation of variables, Fourier aliasing, and special-function identities are classical ingredients rather than claimed discoveries. The contribution claimed here is their complete interaction at every degree and every eligible height, with the exact spectra and parity-sharp recovery indices.

## Limitations
The theorem is restricted to the half-step stagger, symmetric nonzero latitudes, and reduced rational heights with even denominator. For other heights some associated Legendre amplitudes can vanish, and the rank formula need not hold. The lower positive singular value may decay along high degrees; this is an interpolation uniqueness classification, not a uniform conditioning theorem. A historical equivalent statement in spherical spectral sampling or Fourier-grid literature might exist despite the targeted comparisons; no absolute publication-priority assertion is made. Independent mathematical validation has not been performed.

## References
1. W. zu Castell, N. Lain Fernández, Y. Xu, *Polynomial Interpolation on the Unit Sphere II*, arXiv:math/0407448, first posted 2004-07-27, https://arxiv.org/abs/math/0407448.
2. J. D. McEwen and Y. Wiaux, *A novel sampling theorem on the sphere*, arXiv:1110.6298, first posted 2011-10-28, https://arxiv.org/abs/1110.6298.
3. Z. Khalid, R. A. Kennedy and J. D. McEwen, *An Optimal-Dimensionality Sampling Scheme on the Sphere with Fast Spherical Harmonic Transforms*, arXiv:1403.4661, first posted 2014-03-19, https://arxiv.org/abs/1403.4661.
