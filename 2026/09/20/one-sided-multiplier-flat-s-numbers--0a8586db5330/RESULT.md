# Flat classical s-number profiles for one-sided multiplication on symmetric norm ideals

## Statement

Let \(H\) be an infinite-dimensional separable complex Hilbert space and let
\(\mathfrak J\subset K(H)\) be a normalized symmetrically normed Banach ideal.
Thus finite-rank operators lie in \(\mathfrak J\), rank-one operators satisfy
\[
\|\theta_{\xi,\eta}\|_{\mathfrak J}=\|\xi\|\,\|\eta\|,
\qquad
\theta_{\xi,\eta}(h)=\langle h,\eta\rangle \xi,
\]
and the ideal inequality
\[
\|UXV\|_{\mathfrak J}\le \|U\|\,\|X\|_{\mathfrak J}\,\|V\|
\]
holds for \(U,V\in B(H)\), \(X\in\mathfrak J\).

For \(A,B\in B(H)\), write
\[
M_{A,B}(X)=AXB,\qquad L_A=M_{A,I},\qquad R_B=M_{I,B},
\]
and let
\[
\alpha=\|A\|_{\mathrm e},\qquad \beta=\|B\|_{\mathrm e},\qquad
\mu(A,B)=\max\{\alpha\|B\|,\ \|A\|\beta\},
\]
where \(\|\cdot\|_{\mathrm e}\) is the Hilbert-space essential norm.

Then:

1. The multiplier norm is
   \[
   \|M_{A,B}\|=\|A\|\,\|B\|.
   \]

2. For every \(n\ge1\), the approximation, Bernstein, Gelfand and Kolmogorov
   numbers satisfy
   \[
   a_n(M_{A,B}),\ b_n(M_{A,B}),\ c_n(M_{A,B}),\ d_n(M_{A,B})
   \ \ge\ \mu(A,B).
   \]

3. The distances to the compact, finitely strictly singular and strictly
   singular operator ideals on \(\mathfrak J\) satisfy
   \[
   \operatorname{dist}(M_{A,B},\mathcal K),\ 
   \operatorname{dist}(M_{A,B},\mathcal{FSS}),\ 
   \operatorname{dist}(M_{A,B},\mathcal{SS})
   \ \ge\ \mu(A,B).
   \]

4. If at least one coefficient is compact, these lower bounds become exact at
   the ideal-distance level and asymptotically exact for all four \(s\)-numbers.
   Specifically, if \(A\in K(H)\), then
   \[
   \operatorname{dist}(M_{A,B},\mathcal K)
   =\operatorname{dist}(M_{A,B},\mathcal{FSS})
   =\operatorname{dist}(M_{A,B},\mathcal{SS})
   =\|A\|\,\|B\|_{\mathrm e},
   \]
   and
   \[
   \lim_{n\to\infty}a_n(M_{A,B})
   =\lim_{n\to\infty}b_n(M_{A,B})
   =\lim_{n\to\infty}c_n(M_{A,B})
   =\lim_{n\to\infty}d_n(M_{A,B})
   =\|A\|\,\|B\|_{\mathrm e}.
   \]
   If \(B\in K(H)\), the corresponding common value is
   \(\|A\|_{\mathrm e}\|B\|\).

5. In particular, every one-sided multiplier has a completely flat classical
   \(s\)-number profile:
   \[
   \boxed{
   a_n(L_A)=b_n(L_A)=c_n(L_A)=d_n(L_A)=\|A\|
   \quad(n\ge1)
   }
   \]
   and
   \[
   \boxed{
   \operatorname{dist}(L_A,\mathcal K)
   =\operatorname{dist}(L_A,\mathcal{FSS})
   =\operatorname{dist}(L_A,\mathcal{SS})
   =\|A\|.
   }
   \]
   The same statements hold for \(R_B\), with common value \(\|B\|\).

Consequently, for nonzero \(A,B\), \(M_{A,B}\) is compact, finitely strictly
singular, or strictly singular exactly when both \(A\) and \(B\) are compact.
This qualitative consequence is treated as prior-art-adjacent; the originality
claim below concerns the quantitative \(s\)-number and distance formulas.

## Proof

### 1. A spectral-tail lemma

Let \(C\in B(H)\) and \(0<t<\|C\|_{\mathrm e}\). Put
\[
P_t=1_{(t,\infty)}(|C|).
\]
Then \(P_tH\) is infinite-dimensional. Indeed, if \(P_t\) had finite rank,
\(CP_t\) would be finite rank and
\[
\|C-CP_t\|=\|C(I-P_t)\|\le t,
\]
contradicting \(\|C\|_{\mathrm e}>t\). On \(P_tH\),
\[
\|Cx\|\ge t\|x\|.
\]

### 2. A complemented Hilbertian rank-one witness

Fix \(0<t<\alpha\) and \(\varepsilon>0\). Choose a unit vector \(z\in H\) with
\[
\|B^*z\|>\|B\|-\varepsilon,
\]
and put \(M=1_{(t,\infty)}(|A|)H\). Consider
\[
E=\{\theta_{x,z}:x\in M\}\subset\mathfrak J.
\]
The map \(x\mapsto\theta_{x,z}\) is an isometry from \(M\) onto \(E\). Moreover
\[
Q_E(X)=P_MXP_z
\]
is a projection of norm at most one from \(\mathfrak J\) onto \(E\), so \(E\)
is 1-complemented. For \(X=\theta_{x,z}\in E\),
\[
M_{A,B}X=\theta_{Ax,B^*z},
\]
hence
\[
\|M_{A,B}X\|_{\mathfrak J}
=\|Ax\|\,\|B^*z\|
\ge t(\|B\|-\varepsilon)\|X\|_{\mathfrak J}.
\tag{2.1}
\]

The output \(M_{A,B}(E)\) is also a 1-complemented Hilbertian rank-one subspace.
Indeed, \(A(M)\) is closed because \(A\) is bounded below on \(M\), and, after
normalizing \(B^*z\), the map
\[
X\mapsto P_{A(M)}XP_{\mathbb C B^*z}
\]
is a contractive projection onto \(M_{A,B}(E)\).

Interchanging the roles of the two sides gives a second witness. If
\(0<s<\beta\), use the infinite-dimensional spectral subspace of
\(|B^*|\) on which \(B^*\) is bounded below by \(s\), and choose a unit vector
\(y\) with \(\|Ay\|>\|A\|-\varepsilon\). The resulting rank-one row subspace is
1-complemented and satisfies
\[
\|M_{A,B}X\|_{\mathfrak J}
\ge (\|A\|-\varepsilon)s\,\|X\|_{\mathfrak J}.
\tag{2.2}
\]

Letting \(t\uparrow\alpha\), \(s\uparrow\beta\), and
\(\varepsilon\downarrow0\) yields complemented infinite-dimensional witnesses
with lower bounds arbitrarily close to each of
\(\alpha\|B\|\) and \(\|A\|\beta\).

### 3. The four finite-index lower bounds

Suppose \(T=M_{A,B}\) is bounded below by \(\gamma\) on one of the
infinite-dimensional witnesses \(E\).

For approximation numbers, if \(\operatorname{rank}R<n\), then
\(E\cap\ker R\neq\{0\}\), so for a unit \(x\) in this intersection,
\[
\|(T-R)x\|=\|Tx\|\ge\gamma.
\]
Thus \(a_n(T)\ge\gamma\).

For Bernstein numbers, choose any \(n\)-dimensional subspace of \(E\); the
minimum modulus of \(T\) on that subspace is at least \(\gamma\), so
\(b_n(T)\ge\gamma\).

For Gelfand numbers, every subspace of codimension \(<n\) intersects the
infinite-dimensional \(E\) nontrivially. Hence the norm of the restriction of
\(T\) to every such subspace is at least \(\gamma\), and \(c_n(T)\ge\gamma\).

For Kolmogorov numbers, let \(F=T(E)\), with the contractive projection
\(Q_F:\mathfrak J\to F\) described above. If \(N\subset\mathfrak J\) has
dimension \(<n\), then \(Q_FN\) is finite-dimensional. Since \(F\) is Hilbertian,
choose a nonzero \(Tx\in F\) orthogonal to \(Q_FN\), with \(x\in E\), and
normalize \(x\). Contractivity of \(Q_F\) gives
\[
\operatorname{dist}(Tx,N)
\ge \operatorname{dist}(Tx,Q_FN)
=\|Tx\|
\ge\gamma.
\]
Therefore \(d_n(T)\ge\gamma\).

Applying these arguments to (2.1) and (2.2), then passing to the endpoint
values, proves
\[
a_n(T),b_n(T),c_n(T),d_n(T)\ge\mu(A,B).
\]

### 4. Distances to \(\mathcal K,\mathcal{FSS},\mathcal{SS}\)

Let \(S\) be strictly singular on \(\mathfrak J\). Since \(E\) is
infinite-dimensional, \(S|_E\) is not bounded below. Hence for every
\(\delta>0\) there is a unit \(x\in E\) with \(\|Sx\|<\delta\). If \(T\) is
bounded below by \(\gamma\) on \(E\), then
\[
\|T-S\|\ge\|(T-S)x\|\ge\gamma-\delta.
\]
Thus \(\operatorname{dist}(T,\mathcal{SS})\ge\gamma\). Since
\[
\mathcal K\subset\mathcal{FSS}\subset\mathcal{SS},
\]
the same lower bound holds for the distances to \(\mathcal K\) and
\(\mathcal{FSS}\). Taking the two witnesses to their endpoint values gives the
claimed lower bound \(\mu(A,B)\).

### 5. Exactness when one coefficient is compact

Assume \(A\) is compact. For every \(\varepsilon>0\), choose \(K\in K(H)\) with
\[
\|B-K\|<\|B\|_{\mathrm e}+\varepsilon.
\]
The multiplier \(M_{A,K}\) is compact on \(\mathfrak J\): approximate \(A\) and
\(K\) in operator norm by finite-rank operators; the corresponding
two-sided multipliers have finite-dimensional range and converge in operator
norm to \(M_{A,K}\). Consequently
\[
\operatorname{dist}(M_{A,B},\mathcal K)
\le\|M_{A,B-K}\|
=\|A\|\,\|B-K\|.
\]
After \(\varepsilon\downarrow0\), the lower bound from Section 4 gives equality
simultaneously for \(\mathcal K,\mathcal{FSS},\mathcal{SS}\).

The same finite-rank approximation also yields the common \(s\)-number limit.
Given \(\varepsilon>0\), choose a finite-rank operator \(R\) on
\(\mathfrak J\) such that
\[
\|M_{A,B}-R\|<\|A\|\,\|B\|_{\mathrm e}+\varepsilon.
\]
For all \(n>\operatorname{rank}R\), direct use of \(\ker R\) and
\(\operatorname{ran}R\) in the definitions gives
\[
a_n,b_n,c_n,d_n
\le\|A\|\,\|B\|_{\mathrm e}+\varepsilon.
\]
Together with the lower bound, this proves the four limits. The case of compact
\(B\) is symmetric.

### 6. One-sided flatness

For \(L_A=M_{A,I}\), \(\|I\|_{\mathrm e}=1\), so
\[
\mu(A,I)=\max\{\|A\|_{\mathrm e},\|A\|\}=\|A\|.
\]
Every one of \(a_n,b_n,c_n,d_n\) is at most the operator norm
\(\|L_A\|=\|A\|\), while Section 3 gives the reverse inequality. This proves the
four exact identities for every \(n\). Section 4 gives distance at least
\(\|A\|\), while distance to any operator ideal is at most \(\|L_A\|\) by
comparison with the zero operator. Hence all three ideal distances equal
\(\|A\|\). The proof for \(R_B\) is identical.

## Relation to prior literature and originality boundary

Compact and strictly singular multiplication operators on full operator
algebras have substantial prior literature. Vala's compactness theorem says
that for nonzero \(A,B\), the map \(S\mapsto ASB\) on \(B(X)\) is compact
exactly when both coefficients are compact. Lindström, Saksman and Tylli
(2005) study strict singularity and cosingularity of two-sided multiplications
on \(L(X)\); their Fact 2.1 explicitly states analogous basic implications for
the restriction to compact-operator spaces \(K(E_2,E_3)\). Mathieu and
Tradacete (2020) further study strict singularity of multiplication operators
on \(L(X)\). These qualitative mechanisms are prior art and are not claimed as
new here.

Fialkow and Loebl (1984) studied elementary mappings into operator ideals.
Huang, Sukochev, Xu and Zhu (2026) determine exact norms and range criteria for
multiplication maps from a semifinite factor into a symmetrically normed
operator space. That direction concerns mapping *into* an ideal, rather than
the finite-index \(s\)-number and strict-singularity profile of multiplication
acting *on* the ideal.

To the best of our knowledge, the following quantitative statements were not
located in the checked literature:

- the exact all-\(n\) identities
  \[
  a_n(L_A)=b_n(L_A)=c_n(L_A)=d_n(L_A)=\|A\|
  \]
  and their right-multiplication analogues on every normalized symmetrically
  normed Banach ideal of compact operators;
- the exact distances of \(L_A\) and \(R_B\) to
  \(\mathcal K,\mathcal{FSS},\mathcal{SS}\);
- the universal two-sided floor
  \[
  \max\{\|A\|_{\mathrm e}\|B\|,\|A\|\|B\|_{\mathrm e}\}
  \]
  simultaneously for all four classical \(s\)-numbers and the three ideal
  distances;
- the exact one-compact-factor distance and common asymptotic \(s\)-number
  formula.

The main reusable mechanism is the explicit 1-complemented Hilbertian
rank-one witness obtained from an essential spectral tail of one coefficient
and a near-norming vector for the other.

## Limitations

The result is for normalized symmetrically normed **Banach** ideals contained
in \(K(H)\) on an infinite-dimensional separable Hilbert space. It does not
cover quasi-Banach ideals such as \(S_p\) for \(0<p<1\), general sums of
elementary operators, or arbitrary non-symmetric operator spaces.

When both \(A\) and \(B\) are noncompact, the quantity \(\mu(A,B)\) is proved
to be a universal lower bound; no claim is made here that it is always the
exact finite-index \(s\)-number value or exact ideal distance.

Originality is asserted only to the best of our knowledge. Older elementary-
operator and norm-ideal literature is extensive, and an equivalent
quantitative statement under different terminology cannot be ruled out.

## Reproducibility

No numerical computation is needed. The argument reduces to: (i) the spectral
projection \(1_{(t,\infty)}(|C|)\) below the essential norm, (ii) rank-one
operators and the symmetric ideal inequality, and (iii) the definitions of
the four classical \(s\)-numbers and of strict singularity.

## References

1. M. Lindström, E. Saksman, H.-O. Tylli, *Strictly Singular and Cosingular
   Multiplications*, Canadian Journal of Mathematics 57 (2005), 1249–1278.
   https://doi.org/10.4153/CJM-2005-050-7
2. M. Mathieu, P. Tradacete, *Strictly singular multiplication operators on
   \(\mathcal L(X)\)*, Israel Journal of Mathematics 236 (2020), 685–709.
   https://doi.org/10.1007/s11856-020-1985-0
3. L. A. Fialkow, R. Loebl, *Elementary mappings into ideals of operators*,
   Illinois Journal of Mathematics 28 (1984), 555–578.
4. J. Huang, F. Sukochev, R. Xu, Y. Zhu, *Norms of multiplication operators:
   answering Fialkow--Loebl question*, arXiv:2608.18449 (2026).
   https://arxiv.org/abs/2608.18449

## Publication

Record: SCOPE-20260920-0a8586db5330  
Publication date: 2026-09-20 UTC
