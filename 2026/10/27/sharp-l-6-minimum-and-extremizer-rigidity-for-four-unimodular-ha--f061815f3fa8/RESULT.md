# Sharp \(L^6\) minimum and extremizer rigidity for four unimodular harmonics

## Finding

Equip \(\mathbb T=\{z\in\mathbb C:|z|=1\}\) with normalized Haar measure \(dt/(2\pi)\). For every polynomial
\[
P(z)=a_0+a_1z+a_2z^2+a_3z^3,\qquad |a_0|=|a_1|=|a_2|=|a_3|=1,
\]
its sixth moment obeys the **sharp** inequality
\[
\boxed{\ \frac1{2\pi}\int_0^{2\pi}|P(e^{it})|^6\,dt\;\ge\;616-\frac{148}{3}\sqrt{111}\;=\;96.24108152593155\ldots\ }.
\]
Put \(\phi_* = \arccos((\sqrt{111}-12)/6)\), with \(0<\phi_*<\pi\). Equality occurs **if and only if**, for some \(|\lambda|=|\omega|=1\) and \(\phi\in\{\phi_*,-\phi_*\}\),
\[
\boxed{\ P(z)=\lambda\left(1+\omega z+e^{i\phi}\omega^2z^2+e^{3i\phi}\omega^3z^3\right).\ }
\]
There are exactly two conjugate extremizing coefficient-phase orbits after quotienting by common phase and circle modulation. The sixth-moment optimizer differs strictly from the known fourth-moment optimizer for this same four-frequency aperture.

## Assumptions and scope

Only the four consecutive **distinct integer frequencies** \(0,1,2,3\), coefficients of **exactly unit modulus**, and the continuous circle with probability Haar measure are considered. The norm convention is
\[
\|P\|_6^6=\frac{1}{2\pi}\int_0^{2\pi}|P(e^{it})|^6\,dt.
\]
No assertion is made for other frequency supports, non-unimodular coefficients, sampled cyclic grids with aliasing, or non-sixth powers. Phase orbits refer only to the two norm-preserving symmetries \(P(z)\mapsto\lambda P(\omega z)\) with \(\lambda,\omega\in\mathbb T\).

## Proof

**1. Remove inessential phases.** Since every coefficient is nonzero and unimodular, multiplication by a unit scalar and rotation of \(z\) reduce uniquely up to angles modulo \(2\pi\) to
\[
Q(z)=1+z+uz^2+vz^3,\qquad u=e^{i\phi},\quad v=e^{i\psi}.
\]
Indeed, take \(\lambda=a_0\) and \(\omega=a_1/a_0\), so that \(u=a_0a_2/a_1^2\) and \(v=a_0^2a_3/a_1^3\). These transformations preserve the moment.

**2. Exact sixth-moment identity.** Write \(Q(z)^3=\sum_{k=0}^9c_kz^k\). Fourier orthogonality (Parseval) gives \(\|Q\|_6^6=\sum_{k=0}^9|c_k|^2\). Expanding these ten coefficients and pairing conjugate monomials yields the *exact* identity
\[
\begin{aligned}
\|Q\|_6^6={}&256+84\cos\phi+144\cos(\phi-\psi)\\
 &+84\cos(2\phi-\psi)+6\cos\psi+6\cos(3\phi-2\psi).
\end{aligned}
\]
The coefficient-convolution identity is also recomputed with exact integer Laurent arithmetic in `artifacts/verify.py`, independently of numerical quadrature.

**3. Reduce the global two-torus minimum to one real variable.** Set
\[
x=(\psi-\phi)/2,\qquad y=(\psi-3\phi)/2.
\]
Then \(\phi=x-y\), \(\psi=3x-y\); the preceding identity becomes
\[
\|Q\|_6^6=112+288\cos^2x+(132\cos x+48\cos^3x)\cos y.
\]
For \(t=|\cos x|\in[0,1]\), this implies
\[
\|Q\|_6^6\ge F(t):=112+288t^2-132t-48t^3.
\]
The bound is attainable at each \(t\): choose \(\cos y=-\operatorname{sgn}(\cos x)\) for \(t>0\), and any \(y\) for \(t=0\). Thus there is no relaxation gap.

**4. Sharp minimum.** Direct differentiation gives
\[
F'(t)=-12(12t^2-48t+11),\qquad F''(t)=576-288t>0\quad(0\le t\le1).
\]
The unique critical point in the interval is
\[
t_*=(12-\sqrt{111})/6\in(0,1),
\]
while the second quadratic root lies above \(1\). Strict convexity proves this is the unique global minimum, and exact substitution gives
\[
F(t_*)=616-\frac{148}{3}\sqrt{111}.
\]
These algebraic equalities are checked independently in the executable exact-arithmetic certificate.

**5. All equality cases.** Since \(t_*>0\), equality in the \(\cos y\) step forces \(\cos y=-\operatorname{sgn}(\cos x)\), so \(y\equiv0\pmod\pi\). Therefore \(\psi-3\phi=2y\equiv0\pmod{2\pi}\) and \(\cos\phi=-t_*=(\sqrt{111}-12)/6\). There are precisely the two solutions \(\phi=\pm\phi_*\pmod{2\pi}\). Conversely either solution yields every displayed equality, and restoring \(\lambda\) and \(\omega\) gives exactly the stated family. This proves the full quantifier and equality claims.

## Verification

Run `python3 artifacts/verify.py` from the package root; it requires only Python 3's standard library. The checker independently expands all ten coefficients of \(Q^3\) as integer Laurent polynomials in two formal phases, verifies every coefficient of the claimed moment formula, and checks the exact algebraic stationary root and minimum in the quadratic number field \(\mathbb Q(\sqrt{111})\). It additionally compares 50 deterministic coefficient convolutions and four 256-node circle quadratures against the closed formula, including both equality configurations. The committed `artifacts/checker_output.txt` records an actual successful execution.

All universal and sharp claims follow from the displayed symbolic argument. Finite computational samples supply consistency checks only and are not used as an infinite proof.

## Relationship to prior work

Schmidt (2013, arXiv:1302.2766) studies \(L^4\) flatness of long unimodular coefficient sequences; Günther and Schmidt (2016, arXiv:1602.01750) treat asymptotic even moments of specific long Littlewood families; Krenedits (2010, arXiv:1006.0409) treats the majorant problem at non-even exponents. None of their inspected main results gives this short four-mode sixth-moment minimum.

For this *same* four-frequency aperture, the published sharp **fourth** moment for unit-modulus coefficients is \(19\), with normalized minimizing phase satisfying \(\cos\phi=-1/4\); the present sixth-moment minimizing phase instead satisfies \(\cos\phi=(\sqrt{111}-12)/6\ne-1/4\). A separate published four-frequency **sixth-moment maximum over arbitrary magnitudes** is a different inequality with a different feasible-direction objective and does not imply this fixed-modulus lower bound. The standard coefficient majorant principle controls upper moments, not this destructive-interference minimum. The present claim is the sharp lower bound and complete phase-orbit rigidity, not these established formulas.

## Limitations

This exact constant is a four-tap result, not an asymptotic minimum or a general method for arbitrary lengths. Historical publication priority is subject to further scrutiny: older polyphase radar/sequence tables and unindexed specialized short-polynomial extremal formulas could contain an equivalent result. The relevant literature comparisons support a best-knowledge distinction, not an exhaustive global priority certification.

## References

1. S. Krenedits, *Three-term idempotent counterexamples in the Hardy--Littlewood majorant problem*, arXiv:1006.0409v1, first posted 2010-06-02, https://arxiv.org/abs/1006.0409 .
2. K.-U. Schmidt, *On a problem due to Littlewood concerning polynomials with unimodular coefficients*, arXiv:1302.2766v1, first posted 2013-02-12, https://arxiv.org/abs/1302.2766 .
3. C. Günther and K.-U. Schmidt, *\(L^q\) norms of Fekete and related polynomials*, arXiv:1602.01750v1, first posted 2016-02-04, https://arxiv.org/abs/1602.01750 .
4. *Sharp fourth-moment phase range for four-frequency unimodular trigonometric polynomials*, published mathematical finding, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-phase-range-for-four-frequency-unimodular-tr--2e72429a4d8d .
5. *Sharp sixth-moment Fourier norm via four-term even-moment symmetrization*, published mathematical finding, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-sixth-moment-fourier-norm-via-four-term-even-moment-symmet--f3e238ebf219 .
