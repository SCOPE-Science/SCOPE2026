# Exact Hilbert maximal-averaging norms on the first diameter-three cycles

## Finding

For the centered Hardy–Littlewood graph-ball maximal operator \(M_n\) on the unweighted cycles \(C_6\) and \(C_7\), the exact sharp real and complex \(\ell^2\) norms are \(\|M_n\|_{2\to2}=\sqrt{\Lambda_n}\), with \(\Lambda_6\) the largest real root of
\[
24300z^5-73710z^4+68847z^3-20992z^2+2011z-48=0
\]
and \(\Lambda_7\) the largest real root of
\[
11025z^3-22603z^2+9188z-680=0.
\]
Their exact isolations are \(1.520400<\Lambda_6<1.520401\) and \(1.532672<\Lambda_7<1.532673\), giving \(\|M_6\|\approx1.2330453849\) and \(\|M_7\|\approx1.2380116494\).

The maximizing ball-selection masks are exactly the twelve dihedral images of \(\sigma_6=(0,1,0,1,2,3)\) and the seven dihedral images of \(\sigma_7=(0,1,2,3,3,2,1)\). For each representative averaging matrix \(A_{n,\sigma_n}\), let \(v_n\) be the unique positive unit Perron vector of \(A_{n,\sigma_n}^{\mathsf T}A_{n,\sigma_n}\). Every nonzero extremizing input has modulus a positive scalar multiple of a dihedral permutation of \(v_n\); arbitrary independent real signs or complex phases are permitted.

## Assumptions and scope

Vertices of \(C_n\), for \(n\in\{6,7\}\) only, are \(\mathbb Z/n\mathbb Z\) with graph distance \(d(i,j)=\min\{(i-j)\bmod n,(j-i)\bmod n\}\). Define \(B(i,r)=\{j:d(i,j)\le r\}\), and for real or complex \(f\),
\[
(M_nf)(i)=\max_{0\le r\le3}\frac1{|B(i,r)|}\sum_{j\in B(i,r)}|f(j)|.
\]
Counting measure or normalized counting measure has the same induced norm. No claim for larger cycles, weighted variants, uncentered balls or variation norms is made.

## Proof

**Finite selector identity.** For each mask \(\sigma\in\{0,1,2,3\}^n\), let the nonnegative matrix \(A_{n,\sigma}\) have row \(i\) equal to the normalized indicator of \(B(i,\sigma_i)\). Then exactly
\[
\|M_nf\|_2^2=\max_\sigma\|A_{n,\sigma}|f|\|_2^2,
\qquad
\|M_n\|_{2\to2}^2=\max_\sigma\lambda_{\max}(A_{n,\sigma}^{\mathsf T}A_{n,\sigma}).
\]
For the second equality, taking coordinatewise modulus cannot decrease the output of any nonnegative matrix, so its top singular value is attained on nonnegative input.

**Exhaustive exact separator.** Put \(U_{n,\sigma}=d_nA_{n,\sigma}\), where \(d_6=30\) and \(d_7=105\) clear every denominator of the four ball sizes. Construct the dihedral orbits \(W_n\) of the displayed representative masks; they have respectively \(12\) and \(7\) distinct elements. For each of the \(4096-12=4084\) masks outside \(W_6\), the six leading principal minors of
\[
30^2\cdot1517I-1000U_{6,\sigma}^{\mathsf T}U_{6,\sigma}
\]
are strictly positive integers. For each of the \(16384-7=16377\) masks outside \(W_7\), the seven leading principal minors of
\[
105^2\cdot1531I-1000U_{7,\sigma}^{\mathsf T}U_{7,\sigma}
\]
are strictly positive integers. Sylvester's criterion gives strict spectral upper bounds \(1517/1000\) and \(1531/1000\) for every losing mask. The companion `verify_cycles.py` constructs **every mask** and recomputes every determinant with exact fraction-free integer elimination and exact division checks; this is exhaustive finite enumeration, not sampling.

**Strict winning bounds and characteristic polynomials.** Use the integer Rayleigh vectors
\[
F_6=(699001,181094,1000000,204881,204881,101856),
\quad F_7=(1000000,201666,201666,144076,144076,201666,201666).
\]
The exact integer certificate verifies the two strict inequalities
\[
\frac{\|U_{6,\sigma_6}F_6\|_2^2}{30^2\|F_6\|_2^2}>\frac{1520400}{1000000}>\frac{1517}{1000},
\quad
\frac{\|U_{7,\sigma_7}F_7\|_2^2}{105^2\|F_7\|_2^2}>\frac{1532672}{1000000}>\frac{1531}{1000}.
\]
The positive leading-minor test on representative Gram matrices at \(1520401/1000000\) and \(1532673/1000000\) establishes the matching upper root-isolation bounds. Direct signed principal-minor expansion gives
\[
\det(zI-U_{6,\sigma_6}^{\mathsf T}U_{6,\sigma_6})=z(z^5-2730z^4+2294900z^3-629760000z^2+54297000000z-1166400000000),
\]
\[
\det(zI-U_{7,\sigma_7}^{\mathsf T}U_{7,\sigma_7})=z^3(z-3332)(z^3-22603z^2+101297700z-82654425000).
\]
Substitution \(z=d_n^2\Lambda_n\) and removal of nonzero constant factors yield the stated quintic and cubic. Strict separators show no other mask ties the maxima.

**All equality cases.** Isometries of the cycle conjugate representative selectors to the other masks in their orbits. Since radius three covers the entire graph, a uniform averaging row in each representative makes every entry of its Gram matrix positive. Perron–Frobenius gives a simple top eigenvalue with a unique positive modulus eigenvector up to scale. The finite selector identity then shows that precisely the stated dihedral modulus classes attain the norm. Because \(M_nf=M_n|f|\), coordinatewise signs/phases are unconstrained.

## Verification

Run `python3 verify_cycles.py` in the directory containing this document. The standard-library-only checker enumerates all \(4^6+4^7=20480\) selectors, proves every losing separator by strict positivity of each leading principal minor, checks the integer Rayleigh witnesses and upper bounds, and derives both complete characteristic polynomials from exact integer principal minors. It prints `ALL_CERTIFICATES_OK` upon success. The theorem for only two finite cycles is concluded by the analytical selector and equality reductions above; no infinite-cycle extrapolation is asserted.

## Relationship to prior work

Soria and Tradacete (2014) developed maximal operators on finite graphs, obtaining general graph bounds and a four-cycle example. González-Riquelme and Madrid (2020) studied strong-type Hilbert norms for complete graphs and stars. A related 2026 paper computes variation rather than ordinary strong-type norms on smaller graphs. These results do not give the two present algebraic cycle constants or their complete equality classes in inspected statements. The finite selector reduction itself is not claimed as new; the exact global selector comparison and structural parity contrast are the findings. No exhaustive historical-priority guarantee is claimed.

## Limitations

Only the first two diameter-three cycles are included. The decisive spectral inequalities use a complete finite exact-integer certificate, rather than a conceptual uniform formula for arbitrary cycle size. Numerical values are illustrative; strict claims follow from exact rational bounds. Independent mathematical and bibliographic audits have not been performed, and uninspected specialist sources may overlap.

## References

1. J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204v1 (22 October 2014), https://arxiv.org/abs/1410.6204.
2. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146v1 (2020), https://arxiv.org/abs/2005.03146.
3. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, arXiv:2011.02630v1 (2020), https://arxiv.org/abs/2011.02630.
4. C. González-Riquelme, V. Kovač, and J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462v1 (2026), https://arxiv.org/abs/2603.12462.
