# Universal square-root onset of four-periodic nonprobability Hard-Core boundary laws
## Finding
For the countable-state Hard-Core model on a Cayley tree in the \(q=4\) translation-invariant nonprobability branch studied by Rozikov, Khakimov, and Makhammadaliev, fix an integer \(k\ge2\), a positive even activity \(\lambda_2\), and the symmetric odd-activity slice \(\lambda_1=\lambda_3=\lambda\). The source proves that the symmetric boundary law loses uniqueness at
\[
\lambda_c=\frac{2^k(\lambda_2+1)}{(k-1)k^k},
\]
with exactly two additional swapped solutions \((a,c)\) and \((c,a)\) for \(\lambda>\lambda_c\).

Choose the nonsymmetric branch with \(a>c\) and define the dimensionless order parameter
\[
M=\frac{a-c}{a+c}.
\]
Then, as \(\lambda\downarrow\lambda_c\),
\[
M=\sqrt{\frac{6k}{2k^2-k+3}}\,
\sqrt{\frac{\lambda}{\lambda_c}-1}
+O\!\left(\left(\frac{\lambda}{\lambda_c}-1\right)^{3/2}\right).
\]
Equivalently,
\[
\log\frac{a}{c}=
\sqrt{\frac{24k}{2k^2-k+3}}\,
\sqrt{\frac{\lambda}{\lambda_c}-1}
+O\!\left(\left(\frac{\lambda}{\lambda_c}-1\right)^{3/2}\right).
\]
At the critical point,
\[
a=c=\frac{\lambda_2+1}{k-1}.
\]
The normalized contrast amplitude is independent of \(\lambda_2\), and
\[
\sqrt{\frac{6k}{2k^2-k+3}}\sim\sqrt{\frac3k}
\]
as \(k\to\infty\).

## Assumptions and scope
The model, normalization, and \(q=4\) branch are exactly those of arXiv:2307.03432v1. In the source notation, the relevant system is
\[
a=\lambda\left(\frac{1+\lambda_2+a}{a+c}\right)^k,
\qquad
c=\lambda\left(\frac{1+\lambda_2+c}{a+c}\right)^k.
\]
The statement concerns the translation-invariant nonprobability Gibbs measures represented by this branch. It does not count periodic nonprobability measures outside this branch, normalizable Gibbs measures, weakly periodic measures, extremal decompositions, or thermodynamic stability.

The asymptotic is one-sided from \(\lambda>\lambda_c\), where the source proves that the two nonsymmetric solutions exist and are a swap-pair.

## Proof
The source introduces
\[
t=\frac{\lambda_2+1+a}{\lambda_2+1+c}>0
\]
and proves that every nonsymmetric solution has
\[
a=t^k c,
\qquad
c(t)=\frac{\lambda_2+1}{t+t^2+\cdots+t^{k-1}},
\]
with activity
\[
\lambda(t)=
(\lambda_2+1)
\frac{(1+t^k)^k}
{\left(\sum_{j=1}^{k-1}t^j\right)
 \left(\sum_{j=0}^{k-1}t^j\right)^k}.
\]
The source also proves \(\lambda(t)=\lambda(1/t)\), that \(t=1\) is its unique minimum, and that \(\lambda(1)=\lambda_c\).

Set \(t=e^s\) and
\[
L(s)=\log\frac{\lambda(e^s)}{\lambda_c}.
\]
The reciprocal symmetry makes \(L\) even. Writing out the logarithm gives
\[
L(s)=k\log(1+e^{ks})
-\log\left(\sum_{j=1}^{k-1}e^{js}\right)
-k\log\left(\sum_{j=0}^{k-1}e^{js}\right)
-\log\frac{2^k}{(k-1)k^k}.
\]
For a finite set of exponents \(A\), the second derivative at zero of
\(\log\sum_{j\in A}e^{js}\) is the variance of the uniform distribution on \(A\). Hence
\[
L''(0)
=k\frac{k^2}4
-\frac{k(k-2)}{12}
-k\frac{k^2-1}{12}
=\frac{k(2k^2-k+3)}{12}>0.
\]
Therefore, with \(\delta=\lambda/\lambda_c-1\),
\[
\delta=\frac{k(2k^2-k+3)}{24}s^2+O(s^4),
\]
and the positive branch satisfies
\[
s=\sqrt{\frac{24}{k(2k^2-k+3)}}\,\sqrt\delta+O(\delta^{3/2}).
\]

Because \(a/c=t^k=e^{ks}\),
\[
M=\frac{e^{ks}-1}{e^{ks}+1}=\tanh\left(\frac{ks}2\right).
\]
Substituting the expansion for \(s\) and using \(\tanh x=x+O(x^3)\) gives
\[
M=\sqrt{\frac{6k}{2k^2-k+3}}\sqrt\delta+O(\delta^{3/2}).
\]
Similarly, \(\log(a/c)=ks\) gives the second displayed asymptotic. Finally, the source formula for \(c(t)\) gives
\[
a_c=c_c=c(1)=\frac{\lambda_2+1}{k-1}.
\]
The large-\(k\) amplitude follows directly from the closed form.

## Verification
The bundled `verify.py` checks the exact finite-sum variance identity for every integer \(2\le k\le200\), verifies the source parameterization in both original equations over representative \(k\), \(\lambda_2\), and near-critical \(s\), and checks convergence to the stated square-root coefficient. These computations are corroborative only; the proof is the analytic expansion above.

## Relationship to prior work
The primary preprint arXiv:2307.03432v1 gives the exact \(q=4\) parameterization, reciprocal symmetry \(t\leftrightarrow1/t\), the critical activity \(\lambda_c\), and the exact one-versus-three count. Its proof computes a polynomial coefficient containing \(2k^2-k+3\) while establishing monotonicity, but it does not state the local branch expansion, critical exponent, order-parameter amplitude, independence from \(\lambda_2\), or the large-order amplitude law.

The earlier special-case work cited by that paper covers \(\lambda_2=1\) and \(k=2,3,4\), whereas the present asymptotic holds for every \(k\ge2\) and every \(\lambda_2>0\). A later 2024 paper by Khakimov and Makhammadaliev studies translation-invariant probability Gibbs measures under different graph constraints, and does not imply this nonprobability \(q=4\) branch asymptotic.

## Limitations
The result is local to \(\lambda\downarrow\lambda_c\) from the symmetry-broken side. It does not assert that this order parameter controls thermodynamic observables, free-energy singularities, extremality, or stability. The coefficient is invariant under the source normalization only because \(M\) and \(\lambda/\lambda_c\) are dimensionless; different order parameters have different amplitudes.

A residual literature risk is that an equivalent pitchfork expansion may occur in weakly indexed notes under different boundary-law variables. The source's explicit formulas make the present derivation short, but the amplitude and universality statement are not contained in the inspected source text.

## References
1. U. A. Rozikov, R. M. Khakimov, and M. T. Makhammadaliev, *Gibbs measures for a Hard-Core model with a countable set of states*, arXiv:2307.03432v1 (2023); later *Reviews in Mathematical Physics* 37, 2450039, DOI:10.1142/S0129055X24500399.
2. R. M. Khakimov and M. T. Makhammadaliev, *Translation-Invariant Gibbs Measures for the Hard Core Model with a Countable Set of Spin Values*, arXiv:2310.12602v1 (2023); later *Lobachevskii Journal of Mathematics* 45, 3897--3911.
