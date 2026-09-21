# Exact s-number profiles for weighted composition operators on C(K)-spaces

## Statement

Let \(K\) and \(L\) be compact Hausdorff spaces, over either the real or complex scalar field. Let
\[
\phi:L\to K
\]
be continuous and let \(u\in C(L)\). Consider the weighted composition operator
\[
T:C(K)\to C(L),\qquad
(Tf)(x)=u(x)f(\phi(x)).
\]

For \(t\ge 0\), define the threshold image
\[
A_t:=\phi\bigl(\{x\in L:|u(x)|>t\}\bigr),
\qquad
N(t):=\#A_t\in \mathbb N\cup\{0,\infty\}.
\]
For \(n\ge1\), put
\[
\eta_n(T):=\inf\{t\ge0:N(t)<n\}.
\]
Equivalently, if
\[
\omega(y):=\max\{|u(x)|:\phi(x)=y\},
\qquad y\in\phi(L),
\]
then \((\eta_n)\) is the decreasing counting rearrangement of the fiber-maximal weights \(\omega(y)\).

**Theorem.** For every \(n\ge1\),
\[
\boxed{
a_n(T)=b_n(T)=c_n(T)=d_n(T)=\eta_n(T),
}
\]
where \(a_n,b_n,c_n,d_n\) are respectively the approximation, Bernstein, Gelfand and Kolmogorov numbers, with the standard rank/dimension/codimension convention \(<n\).

Let
\[
\rho(T):=\lim_{n\to\infty}\eta_n(T)
=\inf\{t\ge0:N(t)<\infty\}.
\]
Then
\[
\boxed{
\operatorname{dist}(T,\mathcal K)
=\operatorname{dist}(T,\mathcal W)
=\operatorname{dist}(T,\mathcal{FSS})
=\operatorname{dist}(T,\mathcal{SS})
=\rho(T),
}
\]
where \(\mathcal K,\mathcal W,\mathcal{FSS},\mathcal{SS}\) denote the compact, weakly compact, finitely strictly singular and strictly singular operators from \(C(K)\) to \(C(L)\).

In particular,
\[
T\text{ compact}
\iff T\text{ weakly compact}
\iff T\text{ finitely strictly singular}
\iff T\text{ strictly singular}
\iff \rho(T)=0.
\]
Moreover, whenever \(t<\rho(T)\), there is an isometric copy \(E\simeq c_0\) in \(C(K)\) such that
\[
\|Tf\|\ge t\|f\|\qquad(f\in E).
\]
Thus every noncompact weighted composition operator in this class fixes an isomorphic copy of \(c_0\), quantitatively at every level below its common ideal distance.

## Proof

### 1. Finite-rank approximation above a threshold

Fix \(n\ge1\) and \(t>\eta_n(T)\). Then \(F=A_t\) is finite and \(|F|<n\). Choose \(s>t\).

Because \(F\) is a finite subset of the compact Hausdorff space \(K\), choose pairwise disjoint open neighborhoods \(O_y\) of the points \(y\in F\). Set
\[
U_t=\{x\in L:|u(x)|>t\},
\qquad
V_y=U_t\cap\phi^{-1}(O_y).
\]
For \(x\in V_y\), one has \(\phi(x)\in F\cap O_y=\{y\}\); hence \(\phi\) is identically \(y\) on \(V_y\).

The compact set
\[
K_y=\{x\in L:|u(x)|\ge s,\ \phi(x)=y\}
\]
is contained in \(V_y\). By normality of compact Hausdorff spaces, choose \(h_y\in C(L)\) with
\[
0\le h_y\le1,\qquad
h_y=1\text{ on }K_y,\qquad
\operatorname{supp}h_y\subset V_y.
\]
Define
\[
Rf=\sum_{y\in F}u\,h_y\,f(y).
\]
This has rank at most \(|F|<n\). On the support of \(h_y\), \(\phi=y\), and wherever \(T-R\) is nonzero one has \(|u|<s\). Therefore
\[
\|T-R\|\le s.
\]
Letting \(s\downarrow t\) and then \(t\downarrow\eta_n(T)\) gives
\[
a_n(T)\le\eta_n(T).
\]

### 2. A common lower witness for \(a_n,b_n,c_n\)

Let \(t<\eta_n(T)\). Then \(A_t\) contains at least \(n\) distinct points \(y_1,\dots,y_n\). Choose \(x_i\in L\) such that
\[
\phi(x_i)=y_i,\qquad |u(x_i)|>t.
\]
Choose pairwise disjoint open neighborhoods \(O_i\) of the \(y_i\), and functions
\[
f_i\in C(K),\qquad 0\le f_i\le1,\qquad
f_i(y_i)=1,\qquad \operatorname{supp}f_i\subset O_i.
\]
Then
\[
E=\operatorname{span}\{f_1,\dots,f_n\}
\]
is isometric to \(\ell_\infty^n\):
\[
\Big\|\sum_i a_i f_i\Big\|=\max_i|a_i|.
\]
Evaluation at the points \(x_i\) gives
\[
\Big|(T\sum_j a_jf_j)(x_i)\Big|
=|u(x_i)a_i|,
\]
so
\[
\|Tf\|\ge t\|f\|\qquad(f\in E).
\]
Hence \(b_n(T)\ge t\). If \(R\) has rank \(<n\), then \(R|_E\) has a nonzero kernel vector, so \(\|T-R\|\ge t\), giving \(a_n(T)\ge t\). If \(M\subset C(K)\) has codimension \(<n\), then \(M\cap E\ne\{0\}\), so \(\|T|_M\|\ge t\), giving \(c_n(T)\ge t\). Letting \(t\uparrow\eta_n(T)\) yields
\[
a_n(T)=b_n(T)=c_n(T)=\eta_n(T).
\]

### 3. Kolmogorov numbers

Keep the preceding \(x_i,y_i,f_i\) and let
\[
J:C(L)\to\ell_\infty^n,\qquad
Jg=(g(x_1),\dots,g(x_n)).
\]
Then \(\|J\|\le1\), and under the isometry
\[
(a_i)_{i=1}^n\longmapsto \sum_i a_i f_i
\]
from \(\ell_\infty^n\) onto \(E\), the map \(JT|_E\) is the diagonal operator
\[
D(a_1,\dots,a_n)
=(u(x_1)a_1,\dots,u(x_n)a_n).
\]
Since \(\min_i|u(x_i)|>t\),
\[
tB_{\ell_\infty^n}\subset D(B_{\ell_\infty^n}).
\]

Let \(N\subset C(L)\) have dimension \(<n\). Then \(J(N)\) is a proper subspace of \(\ell_\infty^n\). The quotient map onto
\(\ell_\infty^n/J(N)\) has norm \(1\), so
\[
\sup_{\|a\|_\infty\le1}
\operatorname{dist}(Da,J(N))\ge t.
\]
Since \(J\) is contractive,
\[
\operatorname{dist}(JT f,J(N))
\le \operatorname{dist}(Tf,N).
\]
Thus \(\|Q_NT\|\ge t\) for every \(\dim N<n\), and hence \(d_n(T)\ge t\). Letting \(t\uparrow\eta_n(T)\), while \(d_n(T)\le a_n(T)\), gives
\[
d_n(T)=\eta_n(T).
\]

### 4. The limiting threshold

Because \(N(t)\) is nonincreasing in \(t\), the sequence \((\eta_n)\) is nonincreasing. Put \(\rho=\lim_n\eta_n\).

If \(N(t)<\infty\), say \(N(t)=m\), then \(\eta_{m+1}\le t\), so \(\rho\le t\). Conversely, if \(t>\rho\), choose \(n\) with \(\eta_n<t\). By the definition of the infimum and monotonicity of \(N\), there is \(s<t\) with \(N(s)<n\), hence \(N(t)<\infty\). Therefore
\[
\rho=\inf\{t\ge0:N(t)<\infty\}.
\]

For each \(t>\rho\), the construction of Step 1 gives finite-rank operators arbitrarily close to \(T\) within norm \(t\). Hence
\[
\operatorname{dist}(T,\mathcal K)\le\rho,
\]
and the same upper bound holds for \(\mathcal W,\mathcal{FSS},\mathcal{SS}\).

### 5. An isometric \(c_0\) witness below the threshold

Fix \(t<\rho\). Then \(A_t\) is infinite.

We use the following elementary separation fact: if \(A\) is an infinite subset of a compact Hausdorff space, there are distinct points \(y_j\in A\) and pairwise disjoint open sets \(O_j\) with \(y_j\in O_j\). To see this recursively, start with an open set meeting \(A\) infinitely. If it contains a nonisolated point of the relative set, separate that point from another point and retain a neighborhood of the nonisolated point, which still meets \(A\) infinitely. If all relative points are isolated, isolate one point inside an open set whose closure meets \(A\) only there, and retain the open complement of that closure. Repeating gives the required family.

Apply this to \(A_t\). Choose \(x_j\in L\) with
\[
\phi(x_j)=y_j,\qquad |u(x_j)|>t,
\]
and choose \(f_j\in C(K)\) with
\[
0\le f_j\le1,\qquad f_j(y_j)=1,\qquad
\operatorname{supp}f_j\subset O_j.
\]
The closed span
\[
E=[f_j:j\ge1]
\]
is isometric to \(c_0\), because the supports are pairwise disjoint. For finitely supported scalars, and hence by closure for all elements of \(E\),
\[
\|Tf\|\ge t\|f\|.
\]

If \(S\) is strictly singular, \(S|_E\) cannot be bounded below. Thus for every \(\varepsilon>0\) there is \(f\in E\), \(\|f\|=1\), with \(\|Sf\|<\varepsilon\), and
\[
\|T-S\|\ge t-\varepsilon.
\]
The same conclusion holds for finitely strictly singular and compact \(S\).

If \(S\) is weakly compact and \(S|_E\) were bounded below, then the unit ball of \(E\simeq c_0\) would be relatively weakly compact after applying the bounded inverse on \(S(E)\), forcing \(E\) to be reflexive, a contradiction. Hence \(S|_E\) is not bounded below and the same estimate applies.

Letting \(\varepsilon\downarrow0\) and \(t\uparrow\rho\) yields
\[
\operatorname{dist}(T,\mathcal K)
=\operatorname{dist}(T,\mathcal W)
=\operatorname{dist}(T,\mathcal{FSS})
=\operatorname{dist}(T,\mathcal{SS})
=\rho.
\]

## Context and comparison with known results

Compactness and weak compactness of weighted composition operators on spaces of continuous functions are classical. Kamowitz studied compact weighted endomorphisms of \(C(X)\), and Singh--Summers proved the equivalence of compactness and weak compactness with a finite-threshold-image condition in the continuous-function setting. Albanese--Mele explicitly restate this criterion in modern notation.

Takagi--Miura--Takahasi subsequently determined the essential norm of a weighted composition operator on \(C(X)\) in terms of the same threshold images
\[
\phi(\{x:|u(x)|\ge r\}).
\]
Thus the compactness criterion and the exact distance to compact operators are prior art and are not claimed as new here.

Compact disjointness-preserving maps between \(C_0\)-spaces also have a classical structural theory: Lin--Wong showed that they admit norm-convergent decompositions into disjoint rank-one terms. General \(s\)-number theory supplies the definitions and standard inequalities used above.

The contribution claimed here is the finite-index quantitative profile:
\[
a_n(T)=b_n(T)=c_n(T)=d_n(T)
\]
for every \(n\), with the common value given by the counting rearrangement of fiber-maximal weights, together with the exact common distance to the weakly compact, finitely strictly singular and strictly singular classes and the corresponding isometric \(c_0\) witnesses. To the best of our knowledge, no matching statement was located in the literature consulted.

## Limitations

- The theorem is stated for scalar \(C(K)\)-spaces over compact Hausdorff spaces. Vector-valued fibers can introduce additional finite- and infinite-dimensional operator-ideal behavior.
- The essential-norm/compactness component is classical and is included only to place the new finite-index and singular-ideal formulas in one profile.
- The originality claim is to the best of our knowledge. The 1995 Singh--Singh survey, the 1993 Singh--Manhas monograph, and the full text of the 2003 Takagi--Miura--Takahasi paper were not exhaustively inspected; they are the principal residual risks for an equivalent formulation under older terminology.
- Literature on general disjointness-preserving operators is broad. Lin--Wong's compact structure theorem was checked at the statement level, but older Banach-lattice and disjointness-preserver sources were not exhaustively searched for finite \(s\)-number identities.

## References

1. H. Kamowitz, *Compact weighted endomorphisms of \(C(X)\)*, Proc. Amer. Math. Soc. 83 (1981), 517--521. https://doi.org/10.1090/S0002-9939-1981-0627682-1
2. R. K. Singh and W. H. Summers, *Compact and weakly compact composition operators on spaces of vector valued continuous functions*, Proc. Amer. Math. Soc. 99 (1987), 667--670. https://doi.org/10.2307/2046472
3. R. K. Singh and J. S. Manhas, *Composition Operators on Function Spaces*, North-Holland Mathematics Studies 179, 1993.
4. R. K. Singh and B. Singh, *Compact weighted composition operators on spaces of continuous functions: a survey*, Extracta Math. 10 (1995), 1--20.
5. H. Takagi, T. Miura and S.-E. Takahasi, *Essential norms and stability constants of weighted composition operators on \(C(X)\)*, Bull. Korean Math. Soc. 40 (2003), 583--591. https://doi.org/10.4134/BKMS.2003.40.4.583
6. Y.-F. Lin and N.-C. Wong, *The structure of compact disjointness preserving operators on continuous functions*, Math. Nachr. 282 (2009), 1009--1021. https://doi.org/10.1002/mana.200610786
7. A. A. Albanese and C. Mele, *On composition operators between weighted (LF)- and (PLB)-spaces of continuous functions*, Math. Nachr. 296 (2023), 5384--5399. https://doi.org/10.1002/mana.202200171
8. M. Ullrich, *Inequalities between s-numbers*, Adv. Oper. Theory 9 (2024), article 82. https://doi.org/10.1007/s43036-024-00386-x
