# An exact physical-residual resonance in scalar affine infinite GMRES

## Finding

For each real \(a>0\), real target parameter \(s>0\), integer \(m\geq1\), and Taylor-companion truncation \(q\geq m\), apply \(m\) unrestarted, exact-arithmetic infinite-GMRES steps from zero to the right-preconditioned companion system associated with
\[
A(s)x(s)=1,\qquad A(s)=1+as.
\]
Use the unscaled companion \(B=L_1L_0^{-1}\) and extract the physical approximation by the first coordinate of \(L_0^{-1}\widehat v_m\), as in the Toeplitz infinite-GMRES method of Gao and Jiang [1]. Define
\[
W_m(a,s)=1+s^{-2}+(1+as)^2\sum_{j=2}^{m}s^{-2j},
\]
where the sum is zero for \(m=1\). Let \(R_m\) denote the Euclidean norm of the minimized *lifted* residual, and let \(E_m\) denote the absolute *physical* residual \(\lvert1-(1+as)\widetilde x_m(s)\rvert\), which is also the relative solution error.

Then the following are exact for every \(m\geq1\):
\[
\boxed{R_m^2=\frac1{W_m(a,s)},\qquad
E_m=\frac{|1-a/s|}{W_m(a,s)}=|1-a/s|R_m^2.}
\]
Consequently, \(R_m>0\) at every finite iteration, but the recovered physical solution is **already exact at every iteration if and only if \(s=a\)**. The resonance is not limited to parameters inside the unit disk. For instance, \(a=s=2\) gives \(\widetilde x_1=1/5\) and \(R_1^2=4/5\), while \(\lim_{m\to\infty}R_m^2=3/10\): the nonzero lifted-residual floor coexists with zero physical error.

For \(a\ne s\), the exact asymptotic regimes are
\[
\begin{aligned}
0<s<1:\quad &R_m\sim\frac{\sqrt{1-s^2}}{1+as}s^m,\\
&E_m\sim\frac{|1-a/s|(1-s^2)}{(1+as)^2}s^{2m};\\
s=1:\quad &R_m\sim\frac1{(1+a)\sqrt m},\qquad
E_m\sim\frac{|1-a|}{(1+a)^2m};\\
s>1:\quad &R_m^2\longrightarrow\frac{s(s^2-1)}{s^3+a^2s+2a},\\
&E_m\longrightarrow\frac{|s-a|(s^2-1)}{s^3+a^2s+2a}>0.
\end{aligned}
\]
At \(a=s\), \(E_m=0\) identically and the nonzero lifted-residual formulas remain valid.

## Assumptions and scope

The coefficients and target parameter are real and strictly positive; the scalar right-hand side is one; \(A(0)=1\); and exact, unrestarted Euclidean GMRES starts from the zero lifted vector. The companion is precisely \(B=L_1L_0^{-1}\) with the unweighted coefficient blocks of [1, Section 2], not a factorial-weighted, differently normalized, or inexactly preconditioned variant. Every \(q\ge m\) has the same first \(m\) Krylov steps. The original scalar system is nonsingular because \(1+as>0\).

The same phenomenon embeds in arbitrarily large positive-definite diagonal systems \(A(s)=I+s\operatorname{diag}(a,d_2,\ldots,d_n)\) with \(d_j>0\) and right-hand side the first coordinate vector: its invariant one-coordinate Krylov problem reproduces the scalar formulas. This embedding does not assert identical behavior for general right-hand sides or non-diagonal systems.

## Proof

Let \(e_0,e_1,\ldots\) be the canonical lifted coordinate vectors. For the affine coefficients \(A_0=1\), \(A_1=a\), \(A_j=0\) for \(j\ge2\), the prescribed companion has the actions
\[
Be_0=e_1,\qquad Be_1=-ae_1+e_2,\qquad Be_j=e_{j+1}\quad(j\ge2).
\]
Successive powers of \(B\) applied to \(e_0\) therefore span \(\mathcal K_m(B,e_0)=\operatorname{span}\{e_0,\ldots,e_{m-1}\}\). This basis change is invertible for every finite \(m\), so the GMRES minimizer can be computed directly in coordinate form.

Write the lifted iterate as \(\widehat v_m=\sum_{j=0}^{m-1}y_je_j\). The residual is \(r=e_0-M_my\), where the \((m+1)\)-by-\(m\) matrix \(M_m\) has entries
\[
(M_m)_{j,j}=\begin{cases}1+as,&j=1,\\1,&j\ne1,\end{cases}
\quad(0\le j<m),\qquad (M_m)_{j+1,j}=-s\quad(0\le j<m),
\]
with all other entries zero. Its columns are linearly independent, since the first \(m\) rows form an invertible lower-bidiagonal matrix. A nonzero generator for the one-dimensional left null space is
\[
w=(1,s^{-1},(1+as)s^{-2},(1+as)s^{-3},\ldots,(1+as)s^{-m})^{\mathsf T},
\]
with only the first two entries when \(m=1\). Direct substitution gives \(M_m^{\mathsf T}w=0\) and \(\|w\|_2^2=W_m\). Hence the minimum-residual vector is the orthogonal projection of \(e_0\) onto \(\ker M_m^{\mathsf T}\):
\[
r=\frac{w}{W_m},\qquad \|r\|_2^2=\frac1{W_m}.
\]

The first block row of \(L_0^{-1}\) is \((1,-a,0,\ldots)\), so physical recovery is \(\widetilde x_m=y_0-ay_1\), defining \(y_1=0\) for \(m=1\). The first two residual equations, valid also with this convention, read
\[
r_0=1-y_0,\qquad r_1=sy_0-(1+as)y_1.
\]
They imply the exact, signed physical-residual identity
\[
1-(1+as)\widetilde x_m=r_0-ar_1
=\frac{1-a/s}{W_m}.
\]
Since \(W_m\) is finite and strictly positive for every finite \(m\), the asserted equivalence between physical exactness and \(a=s\) follows. Because \(x(s)=1/(1+as)\), the relative solution error equals the absolute physical residual.

For \(0<s<1\), the geometric sum satisfies \(\sum_{j=2}^{m}s^{-2j}\sim s^{-2m}/(1-s^2)\). At \(s=1\), it is exactly \(m-1\). For \(s>1\), it tends to \(1/[s^2(s^2-1)]\), and elementary simplification yields
\[
W_\infty=\frac{s^4+a^2s^2+2as}{s^2(s^2-1)}.
\]
Taking the reciprocal and applying the physical-residual identity gives all stated asymptotics and exact limiting constants. The diagonal embedding follows by invariance of the first-coordinate lifted subspace.

## Verification

The standalone `verify.py` independently builds the actual rectangular companion-GMRES least-squares matrix, solves its normal equations using exact rational Gaussian elimination, recovers the original scalar iterate, and compares both residuals with the closed formulas. It passes **288** exact-rational cases (eight iteration counts, six positive rational coefficients, six positive rational parameters), including \(s<1\), \(s=1\), \(s>1\), and resonant/nonresonant cases. The proof above, rather than this finite test, establishes statements for all iteration counts and continuous parameter ranges.

Run from the directory containing the files: `python3 verify.py`. Only the Python standard library is required.

## Relationship to prior work

Gao and Jiang [1, Sections 2–3] specify the exact right-preconditioned Toeplitz companion and physical recovery used here. Their Section 5 proves a lower bound for the **lifted GMRES residual** outside the unit parameter disk; it does not establish a corresponding lower bound for the recovered physical-system residual. In particular, the positive lifted floor in the present theorem is compatible with that result, while the resonance demonstrates why it cannot be interpreted as a physical-error floor. Their general residual and recovery formulas are credited.

Jarlebring and Correnty [2] introduce infinite GMRES for parameterized systems and derive convergence bounds for a related companion representation. Correnty, Jarlebring and Soodhalter [3] analyze inexact-preconditioned infinite GMRES and show physical-system residual experiments. Neither inspected discussion states this all-iteration scalar lifted-to-physical square identity, its exactness resonance, or the three-regime classification. The finite-dimensional GMRES orthogonal projection principle used in the proof is standard, not claimed as novel.

## Limitations

This is an exact-arithmetic analysis for a scalar affine family (and its invariant diagonal embedding). It neither asserts generic higher-dimensional exactness at the first iteration nor guarantees small computed residuals in finite precision. Changing the companion scaling, normalization, starting vector, or inexact preconditioner may alter the formulas. Existing broad GMRES and least-squares identities might independently yield this special case; historical priority beyond the inspected literature remains uncertain. No independent mathematical audit has been performed.

## References

[1] W. Gao and F. Jiang, *Toeplitz Infinite GMRES for Parameterized Linear Systems*, arXiv:2610.01740v1, first posted October 1, 2026. https://arxiv.org/html/2610.01740v1

[2] E. Jarlebring and S. Correnty, *Infinite GMRES for parameterized linear systems*, arXiv:2102.04082, 2021; *SIAM Journal on Matrix Analysis and Applications* 43 (2022), 1382–1405. https://arxiv.org/abs/2102.04082

[3] S. Correnty, E. Jarlebring and K. M. Soodhalter, *Preconditioned Infinite GMRES for Parameterized Linear Systems*, arXiv:2206.05153, 2022; *SIAM Journal on Scientific Computing*, DOI:10.1137/22M1502380. https://arxiv.org/abs/2206.05153
