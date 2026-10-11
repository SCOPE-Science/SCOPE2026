# Exact parabolic Fourier deficit and extremizer rigidity over prime-square rings

## Finding
Let \(p\ge3\) be prime, \(R=\mathbb Z/p^2\mathbb Z\), and give \(R^2\) the uniform probability measure. Define the unnormalized parabolic extension operator
\[
(T_pf)(u,v)=\sum_{t\in R}f(t)\exp\!\left(\frac{2\pi i(ut+vt^2)}{p^2}\right),\qquad (u,v)\in R^2,
\]
where the input \(\ell^2(R)\) carries counting measure. Write \(f_r(a)=f(r+pa)\) for \(r,a\in\mathbb F_p\), using standard residue representatives, and set
\[
m_r=\sum_{a\in\mathbb F_p}|f_r(a)|^2,\qquad
\widehat f_r(\xi)=\sum_{a\in\mathbb F_p}f_r(a)e^{-2\pi i a\xi/p}.
\]
For every complex-valued \(f:R\to\mathbb C\), the following is an **exact nonnegative fourth-moment deficit identity**:
\[
\boxed{\begin{aligned}
p\|f\|_2^4-\|T_pf\|_{L^4(R^2)}^4
={}&2(p-2)\sum_{0\le r<s<p}m_rm_s\\
&+\frac1p\sum_{r=0}^{p-1}\sum_{\substack{\xi,\eta\in\mathbb F_p\\\xi\ne\eta}}
|\widehat f_r(\xi)|^2|\widehat f_r(\eta)|^2.
\end{aligned}}
\]
Consequently, the **sharp norm** is \(\|T_p\|_{\ell^2\to L^4}=p^{1/4}\), and the nonzero extremizers are **exactly**
\[
\boxed{ f(r+pa)=c\,e^{2\pi i\xi a/p}\quad(a\in\mathbb F_p),\qquad f(t)=0\quad(t\not\equiv r\pmod p), }
\]
with \(c\in\mathbb C\setminus\{0\}\), \(r,\xi\in\mathbb F_p\). Thus the extremizers comprise precisely \(p^2\) projective complex lines, forming an orthogonal packet basis.

The identity also gives a global quantitative stability statement. If \(\|f\|_2=1\), put \(\delta(f)=p-\|T_pf\|_{L^4}^4\), and let \(\mathcal P_p\) be the union of the \(p^2\) extremizer lines together with zero. Then
\[
\boxed{\operatorname{dist}_{\ell^2}(f,\mathcal P_p)^2\le\frac{p-1}{p-2}\,\delta(f).}
\]
The displayed stability coefficient is valid but is not asserted optimal.

## Assumptions and scope
The prime \(p\) is odd, and all equalities hold for *every* complex function on \(R\). The output is measured with probability measure \(p^{-4}\sum_{u,v\in R}\); the input norm is \(\|f\|_2^2=\sum_{t\in R}|f(t)|^2\). Fourier transforms on residue sections are unnormalized. The two-component defect and the equality classification are for the degree-two graph over the ring of characteristic \(p^2\), not over a field of cardinality \(p^2\). No assertion is made for higher prime powers or characteristic two.

## Proof
**1. Pair-sum fibers.** Character orthogonality on \(R^2\) gives
\[
\|T_pf\|_{L^4}^4
=\sum_{(s,z)\in R^2}
\left|\sum_{\substack{x+y=s\\x^2+y^2=z}}f(x)f(y)\right|^2.
\tag{1}
\]
Because \(2\) is invertible, a pair's sums modulo \(p\) determine the unordered pair of its residue classes. Thus pairs from distinct unordered residue-class combinations have disjoint fibers of the map \((x,y)\mapsto(x+y,x^2+y^2)\).

Fix two distinct residues \(r\ne s\). For \(x\equiv r\), \(y\equiv s\pmod p\), the Jacobian determinant of the map from \((x,y)\) to the two sums is \(2(y-x)\), a unit. More explicitly, equality of \(x+y\) and \(x^2+y^2\) for two ordered pairs implies equality of their products, because \(2xy=(x+y)^2-(x^2+y^2)\). Their difference is a unit modulo \(p\), so the roots lift uniquely in the specified two residue classes: if \(x\) changes by \(h\) with \(p\mid h\), fixed sum forces \(y\) to change by \(-h\); fixed product then gives \(h(y-x-h)=0\) modulo \(p^2\). The second factor is a unit, hence \(h=0\) modulo \(p^2\). Each such mixed fiber therefore has exactly the two ordered representatives \((x,y)\) and \((y,x)\). Its contribution to (1), summed over the two residue classes, is \(4m_rm_s\).

For the diagonal residue class \(r\), put \(x=r+pa\), \(y=r+pb\). Modulo \(p^2\),
\[
x+y=2r+p(a+b),\qquad x^2+y^2=2r^2+2rp(a+b).
\]
Hence the pair-sum fiber depends exactly on \(a+b\in\mathbb F_p\). Since distinct residue multisets are disjoint, this gives
\[
\|T_pf\|_{L^4}^4
=\sum_{r\in\mathbb F_p}\sum_{b\in\mathbb F_p}
\left|\sum_{a\in\mathbb F_p}f_r(a)f_r(b-a)\right|^2
+4\sum_{r<s}m_rm_s.
\tag{2}
\]

**2. Fourier separation and exact defect.** Parseval and the convolution theorem on \(\mathbb F_p\) give
\[
\sum_b |(f_r*f_r)(b)|^2=\frac1p\sum_\xi|\widehat f_r(\xi)|^4,
\qquad
\sum_\xi|\widehat f_r(\xi)|^2=pm_r.
\]
Therefore
\[
pm_r^2-\frac1p\sum_\xi|\widehat f_r(\xi)|^4
=\frac1p\sum_{\xi\ne\eta}|\widehat f_r(\xi)|^2|\widehat f_r(\eta)|^2.
\tag{3}
\]
Expanding \(p(\sum_r m_r)^2\) and subtracting (2), then applying (3), proves the deficit identity. All its terms are nonnegative because \(p\ge3\).

**3. All equality cases.** For nonzero \(f\), vanishing of the mixed-residue defect, whose coefficient \(2(p-2)\) is strictly positive, forces exactly one \(m_r\) to be positive. Vanishing of the corresponding Fourier defect forces its transform \(\widehat f_r\) to have precisely one nonzero Fourier coefficient. Fourier inversion makes \(f_r\) a nonzero scalar multiple of a character \(a\mapsto e^{2\pi i\xi a/p}\). Conversely every such function makes both defect terms vanish. Distinct choices of \((r,\xi)\) span mutually orthogonal one-dimensional subspaces; there are \(p^2\) of them, the dimension of \(\ell^2(R)\).

**4. Quantitative stability.** Let \(\|f\|_2=1\). Then \(\sum_rm_r=1\). Writing the two nonnegative summands of the deficit as \(D_{\mathrm{mix}}\) and \(D_{\mathrm{freq}}\), we have
\[
D_{\mathrm{mix}}=(p-2)\left(1-\sum_rm_r^2\right)\le\delta(f).
\]
Choose \(r\) with maximal \(m_r\). Since \(m_r\ge\sum_sm_s^2\) and \(m_r\ge1/p\),
\[
1-m_r\le\delta(f)/(p-2).
\]
For this section define \(q_\xi=|\widehat f_r(\xi)|^2/(pm_r)\). These numbers are nonnegative and sum to one. Put \(V_r=pm_r^2(1-\sum_\xi q_\xi^2)\le D_{\mathrm{freq}}\le\delta(f)\). Because \(\max_\xi q_\xi\ge\sum_\xi q_\xi^2\), the squared orthogonal projection of \(f\) onto the best packet ray is at least
\[
m_r\max_\xi q_\xi\ge m_r-\frac{V_r}{pm_r}.
\]
The squared distance to this ray is consequently at most
\[
1-m_r+\frac{V_r}{pm_r}
\le\frac{\delta(f)}{p-2}+\delta(f)
=\frac{p-1}{p-2}\delta(f),
\]
proving the stated bound.

## Verification
Run `python3 artifacts/verify.py` with a standard Python interpreter. The checker forms exact pair-sum fibers over \(\mathbb Z/p^2\mathbb Z\), verifies their residue-class decomposition, and checks the quartic deficit using Gaussian-integer coefficients for \(p\in\{3,5,7\}\). It tests all \(p^2\) Fourier packets for each selected prime and also independently evaluates the Fourier synthesis sums at \(p\in\{3,5\}\) for four generic examples. Successful replay reports `VERIFY_OK` and the checked case counts. These finite tests corroborate the universal proof above; they are not a substitute for it.

## Relationship to prior work
Mockenhaupt and Tao's even-exponent incidence-fiber argument (arXiv:math/0204234, Lemma 5.1) provides a general mechanism for fourth-moment estimates. Applied to the maximum pair-fiber size \(p\) here, that argument already yields the norm upper bound; a single packet attains it. **The sharp norm bound alone is not claimed as a new principle.** The contribution of the present result is the exact **two-mechanism defect**, the complete complex equality classification, and the quantitative distance-to-packet estimate for the first nonfield modulus.

Hickman and Wright (arXiv:1801.03176, Sections 2–3) develop parabolic wave packets over residue rings, including the prime-square scale, and obtain their explicit physical-space extensions. Their formulation supplies the natural packet model, but the inspected sections and curve results do not state the global quartic defect or classify every \(\ell^2\to L^4\) maximizer.

González-Riquelme and Oliveira e Silva (arXiv:2405.16647, Theorems 1.1–1.3) study sharp extension on finite **fields**, including modulus and optimizer information in different dimensions and exponents. The nilpotent ring fibers and the resulting packet rigidity do not reduce to those field theorems. A published finite-field moment-curve stability inequality likewise controls amplitude nonuniformity over a field, rather than single-residue concentration and within-packet Fourier dispersion on this ring.

## Limitations
The stability coefficient is not certified optimal. The result is confined to odd-prime-square rings and this quadratic graph; it does not assert the same rigidity for higher-power local rings or other polynomial curves. A residual priority risk is an unindexed or implicit equality-case calculation in older \(p\)-adic wave-packet theory. No complete historical-priority certification is claimed.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234, initially public 18 April 2002, especially Section 5.
2. J. Hickman and J. Wright, *The Fourier restriction and Kakeya problems over rings of integers modulo \(N\)*, arXiv:1801.03176, initially public 9 January 2018, especially Sections 2–3 and 7.
3. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, initially public 26 May 2024, especially Theorems 1.1–1.3.
