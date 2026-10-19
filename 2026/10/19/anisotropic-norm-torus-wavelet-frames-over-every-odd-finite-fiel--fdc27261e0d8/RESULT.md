# Anisotropic norm-torus wavelet frames over every odd finite field

## Finding
For every odd prime power \(q\), there is an explicit graph \(E\subset\mathbb F_q^2\), containing the origin, that tiles the plane additively, is a spectral set, and whose nonzero part \(E^*=E\setminus\{(0,0)\}\) tiles the punctured plane multiplicatively under a cyclic norm-one subgroup of \(\mathrm{GL}_2(\mathbb F_q)\) of order \(q+1\). The associated single-generator, equal-norm finite wavelet system is a Parseval frame for the codimension-one mean-zero subspace of \(\ell^2(\mathbb F_q^2)\), for **both** congruence classes \(q\equiv1,3\pmod4\), including nonprime fields.

More precisely, the system has \(q(q+1)\) vectors, norm squared \((q-1)/q\), and Gram matrix unitarily equivalent to \(q+1\) copies of
\[
 I_q-\frac1q\mathbf1_q\mathbf1_q^*,
\]
with \(q^2-1\) eigenvalues equal to \(1\) and \(q+1\) equal to \(0\). For a fixed nonsquare defining the norm form, the construction supplies exactly
\[
 \frac{q-\chi(-1)}2\,2^{(q-1)/2}
\]
distinct graphs of the displayed two-slope type, where \(\chi\) is the quadratic character of \(\mathbb F_q\).

## Assumptions and scope
Let \(q=p^m\) with \(p\) an odd prime and \(m\ge1\). Fix a nonsquare \(\delta\in\mathbb F_q^\times\) and define
\[
 N(x,y)=x^2-\delta y^2.
\]
Choose one representative from each pair \(\{t,-t\}\subset\mathbb F_q^\times\), forming \(H\) of size \((q-1)/2\). Choose \(c\in\mathbb F_q\) such that \(\lambda=1-\delta c^2\) is a nonsquare. Existence of \(c\) is proved below. Define the function \(f:\mathbb F_q\to\mathbb F_q\) by
\[
 f(0)=0,\qquad f(t)=0\ (t\in H),\qquad f(t)=ct\ (t\in-H),
\]
and the graph \(E=\{(t,f(t)):t\in\mathbb F_q\}\). Write
\[
 T=\left\{M_{u,v}=\begin{pmatrix}u&\delta v\\v&u\end{pmatrix}:u^2-\delta v^2=1\right\}.
\]
Use the unitary Fourier transform on \(\ell^2(\mathbb F_q^2)\),
\[
 \widehat h(\xi)=\frac1q\sum_{x\in\mathbb F_q^2}h(x)\exp\!\left(-\frac{2\pi i}{p}\operatorname{Tr}_{\mathbb F_q/\mathbb F_p}(\xi\cdot x)\right).
\]
Define \(\psi\) by \(\widehat\psi=q^{-1/2}\mathbf1_{E^*}\), and for \(M\in T\), \(s\in\mathbb F_q\), set \(w_{M,s}(x)=\psi(M^{\mathsf T}x+(s,0))\). The target space is
\[
 \mathcal H_0=\left\{h\in\ell^2(\mathbb F_q^2):\sum_{x\in\mathbb F_q^2}h(x)=0\right\}.
\]
All claims concern this finite, explicitly normalized construction; not full-space orthonormal wavelet bases.

## Proof
**1. Choice and count of slopes.** For the quadratic character \(\chi\), counting solutions to \(y^2=x^2-a\) for \(a\ne0\) through \((x-y)(x+y)=a\) gives \(\sum_x\chi(x^2-a)=-1\). Hence
\[
 \sum_{c\in\mathbb F_q}\chi(1-\delta c^2)=-\chi(-\delta)=\chi(-1).
\]
The argument of \(\chi\) never vanishes, because \(\delta\) is nonsquare. Therefore exactly \((q-\chi(-1))/2>0\) choices of \(c\) have \(\chi(1-\delta c^2)=-1\). In particular \(c\ne0\).

**2. Simultaneous graph spectrum and additive tiling.** Each first coordinate occurs once in \(E\). Thus \(E\) tiles \(\mathbb F_q^2\) by translations \(\{(0,z):z\in\mathbb F_q\}\). The \(q\) characters \(\xi\mapsto\exp(2\pi i\operatorname{Tr}(s\xi_1)/p)\), \(s\in\mathbb F_q\), restrict to an orthogonal basis on \(E\), since the first coordinates range over the entire field. Hence \(E\) is spectral.

**3. Norms enumerate every nonzero value once.** Since \(H\) and \(-H\) each contain one member of every pair \(\{t,-t\}\), their squared images are both the set of nonzero squares. For \(t\in H\), \(N(t,f(t))=t^2\); for \(t\in-H\), \(N(t,f(t))=\lambda t^2\). The first set runs over all squares, while the second runs over all nonsquares because \(\lambda\) is nonsquare. Thus \(N:E^*\to\mathbb F_q^\times\) is bijective.

**4. Norm-one dilation tiling.** Identify \((x,y)\) with \(x+y\sqrt\delta\in\mathbb F_{q^2}\), whose norm to \(\mathbb F_q\) is \(N(x,y)\). The norm map \(\mathbb F_{q^2}^\times\to\mathbb F_q^\times\) is surjective, so its kernel \(T\) is cyclic of order \(q+1\) and acts freely and transitively on each nonzero norm level. By Step 3, the sets \(ME^*\), \(M\in T\), are pairwise disjoint and partition \(\mathbb F_q^2\setminus\{0\}\).

**5. Parseval identity and exact Gram matrix.** Put \(e(z)=\exp(2\pi i\operatorname{Tr}(z)/p)\). Direct Fourier transformation gives
\[
 \widehat w_{M,s}(\xi)=q^{-1/2}\mathbf1_{ME^*}(\xi)e\big(s\pi_1(M^{-1}\xi)\big).
\]
On the block \(ME^*\), parameterized bijectively by \(\xi=M(t,f(t))\), \(t\in\mathbb F_q^\times\), character orthogonality gives
\[
 \sum_{s\in\mathbb F_q}\widehat w_{M,s}(\xi)\overline{\widehat w_{M,s}(\eta)}
 =\frac1q\sum_s e\big(s(t-t')\big)=\mathbf1_{t=t'}.
\]
Consequently each block is a Parseval frame for \(\ell^2(ME^*)\). Different blocks have disjoint supports, proving Parseval tightness on \(\mathcal H_0\). Moreover,
\[
 \langle w_{M,s},w_{M,s'}\rangle=\frac1q\sum_{t\ne0}e\big((s-s')t\big)
 =\mathbf1_{s=s'}-\frac1q,
\]
and cross-block inner products are zero. The asserted Gram spectrum, nullity, norms, and simplex decomposition follow.

**6. Counting explicit graphs.** For each admissible \(c\), there are \(2^{(q-1)/2}\) choices of \(H\). The graph determines both \(c\) (from any nonzero slope value) and \(H\) (from the zero-slope locations), so all graphs for a fixed \(\delta\) are distinct. This yields the stated count.

## Verification
The standalone `verify_wavelet.py` uses exact finite-field arithmetic and independently tests every norm value, the order and orbit partition of the norm-one group, and the complex Fourier-block Gram entries. It passed eight fields of orders \(3,5,7,9,11,13,25,27\), including both prime powers and the difficult \(q\equiv1\pmod4\) cases. The largest numerical block-Gram discrepancy was below \(1.7\times10^{-16}\). The general theorem rests on the foregoing proof, not on finite computation. Run `python3 verify_wavelet.py` using only the Python standard library; `verification_output.json` records the observed output.

## Relationship to prior work
Iosevich, Lai and Mayeli [1] establish the finite wavelet-frame tiling criterion and construct graph-based rotational tiles over prime fields with \(q\equiv3\pmod4\). Their Proposition 4.6 excludes Euclidean norm rotations when \(q\equiv1\pmod4\), and Section 5 explicitly asks for existence in that regime and for prime-power extensions. Here the **anisotropic norm form** supplies a different dilation group and an explicit graph transversal for every odd prime power; the general spectral-pair-to-wavelet argument in [1] is acknowledged rather than treated as new. Rahimi and Seddighi [2] study a one-dimensional cyclic-prime wavelet setting. Mayeli [3] treats tiling and wavelet-basis criteria in infinite locally compact abelian groups rather than this explicit finite-field design.

## Limitations
This is a two-dimensional finite-field construction with odd characteristic, and an equal-norm Parseval **frame** for the mean-zero subspace, not a basis for all \(\ell^2\). No claim is made for characteristic two, all dilation subgroups, all possible graph transversals, or an unrestricted optimality problem. General spectral and tiling criteria were known. Although the exact anisotropic construction was not identified in the inspected sources, a prior equivalent under a different norm/rotation parametrization remains possible. A related 2021 paper on Riesz and tight wavelet frame sets on locally compact abelian groups [4] was only available at abstract level and was not excluded by full-text comparison.

## References
[1] A. Iosevich, C.-K. Lai, A. Mayeli, *Tight Wavelet Frame Sets in Finite Vector Spaces*, arXiv:1703.06842, first posted 2017-03-20. https://arxiv.org/abs/1703.06842

[2] A. Rahimi, N. Seddighi, *Finite Equal Norm Parseval Wavelet Frames over Prime Fields*, arXiv:1705.11127, first posted 2017-05-30. https://arxiv.org/abs/1705.11127

[3] A. Mayeli, *Riesz Wavelets, Tiling and Spectral Sets in LCA Groups*, arXiv:1703.06771, first posted 2017-03-20. https://arxiv.org/abs/1703.06771

[4] A. K. Sinha, R. Sahoo, *Riesz and Tight Wavelet Frame Sets in Locally Compact Abelian Groups*, Kyungpook Mathematical Journal 61 (2021), 371–381, DOI:10.5666/KMJ.2021.61.2.371.
