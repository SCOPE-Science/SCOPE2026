# Strict Sobolev–BV separation for exceptional BSVY spaces

## Result

Let \(N\ge 1\) and \(\gamma\in[-1,0)\). For a measurable function \(u\) on \(\mathbb R^N\), write
\[
Q_\gamma u(x,y)=\frac{u(x)-u(y)}{|x-y|^{1+\gamma}},
\qquad
d\nu_{N,\gamma}(x,y)=|x-y|^{\gamma-N}\,dx\,dy,
\]
and
\[
[u]_{N,\gamma}
:=\sup_{\lambda>0}\lambda\,
\nu_{N,\gamma}\bigl(\{(x,y):|Q_\gamma u(x,y)|>\lambda\}\bigr).
\]
Following Brezis–Seeger–Van Schaftingen–Yung and Chen–Yang–Yuan–Zhang, define
\[
\dot W_N^{1,1}(\gamma)
=\{u\in \dot W^{1,1}(\mathbb R^N):[u]_{N,\gamma}<\infty\},
\]
\[
\dot{BV}_N(\gamma)
=\{u\in \dot{BV}(\mathbb R^N):[u]_{N,\gamma}<\infty\}.
\]
The natural inclusion \(\dot W_N^{1,1}(\gamma)\subset \dot{BV}_N(\gamma)\) is strict throughout the exceptional range:
\[
\boxed{
\dot W_N^{1,1}(\gamma)\subsetneq \dot{BV}_N(\gamma)
\qquad(N\ge1,\ -1\le\gamma<0).
}
\]

There is a sharp change in the type of singularity that witnesses strictness.

- If \(-1<\gamma<0\), the characteristic function of a cube already lies in \(\dot{BV}_N(\gamma)\setminus\dot W_N^{1,1}(\gamma)\).
- At the endpoint \(\gamma=-1\), every nontrivial jump across a flat interface has infinite BSVY quasi-seminorm. Nevertheless a compactly supported continuous Cantor-staircase construction lies in \(\dot{BV}_N(-1)\setminus\dot W_N^{1,1}(-1)\).

Thus the exceptional BSVY hierarchy contains a genuine Sobolev–BV gap even at the endpoint where jump singularities are excluded.

## 1. The open exceptional range \(-1<\gamma<0\)

Let \(Q=(0,1)^N\) and \(u=\mathbf 1_Q\). Since \(u\in BV(\mathbb R^N)\setminus W^{1,1}(\mathbb R^N)\), it remains only to prove \([u]_{N,\gamma}<\infty\).

Put
\[
R_\lambda=\lambda^{-1/(1+\gamma)}.
\]
For a characteristic function, \(|u(x)-u(y)|\) is either \(0\) or \(1\). With \(h=y-x\), one therefore has the exact identity
\[
\nu_{N,\gamma}\bigl(\{|Q_\gamma u|>\lambda\}\bigr)
=
\int_{|h|<R_\lambda}
|h|^{\gamma-N}\,|Q\triangle(Q-h)|\,dh.
\]
For the unit cube,
\[
|Q\triangle(Q-h)|\le C_N\min\{|h|,1\}.
\]
If \(R_\lambda\le1\), polar coordinates give
\[
\nu_{N,\gamma}(\{|Q_\gamma u|>\lambda\})
\le C_{N,\gamma}\int_0^{R_\lambda}r^\gamma\,dr
=C_{N,\gamma}R_\lambda^{1+\gamma},
\]
and hence
\[
\lambda\,
\nu_{N,\gamma}(\{|Q_\gamma u|>\lambda\})
\le C_{N,\gamma},
\]
because \(\lambda R_\lambda^{1+\gamma}=1\).

If \(R_\lambda>1\), then \(\lambda<1\), and
\[
\nu_{N,\gamma}(\{|Q_\gamma u|>\lambda\})
\le C_N\left(
\int_0^1r^\gamma\,dr+
\int_1^{R_\lambda}r^{\gamma-1}\,dr
\right)
\le C_{N,\gamma},
\]
since \(\gamma<0\). Multiplication by \(\lambda<1\) again gives a uniform bound. Therefore
\[
\mathbf1_Q\in\dot{BV}_N(\gamma)\setminus\dot W_N^{1,1}(\gamma),
\qquad -1<\gamma<0.
\]

The same estimate works for any bounded set of finite perimeter, using the standard translation inequality
\[
|E\triangle(E-h)|\le |h|P(E).
\]

## 2. Why a jump fails at \(\gamma=-1\)

At \(\gamma=-1\), the quotient has no distance factor:
\[
Q_{-1}u(x,y)=u(x)-u(y),
\qquad
d\nu_{N,-1}(x,y)=|x-y|^{-N-1}\,dx\,dy.
\]
For \(u=\mathbf1_Q\) and any \(0<\lambda<1\),
\[
\nu_{N,-1}(\{|Q_{-1}u|>\lambda\})
=
\int_{\mathbb R^N}|h|^{-N-1}|Q\triangle(Q-h)|\,dh.
\]
On a fixed positive-measure cone of sufficiently small translations transverse to one face of the cube,
\[
|Q\triangle(Q-h)|\ge c_N|h|.
\]
Consequently the contribution of that cone is bounded below by a positive constant times
\[
\int_0^\varepsilon \frac{dr}{r}=\infty.
\]
Thus a codimension-one jump has infinite endpoint quasi-seminorm. The open-range witness does not survive at \(\gamma=-1\).

## 3. A Cantor witness at the endpoint in one dimension

Let \(C\subset[0,1]\) be the middle-third Cantor set, let \(\mu_C\) be the standard Cantor probability measure, and let
\[
F(x)=\mu_C(( -\infty,x])
\]
be the Cantor distribution function, extended by \(F=0\) on \(( -\infty,0]\) and \(F=1\) on \([1,\infty)\). Set
\[
\alpha=\frac{\log2}{\log3},
\qquad
v(x)=F(x)-F(x-2).
\]
Then \(v\) is continuous, supported in \([0,3]\), and belongs to \(BV(\mathbb R)\). Its distributional derivative is
\[
Dv=\mu_C-\tau_2\mu_C,
\]
a nonzero singular continuous measure. Hence
\[
v\notin W^{1,1}(\mathbb R).
\]

Two standard Cantor estimates will be used. There are constants \(A,B<\infty\) such that, for \(0<h\le1\),
\[
|v(x+h)-v(x)|\le Ah^\alpha
\quad\text{for all }x,
\]
and, with
\[
K=C\cup(C+2),
\]
the \(h\)-neighborhood of \(K\) satisfies
\[
|K_h|\le Bh^{1-\alpha}.
\]
Both follow directly from the generation-\(m\) Cantor construction: there are \(2^m\) basic intervals of length \(3^{-m}\), while each basic interval has Cantor mass \(2^{-m}=3^{-m\alpha}\).

For \(h>0\), define
\[
m_\lambda(h)
=
\bigl|\{x:|v(x+h)-v(x)|>\lambda\}\bigr|.
\]
If \(0<h\le1\) and \(v(x+h)\ne v(x)\), then \([x,x+h]\) meets \(K\), because \(v\) is locally constant off \(K\). Hence
\[
m_\lambda(h)
\le Bh^{1-\alpha}
\mathbf1_{\{h\ge(\lambda/A)^{1/\alpha}\}}
\qquad(0<h\le1),
\]
up to an immaterial adjustment of constants when the lower cutoff exceeds one. Since \(0\le v\le1\), the level set is empty for \(\lambda\ge1\). For \(0<\lambda<1\),
\[
\lambda\int_0^1m_\lambda(h)h^{-2}\,dh
\le
B\lambda\int_{(\lambda/A)^{1/\alpha}}^1h^{-1-\alpha}\,dh
\le C.
\]
For \(h\ge1\), the compact support gives \(m_\lambda(h)\le6\), and therefore
\[
\lambda\int_1^\infty m_\lambda(h)h^{-2}\,dh\le6.
\]
By symmetry,
\[
\nu_{1,-1}(\{|v(x)-v(y)|>\lambda\})
=2\int_0^\infty m_\lambda(h)h^{-2}\,dh.
\]
Taking the supremum in \(\lambda\) proves
\[
[v]_{1,-1}<\infty.
\]
Thus
\[
\boxed{
v\in\dot{BV}_1(-1)\setminus\dot W_1^{1,1}(-1).
}
\]

This is the endpoint singularity mechanism: the Cantor staircase is Hölder just strongly enough, and its singular support is thin just strongly enough, for the two exponents to cancel in the weak difference-quotient integral.

## 4. Lifting the endpoint witness to every dimension

Let \(N\ge2\), put \(d=N-1\), choose a nonzero \(\psi\in C_c^\infty(\mathbb R^d)\), and define
\[
V(x_1,x')=v(x_1)\psi(x').
\]
Then \(V\in BV(\mathbb R^N)\). Moreover the \(x_1\)-derivative contains the nonzero singular measure
\[
\psi(x')\,dx'\otimes Dv,
\]
so \(V\notin W^{1,1}(\mathbb R^N)\).

It remains to bound \([V]_{N,-1}\). Decompose
\[
V(x_1,x')-V(y_1,y')=A+B,
\]
where
\[
A=(v(x_1)-v(y_1))\psi(x'),
\qquad
B=v(y_1)(\psi(x')-\psi(y')).
\]
The elementary inclusion
\[
\{|A+B|>\lambda\}
\subset
\{|A|>\lambda/2\}\cup\{|B|>\lambda/2\}
\]
reduces the estimate to the two terms separately.

For \(A\), integrate first in \(y'\). For \(a>0\),
\[
\int_{\mathbb R^d}
(a^2+|z|^2)^{-(N+1)/2}\,dz
=C_Na^{-2}.
\]
Thus the \(A\)-contribution reduces, after integration in \(x'\), to the one-dimensional endpoint quasi-seminorm of \(v\), weighted by \(|\psi(x')|\). It is finite because \([v]_{1,-1}<\infty\) and \(\psi\in L^1\).

For \(B\), integrate first in \(x_1\). For \(r>0\),
\[
\int_{\mathbb R}
(s^2+r^2)^{-(N+1)/2}\,ds
=C_Nr^{-N}=C_Nr^{-(d+1)}.
\]
The \(B\)-contribution therefore reduces to the \(d\)-dimensional endpoint quasi-seminorm of \(\psi\), weighted by \(|v(y_1)|\). A compactly supported Lipschitz function has finite endpoint quasi-seminorm: if \(L=\operatorname{Lip}(\psi)\), then
\[
|\psi(x')-\psi(y')|>\eta
\quad\Longrightarrow\quad
|x'-y'|>\eta/L,
\]
and the fact that at least one of the two points lies in a fixed compact set gives
\[
\eta\iint_{|\psi(x')-\psi(y')|>\eta}
|x'-y'|^{-d-1}\,dx'\,dy'
\le C_{d,\psi}.
\]
Since \(v\in L^1\), the \(B\)-contribution is finite as well. Therefore
\[
[V]_{N,-1}<\infty,
\]
and
\[
\boxed{
V\in\dot{BV}_N(-1)\setminus\dot W_N^{1,1}(-1)
\qquad(N\ge2).
}
\]
Together with the one-dimensional construction and the cube argument for \(-1<\gamma<0\), this proves the theorem in every dimension and throughout \([-1,0)\).

## Context

Brezis, Seeger, Van Schaftingen and Yung introduced the exceptional spaces \(\dot W^{1,1}(\gamma)\) and \(\dot{BV}(\gamma)\) while studying weak difference-quotient formulas for first-order Sobolev norms. In the negative range they asked how these spaces fit among familiar first-order spaces.

Chen, Yang, Yuan and Zhang subsequently proved, for every \(\gamma\in[-1,0)\), that the homogeneous Hardy–Sobolev space embeds strictly into each of \(\dot W^{1,1}(\gamma)\) and \(\dot{BV}(\gamma)\), and proved non-normability of the corresponding quotients. Their argument also uses the natural inclusion
\[
\dot W_N^{1,1}(\gamma)\subset\dot{BV}_N(\gamma),
\]
but the inspected theorem statements and proof do not state strictness of this mutual inclusion.

The result above supplies that missing separation. Combined with the recent Hardy–Sobolev strict embedding, it gives the strict chain
\[
\dot H^{1,1}
\subsetneq
\dot W_N^{1,1}(\gamma)
\subsetneq
\dot{BV}_N(\gamma)
\]
for every \(\gamma\in[-1,0)\).

The endpoint construction also distinguishes the singularities admitted by the spaces: jumps work for \(-1<\gamma<0\), fail logarithmically at \(\gamma=-1\), while a singular-continuous Cantor derivative remains admissible.

## Limitations

The theorem establishes strict Sobolev–BV separation, not an intrinsic characterization of \(\dot{BV}_N(\gamma)\). At \(\gamma=-1\) it supplies one singular-continuous witness but does not classify which singular BV derivatives have finite endpoint quasi-seminorm. No claim is made at \(\gamma=0\).

For \(-1<\gamma<0\), the jump-function argument is elementary once the question is isolated, so an unindexed or informal prior observation remains possible. The most closely related source on the exceptional range is very recent, which also leaves a residual risk of parallel observations not yet indexed.

## References

1. Y. Chen, D. Yang, W. Yuan, Y. Zhang, *On Two Questions by Brezis et al Concerning the Critical Difference Quotient Characterization of First-Order Sobolev Spaces*, arXiv:2609.19029 (2026).
2. H. Brezis, A. Seeger, J. Van Schaftingen, P.-L. Yung, *Families of functionals representing Sobolev norms*, Analysis & PDE 17 (2024), 943–979.
3. N. Picenni, *New estimates for a class of non-local approximations of the total variation*, J. Funct. Anal. 287 (2024); arXiv:2307.16471.
