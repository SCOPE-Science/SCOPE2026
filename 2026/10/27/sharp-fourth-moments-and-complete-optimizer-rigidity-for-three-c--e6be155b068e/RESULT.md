# Sharp fourth moments and complete optimizer rigidity for three consecutive \(SU(2)\) characters

## Finding
Let \(\chi_m\) denote the irreducible character of \(SU(2)\) of highest weight \(m\), with Haar probability measure, and let \(n\) be any nonnegative integer. Define
\[
K_n=\sup_{(a,b,c)\ne(0,0,0)}
\frac{\displaystyle\int_{SU(2)}|a\chi_n+b\chi_{n+1}+c\chi_{n+2}|^4\,dg}
{(|a|^2+|b|^2+|c|^2)^2}.
\]
Let \(t_n\in(0,1)\) be the unique positive root of
\[
H_n(t)=(8n^2+13n+6)t^3+(8n^2+29n+20)t^2
+(-8n^2-5n+10)t-(8n^2+21n+13).
\]
Define
\[
u_n=\frac{(t_n+1)(2nt_n^3+2n+2t_n^3+4t_n^2-t_n+3)}
{2nt_n^2+6nt_n+2n+t_n^2+6t_n+4}>0.
\]
Then the **exact sharp constant** is \(K_n=R_n(t_n)\), where
\[
R_n(t)=\frac{N_n(t)}{D_n(t)},
\]
\[
\begin{aligned}
N_n(t)={}&8n^2(t+1)^4+n(15t^4+64t^3+108t^2+96t+31)\\
&+7t^4+36t^3+60t^2+64t+30,\\
D_n(t)={}&4n(t^4+2t^3+t^2+2t+1)
+3t^4+12t^3+8t^2+8t+7.
\end{aligned}
\]
Every nonzero equality triple, and no others, is
\[
(a,b,c)=\zeta\,(t_n,\varepsilon\sqrt{u_n},1),
\qquad\zeta\in\mathbb C\setminus\{0\},\quad\varepsilon\in\{-1,1\}.
\]
In particular, **all three Fourier coefficients are nonzero at every weight**. Moreover,
\[
t_n=1-\frac1{2n}+O(n^{-2}),\quad
u_n=\frac45+\frac8{25n}+O(n^{-2}),\quad
K_n=\frac{32}{7}n+\frac{491}{98}+O(n^{-1})
\]
as \(n\to\infty\). For example, \(K_0=5.5924308075\ldots\) and \(K_1=9.8926635567\ldots\).

## Assumptions and scope
The Haar measure is normalized to one. The character convention is \(\chi_m(\operatorname{diag}(e^{i\theta},e^{-i\theta}))=\sin((m+1)\theta)/\sin\theta\), with continuous extension at \(\sin\theta=0\). These characters form an orthonormal family in the central subspace of \(L^2(SU(2))\). The coefficient triple is unrestricted and complex. The result gives the fourth-power optimal ratio, rather than its fourth root. It does not cover noncentral matrix coefficients or arbitrary longer character packets.

## Proof
**1. Exact Clebsch--Gordan expansion.** The tensor-product rule reads
\[
\chi_j\chi_k=\sum_{r=0}^{\min(j,k)}\chi_{j+k-2r}.
\]
For \(f=a\chi_n+b\chi_{n+1}+c\chi_{n+2}\), the even-index coefficients in the character expansion of \(f^2\) are \(a^2+b^2+c^2\) once, \(a^2+b^2+c^2+2ac\) exactly \(n\) times, \(b^2+c^2+2ac\) once, and \(c^2\) once. The odd-index coefficients are \(2b(a+c)\) exactly \(n+1\) times and \(2bc\) once. Character orthogonality gives, for every \(n\ge0\),
\[
\begin{aligned}
\|f\|_4^4={}&|a^2+b^2+c^2|^2
+n|a^2+b^2+c^2+2ac|^2\\
&+|b^2+c^2+2ac|^2+|c|^4
+4(n+1)|b(a+c)|^2+4|bc|^2.
\end{aligned}
\tag{1}
\]
The count remains valid at \(n=0\) (the repeated even interval is empty).

**2. Reduction to positive coefficients.** Each character-product multiplicity in (1) is nonnegative. Applying the triangle inequality separately to each coefficient of \(f^2\) shows that replacing \((a,b,c)\) with \((|a|,|b|,|c|)\) never reduces the fourth moment. Thus the supremum can be taken over real nonnegative amplitudes. For \(c>0\), homogeneity permits the parametrization \((a,b,c)=\zeta(t,\sqrt u,1)\) with \(t,u\ge0\). The resulting ratio is
\[
F_n(t,u)=\frac{P_n(t,u)}{(1+t^2+u)^2},
\]
\[
\begin{aligned}
P_n(t,u)={}&(1+t^2+u)^2+n(1+t^2+u+2t)^2
+(1+u+2t)^2+1\\
&+4(n+1)u(t+1)^2+4u.
\end{aligned}
\tag{2}
\]
The boundary case \(c=0\) is obtained by continuous limits \(t\to\infty\) and does not need a separate maximizer assumption.

**3. The strictly maximizing middle coefficient.** Writing \(P_n=\alpha u^2+A u+C\) and \(B=1+t^2\), with \(\alpha=n+2\), gives
\[
\frac{\partial F_n}{\partial u}=
\frac{(A-2\alpha B)(u_n(t)-u)}{(u+B)^3},
\]
where
\[
u_n(t)=\frac{(t+1)(2nt^3+2n+2t^3+4t^2-t+3)}
{2nt^2+6nt+2n+t^2+6t+4}
\]
and \(A-2\alpha B=2(2nt^2+6nt+2n+t^2+6t+4)>0\). The numerator of \(u_n(t)\) is positive for \(t\ge0\), because \(4t^2-t+3>0\) and all remaining terms are nonnegative. Hence \(u_n(t)\) is the unique global maximizer in \(u\ge0\) for each fixed \(t\). Direct cancellation yields \(F_n(t,u_n(t))=R_n(t)\), with the explicit numerator and denominator above.

**4. Unique global outer-coefficient ratio.** Differentiating the rational expression gives the exact identity
\[
R_n'(t)=\frac{-4(t+1)(2nt^2+6nt+2n+t^2+6t+4)H_n(t)}{D_n(t)^2}.
\tag{3}
\]
For each integer \(n\ge0\), \(H_n(0)=-(8n^2+21n+13)<0\), \(H_n(1)=16n+23>0\), and \(H_n\) has exactly one positive root by Descartes' rule of signs: its coefficient signs are \((+,+,+,-)\) for \(n=0\) and \((+,+,-,-)\) for every \(n\ge1\). Thus \(R_n\) increases strictly until \(t_n\in(0,1)\) and decreases strictly afterward. This proves the sharp value, including the boundary cases \(a=0\) and \(c=0\).

**5. Exact complex equality cases.** At the real maximizer, \(a,b,c\) have strictly positive magnitudes. Equality in the replacement-by-moduli step forces \(a^2,b^2,c^2\) to have a common phase because of the first squared term of (1), and forces \(a,c\) to share the same phase because \(|a+c|=|a|+|c|\). Hence \(a,b,c\) share a global phase and the sign of \(b\) is free. Both allowed signs attain equality, proving the complete classification.

**6. High-weight expansion.** Divide \(H_n\) by \(8n^2\). Its limiting polynomial is \((t+1)^2(t-1)\), so the unique positive root tends to one. Expanding \(H_n(1-\delta/n)\), the coefficient of \(n\) vanishes precisely at \(\delta=1/2\). Substitution into the explicit formulas for \(u_n(t)\) and \(R_n(t)\) gives the stated asymptotic expansions. The coefficient \(491/98\) is the finite-weight correction to the leading \(32n/7\) term.

## Verification
The included `check.py` verifies the derivative and reduction identities symbolically in \(n,t,u\), compares the Clebsch--Gordan expansion against an independent monomial/Catalan semicircle-moment calculation for randomized complex coefficients in degrees \(0\) through \(8\), and checks representative cubic roots and attained norms through weight \(100\). Run `python3 check.py` from this directory; expected output is recorded in `checks.txt`. These finite checks support but do not replace the universal proof above.

## Relationship to prior work
The general compact-Lie-group Fourier-multiplier framework of Cardona--Ruzhansky (2021) treats boundedness from symbol conditions, not these sharp finite central character-packet constants. Frank (2022) studies coherent-state transforms and sharp inequalities for weighted holomorphic realizations, whose observables differ from central Haar fourth moments of sums of irreducible characters. A published high-weight parity-localization result for fixed sparse \(SU(2)\) packets identifies the leading parity-controlled asymptotic; the present claim instead determines **the exact finite-weight algebraic constant and all equality cases for every adjacent triple**, together with its next asymptotic term. The two-character exact problem and abelian consecutive-character problems do not dominate this nonabelian three-character optimization.

## Limitations
The optimization is for three consecutive central irreducible characters only; no exact formula is asserted for longer packets or noncentral matrix coefficient spaces. The leading high-weight parity phenomenon is previously documented; priority for the present finite-weight algebraic formula is assessed from accessible literature rather than independently established by an external mathematical audit. The full text of a relevant public high-weight record could not be fetched from its repository at review time; its published summary was compared. The numeric values are illustrations and cannot certify an all-weight inequality on their own.

## References
1. D. Cardona and M. Ruzhansky, *Fourier multipliers for Triebel--Lizorkin spaces on compact Lie groups*, arXiv:2101.12314, initially public 2021-01-28, https://arxiv.org/abs/2101.12314.
2. R. L. Frank, *Sharp inequalities for coherent states and their optimizers*, arXiv:2210.14798, initially public 2022-10-26, https://arxiv.org/abs/2210.14798.
3. *High-weight parity localization of central fourth moments on \(SU(2)\)*, published mathematical-result record, 2026; bibliographic access limited to its searchable summary.
4. The standard Weyl character formula, Clebsch--Gordan tensor-product rule, and Schur orthogonality for \(SU(2)\), as used explicitly in the proof.
