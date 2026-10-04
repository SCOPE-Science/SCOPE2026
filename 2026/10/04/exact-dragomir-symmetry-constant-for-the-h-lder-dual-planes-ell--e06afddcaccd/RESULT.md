# Exact Dragomir-symmetry constant for the Hölder-dual planes \(\ell_3^2\) and \(\ell_{3/2}^2\)
## Finding
For the real Banach planes \(X_p=\ell_p^2\), define
\[
\varepsilon_D(X_p)=\inf\left\{\varepsilon\in[0,1):\ x\perp_B y\Longrightarrow y\perp_D^\varepsilon x\text{ for all }x,y\in X_p\right\},
\]
where
\[
z\perp_D^\varepsilon w\quad\Longleftrightarrow\quad
\|z+\lambda w\|\ge \sqrt{1-\varepsilon^2}\,\|z\|\quad\text{for every }\lambda\in\mathbb R.
\]
For the Hölder-conjugate exponents \(p\in\{3,3/2\}\),
\[
\boxed{\ \varepsilon_D(\ell_p^2)=\sqrt{1-\left(\frac{27}{17+7\sqrt7}\right)^{2/3}}\ }
\]
and numerically this is \(0.408781256846\ldots\). The optimum is attained.

## Assumptions and scope
All spaces and scalars are real. Birkhoff--James orthogonality means
\[
x\perp_B y\quad\Longleftrightarrow\quad \|x+\lambda y\|\ge\|x\|\quad\text{for every }\lambda\in\mathbb R.
\]
The approximation is the Dragomir/Chmieliński version \(\perp_D^\varepsilon\), not the distinct Chmieliński approximation \(\perp_B^\varepsilon\). The result concerns the optimal single global constant valid for every ordered Birkhoff--James orthogonal pair. It does not assert a formula for general \(p\), higher dimensions, or complex scalars.

## Proof
It is enough to consider nonzero unit vectors. Coordinate sign changes and the coordinate swap are linear isometries of \(\ell_p^2\), so write
\[
x=(a,b),\qquad a,b\ge0,\qquad a^p+b^p=1.
\]
Let \(q=p/(p-1)\). Smoothness of \(\ell_p^2\) gives the unique norming functional
\[
j(x)=(a^{p-1},b^{p-1})\in\ell_q^2.
\]
Hence \(x\perp_B y\) exactly when \(a^{p-1}y_1+b^{p-1}y_2=0\). A unit vector in this one-dimensional kernel is, up to sign,
\[
y=\frac{(b^{p-1},-a^{p-1})}{\left(a^{p(p-1)}+b^{p(p-1)}\right)^{1/p}}.
\]

For the reverse approximate orthogonality, a norm-one functional that annihilates \(x\) is unique up to sign and equals
\[
g=\frac{(b,-a)}{\left(a^q+b^q\right)^{1/q}}.
\]
The standard functional characterization of Dragomir approximate Birkhoff--James orthogonality says that, for unit \(y\),
\[
y\perp_D^\varepsilon x
\quad\Longleftrightarrow\quad
\text{there is }h\in S_{(\ell_p^2)^*}\text{ with }h(x)=0\text{ and }|h(y)|\ge\sqrt{1-\varepsilon^2}.
\]
Since the annihilator of \(x\) is one-dimensional, the best possible reverse threshold for this pair is therefore exactly \(|g(y)|\). Direct substitution gives
\[
|g(y)|=
\frac{1}{\left(a^q+b^q\right)^{1/q}
\left(a^{p(p-1)}+b^{p(p-1)}\right)^{1/p}}.
\]
Put \(u=a^p\) and \(1-u=b^p\). Then
\[
c_p(u):=|g(y)|=
\frac{1}{
\left(u^{1/(p-1)}+(1-u)^{1/(p-1)}\right)^{(p-1)/p}
\left(u^{p-1}+(1-u)^{p-1}\right)^{1/p}}.
\]
Thus
\[
\varepsilon_D(\ell_p^2)=\sqrt{1-\left(\inf_{0\le u\le1}c_p(u)\right)^2}.
\]

For both \(p=3\) and \(p=3/2\), the two factors above are interchanged by Hölder conjugacy, and the same scalar function results. With
\[
w=\sqrt{u(1-u)}\in[0,1/2],
\]
one has
\[
c_p(u)^{-3}=\left(\sqrt u+\sqrt{1-u}\right)^2\left(u^2+(1-u)^2\right)
=(1+2w)(1-2w^2)=:F(w).
\]
Differentiate:
\[
F'(w)=2-4w-12w^2.
\]
The only critical point in \([0,1/2]\) is
\[
w_*=\frac{\sqrt7-1}{6}.
\]
The derivative is positive before \(w_*\) and negative after it, while \(F(0)=F(1/2)=1\). Therefore \(w_*\) is the unique global maximizer. Substitution yields
\[
F(w_*)=\frac{17+7\sqrt7}{27}.
\]
Consequently
\[
\inf c_p=\left(\frac{27}{17+7\sqrt7}\right)^{1/3},
\]
and hence
\[
\varepsilon_D(\ell_p^2)
=\sqrt{1-\left(\frac{27}{17+7\sqrt7}\right)^{2/3}}
\qquad\text{for }p\in\{3,3/2\}.
\]
Because \(w_*\in(0,1/2)\), there are \(u\in(0,1)\) with \(\sqrt{u(1-u)}=w_*\); the corresponding \(x\) and \(y\) above attain equality.

## Verification
The proof is an exact one-variable maximization, not a finite search. A standalone checker, `verify_dragomir_constant.py`, verifies the radical identities at high precision and independently samples the scalar function on a dense grid as a numerical stress test. The grid is only corroborative; correctness of the global maximum follows from the displayed derivative sign argument.

At the two symmetric boundary configurations \(u=0\) and \(u=1/2\), one gets \(F=1\) and therefore zero reverse defect. The worst defect is genuinely interior, which provides a useful check against accidentally replacing the global optimum by an axis or diagonal calculation.

## Relationship to prior work
Chmieliński, Khurana and Sain introduced the global terminology of D-approximate symmetry and proved that every finite-dimensional Banach space has some global D-approximate symmetry parameter strictly below \(1\). Their theorem is qualitative: it establishes existence but does not compute the optimal constant for \(\ell_p^2\). Their functional characterization of \(\perp_D^\varepsilon\) is the critical input used above.

The earlier work of Chmieliński and Wójcik concerns a different approximate orthogonality, called C-approximate symmetry in the later paper. It therefore does not supply the D-constant computed here. Bose, Roy and Sain later classified exact left- and right-symmetric points in classical sequence spaces, including \(\ell_p\), but their inspected full text does not study approximate symmetry or an optimal D-parameter. A 2025 paper on strong \(\varepsilon\)-symmetry and minimal widths uses another quantitative framework; its accessible abstract does not state the D-constant above.

The exact radical was also searched directly, together with aliases involving Dragomir approximate orthogonality, global D-symmetry, \(\ell_3^2\), and Hölder-dual \(\ell_p\) planes. No inspected statement implied the result.

## Limitations
No claim is made that the displayed value is new under every possible historical notation. The full text of the 2018 C-approximate-symmetry paper was not available in the lawful sources inspected here; its relation to the present D-notion is instead documented explicitly by the 2020 paper, which distinguishes the two definitions. The 2025 minimal-width paper was available only at abstract/metadata level during this review and remains a residual terminology risk, although its stated invariant is different.

The result is restricted to real two-dimensional \(\ell_p\) at the conjugate exponents \(3\) and \(3/2\). The same reduction gives a one-variable optimization for other \(p\), but no general closed form is asserted.

## References
1. J. Chmieliński, D. Khurana, D. Sain, *Local approximate symmetry of Birkhoff-James orthogonality in normed linear spaces*, arXiv:2012.08162, first public 15 December 2020; later published in *Results in Mathematics*.
2. J. Chmieliński, P. Wójcik, *Approximate symmetry of Birkhoff orthogonality*, *Journal of Mathematical Analysis and Applications* 461 (2018), 625--640, DOI: 10.1016/j.jmaa.2018.01.031.
3. B. Bose, S. Roy, D. Sain, *Birkhoff-James Orthogonality and Its Local Symmetry in Some Sequence Spaces*, arXiv:2205.11586, first public 23 May 2022.
4. C. He, H. Martini, S. Wu, *Minimal widths and orthogonality types*, *Acta Mathematica Scientia* 45 (2025), 27--39, DOI: 10.1007/s10473-025-0103-0.
