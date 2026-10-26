# Strict three-mode mixing and the sharp high-weight correction for quadratic Bergman fourth moments

## Finding

On the probability-weighted unit disk, consider the sharp degree-two Bergman embedding constant
\[
K_\beta=\max_{0\ne f\in\operatorname{span}\{1,z,z^2\}}
\frac{\int_{\mathbb D}|f(z)|^4\,d\mu_\alpha(z)}
{\left(\int_{\mathbb D}|f(z)|^2\,d\mu_\alpha(z)\right)^2},\qquad\beta=\alpha+2>1.
\]
Every extremizer uses **all three monomials** and the nonzero coefficient phases obey \(2\arg b=\arg a+\arg c\pmod{2\pi}\) for \(f(z)=a+bz+cz^2\). In particular, the normalized quadratic monomial is never extremal. Its moment is
\[
W_\beta=\frac{6\beta(\beta+1)}{(\beta+2)(\beta+3)},\qquad K_\beta>W_\beta.
\]
The sharp first high-weight correction is
\[
\boxed{K_\beta-W_\beta=\frac{48}{\beta^2}+o(\beta^{-2})\quad(\beta\to\infty).}
\]
For any choice of normalized extremizer \(\|f\|_2=1\), the normalized coefficient magnitudes \(A=|a|\), \(B=\sqrt{m_1}|b|\), and \(C=\sqrt{m_2}|c|\) satisfy
\[
\boxed{\beta A\longrightarrow\sqrt2,\qquad\beta B^2\longrightarrow4,\qquad C\longrightarrow1.}
\]
The asymptotics hold for every maximizing choice, with no assumption of uniqueness at finite weight.

## Assumptions and scope

For each real \(\alpha>-1\), the disk probability measure is \(d\mu_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha\,dA(z)/\pi\). Its radial moments are \(m_j=\int_{\mathbb D}|z|^{2j}\,d\mu_\alpha=j!\Gamma(\beta)/\Gamma(\beta+j)\), where \(\beta=\alpha+2>1\). A maximizing polynomial exists by compactness of the unit sphere in the three-dimensional coefficient Hilbert space. Complex coefficients are unrestricted; zero coefficients are permitted before optimization. All integrals use the same measure in their numerator and denominator.

## Proof

**1. Exact fourth-moment reduction.** Fourier orthogonality of the angular powers in \(f^2=a^2+2abz+(b^2+2ac)z^2+2bcz^3+c^2z^4\) gives
\[
\|f\|_4^4=|a|^4+4m_1|ab|^2+m_2|b^2+2ac|^2+4m_3|bc|^2+m_4|c|^4.
\]
Let \(A=|a|\), \(B=\sqrt{m_1}|b|\), \(C=\sqrt{m_2}|c|\), so \(\|f\|_2^2=A^2+B^2+C^2\). Define
\[
U=\frac{2\beta}{\beta+1},\qquad
V=\frac{3\beta}{\beta+2},\qquad
W=\frac{6\beta(\beta+1)}{(\beta+2)(\beta+3)}.
\]
When \(A^2+B^2+C^2=1\), the fourth moment is at most
\[
F_\beta(A,B,C)=A^4+4A^2B^2+UB^4+4A^2C^2+4VB^2C^2+WC^4+4\sqrt U\,ACB^2.
\]
The only phase-sensitive term is \(4m_2\operatorname{Re}(b^2\overline{ac})\). If the three coefficients are nonzero, equality in the displayed bound occurs if and only if \(b^2\overline{ac}\) is strictly positive real, equivalently \(2\arg b\equiv\arg a+\arg c\pmod{2\pi}\).

**2. No boundary maximizers.** We show the maximum of \(F_\beta\) over \(A,B,C\ge0\), \(A^2+B^2+C^2=1\), has \(ABC>0\). If \(A=0\) with \(B,C>0\), switching on a small positive \(A\), with normalization restored, gains a strictly positive term linear in \(A\), namely \(4\sqrt U ACB^2\), while all normalization losses are quadratic. The same holds with \(C=0\) and \(A,B>0\).

For the remaining edge \(B=0\), write \(z=C^2\in[0,1]\), \(A^2=1-z\), and switch on \(B^2=\varepsilon\) while multiplying \(A,C\) by \(\sqrt{1-\varepsilon}\). The right derivative at \(\varepsilon=0\) is
\[
4(1-z)+4Vz-2\big((1-z)^2+4z(1-z)+Wz^2\big)
=2\big((1-z)^2+2(V-1)z(1-z)+(2V-W)z^2\big)>0,
\]
where \(V>1\) and \(2V-W=12\beta/((\beta+2)(\beta+3))>0\). This covers the pure constant and pure quadratic endpoints as well. At the pure middle monomial, adding a small squared amplitude to the quadratic term gives derivative \(4V-2U>0\). Hence no boundary point maximizes, proving strict three-mode mixing and phase alignment. In particular \(K_\beta>W\) at every finite weight.

**3. Limiting deficit and localization.** As \(\beta\to\infty\), the coefficients tend to \((U,V,W)=(2,3,6)\). Let \(F_\infty\) be this limiting polynomial. With \(A^2+B^2+C^2=1\), direct expansion yields the **exact sum-of-squares identity**
\[
6-F_\infty=(2\sqrt2\,AC-B^2)^2+3B^4+8A^2B^2+5A^4.
\]
Its unique normalized zero is \((A,B,C)=(0,0,1)\). Thus every sequence of maximizers converges to that point, by compactness and uniform convergence. Set \(x=A\), \(y=B^2\), \(C=\sqrt{1-x^2-y}\). The exact excess relative to the pure quadratic value is
\[
\begin{aligned}
F_\beta-W={}&(4-2W)x^2+(4V-2W)y+(W-3)x^4\\
&+(2W-4V)x^2y+(W-4V+U)y^2
+4\sqrt U\,xy\sqrt{1-x^2-y}.
\end{aligned}
\]
Near the unique limiting optimizer, the sum-of-squares controls \(x^2+y^2\) from below by a positive constant times \(x^2+y^2\). Moreover the difference of the finite-weight excess and the limiting excess is bounded by \(O(\beta^{-1})(x^2+y)\), uniformly there: the coefficients are rational functions of \(\beta\), and the cross term differs by a factor \(O(\beta^{-1})\). Since an optimizer has \(F_\beta-W\ge0\), these two estimates give \(y=O(\beta^{-1})\) and \(x=O(\beta^{-1})\), hence \(\beta y\) and \(\beta x\) are bounded.

**4. Sharp scaled correction.** Put \(t=\beta x\ge0\) and \(s=\beta y\ge0\). Substituting into the exact excess and using the preceding bounds gives, uniformly on bounded \((t,s)\),
\[
\beta^2(F_\beta-W)=J(t,s)+o(1),\qquad
J(t,s)=24s-4s^2+4\sqrt2\,ts-8t^2.
\]
This quadratic has the exact completion-of-squares formula
\[
J(t,s)=48-3(s-4)^2-8\left(t-\frac{s}{2\sqrt2}\right)^2,
\]
with unique maximum \(48\) at \((t,s)=(\sqrt2,4)\), in the nonnegative quadrant. The normalized test profile \(A=\sqrt2/\beta\), \(B=2/\sqrt\beta\), \(C=\sqrt{1-A^2-B^2}\), valid for sufficiently large \(\beta\), gives \(\liminf\beta^2(K_\beta-W)\ge48\). Every maximizing subsequence has a convergent scaled subsequence, whose limit must achieve the same maximum and thus must equal \((\sqrt2,4)\). This proves the full limits and the stated sharp correction.

## Verification

The standalone script `verify.py` uses exact SymPy arithmetic to reconstruct radial moments and the fourth-moment identity, checks the boundary derivative, proves the limiting sum-of-squares polynomial identity and the exact quadratic completion, and compares independent angular Fourier expansions with the normalized formula for complex coefficient triples. Numerical multi-start optimization at six weights illustrates convergence; these finite experiments are not used as proof of the all-weight claims. Run `python verify.py` in an environment with Python 3, SymPy, NumPy, and SciPy. The observed output is in `verification_output.txt`.

## Relationship to prior work

Bayart, Brevig, Haimi, Ortega-Cerdà and Perfekt study contractive Bergman-space inequalities and related Hankel forms, including Carleman/Weissler-type estimates. Melentijević obtains sharp dilation hypercontractivity for weighted Bergman spaces. Neither inspected result states this degree-two **nondilated same-measure sharp fourth-moment excess**, the exclusion of every boundary coefficient profile, or the exact high-weight correction. General embedding estimates and dilation contractivity do not by themselves imply these coefficient-sensitive equalities. This comparison is based on the identified statements and material examined, not an exhaustive uniqueness guarantee.

## Limitations

The finite-weight constant \(K_\beta\) is defined by a compact maximization, not provided as an algebraic closed form. The finite-weight positive maximizing magnitude triple is not proved unique. The asymptotic has an \(o(\beta^{-2})\) remainder without an explicit uniform rate. The theorem applies only to the three-dimensional quadratic analytic subspace and the standard power-weighted disk; it makes no assertion about all-degree Bergman embeddings, other radial weights, or independently certified priority.

## References

1. F. Bayart, O. F. Brevig, A. Haimi, J. Ortega-Cerdà, K.-M. Perfekt, *Contractive inequalities for Bergman spaces and multiplicative Hankel forms*, arXiv:1701.06897, first version 24 January 2017.
2. P. Melentijević, *Hypercontractive inequalities for weighted Bergman spaces*, arXiv:2211.03655, first version 7 November 2022 (primary MSC 30H20).
