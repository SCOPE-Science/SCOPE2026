# Sharp Hadamard-convolution threshold for bounded-turning semigroup generators

## Finding
Let \(\mathbb D\) be the open unit disk and let \(\mathcal R\) be the normalized class of analytic functions \(f(0)=0\), \(f'(0)=1\), and \(\operatorname{Re}f'(z)>0\) on \(\mathbb D\). Write \(f*g\) for the coefficientwise Hadamard product. For \(0\le\beta\le1\), put
\[
\mathcal A_\beta=\left\{h(0)=0,\ h'(0)=1:\ \operatorname{Re}\left[(1-\beta)h'(z)+\beta h(z)/z\right]>0\text{ in }\mathbb D\right\}.
\]
Define the real-valued sharp profile, for \(0\le r\le1\), by
\[
Q_\beta(r)=1-4\int_0^1\left[(1-\beta)-\beta\log t\right]\frac{rt}{1+rt}\,dt.
\]
Then for every \(0<r<1\) and \(0\le\beta\le1\),
\[
\min_{f,g\in\mathcal R,\ |z|=r}\operatorname{Re}\left[(1-\beta)(f*g)'(z)+\beta\frac{(f*g)(z)}z\right]=Q_\beta(r).
\]
The minimum is attained by the same two fixed normalized functions \(f_*(z)=g_*(z)=-z-2\log(1-z)\) at \(z=-r\). The largest universal disk radius for the condition \((f*g)(Rz)/R\in\mathcal A_\beta\), simultaneously for all \(f,g\in\mathcal R\), is
\[
R_\beta=\begin{cases}
\text{the unique root of }Q_\beta(r)=0\text{ in }(0,1),&0\le\beta<\beta_*,\\
1,&\beta_*\le\beta\le1,
\end{cases}
\qquad
\beta_* = \frac{3/4-\log 2}{\pi^2/12-\log 2}=0.439629478234641\ldots.
\]
In particular, the sharp global closure criterion is
\[
\boxed{\mathcal R*\mathcal R\subseteq\mathcal A_\beta\quad\Longleftrightarrow\quad\beta\ge\beta_*.}
\]
For \(0\le\beta<\beta_*\), the sharp radius \(R_\beta\) is strictly increasing with \(\beta\), with \(R_0=0.733600988878758\ldots\), determined equivalently by \(\log(1+R_0)=3R_0/4\).

## Assumptions and scope
All functions are holomorphic on \(\mathbb D\), normalized by \(f(0)=0\), \(f'(0)=1\). The complex logarithm in \(f_*\) is its branch analytic in \(\mathbb D\) with \(\log1=0\). The parameter \(\beta\) ranges over the **entire closed interval** \([0,1]\). The integral at \(t=0\) is understood by integrability of \(-\log t\). The quotient \(h(z)/z\) is defined at zero by its analytic continuation, equal to \(1\). The radius \(R_\beta\) is defined via the OPEN disk \(|z|<R_\beta\); at a strict subcritical parameter, the extremal expression is zero exactly at the limiting boundary point \(z=-R_\beta\), and becomes negative beyond it.

## Proof
**1. Herglotz reduction.** Because \(\operatorname{Re}f'(z)>0\) and \(f'(0)=1\), the Herglotz representation gives a probability measure \(\mu\) on \(\mathbb T\) such that
\[
f'(z)=\int_{\mathbb T}\frac{1+\xi z}{1-\xi z}\,d\mu(\xi)
=1+2\sum_{n\ge1}\widehat\mu(n)z^n,
\quad\widehat\mu(n)=\int_{\mathbb T}\xi^n\,d\mu(\xi).
\]
Similarly, \(g'\) is represented by a probability measure \(\nu\). Consequently
\[
f(z)=z+2\sum_{n\ge1}\frac{\widehat\mu(n)}{n+1}z^{n+1},\qquad
(f*g)(z)=z+4\sum_{n\ge1}\frac{\widehat\mu(n)\widehat\nu(n)}{(n+1)^2}z^{n+1}.
\]
Let \(\lambda\) be the pushforward of \(\mu\otimes\nu\) under multiplication \((\xi,\eta)\mapsto\xi\eta\). It is a probability measure, with \(\widehat\lambda(n)=\widehat\mu(n)\widehat\nu(n)\). Hence, for \(h=f*g\),
\[
(1-\beta)h'(z)+\beta h(z)/z
=\int_{\mathbb T}q_\beta(\xi z)\,d\lambda(\xi),
\quad
q_\beta(w)=1+4\sum_{n\ge1}\left(\frac{1-\beta}{n+1}+\frac{\beta}{(n+1)^2}\right)w^n.
\]
All power series converge absolutely on compact disks, justifying coefficientwise products and interchanges.

**2. Pointwise angular minimum.** Set \(w_\beta(t)=1-\beta-\beta\log t\ge0\) for \(0<t<1\). Using
\(\int_0^1t^n\,dt=1/(n+1)\) and \(\int_0^1t^n(-\log t)\,dt=1/(n+1)^2\), sum the geometric series to obtain
\[
q_\beta(w)=1+4\int_0^1w_\beta(t)\frac{tw}{1-tw}\,dt.
\]
For \(0<s<1\) and \(x=\cos\theta\),
\[
\operatorname{Re}\frac{se^{i\theta}}{1-se^{i\theta}}
=\frac{sx-s^2}{1-2sx+s^2},\qquad
\frac{d}{dx}\left(\frac{sx-s^2}{1-2sx+s^2}\right)
=\frac{s(1-s^2)}{(1-2sx+s^2)^2}>0.
\]
Thus the unique minimizing angle of \(q_\beta\) on \(|w|=r\) is \(w=-r\), with \(\min_{|w|=r}\operatorname{Re}q_\beta(w)=Q_\beta(r)\). Integrating over \(\lambda\) implies the claimed universal lower bound. It is achieved by the atomic measures \(\mu=\nu=\delta_1\), corresponding to \(f_*=g_*=-z-2\log(1-z)\), and \(z=-r\). In particular, this is an EXACT sharp bound at every radius, not a coefficient estimate with an uncontrolled triangle inequality.

**3. Full-disk phase transition.** The function \(Q_\beta\) is continuous and strictly decreasing in \(r>0\):
\[
\frac{dQ_\beta(r)}{dr}=-4\int_0^1w_\beta(t)\frac{t}{(1+rt)^2}\,dt<0,\qquad Q_\beta(0)=1.
\]
Elementary integrals and the alternating zeta value give
\[
\int_0^1\frac{t}{1+t}\,dt=1-\log2,\qquad
\int_0^1\frac{-t\log t}{1+t}\,dt=1-\frac{\pi^2}{12}.
\]
Therefore
\[
Q_\beta(1)=4\log2-3+\beta\left(\frac{\pi^2}{3}-4\log2\right),
\]
which changes sign exactly once, at the displayed \(\beta_*\in(0,1)\). For \(\beta\ge\beta_*\), strict monotonicity implies \(Q_\beta(r)>0\) for every \(r<1\), so \(f*g\in\mathcal A_\beta\) for every pair. For \(\beta<\beta_*\), there is exactly one root \(R_\beta\in(0,1)\), positivity holds throughout \(|z|<R_\beta\), and the extremizing pair yields a negative value at each real \(z=-r\) with \(R_\beta<r<1\). This proves both necessity and sufficiency of the threshold and sharpness of every subcritical radius.

**4. Strict increase of subcritical radii.** The function \(\phi_r(t)=rt/(1+rt)\) is strictly increasing in \(t\), whereas \(-\log t\) is strictly decreasing, and both have finite uniform means, with \(\int_0^1(-\log t)\,dt=1\). Their strictly negative covariance implies
\(\int_0^1(-\log t)\phi_r(t)\,dt<\int_0^1\phi_r(t)\,dt\). Hence \(Q_\beta(r)\) strictly increases with \(\beta\) for each \(r>0\), and the implicit sharp root \(R_\beta\) strictly increases while below one. For \(\beta=0\), elementary integration yields \(Q_0(r)=1-4[1-\log(1+r)/r]\), giving the stated scalar equation and numerical radius.

## Verification
The standalone standard-library script `checker.py` independently checks the exact rational coefficient identities for selected \(\beta\), the boundary threshold identity, the scalar equation at \(\beta=0\), several angular-minimum inequalities, and the nonapplicability of the earlier convex-factor/half-plane sufficient conditions to the sharp pair. It cannot certify Herglotz representation, global positivity or infinite-dimensional sharpness; these follow from the explicit analytical argument in the preceding section.

## Relationship to prior work
Mandal and Ahamed (arXiv:2604.24776, first posted 2026-04-18) study the filtration \(\mathcal A_\beta\) with sharp low-order logarithmic, inverse and Fekete–Szegő coefficient estimates. Their Sections 2–4 and concluding problems do not give a threshold for convolution of two members of \(\mathcal R\). Giri and Kumar (arXiv:2205.10777, first posted 2022-05-22) prove in Theorems 2.5–2.6 that \(f*g\in\mathcal A_\beta\) when \(f\in\mathcal A_\beta\) and the other factor \(g\) either satisfies \(\operatorname{Re}[g(z)/z]>1/2\) or is convex. These sufficient hypotheses are not automatic for \(g\in\mathcal R\): indeed the present sharp factor satisfies \(\lim_{r\uparrow1}f_*(-r)/(-r)=2\log2-1<1/2\), and \(\operatorname{Re}[1+zf_*''/f_*']<0\) on some negative real points. The earlier theorems therefore do not imply the sharp \(\mathcal R*\mathcal R\) phase transition. A broad historical equivalence with an older convolution-multiplier theorem cannot be excluded without independent literature audit.

## Limitations
This theorem concerns **normalized** bounded-turning factors \(\mathcal R\), **twofold** Hadamard products, the **positive-real-part filtration** \(\mathcal A_\beta\), and \(0\le\beta\le1\); it does not claim the same cutoff for general semigroup generators, unnormalized factors, or repeated products. The sharpness statement is on the circle \(|z|=r\) and membership concerns the open disk; at the critical boundary \(\beta=\beta_*\), positivity remains strict at every interior point. Numerical checks do not constitute a computer-assisted proof. Priority outside the inspected literature is unverified, and independent mathematical review has not occurred.

## References
1. S. Mandal and M. B. Ahamed, *Sharp Coefficient and Inverse Problems for Holomorphic Semigroup Generators*, arXiv:2604.24776 (initial public posting 2026-04-18), primary MSC2020 30C45 and 30C50; https://arxiv.org/abs/2604.24776.
2. S. Giri and S. Sivaprasad Kumar, *Radius and Convolution Problems of Analytic Functions Involving Semigroup Generators*, arXiv:2205.10777 (initial public posting 2022-05-22), Theorems 2.5–2.6; https://arxiv.org/abs/2205.10777.
3. Classical Herglotz representation theorem for normalized holomorphic functions with positive real part; applied explicitly in the proof.
