# Quantized inversion symmetries of two-boundary weighted annular Hardy spaces

## Finding
Fix \(0<r<1\), \(0<p<\infty\), and boundary weights \(w_o,w_i>0\). Let \(A_r=\{z\in\mathbb C:r<|z|<1\}\) and \(dm(e^{it})=dt/(2\pi)\). Equip the analytic Hardy class with
\[
\|f\|_{p,w}^{p}=w_o\int_{\mathbb T}|f(e^{it})|^{p}\,dm+w_i\int_{\mathbb T}|f(re^{it})|^{p}\,dm.
\]
For an annulus automorphism \(\phi\), and a bounded holomorphic multiplier \(\psi\) with bounded holomorphic inverse, define \(T_{\psi,\phi}f=\psi(f\circ\phi)\). Then this operator is a surjective linear isometry if and only if precisely one of the following alternatives applies:

1. \(\phi(z)=e^{i\theta}z\) and \(\psi(z)=e^{i\eta}\) for real \(\theta,\eta\).
2. \(\phi(z)=e^{i\theta}r/z\), and an integer \(k\in\mathbb Z\) satisfies
\[
\frac{w_i}{w_o}=r^{-kp/2},\qquad \psi(z)=e^{i\eta}r^{-k/2}z^k.
\]

In particular, an inversion-induced isometry exists if and only if
\[
\frac{2\log(w_i/w_o)}{p\log(1/r)}\in\mathbb Z.
\]
For each permissible inversion, its multiplier is unique up to a unimodular scalar. When the ratio is not in the discrete set \(\{r^{-kp/2}:k\in\mathbb Z\}\), only rotation-induced weighted-composition isometries survive.

## Assumptions and scope
The boundary integrals refer to almost-everywhere nontangential traces; Laurent polynomials are dense in the resulting annular Hardy class. The multiplier is required to satisfy \(\psi,1/\psi\in H^\infty(A_r)\); no smooth boundary extension is needed. The exponent may be less than one (when the displayed expression defines a quasi-norm). **Only isometries already known to be of weighted-composition form** are classified. No assertion concerns arbitrary linear isometries (notably the other Hilbert-space unitaries at \(p=2\)). An automorphism of a concentric annulus is either a rotation or a rotated inversion.

## Proof
**Boundary density lemma.** Let \(\rho\) be a positive bounded measurable density on the circle. Suppose for every complex Laurent polynomial \(P\),
\[
\int_{\mathbb T}\rho(z)|P(z)|^pdm(z)=c\int_{\mathbb T}|P(z)|^pdm(z).
\]
Taking \(P\equiv1\) gives \(\int\rho=c\). For each nonzero integer \(m\), insert \(P(z)=1+\varepsilon z^m\), with \(\varepsilon\) in a sufficiently small complex neighborhood of zero. Differentiate with respect to its real and imaginary parts at zero, using \(p>0\); the resulting first-order identities make both parts of every nonzero Fourier coefficient of \(\rho\) vanish. Therefore \(\rho=c\) almost everywhere, by uniqueness of Fourier coefficients of integrable functions. The same argument applies to circles of radius \(r\), after rescaling their angular coordinate.

**Boundary mass identities.** Write \(A(P)=\int_{\mathbb T}|P(z)|^pdm\) and \(B(P)=\int_{\mathbb T}|P(rz)|^pdm\). For each integer \(n\), test the isometry with \(f(z)=z^nP(z)\). For inversion \(\phi(z)=e^{i\theta}r/z\), the norm identity is
\[
 w_o A(P)+w_i r^{np}B(P)=w_o r^{np}C(P)+w_iD(P),
\]
where
\[
 C(P)=\int_{\mathbb T}|\psi(z)|^p|P(e^{i\theta}r/z)|^pdm(z),\quad
 D(P)=\int_{\mathbb T}|\psi(rz)|^p|P(e^{i\theta}/z)|^pdm(z).
\]
Letting \(n\to+\infty\) and then \(n\to-\infty\) after dividing by \(r^{np}\), respectively, yields \(w_oA(P)=w_iD(P)\) and \(w_iB(P)=w_oC(P)\), for every Laurent polynomial \(P\). The boundary density lemma, followed by the change of variable \(z\mapsto e^{i\theta}/z\), proves
\[
 |\psi(z)|^p=w_i/w_o\quad(|z|=1),\qquad
 |\psi(z)|^p=w_o/w_i\quad(|z|=r)
\]
in the almost-everywhere boundary sense. For the rotation case, an analogous separation on the two boundary circles gives \(|\psi|=1\) on both.

**Holomorphic winding rigidity.** Because \(\psi\) and \(1/\psi\) are bounded analytic functions, \(u=\log|\psi|\) is a bounded harmonic function in \(A_r\). Its two boundary traces are constant. The uniqueness of the bounded harmonic Dirichlet solution on the annulus forces \(u(z)=\log|c|+a\log|z|\) for a real \(a\). Local harmonic conjugation yields \(\psi(z)=cz^a\) on the universal covering strip; single-valuedness around the annular core forces \(a=k\in\mathbb Z\), hence \(\psi(z)=cz^k\). In the inversion case the two boundary identities give
\[
 |c|^p=w_i/w_o,\qquad |c|^pr^{kp}=w_o/w_i.
\]
Consequently \(w_i/w_o=r^{-kp/2}\) and \(|c|=r^{-k/2}\). For rotations the two boundary moduli equal one, hence \(k=0\) and \(|c|=1\).

**Sufficiency and surjectivity.** For rotations with constant unimodular multiplier, angular integration is unchanged. For the inversion alternative, the outer boundary contribution of \(Tf\) is \(w_o|c|^pB(f)=w_iB(f)\); the inner contribution is \(w_i|c|^pr^{kp}A(f)=w_oA(f)\). Thus the norm is preserved. The symbol is an automorphism and the multiplier is boundedly invertible, so the inverse weighted-composition operator exists on the Hardy class, proving surjectivity. These arguments work for every \(p>0\).

## Verification
The proof uses Laurent tests for all integer modes, the elementary boundary-density lemma, uniqueness of bounded harmonic functions on an annulus and monodromy of the harmonic conjugate. A standalone Python checker (`verify.py`) checks the inversion norm identity at two nontrivial integer winding numbers on independently chosen Laurent data (using exact coefficient sums at \(p=2\)), and checks that an off-lattice weight ratio violates at least one monomial norm equality for each attempted exponent in a finite range. The latter finite test is illustrative, not a substitute for the universal winding argument.

## Relationship to prior work
Chen–Li–Long–Luo (2026) investigate boundary measures and weighted Hardy-space isometries on smoothly bounded pseudoconvex domains in dimensions at least two; their source motivates the boundary-measure question but does not cover this one-dimensional annulus. Leblond–Pozzi–Russ (2015), §6.2, classify *unweighted composition* isometries on annular Hardy spaces, including inversion. Chalendar–Oger–Partington (2025) classify isometries of the distinct Fréchet space of *all* holomorphic functions on a symmetric annulus, for seminorm geometry rather than the two-boundary weighted Hardy integral. Neither inspected result gives the discrete weight-ratio condition and integer-winding multiplier classification above. The new statement is restricted to weighted-composition operators and does not assert a general Forelli classification.

## Limitations
No claim is made for angularly varying boundary weights, noninvertible holomorphic multipliers, nonautomorphic symbols or general surjective linear isometries. The annulus excludes the punctured disk limit and its degeneration. The finding is self-contained, but priority in the larger weighted Hardy operator literature remains a residual risk; an inaccessible full manuscript is not treated as proved noncoverage. The theorem has not undergone independent validation.

## References
- R.-Y. Chen, S.-Y. Li, S. Long, and J. Luo, *Boundary Geometry and Surjective Linear Isometries of Weighted Hardy Spaces*, arXiv:2609.04612v1 (first posted 2026-09-04), introduction and §5; https://arxiv.org/html/2609.04612v1.
- J. Leblond, E. Pozzi, and E. Russ, *Composition Operators on Generalized Hardy Spaces*, Complex Analysis and Operator Theory 9 (2015), 1733–1757, especially §6.2, doi:10.1007/s11785-015-0464-9.
- I. Chalendar, L. Oger, and J. R. Partington, *Linear isometries on the annulus: description and spectral properties*, Banach Journal of Mathematical Analysis 19 (2025), paper 23, arXiv:2409.16105v2, especially §4; https://arxiv.org/html/2409.16105v2.
