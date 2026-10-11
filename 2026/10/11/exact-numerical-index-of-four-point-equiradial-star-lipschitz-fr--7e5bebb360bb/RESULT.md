# Exact numerical index of four-point equiradial star Lipschitz-free spaces

## Finding
For every real \(\tfrac12\le t\le1\), let \(M_t=\{o,a_1,a_2,a_3\}\) have distances \(d(o,a_i)=t\) and \(d(a_i,a_j)=1\) when \(i\ne j\). The real Lipschitz-free space \(X_t=\mathcal F(M_t)\) has the exact numerical index
\[
n(X_t)=\frac{1+3(2t-1)}{1+6(2t-1)+(2t-1)^2}.
\]
In particular the index decreases strictly from \(1\) at the star-tree endpoint \(t=1/2\) to \(1/2\) at the equilateral endpoint \(t=1\). The formula includes both endpoints.

## Assumptions and scope
The scalar field is real. The numerical radius of an operator \(T:X\to X\) is
\[
v(T)=\sup\{|x^*(Tx)|:\|x\|=\|x^*\|=1,\ x^*(x)=1\},
\quad n(X)=\inf_{\|T\|=1}v(T).
\]
Identify \(X_t\) with \(\mathbb R^3\) by the vectors \(e_i=\delta_{a_i}\), with \(\delta_o=0\). Put \(q=2t-1\in[0,1]\) and \(R=(1+6q+q^2)/(1+3q)\). The unit ball is the convex hull of the twelve molecules
\[
P=\{\pm e_i/t:1\le i\le3\}\cup\{\pm(e_i-e_j):1\le i<j\le3\}.
\]
The dual Lipschitz unit ball is \(Q=\{f: |f_i|\le t,\ |f_i-f_j|\le1\}\). It is the convex hull of the fourteen potentials \(\pm u\), \(\pm f_S\), where \(u=(t,t,t)\) and \((f_S)_i=t\) for \(i\in S\), \((f_S)_i=t-1\) otherwise, and \(S\) ranges over the six nonempty proper subsets of \(\{1,2,3\}\). This generating list remains valid at both parameter endpoints, with possible redundancy.

## Proof
**Polyhedral reduction.** For an operator \(T\), its norm is \(\max_{p\in P,\ f\in Q}|f(Tp)|\). Its numerical radius is
\[
v(T)=\max\{|f(Tp)|:p\in P,\ f\in Q,\ f(p)=1\}.
\]
Here \(Q\) can be restricted to the fourteen listed extreme or generating potentials. Indeed, every unit vector is a convex combination of the finitely many molecule vertices, and on each duality slice \(f(x)=1\) only the molecules supported by \(f\) can occur, so the largest absolute pairing is attained by a supported molecule. For an arbitrary norm-one functional one may maximize over the vertices of the corresponding dual face, which are among the displayed potentials. Hence it suffices to bound every pairing \(f(Tp)\) by \(R v(T)\).

**Universal estimate.** By symmetry choose \(f=u\) or \(f=f_S\), while retaining both molecule orientations. If \(p=e_i/t\) and \(f_i=t\), then \(f(p)=1\), hence \(|f(Tp)|\le v(T)\). If \(p=e_i/t\) and \(f_i=t-1\), choose a displayed positive potential \(g\) with \(g_i=t\) and with \(g_j=t-1\) exactly when \(f_j=t\) for \(j\ne i\) (otherwise \(g_j=t\)). Then \(f=(q/t)u-g\), and both \(u\) and \(g\) support \(e_i/t\). Thus
\[
|f(Tp)|\le(1+q/t)v(T)\le Rv(T).
\]
If \(p=e_j-e_i\) and \(|f_j-f_i|=1\), either \(f\) or \(-f\) supports \(p\), so \(|f(Tp)|\le v(T)\). Otherwise \(f_i=f_j\). If the common value is \(t\), then both \(f(e_i/t)=f(e_j/t)=1\), and
\[
|f(T(e_j-e_i))|\le2t\,v(T)=(1+q)v(T)\le Rv(T).
\]
If \(f_i=f_j=t-1\), let \(k\) denote the remaining index, which must have \(f_k=t\). Define potentials by their coordinates in order \((i,j,k)\):
\[
g=(t,t,t-1),\quad h=(t-1,t,t),\quad \ell=(-t,1-t,-t),
\]
all belonging to the displayed signed generating set. The first potential supports both \(e_i/t\) and \(e_j/t\); the last two support \(p=e_j-e_i\). Put
\[
A=\frac{(1+q)^2}{2(1+3q)},\qquad B=\frac{2q}{1+3q}.
\]
Direct substitution gives the *exact identity of functionals* \(f=-(A/t)g+B(h-\ell)\). Consequently,
\[
\begin{aligned}
|f(Tp)|&\le A\bigl(|g(T(e_i/t))|+|g(T(e_j/t))|\bigr)\\
&\quad+B\bigl(|h(Tp)|+|\ell(Tp)|\bigr)\\
&\le(2A+2B)v(T)=Rv(T).
\end{aligned}
\]
The two elementary comparisons used above are
\[
R-(1+q)=\frac{2q(1-q)}{1+3q}\ge0,
\qquad R-\left(1+\frac q t\right)=\frac{q(1-q)^2}{(1+q)(1+3q)}\ge0.
\]
Negating \(p\) or \(f\) preserves the absolute pairing and the support condition, so the listed cases cover all molecule/potential pairs. Thus \(\|T\|\le Rv(T)\), and \(n(X_t)\ge1/R\).

**Sharp operator.** Set \(c=q(1-q)/(1+3q)\) and consider, in the basis \((e_1,e_2,e_3)\),
\[
S=\begin{pmatrix}
c&-c-q&-t\\ c+q&-c&t\\c-1&1-c&0
\end{pmatrix}.
\]
To verify its numerical radius without numerical optimization, enumerate the displayed twelve molecules and fourteen signed potentials for which \(f(p)=1\). Every value \(f(Sp)\) belongs to the following explicit list (the signs may occur separately):
\[
0,\quad\pm1,\quad\pm\frac{1-q}{1+3q},\quad
\pm\frac{1+q+2q^2}{1+3q},\quad
\pm\frac{1+6q+q^2}{2(1+3q)},\quad
\pm\frac{1+q}{2},\quad
\pm\frac{(1+q)^2}{1+3q}.
\]
This finite symbolic list is obtained by substituting the given coordinates into \(f(Sp)\), checking the support equation, and simplifying. Each listed modulus is at most \(1\) for \(0\le q\le1\): the nonobvious checks reduce respectively to \(2q(q-1)\le0\), \(q^2\le1\), and \(q(q-1)\le0\). The list contains both \(1\) and \(-1\), so \(v(S)=1\). For \(p=e_2-e_1\) and \(f=(t-1,t-1,t)\), which lies in \(Q\) although \(f(p)=0\), direct multiplication gives
\[
f(Sp)=\frac{1+6q+q^2}{1+3q}=R.
\]
The universal estimate yields \(\|S\|\le Rv(S)=R\), while this pairing shows \(\|S\|\ge R\). Thus \(\|S\|=R\), and the normalized operator \(S/R\) attains \(n(X_t)=1/R\). Finally \(d((1+3q)/(1+6q+q^2))/dq=-(3+2q+3q^2)/(1+6q+q^2)^2<0\) on \([0,1]\), proving strict interpolation.

## Verification
The upper bound uses exact convex generating lists and finitely many exact support identities, not sampling. The candidate matrix has all supported pairings determined by a closed symbolic list; substitution verifies the critical equality. Finite-dimensional linear-programming instances at rational parameters and independent symbolic simplification agreed with the formula, serving only as diagnostics. The analytic argument establishes every real parameter \(t\in[1/2,1]\).

## Relationship to prior work
Cobollo, Guirao, and Montesinos (2023, arXiv:2304.13183v1) determine the numerical index of **two-dimensional** Lipschitz-free spaces over three-point metrics; their theorem does not cover the four-point, three-dimensional spaces above. Sain, Paul, Bhunia, and Bag (2018, arXiv:1809.04778v2) develop finite-dimensional polyhedral numerical-index methods and exact results for other special polyhedra, but do not give this interpolating star family or its exact formula. The equilateral endpoint and related graph metrics have separate index calculations; the novel claim here is the complete explicit continuum between the two endpoints.

## Limitations
The result concerns real scalars, exactly three leaves, and equal center-to-leaf distances. No assertion is made for unequal weights, other dimensions, or complex scalar fields. Independent mathematical audit has not been performed.

## References
1. Ch. Cobollo, A. J. Guirao, V. Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces* (2023), arXiv:2304.13183v1, https://arxiv.org/abs/2304.13183.
2. D. Sain, K. Paul, P. Bhunia, S. Bag, *On the numerical index of polyhedral Banach spaces* (2018), arXiv:1809.04778v2, https://arxiv.org/abs/1809.04778.
