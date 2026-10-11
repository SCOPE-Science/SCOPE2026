# Sharp qutrit even-Schatten off-diagonal bounds and phase-holonomy extremizers

## Finding
Fix the standard orthonormal basis of \(\mathbb C^3\). For a density matrix \(\rho\succeq0\) with \(\operatorname{Tr}\rho=1\), write \(\Delta\rho=\operatorname{diag}(\rho_{11},\rho_{22},\rho_{33})\), \(B=\rho-\Delta\rho\), and \(t=\operatorname{Tr}(\rho^2)\). For **every integer \(m\ge3\)** and every \(t\in[1/3,1]\),

\[
\max_{\substack{\rho\succeq0,\ \operatorname{Tr}\rho=1\\ \operatorname{Tr}(\rho^2)=t}}
\|\rho-\Delta\rho\|_{S_{2m}}
=\frac{(2^{2m}+2)^{1/(2m)}}{\sqrt6}\sqrt{t-\frac13}.
\]

In particular, the sharp sixth-moment inequality is
\[
\operatorname{Tr}\bigl((\rho-\Delta\rho)^6\bigr)
\le\frac{11}{36}\left(t-\frac13\right)^3.
\]
For \(t>1/3\), put \(s=\sqrt{(3t-1)/2}\). **All** matrices attaining either bound, for any \(m\ge3\), have the form
\[
\rho=\frac{I_3}{3}+\varepsilon s\left(ww^*-\frac{I_3}{3}\right),\qquad
|w_1|=|w_2|=|w_3|=\frac1{\sqrt3},
\]
where \(\varepsilon=+1\) is admissible for all \(t\), while \(\varepsilon=-1\) is admissible exactly when \(t\le1/2\). At \(t=1/3\), the unique density matrix is \(I_3/3\).

The maximizers of the **entrywise** \(\ell_1\) off-diagonal quantity, by contrast, form a larger phase family. Its exact maximum is \(2s\). For \(s>0\), every maximizer has diagonal \(1/3\) and all three off-diagonal moduli equal to \(s/3\). Set \(\theta=\arg(\rho_{12}\rho_{23}\rho_{31})\). Such a matrix is positive semidefinite **if and only if**
\[
1-3s^2+2s^3\cos\theta\ge0.
\]
Thus every phase is permitted for \(0<s\le1/2\), whereas the even-Schatten norm chooses only \(\theta=0\) and, below the sharp purity threshold \(t=1/2\), \(\theta=\pi\). The phase product is invariant under diagonal-unitary changes of basis; the two signs are genuinely inequivalent.

## Assumptions and scope
Matrices are complex Hermitian \(3\times3\) positive semidefinite matrices of trace one; purity means \(\operatorname{Tr}(\rho^2)\). The dephasing map \(\Delta\) is in a **fixed** basis. The Schatten norm is \(\|A\|_{S_p}=(\operatorname{Tr}|A|^p)^{1/p}\). The off-diagonal Schatten quantity is a matrix norm, **not asserted to be a coherence monotone**. The main strict phase-selection assertion requires integers \(m\ge3\); it deliberately does not assert the same equality classification for the quartic moment.

## Proof
**Step 1: purity budget.** Set \(u=\operatorname{Tr}B^2=2\sum_{i<j}|\rho_{ij}|^2\). Orthogonality of diagonal and off-diagonal matrices in Hilbert–Schmidt inner product gives
\[
t=\sum_{i=1}^3\rho_{ii}^2+u\ge\frac13+u.
\]
Equality holds exactly when all diagonal entries equal \(1/3\). Let \(v=\operatorname{Tr}B^3=6\operatorname{Re}(\rho_{12}\rho_{23}\rho_{31})\). The arithmetic–geometric mean inequality on the three squared edge moduli yields
\[
|v|\le6\bigl(u/6\bigr)^{3/2}=\frac{u^{3/2}}{\sqrt6}.
\]
When \(u>0\), equality holds exactly when the three off-diagonal moduli agree and the gauge-invariant triangle product is real, i.e. \(\cos\theta=\pm1\).

**Step 2: all even spectral moments.** The traceless Hermitian matrix \(B\) obeys
\[
B^3-\frac u2 B-\frac v3 I_3=0.
\]
For \(h_k=\operatorname{Tr}B^k\), the initial conditions are \(h_0=3\), \(h_1=0\), \(h_2=u\), and the exact recurrence is
\[
h_k=\frac u2h_{k-2}+\frac v3h_{k-3}\quad(k\ge3).
\]
By induction each \(h_k\) is a polynomial with nonnegative rational coefficients in monomials \(u^av^b\) satisfying \(2a+3b=k\). For even \(k=2m\), every \(b\) is even, so \(h_{2m}\) is nondecreasing in \(v^2\) at fixed \(u\ge0\); for \(m\ge3\) this dependence is strictly increasing if \(u>0\), since \(h_6=u^3/4+v^2/3\) and later even recurrences inherit a positive coefficient of \(v^2\). Consequently \(h_{2m}\) is maximal at \(|v|=u^{3/2}/\sqrt6\), where the spectrum of \(B\) is \(\{2a,-a,-a\}\) or \(\{-2a,a,a\}\) with \(a=\sqrt{u/6}\). Therefore
\[
\operatorname{Tr}B^{2m}\le (2^{2m}+2)(u/6)^m\le(2^{2m}+2)((t-1/3)/6)^m.
\]
Taking roots proves the upper bound, and \(m=3\) reduces to \(11(t-1/3)^3/36\). This is an analytic inequality for **all** matrices in the stated domain, not a conclusion from finite testing.

**Step 3: attainable bounds and all equality cases.** For \(t>1/3\), equality in both inequalities requires diagonal entries \(1/3\), three equal off-diagonal moduli \(s/3\), and \(\cos\theta=\pm1\). Diagonal-unitary conjugation converts these precisely to the stated \(\varepsilon=+1\) and \(\varepsilon=-1\) forms. Their eigenvalues are respectively \(((1+2s)/3,(1-s)/3,(1-s)/3)\) and \(((1-2s)/3,(1+s)/3,(1+s)/3)\). The first is positive for \(0\le s\le1\); the second only for \(0\le s\le1/2\), equivalent to \(t\le1/2\). Both have purity \(1/3+2s^2/3=t\) and attain the bound. At minimal purity, Cauchy–Schwarz forces \(\rho=I_3/3\).

**Step 4: the full entrywise \(\ell_1\) phase family.** Cauchy–Schwarz on the six off-diagonal entries gives \(\sum_{i\ne j}|\rho_{ij}|\le\sqrt{6u}\le\sqrt{6(t-1/3)}=2s\). Equality requires uniform diagonal and equal off-diagonal moduli \(a=s/3\). Conversely these conditions give the stated \(\ell_1\) value. Every such Hermitian matrix has positive one-by-one and two-by-two principal minors for \(0<s\le1\); its determinant is
\[
\det\rho=\frac{1-3s^2+2s^3\cos\theta}{27}.
\]
Thus the determinant inequality is exactly its remaining positivity condition. If \(s\le1/2\), the determinant is nonnegative for all \(\theta\); if \(s>1/2\), \(\theta=\pi\) is excluded. Finally \(\rho_{12}\rho_{23}\rho_{31}\) is unchanged under diagonal-unitary conjugation, so \(\theta=0\) and \(\theta=\pi\) cannot be equivalent.

## Verification
The accompanying `verify.py` uses exact rational polynomial recurrences up to power 32, checks \(3500\) reproducibly sampled positive density matrices for moment and purity bounds, checks \(4355\) phase-parameter pairs against positivity and purity, and tests both analytic equality branches at several values of \(s\). Replay with `python verify.py` using Python 3.10+ and NumPy. Expected output: `VERIFY_OK checks=41205 exact_trace_recursion=60 random_density_matrices=3500 phase_grid=4355`. These finite calculations supplement, but cannot replace, Steps 1–4.

## Relationship to prior work
Singh, Bera, Dhar and Pati (2015) prove the sharp purity/entrywise-\(\ell_1\) coherence trade-off and exhibit the positive-sign pseudo-pure family. Their Theorem 2's uniqueness wording is stronger than that exhibited family: the phase-holonomy description here supplies additional maximizing states; in particular the negative-sign branch for \(1/3<t\le1/2\) is not diagonal-unitarily equivalent to its positive-sign counterpart. The already-known maximum \(2s\) is **not presented as a new numerical bound**.

Rana, Parashar and Lewenstein (2015 preprint, 2016 publication) discuss Schatten-\(p\) coherence quantities minimized over incoherent states and show failures of monotonicity. The quantity here is instead the direct norm of the off-diagonal matrix; it is not silently identified with that minimized quantity. Yao and collaborators (2016) analyze Frobenius/purity-based norms, not the sharp higher even spectral moments and their phase-restricted equality conditions. Streltsov and collaborators (first preprint 2016-12, later literature) give strong maximal-coherence results for different fixed-spectrum/minimized-distance functionals; those do not directly state this fixed-purity, dephased-matrix theorem. An older matrix-analysis equivalent under different terminology has not been excluded by a complete historical bibliography.

## Limitations
The result concerns only three-level density matrices, their off-diagonal part in a fixed basis, and even integer exponents at least six. It does not classify optimizers for general noninteger Schatten exponents or matrices in higher dimensions. The quartic moment has the separate traceless-three-dimensional identity \(\operatorname{Tr}B^4=u^2/2\), which explains why the strict phase selection starts at order six. The connection to quantum coherence is quantitative, not a claim that Schatten-\(p\) off-diagonal norms are resource monotones.

## References
1. U. Singh, M. N. Bera, H. S. Dhar, and A. K. Pati, *Maximally coherent mixed states: Complementarity between maximal coherence and mixedness*, arXiv:1503.06303 (first submitted 2015-03-21), especially Theorems 1 and 2 and Eq. (9). https://arxiv.org/abs/1503.06303
2. S. Rana, P. Parashar, and M. Lewenstein, *Trace-distance measure of coherence*, arXiv:1511.01854 (first submitted 2015-11-05); Phys. Rev. A 93, 012110 (2016), especially the Schatten-norm discussion. https://arxiv.org/abs/1511.01854
3. Y. Yao and coauthors, *Frobenius-norm-based measures of quantum coherence and asymmetry*, Scientific Reports 6, 32010 (2016). https://www.nature.com/articles/srep32010
4. A. Streltsov and coauthors, *Maximal Coherence and the Resource Theory of Purity*, arXiv:1612.07570 (first submitted 2016-12-22), Theorem 2 and Appendix A; later contextual comparison, not the initiating source. https://arxiv.org/abs/1612.07570
