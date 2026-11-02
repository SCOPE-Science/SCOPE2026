# Exact zero staircase and the ninth-jet barrier for Sobolev–Bergman kernels

## Finding
Let \(m\ge1\) be an integer and \(\tau\ge0\). On the classical analytic Bergman space of the unit disk, augment the normalized-area norm by the squared \(m\)-th derivative at the origin:
\[
\|f\|_{m,\tau}^{2}=\frac1\pi\int_{\mathbb D}|f(z)|^{2}\,dA(z)+\tau|f^{(m)}(0)|^{2}.
\]
Define
\[
 d=\tau(m+1)(m!)^{2},\qquad c=\frac{(m+1)d}{1+d},\qquad n=m+1.
\]
The reproducing kernel and its exact number of distinct scalar zero fibres are
\[
 K_{m,\tau}(z,w)=\frac1{(1-z\overline w)^2}-c(z\overline w)^m,
\qquad
 N_m(c)=\#\left\{0\le j<n:\;4c\sin^{2}\!\left(\frac{(2j+1)\pi}{2n}\right)>1\right\}.
\]
Here a scalar zero fibre is a distinct \(t\in\mathbb D\) for which \(K_{m,\tau}(z,w)=0\) whenever \(z\overline w=t\). Every such zero is simple as a scalar root. Equality in the displayed strict inequality corresponds to a boundary root, not an interior zero.

In particular the kernel is zero-free exactly when \(c\le c_m^{\mathrm{first}}\), where
\[
 c_m^{\mathrm{first}}=
 \begin{cases}
 1/4,&m\text{ even},\\
 [4\cos^{2}(\pi/(2n))]^{-1},&m\text{ odd}.
 \end{cases}
\]
The corresponding sharp penalty threshold is
\[
 \tau_m^{\mathrm{first}}=
 \frac{c_m^{\mathrm{first}}}{(m+1)(m!)^{2}(m+1-c_m^{\mathrm{first}})}.
\]
For example, \(\tau_1^{\mathrm{first}}=1/6\) and \(\tau_2^{\mathrm{first}}=1/132\).

The full \(m+1\) interior zero fibres can occur at a finite positive penalty \(\tau\) **if and only if \(1\le m\le8\)**. For \(m\ge9\) at least one scalar root remains outside the disk for every finite penalty. Finally, for every fixed \(\tau>0\),
\[
 N_m(c_{m,\tau})=m+1-\frac{\sqrt{m+1}}\pi+O(1)\qquad(m\longrightarrow\infty).
\]
The zero-fibre count does not count the infinitely many pairs \((z,w)\) realizing a given scalar product.

## Assumptions and scope
The disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), area measure is ordinary planar area divided by \(\pi\), and \(f^{(m)}(0)\) is the unnormalized ordinary complex derivative. The result holds for each integer \(m\ge1\) and every \(\tau\in[0,\infty)\); at \(\tau=0\) the unperturbed kernel has no zeros. The constant in the final \(O(1)\) may depend on fixed \(\tau\), not on \(m\). The parameter \(c\) always belongs to \([0,m+1)\). Nonzero points \(t\) in the unit disk are realized as \(z\overline w=t\), for example with \(z\) and \(w\) of modulus \(\sqrt{|t|}\).

## Proof
The monomials are mutually orthogonal for the perturbed inner product, since the derivative term changes only the \(m\)-th coefficient. Their squared norms are \(1/(j+1)\) for \(j\ne m\) and \(1/(m+1)+\tau(m!)^2=(1+d)/(m+1)\) for \(j=m\). Summation of the reciprocals gives the displayed kernel and reduces every zero to a root of
\[
 P_{m,c}(t)=1-cg_m(t),\qquad g_m(t)=t^m(1-t)^2.
\]
No zero has \(t=0\), and \(P_{m,c}\) has degree \(m+2\) when \(c>0\).

On \(|t|=1\), write \(t=e^{i\theta}\). The exact phase identity is
\[
 g_m(e^{i\theta})=4\sin^2(\theta/2)e^{i((m+1)\theta+\pi)}.
\]
Thus \(P_{m,c}\) has a boundary zero precisely at \(\theta_j=(2j+1)\pi/(m+1)\) and \(c=[4\sin^2(\theta_j/2)]^{-1}\), for \(0\le j\le m\). These boundary zeros are simple: differentiating gives
\[
 \frac{tg'_m(t)}{g_m(t)}=m-\frac{2t}{1-t}.
\]
The only possible nonzero multiple root is at \(t=m/(m+2)\), with \(g_m(t)=4m^m/(m+2)^{m+2}\). But for physical \(c<m+1\),
\[
 c\,g_m(t)<\frac{4(m+1)}{(m+2)^2}<1,
\]
so no multiple root occurs in the entire physical parameter range. At a boundary root, \(\operatorname{Re}(t/(1-t))=-1/2\). Implicit differentiation of \(c g_m(t)=1\) along its simple root branch yields
\[
 \frac{d\log|t|}{dc}=-\frac1c\operatorname{Re}\frac1{m-2t/(1-t)}<0,
\]
since the denominator has positive real part \(m+1\). Therefore **every** boundary crossing moves strictly into the disk as \(c\) increases.

For sufficiently small \(c>0\), \(|c g_m(t)|\le4c<1\) on \(|t|\le1\), hence there are no interior roots. Roots cannot appear or disappear in the interior as \(c\) varies, because the constant term never vanishes and a polynomial root cannot escape except across the circle. The preceding transverse crossings consequently give the exact strict-inequality count \(N_m(c)\), including simultaneous conjugate crossings. The smallest of the boundary thresholds is attained at angles closest to \(\pi\), giving the parity-dependent zero-free constants. Solving \(c=(m+1)d/(1+d)\) and \(d=\tau(m+1)(m!)^2\) proves the penalty formula.

There is always a real root \(t>1\), because \(g_m(t)\) rises continuously from zero at \(t=1\) to infinity on \((1,\infty)\). The last boundary-crossing threshold is
\[
 c_m^{\mathrm{last}}=\frac1{4\sin^{2}(\pi/[2(m+1)])}.
\]
All \(m+1\) eligible roots are inside for some finite \(\tau\) exactly when \(c_m^{\mathrm{last}}<m+1\). Writing \(n=m+1\), this is \(F(n)=4n\sin^2(\pi/(2n))>1\). The function \(F(x)\) decreases strictly on \([2,\infty)\): with \(u=\pi/(2x)\), the sign of its derivative is that of \(\tan u-2u\), which is negative for \(0<u\le\pi/4\) by convexity of tangent and \(\tan u\le 4u/\pi<2u\). Further \(F(9)>1>F(10)\), rigorously from \(3.14<\pi<22/7\), \(\sin u\ge u-u^3/6\), and \(\sin u\le u\) on \([0,\pi/2]\). This proves the exact ninth-jet barrier.

For fixed \(\tau>0\), factorial growth gives \(d\to\infty\) and \(c_{m,\tau}=m+1-o(1)\). Put \(n=m+1\) and \(q=\arcsin(1/(2\sqrt c))\). The indices whose roots have not entered the unit disk correspond exactly to odd boundary angles in the two arcs of angular half-width \(2q\) around \(0\) and \(2\pi\). Their number is \(2nq/\pi+O(1)\). Since \(q=(2\sqrt n)^{-1}+O(n^{-3/2})\), the number of nonentered roots is \(\sqrt n/\pi+O(1)\), proving the high-jet asymptotic.

## Verification
The standalone Python/NumPy checker `checks.py` performs 1,130 finite assertions. It verifies the normalized monomial coefficient, boundary thresholds and phase identity, root counts by independent polynomial-root computations for degrees up to 12, the first-crossing parity law, and the order-eight/nine numerical separation. The script printed `VERIFY_OK 1130 finite assertions`. These computations are finite corroboration; the arbitrary-order phase transitions and asymptotics follow from the analytic proof above.

## Relationship to prior work
Miña-Díaz (arXiv:2212.08118v1, December 15, 2022) develops representations for kernels of **multiplicatively weighted** Bergman spaces, with derivatives at the origin entering those representations. Perälä (arXiv:1703.05976v1, March 17, 2017) proves existence and finiteness theorems for zero fibres under integrable radial weights. The present space instead uses an **additive rank-one derivative penalty** in the Hilbert norm, so neither cited weighted-space theorem gives the stated staircase. Gehlawat, Jain and Sarkar (arXiv:2608.13193v1, August 13, 2026) investigate **Gram kernels of jet-evaluation functionals**, not the reproducing kernel of the penalty-renormed space. Published unit-disk first-order and pure-jet Gram-kernel classifications likewise concern a different operation and do not imply the results here. The elementary rank-one kernel calculation itself is not asserted to be original; the claim is the complete sharp zero-fibre staircase, the ninth-jet barrier, and the asymptotic count.

## Limitations
The result concerns only the ordinary disk Bergman norm augmented at the origin by one nonnegative unnormalized derivative penalty. It does not classify multiple simultaneous penalties, negative coefficients, noncentral constraints, or other domains. The count is of scalar product values, not points in the two-variable zero set. Numerical checks are not a proof of arbitrary-jet assertions. The cited and examined literature cannot exclude every equivalent treatment outside the surveyed record; independent mathematical validation has not been performed.

## References
1. E. Miña-Díaz, *A representation for the reproducing kernel of a weighted Bergman space*, arXiv:2212.08118v1, first posted December 15, 2022, Theorem 1.1 and Sections 1–2. https://arxiv.org/abs/2212.08118
2. A. Perälä, *Vanishing Bergman kernels on the disk*, arXiv:1703.05976v1, March 17, 2017, Theorems 3.1 and 3.3 and Remark 3.2. https://arxiv.org/abs/1703.05976
3. S. Gehlawat, A. Jain and A. D. Sarkar, *A Canonical Positive Definite Kernel Associated with the ξ-Bergman Kernel*, arXiv:2608.13193v1, August 13, 2026, Gram-kernel framework and upper-half-plane discussion. https://arxiv.org/abs/2608.13193
4. N. Aronszajn, *Theory of Reproducing Kernels*, Transactions of the American Mathematical Society 68 (1950), 337–404.
