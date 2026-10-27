# Sharp anchored Bohr sets and coefficient-modulus rigidity for Drury–Arveson multipliers

## Finding
Fix a finite integer \(d\ge2\), or \(d=\infty\). Let \(H_d^2\) be the Drury–Arveson Hilbert space of analytic functions on the open complex \(\ell_2\)-unit ball \(\mathbb B_d\), with reproducing kernel \(K(z,w)=(1-\langle z,w\rangle)^{-1}\). Define the *anchored multiplier Bohr set* by
\[
\mathfrak B_{d,0}=\left\{x\in\mathbb B_d:\ \sum_{\alpha\ne0}|c_\alpha x^\alpha|\le1\quad\text{for every }\varphi(z)=\sum_\alpha c_\alpha z^\alpha\text{ with }\varphi(0)=0,\ \|M_\varphi\|\le1\right\}.
\]
Here finite-support multiindices are used in infinite dimensions. The anchored Bohr set is exactly
\[
\boxed{\mathfrak B_{d,0}=\{x\in\mathbb B_d:\ \|x\|_2\le1/\sqrt2\}.}
\]
Furthermore, at any \(x\) with \(\|x\|_2=1/\sqrt2\), set \(w_\alpha=\alpha!/|\alpha|!\), \(b_\alpha=(|\alpha|!/\alpha!)|x^\alpha|\) for \(\alpha\ne0\), and \(\mathcal M_x(\varphi)=\sum_{\alpha\ne0}|c_\alpha x^\alpha|\). Every contractive multiplier vanishing at the origin satisfies the **exact identity**
\[
\boxed{2(1-\mathcal M_x(\varphi))=(1-\|\varphi\|_{H_d^2}^2)+\sum_{\alpha\ne0}w_\alpha(|c_\alpha|-b_\alpha)^2.}
\]
Consequently \(\mathcal M_x(\varphi)=1\) if and only if \(|c_\alpha|=(|\alpha|!/\alpha!)|x^\alpha|\) for every \(\alpha\ne0\), within the contractive multiplier class. In particular the squared weighted coefficient-modulus distance to this profile is at most \(2(1-\mathcal M_x(\varphi))\). Boundary attainment occurs at **every** \(x\) on that sphere, by an explicit multiplier that is nonlinear in a directional coordinate.

## Assumptions and scope
The kernel normalization is \(K(z,w)=1/(1-\langle z,w\rangle)\), so the constant function has norm one. For a finite-support multiindex \(\alpha=(\alpha_j)\), write \(|\alpha|=\sum_j\alpha_j\), \(\alpha!=\prod_j\alpha_j!\), \(z^\alpha=\prod_j z_j^{\alpha_j}\). Monomials are orthogonal with squared norm \(\alpha!/|\alpha|!\). The notation \(M_\varphi\) denotes bounded multiplication on this Hilbert space. No polynomial or finite-coordinate hypothesis is imposed on multipliers. The series in the Bohr sum is absolutely convergent at all points under discussion, by the proof below. The equality characterization concerns coefficient **moduli**, not all possible phases or an operator-theoretic classification of extremizers. The one-variable result is not claimed as new; the theorem is stated for genuinely multivariable or infinitely many variables.

## Proof
**1. The norm bound and the exact multinomial kernel.** Since \(M_\varphi1=\varphi\), a contractive multiplier satisfies \(\|\varphi\|_{H_d^2}\le1\). With \(\varphi(0)=0\), orthogonality gives \(\sum_{\alpha\ne0}w_\alpha|c_\alpha|^2=\|\varphi\|_{H_d^2}^2\le1\). At a point of norm \(t=\|x\|_2<1\), the multinomial theorem yields
\[
\sum_{\alpha\ne0}\frac{|\alpha|!}{\alpha!}|x^\alpha|^2=\sum_{n\ge1}\Big(\sum_j|x_j|^2\Big)^n=\frac{t^2}{1-t^2}.
\]
In countably many variables, apply finite-coordinate truncation and monotone convergence. Weighted Cauchy–Schwarz therefore gives
\[
\mathcal M_x(\varphi)\le\|\varphi\|_{H_d^2}\frac{t}{\sqrt{1-t^2}}\le\frac{t}{\sqrt{1-t^2}}.
\]
This is at most one for \(t\le r=1/\sqrt2\), proving inclusion of the closed radius-\(r\) ball.

**2. An attained, pointwise sharp obstruction.** Fix a unit vector \(v\) in the coordinate Hilbert space and let \(\ell(z)=\langle z,v\rangle\), taking conjugation convention consistently. The Drury–Arveson coordinate row multiplier is a contraction, so \(\|M_\ell\|\le1\). Define
\[
\psi(s)=s\frac{r-s}{1-rs},\qquad \Phi_v(z)=\psi(\ell(z)).
\]
The one-variable function \(\psi\) is a finite Blaschke product, hence has supremum norm one on the unit disc. The contraction functional calculus applied to \(M_\ell\) gives \(\|M_{\Phi_v}\|\le1\), and \(\Phi_v(0)=0\). Its Taylor coefficients are \(a_1=r\) and \(a_n=-(1-r^2)r^{n-2}=-r^n\) for \(n\ge2\), so \(|a_n|=r^n\) for every \(n\ge1\).

For any nonzero point \(y\), choose \(v\) along \(y\), with unit coordinates so \(|\ell(y)|=\|y\|_2=t\) and \(\sum_j|v_jy_j|=t\). The multinomial theorem applied to each homogeneous term gives
\[
\mathcal M_y(\Phi_v)=\sum_{n\ge1}|a_n|t^n=\sum_{n\ge1}(rt)^n=\frac{rt}{1-rt}.
\]
For \(t=r\) this equals one, and for \(r<t<1\) it exceeds one. Thus all boundary points admit an extremizer, and no point of larger norm lies in \(\mathfrak B_{d,0}\). This also works in countably many coordinates, by norm convergence of the multinomial expansion. The constant \(r\) is therefore sharp in each prescribed dimension.

**3. Exact rigidity and stability at every boundary point.** Now fix \(\|x\|_2=r\) and define \(b_\alpha=(1/w_\alpha)|x^\alpha|\). The norm computation in Step 1 gives \(\sum_{\alpha\ne0}w_\alpha b_\alpha^2=\sum_{n\ge1}r^{2n}=1\). Moreover \(\sum w_\alpha|c_\alpha|b_\alpha=\mathcal M_x(\varphi)\). Expanding the square yields
\[
\sum_{\alpha\ne0}w_\alpha(|c_\alpha|-b_\alpha)^2=\|\varphi\|_{H_d^2}^2+1-2\mathcal M_x(\varphi).
\]
Rearrangement gives the claimed exact identity. Both terms on its right are nonnegative. If the majorant equals one, then the profile matches in every coefficient and \(\|\varphi\|_{H_d^2}=1\); conversely matching the profile forces majorant one. At any boundary point, the explicit \(\Phi_v\) from Step 2 has exactly these moduli. Finally, dropping the nonnegative Hilbert-norm defect gives the quantitative modulus-stability bound. \(\square\)

## Verification
The algebraic parts can be checked using rational arithmetic at boundary points with rational squared radii. The accompanying standalone `CHECKER.py` verifies the multinomial coefficient identity and the profile match for two-coordinate sample points through degree twelve, and tests the exact deficit identity with rational trial coefficients. In the proof, no finite truncation is used to infer the infinite-dimensional statement: the norm identity and geometric-series convergence justify the passages to all degrees and countably many coordinates. The only multiplier norm fact beyond direct coefficient algebra is contractivity of the linear-coordinate multiplier and the standard one-variable von Neumann inequality for a contraction.

## Relationship to prior work
Brevig, Seip, and Zlotnikov, arXiv:2609.26395 (first public version 2026-09-22), describe the **unrestricted** Drury–Arveson multiplier Bohr set as the radius-\(1/3\) Hilbert ball. Restricting to multipliers whose constant term vanishes defines a different natural extremal problem: the present result gives its sharp radius \(1/\sqrt2\), an extremizer at every boundary point, and an exact squared coefficient-modulus defect. The earlier one-variable fixed-zero-coefficient theory (Alkhaleefah–Kayumov–Ponnusamy, arXiv:1903.12646) is acknowledged and not claimed as a new result in one variable. Paulsen–Popescu–Singh (Proc. London Math. Soc. 2002) treat related multivariable Bohr inequalities; an equivalent older anchored statement remains a historical-priority risk and requires independent comparison.

## Limitations
This result does not classify the phases of all contractive boundary extremizers, or treat interpolation constraints at nonzero points. The stability term measures weighted differences of coefficient moduli and cannot be interpreted as a norm-distance theorem to a specified phase-normalized extremizer. The original-paper comparisons do not prove absolute historical novelty; the 2002 full text was not available for inspection in the present investigation. The theorem uses the Drury–Arveson kernel normalization and is not asserted for arbitrary complete Pick spaces. Independent audit and independent historical-priority validation have not been performed.

## References
1. O. F. Brevig, K. Seip, I. Zlotnikov, *Bohr sets for multiplier algebras of complete Pick spaces*, arXiv:2609.26395 (2026-09-22), https://arxiv.org/abs/2609.26395.
2. A. Alkhaleefah, I. R. Kayumov, S. Ponnusamy, *On the Bohr inequality with a fixed zero coefficient*, arXiv:1903.12646 (2019), https://arxiv.org/abs/1903.12646.
3. V. I. Paulsen, G. Popescu, D. Singh, *On Bohr's Inequality*, Proceedings of the London Mathematical Society 85 (2002), https://doi.org/10.1112/S0024611502013692.
4. J. von Neumann, classical contraction polynomial inequality (functional calculus used only in one complex variable).
