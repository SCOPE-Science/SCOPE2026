# Strict alpha-filtration of logarithmically monotone Marcinkiewicz kernels

## Statement

Let
\[
\psi(t)=
\begin{cases}
t,&0<t\le 1,\\
1+\log t,&t>1,
\end{cases}
\qquad
M_\psi=M_\psi(0,\infty),
\]
and use the scales from Huang's construction
\[
L_0=0,\quad L_1=4,\quad L_n=L_{n-1}^2,\quad
T_n=e^{L_n},\quad r_n=L_n-L_{n-1}.
\]
For \(0<\alpha\le 1\), put
\[
p_n^{(\alpha)}=1-r_n^{-\alpha},
\]
\[
A_n^{(\alpha)}(h)=
\left(\frac1{T_n}\int_0^{T_n}h^*(s)^{p_n^{(\alpha)}}\,ds\right)^{1/p_n^{(\alpha)}},
\]
and
\[
\Phi_\alpha(h)=
\limsup_{n\to\infty}
\frac{T_n}{1+L_n}A_n^{(\alpha)}(h),
\qquad
X_\alpha=\ker\Phi_\alpha.
\]

Huang proved that each \(\Phi_\alpha\) is a continuous symmetric lattice seminorm, monotone under logarithmic submajorization, and that each \(X_\alpha\) is a closed strongly symmetric Banach function ideal with the inherited \(M_\psi\)-norm.

The dependence on \(\alpha\) is in fact strict.

**Theorem.** If \(0<\alpha<\beta\le1\), then
\[
\Phi_\alpha(h)\le \Phi_\beta(h)\qquad(h\in M_\psi)
\]
and
\[
\boxed{X_\beta\subsetneq X_\alpha.}
\]
More precisely, for every \(0<\gamma<1\) there is a nonnegative decreasing
\(h_\gamma\in M_\psi\) such that
\[
\boxed{
\Phi_\alpha(h_\gamma)=
\begin{cases}
0,&0<\alpha<\gamma,\\
e^{-1},&\alpha=\gamma,\\
1,&\gamma<\alpha\le1.
\end{cases}
}
\]
Consequently \((X_\alpha)_{0<\alpha<1}\) is a continuum-sized strictly decreasing chain of logarithmically solid, strongly symmetric Banach function ideals. Every one of these spaces fails Hardy--Littlewood solidity and therefore admits no equivalent fully symmetric norm.

In addition, for every \(0<\alpha\le1\) and \(\lambda>0\),
\[
N_{\lambda,\alpha}(h)=\|h\|_{M_\psi}+\lambda\Phi_\alpha(h)
\]
is logarithmically monotone but not strongly symmetric. Thus the parameter in Huang's construction records a genuine concentration scale rather than an inessential choice.

## Proof

### 1. Monotonicity in the parameter

Fix \(n\). If \(0<\alpha<\beta\le1\), then
\[
p_n^{(\alpha)}<p_n^{(\beta)}.
\]
On the probability space \(([0,T_n],T_n^{-1}dt)\), Lyapunov's inequality for positive moments gives
\[
A_n^{(\alpha)}(h)\le A_n^{(\beta)}(h).
\]
Multiplication by \(T_n/(1+L_n)\) and passage to the limsup yield
\[
\Phi_\alpha(h)\le\Phi_\beta(h).
\]
Hence \(X_\beta\subseteq X_\alpha\).

### 2. A threshold probe at every exponent

Fix \(0<\gamma<1\), and set
\[
R_n=\exp(L_n-r_n^\gamma).
\]
For all sufficiently large \(n\), the sequence \(R_n\) is strictly increasing,
\[
R_n<T_n<R_{n+1},
\]
and, with
\[
\Delta_n'=R_n-R_{n-1},\qquad b_n=\frac{r_n}{\Delta_n'},
\]
the sequence \(b_n\) is strictly decreasing. Choose such an index \(N\), and define a decreasing function \(h_\gamma\) by
\[
h_\gamma(t)=
\begin{cases}
b_N,&0<t\le R_N,\\
b_n,&R_{n-1}<t\le R_n,\quad n>N.
\end{cases}
\]

For \(n>N\),
\[
\int_{R_{n-1}}^{R_n}h_\gamma(t)\,dt=r_n.
\]
Therefore
\[
\int_0^{R_n}h_\gamma(t)\,dt=L_n+O(1).
\]
Since
\[
\log R_n=L_n-r_n^\gamma\sim L_n,
\]
the endpoint Marcinkiewicz ratios remain bounded. For an interior point
\(t\in[R_{n-1},R_n]\), concavity of \(\log\) gives
\[
\frac{t-R_{n-1}}{R_n-R_{n-1}}
\le
\frac{\log t-\log R_{n-1}}{\log R_n-\log R_{n-1}},
\]
while
\[
\frac{r_n}{\log R_n-\log R_{n-1}}\longrightarrow1.
\]
It follows that
\[
\sup_{t>0}
\frac{\int_0^t h_\gamma(s)\,ds}{\psi(t)}<\infty,
\]
so \(h_\gamma\in M_\psi\).

Now fix \(0<\alpha\le1\), abbreviate
\[
p=p_n^{(\alpha)},\qquad \delta=1-p=r_n^{-\alpha},
\]
and put
\[
I_n=\int_0^{T_n}h_\gamma(t)^p\,dt.
\]
The contribution of the \(n\)-th compressed block is
\[
C_n
=
\Delta_n'b_n^p
=
r_n^p(\Delta_n')^\delta.
\]

The preceding blocks are negligible. Indeed, if
\[
M_{n-1}=\int_0^{R_{n-1}}h_\gamma(t)\,dt=O(L_{n-1}),
\]
then Jensen's inequality for \(x\mapsto x^p\) gives
\[
\int_0^{R_{n-1}}h_\gamma(t)^p\,dt
\le
R_{n-1}^\delta M_{n-1}^p,
\]
and hence, since \(R_{n-1}/\Delta_n'\to0\) and
\(M_{n-1}/r_n\to0\),
\[
\frac{\int_0^{R_{n-1}}h_\gamma^p}{C_n}\longrightarrow0.
\]

The part of the next block lying before \(T_n\) is also negligible:
\[
\int_{R_n}^{T_n}h_\gamma(t)^p\,dt
\le
T_n b_{n+1}^p=o(C_n).
\]
This follows from
\[
\log b_{n+1}
=
-L_{n+1}+r_{n+1}^\gamma+O(\log r_{n+1}),
\]
whereas all positive terms in the logarithm of the ratio are
\(o(L_{n+1})\). Thus
\[
I_n\sim C_n.
\]

Consequently,
\[
\begin{aligned}
\frac{T_n}{1+L_n}
\left(\frac{I_n}{T_n}\right)^{1/p}
&\sim
\frac{r_n}{1+L_n}
\exp\left(
\frac{\delta}{p}(\log\Delta_n'-L_n)
\right)\\
&=
\frac{r_n}{1+L_n}
\exp\left(
-\frac{r_n^{\gamma-\alpha}}{p}+o(1)
\right),
\end{aligned}
\]
because
\[
\log\Delta_n'=L_n-r_n^\gamma+o(1).
\]
Since \(r_n/(1+L_n)\to1\) and \(p\to1\), the displayed quantity converges to
\(0\), \(e^{-1}\), or \(1\) according as
\(\alpha<\gamma\), \(\alpha=\gamma\), or \(\alpha>\gamma\).
This proves the asserted formula for \(\Phi_\alpha(h_\gamma)\).

If \(0<\alpha<\beta\le1\), choose
\(\gamma\in(\alpha,\beta)\). Then
\[
h_\gamma\in X_\alpha,\qquad h_\gamma\notin X_\beta,
\]
so \(X_\beta\subsetneq X_\alpha\).

### 3. Every interior kernel has the same Hardy--Littlewood obstruction

Use Huang's decreasing functions
\[
f(t)=
\begin{cases}
1,&0<t\le1,\\
t^{-1},&t>1,
\end{cases}
\]
and
\[
g(t)=
\begin{cases}
1,&0<t\le1,\\
a_n,&T_{n-1}<t\le T_n,
\end{cases}
\qquad
a_n=\frac{r_n}{T_n-T_{n-1}}.
\]
Huang proved
\[
g\prec\!\prec f,\qquad
\|f\|_{M_\psi}=\|g\|_{M_\psi}=1.
\]

For \(0<\alpha<1\), with
\(\delta=r_n^{-\alpha}\) and \(p=1-\delta\),
\[
\int_0^{T_n}f(t)^p\,dt
=
1+\frac{T_n^\delta-1}{\delta}
\le
2\delta^{-1}T_n^\delta
\]
for all sufficiently large \(n\). Hence
\[
\frac{T_n}{1+L_n}A_n^{(\alpha)}(f)
\le
\frac{2^{1/p}r_n^{\alpha/p}}{1+L_n}
\longrightarrow0.
\]
Thus
\[
\Phi_\alpha(f)=0\qquad(0<\alpha<1).
\]

For \(g\), the \(n\)-th block gives
\[
\frac{T_n}{1+L_n}A_n^{(\alpha)}(g)
\ge
\frac{r_n}{1+L_n}
(1-e^{-r_n})^{1/p-1}
\longrightarrow1,
\]
while Huang's general estimate
\[
\frac{T_n}{1+L_n}A_n^{(\alpha)}(g)
\le
\frac{K_{T_n}(g)}{\psi(T_n)}=1
\]
gives
\[
\Phi_\alpha(g)=1
\qquad(0<\alpha\le1).
\]

Therefore, for every \(0<\alpha<1\),
\[
f\in X_\alpha,\qquad g\notin X_\alpha,\qquad g\prec\!\prec f.
\]
So \(X_\alpha\) is not solid under Hardy--Littlewood submajorization. Since a fully symmetric norm necessarily has Hardy--Littlewood-solid domain, no equivalent fully symmetric norm exists on \(X_\alpha\).

Finally, the same pair proves that every \(N_{\lambda,\alpha}\) fails strong symmetry. For \(0<\alpha<1\),
\[
N_{\lambda,\alpha}(g)=1+\lambda>1=N_{\lambda,\alpha}(f),
\]
despite \(g\prec\!\prec f\). At \(\alpha=1\), Huang computed
\[
\Phi_1(f)=1-e^{-1},\qquad \Phi_1(g)=1,
\]
which gives the same strict reversal.

## Interpretation

The parameter \(\alpha\) measures a concentration exponent. The probe \(h_\gamma\) places the \(r_n\)-sized mass of the \(n\)-th logarithmic block into a relative portion approximately
\[
\exp(-r_n^\gamma)
\]
of its ambient scale. The normalized \(p_n^{(\alpha)}\)-moment then sees exactly the product
\[
r_n^{-\alpha}r_n^\gamma=r_n^{\gamma-\alpha},
\]
producing a sharp transition at \(\alpha=\gamma\). Thus Huang's one-parameter family contains a continuum of genuinely different kernels, rather than two isolated examples corresponding to the special choices \(\alpha=1\) and \(\alpha=1/2\).

## Relation to prior literature and originality

Huang's current arXiv version defines the construction for all
\(\alpha\in(0,1]\), but specializes to \(\alpha=1\) for the non-strongly-symmetric norm and to \(\alpha=1/2\) for the non-fully-symmetric kernel. It does not state monotone nesting of the kernels, strictness of that nesting, or threshold probes with the above \(0/e^{-1}/1\) phase diagram.

Earlier work of Kalton and Sukochev constructs singular rearrangement-invariant functionals on Marcinkiewicz spaces that need not be Hardy--Littlewood symmetric. That broad phenomenon is prior art and is not claimed here. The contribution claimed here is specifically the exact parameter ordering and strict continuum filtration inside Huang's explicit 2026 family, together with the concentration-scale probes that distinguish every pair of parameters.

Originality is therefore asserted only to the best of our knowledge.

## Limitations

- The theorem concerns Huang's specific \(\psi\), scales \(L_n,T_n,r_n\), and moment seminorms \(\Phi_\alpha\); it is not a classification of logarithmically monotone seminorms on arbitrary Marcinkiewicz spaces.
- The spaces \(X_\alpha\) are proved distinct as embedded subspaces of the same \(M_\psi\). No claim is made that they are pairwise non-isomorphic as abstract Banach lattices.
- The Hardy--Littlewood obstruction is established here for \(0<\alpha<1\). No claim is made about full symmetry of the endpoint kernel \(X_1\).
- No noncommutative/operator-ideal analogue of the strict filtration is claimed.

## References

1. J. Huang, *A logarithmically monotone symmetric norm which is not fully symmetric*, arXiv:2609.20270v1 (2026). https://arxiv.org/abs/2609.20270
2. N. J. Kalton and F. A. Sukochev, *Rearrangement-Invariant Functionals with Applications to Traces on Symmetrically Normed Ideals*, Canad. Math. Bull. 51 (2008), 67--80. https://doi.org/10.4153/CMB-2008-009-3
3. N. J. Kalton and F. A. Sukochev, *Symmetric norms and spaces of operators*, J. Reine Angew. Math. 621 (2008), 81--121. https://doi.org/10.1515/CRELLE.2008.059
