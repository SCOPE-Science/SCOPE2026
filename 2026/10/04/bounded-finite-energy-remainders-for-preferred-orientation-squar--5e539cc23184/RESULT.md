# Bounded finite-energy remainders for preferred-orientation square and hexagonal quantum lattices

## Finding
For the equilateral square and hexagonal periodic quantum graphs with the cyclic preferred-orientation coupling studied by Exner and Tater, use their normalization in which the coupling length scale is one and let the common edge length be \(\ell>0\). Define the positive-energy spectral measures
\[
M_{{\square}}(K)=|\sigma(H_{{\square}})\cap[0,K]|,
\qquad
M_{{\hexagon}}(K)=|\sigma(H_{{\hexagon}})\cap[0,K]|,
\]
where \(|\cdot|\) denotes Lebesgue measure in the energy variable. Then
\[
M_{{\square}}(K)=K-\frac{{8}}{{\pi}}\sqrt K+O(1),
\qquad
M_{{\hexagon}}(K)=\frac{{8(\sqrt3-1)}}{{\pi}}\sqrt K+O(1)
\]
as \(K\to\infty\). Thus
\[
1-\frac{{M_{{\square}}(K)}}{{K}}=\frac{{8}}{{\pi\sqrt K}}+O(K^{{-1}}),
\qquad
\frac{{M_{{\hexagon}}(K)}}{{K}}=\frac{{8(\sqrt3-1)}}{{\pi\sqrt K}}+O(K^{{-1}}).
\]
The coefficients are independent of \(\ell\). Countable flat bands do not affect these Lebesgue measures.

More precisely, if \(E_m=(m\pi/\ell)^2\), the square gap centered at \(E_m\) has energy width
\[
G_m=\frac8{\ell}-\frac{{8\ell}}{{3\pi^2m^2}}+O(m^{{-4}}),
\]
and the sum of the widths of the two hexagonal absolutely continuous bands surrounding \(E_m\) is
\[
B_m=\frac{{8(\sqrt3-1)}}{{\ell}}+
\frac{{8\ell(4-3\sqrt3)}}{{3\pi^2m^2}}+O(m^{{-4}}).
\]
The absence of an \(m^{{-1}}\) term sharpens the published \(O(m^{{-1}})\) width bounds and is exactly what turns the naively possible logarithmic cumulative error into a bounded one.

## Assumptions and scope
The statement concerns the exact square and hexagonal lattices and the cyclic vertex condition of arXiv:1710.02664v1, with all lattice edges of the same length \(\ell\). It is a statement about Lebesgue measure in the energy variable, not about the momentum-band density of Band--Berkolaiko, density of states, eigenvalue counting on finite graphs, or random-matrix spectral statistics. The negative spectrum contributes nothing to \([0,K]\), and the infinitely degenerate flat bands are countable and therefore have zero Lebesgue measure.

The \(O(1)\) remainders need not converge: moving the cutoff \(K\) through the last partially included gap or band pair can produce bounded cutoff-phase oscillations. No claim is made about an explicit limiting constant.

## Proof
Write \(t_m=m\pi\) and parameterize momenta near the \(m\)-th Neumann center by
\[
k=\frac{{t_m+y}}{{\ell}},
\qquad y=O(t_m^{{-1}}).
\]

For the square lattice, Exner--Tater's dispersion condition implies that a high-energy gap boundary satisfies
\[
\cos y=1-\frac{{2\ell^2}}{{(t_m+y)^2+\ell^2}}.
\]
Taylor expansion at \(t_m^{-1}=0\), separately for the positive and negative roots, gives
\[
y_+=\frac{{2\ell}}{{t_m}}-\frac{{2\ell^2(\ell+6)}}{{3t_m^3}}+O(t_m^{{-5}}),
\qquad
y_-=-\frac{{2\ell}}{{t_m}}+\frac{{2\ell^2(\ell-6)}}{{3t_m^3}}+O(t_m^{{-5}}).
\]
Since energy is \(E=(t_m+y)^2/\ell^2\), subtraction of the two edge energies yields
\[
G_m=\frac8{\ell}-\frac{{8\ell}}{{3t_m^2}}+O(t_m^{{-4}}),
\]
which is the displayed square expansion.

For the hexagonal lattice, the exact dispersion relation is
\[
\cos(2k\ell)=
\frac{{k^4-6k^2-3-4d(k^2-1)}}{{(k^2+3)^2}},
\qquad d\in[-1,3].
\]
The four high-energy band edges around \(t_m\) occur at \(d=-1\) and \(d=3\), on the two sides of \(y=0\). For a fixed boundary value \(d\), expanding the corresponding root gives a leading displacement
\[
y=\pm\frac{{\ell\sqrt{{2(d+3)}}}}{{t_m}}+O(t_m^{{-3}}).
\]
Carrying the Taylor expansion through order \(t_m^{-3}\), inserting the four roots into \(E=(t_m+y)^2/\ell^2\), and adding the left and right band widths gives
\[
B_m=\frac{{8(\sqrt3-1)}}{{\ell}}+
\frac{{8\ell(4-3\sqrt3)}}{{3t_m^2}}+O(t_m^{{-4}}).
\]
In particular, the \(t_m^{-1}\) term is absent.

Now let \(N(K)=\lfloor \ell\sqrt K/\pi\rfloor\). Apart from finitely many low-energy components and at most one partially cut high-energy cell, the square complement in \([0,K]\) is the union of one gap for each \(m\le N(K)\), while the hexagonal spectrum is the union of two bands for each such \(m\), together with measure-zero flat bands. Because \(\sum_{{m\ge1}}m^{{-2}}<\infty\), summing the refined widths gives
\[
\sum_{{m\le N(K)}}G_m=\frac8{\ell}N(K)+O(1)
=\frac8\pi\sqrt K+O(1),
\]
and
\[
\sum_{{m\le N(K)}}B_m=\frac{{8(\sqrt3-1)}}{{\ell}}N(K)+O(1)
=\frac{{8(\sqrt3-1)}}{{\pi}}\sqrt K+O(1).
\]
The omitted initial pieces and the last partial cell are uniformly bounded in energy measure. This proves both cumulative formulas.

## Verification
The included `verify.py` solves the exact square and hexagonal band-edge equations by bisection for several edge lengths and large mode numbers. It checks the two displayed second-order width formulas and their \(m^{{-4}}\)-scale residuals. The finite computations support the algebraic expansion but are not used as a proof of the asymptotic statement.

## Relationship to prior work
Exner--Tater (2017/2018) derive the exact square and hexagonal dispersion relations and state only the coarser high-energy width estimates: square gaps have energy width \(8/\ell+O(m^{{-1}})\), while each of the two hexagonal bands has width \(4(\sqrt3-1)/\ell+O(m^{{-1}})\). Those statements do not imply the vanishing first-order correction, the explicit \(m^{{-2}}\) coefficients above, or the bounded cumulative remainders; direct summation of the published error bounds permits an \(O(\log K)\) remainder.

Exner--Tater (2021) explicitly use the energy-spectrum probability \(\lim_{{K\to\infty}}K^{{-1}}|\sigma(H)\cap[0,K]|\) as a transport statistic and record limiting values zero or one in related preferred-orientation square-lattice models, but do not give these finite-cutoff coefficients or bounded remainders. Band--Berkolaiko (2013) study relative density in the momentum spectrum, which is a different statistic. A 2026 paper on spectral statistics of preferred-orientation quantum graphs studies finite-graph spacing and form-factor statistics rather than the periodic-lattice energy-measure asymptotics proved here.

## Limitations
The calculation is specific to the equilateral square and hexagonal lattices and the coupling normalization of the cited source. It does not establish analogous coefficients for magnetic lattices, incommensurate edges, other vertex degrees, or interpolating couplings. The proof gives only a bounded cumulative remainder, not a convergent second term, because the terminal cutoff can slice a gap or band pair at an arbitrary phase.

## References
1. P. Exner and M. Tater, "Quantum graphs with vertices of a preferred orientation," arXiv:1710.02664v1 (2017); Phys. Lett. A 382 (2018), 283--287; DOI:10.1016/j.physleta.2017.11.028.
2. P. Exner and M. Tater, "Quantum graphs: self-adjoint, and yet exhibiting a nontrivial PT-symmetry," arXiv:2108.04708v1 (2021); Phys. Lett. A 416 (2021), 127669.
3. R. Band and G. Berkolaiko, "Universality of the Momentum Band Density of Periodic Networks," arXiv:1304.6028 (2013); Phys. Rev. Lett. 111, 130404.
4. R. Band, P. Exner, D. Goel, and A. Strauss, "Spectral statistics of preferred orientation quantum graphs," J. Math. Phys. 67, 013502 (2026); DOI:10.1063/5.0295424.
