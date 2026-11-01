# The sharp quadratic Hankel kernel-testing constant

## Finding

Let \(\psi(z)=az+bz^2\), where \(a,b\in\mathbb C\) are not both zero. On the Hardy space \(H^2(\mathbb D)\), let
\[
H_{\overline\psi}f=P_-(\overline\psi f):H^2\longrightarrow H^2_-,
\qquad
k_w(z)=\frac{\sqrt{1-|w|^2}}{1-\overline w z}.
\]
Then the **optimal uniform comparison constant** between the full Hankel norm and testing only on normalized reproducing kernels is
\[
\boxed{\ \|H_{\overline\psi}\|\leq\frac{3\sqrt3}{5}
\sup_{w\in\mathbb D}\|H_{\overline\psi}k_w\|_2.\ }
\]
The coefficient \(3\sqrt3/5\) is best possible. Equality holds **exactly** when \(a\ne0\), \(b\ne0\) and
\[
\boxed{\ \frac{|a|}{|b|}=\frac1{\sqrt6}.\ }
\]
At equality, the unique maximizing kernel parameter has modulus \(1/\sqrt6\) and its phase aligns the two terms of \(a+bw\). Equivalently, with the Garsia and Nehari quotient norms of the motivating paper,
\[
\boxed{\ \|\psi\|_*\le\frac{3\sqrt3}{5}\|\psi\|_G,\quad
\text{and the constant is sharp within the nonzero quadratic symbols.}\ }
\]
This result concerns a **global sharp norm ratio** on the entire two-coefficient quadratic family, not merely failure or occurrence of equality in the strong reproducing kernel thesis.

## Assumptions and scope

All scalars are complex, the Hardy basis is \(1,z,z^2,\ldots\), and \(P_-\) projects \(L^2(\mathbb T)\) onto negative Fourier modes. The norms are the standard Hilbert operator norm and the standard Hardy kernel-testing supremum. The zero symbol is excluded only to avoid an undefined ratio, although the inequality itself also holds trivially for it.

The family is the complete analytic degree-at-most-two polynomial subspace normalized by \(\psi(0)=0\). The classification of equality allows arbitrary nonzero complex scaling and independent coefficient phases; the phase of the maximizing kernel changes accordingly.

## Proof

**1. Finite Hankel matrix and kernel formula.** The only nonzero matrix block of \(H_{\overline\psi}\) in the Hardy/negative-Fourier bases is
\[
\begin{pmatrix}\overline a&\overline b\\\overline b&0\end{pmatrix}.
\]
Put \(A=|a|\), \(B=|b|\). Its largest singular value is
\[
N=\|H_{\overline\psi}\|=\frac{A+\sqrt{A^2+4B^2}}2.
\]
The normalized kernel has first two coordinates \(\sqrt{1-|w|^2}(1,\overline w)\); hence
\[
\|H_{\overline\psi}k_w\|_2^2
=(1-|w|^2)\bigl(|a+bw|^2+B^2\bigr).
\]
Maximizing the phase of \(w\) gives
\[
G^2:=\sup_{w\in\mathbb D}\|H_{\overline\psi}k_w\|_2^2
=\max_{0\le r\le1}(1-r^2)\bigl((A+Br)^2+B^2\bigr).
\]
The closed interval is harmless because the value at \(r=1\) is zero and the supremum is positive. If either coefficient vanishes, a direct check yields \(G=N\), so these cases are not extremal.

**2. Normalize the operator norm.** Divide the coefficients by \(N>0\), so that \(N=1\). The preceding singular-value formula is equivalent to
\[
A=1-B^2,\qquad0\le B\le1.
\]
Write \(b=B\) (now a real nonnegative parameter, not the original complex coefficient), and define
\[
F(b,r)=(1-r^2)\bigl((1-b^2+br)^2+b^2\bigr).
\]
It suffices to prove \(\max_{0\le r\le1}F(b,r)\ge25/27\), with equality exactly at \(b_0=\sqrt{2/3}\).

**3. A two-regime global lower certificate.** For \(0\le b\le1/2\), test the admissible radius \(r=b\):
\[
F(b,b)=(1-b^2)(1+b^2)=1-b^4\ge\frac{15}{16}>\frac{25}{27}.
\]
For \(1/2\le b\le1\), test the **fixed** radius \(r_0=1/\sqrt6\). Direct differentiation gives
\[
\frac{\partial F}{\partial b}(b,r_0)
=2(1-r_0^2)(b-r_0)(2b^2-br_0-1).
\]
On \([1/2,1]\), the first factor and \(b-r_0\) are positive; the last factor is strictly increasing and has its unique zero at \(b_0=\sqrt{2/3}\). Thus \(b_0\) is the unique global minimum of \(b\mapsto F(b,r_0)\) on this interval, and direct substitution yields
\[
F(b,r_0)\ge F(b_0,r_0)=\frac{25}{27},
\]
with equality only at \(b_0\). Together, the two regimes prove the bound and the necessity of the equality parameter.

**4. Sharpness and exact equality.** At \(b=b_0\), the normalized linear coefficient is \(1-b_0^2=1/3\). With \(t=\sqrt6\,r\), a direct polynomial factorization gives
\[
\frac{25}{27}-F(b_0,r)
=\frac{(t-1)^2(t^2+4t+8)}{54}\ge0.
\]
The second factor is strictly positive for \(t\ge0\). Therefore the full kernel supremum is **exactly** \(G^2=25/27\), attained only at radius \(r=r_0\). Since \(N=1\), the sharp ratio is \(N/G=\sqrt{27}/5=3\sqrt3/5\). Undoing normalization gives
\[
\frac{A}{B}=
\frac{1/3}{\sqrt{2/3}}=\frac1{\sqrt6}.
\]
Conversely, every nonzero quadratic pair with this modulus ratio normalizes to \(b_0\), and the aligning kernel realizes equality. All conclusions hold independently of the original coefficient phases.

## Verification

The proof is algebraic and holds simultaneously for all nonzero complex coefficients and every kernel parameter. The only nonstandard global step is the explicit two-test lower certificate together with the factored upper certificate at its equality parameter. Both are displayed above and can be checked by polynomial expansion and one-variable differentiation.

For the concrete example \(\psi(z)=z^2+z/\sqrt6\), the full operator norm is \(\sqrt{3/2}\), while the maximal kernel norm is \(5/(3\sqrt2)\); their ratio is \(3\sqrt3/5\).

The companion script `verify.py` uses only the Python standard library. Run `python3 verify.py` alongside this document. It verifies the factorization using exact rational-polynomial arithmetic, then checks the lower test certificates, direct complex-phase profiles, and sharp equality on finite deterministic grids. It is supplementary evidence, **not** an infinite proof. The analytical argument above, including boundary and equality cases, is independent of that script.

## Relationship to prior work

Dyakonov's 2026 paper formulates the strong reproducing kernel thesis for Hardy Hankel operators, proves the identification of the kernel testing norm with the Garsia norm, and explicitly notes that a suitable symbol of the form \(az+z^2\) violates equality of the two norms. Its October 2026 addendum describes the norm-attaining equality class by inner functions; it does not compute the best **uniform quantitative** inequality for the quadratic family. The present result supplies that sharp finite-degree test-to-operator constant and its complete equality family.

Previously published polynomial-symbol and finite-rank classifications identify cases with **zero** norm gap, but do not determine the largest positive gap across quadratic coefficients. An earlier analysis of two-monomial Hankel symbols gives strictness and a small-coefficient expansion, not the global optimal quadratic ratio. A separately computed logarithmic-Hankel gap concerns a nonpolynomial infinite-rank symbol and does not imply the quadratic extremal value.

Classical reproducing-kernel-thesis results of Bonsall and Treil furnish bounds and boundedness criteria for broader Hankel classes; those statements do not specify this best constant for the first nontrivial polynomial subclass. Results about maximal/minimal Hankel norm concern different norm equalities. These comparisons do not constitute independent publication-priority certification.

## Limitations

Only the quadratic polynomial family \(\psi(z)=az+bz^2\) is treated. The constant is **not** claimed to be optimal for all polynomial degrees, all finite-rank Hankel operators, all BMOA symbols, or unrelated reproducing-kernel Hilbert spaces. The result does not classify arbitrary nonpolynomial norming symbols. A differently formulated older finite-matrix kernel-testing inequality might predate this sharp calculation; a targeted search found no such coverage, but publication priority remains open to human verification.

## References

1. K. M. Dyakonov, *The Strong Reproducing Kernel Thesis for Hankel Operators and the Garsia Norm*, arXiv:2609.33242v1 (27 September 2026); v3 addendum (18 October 2026), https://arxiv.org/abs/2609.33242.
2. O. F. Brevig, *Minimal norm Hankel operators*, Proc. Amer. Math. Soc. 150 (2022), 4383–4391; arXiv:2107.01680.
3. O. F. Brevig and K. Seip, *Maximal norm Hankel operators*, J. Math. Anal. Appl. 529 (2024), 127221; arXiv:2301.07937.
4. S. Treil, *A remark on the reproducing kernel thesis for Hankel operators*, St. Petersburg Math. J. 26 (2015), 479–485; arXiv:1201.0063.
5. F. F. Bonsall, *Boundedness of Hankel matrices*, J. London Math. Soc. 29 (1984), 289–300.
6. *Monomial rigidity for polynomial-symbol Hankel operators obeying the strong reproducing kernel thesis*, published-finding corpus mathematical record, 2026-10-04, identifier bc8369ca1a24.
7. *Shifted-Blaschke classification of finite-rank SRKT Hankel operators*, published-finding corpus mathematical record, 2026-10-11, identifier c64bd5a5783f.
