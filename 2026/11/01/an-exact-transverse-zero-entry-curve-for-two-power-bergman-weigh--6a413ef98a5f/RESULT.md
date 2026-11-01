# An exact transverse zero-entry curve for two-power Bergman weights

## Finding

Let the analytic weighted Bergman space on the unit disk have measure
\[
|z|^{2s}(1-|z|^2)^\alpha\,dA(z)/\pi,
\]
where \(s>0\) and \(\alpha>-1\). Its reproducing kernel depends on \(u=z\overline w\), and its scalar zeros are the zeros with \(|u|<1\).

There is \(\varepsilon>0\) and a unique real-analytic function \(\alpha_c\) on \((1-\varepsilon,1+\varepsilon)\), with \(\alpha_c(1)=4\), such that, for \(|s-1|<\varepsilon\) and \(|\alpha-4|<\varepsilon\):

* If \(\alpha\leq\alpha_c(s)\), the reproducing kernel has **no zero** on the product of two open disks.
* If \(\alpha>\alpha_c(s)\), it has **exactly two distinct scalar product zeros** \(u_+(s,\alpha)\) and \(\overline{u_+(s,\alpha)}\) in \(|u|<1\); both are simple.
* At equality, the two roots lie on \(|u|=1\) and therefore are not attained by \(u=z\overline w\) with \(z,w\) in the open disk.

The boundary is transverse and has the **exact tangent**
\[
\boxed{\alpha_c'(1)=-\frac{49\sqrt3}{60\pi}},\qquad
\alpha_c(s)=4-\frac{49\sqrt3}{60\pi}(s-1)+O((s-1)^2).
\]
The two roots crossing the unit circle at the base parameters converge to \(e^{\pm i\pi/3}\), not to the negative real axis. The assertion is local in the two real weight parameters; it makes no global classification claim.

## Assumptions and scope

The disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and area is normalized by \(\pi^{-1}\). For \(s>0\), \(\alpha>-1\), set
\[
\|f\|_{s,\alpha}^2=\frac1\pi\int_{\mathbb D}|f(z)|^2|z|^{2s}(1-|z|^2)^\alpha\,dA(z).
\]
Every point evaluation is bounded; monomials are complete and orthogonal. Write \(K_{s,\alpha}(z,w)=\mathcal K_{s,\alpha}(z\overline w)\). A **scalar product zero** means a distinct value \(u\) in the unit disk for which \(\mathcal K_{s,\alpha}(u)=0\). Each such \(u\) corresponds to infinitely many pairs \((z,w)\); the count is not a count of pairs.

## Proof

**1. Exact moment and holomorphic zero reduction.** Radial integration gives, for every integer \(n\ge0\),
\[
\|z^n\|_{s,\alpha}^2
=B(n+s+1,\alpha+1),
\]
so that
\[
\mathcal K_{s,\alpha}(u)=
\sum_{n=0}^\infty
\frac{u^n}{B(n+s+1,\alpha+1)}
=\frac{\Gamma(s+\alpha+2)}{\Gamma(s+1)\Gamma(\alpha+1)}
{}_2F_1(1,s+\alpha+2;s+1;u).
\]
Euler's hypergeometric transformation followed by Euler's integral for \(s>0\) yields
\[
\mathcal K_{s,\alpha}(u)=
\frac{\Gamma(s+\alpha+2)}{\Gamma(s+1)\Gamma(\alpha+1)}
(1-u)^{-\alpha-2}G_{s,\alpha}(u),
\]
where
\[
G_{s,\alpha}(u)={}_2F_1(-\alpha-1,s;s+1;u)
=s\int_0^1t^{s-1}(1-ut)^{\alpha+1}\,dt.
\]
For \(|u|<1\), the prefactors are nonzero. Thus the kernel and \(G_{s,\alpha}\) have exactly the same scalar zeros there. Powers in this integral take the branch continuous from \(u=0\); for \(|u|\le1\), \(1-ut\) lies in the closed right half-plane, with a possible zero only at \((u,t)=(1,1)\).

**2. The critical unperturbed configuration.** At \((s,\alpha)=(1,4)\), direct integration gives
\[
G_{1,4}(u)=\int_0^1(1-ut)^5dt
=\frac{1-(1-u)^6}{6u},
\]
with the removable value \(G_{1,4}(0)=1\). Its five zeros are exactly
\[
u_j=1-e^{2\pi i j/6},\quad j=1,2,3,4,5.
\]
Their moduli, in this order, are \(1,\sqrt3,2,\sqrt3,1\). All five zeros are simple. In particular, the only zeros in the *closed* unit disk are the conjugate boundary points
\[
u_0=e^{i\pi/3}=\frac{1+i\sqrt3}{2}
\quad\text{and}\quad\overline{u_0}.
\]
The boundary point \(u=1\) is not a zero: \(G_{1,4}(1)=1/6\).

**3. Exhaustion of all nearby zeros.** On a compact real neighborhood of \((1,4)\) with \(s>0\) and \(\alpha+1>0\), the defining integral for \(G\) depends continuously and uniformly on \((s,\alpha,u)\) for \(|u|\le1\); at \(u=1\) this follows from the positive exponent \(\alpha+1\) and dominated convergence. It is holomorphic in \(u\) in the open disk and across every unit-circle point other than \(1\). Choose disjoint small complex neighborhoods of \(u_0\) and \(\overline{u_0}\), not containing \(1\) or any other critical zero. The base function has a strictly positive modulus on the complementary compact portion of the closed disk. Uniform convergence keeps this portion zero-free for sufficiently small parameter perturbations. Rouché's theorem gives exactly one simple root in each chosen neighborhood, including any root just outside the circle. Denote the root near \(u_0\) by \(u_+(s,\alpha)\). Its conjugate is the other root, since all defining coefficients are real. The analytic implicit-function theorem makes \(u_+\) real-analytic in \((s,\alpha)\).

**4. Exact transverse derivatives.** At the critical root, direct differentiation of the polynomial integral gives
\[
(G_{1,4})'(u_0)=1.
\]
The parameter derivatives are
\[
\begin{aligned}
\partial_sG_{s,\alpha}(u_0)|_{(1,4)}
&=\int_0^1(1-u_0t)^5\log t\,dt\\
&=-\sum_{k=0}^{5}\binom5k\frac{(-u_0)^k}{(k+1)^2}
=-\frac{119}{360}+\frac{7\sqrt3}{45}i,
\\[3pt]
\partial_\alpha G_{s,\alpha}(u_0)|_{(1,4)}
&=\int_0^1(1-u_0t)^5\log(1-u_0t)\,dt\\
&=-\frac{\log(1-u_0)}{6u_0}
=\frac{\pi}{36}(\sqrt3+i).
\end{aligned}
\]
In the first derivative, the term from differentiating the leading factor \(s\) vanishes because \(G_{1,4}(u_0)=0\). The second derivative uses \((1-u_0)^6=1\) and the principal logarithm \(\log(1-u_0)=-i\pi/3\).

Differentiating the identity \(G_{s,\alpha}(u_+(s,\alpha))=0\) gives \(\partial_su_+=-\partial_sG\) and \(\partial_\alpha u_+=-\partial_\alpha G\) at the critical point. For the real-analytic function
\[
\Phi(s,\alpha)=\log|u_+(s,\alpha)|,
\]
we therefore obtain
\[
\partial_s\Phi(1,4)=-\frac{49}{720},\qquad
\partial_\alpha\Phi(1,4)=-\frac{\pi\sqrt3}{36}<0.
\]
The real implicit-function theorem supplies the unique local curve \(\Phi(s,\alpha_c(s))=0\). Its derivative is
\[
\alpha_c'(1)=-\frac{\partial_s\Phi(1,4)}{\partial_\alpha\Phi(1,4)}
=-\frac{49\sqrt3}{60\pi}.
\]
After shrinking the neighborhood, \(\partial_\alpha\Phi<0\) throughout. Hence \(\Phi>0\) below the curve (both simple roots outside the disk), \(\Phi=0\) on it (both on the circle), and \(\Phi<0\) above it (both inside). Step 3 excludes every other scalar zero. This proves all assertions.

## Verification

A standalone `CHECKER.py` performs exact symbolic calculations of the polynomial, its five critical zeros, the first derivatives and the tangent, independently evaluates the defining integral against the Gauss hypergeometric function, and numerically solves the two-real-equation unit-circle crossing near two nearby parameter values. It also checks that moving the boundary exponent across the computed curve moves a conjugate root pair in the predicted direction. Execute `python CHECKER.py` after installing the dependencies in `REQUIREMENTS.txt`. Finite checks support the identities; the neighborhood-wide result is justified by the analytic proof above.

## Relationship to prior work

The 2017 work of Perälä studies zero sets of radial weighted Bergman kernels, establishes finite zero counts for each radial kernel section, and constructs weights with arbitrarily many zeros. It supplies motivation but does not give this two-parameter local phase curve. Jacobson's general meromorphic-weight transformation (2013 preprint; 2017 journal) includes the integer origin factor \(|z|^2\) and thus contains the *unperturbed kernel-reduction method*, not the fractional-origin perturbation nor the exact transverse tangent. Miña-Díaz (2022 preprint, 2023 journal) gives representation formulas for weights built from powers of Blaschke factors against the **unweighted** area measure; those formulas do not cover the simultaneous nonzero boundary exponent used here. A previously established meromorphic punctured-disk classification for \(-1<\alpha<0\) concerns a disjoint exponent range and different zero-entry geometry. These distinctions are statements of coverage, not a claim that all possibly equivalent literature has been exhaustively ruled out.

## Limitations

The size of \(\varepsilon\) is not quantified. The result gives neither a global phase diagram nor any assertion outside a neighborhood of \((s,\alpha)=(1,4)\). The two zeros are *distinct scalar values* of \(z\overline w\), not isolated pairs of evaluation points. The result is analytically proved and has supplementary finite checks, but it has not received an independent mathematical audit. An earlier equivalent theorem stated in different hypergeometric or weighted-domain terminology remains a possible historical-priority risk.

## References

1. A. Perälä, *Vanishing Bergman kernels on the disk*, arXiv:1703.05976v1 (first posted March 17, 2017), especially Sections 1–3. https://arxiv.org/abs/1703.05976.
2. R. Jacobson, *Weighted Bergman kernel functions associated to meromorphic functions*, arXiv:1309.4800v1 (first posted September 18, 2013), especially Theorem 4 and Section 4. https://arxiv.org/abs/1309.4800.
3. E. Miña-Díaz, *A representation for the reproducing kernel of a weighted Bergman space*, arXiv:2212.08118 (first posted December 2022), especially Theorem 1.1. https://arxiv.org/abs/2212.08118.
