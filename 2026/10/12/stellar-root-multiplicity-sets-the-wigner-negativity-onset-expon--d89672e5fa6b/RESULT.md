# Stellar-root multiplicity sets the Wigner-negativity onset exponent under pure loss

## Finding
For every normalized, nonvacuum, finite Fock-support pure state of one optical mode, the leading onset power of Wigner negative volume at the one-half-transmissivity boundary is determined by the **smallest multiplicity of a zero** of the state's stellar (Segal–Bargmann) polynomial—not by its total degree. The leading coefficient is an explicit positive sum of local contributions from precisely those least-multiple zeros.

Precisely, write the finite stellar polynomial of the input state as
\[
f(z)=\sum_{k=0}^{N}\frac{c_k}{\sqrt{k!}}z^k,\qquad N\ge1,\quad c_N\ne0,\quad\sum_{k=0}^{N}|c_k|^2=1.
\]
Let its distinct complex zeros be \(z_1,\ldots,z_s\), of positive multiplicities \(m_1,\ldots,m_s\), and write
\[
a_j=\frac{f^{(m_j)}(z_j)}{m_j!}\ne0,\qquad m_* = \min_{1\le j\le s}m_j.
\]
For the quantum-limited pure-loss channel of transmissivity \(\eta\), use the normalized output Wigner function \(W_\eta\) with \(\int_{\mathbb C}W_\eta(\beta)\,d^2\beta=1\), and set its negative volume to
\[
\mathcal N(\eta)=\int_{\mathbb C}\max\{0,-W_\eta(\beta)\}\,d^2\beta.
\]
For \(m\ge1\), let \(L_m(x)=\sum_{k=0}^m(-1)^k\binom{m}{k}x^k/k!\) be the ordinary Laguerre polynomial, and define the finite positive universal constant
\[
C_m=\int_0^\infty\max\{0,(-1)^{m+1}L_m(x)\}\,dx.
\]
Then, as \(q=2\eta-1\downarrow0\) through positive values,
\[
\boxed{\mathcal N(\eta)=A_fq^{m_*+1}+o(q^{m_*+1}),\qquad
 A_f=m_*!C_{m_*}\sum_{\{j:m_j=m_*\}}e^{-|z_j|^2}|a_j|^2>0.}
\]
For a squarefree stellar polynomial the exponent is always two, with \(A_f=\frac12\sum_j e^{-|z_j|^2}|f'(z_j)|^2\). For the number state \(|N\rangle\), the exponent is \(N+1\) and the coefficient is \(C_N\). In particular, \(C_1=1/2\) and \(C_2=4\sqrt2/3\). The already-known general one-half-transmissivity positivity boundary is **not** claimed as new.

## Assumptions and scope
The single optical mode obeys the usual bosonic commutation relation. Input is the normalized pure state \(|\psi\rangle=\sum_{k=0}^N c_k|k\rangle\), with finite nonzero degree \(N\). The quantum-limited attenuator mixes this mode with environmental vacuum on a beamsplitter of intensity transmissivity \(\eta\in[0,1]\). No thermal excitations, phase diffusion, other noise, infinite Fock tails, multimode coupling, or simultaneous state-dependent limit are assumed. Complex phase-space coordinate \(\beta\) satisfies \(W_{|0\rangle}(\beta)=2e^{-2|\beta|^2}/\pi\); consequently \(d^2\beta\) is the ordinary planar Lebesgue area. The specified coefficient is not invariant under changing the input state while taking the limit; this is a fixed-input theorem.

## Proof
**1. Exact polynomial representation of the lossy Wigner function.** Write \(q=2\eta-1\). The exact formula, for every \(\eta\in[0,1]\), is
\[
 W_\eta(\beta)=\frac{2}{\pi}e^{-2|\beta|^2}
 \sum_{\ell=0}^N\frac{(-q)^\ell}{\ell!}
 \left|f^{(\ell)}(2\sqrt\eta\,\beta)\right|^2. \tag{1}
\]
This is a finite identity, obtained without a limiting approximation. One verification from the standard attenuator Kraus expansion is as follows. For \(0\le k,l\le N\),
\[
\mathcal E_\eta(|k\rangle\langle l|)
=\sum_{h=0}^{\min(k,l)}\sqrt{\binom{k}{h}\binom{l}{h}}
\eta^{(k+l)/2-h}(1-\eta)^h
|k-h\rangle\langle l-h|.
\]
For \(r\ge s\), the Wigner matrix element is
\[
W_{|r\rangle\langle s|}(\beta)=\frac2\pi e^{-2|\beta|^2}(-1)^s
\sqrt{\frac{s!}{r!}}(2\beta)^{r-s}L_s^{(r-s)}(4|\beta|^2),
\]
with the opposite ordering given by complex conjugation. Inserting the Kraus expansion and the finite Laguerre sum and collecting powers of \(2\sqrt\eta\,\beta\) yields (1). Equivalently, coefficient comparison uses the elementary polynomial identity
\[
\sum_{\ell=0}^{\min(k,l)}\frac{(-q)^\ell}{\ell!}
\frac{k!}{(k-\ell)!}\frac{l!}{(l-\ell)!}
 z^{k-\ell}\bar z^{l-\ell}
\]
for each input matrix element \(c_k\bar c_l/\sqrt{k!l!}\). A completely independent numerical replay of the Kraus–Laguerre side and derivative side is included in the verifier. When \(q\le0\), every summand in (1) is nonnegative, recovering the known absence of Wigner negativity under at least one-half loss.

**2. Exact negative-volume integral.** Set \(z=2\sqrt\eta\,\beta\), so \(2\eta=1+q\). Defining the real polynomial
\[
 P_q(z)=\sum_{\ell=0}^N\frac{(-q)^\ell}{\ell!}|f^{(\ell)}(z)|^2,
\]
the Jacobian gives the exact identity, for \(q>0\),
\[
\mathcal N(\eta)=\frac{1}{\pi(1+q)}
\int_{\mathbb C}e^{-|z|^2/(1+q)}[-P_q(z)]_+\,d^2z,
\qquad [t]_+=\max\{0,t\}. \tag{2}
\]

**3. Exhaustive localization of possible negativity.** Let \(z_j\) be any root of order \(m=m_j\). Choose pairwise disjoint fixed disks about the roots containing no other zeros. On each disk, the factorization \(f(z)=(z-z_j)^m h_j(z)\) with \(h_j(z_j)\ne0\) implies, for \(r=|z-z_j|\) small, \(|f(z)|\ge c_jr^m\) and \(|f^{(\ell)}(z)|\le C_{j,\ell}r^{\max\{m-\ell,0\}}\). For \(r\ge R\sqrt q\), the ratio of each subtracted term of order \(\ell\le m\) to \(|f(z)|^2\) is bounded by a constant times \(R^{-2\ell}\); for \(\ell>m\) it is bounded by a constant times \(q^{\ell-m}R^{-2m}\). Taking \(R\) large, then \(q\) sufficiently small, forces \(P_q(z)>0\) throughout those annuli. On a fixed compact subset of the remaining plane the nonvanishing \(|f|^2\) dominates by continuity as \(q\downarrow0\). Finally, because \(f\) is a polynomial, \(|f^{(\ell)}(z)/f(z)|=O(|z|^{-\ell})\) at infinity; thus all large \(|z|\) also have \(P_q(z)>0\) uniformly for small \(q\). Hence, for all sufficiently small positive \(q\), the entire negative support is contained in disjoint disks \(|z-z_j|\le R\sqrt q\). This establishes completeness rather than assuming a finite experimental sampling grid finds all negative lobes.

**4. Blow-up at each zero.** Put \(z=z_j+\sqrt q\,w\). Taylor's theorem at a zero of order \(m\) gives, uniformly for bounded complex \(w\),
\[
 q^{-m}P_q(z_j+\sqrt q\,w)
\longrightarrow
|a_j|^2\sum_{\ell=0}^m\frac{(-1)^\ell}{\ell!}
\left(\frac{m!}{(m-\ell)!}\right)^2|w|^{2(m-\ell)}
=|a_j|^2(-1)^m m!L_m(|w|^2). \tag{3}
\]
Terms with \(\ell>m\) vanish after the displayed normalization. The negative-part map is continuous and Lipschitz. On the fixed scaled disks from step 3, dominated convergence therefore applies to (2), including the Gaussian factor, and yields the contribution
\[
q^{m+1}e^{-|z_j|^2}|a_j|^2\frac{m!}{\pi}
\int_{\mathbb C} [(-1)^{m+1}L_m(|w|^2)]_+\,d^2w
+o(q^{m+1}).
\]
Polar coordinates \(x=|w|^2\) give \(d^2w\) radial integral \(\pi\,dx\), and all possible negative Laguerre lobes lie in a bounded interval. The integral is precisely \(\pi C_m\). Higher-multiplicity roots contribute asymptotically smaller terms, and summing the finite collection of roots proves the stated coefficient and exponent. The positivity of \(C_m\) follows from the \(m\) simple positive zeros of \(L_m\), which force a negative lobe of \((-1)^mL_m\), for every \(m\ge1\). The Gaussian and squared-leading-coefficient factors are positive, so cancellation between different zeros is impossible.

## Verification
Run `python verify.py` with Python 3, NumPy, and SciPy as specified in `requirements.txt`. Its independent calculation forms the lossy density matrix using the Fock-basis beamsplitter Kraus coefficients, then evaluates the Wigner function via generalized Laguerre matrix elements. It checks (1) on 720 state/channel/phase-space combinations, including complex input amplitudes and efficiencies below and above one-half. Separately, quadrature of the local negative regions checks the leading coefficients for one-photon, two-photon, squarefree and mixed-multiplicity polynomial states at twelve near-threshold settings. The diagnostic prints the measured coefficient ratios; those finite tests corroborate but cannot replace the all-degree, all-input proof. In particular, a mixed-root example with one double and one simple zero has onset exponent two, not three. This matches the minimum-multiplicity rather than maximum-multiplicity rule.

## Relationship to prior work
Kenfack and Życzkowski introduced and evaluated negative-volume measures of Wigner nonclassicality, including number-state Laguerre expressions. Chabaud, Markham and Grosshans established the Segal–Bargmann/stellar representation in terms of Husimi zeros, including multiplicity, and characterized the stellar rank. Nugmanov, Zunikov and Khalili established the **already-known** sharp 50-percent survival threshold for pointwise Wigner negativity of non-Gaussian pure states. In the latter paper the dissipation-rate comparison uses the minimum of the Wigner function, and a detailed negative-volume treatment is explicitly deferred; a pointwise-minimum exponent does not imply the integrated-volume exponent because the shrinking negative region adds a power of \(q\). Zinoghli and Salehi examined additive Gaussian noise and numerically plotted Fock-state negative volumes. Gaussian convolution is relevant to attenuator smoothing after rescaling, so that work is compared by its quantitative claim rather than excluded by channel nomenclature. Those results do not state the all-polynomial local multiplicity-resolved, exact-coefficient asymptotic proved above in the inspected text. A specialized equivalent result elsewhere remains a publication-priority risk; database search absence is not proof of novelty.

## Limitations
This is an analytic asymptotic for each fixed finite Fock-support pure state. It establishes neither a uniform remainder as roots coalesce nor a theorem for infinite-degree stellar functions, mixed inputs, thermal attenuators, or multi-mode states. A root of multiplicity greater than one can split under an arbitrarily small perturbation of the input, changing the exponent in the subsequent fixed-state limit; the two limits need not commute. The coefficient is in a half-of-\(L^1\)-excess convention, and differs by a factor of two from papers that call the full \(L^1\)-excess the negative volume. It does not assert that photon-number Fock states uniquely maximize robustness, nor that any finite test is a proof for arbitrary degree. Independent publication-priority assessment has not been performed.

## References
1. A. Kenfack and K. Życzkowski, *Negativity of the Wigner function as an indicator of nonclassicality*, arXiv:quant-ph/0406015v1 (publicly posted 2004-06-02), https://arxiv.org/abs/quant-ph/0406015.
2. U. Chabaud, D. Markham and F. Grosshans, *Stellar representation of non-Gaussian quantum states*, arXiv:1907.11009v3 (first posted 2019-07-25), https://arxiv.org/abs/1907.11009.
3. B. Nugmanov, N. Zunikov and F. Khalili, *Robustness of negativity of the Wigner function to dissipation*, arXiv:2201.03257v1 (2022-01-10), https://arxiv.org/abs/2201.03257.
4. E. Zinoghli and J. A. Salehi, *Fock States in Additive Gaussian Noise Channels: Analytical and Numerical Considerations*, IET Quantum Communication 6, e70011 (2025), https://doi.org/10.1049/qtc2.70011.
