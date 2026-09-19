# Sharp residual expansion for cubic reciprocal Fibonacci tails

Let \(F_0=0,F_1=1,F_{n+1}=F_n+F_{n-1}\), and define
\[
S_n=\sum_{k=n}^{\infty}\frac1{F_k^3}.
\]
Hwang, Park and Song (2026) proved that, for
\[
g_n=F_n^3-F_{n-1}^3+\frac{3(-1)^n}{11}(3F_n-F_{n-1}),
\]
one has \(S_n^{-1}-g_n\to0\), and more sharply
\[
0<S_n^{-1}-g_n<\frac2{F_n}
\]
for all sufficiently large \(n\). The asymptotic size and parity structure of this residual can be determined explicitly.

## Theorem

As \(n\to\infty\),
\[
\boxed{
S_n^{-1}
=g_n+\frac{\kappa}{F_n}
+\lambda\frac{(-1)^n}{F_n^3}
+O(F_n^{-5})
}
\]
where
\[
\boxed{
\kappa=\frac{948+72\sqrt5}{3509}
=0.316043572066111387330139784596\ldots
}
\]
and
\[
\boxed{
\lambda=\frac{18175-11739\sqrt5}{3666905}
=-0.00220191196332330159798175564877\ldots .
}
\]
In particular,
\[
\boxed{
F_n\bigl(S_n^{-1}-g_n\bigr)\longrightarrow \kappa .
}
\]
Thus the coefficient \(2\) in the known upper window \(g_n<S_n^{-1}<g_n+2/F_n\) is not asymptotically sharp. More precisely, for every \(\varepsilon>0\),
\[
g_n+\frac{\kappa-\varepsilon}{F_n}
<S_n^{-1}<
g_n+\frac{\kappa+\varepsilon}{F_n}
\]
for all sufficiently large \(n\). The infimum of constants \(C\) for which
\(S_n^{-1}<g_n+C/F_n\) eventually holds is therefore \(\kappa\).

The next term records a genuine parity oscillation:
\[
\boxed{
(-1)^nF_n^3\left(S_n^{-1}-g_n-\frac{\kappa}{F_n}\right)
\longrightarrow \lambda .
}
\]
Since \(\lambda<0\), the first-corrected residual lies asymptotically below \(\kappa/F_n\) for even \(n\) and above it for odd \(n\).

## Exact analytic representation and all-order expansion

Let
\[
\phi=\frac{1+\sqrt5}{2},\qquad x=\phi^{-n},\qquad \epsilon=(-1)^n.
\]
Binet's formula gives
\[
F_k=\frac{\phi^k}{\sqrt5}\left(1-(-1)^k\phi^{-2k}\right).
\]
Using
\((1-u)^{-3}=\sum_{m\ge0}\binom{m+2}{2}u^m\), absolute convergence permits summation first over \(k\), giving the exact identity
\[
S_n
=5\sqrt5\,x^3 A(\epsilon x^2),
\]
where
\[
A(z)=\sum_{m=0}^{\infty}
\binom{m+2}{2}
\frac{z^m}{1-(-1)^m\phi^{-(2m+3)}}.
\]
The series \(A\) is analytic for \(|z|<1\) and \(A(0)>0\). Hence \(1/A\) is analytic in a neighborhood of zero. If
\[
\frac1{A(z)}=\sum_{j=0}^{\infty}c_jz^j
\]
in that neighborhood, then for all sufficiently large \(n\),
\[
\boxed{
S_n^{-1}
=\frac{x^{-3}}{5\sqrt5}
\sum_{j=0}^{\infty}c_j\epsilon^j x^{2j}.
}
\]
This is a convergent local expansion and, in particular, provides an effective asymptotic expansion to arbitrary order. Writing
\[
a_m=\binom{m+2}{2}\Big/\left(1-(-1)^m\phi^{-(2m+3)}\right),
\]
the coefficients are recursively explicit:
\[
c_0=a_0^{-1},\qquad
c_j=-a_0^{-1}\sum_{i=1}^j a_i c_{j-i}\quad(j\ge1).
\]

## Derivation of the first two residual coefficients

Set
\[
B_0=\frac1{1-\phi^{-3}},\quad
B_1=\frac3{1+\phi^{-5}},\quad
B_2=\frac6{1-\phi^{-7}},\quad
B_3=\frac{10}{1+\phi^{-9}},
\]
\[
K=\frac1{5\sqrt5 B_0},\qquad r_j=\frac{B_j}{B_0}\quad(j=1,2,3).
\]
Then
\[
\begin{aligned}
S_n^{-1}
={}&Kx^{-3}-\epsilon Kr_1x^{-1}
+K(r_1^2-r_2)x\\
&+\epsilon K(-r_1^3+2r_1r_2-r_3)x^3+O(x^5).
\end{aligned}
\]
The exact simplifications needed here are
\[
K=-\frac15+\frac{3\sqrt5}{25},\quad
r_1=\frac3{11}+\frac{9\sqrt5}{11},\quad
r_2=\frac{84}{29}+\frac{24\sqrt5}{29},\quad
r_3=\frac{65}{19}+\frac{35\sqrt5}{19}.
\]
Direct substitution of Binet's formula in \(g_n\) gives
\[
g_n
=Kx^{-3}-\epsilon Kr_1x^{-1}
+G_1x+\epsilon G_3x^3,
\]
with
\[
G_1=-\frac{24}{55}-\frac{36\sqrt5}{275},
\qquad
G_3=-\frac15-\frac{3\sqrt5}{25}.
\]
Subtracting yields
\[
S_n^{-1}-g_n=C_1x+\epsilon C_3x^3+O(x^5),
\]
where
\[
C_1=\frac{360+948\sqrt5}{3509},
\qquad
C_3=\frac{16545+216307\sqrt5}{733381}.
\]
Finally,
\[
\frac1{F_n}=\sqrt5x\left(1+\epsilon x^2+x^4+O(x^6)\right),
\]
\[
\frac{\epsilon}{F_n^3}=5\sqrt5\,\epsilon x^3+O(x^5).
\]
Matching the \(x\) and \(\epsilon x^3\) coefficients gives
\[
\kappa=\frac{C_1}{\sqrt5},\qquad
\lambda=\frac{C_3-C_1}{5\sqrt5},
\]
which simplify to the constants stated above. Since \(x\asymp F_n^{-1}\), the remaining \(O(x^5)\) term is \(O(F_n^{-5})\).

## Verification

`artifacts/verify.py` independently performs the algebra in \(\mathbb Q(\sqrt5)\) with Python 3.13.5 / SymPy 1.14.0 and evaluates the original infinite tail at high precision with mpmath 1.3.0. The exact symbolic identities for \(\kappa\) and \(\lambda\) are asserted before the numerical checks. Representative outputs are recorded in `artifacts/verification.txt`.

For example,
\[
F_{40}(S_{40}^{-1}-g_{40})
=0.3160435720661113871198788\ldots,
\]
while
\[
F_{40}^3\left(S_{40}^{-1}-g_{40}-\frac{\kappa}{F_{40}}\right)
=-0.00220191196332330275911483\ldots,
\]
in agreement with the two stated constants.

## Relation to prior results

Li, Yang and Yuan (2025), in their Theorem 2.3 for generalized Fibonacci sequences, give an approximation whose specialization to the ordinary Fibonacci sequence is algebraically the same \(g_n\); their convention \(A_n\sim B_n\) means \(A_n-B_n\to0\). Wan, Liang and Liao (2026), Remark 3.3, explicitly state that their cubic specialization to the special Lucas sequence reduces to that 2025 theorem. Hwang, Park and Song (2026) then establish the algebraic inequalities
\[
g_n<S_n^{-1}<g_n+2/F_n
\]
for sufficiently large \(n\) and use them to recover the exact floor function.

The result here refines these statements by identifying the first nonzero residual coefficient, the next parity-dependent coefficient, and an exact analytic mechanism yielding all higher asymptotic coefficients.

## Limitations

Originality is asserted only to the best of our knowledge. The theorem concerns the full cubic Fibonacci tail \(\sum_{k\ge n}F_k^{-3}\); it does not give new floor formulas, and it does not claim analogous constants for arbitrary powers, subsequences, or general Lucas/Horadam sequences. The all-order expansion is local near \(\phi^{-n}=0\), so no explicit smallest threshold in \(n\) is claimed. The related 2024 paper of Li and He concerns odd/even cubic subsequences rather than this full tail. No independent validation or formal proof-assistant verification is asserted.

## References

1. W. Hwang, J.-D. Park, K. Song, *Continuous approximation to the reciprocal sum of the cubes of Fibonacci numbers*, arXiv:2609.18179 (2026). https://arxiv.org/abs/2609.18179
2. H. Li, K. Yang, P. Yuan, *The asymptotic behavior of the reciprocal sum of generalized Fibonacci numbers*, Electronic Research Archive 33 (2025), 409–432. https://doi.org/10.3934/era.2025020
3. Y. Wan, Z. Liang, Q. Liao, *The asymptotic estimation for two classes of generalized Fibonacci sub-sequences*, Mathematica Bohemica (online first, 2026). https://doi.org/10.21136/MB.2026.0161-25 ; arXiv:2510.13472
4. H. Li, Y. He, *The reciprocal sums of the cubes of odd and even terms in the Fibonacci sequence*, Acta Mathematica Sinica, Chinese Series 67 (2024), 926–938. https://doi.org/10.12386/A20210193
