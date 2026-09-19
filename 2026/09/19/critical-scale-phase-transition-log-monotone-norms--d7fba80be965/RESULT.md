# Critical-scale phase transition in logarithmically monotone Marcinkiewicz renormings

## Result

Let
\[
\psi(t)=
\begin{cases}
t,&0<t\le 1,\\
1+\log t,&t>1,
\end{cases}
\qquad
\|h\|_{M_\psi}
=
\sup_{t>0}\frac{K_t(h)}{\psi(t)},
\]
where
\[
K_t(h)=\int_0^t h^*(s)\,ds.
\]
Use the scales introduced by Huang:
\[
L_0=0,\qquad L_1=4,\qquad L_n=L_{n-1}^2\quad(n\ge2),
\]
\[
T_n=e^{L_n},\qquad r_n=L_n-L_{n-1},\qquad
d_n=\frac{T_n}{1+L_n}.
\]
Then \(r_n/L_n\to1\).

The construction admits a useful generalization. Let \((\delta_n)\) be any sequence with
\[
0<\delta_n<1,\qquad \delta_n\to0,
\]
put
\[
p_n=1-\delta_n,
\]
and define
\[
A_n^\delta(h)
=
\left(
\frac1{T_n}\int_0^{T_n}(h^*(s))^{p_n}\,ds
\right)^{1/p_n},
\qquad
\Phi_\delta(h)
=
\limsup_{n\to\infty}d_n A_n^\delta(h).
\]

### Theorem 1: general moment family

For every such \((\delta_n)\), \(\Phi_\delta\) is a finite continuous symmetric lattice seminorm on \(M_\psi(0,\infty)\), satisfies
\[
0\le \Phi_\delta(h)\le \|h\|_{M_\psi},
\]
vanishes on bounded functions of finite-measure support, and is monotone under logarithmic submajorization:
\[
u\prec\!\prec_{\log}v
\quad\Longrightarrow\quad
\Phi_\delta(u)\le \Phi_\delta(v).
\]

Thus, for every \(\lambda>0\),
\[
N_{\lambda,\delta}(h)
=
\|h\|_{M_\psi}+\lambda\Phi_\delta(h)
\]
is an equivalent logarithmically monotone symmetric Banach norm.

### Theorem 2: subcritical-moment collapse to a fully symmetric tail seminorm

If
\[
\delta_n L_n\longrightarrow0,
\]
then, for every \(h\in M_\psi(0,\infty)\),
\[
\boxed{
\Phi_\delta(h)
=
\Theta(h)
:=
\limsup_{n\to\infty}
\frac{K_{T_n}(h)}{1+L_n}.
}
\]
Consequently \(\Phi_\delta\) is Hardy--Littlewood monotone,
\[
u\prec\!\prec v
\quad\Longrightarrow\quad
\Phi_\delta(u)\le\Phi_\delta(v),
\]
the norm \(N_{\lambda,\delta}\) is fully symmetric, and
\[
X_\delta:=\ker\Phi_\delta
\]
is a fully symmetric Banach function ideal with the restricted Marcinkiewicz norm.

### Theorem 3: exact critical response on Huang's extremal pair

Let
\[
f(t)=
\begin{cases}
1,&0<t\le1,\\
t^{-1},&t>1.
\end{cases}
\]
Set \(T_0=1\),
\[
I_n=(T_{n-1},T_n],\qquad
\Delta_n=T_n-T_{n-1},\qquad
a_n=\frac{r_n}{\Delta_n},
\]
and
\[
g(t)=
\begin{cases}
1,&0<t\le1,\\
a_n,&t\in I_n.
\end{cases}
\]
Huang proves that
\[
g\prec\!\prec f,
\qquad
\|g\|_{M_\psi}=\|f\|_{M_\psi}=1,
\qquad
K_{T_n}(g)=K_{T_n}(f)=1+L_n.
\]

For every sequence \(\delta_n\to0\),
\[
\boxed{\Phi_\delta(g)=1.}
\]
If
\[
\delta_nL_n\longrightarrow c\in[0,\infty],
\]
then
\[
\boxed{
\Phi_\delta(f)=F(c),
}
\]
where
\[
F(0)=1,\qquad
F(c)=\frac{1-e^{-c}}{c}\quad(0<c<\infty),\qquad
F(\infty)=0.
\]

Hence the scale \(\delta_nL_n\) gives a sharp three-regime boundary:

- if \(\delta_nL_n\to0\), the auxiliary seminorm is exactly the fully symmetric tail seminorm \(\Theta\);
- if \(\delta_nL_n\to c\in(0,\infty)\), then \(N_{\lambda,\delta}\) is not strongly symmetric, with the explicit gap \(1-F(c)\) on the pair \(g\prec\!\prec f\);
- if \(\delta_nL_n\to\infty\), then \(N_{\lambda,\delta}\) is not strongly symmetric and \(X_\delta\) is not solid under Hardy--Littlewood submajorization, because \(f\in X_\delta\), \(g\notin X_\delta\), and \(g\prec\!\prec f\).

In the last regime no equivalent fully symmetric norm can make \(X_\delta\) fully symmetric, since the obstruction is failure of the underlying set to be closed downward under Hardy--Littlewood submajorization.

### Corollary: sharp phase transition in Huang's power family

Huang takes
\[
\delta_n=r_n^{-\alpha}.
\]
The source paper restricts to \(0<\alpha\le1\), using \(\alpha=1\) for failure of strong symmetry and \(\alpha=\tfrac12\) for failure of Hardy--Littlewood solidity. The same formulas are well-defined for every \(\alpha>0\). Since \(r_n/L_n\to1\),
\[
L_n\delta_n=\frac{L_n}{r_n^\alpha}
\sim L_n^{1-\alpha}.
\]
Therefore
\[
\boxed{
\begin{array}{c|c|c|c}
\alpha&\Phi_\alpha(f)&\Phi_\alpha(g)&\text{order structure}\\ \hline
0<\alpha<1&0&1&N_{\lambda,\alpha}\text{ not strongly symmetric; }X_\alpha\text{ not HL-solid}\\
\alpha=1&1-e^{-1}&1&N_{\lambda,1}\text{ not strongly symmetric}\\
\alpha>1&1&1&N_{\lambda,\alpha}\text{ fully symmetric and }X_\alpha\text{ fully symmetric}
\end{array}}
\]
Thus \(\alpha=1\) is the exact transition scale: below it the kernel loses Hardy--Littlewood solidity, at it a nonzero strong-symmetry defect remains, and above it the moment correction collapses to a fully symmetric asymptotic Marcinkiewicz seminorm.

## Proof

### 1. The construction works for arbitrary \(\delta_n\to0\)

For \(0<p_n<1\), concavity of \(x\mapsto x^{p_n}\) gives
\[
A_n^\delta(h)
\le
\frac1{T_n}\int_0^{T_n}h^*(s)\,ds.
\]
Therefore
\[
d_nA_n^\delta(h)
\le
\frac{K_{T_n}(h)}{1+L_n}
\le
\|h\|_{M_\psi}.
\]

If \(\|h\|_\infty\le B\) and \(|\operatorname{supp}h|\le S<\infty\), then
\[
d_nA_n^\delta(h)
\le
\frac{B\,S^{1/p_n}}{1+L_n}
e^{-L_n\delta_n/p_n}
\le
\frac{B\,S^{1/p_n}}{1+L_n}\longrightarrow0.
\]

For subadditivity,
\[
|u+v|^{p_n}\le |u|^{p_n}+|v|^{p_n}
\]
and
\[
A_n^\delta(u+v)
\le
2^{1/p_n-1}\bigl(A_n^\delta(u)+A_n^\delta(v)\bigr).
\]
Because \(p_n\to1\), the prefactor tends to \(1\); taking limsups yields the triangle inequality for \(\Phi_\delta\). The same upper bound gives continuity.

Finally, the power-integral consequence of logarithmic submajorization used by Huang states that, for every \(q>0\),
\[
u\prec\!\prec_{\log}v
\quad\Longrightarrow\quad
\int_0^t(u^*)^q
\le
\int_0^t(v^*)^q
\qquad(t>0).
\]
Taking \(q=p_n\) gives \(A_n^\delta(u)\le A_n^\delta(v)\) for every \(n\), hence logarithmic monotonicity. None of these estimates requires a power-law choice of \(\delta_n\).

### 2. Proof of the fully symmetric regime

Fix \(h\in M_\psi\). The Marcinkiewicz estimate near the origin implies \(h^*\in L^\infty\); set
\[
B=\|h\|_\infty.
\]
If \(B=0\), the result is trivial. Define
\[
m_n=\frac1{T_n}K_{T_n}(h),
\qquad
b_n=d_nm_n=\frac{K_{T_n}(h)}{1+L_n}.
\]
The preceding Jensen estimate gives
\[
d_nA_n^\delta(h)\le b_n.
\]

For \(0\le x\le B\) and \(p_n=1-\delta_n\),
\[
x^{p_n}=x\,x^{-\delta_n}\ge x\,B^{-\delta_n}.
\]
Hence
\[
A_n^\delta(h)
\ge
m_n\left(\frac{m_n}{B}\right)^{\delta_n/p_n},
\]
and therefore
\[
d_nA_n^\delta(h)
\ge
b_n
\exp\!\left[
-\frac{\delta_n}{p_n}\log\frac{B}{m_n}
\right].
\]

Let
\[
\beta=\limsup b_n.
\]
If \(\beta=0\), the upper estimate already gives \(\Phi_\delta(h)=0=\beta\). If \(\beta>0\), choose a subsequence along which \(b_n\to\beta\) and eventually \(b_n\ge\beta/2\). Since
\[
m_n=b_n(1+L_n)e^{-L_n},
\]
along that subsequence
\[
\log\frac{B}{m_n}
\le
L_n-\log(1+L_n)+O_{B,\beta}(1).
\]
Thus, if \(\delta_nL_n\to0\),
\[
\frac{\delta_n}{p_n}\log\frac{B}{m_n}\longrightarrow0.
\]
The lower estimate then gives
\[
\Phi_\delta(h)\ge\beta.
\]
Together with the upper estimate,
\[
\Phi_\delta(h)=\beta=\Theta(h).
\]

If \(u\prec\!\prec v\), then \(K_t(u)\le K_t(v)\) for all \(t\), so \(\Theta(u)\le\Theta(v)\). This proves the stated full-symmetry consequences.

### 3. The exact critical response

For \(g\), restrict the \(p_n\)-moment integral to the last block \(I_n\). Since \(g=a_n=r_n/\Delta_n\) there,
\[
d_nA_n^\delta(g)
\ge
\frac{r_n}{1+L_n}
\left(\frac{\Delta_n}{T_n}\right)^{\delta_n/p_n}
=
\frac{r_n}{1+L_n}
(1-e^{-r_n})^{\delta_n/p_n}.
\]
Now
\[
\frac{r_n}{1+L_n}\to1,
\qquad
\frac{\delta_n}{p_n}\log(1-e^{-r_n})\to0,
\]
so the lower bound tends to \(1\). The Jensen estimate and \(K_{T_n}(g)=1+L_n\) give the reverse bound \(d_nA_n^\delta(g)\le1\). Thus
\[
\Phi_\delta(g)=1.
\]

For \(f\),
\[
\int_0^{T_n}f(t)^{p_n}\,dt
=
1+\frac{T_n^{\delta_n}-1}{\delta_n}
=
1+\frac{e^{q_n}-1}{\delta_n},
\qquad
q_n=L_n\delta_n.
\]
Consequently
\[
d_nA_n^\delta(f)
=
\frac{e^{-q_n/p_n}}{1+L_n}
\left(
1+\frac{e^{q_n}-1}{\delta_n}
\right)^{1/p_n}.
\]

If \(q_n\to c\in(0,\infty)\), then
\[
\frac1{L_n}
\left(
1+\frac{e^{q_n}-1}{\delta_n}
\right)
\longrightarrow
\frac{e^c-1}{c},
\]
while
\[
\delta_n\log L_n\longrightarrow0.
\]
Therefore
\[
d_nA_n^\delta(f)
\longrightarrow
e^{-c}\frac{e^c-1}{c}
=
\frac{1-e^{-c}}{c}.
\]

If \(q_n\to0\), Theorem 2 applies and \(K_{T_n}(f)=1+L_n\), so the limit is \(1\).

If \(q_n\to\infty\), then
\[
1+\frac{e^{q_n}-1}{\delta_n}
=
\delta_n^{-1}e^{q_n}(1+o(1)),
\]
and hence
\[
d_nA_n^\delta(f)
=
\frac{\delta_n^{-1/p_n}}{1+L_n}(1+o(1)).
\]
Since
\[
\frac{\delta_n^{-1/p_n}}{L_n}
=
\frac1{L_n\delta_n}
\exp\!\left(
\frac{\delta_n}{p_n}\log\frac1{\delta_n}
\right),
\]
the exponential factor tends to \(1\) while \(L_n\delta_n=q_n\to\infty\). Thus the limit is \(0\).

The order-theoretic conclusions follow from Huang's relation \(g\prec\!\prec f\) and the equality of the two Marcinkiewicz norms.

## Relation to prior literature and originality

Huang's arXiv:2609.20270v1 constructs the logarithmically monotone renorming above with the specific choice
\[
\delta_n=r_n^{-\alpha},\qquad 0<\alpha\le1.
\]
The paper proves the \(\alpha=1\) values
\[
\Phi(f)=1-e^{-1},\qquad \Phi(g)=1,
\]
to obtain a logarithmically monotone norm which is not strongly symmetric. It then specializes to \(\alpha=\tfrac12\), where
\[
\Phi(f)=0,\qquad \Phi(g)=1,
\]
to construct a strongly symmetric logarithmically solid space which is not Hardy--Littlewood solid.

The present result identifies the governing dimensionless scale \(L_n(1-p_n)\), extends the construction to arbitrary \(p_n\uparrow1\), computes the full critical response \(F(c)\), and proves that the same family re-enters the fully symmetric category precisely in the regime
\[
L_n(1-p_n)\to0.
\]
For the power family, this yields the exact boundary \(\alpha=1\) and the previously untreated fully symmetric phase \(\alpha>1\).

To the best of our knowledge, no prior source located in searches for the exact paper, logarithmic submajorization, Marcinkiewicz asymptotic seminorms, Hardy--Littlewood solidity, and the scale \(L_n(1-p_n)\) states this phase diagram or the identity \(\Phi_\delta=\Theta\) in the subcritical-moment regime.

Classical work on Marcinkiewicz ideals, Dixmier traces, and asymptotic functionals contains related fully symmetric tail quantities, while Dodds--Dodds--Sukochev--Zanin develops the logarithmic-submajorization framework used by Huang. Those theories are background rather than claimed new ingredients here. A residual prior-art risk remains that an equivalent asymptotic-moment transition appears in older singular-functional literature under different terminology.

## Limitations

The theorem concerns Huang's specific Marcinkiewicz scale \(T_n=e^{L_n}\) and the associated sparse limsup functional. It does not classify arbitrary choices of sampling scales, and no claim is made for sequences \(\delta_nL_n\) with genuinely oscillatory asymptotics beyond the stated regimes. The status of Hardy--Littlewood solidity of \(X_\delta\) in the finite positive critical regime is not determined here. No noncommutative operator-ideal analogue is asserted.

## References

1. Jinghao Huang, *A logarithmically monotone symmetric norm which is not fully symmetric*, arXiv:2609.20270v1 (2026). https://arxiv.org/abs/2609.20270
2. P. G. Dodds, T. K. Dodds, F. A. Sukochev and D. Zanin, *Logarithmic submajorization, uniform majorization and Hölder type inequalities for \(\tau\)-measurable operators*, Indagationes Mathematicae 31 (2020), 809--830. https://arxiv.org/abs/1910.10874
3. A. L. Carey, A. Rennie, A. Sedaev and F. A. Sukochev, *The Dixmier trace and asymptotics of zeta functions*, Journal of Functional Analysis 249 (2007), 253--283. https://arxiv.org/abs/math/0611629
