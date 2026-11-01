# Arithmetic Hilbert–Schmidt resonance and a Gaussian column-energy law for atomic Hausdorff commutators

## Finding

Write \(H^2=H^2(\mathbb D)\) for the classical complex Hardy Hilbert space, with orthonormal basis \(e_k(z)=z^k\), \(k\geq0\). Fix distinct \(0<t_1,\ldots,t_m<1\), nonzero complex coefficients \(a_1,\ldots,a_m\), and a real frequency \(\tau\). Define the atomic Hausdorff operators and a bounded analytic multiplier by
\[
\phi_t(z)=\frac{tz}{1-(1-t)z},\qquad
H_t f(z)=\frac{f(\phi_t(z))}{1-(1-t)z},\qquad
H_\mu=\sum_{j=1}^m a_j H_{t_j},\qquad
h_\tau(z)=(1-z)^{i\tau}.
\]
Here the logarithm defining the last power is the principal analytic logarithm in the right half-plane \(\operatorname{Re}(1-z)>0\). Let \(D_{\mu,\tau}=[H_\mu,M_{h_\tau}]=H_\mu M_{h_\tau}-M_{h_\tau}H_\mu\). For integer \(K\geq1\), let \(P_K\) be the orthogonal projection onto polynomials of degree less than \(K\), and define the canonical column energy
\[
E_K(\mu,\tau)=\|D_{\mu,\tau}P_K\|_{\mathcal S_2}^2=\sum_{k=0}^{K-1}\|D_{\mu,\tau}z^k\|_{H^2}^2.
\]
Then, without any positivity assumption on the atomic coefficients,
\[
\boxed{\displaystyle
\lim_{K\to\infty}\frac{E_K(\mu,\tau)}{\sqrt K}
=\frac{\cosh(\pi\tau)}{\sqrt\pi}
\sum_{j=1}^m\frac{|a_j|^2\,|t_j^{-i\tau}-1|^2}{t_j\sqrt{1-t_j}}.}
\tag{1}
\]
Moreover,
\[
\boxed{\displaystyle D_{\mu,\tau}\in\mathcal S_2
\quad\Longleftrightarrow\quad
\tau\log(1/t_j)\in2\pi\mathbb Z\ \text{for every }j.}
\tag{2}
\]
If the equivalent conditions in (2) hold, the individual columns obey \(\|D_{\mu,\tau}z^k\|_{H^2}^2=O((k+1)^{-3/2})\). If they fail, (1) has a strictly positive coefficient, so \(E_K\) diverges at the exact rate \(\sqrt K\).

In particular, a nonzero resonant frequency exists if and only if all ratios \(\log(1/t_j)/\log(1/t_1)\) are rational. If these logarithms are incommensurable, only the constant multiplier \(h_0=1\) has a Hilbert–Schmidt commutator within this imaginary-power family. The formula is additive in the squared absolute atomic coefficients: distinct atoms cannot cancel the leading nonresonant energy even when the coefficients have arbitrary complex phases.

## Assumptions and scope

All operators act on the analytic Hardy space \(H^2(\mathbb D)\). The measure is *finite atomic* with distinct support points strictly inside \((0,1)\); repeated support points must be combined first, and zero coefficients discarded. The coefficients may be complex. The frequency is real and no integrality restriction is imposed. Formula (1) concerns the **specified degree cutoffs** \(P_K\); it is not asserted to be a singular-value counting law or a basis-independent spectral coefficient. Formula (2) is the genuine operator-ideal characterization. The source paper studying spectra of Hausdorff operators on BMOA and the Bloch space is used as motivation, not as a premise for these Hardy-space calculations.

For \(t\in(0,1)\), the matrix of \(H_t\) on the Hardy monomial basis has nonnegative entries
\[
(H_t)_{n,k}=\begin{cases}\binom nk t^k(1-t)^{n-k},&n\ge k,\\0,&n<k.\end{cases}
\]
Its row sums equal \(1\), and each column sum equals \(1/t\); Schur's test gives \(\|H_t\|_{H^2\to H^2}\leq t^{-1/2}\). Also \(e^{-\pi|\tau|/2}\le|h_\tau(z)|\le e^{\pi|\tau|/2}\) on the disk, so all multipliers and commutators in this statement are bounded.

## Proof

**1. Exact column representation.** Put \(q_j=1-t_j\). The elementary identity
\[
1-\phi_t(z)=\frac{1-z}{1-(1-t)z}
\]
implies
\[
H_t M_{h_\tau}-M_{h_\tau}H_t
=M_{h_\tau\circ\phi_t-h_\tau}H_t,
\qquad
h_\tau(\phi_t(z))-h_\tau(z)
=h_\tau(z)\big((1-(1-t)z)^{-i\tau}-1\big).
\]
For every integer \(k\ge0\),
\[
D_{\mu,\tau}z^k
=z^k h_\tau(z)\sum_{j=1}^m A_j(z)B_j(z)^k,
\]
where
\[
A_j(z)=\frac{a_j[(1-q_jz)^{-i\tau}-1]}{1-q_jz},
\qquad B_j(z)=\frac{t_j}{1-q_jz}.
\tag{3}
\]
There are no singularities on the closed disk in these two auxiliary functions. For \(z=e^{i\theta}\) and \(-\pi\le\theta\le\pi\), \(B_j(1)=1\) and
\[
|B_j(e^{i\theta})|^2
=\frac{t_j^2}{t_j^2+2q_j(1-\cos\theta)}.
\tag{4}
\]
In particular, for each \(j\) there exists \(c_j>0\) with \(|B_j(e^{i\theta})|\le e^{-c_j\theta^2}\) throughout this interval. Hardy boundary integration gives the **exact** expression
\[
\|D_{\mu,\tau}z^k\|_{H^2}^2
=\frac1{2\pi}\int_{-\pi}^{\pi}
W_\tau(\theta)
\left|\sum_{j=1}^m A_j(e^{i\theta})B_j(e^{i\theta})^k\right|^2d\theta,
\tag{5}
\]
where \(W_\tau(\theta)=|(1-e^{i\theta})^{i\tau}|^2=\exp[-2\tau\arg(1-e^{i\theta})]\) is a positive real weight defined almost everywhere.

**2. One-atom Gaussian limit.** Let \(s_j=t_j^{-i\tau}-1\). As \(\theta\to0\),
\[
A_j(e^{i\theta})=\frac{a_js_j}{t_j}+O(|\theta|),\qquad
\log B_j(e^{i\theta})
=i\frac{q_j}{t_j}\theta-\frac{q_j}{2t_j^2}\theta^2+O(|\theta|^3).
\tag{6}
\]
For nonzero real \(u\),
\[
\lim_{k\to\infty}|h_\tau(e^{iu/\sqrt k})|^2
=\begin{cases}e^{\pi\tau},&u>0,\\e^{-\pi\tau},&u<0.\end{cases}
\]
Using the change \(\theta=u/\sqrt k\), the Gaussian domination in (4), and dominated convergence yields
\[
\begin{aligned}
&\lim_{k\to\infty}\sqrt k\,\frac1{2\pi}
\int_{-\pi}^{\pi}|h_\tau(e^{i\theta})|^2|A_j(e^{i\theta})|^2|B_j(e^{i\theta})|^{2k}d\theta\\
&\quad=\frac{|a_js_j|^2}{2\pi t_j^2}
\left(e^{\pi\tau}\int_0^\infty e^{-q_ju^2/t_j^2}du
+e^{-\pi\tau}\int_{-\infty}^0e^{-q_ju^2/t_j^2}du\right)\\
&\quad=\frac{\cosh(\pi\tau)}{2\sqrt\pi}\,
\frac{|a_j|^2|s_j|^2}{t_j\sqrt{q_j}}.
\end{aligned}
\tag{7}
\]

**3. Distinct atoms have no leading cross energy.** For \(j\ne l\), the linear angular frequencies \(q_j/t_j\) and \(q_l/t_l\) in (6) are unequal because the \(t_j\)'s are distinct. After \(\theta=u/\sqrt k\), the cross integrand, multiplied by \(\sqrt k\), equals an \(L^1(\mathbb R)\)-convergent Gaussian amplitude (including the two one-sided boundary limits of \(|h_\tau|^2\)) multiplied by
\[
\exp\left(i\sqrt k\left(\frac{q_j}{t_j}-\frac{q_l}{t_l}\right)u\right).
\]
The \(L^1\) convergence follows by (4), (6), and domination by a fixed Gaussian after extending the rescaled amplitude by zero outside \(|u|\le\pi\sqrt k\). The Riemann–Lebesgue lemma makes the resulting oscillatory integral tend to zero. Thus the cross terms contribute \(o(k^{-1/2})\), irrespective of the complex phases of \(a_j\).

Combining (5)–(7) gives
\[
\|D_{\mu,\tau}z^k\|_{H^2}^2
=\frac{\cosh(\pi\tau)}{2\sqrt{\pi k}}
\sum_{j=1}^m\frac{|a_j|^2|s_j|^2}{t_j\sqrt{1-t_j}}
+o(k^{-1/2})
\qquad(k\to\infty).
\tag{8}
\]
Since \(\sum_{k=1}^{K-1}k^{-1/2}\sim2\sqrt K\), the stated limit (1) follows.

**4. Exact Hilbert–Schmidt criterion and arithmetic consequence.** If some \(s_j\ne0\), the coefficient in (8) is strictly positive, so \(\sum_k\|D_{\mu,\tau}z^k\|^2=\infty\). Conversely, if all \(s_j=0\), then \(A_j(1)=0\); analyticity near the closed disk gives \(|A_j(e^{i\theta})|\le C_j|\theta|\). From (4), (5) and boundedness of \(h_\tau\),
\[
\|D_{\mu,\tau}z^k\|_{H^2}^2
\le C\int_{-\pi}^\pi\theta^2e^{-2ck\theta^2}\,d\theta
\le C'(k+1)^{-3/2}.
\]
The series converges, proving (2). Finally \(s_j=e^{i\tau\log(1/t_j)}-1\), so simultaneous vanishing is equivalent to the displayed arithmetic congruences. A nonzero common frequency exists exactly when the finitely many positive logarithms are commensurable. This completes the proof.

## Verification

The accompanying standalone `check.py` independently checks 1125 exact rational coefficient identities for the atomic Hausdorff matrices and their shift commutators. It also evaluates the *exact Hardy boundary integral* in (5) numerically for one-, two-, and three-atom examples at degrees 200, 600, 1500 and 4000, comparing the rescaled column energies with the independent closed-form coefficient in (8); the relative errors at degree 4000 are less than 2%. A separate finite summation confirms consistency with the elementary one-atom shift-commutator Hilbert–Schmidt norm. All assertions pass in the supplied environment. These checks are finite diagnostics; dominated convergence and the Riemann–Lebesgue lemma, not the experiments, prove the limits.

The rational coefficient checks do not establish the spectral asymptotic, and the numerical quadrature does not independently establish (2). The proof above supplies the infinite-dimensional argument. To reproduce the diagnostics, run `python check.py` with NumPy and SciPy installed.

## Relationship to prior work

Galanopoulos, Mahillo, Oliva-Maza and Siskakis (arXiv:2610.22554v1; first submitted 2026-10-15) study Hausdorff operators and determine spectra and Fredholm essential spectra on BMOA and the Bloch space. Their explicit Hausdorff matrix and weighted-composition representation motivate the present Hardy-space degree-cutoff question; the spectral formulas neither state nor imply its oscillatory Hilbert–Schmidt column-energy coefficient.

The earlier Hausdorff-matrix representation on Hardy spaces is classical (Galanopoulos–Siskakis–Papadimitrakis, 2001), and we do not claim that representation as new. Matache's Hardy-space Hilbert–Schmidt criterion for a *single* weighted composition operator is quoted by Lo–Loh (2020, §2); Lo–Loh §3 also studies differences of *two* weighted composition operators. These results make single-atom Hilbert–Schmidt membership an accessible special-case consequence. The specific contribution here is instead the **complete finite-atomic frequency criterion together with the nonresonant leading \(\sqrt K\) law and its additive, phase-insensitive coefficient**. The latter requires the asymptotic decoupling of distinct boundary scales proved in step 3; it is not a norm or spectral formula claimed by those sources.

Related prior investigations of oscillatory real-variable Cesàro commutators concern a different operator setting and phase-velocity mechanism. No equivalence or implication to the finite-atomic Hardy-space coefficient has been established.

## Limitations

The result applies only to finite atomic measures supported strictly between zero and one and to imaginary-power analytic multipliers. It does not claim a corresponding formula for continuous measures, arbitrary analytic symbols, general Schatten exponents, essential spectra, or singular-value sequences. The \(\sqrt K\) coefficient depends on the canonical monomial cutoff. Prior general weighted-composition Hilbert–Schmidt criteria already account for the single-atom membership test; that part alone is not asserted to be new. The principal residual originality risk is an indirectly equivalent asymptotic in older literature on finite sums of weighted composition operators or Hausdorff kernels. The 2001 Hardy-space representation paper was confirmed through its bibliographic record and abstract; the full text was not available through the inspected record. No independent validation or definitive publication-priority certification has been carried out.

## References

1. P. Galanopoulos, A. Mahillo, J. Oliva-Maza, A. G. Siskakis, *Hausdorff Matrices on the BMOA and Bloch spaces*, arXiv:2610.22554v1 (2026-10-15), https://arxiv.org/abs/2610.22554.
2. P. Galanopoulos, A. G. Siskakis, M. Papadimitrakis, *Hausdorff matrices and composition operators*, Illinois Journal of Mathematics **45** (2001), 757–773, DOI:10.1215/IJM/1258138149.
3. C.-o. Lo, A. W.-k. Loh, *Hilbert-Schmidtness of weighted composition operators and their differences on Hardy spaces*, Opuscula Mathematica **40** (2020), 495–507, DOI:10.7494/OpMath.2020.40.4.495.
4. E. Liflyand, *Hausdorff operators on Hardy spaces*, Eurasian Mathematical Journal **4** (2013), 101–141.
