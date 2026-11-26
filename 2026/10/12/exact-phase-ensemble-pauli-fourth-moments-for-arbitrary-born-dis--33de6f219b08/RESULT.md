# Exact phase-ensemble Pauli fourth moments for arbitrary Born distributions

## Finding
Fix an integer \(n\ge1\), set \(N=2^n\), and let \(p=(p_x)_{x\in\mathbb F_2^n}\) be a Born probability distribution. Let \(\psi_x=\sqrt{p_x}e^{i\theta_x}\), where the phases are independent and uniform on \([0,2\pi)\). Define
\[
C(a)=\sum_xp_xp_{x\oplus a},\qquad
K(\psi)=\frac1N\sum_{P\in\{I,X,Y,Z\}^{\otimes n}}\langle\psi|P|\psi\rangle^4=2^{-M_2(\psi)}.
\]
Then
\[
\boxed{\mathbb E_\theta K(\psi)=4\sum_{a\ne0}C(a)^2-2C(0)^2+3\sum_x p_x^4.}
\]
For \(p_x=1/N\) this yields
\[
\mathbb E K=\frac{4N^2-6N+3}{N^3},\qquad
\mathbb E M_2\ge -\log_2\mathbb E K\ge n-2,\qquad
\Pr\{M_2\le n-2-t\}\le 2^{-t}\quad(t\ge0).
\]
For this flat Born distribution, the zero-phase member is the stabilizer state \(|+\rangle^{\otimes n}\) and has \(M_2=0\).

## Assumptions and scope
The distribution obeys \(p_x\ge0\) and \(\sum_xp_x=1\), including distributions with zeros. XOR indexes translations of \(\mathbb F_2^n\). The Pauli sum is over unsigned Hermitian tensor strings, with one representative for each pair of binary Pauli masks. The phase ensemble is on individual basis amplitudes, with no assumption of locality, efficient preparation, or Haar-distributed amplitudes.

## Proof
For \(a,b\in\mathbb F_2^n\) put
\[
c_a(x)=\overline{\psi_x}\psi_{x\oplus a},\qquad
W_a(b)=\sum_x(-1)^{b\cdot x}c_a(x),\qquad
K_a=N^{-1}\sum_b|W_a(b)|^4.
\]
The absolute value of the expectation of the corresponding Hermitian Pauli equals \(|W_a(b)|\): shifting the summation index and using the Pauli phase can only multiply it by a unit-modulus factor. The expectation of a Hermitian Pauli is real, so \(K=\sum_a K_a\). At \(a=0\) the Walsh transform is that of \(p\); expanding its fourth power and using character orthogonality gives
\[
K_0=\sum_{u\in\mathbb F_2^n}\left(\sum_xp_xp_{x\oplus u}\right)^2=\sum_u C(u)^2.
\]

Fix \(a\ne0\). Choose one endpoint \(x_O\) in each orbit \(O=\{x_O,x_O\oplus a\}\), and put
\[
q_O=p_{x_O}p_{x_O\oplus a},\qquad \phi_O=\theta_{x_O\oplus a}-\theta_{x_O}\pmod {2\pi}.
\]
The \(\phi_O\) are independent and uniform because the orbits are disjoint. The pair's contribution to \(W_a(b)\) is
\[
(-1)^{b\cdot x_O}\sqrt{q_O}\big(e^{i\phi_O}+(-1)^{b\cdot a}e^{-i\phi_O}\big).
\]
Thus for a fixed \(b\), up to a common factor \(i\) when \(b\cdot a=1\), \(W_a(b)\) is a sum of independent real mean-zero variables, the pair variables being \(2(-1)^{b\cdot x_O}\sqrt{q_O}\cos\phi_O\) or \(2(-1)^{b\cdot x_O}\sqrt{q_O}\sin\phi_O\). In either case their second moments are \(2q_O\), and their fourth moments are \(6q_O^2\). Expanding the fourth power of this real sum, terms with a variable occurring only once vanish. The contribution of two distinct variables each used twice is six times the product of their second moments. It follows that, for every \(b\),
\[
\mathbb E |W_a(b)|^4=6\sum_O q_O^2+24\sum_{O<O'}q_Oq_{O'}.
\]
The summation order is arbitrary. Writing \(D(a)=\sum_xp_x^2p_{x\oplus a}^2\), we have \(C(a)=2\sum_Oq_O\) and \(D(a)=2\sum_Oq_O^2\). Hence \(\mathbb E K_a=3C(a)^2-3D(a)\). As \(\sum_{a\ne0}D(a)=C(0)^2-\sum_xp_x^4\), adding \(K_0\) proves the formula, with no nonzero-amplitude restriction.

For flat \(p\), \(C(a)=1/N\) for every \(a\), so \(\mathbb E K=(4N^2-6N+3)/N^3\le4/N\). Jensen's inequality for \(-\log_2\) yields the entropy bound. The identity Pauli ensures \(K>0\). Markov's inequality at \(K\ge 2^{-(n-2-t)}\) gives \(\Pr\{M_2\le n-2-t\}\le2^{-t}\).

## Verification
The accompanying standard-library script `verify_magic_phase.py` computes the full fourth Pauli moment over every fifth-root phase configuration for six two- or four-amplitude distributions, including zeros. The fifth-root grid integrates each phase monomial exactly in theory because each nonzero exponent has magnitude at most four; the implementation uses floating-point complex arithmetic. The script then checks the pair-moment expression and the closed form on 450 reproducible random probability vectors and verifies the flat specialization at eight sizes. These finite checks are supplementary; the proof above establishes the universal statement.

## Relationship to prior work
Płodzień [1, §III and Appendices A–B] considers the same fixed-Born phase orbit, uses the Walsh decomposition to minimize \(M_2\) over phases, and includes numerical phase draws. Liu and Xu [2, Lemma 2, Eqs. (13)–(14)] give a general pointwise expression for \(K\) as an amplitude-weighted parallelogram energy; their arbitrary state covers this setting by taking the full binary cube or the given support. Neither identity is claimed as new here. The contribution is the evaluation of the independent-phase average as a simple autocorrelation polynomial. In particular, a pointwise expression still requires averaging over phase differences and accounting separately for coincident and distinct endpoints. The expected-entropy and low-entropy tail bounds are immediate consequences of the evaluated mean, not separate concentration methods.

Chen, Yan and Zhou [3, Theorem 5] obtain an exact averaged Pauli moment in a flat-amplitude hypergraph ensemble with Boolean phases from randomly retained edges. That phase law is not independent continuous phases on individual amplitudes. Piemontese, Roscilde and Hamma [4, §III] discuss flat-amplitude random-sign magic, another different phase law. The \(n-2\) entropy scale also appears for typical Haar states [5]; Haar states do not fix the Born distribution. The stabilizer Rényi entropy used here was introduced in [6].

## Limitations
The exact identity is for \(\mathbb E(2^{-M_2})\), not \(2^{-\mathbb E M_2}\); Jensen gives a lower bound, not an exact value of the expected entropy. The Markov estimate controls only the low-entropy tail. Neither a circuit of bounded depth nor a replacement of the continuous phases by arbitrary random signs is covered. The literature comparisons are targeted and do not exclude unindexed equivalent calculations.

## References
1. M. Płodzień, *Nonstabilizerness of the entangling layer in quantum circuit Born machines*, arXiv:2609.32025v1, https://arxiv.org/html/2609.32025v1.
2. Y. Liu and K.-M. Xu, *Quantifying Nonstabilizerness of Codeword-Stabilized Codes*, arXiv:2608.22017v1, https://arxiv.org/pdf/2608.22017v1.
3. Chen, Yan and Zhou, *Magic of quantum hypergraph states*, arXiv:2308.01886v2, https://arxiv.org/abs/2308.01886v2.
4. Piemontese, Roscilde and Hamma, arXiv:2211.01428, https://arxiv.org/abs/2211.01428.
5. X. Turkeshi, A. Dymarsky and P. Sierant, *Pauli Spectrum and Non-stabilizerness of Typical Quantum Many-Body States*, Phys. Rev. B 111, 054301 (2025), arXiv:2312.11631v2, https://arxiv.org/html/2312.11631v2.
6. L. Leone, S. F. E. Oliviero and A. Hamma, *Stabilizer Rényi Entropy*, Phys. Rev. Lett. 128, 050402 (2022), DOI:10.1103/PhysRevLett.128.050402.
