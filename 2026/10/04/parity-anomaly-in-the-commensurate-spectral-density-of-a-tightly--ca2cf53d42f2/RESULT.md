# Parity anomaly in the commensurate spectral density of a tightly connected ring chain
## Finding
Consider the tightly connected ring chain obtained by collapsing the connecting edge in the periodic preferred-orientation model of Baradaran, Exner, and Tater. Write the two positive ring-arc lengths as \(L_2,L_3>0\) with \(L_2+L_3=2\pi\), and let \(a>0\) denote the length scale in the vertex coupling. Define
\[
P:=\lim_{K\to\infty}\frac{|\sigma(H)\cap[0,K]|}{K},
\]
whenever the limit exists. If
\[
\frac{L_2}{L_3}=\frac{p}{q},\qquad \gcd(p,q)=1,
\]
then
\[
P=\begin{cases}
\frac12,&\text{if at least one of }p,q\text{ is even},\\[2mm]
\frac12+\frac{1}{2pq},&\text{if }p\text{ and }q\text{ are both odd}.
\end{cases}
\]
The symmetric case \(p=q=1\) gives \(P=1\). For asymmetric commensurate arcs with both reduced integers odd, the density is therefore strictly larger than \(1/2\). The simplest example is
\[
\frac{L_2}{L_3}=\frac13,\qquad P=\frac23.
\]
This contradicts the published assertion that every asymmetric tightly connected chain has density \(1/2\).

## Assumptions and scope
The Hamiltonian and coupling are exactly those of the degree-four \(L_1=0\) limit in arXiv:2012.14344v1. The operator acts as the free one-dimensional Laplacian on each edge and uses the cyclic time-reversal-noninvariant vertex condition from that paper. The scale normalization is \(L_2+L_3=2\pi\). Only the positive spectrum enters \(P\); isolated flat-band energies are countable and hence do not affect Lebesgue density.

The claim is for rational \(L_2/L_3\). For irrational ratios, the usual torus equidistribution argument gives \(P=1/2\), consistent with the generic-edge regime. No statement is made about finite-energy convergence rates beyond what is needed to pass from the exact band condition to the density.

## Proof
The exact continuous-band criterion in Sec. 3.1 of arXiv:2012.14344v1 is
\[
F(k):=4a^2k^2-(a^2k^2+1)^2\cos(2\pi k)+(a^2k^2-1)^2\cos\bigl(2k(\pi-L_3)\bigr)\ge0.
\]
After division by \(a^4k^4\),
\[
\frac{F(k)}{a^4k^4}=G(k)+R(k),
\]
where
\[
G(k):=\cos\bigl(2k(\pi-L_3)\bigr)-\cos(2\pi k)
      =2\sin(kL_2)\sin(kL_3)
\]
and, uniformly for \(k\ge1\),
\[
|R(k)|\le \frac{8}{a^2k^2}+\frac{2}{a^4k^4}.
\]
Hence the exact band indicator can differ from \(\mathbf 1_{\{G\ge0\}}\) only where \(|G(k)|=O(k^{-2})\).

For rational \(L_2/L_3=p/q\) in lowest terms,
\[
L_2=\frac{2\pi p}{p+q},\qquad L_3=\frac{2\pi q}{p+q}.
\]
With \(t=2\pi k/(p+q)\), the leading sign is that of
\[
\sin(pt)\sin(qt).
\]
This is periodic. Its zeros have order at most two. On the \(n\)-th momentum period, the set on which \(|G(k)|\le Ck^{-2}\) therefore has length \(O(n^{-1})\): neighborhoods of simple zeros are smaller, while a double zero needs only an \(O(n^{-1})\) neighborhood. Multiplication by the energy Jacobian \(2k\) gives an \(O(1)\) discrepancy per period. Summing through momentum \(R\) yields an \(O(R)\) discrepancy in energy measure, which is \(o(R^2)\). Thus the exact density equals the period average of \(\mathbf 1_{\{\sin(pt)\sin(qt)\ge0\}}\).

It remains to compute that period average. Put
\[
s_m(t):=\operatorname{sgn}(\sin(mt)).
\]
Up to a null set,
\[
\mathbf 1_{\{\sin(pt)\sin(qt)\ge0\}}=\frac{1+s_p(t)s_q(t)}2.
\]
The square-wave Fourier series is valid in \(L^2(0,2\pi)\):
\[
s_m(t)=\frac4\pi\sum_{r\ge1\atop r\ {\rm odd}}\frac{\sin(rmt)}r.
\]
Therefore the normalized correlation
\[
C_{p,q}:=\frac1{2\pi}\int_0^{2\pi}s_p(t)s_q(t)\,dt
\]
receives contributions only from common odd harmonics. Since \(p\) and \(q\) are coprime, the equation \(rp=sq\) with odd \(r,s\) has no solution if one of \(p,q\) is even, and hence \(C_{p,q}=0\). If both are odd, all common odd harmonics are \(r=qh\), \(s=ph\) with odd \(h\), so
\[
C_{p,q}=\frac8{\pi^2pq}\sum_{h\ge1\atop h\ {\rm odd}}\frac1{h^2}
=\frac1{pq}.
\]
Consequently
\[
P=\frac{1+C_{p,q}}2,
\]
which is exactly the stated parity formula.

Finally, for any bounded periodic indicator \(b(k)\),
\[
\frac2{R^2}\int_0^R k b(k)\,dk
\]
converges to the ordinary period average of \(b\). Thus the same fraction governs the paper's energy-density definition with \(K=R^2\), not merely the unweighted momentum fraction.

## Verification
The accompanying `verify_density.py` performs two independent finite checks. First, it partitions one period at all exact rational zeros of \(\sin(pt)\) and \(\sin(qt)\) and computes the positive-sign measure using `Fraction`; for every coprime \(1\le p,q\le25\) it exactly reproduces the parity formula. Second, it samples the exact published band inequality for representative ratios and verifies numerical convergence of the energy-weighted density toward \(2/3\) for \((p,q)=(1,3)\), toward \(8/15\) for \((3,5)\), and toward \(1/2\) for even-odd examples. The computation is a check, not the infinite proof.

## Relationship to prior work
Baradaran, Exner, and Tater derive the exact criterion above and then reduce it at high energy to \(\sin(kL_2)\sin(kL_3)\ge0\). They correctly note that the band pattern is periodic when \(L_2/L_3\) is rational, but their equation (3.34) asserts \(P=1/2\) for every asymmetric chain and justifies this by treating the signs of the two sine factors as uncorrelated. For rationally related arcs that independence step fails. The later interpolation paper arXiv:2403.09457v1 repeats the same conclusion and explicitly says it remains true for unequal rationally related arcs; it does not derive the parity correction above.

Band and Berkolaiko's universality theorem concerns generic edge lengths. Its genericity hypothesis does not cover this commensurate rational locus, so it neither implies nor contradicts the arithmetic formula here.

Targeted searches for the exact paper title together with “erratum”, “correction”, “commensurate”, “band density”, and the sign product, as well as searches of published mathematical records for rational commensurate ring-chain band density and equivalent parity formulas, did not locate a published correction containing this result.

## Limitations
The theorem uses the exact \(L_1=0\) degree-four model, not a small positive connecting length. It computes the asymptotic spectral-energy density, not detailed finite-energy band widths. The proof does not quantify the optimal remainder in the finite-cutoff density. The originality search cannot rule out an equivalent observation hidden under unrelated terminology; no such source was found in the inspected primary literature or targeted database searches.

## References
1. M. Baradaran, P. Exner, M. Tater, “Spectrum of periodic chain graphs with time-reversal non-invariant vertex coupling,” arXiv:2012.14344v1; Annals of Physics 443 (2022), 168992, doi:10.1016/j.aop.2022.168992.
2. P. Exner, J. Pekař, “Vertex coupling interpolation in quantum chain graphs,” arXiv:2403.09457v1; Journal of Mathematical Physics 65 (2024), 092102, doi:10.1063/5.0208361.
3. R. Band, G. Berkolaiko, “Universality of the Momentum Band Density of Periodic Networks,” Physical Review Letters 111 (2013), 130404, doi:10.1103/PhysRevLett.111.130404.
