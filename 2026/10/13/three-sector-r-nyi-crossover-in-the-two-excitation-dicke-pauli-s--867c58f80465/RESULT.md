# Three-sector Rényi crossover in the two-excitation Dicke Pauli spectrum

## Finding

For every integer \(n\geq4\), let \(N=\binom n2\) and define the normalized two-excitation symmetric Dicke state
\[
|D_n^{(2)}\rangle=N^{-1/2}\sum_{|x|=2}|x\rangle.
\]
The complete magnitude of every phase-free Hermitian Pauli expectation \(q(P)=|\langle D_n^{(2)}|P|D_n^{(2)}\rangle|\), for \(P\in\{I,X,Y,Z\}^{\otimes n}\), depends only on \(r=\#\{X,Y\}\), \(b=\#Y\), and \(c=\#Z\). It is exactly
\[
q(P)=\begin{cases}
\left|\dfrac{(n-2c)^2-n}{n(n-1)}\right|,&r=0,\\[3pt]
\left|\dfrac{2(n-2-2c)}{N}\right|,&r=2,\ b\in\{0,2\},\\[3pt]
\dfrac6N,&r=4,\ b\in\{0,4\},\\[3pt]
\dfrac2N,&r=4,\ b=2,\\[3pt]
0,&\text{otherwise}.
\end{cases}
\]
These labelled values determine the full Pauli-magnitude distribution including accidental zeros. With the pure-state stabilizer moment and Rényi entropy normalized as
\[
T_\alpha(n)=2^{-n}\sum_P q(P)^{2\alpha},\qquad
M_\alpha(n)=\frac{\log_2 T_\alpha(n)}{1-\alpha},\qquad \alpha>1,
\]
put \(U_c=((n-2c)^2-n)/(n(n-1))\) and \(V_c=2(n-2-2c)/N\). For all real \(\alpha>1\),
\[
\begin{aligned}
T_\alpha(n)=2^{-n}\bigg[&\sum_{c=0}^n\binom nc |U_c|^{2\alpha}
+2N\sum_{c=0}^{n-2}\binom{n-2}c|V_c|^{2\alpha}\\
&+\binom n4 2^{n-4}\left(2(6/N)^{2\alpha}+6(2/N)^{2\alpha}\right)\bigg].
\end{aligned}
\]
In particular, the order-two moment has the exact closed form
\[
\boxed{T_2(n)=\frac{4(91n^2-427n+492)}{n^3(n-1)^3}.}
\]
The moment exhibits a sharp Rényi-index crossover. If \(1<\alpha<2\), then
\[
\boxed{\lim_{n\to\infty}n^{4\alpha-4}T_\alpha(n)
=B_\alpha:=\frac{2\cdot12^{2\alpha}+6\cdot4^{2\alpha}}{384}.}
\]
If \(\alpha>2\), then
\[
\boxed{\lim_{n\to\infty}n^{2\alpha}T_\alpha(n)
=A_\alpha:=\mathbb E\,|G^2-1|^{2\alpha},\quad G\sim\mathcal N(0,1).}
\]
Exactly at the crossover, \(\lim_{n\to\infty}n^4T_2(n)=364\). More sharply, for every fixed real \(s\) and \(\alpha_n=2+s/\log n\),
\[
\boxed{\lim_{n\to\infty}n^4T_{\alpha_n}(n)
=60e^{-2s}+192e^{-3s}+112e^{-4s}.}
\]
Thus three distinct Pauli-flip sectors coexist in a critical window of width \(1/\log n\). Equivalently,
\[
\lim_{n\to\infty}\frac{M_\alpha(n)}{\log_2n}
=\begin{cases}4,&1<\alpha\le2,\\2\alpha/(\alpha-1),&\alpha>2.\end{cases}
\]

## Assumptions and scope

The qubits are distinguishable, their computational basis is fixed, and the Dicke state is the equal positive-amplitude pure state in the exactly-two-excitation sector. The phase-free Pauli basis has \(4^n\) strings, each counted once; global Pauli phases are not counted. All powers at vanishing expectations use \(0^{2\alpha}=0\). The asymptotic formulas hold for fixed \(\alpha>1\), or for the specified logarithmic window \(s\in\mathbb R\) fixed as \(n\to\infty\). The entropy convention is for pure states and matches the normalized squared Pauli expectation distribution.

## Proof

**1. Complete Pauli magnitudes.** A Pauli string with \(r\) letters from \(\{X,Y\}\) flips precisely \(r\) bits of each computational state. A weight-two binary string can be carried to another weight-two string only when exactly half the flipped bits were occupied, forcing \(r=0,2,4\). Real amplitudes and Hermitian Paulis make expectations with odd \(b\) vanish: complex conjugation changes their sign. For \(r=0\), count the weight-two strings having \(j\) occupied sites inside the \(c\) Z positions. Their signed average is
\[
N^{-1}\sum_{j=0}^2(-1)^j\binom cj\binom{n-c}{2-j}
=\frac{(n-2c)^2-n}{n(n-1)}.
\]
For \(r=2\) and even \(b\), exactly one flip site is occupied and the other occupied site lies outside the flipped pair. Each exterior site contributes twice, with sign determined by whether it bears Z, giving signed magnitude \(|2(n-2-2c)/N|\). For \(r=4\), both occupied sites lie among the four flips. Summing the six choices gives magnitude \(6/N\) for zero or four Y sites, and \(2/N\) for two Y sites. This covers all Pauli strings.

**2. Exact moment formula.** With zero flips there is one I/Z string for each choice of the \(c\) Z positions, giving \(\binom nc\) multiplicity. With two flips there are \(N\) choices of sites and two even-Y patterns, while the \(n-2\) other positions have independently I or Z; the multiplicity at each \(c\) is \(2N\binom{n-2}c\). With four flips there are \(\binom n4\) position sets and \(2^{n-4}\) exterior I/Z patterns, with two even-Y patterns of magnitude \(6/N\) and six of magnitude \(2/N\). Summing their \(2\alpha\)-powers and multiplying by \(2^{-n}\) proves the displayed moment identity.

**3. Exact order-two moment.** The respective zero-, two-, and four-flip contributions at \(\alpha=2\) reduce by the even binomial moments to
\[
\begin{aligned}
T_2^{(0)}(n)&=\frac{4(15n^2-63n+68)}{n^3(n-1)^3},\\
T_2^{(2)}(n)&=\frac{64(n-2)(3n-8)}{n^3(n-1)^3},\\
T_2^{(4)}(n)&=\frac{112(n-3)(n-2)}{n^3(n-1)^3}.
\end{aligned}
\]
For example, with independent symmetric unit Rademacher signs and their normalized sum \(S_n\), their fourth, sixth and eighth moments are \(3-2/n\), \(15-30/n+16/n^2\), and \(105-420/n+588/n^2-272/n^3\); these directly evaluate the zero-flip term. The four-flip term is an elementary binomial count, and the two-flip term uses the fourth moment. Summing the three rational expressions proves the closed form.

**4. Universal asymptotics.** Let \(C_m\sim\operatorname{Bin}(m,1/2)\) and \(S_m=(m-2C_m)/\sqrt m\). The central limit theorem yields \(S_m\Rightarrow G\), while the elementary Rademacher moment-generating-function bound \(\mathbb E e^{tS_m}\le e^{t^2/2}\) implies convergence of \(\mathbb E|S_m|^p\) and \(\mathbb E|S_m^2-1|^p\) for every fixed \(p>0\), uniformly for \(p\) in compact intervals. Here \(U_{C_n}=(S_n^2-1)/(n-1)\) and \(V_{C_{n-2}}=(2\sqrt{n-2}/N)S_{n-2}\). Hence for \(p=2\alpha\), the three sector contributions satisfy
\[
\begin{aligned}
T_{p/2}^{(0)}(n)&\sim n^{-p}\,\mathbb E|G^2-1|^p,\\
T_{p/2}^{(2)}(n)&\sim n^{2-3p/2}\,4^{p-1}\mathbb E|G|^p,\\
T_{p/2}^{(4)}(n)&\sim n^{4-2p}\,\frac{2\cdot12^p+6\cdot4^p}{384}.
\end{aligned}
\]
At \(p=4\), all three powers coincide, with coefficients \(60\), \(192\), and \(112\): indeed \(\mathbb E(G^2-1)^4=60\) and \(4^3\mathbb EG^4=192\). For \(p<4\) the four-flip sector dominates; for \(p>4\) the zero-flip sector dominates. Setting \(p_n=4+2s/\log n\) in the same uniform-in-\(p\) asymptotics and multiplying by \(n^4\) gives \(e^{-2s},e^{-3s},e^{-4s}\), respectively, completing the crossover law. Taking logarithms gives the entropy exponent.

## Verification

Run \(\texttt{python3 verify.py}\) with Python's standard library. It computes Pauli actions directly on all two-excitation basis strings for \(4\le n\le8\), compares the complete per-string magnitude spectrum with the theorem, and checks the finite exact moment identity and closed rational \(T_2(n)\) for \(4\le n\le30\) using integer arithmetic. A successful run prints \(\texttt{VERIFY_OK}\). Those finite computations cross-check the derivation, not its infinite-size conclusion; the latter follows from the analytic argument above.

## Relationship to prior work

Salazar, Saxena, Baker, Kwek and Kyaw (2026) motivate the full Pauli spectrum via a stabilizer partition function and obtain ensemble-level formulas for different state families; inspection of their manuscript's formalism, examples, and supplementary discussion found no two-excitation Dicke specialization or three-sector crossover. Turkeshi, Sierant and Tarabunga (2026) show a Rényi-index-two freezing threshold for random fermionic Gaussian states, not for a deterministic low-excitation symmetric Dicke state; equality of the critical indices does not imply equality of spectra or scaling coefficients. Miller et al. (2022/2023), especially their Appendix D, explicitly credit an earlier formula for Shor–Laflamme distributions of general Dicke states; those weight-resolved sums of **squared** Pauli expectations do not determine the present complete labelled expectation magnitudes or higher-order moments. Munizzi and Schnitzer (2023) characterize stabilizer groups and entanglement of Dicke states, not this all-order magic crossover. Exact enumeration here is new only insofar as this particular classification is not already implied by a stronger published full-spectrum formula; obscure equivalent formulas remain a residual risk.

## Limitations

The result applies only to the symmetric Dicke state with exactly two excitations; it neither gives the corresponding phase diagram for a number of excitations growing with system size nor provides experimental magic-distillation rates. The crossover is in the mathematical Rényi index, not a physical temperature transition, and its three finite-size sector coefficients rely on the stated Pauli normalization. No claim is made that numerical tests prove an infinite theorem, or that unsuccessful literature searches prove absolute novelty.

## References

1. W. E. Salazar, G. Saxena, J. S. Baker, L. C. Kwek, T. H. Kyaw, *Stabilizer Statistical Mechanics: A Framework for Efficient Quantification and Classification of Magic States*, arXiv:2608.14798v1 (first posted 2026-08-14).
2. X. Turkeshi, P. Sierant, P. S. Tarabunga, *Pauli spectrum and nonstabilizerness of random fermionic Gaussian states*, arXiv:2609.15739 (2026).
3. D. Miller et al., *Shor-Laflamme distributions of graph states and noise robustness of entanglement*, arXiv:2207.07665; J. Phys. A 56, 335303 (2023), doi:10.1088/1751-8121/ace8d4.
4. M. Munizzi and H. Schnitzer, *Entropy Cones and Entanglement Evolution for Dicke States*, arXiv:2306.13146 (2023).
5. L.-Y.-N. Liu, S. Yi, and J. Cui, *Stabilizer Rényi entropy for translation-invariant matrix product states*, Phys. Rev. A 113, 062414 (2026), doi:10.1103/7hzd-lv9k.
