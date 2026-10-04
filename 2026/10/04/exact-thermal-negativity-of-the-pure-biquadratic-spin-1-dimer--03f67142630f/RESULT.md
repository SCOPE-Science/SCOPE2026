# Exact thermal negativity of the pure-biquadratic spin-1 dimer

## Finding

For two spin-\(1\) particles consider
\[
H=K(\mathbf S_1\!\cdot\!\mathbf S_2)^2+B(S_{1z}+S_{2z}),\qquad K<0.
\]
At positive temperature \(T\), define
\[
r=e^{-3K/T}=e^{3|K|/T},\qquad b=\frac BT,\qquad a=\frac{r-1}{3},
\]
and
\[
Z'=(1+2\cosh b)^2+r-1.
\]
Then the thermal negativity is
\[
\boxed{\mathcal N=
\frac{
2\left(\sqrt{\sinh^2b+a^2}-\cosh b\right)
+\left(\sqrt{\sinh^2(2b)+a^2}-\cosh(2b)\right)
}{Z'}}
\]
when \(r>4\), and
\[
\boxed{\mathcal N=0}
\]
when \(r\le4\).

Consequently
\[
\boxed{T_c=\frac{3|K|}{\log4}}
\]
is the exact positive-temperature negativity threshold and is independent of every finite uniform magnetic field. Moreover,
\[
0<T<T_c\quad\Longrightarrow\quad \mathcal N(T,B)>0
\]
for every finite \(B\). Thus there is no finite positive-temperature critical magnetic field for this Hamiltonian.

At exactly zero temperature the ground-state crossing is instead
\[
\boxed{|B|=\frac{3|K|}{2}}.
\]
Below it the ground state is the maximally entangled spin singlet, with qutrit negativity \(1\); above it the ground state is fully polarized and separable.

For the source value \(K=-3\),
\[
T_c=\frac9{\log4}=6.492127684000335\ldots,
\]
while the zero-temperature field crossing is \(|B|=4.5\).

## Assumptions and scope

The claim concerns exactly the reduced Hamiltonian displayed above with standard spin-\(1\) matrices, \(K<0\), a uniform \(z\)-directed field, and \(k_B=1\).

The threshold is a threshold for negativity, equivalently for non-positive partial transpose in this family. The statement does not claim that every PPT two-qutrit state above threshold is separable, since PPT is not sufficient for separability in general dimension \(3\times3\).

The strict nonvanishing statement concerns positive temperature. The \(T=0\) level crossing is explicitly separate.

## Proof

For two spin-\(1\) particles,
\[
\mathbf S_1\!\cdot\!\mathbf S_2
=\frac12\left(\mathbf S_{\mathrm{tot}}^2-4\right).
\]
Hence it has eigenvalue \(-2\) on total spin \(S=0\), and eigenvalues \(-1\) and \(1\) on total spin \(S=1\) and \(S=2\). Therefore
\[
(\mathbf S_1\!\cdot\!\mathbf S_2)^2=I+3P_0,
\]
where \(P_0\) projects onto the spin singlet.

Since the singlet has total magnetic quantum number \(0\),
\[
H=KI+3KP_0+BM,\qquad M=S_{1z}+S_{2z}.
\]
Thus the singlet energy is \(4K\), and the orthogonal complement has energies \(K+BM\). The multiplicities at \(M=-2,-1,0,1,2\) are \(1,2,2,2,1\).

Because \(P_0\) commutes with \(M\),
\[
e^{-H/T}=e^{-K/T}\left[e^{-bM}+(r-1)P_0\right].
\]
The common factor cancels on normalization, and
\[
Z'=\operatorname{tr}(e^{-bM})+r-1=(1+2\cosh b)^2+r-1.
\]

Up to local phases,
\[
|\psi_0\rangle=\frac{|1,-1\rangle-|0,0\rangle+|-1,1\rangle}{\sqrt3}.
\]
After partial transpose, the only blocks that can become negative are two copies of
\[
\begin{pmatrix}e^b&\pm a\\ \pm a&e^{-b}\end{pmatrix}
\]
and one copy of
\[
\begin{pmatrix}e^{2b}&\pm a\\ \pm a&e^{-2b}\end{pmatrix},
\qquad a=\frac{r-1}{3}.
\]
Every block has determinant
\[
1-a^2.
\]
Hence the partial transpose is positive exactly when \(a\le1\), equivalently \(r\le4\). When \(r>4\), each of the three blocks has one negative eigenvalue.

For a block with exponent \(d\in\{1,2\}\), the magnitude of the negative eigenvalue is
\[
\frac{\sqrt{\sinh^2(db)+a^2}-\cosh(db)}{Z'}.
\]
There are two \(d=1\) blocks and one \(d=2\) block, which gives the displayed formula.

The condition \(r=4\) yields
\[
T_c=\frac{3|K|}{\log4}.
\]
If \(r>4\), then \(a>1\), so for every finite \(b\),
\[
\sqrt{\sinh^2(db)+a^2}>\sqrt{\sinh^2(db)+1}=\cosh(db).
\]
Thus the negativity is strictly positive for every finite field.

At \(T=0\), for \(B>0\), the singlet energy \(4K\) crosses the polarized energy \(K-2B\) at \(B=3|K|/2\); the case \(B<0\) is symmetric.

## Verification

`verify_biquadratic_qutrit.py` reconstructs the \(9\times9\) Hamiltonian from the standard spin-\(1\) matrices. It verifies the full spectrum, exponentiates the Hamiltonian by diagonalization, partially transposes the Gibbs state, and compares the direct negativity with the closed formula on deterministic parameter grids.

The script also checks the threshold immediately above and below \(T_c\), the zero-field identity
\[
\mathcal N=\frac{r-4}{r+8}
\]
for \(r>4\), and positive negativity at large finite fields below threshold.

The finite replay supplements rather than replaces the analytic proof.

## Relationship to prior work

Zhang and Li write the same reduced Hamiltonian but print eigenvalues containing \(K/4\) and \((2\pm\sqrt3)K/2\). Those values cannot be eigenvalues of \(K(\mathbf S_1\!\cdot\!\mathbf S_2)^2\), whose total-spin eigenvalues are only \(K\) and \(4K\) before Zeeman splitting. Their figures consequently report a finite critical magnetic field at positive temperature and a zero-field ground-state negativity near \(0.972\).

The corrected Hamiltonian instead has a maximally entangled singlet ground state at zero field, with negativity \(1\), and no finite positive-temperature critical field below \(T_c\).

Zhou, Yi, Song, and Guo study spin-\(1\) optical-lattice chains with bilinear and biquadratic couplings, including the two-particle problem but without the uniform-field correction claimed here.

Sargolzahi, Mirafzali, and Sarbishaei later analyze the more general bilinear-biquadratic Hamiltonian with nonuniform fields. Their manuscript explicitly identifies the uniform-field nonlinear case as earlier work and then studies a different nonuniform regime. The inspected text does not state the closed pure-biquadratic uniform-field negativity formula, the exact \(3|K|/\log4\) threshold, or the absence of a finite positive-temperature critical field.

Targeted searches for the source title, DOI, its printed eigenvalues, the exact threshold, and a correction or erratum did not locate a published statement of these conclusions together.

## Limitations

Negativity zero implies PPT, not general two-qutrit separability.

The finding is specific to the source's reduced \(|K|\gg|J|\) Hamiltonian with the bilinear term omitted. It does not classify the full \(J\ne0\) bilinear-biquadratic dimer.

At fields beyond the zero-temperature crossing, the limits \(T\downarrow0\) and fixed positive \(T\) differ: the ground state is separable, yet for every positive \(T<T_c\) a finite field leaves an exponentially small but nonzero NPT contribution.

The full text of one earlier optical-lattice paper was not reliably available during the comparison, leaving a residual possibility that an equivalent zero-field specialization appears there.

## References

1. G.-F. Zhang and S.-S. Li, “The effects of nonlinear couplings and external magnetic field on the thermal entanglement in a two-spin-qutrit system,” arXiv:quant-ph/0510129, first public 17 October 2005; *Optics Communications* 260 (2006), 347–350, DOI: 10.1016/j.optcom.2005.10.039.
2. L. Zhou, X.-X. Yi, H.-S. Song, and Y.-Q. Guo, “Thermal entanglement in 1D optical lattice chains with nonlinear coupling,” *Chinese Physics* 14 (2005), 1168–1173, DOI: 10.1088/1009-1963/14/6/019.
3. I. Sargolzahi, S. Y. Mirafzali, and M. Sarbishaei, “Thermal entanglement in a two-qutrit system with nonlinear coupling under nonuniform external magnetic field,” arXiv:0705.3568, first public 24 May 2007; *International Journal of Quantum Information* 6 (2008), 867–884, DOI: 10.1142/S0219749908004158.
