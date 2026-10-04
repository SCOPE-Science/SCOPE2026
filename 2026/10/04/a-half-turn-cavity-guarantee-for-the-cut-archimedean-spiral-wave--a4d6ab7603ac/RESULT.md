# A half-turn cavity guarantee for the cut Archimedean spiral waveguide
## Finding
Let \(a>0\) and \(\beta\ge\pi\). For the Dirichlet Laplacian \(H_{a,\beta}\) in the complement of the cut Archimedean spiral
\[
\Gamma_{a,\beta}=\{(a\theta\cos\theta,a\theta\sin\theta):\theta\ge\beta}\},
\]
the discrete spectrum is nonempty:
\[
\sigma_{\mathrm{disc}}(H_{a,\beta})\ne\varnothing.
\]
This strengthens the published disk-bracketing guarantee \(\beta>2j_{0,1}\approx4.805\) to the clean half-turn condition \(\beta\ge\pi\).

## Assumptions and scope
The operator and cut-spiral convention are those of Exner and Tater. Their essential-spectrum threshold is \((2a)^{-2}\). The statement is only a sufficient condition for existence of at least one eigenvalue below that threshold. It does not identify the true critical angle, which the source's finite-element study places numerically near \(1.43\), and it does not claim that \(\pi\) is optimal among all possible comparison domains or even all disks.

## Proof
By the scaling used in the source, it is enough to take \(a=1/2\), where the essential threshold equals \(1\). Write
\[
\gamma(\theta)=\left(\frac\theta2\cos\theta,\frac\theta2\sin\theta\right),\qquad \theta\ge\pi,
\]
and choose
\[
c=\left(\frac{73}{100},\frac{73}{100}\right),\qquad R=\frac{481}{200}=2.405.
\]
For \(\pi\le\theta\le7\), the squared distance is
\[
F(\theta)=\frac{\theta^2}4-\frac{73}{100}\theta(\cos\theta+\sin\theta)+2\left(\frac{73}{100}\right)^2.
\]
The accompanying interval checker covers the larger interval \([3.1415,7]\) by one thousand boxes and, with outward interval arithmetic, proves on every box
\[
F(\theta)>R^2.
\]
Its smallest certified lower endpoint is greater than \(5.814\), whereas \(R^2=5.784025\). For \(\theta\ge7\), the reverse triangle inequality gives
\[
|\gamma(\theta)-c|\ge \frac\theta2-|c|.
\]
Since \(|c|<1.033\), the right side exceeds \(2.467>R\). Hence the open disk \(B(c,R)\) is disjoint from \(\Gamma_{1/2,\pi}\) and lies in its complement.

It remains to put the disk eigenvalue below the threshold. With \(j_{0,1}\) denoting the first positive zero of \(J_0\), the first Dirichlet eigenvalue of a radius-\(R\) disk is \(j_{0,1}^2/R^2\). The checker proves \(J_0(R)<0\) by an exact rational alternating-series bound: the partial sum through order six is already negative and the remaining tail starts negative with decreasing magnitude. Since \(J_0(0)=1\), this implies \(j_{0,1}<R\), and therefore \(j_{0,1}^2/R^2<1\). Dirichlet bracketing gives an eigenvalue of \(H_{1/2,\pi}\) below its essential threshold. If \(\beta>\pi\), the cut spiral \(\Gamma_{1/2,\beta}\) is a subset of \(\Gamma_{1/2,\pi}\), so the same disk remains admissible. Scaling by \(2a\) proves the statement for every \(a>0\).

## Verification
Run `python3 artifacts/verify.py`. It checks the exact Bessel-series sign, rigorously encloses the distance inequality on \([3.1415,7]\), and checks the analytic radial tail. The interval computation certifies a continuum inequality; it is not being used as a finite sample of the spiral.

## Relationship to prior work
Exner and Tater prove \(\sigma_{\mathrm{ess}}(H_{a,\beta})=[(2a)^{-2},\infty)\) and obtain nonempty discrete spectrum from a centered comparison disk when \(\beta>2j_{0,1}\). Immediately afterward they note that shifting the disk center can improve the bracketing bound, but they do not carry out that optimization or give a smaller explicit analytic angle. Their numerical study suggests a much lower true onset, near \(1.43\), so the present result should be read as a rigorous analytic improvement rather than a determination of the spectral threshold. The later Barseghyan--Exner paper studies strictly shrinking spirals and Lieb--Thirring estimates; its inspected text contains no cavity or cut-spiral result.

## Limitations
The constant \(\pi\) is not asserted to be sharp. The proof supplies one explicit shifted disk and one bound state only. It does not prove simplicity, count additional eigenvalues, or convert the source's numerical critical angle into a theorem. The originality search cannot exclude an unindexed geometric observation or informal note giving the same explicit disk.

## References
Exner, P.; Tater, M., *Spectral properties of spiral-shaped quantum waveguides*, arXiv:2009.02730v1 (2020), later J. Phys. A 53 (2020), 505303, DOI 10.1088/1751-8121/abc5d3.

Barseghyan, D.; Exner, P., *Spectral estimates for the Dirichlet Laplacian on spiral-shaped regions*, J. Spectr. Theory 13 (2023), 243--261, DOI 10.4171/JST/454.
