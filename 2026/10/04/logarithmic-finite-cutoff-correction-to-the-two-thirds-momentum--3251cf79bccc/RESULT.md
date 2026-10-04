# Logarithmic finite-cutoff correction to the two-thirds momentum density of the preferred-orientation triangular quantum graph
## Finding
For the triangular periodic quantum graph with edge length parameter \(d>0\) and preferred-orientation degree-six vertex coupling of length scale \(\ell>0\), define the momentum spectrum
\[
S=\{k>0:k^2\in\sigma(H)\},
\]
and the finite-cutoff spectral momentum measure
\[
M(K)=|S\cap[0,K]|.
\]
Then
\[
M(K)=\frac{2}{3}K-\frac{4}{\sqrt{3}\,\pi\,\ell}\log(K\ell)+O(1)
\qquad (K\to\infty).
\]
In particular, the known limiting momentum density \(2/3\) has a negative logarithmic finite-cutoff correction with a coefficient independent of the lattice edge length \(d\).

## Assumptions and scope
The graph and coupling are exactly those of the triangular-lattice degeneration in Section 4 of Baradaran--Exner, arXiv:2106.16019v1. The parameters \(d\) and \(\ell\) are fixed positive numbers while \(K\to\infty\). The statement concerns Lebesgue measure in momentum \(k\), not energy \(k^2\). Infinitely degenerate flat-band momenta are retained in \(S\) but contribute zero Lebesgue measure. The isolated singular momentum \(k=\ell^{-1}\), any low-energy exceptional behavior, and finitely many early phase periods are absorbed into the \(O(1)\) remainder.

## Proof
The source proves that away from its explicitly separated flat-band points the continuous spectrum is characterized by
\[
-\frac32\le G(k)\le3,
\]
where, with \(u=k\ell\) and \(c=\cos(kd)\),
\[
G(k)=\frac{2u^2\sec^2(kd/2)+(3u^4+10u^2+3)c}{(u^2-1)^2}.
\]
Using \(\sec^2(kd/2)=2/(1+c)\), the two boundary equations factor exactly. For \(G(k)=3\),
\[
((u^2+3)c-u^2+3)((3u^2+1)c+3u^2-1)=0.
\]
For \(G(k)=-3/2\),
\[
(2c+1)(3cu^4+10cu^2+3c+3u^4+2u^2+3)=0.
\]
Thus the broad-band outer edges satisfy exactly \(c=-1/2\), while the upper boundary near an even Brillouin-zone center satisfies
\[
\cos(kd)=\frac{u^2-3}{u^2+3},
\qquad
\left|\tan\frac{kd}{2}\right|=\frac{\sqrt3}{u}.
\]
Let \(K_n=2n\pi/d\). The two continuous-spectrum edges adjacent to \(K_n\) are at \(K_n-\delta_n^-\) and \(K_n+\delta_n^+\), where the preceding exact equation and Taylor expansion give
\[
\delta_n^\pm=\frac{\sqrt3}{\pi\ell n}+O(n^{-3}).
\]
The flat point at \(K_n\) itself has zero measure, so this produces the shrinking central hole relevant to the integrated measure.

Near the odd center \(J_n=(2n+1)\pi/d\), the second factor of the \(G=3\) equation gives the inner narrow-band edges, while the second factor of the \(G=-3/2\) equation gives the outer edges. Writing the positive distance from \(J_n\) as \(s\), their half-angle equations are, respectively,
\[
\tan\frac{ds}{2}=\frac{1}{\sqrt3\,u},
\qquad
\tan\frac{ds}{2}=\frac{2u}{\sqrt3\,(u^2+1)},
\]
with \(u=k\ell\) evaluated at the corresponding edge. Consequently the two narrow bands around \(J_n\) have combined momentum width
\[
\frac{4}{\sqrt3\,\pi\,\ell(2n+1)}+O(n^{-3})
=\frac{2}{\sqrt3\,\pi\,\ell n}+O(n^{-2}).
\]

Consider the full phase period \(P_n=[2n\pi/d,2(n+1)\pi/d]\). The broad portions would contribute \(4\pi/(3d)\) at leading order. The two half-holes at its even endpoints remove
\[
\frac{\sqrt3}{\pi\ell}\left(\frac1n+\frac1{n+1}\right)+O(n^{-3}),
\]
while the odd-center pair adds the narrow-band width above. Therefore
\[
|S\cap P_n|=\frac{4\pi}{3d}-\frac{4}{\sqrt3\,\pi\,\ell}\frac1n+O(n^{-2}).
\]
Summing full periods uses \(\sum_{n\le N}n^{-1}=\log N+O(1)\) and \(N=Kd/(2\pi)+O(1)\), hence
\[
M(K)=\frac23K-\frac{4}{\sqrt3\,\pi\,\ell}\log(K\ell)+O(1).
\]
An incomplete final phase period changes the expression by only a bounded amount.

## Verification
The standalone file `verify.py` evaluates the exact source quotient, verifies both displayed algebraic factorizations numerically at independent points, resolves all four continuous-band pieces in complete high-energy periods by bisection, and checks that
\[
n\left(\frac{4\pi}{3d}-|S\cap P_n|\right)
\to\frac{4}{\sqrt3\,\pi\,\ell}
\]
for several choices of \(d\) and \(\ell\). It also checks boundedness of a cumulative harmonic-corrected residual. Running the packaged script returns `VERIFY_OK`. These finite calculations are replay checks only; the all-
\(K\) asymptotic is proved by the exact factorizations and the analytic expansions above.

## Relationship to prior work
Baradaran--Exner derive the exact quotient \(G(k)\), identify both the narrow-band family near odd multiples of \(\pi/d\) and the wide-band family near even multiples, and prove the limiting momentum density \(2/3\). Their displayed analysis gives the leading narrow-band offsets but does not state a finite-cutoff cumulative asymptotic or a logarithmic correction. The present calculation keeps both families at the first order that survives harmonic summation and uses the exact boundary factorization to determine the missing shrinking central-hole contribution.

Band--Berkolaiko study the limiting momentum-band density for periodic Kirchhoff networks. Their result is a limiting-density statement and does not provide this model-specific second term. Berkolaiko--Kha study degeneracies of band edges in a different periodic-graph setting; that work does not imply the cumulative coefficient above.

## Limitations
The result is specific to the triangular degeneration with the preferred-orientation degree-six coupling and to momentum measure. It does not claim an analogous logarithmic term for the nondegenerate Kagome lattice, for other vertex couplings, or for energy-measure density. The bounded \(O(1)\) term is not evaluated, and the result does not classify all low-energy band crossings.

## References
1. M. Baradaran and P. Exner, *Kagome network with vertex coupling of a preferred orientation*, arXiv:2106.16019v1; Journal of Mathematical Physics 63, 083502 (2022), DOI:10.1063/5.0093546.
2. R. Band and G. Berkolaiko, *Universality of the Momentum Band Density of Periodic Networks*, Physical Review Letters 111, 130404 (2013), DOI:10.1103/PhysRevLett.111.130404.
3. G. Berkolaiko and M. Kha, *Degenerate band edges in periodic quantum graphs*, Letters in Mathematical Physics 110, 2965--2982 (2020), arXiv:2001.03566.
