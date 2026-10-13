# Logarithmic momentum length at the zero-density half-flux point
## Finding
Consider the tightly connected symmetric magnetic ring chain of Baradaran--Exner--Lipovský. The connecting edge has zero length, the two ring arcs have lengths \(\ell_2=\ell_3=\pi\), the preferred-orientation vertex condition has length parameter \(\ell>0\), and the magnetic flux is half-integer, \(A\in\mathbb Z+\tfrac12\). Let \(\Sigma_\ell^{(k)}\) denote the set of positive momenta belonging to non-flat Bloch bands; the isolated half-integer flat-band momenta are omitted because they have zero Lebesgue measure.

For every sufficiently large integer \(n\), there is exactly one non-flat band
\[
I_n=[n-\delta_n^-,n+\delta_n^+]
\]
in the unit cell around \(n\), and
\[
\delta_n^\pm=\frac{2}{\pi\ell n}+O(n^{-3}).
\]
Hence
\[
|I_n|=\frac{4}{\pi\ell n}+O(n^{-3}).
\]
If
\[
M_\ell(K)=\bigl|\Sigma_\ell^{(k)}\cap[0,K]\bigr|
\]
denotes Lebesgue measure in momentum, then
\[
M_\ell(K)=\frac{4}{\pi\ell}\log K+O(1)\qquad(K\to\infty).
\]
Thus the limiting momentum-band density is zero, as stated in the source, but the total occupied momentum length still diverges logarithmically.

Under the monotone change of variable \(E=k^2\), let \(\Sigma_\ell^{(E)}=\{k^2:k\in\Sigma_\ell^{(k)}}\). The energy width of the band corresponding to \(I_n\) is
\[
(n+\delta_n^+)^2-(n-\delta_n^-)^2
=\frac{8}{\pi\ell}+O(n^{-2}).
\]
Therefore the cumulative energy-band measure
\[
S_\ell(E)=\bigl|\Sigma_\ell^{(E)}\cap[0,E]\bigr|
\]
satisfies
\[
S_\ell(E)=\frac{8}{\pi\ell}\sqrt E+O(1)\qquad(E\to\infty).
\]

## Assumptions and scope
The result is for the symmetric tight chain only: \(\ell_1=0\), \(\ell_2=\ell_3=\pi\), fixed preferred-orientation coupling scale \(\ell>0\), and \(A\in\mathbb Z+\tfrac12\). It concerns the non-flat Bloch bands at positive energy. The source also has flat bands at half-integer momenta; those isolated points do not affect either Lebesgue-measure asymptotic.

The big-O constants may depend on \(\ell\), which is fixed while \(n\), \(K\), and \(E\) tend to infinity.

## Proof
For the symmetric tight chain, equation (33) of the primary source is
\[
\Bigl(2(k^2\ell^2+1)\sin(\pi k)\cos(\pi A)+4k\ell\sin(\pi A)\cos(\pi k)\Bigr)\cos\theta
=2k\ell\sin(2\pi A)+(k^2\ell^2+1)\sin(2\pi k).
\]
At half-integer flux, \(\cos(\pi A)=0\), \(|\sin(\pi A)|=1\), and \(\sin(2\pi A)=0\). Away from the half-integer flat-band points, \(\cos(\pi k)\ne0\), so division by \(2\cos(\pi k)\) gives
\[
\cos\theta=\pm\frac{k^2\ell^2+1}{2k\ell}\sin(\pi k).
\]
A real Floquet quasimomentum exists exactly when
\[
|\sin(\pi k)|\le r_\ell(k),
\qquad
r_\ell(k)=\frac{2k\ell}{k^2\ell^2+1}.
\]
This is an exact condition, not the leading-order approximation (34).

For fixed \(\ell>0\), \(r_\ell(k)=2/(\ell k)+O(k^{-3})\). Hence for large \(n\), the inequality in the cell centered at \(n\) can hold only within distance \(O(n^{-1})\) of \(n\). On the right and left, respectively, the two boundary distances are the unique small positive solutions of
\[
\sin(\pi\delta_n^+)=r_\ell(n+\delta_n^+),
\qquad
\sin(\pi\delta_n^-)=r_\ell(n-\delta_n^-).
\]
Uniqueness follows because, on a fixed sufficiently small neighborhood of zero, \(\pi\cos(\pi\delta)\) is bounded away from zero while \(r_\ell'(n\pm\delta)=O(n^{-2})\). Existence follows from the opposite signs at \(\delta=0\) and at any fixed small positive \(\delta\) once \(n\) is large.

The boundary equations first give \(\delta_n^\pm=O(n^{-1})\). Using
\[
\arcsin x=x+O(x^3)
\]
and
\[
r_\ell(n\pm\delta_n^\pm)
=\frac{2}{\ell n}+O(n^{-3}),
\]
we obtain
\[
\delta_n^\pm=\frac{2}{\pi\ell n}+O(n^{-3}).
\]
Adding the two boundary distances gives the momentum width. Summing over full bands up to \(K\), the harmonic sum gives
\[
\sum_{n\le K}\frac{4}{\pi\ell n}
=\frac{4}{\pi\ell}\log K+O(1),
\]
while the sum of the \(O(n^{-3})\) errors converges. A possibly partial terminal band contributes a bounded amount, proving the momentum formula.

For energy, one full band contributes
\[
(n+\delta_n^+)^2-(n-\delta_n^-)^2
=2n(\delta_n^++\delta_n^-)+(\delta_n^+)^2-(\delta_n^-)^2
=\frac{8}{\pi\ell}+O(n^{-2}).
\]
The error is summable. There are \(\sqrt E+O(1)\) full bands below energy \(E\), and a terminal partial band contributes \(O(1)\). This proves the energy-measure law.

## Verification
The accompanying `verify.py` solves the exact boundary equations by bisection for three distinct coupling scales and several large band indices. It checks the exact boundary residuals, the convergence of \(n|I_n|\) to \(4/(\pi\ell)\), and the convergence of the energy width to \(8/(\pi\ell)\). Running `python verify.py` prints `VERIFY_OK`.

These numerical checks are corroborative only. The infinite asymptotic statements follow from the exact dispersion reduction and the analytic estimates above.

## Relationship to prior work
Baradaran--Exner--Lipovský derive the exact symmetric-chain dispersion relation and show that at half-integer flux the momentum-band probability is zero while bands may still appear near integer momenta. They do not state the widths of those surviving bands, their cumulative momentum length, or the resulting energy-measure growth. The present result resolves that critical zero-density scale directly from their exact equation (33).

Band--Berkolaiko study the limiting relative density of momentum bands for periodic quantum graphs and establish generic universality properties. A limiting density equal to zero does not determine a sublinear cumulative measure, so their theorem does not imply the logarithmic law or the \(\sqrt E\) energy law here.

## Limitations
No claim is made for nonsymmetric ring lengths, non-half-integer flux, the negative spectrum, or the isolated flat-band multiplicities. The asymptotics concern Lebesgue measure of the non-flat band set, not a density-of-states measure weighted by Bloch multiplicity. The originality search did not locate an equivalent subleading zero-density law, but an older calculation under different magnetic-chain terminology remains a residual literature risk.

## References
1. M. Baradaran, P. Exner, J. Lipovský, *Magnetic ring chains with vertex coupling of a preferred orientation*, arXiv:2201.01502v1 (5 January 2022), later J. Phys. A: Math. Theor. 55 (2022) 375203, DOI:10.1088/1751-8121/ac820b. Relevant material: symmetric tight chain, equation (33), and the half-integer-flux discussion around equation (37).
2. R. Band, G. Berkolaiko, *Universality of the momentum band density of periodic networks*, arXiv:1304.6028v1; Phys. Rev. Lett. 111 (2013) 130404, DOI:10.1103/PhysRevLett.111.130404.
