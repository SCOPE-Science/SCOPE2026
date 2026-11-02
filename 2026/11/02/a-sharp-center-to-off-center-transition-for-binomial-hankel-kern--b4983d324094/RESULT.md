# A sharp center-to-off-center transition for binomial Hankel kernel tests

## Finding

For integers \(m>n\ge1\) and a real coefficient \(c>0\), set
\[
\psi_c(z)=z^m+cz^n,
\qquad H_c f=P_-(\overline{\psi_c}f):H^2(\mathbb D)\to H^2_-,
\]
and define the reproducing-kernel test norm
\[
G_{m,n}(c)=\sup_{a\in\mathbb D}\|H_ck_a\|_2
=\|\psi_c\|_G,
\qquad k_a(z)=\frac{\sqrt{1-|a|^2}}{1-\overline a z}.
\]
The question of whether the **center kernel** \(k_0\) realizes this testing norm has the following exact three-regime answer.

* If \(m<3n\), the center never realizes the test supremum for any \(c>0\).
* If \(m=3n\), it realizes the supremum exactly when \(c\ge2\). For \(0<c<2\), the radius of every maximizing kernel is given exactly by
\[
 r_c^{2n}=\frac{\sqrt{c^2+6c}-2c}{3}>0.
\]
At \(c=2\), the center is the unique maximizing point.
* If \(m>3n\), define
\[
 p=\frac{m-3n}{2n}>0,
 \quad C_{m,n}=\frac{1}{2^{p+1}}
 \left(\frac{p}{p+1}\right)^p
 \left(\frac{p+2}{p+1}\right)^{p+2}.
\]
The center realizes the supremum exactly when \(c\ge C_{m,n}\). Above the threshold it is the only maximizing point; at the threshold there are also off-center maximizing points at radius
\[
 r_*=\left(\frac{p(p+2)}{2(p+1)^2}\right)^{1/(2n)}.
\]
For \(0<c<C_{m,n}\), all maximizing points are off-center, and their radii converge to \(r_*>0\) as \(c\uparrow C_{m,n}\). Thus the optimal kernel's radius jumps at the threshold for \(m>3n\), whereas it approaches zero continuously for \(m=3n\). For example, the family \(z^5+cz\) has the exact critical coefficient \(27/64\) and a coexisting off-center optimal radius \(\sqrt{3/8}\) at the transition.

There is also a sharp, *noninteger-power* law as \(c\downarrow0\), valid throughout \(m>n\ge1\). Put
\[
 d=m-n,\quad M=m+n,\quad
 \alpha=\frac{2m}{M},\quad
 K_{m,n}=\frac{M}{m}\left(\frac d m\right)^{d/M},
 \quad L=\left\lceil\frac{m}{d}\right\rceil.
\]
For every maximizing radius \(r_c\),
\[
 \frac{r_c}{c^{1/M}}\longrightarrow
 \left(\frac d m\right)^{1/M},\qquad
 G_{m,n}(c)^2=1+K_{m,n}c^\alpha+o(c^\alpha).
\]
By contrast, the full Hankel operator has the **linear** perturbation law
\[
 \|H_c\|=1+\cos\left(\frac{\pi}{L+1}\right)c+O(c^2),
\]
so the strict kernel-testing deficit has the two-term expansion
\[
 \boxed{\|H_c\|-G_{m,n}(c)
 =\cos\left(\frac{\pi}{L+1}\right)c
 -\frac{K_{m,n}}2c^\alpha+o(c^\alpha).}
\]
In particular \(1<\alpha<2\), \(\|H_c\|>G_{m,n}(c)\) for every \(c>0\), and the testing norm is only fractionally smooth as it leaves a monomial symbol.

## Assumptions and scope

We work on the classical complex Hardy space \(H^2(\mathbb D)\) with orthonormal basis \(1,z,z^2,\ldots\), its negative-frequency counterpart \(H^2_-=L^2(\mathbb T)\ominus H^2\), and orthogonal projection \(P_-\). Poisson integrals use normalized arc length on \(\mathbb T\). The integers \(m,n\) are fixed throughout the small-\(c\) limit. For a general nonzero complex coefficient, rotation of the disk and multiplication of the symbol by a unimodular scalar reduce the norms and maximizing radii to the case \(c=|c|>0\). No assertion is made about infinitely supported symbols or limits in which the exponents vary with \(c\).

The exact threshold concerns the point \(a=0\) being a **maximizer of the kernel test norm**, not equality of this norm with the full operator norm. These are different properties.

## Proof

**1. Exact testing functional.** The standard Hardy Hankel/kernel identity gives
\[
 \|H_ck_a\|_2^2
 =\mathcal P(|\psi_c|^2)(a)-|\psi_c(a)|^2.
\]
Writing \(a=re^{i\theta}\), direct Fourier multiplication gives
\[
 \|H_ck_a\|_2^2
 =1+c^2-r^{2m}-c^2r^{2n}
 +2c(r^{m-n}-r^{m+n})\cos((m-n)\theta).
\]
For \(0<r<1\), the angular maximum is realized when \(\cos((m-n)\theta)=1\). Consequently, the exact squared test norm is the maximum over \(0\le r\le1\) of
\[
 F_c(r)=1+c^2-r^{2m}-c^2r^{2n}
 +2c r^{m-n}(1-r^{2n}),
\]
with \(F_c(1)=0\) and \(F_c(0)=1+c^2\). Every maximum occurs at \(r<1\).

**2. The threshold.** Set \(d=m-n\) and
\[
 B_c(r)=F_c(r)-F_c(0)
 =-r^{2m}-c^2r^{2n}+2cr^d(1-r^{2n}).
\]
If \(m<3n\), the positive term has strictly smaller exponent of \(r\) than the two negative terms; hence \(B_c(r)>0\) for all sufficiently small positive \(r\), at each fixed \(c>0\).

For \(m\ge3n\), put \(x=r^{2n}\) and \(p=(m-3n)/(2n)\ge0\). After dividing by \(r^{2n}>0\), the inequality \(B_c(r)>0\) becomes
\[
 c^2-2cx^p(1-x)+x^{2(p+1)}<0.
\]
Its discriminant is \(4x^{2p}(1-2x)\), so a strict improvement over the center requires \(0<x<1/2\), with \(c\) strictly between
\[
 c_\pm(x)=x^p\bigl(1-x\pm\sqrt{1-2x}\bigr).
\]
Set \(y=\sqrt{1-2x}\in(0,1)\). The upper root is
\[
 c_+(x)=2^{-p-1}(1-y)^p(1+y)^{p+2}.
\]
For \(p=0\) its supremum is \(2\), approached only as \(x\downarrow0\); for \(p>0\), its unique maximum is at \(y=(p+1)^{-1}\), with value \(C_{m,n}\) and radius \(r_*\) as stated. Thus no off-center point improves on the center when \(c\) is at least the threshold. Conversely, every \(0<c<C_{m,n}\) has an \(x\) between the two roots: for \(p>0\), start at the first ascending solution of \(c_+(x)=c\), where \(c_-(x)<c\), and move slightly toward the maximizer of \(c_+\); for \(p=0\), choose \(x>0\) sufficiently small. This proves the exact center-optimality classification.

At the threshold for \(p>0\), equality \(B_c(r)=0\) away from the center forces \(c=c_+(x)=\max c_+\), hence \(x=p(p+2)/(2(p+1)^2)\), the unique positive maximizing radius. For \(p=0\), no positive \(x\) reaches the supremum of \(c_+\). As \(c\uparrow C_{m,n}\) with \(p>0\), any off-center maximizing radius must converge to \(r_*\): compactness restricts its limit to \(0\) or \(r_*\), while \(B_c(r)<0\) uniformly at sufficiently small positive radii for all \(c\) close to the positive threshold, because \(-c^2r^{2n}\) is then the leading term. This proves the jump.

When \(m=3n\), write \(x=r^{2n}\). Directly,
\[
 B_c(r)=x\bigl((2c-c^2)-2cx-x^2\bigr).
\]
For \(0<c<2\), its unique positive maximizer solves
\[
 3x^2+4cx-(2c-c^2)=0,
\]
which yields the displayed formula and tends to zero as \(c\uparrow2\).

**3. Fractional-power response at a monomial.** Let \(M=m+n\), \(d=m-n\), \(\alpha=2m/M\), and scale \(r=c^{1/M}s\). The exact radial identity becomes
\[
 \frac{F_c(c^{1/M}s)-1}{c^\alpha}
 =2s^d-s^{2m}
 +c^{2-\alpha}(1-2s^M)
 -c^{2+2n/M-\alpha}s^{2n}.
\]
The limiting function \(2s^d-s^{2m}\) on \([0,\infty)\) has a unique positive maximum at \(s_0=(d/m)^{1/M}\), with value \(K_{m,n}\). To justify the global maximization, the bound
\[
 F_c(r)-1\le c^2+2cr^d-r^{2m}
\]
forces every maximizing radius to tend to zero, and forces its scaled value \(r/c^{1/M}\) to remain bounded. Since the explicit test at \(s_0\) gives a positive limiting gain, no scaled maximizing radius can tend to zero. Uniform convergence on the remaining compact annulus then implies every scaled maximizer tends to \(s_0\) and the squared-norm expansion follows. The displayed deficit follows after taking square roots, because \(\alpha<2\).

**4. Full Hankel norm and strictness.** On the span of the first \(m\) Hardy monomials, the Hankel matrix is the sum of the reversal matrix \(J_m\) and \(cJ_n\), where \(J_n\) occupies the upper-left \(n\times n\) corner; it vanishes on the orthogonal complement. With \(S\) the nilpotent forward coordinate shift on \(\mathbb C^m\),
\[
 (J_m+cJ_n)^*(J_m+cJ_n)
 =I_m+c(S^d+(S^*)^d)+c^2P_n.
\]
The graph of \(S^d+(S^*)^d\) is the disjoint union of path graphs along residue classes modulo \(d\). Its longest path has \(L=\lceil m/d\rceil\) vertices and largest eigenvalue \(2\cos(\pi/(L+1))\). The \(c^2P_n\) term changes the largest eigenvalue by at most \(c^2\), giving the stated full-norm expansion and, combined with Step 3, the two-term deficit.

For strictness at every \(c>0\), note that for \(a\ne0\) the unit kernel has a nonzero tail beyond the first \(m\) coordinates; therefore \(\|H_ck_a\|<\|H_c\|\). At \(a=0\), the positive matrix above maps the first basis vector to \((1+c^2)e_0+ce_d\), so that vector is not an eigenvector and cannot norm \(H_c\). The kernel testing norm is attained in the open disk because its continuous squared norm tends uniformly to zero at the boundary, and hence it is strictly below \(\|H_c\|\).

## Verification

The exact Poisson formula was independently evaluated from Fourier coefficients and compared with direct finite Hankel matrices. The standalone program `check_binomial.py` checks the Fourier/radial identity, exact threshold tangencies in rational cases, off-center versus center optimizers, the path-spectrum perturbation coefficient, and the predicted fractional-power scale at several exponent pairs and coefficient values. These are finite, independent consistency checks; the continuum and asymptotic assertions are proved in Steps 1–4, not inferred from samples.

## Relationship to prior work

Dyakonov's 2026 paper formulates the strong reproducing kernel thesis for Hardy Hankel operators, gives the exact kernel-testing/Garsia identity, and records non-SRKT examples among quadratic polynomial symbols. Its addendum also states the qualitative classification that only monomial polynomial symbols satisfy the strong thesis. The present result does **not** present that classification as new: it resolves the distinct quantitative question of *where* the kernel test is largest in the two-term polynomial family, with a sharp coefficient threshold and a fractional-power versus linear perturbation law.

The 2025 Garsia-norm study by Dyakonov establishes general extremality and norm-attainment facts, not this coefficient/exponent transition. Accessible published mathematical notes on polynomial monomial rigidity and finite-rank shifted-Blaschke SRKT likewise establish equality classifications, not the explicit center-optimality threshold or two-term binomial deficit. The operator and its normalization are the same, but the previously established implication `SRKT iff monomial` gives only strictness, not the present constants or kernel-location transition.

## Limitations

The coefficients are reduced to their moduli by symmetry; exponents are fixed positive integers \(m>n\). The threshold concerns a single two-term symbol family, not arbitrary analytic polynomials. The small-\(c\) error estimates are pointwise in fixed \(m,n\), not uniform as the exponents grow. No external independent verification or publication-priority determination is claimed. An earlier specialized computation of binomial Garsia maximizers, if found, could affect originality; exact-target searches and accessible primary comparisons did not locate one.

## References

1. K. M. Dyakonov, *The strong reproducing kernel thesis for Hankel operators and the Garsia norm*, arXiv:2609.33242v3 (first public v1, 2026-09-27), especially Sections 1–3.
2. K. M. Dyakonov, *Extremal problems in BMO and VMO involving the Garsia norm*, arXiv:2404.05565v2, J. Funct. Anal. 288 (2025), 110833.
3. F. F. Bonsall, *Boundedness of Hankel matrices*, J. London Math. Soc. 29 (1984), 289–300 (the kernel identity quoted in Reference 1).
4. *Monomial rigidity for polynomial-symbol Hankel operators obeying the strong reproducing kernel thesis*, published mathematical note (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-monomial-rigidity-for-polynomial-symbol-hankel-operators-obeying--bc8369ca1a24.
5. *Shifted-Blaschke classification of finite-rank SRKT Hankel operators*, published mathematical note (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-shifted-blaschke-classification-of-finite-rank-srkt-hankel-opera--c64bd5a5783f.
