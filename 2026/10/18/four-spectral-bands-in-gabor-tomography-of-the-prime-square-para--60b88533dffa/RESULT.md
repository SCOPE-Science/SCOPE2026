# Four spectral bands in Gabor tomography of the prime-square parabola

## Finding
For each odd prime \(p\), let \(R=\mathbb Z/p^2\mathbb Z\), \(G=R^2\), \(d=p^4\), and let the unit vector \(g=p^{-1}\mathbf 1_C\in \mathbb C^G\) be supported on the parabola \(C=\{(t,t^2):t\in R\}\). For every translation \(a\in G\) and modulation \(b\in G\), form the Weyl shift \(W_{a,b}=M_bT_a\) and the rank-one projector \(P_{a,b}=|W_{a,b}g\rangle\langle W_{a,b}g|\). The linear matrix-measurement operator is \(\mathcal L_g(X)=(\operatorname{tr}(XP_{a,b}))_{a,b\in G}\), equipped with the Hilbert--Schmidt norm on complex matrices and the ordinary coefficient norm on the output.

Its nonzero singular values, with multiplicities, are **exactly**
\[
\begin{array}{c|c}
\text{singular value}&\text{multiplicity}\\\hline
1&p^7(p-1)\\
p&p^5-p^3\\
p^{3/2}&p(p-1)\\
p^2&1
\end{array}.
\]
The remaining \(p^8-p^7+p^5-p^3+p^2-p+1\) expression is the **rank**, not the nullity:
\[
\operatorname{rank}(\mathcal L_g)=p^8-p^7+p^5-p^3+p^2-p+1,\qquad
\operatorname{nullity}(\mathcal L_g)=p^7-p^5+p^3-p^2+p-1.
\]
All null Weyl directions are identified by the zero conditions in the proof. The exact condition number of the restriction to the identifiable matrix subspace is \(p^2\).

## Assumptions and scope
The ring is the composite-order ring \(\mathbb Z/p^2\mathbb Z\), not the field \(\mathbb F_{p^2}\). The prime is odd, including \(p=3\). Modulations act by \((M_bf)(x)=e_{p^2}(b\cdot x)f(x)\), translations by \((T_af)(x)=f(x-a)\), and \(e_{p^2}(z)=\exp(2\pi iz/p^2)\). The four singular-value levels include multiplicities and are for the unrescaled full collection of \(d^2=p^8\) intensity-lifting measurements. Singular values at zero are omitted from the table.

## Proof
Write \(a=(u,v)\), \(b=(r,s)\). The ambiguity coefficient is, up to a unit-modulus convention factor,
\[
A(a,b)=\langle g,W_{a,b}g\rangle
=p^{-2}\sum_{\substack{t\in R\\2ut-u^2=v}}e_{p^2}(rt+st^2).
\]
This follows from intersecting the parabola with its translate and the identity \(t^2-(t-u)^2=2ut-u^2\). We classify all possible absolute values.

**Unit first-coordinate displacement:** If \(p\nmid u\), the intersection equation uniquely determines \(t\in R\), for every \(v\) and every modulation \((r,s)\). Thus \(|A|=p^{-2}\). There are \(p^3(p-1)\) such translations and \(p^4\) modulations, giving \(p^7(p-1)\) coefficients.

**Nonzero nilpotent displacement:** If \(u=pU\ne0\) modulo \(p^2\), then the equation is solvable if and only if \(v=pV\). In that case all its solutions are \(t=t_0+pk\), \(k\in\mathbb F_p\), where \(2Ut_0\equiv V\pmod p\). The sum over \(k\) is zero unless \(r+2st_0\equiv0\pmod p\); otherwise \(|A|=p^{-1}\). Each of the \(p(p-1)\) admissible translations has exactly \(p^3\) nonzero modulations, contributing \(p^4(p-1)\) coefficients of modulus \(p^{-1}\).

**Other nonzero displacements:** If \(u=0\), \(v\ne0\), or \(u=pU\ne0\) and \(p\nmid v\), the parabola and its translate are disjoint, so the ambiguity is zero.

**Zero displacement:** For \(a=0\), the ambiguity is the normalized complete quadratic sum
\[
A(0,(r,s))=p^{-2}\sum_{t\pmod{p^2}}e_{p^2}(rt+st^2).
\]
When \(p\nmid s\), completing the square and the elementary quadratic Gauss-sum identity modulo \(p^2\) give absolute value \(p^{-1}\), for exactly \(p^4-p^3\) frequency pairs. If \(p\mid s\) but \(p\nmid r\), summation over the top base-\(p\) digit gives zero. If \(r=pR\), \(s=pS\), \(S\ne0\pmod p\), the sum is \(p\) times an ordinary nondegenerate quadratic Gauss sum modulo \(p\), so \(|A|=p^{-1/2}\); exactly \(p(p-1)\) pairs have this form. Finally \(A(0,0)=1\), and \(s=0\), \(r\ne0\) gives zero. The classical Gauss identities used here follow directly by multiplying each sum by its complex conjugate and applying orthogonality of additive characters after the invertible substitution \(t\mapsto t+h\).

Consequently the nonzero ambiguity magnitudes and multiplicities are
\[
\begin{array}{c|c}
|A|&\text{count}\\\hline
p^{-2}&p^7(p-1)\\
p^{-1}&p^5-p^3\\
p^{-1/2}&p(p-1)\\
1&1
\end{array}.
\]
The orthogonal Weyl matrices are simultaneous eigenvectors of the projector-frame superoperator \(\mathcal L_g^*\mathcal L_g\): Weyl covariance turns its action into character orthogonality, yielding eigenvalues \(d|A(a,b)|^2\) with the same multiplicities. As \(d=p^4\), their square roots are the four stated singular values. The kernel is the span of those Weyl matrices whose corresponding ambiguity value is zero; equivalently, it comprises (i) every disjoint-translation direction, (ii) nilpotent translations violating \(r+2st_0\equiv0\pmod p\), and (iii) origin translations with \(p\mid s\) and either \(p\nmid r\) or \(s=0\), \(r\ne0\). Counting positive eigenvalues proves the rank; subtracting from \(p^8\) proves the nullity. Finally, the ratio of largest to smallest nonzero singular values equals \(p^2\).

## Verification
The accompanying `verify.py` directly enumerates parabola intersections and performs a two-dimensional FFT of each intersection indicator over \(R^2\) for \(p\in\{3,5,7\}\). It checks every ambiguity frequency, all magnitude classes, and the predicted ranks. The separate `verify_output.txt` records its successful result. The global theorem follows from the symbolic case split above, not from the three finite tests.

## Relationship to prior work
Goldberger--Kang--Okoudjou establish the general relation between Gabor projector Gram eigenvalues and the ambiguity transform for cyclic systems (arXiv:2106.01509v1). The Fourier-restriction framework over composite rings developed by Hickman--Wright (arXiv:1801.03176v1) motivates treating prime-square rings differently from finite fields. Neither cited result supplies the zero-classification or the four-band spectrum for this prime-square parabola. Separately, known sharp fourth-moment extension results for this parabola address synthesis norms, not projector-tomography rank.

## Limitations
This is a statement about **linear recovery of arbitrary complex matrices**, not nonlinear recovery of pure states. No independent audit is claimed. Older unindexed literature could contain equivalent formulas. The FFT checks are finite illustrations; they are not proof for all primes.

## References
1. A. Goldberger, T. Kang and K. A. Okoudjou, *Towards a Classification of Incomplete Gabor POVMs in \(\mathbb C^d\)*, arXiv:2106.01509v1 (June 2, 2021).
2. J. Hickman and J. Wright, *The Fourier Restriction and Kakeya Problems over Rings of Integers Modulo \(N\)*, arXiv:1801.03176v1 (January 9, 2018).
