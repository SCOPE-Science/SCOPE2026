# A lattice-phase second term for second-chaos projection constants on the Boolean cube
## Finding
For every integer \(N\ge2\), let \(\mathcal B_{=2}^N\) be the real Banach space spanned by the Walsh characters \(x_i x_j\), \(1\le i<j\le N\), on the Boolean cube \(\{-1,1\}^N\), with the supremum norm. Let \(r_N\) be the largest nonnegative integer satisfying \(r_N\le\sqrt N\) and \(r_N\equiv N\pmod 2\), put \(a_N=(N-r_N)/2\), \(\delta_N=\sqrt N-r_N\), and
\[
c=\sqrt{\frac{2}{\pi e}}.
\]
Then
\[
\lambda(\mathcal B_{=2}^N)=\frac{4\binom N2}{2^N}\left[\binom{N-2}{a_N-1}-\binom{N-2}{a_N-2}\right]
=\frac{N(N-1)(r_N+1)}{N+r_N}\,2^{-(N-2)}\binom{N-2}{(N-2-r_N)/2}.
\]
Here an out-of-range binomial coefficient is zero. In addition,
\[
\lambda(\mathcal B_{=2}^N)
=cN+c\left(\frac16-(\delta_N-1)^2\right)+O(N^{-1/2}),
\]
where the error is uniform because \(0\le\delta_N<2\). Hence
\[
\limsup_{N\to\infty}\bigl(\lambda(\mathcal B_{=2}^N)-cN\bigr)=\frac c6,
\qquad
\liminf_{N\to\infty}\bigl(\lambda(\mathcal B_{=2}^N)-cN\bigr)=-\frac{5c}{6}.
\]

## Assumptions and scope
The cube carries normalized counting measure. The projection constant is the absolute projection constant of the real Banach space \(\mathcal B_{=2}^N\). A general invariant-subspace formula established in the cited projection-constant literature identifies this constant with the \(L^1\) norm of the canonical Walsh projection kernel. The new content here is the exact collapse of that norm to one boundary binomial mass and the order-one lattice-phase correction, including its sharp limsup and liminf.

## Proof
Write \(S_N(x)=x_1+\cdots+x_N\). The degree-two Walsh kernel is
\[
K_N(x)=\sum_{1\le i<j\le N}x_i x_j=\frac{S_N(x)^2-N}{2}.
\]
The invariant projection formula therefore gives
\[
\lambda(\mathcal B_{=2}^N)=\mathbb E|K_N|=\frac12\mathbb E|S_N^2-N|.
\]
If exactly \(k\) coordinates equal \(-1\), then \(S_N=N-2k\). Since \(\mathbb E K_N=0\), twice the negative mass equals the absolute mass. The negative values are exactly those with \(|N-2k|<\sqrt N\); allowing equality does not change the sum because the kernel is then zero. With \(a_N=(N-r_N)/2\), this is the central interval \(a_N\le k\le N-a_N\), and therefore
\[
\lambda(\mathcal B_{=2}^N)
=-\frac{2}{2^N}\sum_{k=a_N}^{N-a_N}K_N(k)\binom Nk.
\]
The elementary second-difference identity
\[
K_N(k)\binom Nk
=\binom N2\left[\binom{N-2}{k}-2\binom{N-2}{k-1}+\binom{N-2}{k-2}\right]
\]
turns the whole central sum into two boundary terms. Telescoping and binomial symmetry give
\[
\sum_{k=a_N}^{N-a_N}K_N(k)\binom Nk
=2\binom N2\left[\binom{N-2}{a_N-2}-\binom{N-2}{a_N-1}\right],
\]
which proves the first exact formula. Since
\[
\binom{N-2}{a_N-1}-\binom{N-2}{a_N-2}
=\binom{N-2}{a_N-1}\frac{r_N+1}{N-a_N},
\]
and \(N-a_N=(N+r_N)/2\), the second exact formula follows.

For the second term, put \(n=N-2\), \(r=r_N\), \(\delta=\delta_N\), and
\[
p_N=2^{-n}\binom n{(n-r)/2}.
\]
Uniform Stirling expansion in the regime \(r=\sqrt N-\delta\), \(0\le\delta<2\), yields
\[
\log\!\left(\frac{p_N}{cN^{-1/2}}\right)
=\frac{\delta}{\sqrt N}+\left(\frac16-\frac{\delta^2}{2}\right)\frac1N+O(N^{-3/2}),
\]
so
\[
p_N=cN^{-1/2}\left(1+\frac{\delta}{\sqrt N}+\frac1{6N}+O(N^{-3/2})\right).
\]
The rational prefactor in the exact formula has the uniform expansion
\[
\frac{N(N-1)(r+1)}{N+r}
=N^{3/2}\left(1-\frac{\delta}{\sqrt N}+\frac{2\delta-1}{N}+O(N^{-3/2})\right).
\]
Multiplication gives
\[
\lambda(\mathcal B_{=2}^N)
=cN+c\left(2\delta-\delta^2-\frac56\right)+O(N^{-1/2})
=cN+c\left(\frac16-(\delta-1)^2\right)+O(N^{-1/2}).
\]
Because \(0\le\delta_N<2\), the phase term lies between \(-5c/6\) and \(c/6\). For \(N=m^2\), \(\delta_N=0\), while for \(N=m^2+1\), \(\delta_N\to1\). These two subsequences prove the stated liminf and limsup.

## Verification
The accompanying `verify.py` checks the exact binomial formula against the direct Walsh-kernel average for every \(2\le N\le400\), checks the two exact closed forms against each other, and numerically stress-tests the scaled remainder in the lattice-phase expansion on \(100\le N\le20000\). These finite checks corroborate the algebra; they are not used as a proof of the all-\(N\) identities or the asymptotic error bound.

## Relationship to prior work
Nayar's archive-era work treats the first two Fourier levels of the Boolean cube as a natural harmonic-analytic object and records primary MSC 42C10. Defant, Galicer, Mansilla, Mastyło, and Muro later proved a general exact integral formula for projection constants of Boolean-cube Fourier support spaces and, for homogeneous degree two, obtained the leading asymptotic
\[
\lambda(\mathcal B_{=2}^N)/N\longrightarrow\sqrt{\frac{2}{\pi e}}.
\]
That general integral formula already gives the reduction \(\lambda=\frac12\mathbb E|S_N^2-N|\); no originality is claimed for that reduction or for the leading limit. The result here evaluates the finite-dimensional degree-two norm to a single boundary mass and identifies the previously unresolved order-one lattice phase, showing in particular that there is no dimension-independent constant second term. Polyanskiy's work on Hamming-sphere Fourier multipliers supplies nearby Krawtchouk analysis but studies different \(L^p\to L^2\) operator norms.

## Limitations
The result concerns the second homogeneous Walsh level only. It does not give a corresponding finite-size phase law for degree \(d\ge3\), where the kernel is a higher Krawtchouk polynomial with several sign changes. The originality comparison cannot rule out an equivalent boundary-mass or lattice-phase identity hidden in older probability or Krawtchouk literature under unrelated terminology; targeted searches did not locate one.

## References
1. P. Nayar, *FKN Theorem on the biased cube*, arXiv:1311.3179v1 (first public 2013-11-13), Colloquium Mathematicum 137 (2014), 253-261. Primary MSC 42C10.
2. A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, *Asymptotic insights for projection, Gordon-Lewis and Sidon constants in Boolean cube function spaces*, arXiv:2302.00233v2; International Mathematics Research Notices 2024, no. 15, 11239-11270.
3. Y. Polyanskiy, *Hypercontractivity of spherical averages in Hamming space*, arXiv:1309.3014v1; SIAM Journal on Discrete Mathematics 33 (2019), 731-754.
