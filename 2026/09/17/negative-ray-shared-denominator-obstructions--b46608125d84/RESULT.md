# Uniform rational approximation on the negative ray: obstructions to a no-assumptions shared-denominator theorem

## Result

Let \(I=(-\infty,0]\), and let \(\mathcal R_n\) denote the rational functions \(r=p/q\) with
\(\deg p,\deg q\le n\), interpreted after cancellation, and with no pole on \(I\).
Write
\[
E_n(f;I):=\inf_{r\in\mathcal R_n}\sup_{x\in I}|f(x)-r(x)|.
\]

A recent theorem of Al-Mohy, *Shared-Pole Carathéodory--Fejér Approximations for Linear Combinations of \(\phi\)-Functions* (Mathematics 13 (2025), 3985), states that for every finite family
\[
\{f_0,\ldots,f_p\}\subset \mathcal A(D),\qquad D=\mathbb C\setminus(-\infty,0],
\]
there are type-\((n,n)\) rational approximants with a common denominator and a uniform geometric error \(C\rho^{-n}\) on \(I\), with no hypotheses beyond membership in \(\mathcal A(D)\). The conclusion is false at this level of generality.

Two independent obstructions are given below. The second remains valid even after imposing boundedness and a finite limit at \(-\infty\).

### 1. Exact uniform-closure obstruction

Let
\[
C_\infty(I)=\left\{f\in C_b(I):\lim_{x\to-\infty}f(x)\ \text{exists in }\mathbb C\right\}.
\]
Then the uniform closure in \(C_b(I)\) of rational functions with no poles on \(I\) is exactly \(C_\infty(I)\).

Moreover, for every finite family \(f_0,\ldots,f_p\in C_\infty(I)\), uniform convergence can be achieved with the single explicit denominator
\[
q_n(x)=(1-x)^n
\]
for all members of the family.

#### Proof

A rational function bounded on \(I\) has a finite limit at \(-\infty\): after cancellation it has numerator degree at most denominator degree. Uniform limits preserve this property. Indeed, if \(r_m\to f\) uniformly and \(L_m=\lim_{x\to-\infty}r_m(x)\), then
\[
|L_m-L_k|\le \|r_m-r_k\|_{\infty,I},
\]
so \(L_m\) converges to some \(L\), and a standard three-term estimate gives \(f(x)\to L\).

Conversely, set
\[
y=\frac{-x}{1-x},\qquad x=\frac{-y}{1-y}.
\]
This identifies the one-point compactification \(I\cup\{-\infty\}\) with \([0,1]\). If \(f\in C_\infty(I)\), then
\[
F(y)=f\!\left(\frac{-y}{1-y}\right),\qquad F(1)=\lim_{x\to-\infty}f(x),
\]
is continuous on \([0,1]\). By Weierstrass approximation there are polynomials \(P_n\) of degree at most \(n\) with \(P_n\to F\) uniformly. Hence
\[
P_n\!\left(\frac{-x}{1-x}\right)=\frac{p_n(x)}{(1-x)^n},
\qquad \deg p_n\le n,
\]
converges uniformly to \(f\) on \(I\). For a finite family, choose the numerator polynomials separately and retain the same denominator \((1-x)^n\).

This proves the characterization.

As an immediate counterexample to geometric approximation, take the entire function
\[
f(z)=e^{iz}.
\]
For every \(n\),
\[
\boxed{E_n(e^{i\cdot};I)=1.}
\]
Indeed, any rational \(r\) with finite uniform error is bounded on \(I\), hence tends to a finite \(L\) at \(-\infty\). Along the two sequences
\[
x_k=-2\pi k,\qquad y_k=-(2k+1)\pi,
\]
the target tends alternately to \(1\) and \(-1\). Thus
\[
\sup_{x\le0}|e^{ix}-r(x)|
\ge \max\{|1-L|,|-1-L|\}\ge1,
\]
while \(r\equiv0\) attains error \(1\).

Thus even a bounded entire member of \(\mathcal A(D)\) need not admit uniform rational convergence on the whole negative ray.

### 2. A finite-limit entire counterexample with an algebraic lower bound

The failure is not repaired merely by requiring a finite limit at \(-\infty\). Define
\[
g(z)=e^z\sin(e^{-z}).
\]
This function is entire, satisfies \(|g(x)|\le e^x\le1\) on \(I\), and
\[
\lim_{x\to-\infty}g(x)=0.
\]
Nevertheless,
\[
\boxed{
E_n(g;I)\ge \frac{1}{(2n+\tfrac32)\pi}
\qquad(n\ge0).
}
\]
In particular, no constants \(C>0\) and \(\rho>1\) can satisfy
\[
E_n(g;I)\le C\rho^{-n}
\quad\text{for all }n.
\]

#### Proof

For
\[
a_k=(k+\tfrac12)\pi,\qquad x_k=-\log a_k,
\]
we have
\[
g(x_k)=\frac{(-1)^k}{a_k}.
\]
Take \(k=0,\ldots,2n+1\). Suppose \(r=p/q\in\mathcal R_n\) has
\[
\sup_{x\le0}|g(x)-r(x)|<\frac{1}{a_{2n+1}}.
\]
Then \(\operatorname{Re}r(x_k)\) has sign \((-1)^k\), so \(\operatorname{Re}r\) has at least \(2n+1\) distinct real zeros between consecutive \(x_k\)'s.

For real \(x\),
\[
\operatorname{Re}\frac{p(x)}{q(x)}
=
\frac{p(x)q^\#(x)+p^\#(x)q(x)}
     {2q(x)q^\#(x)},
\qquad
h^\#(z):=\overline{h(\overline z)}.
\]
The numerator has degree at most \(2n\), while the denominator is nonzero on \(I\). It therefore cannot have \(2n+1\) distinct zeros unless it vanishes identically, which is also incompatible with the forced alternating signs. This contradiction proves the bound.

This example shows that a finite limit at the unbounded endpoint is enough for qualitative shared-denominator convergence, but not for a geometric rate. Quantitative analytic continuation or an equivalent regularity condition is essential.

### 3. The conformal step in the published proof is incompatible with the slit domain

The proof of the cited Theorem 1 begins by postulating a conformal bijection
\[
\Phi:D\longrightarrow\{w:|w|>1\}
\]
with \(\Phi(\infty)=\infty\), and then defines \(g_D(z,\infty)=\log|\Phi(z)|\) and compact level curves from \(|\Phi|=\sigma\).

This geometry does not apply to \(D=\mathbb C\setminus(-\infty,0]\):

1. \(D\) is simply connected; for example, the principal square root maps it conformally onto a half-plane.
2. The plane domain \(\{w:|w|>1\}\) is not simply connected.
3. If the exterior disk is instead interpreted on the Riemann sphere with \(\infty\) included, then \(\infty\) is an interior point of that target, whereas \(\infty\) is a boundary point of \(D\) because the removed ray is unbounded.
4. No compact Jordan curve in \(D\) can enclose the entire unbounded ray in the ordinary planar sense.

Hence the stated exterior-domain Green-function normalization and the resulting contour construction cannot justify Theorem 1. The paper itself correctly uses a disk-to-slit conformal map earlier in its construction; the difficulty arises when the proof of the general theorem switches to compact-complement exterior geometry.

### 4. Consequences and scope

The counterexamples invalidate Theorem 1 and therefore the generality claimed for its shared-denominator Corollary 1. Any matrix statement whose proof invokes that theorem also requires hypotheses sufficient for the scalar approximation estimate used in the lifting argument.

This does **not** refute the paper's numerical shared-pole method for the specific \(\phi\)-functions. Those functions have much better behavior on the negative ray than arbitrary members of \(\mathcal A(D)\). In particular, \(\phi_0(x)=e^x\to0\) and \(\phi_\ell(x)=O(|x|^{-1})\) for \(\ell\ge1\) as \(x\to-\infty\). The reported numerical tables may therefore remain valid independently of the overbroad theorem.

A recent result of Schmelzer, *The `1/9'-problem for the \(\varphi\)-functions* (arXiv:2609.14489, 2026), proves the scalar best-approximation rate
\[
E_n(\varphi_\ell)^{1/n}\to H
\]
for every fixed \(\ell\), with \(H\) Halphen's constant. That scalar theorem does not by itself establish the same optimal rate for a finite family constrained to share one denominator. Thus the optimal common-pole asymptotic rate remains a separate question.

A viable repair of the 2025 general theorem must impose substantially more than analyticity in the slit domain. The paper's own trapezoidal argument requires the transformed integrand to extend analytically to a fixed annulus with suitable bounds. The examples above show, respectively, that one must at least control behavior at the unbounded endpoint and that endpoint convergence alone still does not imply geometric rational approximation.

## References

1. A. H. Al-Mohy, “Shared-Pole Carathéodory--Fejér Approximations for Linear Combinations of \(\phi\)-Functions,” *Mathematics* **13** (2025), 3985. https://doi.org/10.3390/math13243985
2. T. Schmelzer, “The `1/9'-problem for the \(\varphi\)-functions,” arXiv:2609.14489 (2026). https://arxiv.org/abs/2609.14489
