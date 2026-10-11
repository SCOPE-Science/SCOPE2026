# Coordinate-shadow norm formula for Walsh projections on Hamming Lipschitz-free spaces

## Finding

Let \(n\ge 1\) be an integer and give \(M_n=\{-1,1\}^n\) the Hamming distance \(d(x,y)=\tfrac12\sum_{i=1}^n|x_i-y_i|\), pointed at \(o=(1,\ldots,1)\). Work over \(\mathbb K=\mathbb R\) or \(\mathbb C\). Let \(\varnothing\ne\mathscr A\subseteq 2^{[n]}\setminus\{\varnothing\}\). Write \(\chi_S(x)=\prod_{j\in S}x_j\) and let \(Q_{\mathscr A}\) be the Fourier-Walsh projection on \(\operatorname{Lip}_0(M_n;\mathbb K)\), with the output normalized to vanish at \(o\):

\[
Q_{\mathscr A}f(x)=\sum_{S\in\mathscr A}\widehat f(S)(\chi_S(x)-1),\qquad
\widehat f(S)=2^{-n}\sum_{x\in M_n}f(x)\chi_S(x).
\]

For \(i\in[n]\), set
\[
\mathscr A_i=\{S\setminus\{i\}:S\in\mathscr A,\ i\in S\}\subseteq 2^{[n]\setminus\{i\}},
\qquad K_i(u)=\sum_{T\in\mathscr A_i}\chi_T(u),
\]
where the empty sum is zero. Then the **exact operator norm and the least possible norm of a projection onto this Walsh subspace** are

\[
\boxed{\lambda\big(\operatorname{span}\{\chi_S-1:S\in\mathscr A\},\operatorname{Lip}_0(M_n;\mathbb K)\big)
=\|Q_{\mathscr A}\|
=\max_{i\in[n]}2^{-(n-1)}\sum_{u\in\{-1,1\}^{n-1}}|K_i(u)|.}
\]

The adjoint projection acts on \(\mathcal F(M_n;\mathbb K)\) and has the same norm; it is likewise a minimum-norm projection onto its range. In particular, for the full degree-\(k\) projection \(Q_k\), \(1\le k\le n\), writing \(m=n-1\) and \(d=k-1\),

\[
\|Q_k\|=2^{-m}\sum_{r=0}^{m}\binom mr
\left|\sum_{j=0}^{d}(-1)^j\binom rj\binom{m-r}{d-j}\right|.
\]

For the quadratic layer, \(n\ge2\), this specializes to the sharp formula and growth

\[
\boxed{\|Q_2\|=\frac{(n-1)\binom{n-2}{\lfloor(n-2)/2\rfloor}}{2^{n-2}}
\sim\sqrt{\frac{2(n-1)}{\pi}}.}
\]

## Assumptions and scope

The metric is the **unweighted** Hamming shortest-path metric; every coordinate edge has length one. The support family is arbitrary and nonempty but excludes the constant Walsh character because \(\operatorname{Lip}_0\) identifies constants with zero. Projection constants here are *relative* projection constants inside \(\operatorname{Lip}_0(M_n)\) or, for the adjoint, inside the finite-dimensional free space; no assertion concerns the absolute projection constant of an abstract Banach space. The formulas hold for both scalar fields. If \(n=1\), the only permitted nonempty family is \(\{\{1\}\}\), and the formula gives one.

## Proof

**1. Edge norm.** For \(i\in[n]\), put
\[
D_if(u)=\tfrac12\big(f(x_i=1,x_{\widehat i}=u)-f(x_i=-1,x_{\widehat i}=u)\big).
\]
Every pair of cube vertices is connected by a path of unit coordinate edges, so
\[
\|f\|_{\operatorname{Lip}}=2\max_i\|D_i f\|_\infty.
\]
The constant subtracted at the base point has no effect on any \(D_i\).

**2. Coordinate-shadow upper bound.** The Fourier expansion gives
\[
D_i(Q_{\mathscr A}f)=T_{\mathscr A_i}(D_if),
\]
where \(T_{\mathscr A_i}\) is the ordinary Fourier projection on bounded functions of the remaining \(n-1\) coordinates. By convolution with the Walsh kernel \(K_i\),
\[
\|T_{\mathscr A_i}\|_{\ell_\infty\to\ell_\infty}
=2^{-(n-1)}\sum_u|K_i(u)|=:c_i.
\]
Consequently \(\|Q_{\mathscr A}f\|_{\operatorname{Lip}}\le (\max_i c_i)\|f\|_{\operatorname{Lip}}\). This also applies for complex scalars because the kernel is real and the absolute-value convolution bound is unchanged.

**3. Simultaneous sharpness mechanism.** Fix \(i\) with \(c_i>0\) and define \(g(u)=1\) where \(K_i(u)\ge0\), and \(g(u)=-1\) otherwise. Set
\[
f(x)=x_i g(x_{\widehat i})-g(o_{\widehat i}).
\]
This vanishes at the base point and takes values among two translates of \(\{-1,1\}\), so every edge difference has modulus at most \(2\). Along the \(i\)-th coordinate the edge difference is exactly \(2g(u)\), hence \(\|f\|_{\operatorname{Lip}}=2\). At the all-positive vertex of the remaining coordinates,
\[
T_{\mathscr A_i}g(o_{\widehat i})
=2^{-(n-1)}\sum_u g(u)K_i(u)=c_i.
\]
Thus \(\|Q_{\mathscr A}f\|_{\operatorname{Lip}}\ge 2c_i\). Maximizing over \(i\) proves the exact norm, not merely a bound. The same real-valued witness proves sharpness over \(\mathbb C\).

**4. Optimality among all projections.** For \(y\in M_n\), define the pointed translation isometry
\[
(U_yf)(x)=f(xy)-f(y),
\]
where multiplication is coordinatewise. The anchored Walsh characters \(e_S=\chi_S-1\) satisfy \(U_y e_S=\chi_S(y)e_S\). If \(R\) is any projection of \(\operatorname{Lip}_0(M_n)\) onto \(Y_{\mathscr A}=\operatorname{span}\{e_S:S\in\mathscr A\}\), then the average
\[
\overline R=2^{-n}\sum_{y\in M_n}U_y^{-1}RU_y
\]
is again a projection onto \(Y_{\mathscr A}\) and has norm at most \(\|R\|\). The distinct characters are one-dimensional joint eigenspaces of the translation action, so the only translation-equivariant projection onto \(Y_{\mathscr A}\) fixes every \(e_S\) in the family and annihilates every other \(e_T\); it is precisely \(Q_{\mathscr A}\). Thus \(Q_{\mathscr A}\) minimizes the norm. Duality preserves its operator norm. On the finite-dimensional free space the dual translations again diagonalize into distinct characters, and the identical averaging argument shows that \(Q_{\mathscr A}^{*}\) is minimum-norm among projections onto its range.

**5. Degree formula and quadratic layer.** For \(\mathscr A=\{S\subseteq[n]:|S|=k\}\), all shadows are the full degree-\(d=k-1\) Walsh layer in \(m=n-1\) variables. If \(u\) has \(r\) negative coordinates, counting the negative choices in \(T\) gives \(K_i(u)=\sum_{j=0}^{d}(-1)^j\binom rj\binom{m-r}{d-j}\). There are \(\binom mr\) such \(u\), proving the displayed finite sum.

For \(d=1\), the kernel is \(\sum_{j=1}^{m}u_j\). Its absolute first moment equals \(m\binom{m-1}{\lfloor(m-1)/2\rfloor}/2^{m-1}\), by pairing the symmetric binomial terms, or by induction from the recurrence \(\mathbb E|S_m|-\mathbb E|S_{m-1}|=\Pr(S_{m-1}=0)\) for a simple symmetric random walk. Stirling's formula gives the stated asymptotic.

## Verification

The accompanying self-contained `check.py` uses integer Walsh transforms and rational kernel expectations. It checked every nonempty spectral family for \(n=1,2,3\), and 150 reproducibly sampled families at each of \(n=4,5,6\), comparing the exact shadow value against an explicit extremizing Lipschitz function. It separately checked 23 exact binomial first-moment identities, including direct homogeneous-layer calculations in dimensions up to six. Output: `PASS 585 nonempty arbitrary-spectrum witness checks; 23 exact degree-two moment identities`. These finite checks corroborate the explicit constructions; the universal statement is established by steps 1–5, not by enumeration.

## Relationship to prior work

Defant, Galicer, Mansilla, Mastyło and Muro proved the absolute/relative projection-constant kernel formula for Walsh-supported subspaces of \(C(\{-1,1\}^m)\), notably Theorem 8.1.1 of their 2022 monograph and Theorem 3.1 of the 2023 companion article. Their 2022 Chapter 8 and the 2023 Section 4 also give homogeneous-layer asymptotics on the *supremum-norm* cube. Those kernel formulas and asymptotics are **prior results** and are not claimed new here. The present result identifies the exact *Lipschitz-norm* projection invariant for an arbitrary spectral family, by proving a coordinate-shadow reduction, its sharp realization within the coupled gradient constraints, and minimality in Lipschitz and Lipschitz-free spaces. Cúth and Doucha studied norm-one projections arising from group-orbit invariants in Lipschitz-free spaces; their invariant-subspace result does not compute the nontrivial Walsh spectral projections treated here. Eskenazis's work on metric properties of Hamming cubes studies embeddings and type inequalities rather than these relative projection constants.

## Limitations

The coordinate-shadow sharpness construction uses the fact that **all** Hamming edges have equal length; a weighted Hamming metric requires a separate argument and is not covered. The result identifies the canonical/minimum spectral projection constant, not the Banach–Mazur distance or arbitrary operator norm on the free space. The quadratic asymptotic and the higher-degree Krawtchouk expression are consequences of the new exact transfer identity together with classical Walsh/binomial analysis; they are not claimed as independently new estimates for bounded cube functions. A comparable Lipschitz-seminorm formulation could exist in literature not identified by the searches. No independent audit is claimed.

## References

1. A. Defant, D. Galicer, M. Mansilla, M. Mastyło and S. Muro, *Projection constants for spaces of multivariate polynomials*, arXiv:2208.06467v1, first public 2022-08-12. Especially Sections 2.2–2.3 and Chapter 8: https://arxiv.org/pdf/2208.06467.
2. A. Defant, D. Galicer, M. Mansilla, M. Mastyło and S. Muro, *Asymptotic insights for projection, Gordon–Lewis and Sidon constants in Boolean cube function spaces*, arXiv:2302.00233v1, first public 2023-02-01. Especially Theorems 3.1 and 4.1: https://arxiv.org/html/2302.00233v2.
3. M. Cúth and M. Doucha, *Projections in Lipschitz-free spaces induced by group actions*, arXiv:2104.11519v1, first public 2021-04-23. Especially Section 4: https://arxiv.org/html/2104.11519v1.
4. A. Eskenazis, *Some geometric applications of the discrete heat flow*, arXiv:2310.01868v1, first public 2023-10-03: https://arxiv.org/html/2310.01868v1.
