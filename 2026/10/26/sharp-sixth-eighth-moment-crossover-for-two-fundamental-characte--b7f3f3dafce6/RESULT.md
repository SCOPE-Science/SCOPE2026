# Sharp sixth–eighth moment crossover for two fundamental characters of \(\mathrm{USp}(4)\)

## Finding

Let \(G=\mathrm{USp}(4)\) carry probability Haar measure. Let \(U\) be its four-dimensional defining representation, and let \(W\) be the five-dimensional irreducible complement of the invariant line in \(\bigwedge^2 U\). Write \(u=\chi_U\), \(v=\chi_W\) for the *ordinary trace* characters, not dimension-normalized characters. Then \(u,v\) are real-valued and orthonormal in \(L^2(G)\).

For arbitrary complex \(a,b\), define \(F=a u+b v\). Its sharp normalized sixth and eighth moments are

\[
\int_G |F|^6\,dg\ \le\ K_6(|a|^2+|b|^2)^3,
\qquad
\int_G |F|^8\,dg\ \le\ K_8(|a|^2+|b|^2)^4,
\]
where \(K_6=H_6(p_6)\), \(K_8=H_8(p_8)\),

\[
H_6(p)=14p^3+165p^2(1-p)+150p(1-p)^2+15(1-p)^3,
\]
\[
H_8(p)=84p^4+2100p^3(1-p)+5110p^2(1-p)^2
 +2100p(1-p)^3+105(1-p)^4,
\]
\[
p_6=\frac{\sqrt{365}-15}{8}=0.513121646817850\ldots,
\]
and \(p_8=0.497688591799567\ldots\) is the unique root in \((0,1)\) of
\[
157p^3-240p^2-40p+60=0.
\]
Numerically, \(K_6=43.019700544257629\ldots\), \(K_8=593.699634602355109\ldots\).

For exponent \(2m\in\{6,8\}\), **every nonzero equality pair** is, and only is,
\[
(a,b)=\lambda\big(\sqrt{p_{2m}},\,\pm\sqrt{1-p_{2m}}\big),
\qquad \lambda\in\mathbb C\setminus\{0\},
\]
where \(p_{6}=p_6\) and \(p_{8}=p_8\) (the subscript here records the moment order). In particular, the coefficient dominance changes *strictly* between the sixth and eighth moments:
\[
\boxed{p_6>\tfrac12>p_8.}
\]
The sixth-power maximizer favors the four-dimensional fundamental character, while the eighth-power maximizer favors the five-dimensional fundamental character. For comparison, the fourth-order real-aligned moment is \(3+6p(1-p)\), uniquely maximized at the balanced weight \(p=1/2\). Thus the sixth/eighth reversal is a genuine change in optimal mixing with moment order, not a choice of coefficient normalization. This is a sharp inequality and equality-classification result for this fixed two-dimensional central Fourier packet.

## Assumptions and scope

The group is the compact real form \(\mathrm{USp}(4)\), not \(\mathrm{Sp}(4,\mathbb R)\). All integrals are with total Haar mass one. Coefficients are arbitrary complex numbers. The characters are as above and satisfy \(\int_G u^2=\int_G v^2=1\), \(\int_G uv=0\). The zero pair is trivially an equality case, omitted from the nonzero classification. No statement is made for other Fourier supports, all exponents, or all Sato–Tate subgroups.

In genus-two characteristic-polynomial notation, if \(\det(I-Tg)=1+c_1T+c_2T^2+c_1T^3+T^4\), then \(u=-c_1\) and \(v=c_2-1\). Thus the packet is precisely the pair of mean-zero, unit-variance first and second fundamental coefficient statistics for the generic compact symplectic model.

## Proof

**1. Exact Weyl moments.** On the diagonal maximal torus write \(z=e^{i\theta}\), \(w=e^{i\phi}\), so
\[
u=z+z^{-1}+w+w^{-1},\qquad
v=1+zw+zw^{-1}+z^{-1}w+z^{-1}w^{-1}.
\]
The \(C_2\) Weyl integration formula states that for any Laurent polynomial \(Q\) invariant under the Weyl group,
\[
\int_G Q(g)\,dg=\frac18\operatorname{CT}_{z,w}
\left[Q(z,w)\prod_{(r,s)\in\{(2,0),(0,2),(1,1),(1,-1)\}}
(2-z^rw^s-z^{-r}w^{-s})\right].
\]
Here \(\operatorname{CT}\) is the coefficient of \(z^0w^0\). The Weyl kernel has constant term eight, confirming normalization. Multiplying the displayed finite Laurent polynomials gives the *exact integer table*

| total degree \(n\) | \(\int_G u^{n-k}v^k\,dg\), for \(k=0,1,\ldots,n\) |
| --- | --- |
| \(2\) | \((1,0,1)\) |
| \(4\) | \((3,0,2,0,3)\) |
| \(6\) | \((14,0,11,0,10,0,15)\) |
| \(8\) | \((84,0,75,0,73,0,75,0,105)\) |

The formulas follow by a fully specified finite coefficient extraction, without numerical integration. The standalone \(\texttt{check.py}\) independently builds the Laurent coefficient maps and reproduces every entry. The vanishing of all odd-index entries also follows from the central involution \(g\mapsto-g\), under which \(u\mapsto-u\) and \(v\mapsto v\).

**2. Global phase reduction and equality.** Let \(m\in\{3,4\}\). Expansion of \(F^m\overline F^m\), together with the moment table, gives
\[
\int_G|F|^{2m}\,dg=\sum_{i,j=0}^{m}
\binom mi\binom mj a^{m-i}b^i\overline a^{m-j}\overline b^j
\int_G u^{2m-i-j}v^{i+j}\,dg.
\]
All potentially nonzero moments in this sum are **strictly positive**; the others vanish by parity. Applying the triangle inequality term by term yields
\[
\int_G|a u+b v|^{2m}\,dg\le
\int_G(|a|u+|b|v)^{2m}\,dg.
\]
For \(a b\ne0\), equality requires \(e^{2i(\arg b-\arg a)}=1\), since the \((i,j)=(0,2)\) mixed summand and its conjugate have strictly positive coefficients and maximal real part only in that phase condition. Conversely, that condition aligns every nonzero term because \(i+j\) is even, hence all the phase constraints are satisfied. Thus the maximizing ratio \(b/a\) must be real. For real magnitudes with \(p=|a|^2/(|a|^2+|b|^2)\) and \(1-p=|b|^2/(|a|^2+|b|^2)\), the degree-six and degree-eight rows and the binomial coefficients give exactly \(H_6(p)\) and \(H_8(p)\), respectively.

**3. Unique sharp magnitude and crossover.** Direct differentiation yields
\[
H'_6(p)=-3(16p^2+60p-35).
\]
It is strictly decreasing on \([0,1]\), positive at zero and negative at one, so its sole zero \(p_6=(\sqrt{365}-15)/8\) is the unique global maximum. Since \(365>19^2\), one has \(p_6>1/2\).

Similarly,
\[
H'_8(p)=28h(p),\quad h(p)=157p^3-240p^2-40p+60,
\]
\[
h'(p)=471p^2-480p-40\le-9p-40<0\quad(0\le p\le1).
\]
Here \(h(0)=60>0\), \(h(1)=-63<0\), and \(h(1/2)=-3/8<0\), so the sole maximum is attained at \(0<p_8<1/2\). Both maximizing magnitudes are strictly positive, and Step 2 gives precisely the stated nonzero equality families. Substitution proves the sharp constants. All claims follow.

## Verification

Run \(\texttt{python3 check.py}\) from a directory containing the attached standalone checker. Only the Python standard library is needed. It constructs the exact Weyl kernel, extracts the complete degree-\(0,2,4,6,8\) integer moments, checks the sixth/eighth polynomial formulas at 1001 sample ratios, verifies the algebraic critical-point signs and values, and separately compares eight complex-coefficient examples against direct \(64\times64\) torus quadrature. The latter is corroborative only; exact coefficient extraction and the global derivative proof establish the universal assertion. A recorded execution is included as \(\texttt{check_output.txt}\).

## Relationship to prior work

Costa, Fité and Sutherland (2019, arXiv:1910.00518) relate certain low Sato–Tate coefficient moments to arithmetic invariants, motivating the first two coefficient statistics. Lee and Oh (2020, arXiv:2006.06116) give symplectic-character expansions of general characteristic-polynomial autocorrelations; this is an important broad moment-calculus precursor. Their displayed identities do not provide the two sharp \(L^2\)-normalized coefficient-packet norms, strict optimizer proportions, or the sixth/eighth dominance reversal. Assiotis, Gunes, Keating and Wei (2025, arXiv:2508.09910) investigate joint moments of characteristic polynomials and derivatives evaluated at \(1\), predominantly across growing matrix dimension, rather than this fixed-rank sharp Fourier packet. The present claim is the explicit **global optimization and complete equality classification**, not the mere availability of mixed moments through general generating functions.

## Limitations

This is a fixed-rank, fixed-support theorem at two even exponents, not an all-exponent phase diagram or an arithmetic equidistribution theorem for any particular curve. The exact Weyl moments are elementary consequences of representation theory; the added sharp optimization and crossover are the asserted contributions. Broad literature searches and full-text comparisons do not establish absolute bibliographic priority. No independent mathematical validation has been performed.

## References

1. E. Costa, F. Fité and A. V. Sutherland, *Arithmetic invariants from Sato–Tate moments* (public preprint October 1, 2019), arXiv:1910.00518. https://arxiv.org/abs/1910.00518
2. K.-H. Lee and S. Oh, *Auto-correlation functions of Sato–Tate distributions and identities of symplectic characters* (public preprint June 10, 2020), arXiv:2006.06116. https://arxiv.org/abs/2006.06116
3. T. Assiotis, M. A. Gunes, J. P. Keating and F. Wei, *Joint Moments of Characteristic Polynomials from the Orthogonal and Unitary Symplectic Groups* (public preprint August 13, 2025), arXiv:2508.09910. https://arxiv.org/abs/2508.09910
