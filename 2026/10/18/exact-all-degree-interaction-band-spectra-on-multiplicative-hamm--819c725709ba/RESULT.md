# Exact all-degree interaction-band spectra on multiplicative Hamming varieties

## Finding

Let \(q\ge3\) be a prime power, \(d\ge2\), \(j\in\mathbb F_q^\times\), and \(0\le k\le d\). For the Hamming variety
\[
H_j=\{(x_1,\ldots,x_d)\in(\mathbb F_q^\times)^d:\ x_1\cdots x_d=j\},
\]
put \(M=q-1\). Choose a generator \(g\) of \(\mathbb F_q^\times\) and define \(\chi_a(g^u)=e^{2\pi i au/M}\), \(a\in\mathbb Z/M\mathbb Z\). For every index \(\alpha=(\alpha_1,\ldots,\alpha_d)\in(\mathbb Z/M\mathbb Z)^d\), set \(\Phi_\alpha(x)=\prod_i\chi_{\alpha_i}(x_i)\). Restrict the **interaction band**
\[
\mathcal B_k=\{\Phi_\alpha:\#\{i:\alpha_i\ne0\}\le k\}
\]
to \(H_j\), with normalized uniform measure on \(H_j\). Let \(T_k\) send Euclidean coefficient vectors of the listed characters to their restricted functions, and put \(G_k=T_k^*T_k\).

**Complete spectral law.** For \(\alpha\in(\mathbb Z/M\mathbb Z)^d\), write \(n_c(\alpha)=\#\{i:\alpha_i=c\}\). The diagonal-shift orbit \(C_\alpha=\{\alpha+(c,\ldots,c):c\in\mathbb Z/M\mathbb Z\}\) contains
\[
t(C_\alpha)=\#\{c\in\mathbb Z/M\mathbb Z:n_c(\alpha)\ge d-k\}
\]
indices from the interaction band. Every orbit with \(t>0\) contributes exactly **one** eigenvalue \(t\) and \(t-1\) zero eigenvalues to \(G_k\); orbits with \(t=0\) contribute no columns. Consequently the multiplicity of positive eigenvalue \(r\) is the explicit integer
\[
\boxed{\displaystyle
\mu_r=\frac1M\sum_{\substack{n_0+\cdots+n_{M-1}=d\\\#\{c:n_c\ge d-k\}=r}}
\frac{d!}{n_0!\cdots n_{M-1}!}.}
\]
The number of columns is \(B_k=\sum_{s=0}^k\binom ds(M-1)^s\), the rank is \(\sum_{r\ge1}\mu_r\), and the nullity is \(B_k-\sum_{r\ge1}\mu_r\). These formulas describe **all** singular values, including zeros, for every permitted parameter.

**Two sharp degree thresholds.** The columns are orthonormal (hence linearly independent) if and only if \(2k<d\). They span the entire \((q-1)^{d-1}\)-dimensional space \(L^2(H_j)\) if and only if
\[
\boxed{\displaystyle k\ge d-\left\lceil\frac d{q-1}\right\rceil.}
\]
For \(0\le k<d\), all positive eigenvalue levels occur and are precisely
\[
\boxed{1,2,\ldots,\min\left\{q-1,\left\lfloor\frac d{d-k}\right\rfloor\right\};}
\]
at \(k=d\) the only positive eigenvalue is \(q-1\). Thus each new level \(2\le r\le\min\{q-1,d\}\) first appears exactly at degree \(d-\lfloor d/r\rfloor\).

At the first loss of independence in even dimension \(d=2m\), i.e. at \(k=m\), precisely \(\frac{q-2}{2}\binom{2m}{m}\) distinct diagonal-shift orbits have two columns, producing exactly that many zero eigenvalues and eigenvalues \(2\). For \(q=3\) and odd \(d\), the band \(k=(d-1)/2\) gives an **orthonormal basis** of functions on \(H_j\).

## Assumptions and scope

All function spaces use complex coefficients. The coefficient space for \(T_k\) has the Euclidean norm in the *multiplicative-character tensor basis*, which is orthonormal on the unrestricted torus \((\mathbb F_q^\times)^d\); the target has the normalized counting norm on \(H_j\). The calculated singular values refer to this canonical multiplicative preconditioning, **not** to the unconditioned list of ambient additive characters.

The spans nevertheless agree with the corresponding additive-coordinate Fourier interaction bands restricted from \(\mathbb F_q^d\): on the nonzero elements of one coordinate, the \(q\) additive characters span the full \((q-1)\)-dimensional function space, and changing to its \(q-1\) multiplicative characters is an invertible basis change. Tensoring by subsets of at most \(k\) active coordinates gives equality of the two restricted band **spaces**, without claiming equality of their raw Gram spectra. The field may have even or odd characteristic, and the conclusion is independent of the chosen nonzero level \(j\).

## Proof

**1. Exact inner products.** Write \(j=g^b\), and write every \(x_i=g^{u_i}\), with \(u_i\in\mathbb Z/M\mathbb Z\). Then \(H_j\) is the affine congruence \(\sum_i u_i=b\pmod M\) and has \(M^{d-1}\) points. For any two frequency indices \(\alpha,\beta\), averaging \(\Phi_\alpha\overline{\Phi_\beta}\) over the free variables \(u_1,\ldots,u_{d-1}\) gives zero unless \(\alpha_i-\beta_i\) is a common residue \(c\) for all \(i\). In that exceptional case the average is \(e^{2\pi i cb/M}\). Therefore two restricted columns are either orthogonal or proportional by a unit phase; proportionality is exactly membership in the same diagonal-shift orbit. Every orbit has \(M\) distinct indices.

**2. Exact block spectra and occupancies.** A band index belongs to the orbit of \(\alpha\) precisely when the common shift makes at least \(d-k\) of its coordinates zero. This happens once for each distinct character label occurring at least \(d-k\) times in \(\alpha\), proving the formula for \(t(C_\alpha)\). After conjugating each column by an appropriate unit scalar, the Gram block of an occupied orbit is the all-ones matrix of size \(t\), with spectrum \(\{t,0^{[t-1]}\}\). Orbits of different classes are orthogonal. Among all \(M^d\) full-torus indices, the number with prescribed occupancy vector \((n_0,\ldots,n_{M-1})\) equals \(d!/(\prod_c n_c!)\). Each orbit contains exactly \(M\) indices, and \(t\) is orbit invariant. Dividing the occupancy count by \(M\) proves the multiplicity formula and the rank/nullity identities, including \(k=d\).

**3. First dependency and all eigenvalue levels.** If two distinct shifts of a single orbit have at most \(k\) nonzero entries, their nonzero supports must cover all \(d\) positions: their coordinatewise difference is a nonzero constant. Hence \(d\le2k\). Conversely, when \(2k\ge d\), choose a nonzero residue \(c\), divide the coordinates into two groups each of size at most \(k\), and assign frequency label \(0\) on one group and \(c\) on the other. Its two suitable shifts have weight at most \(k\), proving strict non-injectivity and the sharp boundary.

For \(k<d\), a given orbit contains exactly as many admissible shifts as there are alphabet symbols occurring at least \(s=d-k\) times among its \(d\) coordinates. Thus at most \(\min\{M,\lfloor d/s\rfloor\}\) such shifts exist. For each integer \(1\le r\le\min\{M,\lfloor d/s\rfloor\}\), choose exactly \(r\) different labels, give each at least \(s\) occurrences, and allocate the remaining occurrences to one of these labels. This creates an orbit with exactly \(r\) admissible shifts. The claimed integer spectral levels and their first degrees follow.

**4. Exact interpolation threshold.** The band spans the target if and only if every diagonal-shift orbit is occupied: the \(M^{d-1}\) different occupied orbit functions are mutually orthogonal and each full-torus orbit contributes one basis direction on \(H_j\). Every \(d\)-tuple over an alphabet of \(M\) symbols has some symbol occurring at least \(\lceil d/M\rceil\) times, and balanced occupancy vectors attain this bound. Hence the maximum, over all orbits, of their minimum Hamming weight is exactly \(d-\lceil d/M\rceil\). This proves necessity and sufficiency.

**5. Boundary corollaries.** If \(d=2m\) and \(k=m\), two admissible shifts require disjoint complementary nonzero supports of size \(m\), so exactly two labels each occur \(m\) times. Counting choices of the two labels and the support, then dividing by \(M\), gives \(\binom M2\binom{2m}m/M=(M-1)\binom{2m}m/2\) double blocks. If \(M=2\) and \(d\) is odd, the interpolation threshold is \((d-1)/2<d/2\), so the target is spanned by orthonormal columns, completing the proof.

## Verification

The accompanying independent checker enumerates interaction-band indices and diagonal orbits, compares the orbit spectra with independently computed multinomial occupancy counts, and checks the sharp injectivity/interpolation threshold identities for \(124\) parameter triples. It also constructs normalized **complex** restricted character matrices directly on multiplicative exponent hyperplanes for \(56\) cases and diagonalizes their Gram matrices, with maximum discrepancy \(6.67\times10^{-15}\). The tests include both zero and nonzero product levels and the orthonormal \(q=3\), odd-\(d\) boundary. Run `python verify.py` with NumPy available. The quantified theorem is proved by the preceding character and occupancy argument; numerical checks do not establish the infinite-family result.

## Relationship to prior work

Cheong, Koh, and Pham studied the same Hamming varieties and proved finite-field \(L^2\) Fourier extension estimates, together with their additive Fourier-decay formula (2019 preprint, sections 1, 3, and 4). Those results do not state or quantify the all-interaction-degree multiplicative-character Gram spectrum, its exact occupancy multiplicities, or the two sharp sampling thresholds. The separate online work *An all-degree spectral law for Fourier sampling on q-ary Hamming spheres* treats additive Hamming-weight shells, not the fixed **multiplicative product** variety considered here; its Hamming-sphere eigenvalues do not specialize to the diagonal-shift occupancy formula. General finite-group character orthogonality supplies the mechanism for the Gram blocks, but the complete multidegree occupancy law and the two sharp interpolation/isometry thresholds are the extra specialized conclusions established above.

## Limitations

The integer Gram eigenvalues depend on the use of the canonically orthonormal multiplicative-character tensor basis before restriction. No such integer-spectrum claim is made for the raw additive-character frame. The result concerns deterministic exact sampling of entire interaction bands, not sparse recovery within a band, noisy inversion, sharp unrestricted \(L^p\) extension constants, or best numerical conditioning under arbitrary nonunitary basis changes. The finite literature comparison cannot rule out an equivalent earlier occupancy theorem, particularly one phrased in terms of quotient characters or parity-check codes. No independent mathematical audit has been performed.

## References

[1] D. Cheong, D. Koh, and T. Pham, *Extension theorems for Hamming varieties over finite fields*, arXiv:1903.03904, initially posted 2019-03-10, 2010 MSC 42B05, 11T23, https://arxiv.org/abs/1903.03904.

[2] *An all-degree spectral law for Fourier sampling on q-ary Hamming spheres*, public mathematical note dated 2026-10-11, with a different fixed-weight geometric constraint.
