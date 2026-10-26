# Arithmetic phase locking in sharp fourth moments of adjacent dual symmetric-power characters of \(SU(3)\)

## Finding
Let \(G=SU(3)\) have probability-normalized Haar measure and, for integers \(r\geq1\), let \(\chi_r(g)=\operatorname{tr}(\operatorname{Sym}^r g)\) be the ordinary (dimension-unnormalized) irreducible character. For \(n\geq1\) and \((a,b)\neq(0,0)\), define
\[
F(g)=a\chi_n(g)+b\overline{\chi_{n+1}(g)},\quad
Q_n(a,b)=\frac{\int_G|F(g)|^4\,dg}{(|a|^2+|b|^2)^2},\quad
\delta_n=\mathbf1_{n\equiv1\pmod3}.
\]
The exact character-moment identity, for every \(a,b\in\mathbb C\), is
\[
\begin{aligned}
\int_G|F|^4\,dg={}&(n+1)|a|^4+(n+2)|b|^4+4(n+1)|ab|^2\\
&+\delta_n\left[4(|a|^2+|b|^2)\operatorname{Re}(a\overline b)
+2\operatorname{Re}\big((a\overline b)^2\big)\right].
\end{aligned}
\]
Write \(L_n=\inf Q_n(a,b)\) and \(U_n=\sup Q_n(a,b)\), with both extrema over nonzero pairs.

If \(n\not\equiv1\pmod3\), the exact sharp endpoints are
\[
\boxed{L_n=n+1,\qquad U_n=n+2+\frac{n^2}{2n+1}.}
\]
Equality at the lower endpoint holds exactly when \(b=0\); equality at the upper endpoint holds exactly when \(|a|^2:|b|^2=n:(n+1)\), with unrestricted relative phase.

If \(n\equiv1\pmod3\), put, for \(t>0\),
\[
R_n^{\pm}(t)=\frac{(n+1)t^4+(n+2)+(4n+6)t^2\pm4t(1+t^2)}{(1+t^2)^2}.
\]
Let \(t_{n,+}\in(0,1)\) and \(t_{n,-}\in(1,\infty)\) be the unique roots in the indicated intervals of
\[
\begin{aligned}
t^4+(n+2)t^3-(n+1)t-1&=0&&\text{(upper)},\\
t^4-(n+2)t^3+(n+1)t-1&=0&&\text{(lower)}.
\end{aligned}
\]
Then the sharp endpoints and **all** equality cases are
\[
\boxed{U_n=R_n^+(t_{n,+}),\quad a/b=t_{n,+}>0,}
\qquad
\boxed{L_n=R_n^-(t_{n,-}),\quad a/b=-t_{n,-}<0.}
\]
The equality descriptions are invariant under arbitrary common nonzero complex scaling. Thus the upper optimizer is phase-aligned, while the lower optimizer is phase-opposed, and neither is supported on one character.

The norm displays a persistent arithmetic oscillation:
\[
\boxed{U_n=\frac32n+\frac74+\frac52\delta_n+\frac{1}{8n}+O(n^{-2})}
\qquad (n\to\infty).
\]
For \(n\equiv1\pmod3\), also \(L_n=n+1-2/(n+2)+O(n^{-3})\). In particular,
\[
\boxed{U_{3k+1}>U_{3k+2}\quad\text{for every integer }k\geq0,}
\]
so the optimal fourth-moment amplification is not monotone in the symmetric-power degree.

## Assumptions and scope
All integrals are over compact \(SU(3)\), with total Haar mass one. The symbol \(\operatorname{Sym}^r\) denotes the \(r\)-th symmetric power of the defining three-dimensional complex representation, and \(\chi_r\) is **not** divided by its dimension. Complex conjugation is pointwise conjugation of a character. All statements hold for every integer \(n\geq1\), every nonzero complex coefficient pair, and the indicated limits through all positive integers. Orthogonality of the two distinct irreducible characters gives \(\int_G|F|^2\,dg=|a|^2+|b|^2\), so \(Q_n\) is precisely the fourth power of the sharp \(L^2\)-to-\(L^4\) quotient on this two-dimensional character space.

## Proof
**1. Three universal quadratic products.** On \(SU(3)\), identify Schur partitions differing by a complete column of height three, and write a two-row partition \((u,v,0)\) as the highest-weight character with Dynkin labels \((u-v,v)\). Pieri's rule gives, multiplicity-freely,
\[
\chi_r^2=\sum_{j=0}^{r}\chi_{(2r-2j,j)}.
\]
Schur orthogonality therefore gives \(\int_G|\chi_r|^4\,dg=r+1\). Likewise, \(\chi_n\chi_m\), with \(m=n+1\), has exactly \(n+1\) distinct Pieri components, whence
\[
\int_G|\chi_n\chi_m|^2\,dg=n+1.
\]

**2. Three mixed moments and ternary selection.** The nontrivial scalar central matrices \(\omega I\), where \(\omega^3=1\), multiply \(\chi_r\) by \(\omega^r\). Thus the moments
\[
E=\int_G\chi_n^2\chi_m\overline{\chi_n}\,dg,\qquad
E'=\int_G\chi_m^2\chi_n\overline{\chi_m}\,dg,\qquad
D=\int_G\chi_n^2\chi_m^2\,dg
\]
vanish unless \(n+m\equiv0\pmod3\). Since \(m=n+1\), this occurs exactly when \(n\equiv1\pmod3\).

In that case set \(k=(n+m)/3=(2n+1)/3\), an integer. The only polynomial \(GL(3)\)-partition of total degree \(2n+m\) restricting to \(\chi_n\) on \(SU(3)\) is \((n+k,k,k)\). In the Pieri expansion of \(\chi_n^2\chi_m\), a precursor \((2n-j,j,0)\) can extend by a horizontal \(m\)-strip to that partition exactly when \(j=k\). The inequalities \(k\le n\) and \(2k\ge n\) hold for every \(n\ge1\), so this precursor exists, with multiplicity one. Hence \(E=1\). Interchanging \(n,m\) gives \(E'=1\), since \(k\le m\) and \(2k\ge m\).

For \(D\), an invariant in \(\chi_n^2\chi_m^2\) pairs one Pieri summand of \(\chi_n^2\) with the dual of a Pieri summand of \(\chi_m^2\). A summand with Dynkin labels \((2n-2j,j)\) is dual to one with labels \((j,2n-2j)\). Thus the unique possible pair has
\[
j=\frac{4n-2m}{3}=\frac{2n-2}{3},\qquad
\ell=\frac{4m-2n}{3}=\frac{2n+4}{3}.
\]
Both indices are integers and satisfy \(0\le j\le n\), \(0\le\ell\le m\) precisely in the present congruence class; each Pieri summand occurs once. Consequently \(D=1\). Expanding \(F^2\overline F^2\) using these six character moments gives exactly the stated quartic identity.

**3. Phase optimization.** Homogeneity permits \(|a|^2+|b|^2=1\). Write \(u=|a|^2\), \(v=1-u\), \(r=\sqrt{uv}\), and \(c=\cos(\arg(a\overline b))\) when \(ab\ne0\). For \(\delta_n=1\), the phase-dependent part is
\[
4rc+2r^2(2c^2-1).
\]
Its derivative in \(c\in[-1,1]\) equals \(4r(1+2rc)\ge0\), because \(r\le1/2\). Therefore the maximum is attained exactly at \(c=1\), and the minimum exactly at \(c=-1\) for nonzero \(a,b\). The resulting magnitude objectives are
\[
q_\pm(u)=n+2+2(n+1)u-(2n+3)u^2\pm4\sqrt{u(1-u)}.
\]
For \(\delta_n=0\), the phase term disappears and the objective reduces to the strictly concave quadratic \(n+2+2nu-(2n+1)u^2\), whose maximum is at \(u=n/(2n+1)\) and whose minimum is the smaller endpoint value \(n+1\).

**4. Unique resonant extremizers.** The second derivative of \(q_+\) is
\[
q_+''(u)=-2(2n+3)-[u(1-u)]^{-3/2}<0.
\]
Its first derivative runs from \(+\infty\) to \(-\infty\) and equals \(-1\) at \(u=1/2\), giving one maximizer in \((0,1/2)\). For the minimum, the symmetry identity \(q_-(u)-q_-(1-u)=1-2u\) puts every global minimizer in \([1/2,1]\). On \((1/2,1)\),
\[
q_-''(u)=-2(2n+3)+[u(1-u)]^{-3/2}
\]
increases strictly from \(2-4n<0\) to \(+\infty\). Since \(q_-'(1/2)=-1\) and \(q_-'(u)\to+\infty\) as \(u\uparrow1\), exactly one minimizing stationary point lies in \((1/2,1)\). Substitution \(t=\sqrt{u/(1-u)}\) yields \(R_n^+\) and \(R_n^-\); differentiating gives precisely the two displayed quartics. Strictness in the phase and magnitude steps proves every equality case.

**5. Large degree and degree reversal.** For the nonresonant class, polynomial division gives the exact formula \(U_n=3n/2+7/4+1/[4(2n+1)]\). For the resonant class, write \(u=1/2+\eta\). Taylor expansion at the unique maximizer gives
\[
q_+(u)=\frac{3n}{2}+\frac{17}{4}-\eta-(2n+7)\eta^2+O(\eta^4),\qquad
\eta=-\frac1{4n}+O(n^{-2}),
\]
therefore \(U_n=3n/2+17/4+1/(8n)+O(n^{-2})\). For the minimum put \(u=1-\varepsilon\); its stationary equation gives \(\varepsilon=(n+2)^{-2}+O(n^{-4})\), and substitution into \(q_-\) gives \(L_n=n+1-2/(n+2)+O(n^{-3})\).

Finally, when \(n\equiv1\pmod3\), evaluating \(q_+\) at \(u=1/2\) yields \(U_n\ge3n/2+17/4\). The exact nonresonant formula at \(n+1\) gives \(U_{n+1}=3n/2+13/4+1/[4(2n+3)]\), strictly smaller. This proves every asserted degree reversal.

## Verification
Run `python3 verify.py` alongside this document with Python 3 and no third-party packages. The checker separately expands complete homogeneous characters on the \(SU(3)\) maximal torus and applies the Weyl integration formula, extracting the constant term after multiplication by \(\prod_{i<j}(1-x_i/x_j)(1-x_j/x_i)/6\). It verifies all six required moments with **exact integer arithmetic** for degrees \(1\le n\le9\), independently of the Pieri derivation. It also checks quartic stationarity, sharp two-sided inequalities on deterministic phase/magnitude grids, and the degree reversal for the first seventeen resonant degrees. The recorded run returned `ALL_CHECKS_PASSED assertions=3148`. This finite checking corroborates, but does not replace, the all-degree argument above.

## Relationship to prior work
General integration of symmetric functions and unitary characters via Schur orthogonality, Pieri decomposition and Haar moment calculus predates this result. Issa–Abbas–Mourad provide integral representations for normalized symmetric-power traces over Euclidean spheres (not this Haar fourth-norm optimization). Lee–Oh compute characteristic-polynomial autocorrelations for specified unitary subgroups using branching rules (not the present two-character extremal problem). Vleeshouwers–Gritsev treat broad unitary symmetric-polynomial integrals and give Schur and Pieri machinery, but the inspected sections do not state the adjacent conjugate-power \(SU(3)\) norm endpoints or the arithmetic phase-locking classification. Collins surveys general Weingarten moment formulas, which provide a possible route to calculate the raw moments but not the optimized statements. The closest compared equal-degree character-pair result concerns \(\chi_n\) and \(\overline{\chi_n}\); its mixed moments do not imply those between unequal adjacent powers, and its resonance occurs in a different congruence class. The genuinely new claim here is the full adjacent-degree norm and equality classification, including nonmonotonicity; not Pieri's rule itself. Historical priority has not been independently certified.

## Limitations
The theorem covers exactly the two-character family \(\operatorname{span}\{\chi_n,\overline{\chi_{n+1}}\}\) on \(SU(3)\), not arbitrary pairs of character degrees or other compact groups. It concerns fourth moments, not all even exponents. The explicit optimizer formulas are algebraic rather than elementary radicals; no claim of uniqueness across the mathematical literature is made. The computation checks only finitely many degrees. No independent mathematical audit or validation has been performed.

## References
1. H. Issa, H. Abbas, B. Mourad, *On an integral representation of the normalized trace of the k-th symmetric tensor power of matrices and some applications*, arXiv:2106.01486v1 (first public 2021-06-02), Sections 2 and 4. https://arxiv.org/abs/2106.01486
2. K.-H. Lee, S.-J. Oh, *Auto-correlation functions for unitary groups*, arXiv:2110.00505, Sections 1 and 3. https://arxiv.org/abs/2110.00505
3. W. L. Vleeshouwers, V. Gritsev, *Unitary matrix integrals, symmetric polynomials, and long-range random walks*, arXiv:2209.06538, Sections 2 and Appendix A (Pieri). https://arxiv.org/abs/2209.06538
4. B. Collins, *Moment methods on compact groups: Weingarten calculus and its applications*, Proceedings of the ICM 2022, DOI:10.4171/ICM2022/114, Sections 1–2.5. https://doi.org/10.4171/ICM2022/114
5. I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., Oxford University Press, 1995, Chapter I (Schur functions and Pieri formulas).
