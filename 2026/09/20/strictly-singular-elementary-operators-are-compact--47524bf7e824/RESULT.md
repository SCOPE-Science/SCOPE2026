# Strict singularity collapses to compactness for finite elementary operators on norm ideals

## Statement

Let \(H\) be a separable infinite-dimensional complex Hilbert space. Let
\(\mathfrak J\subset K(H)\) be a Banach operator ideal with its normalized ideal norm:
\[
\|AXB\|_{\mathfrak J}\le \|A\|\,\|X\|_{\mathfrak J}\,\|B\|,
\qquad
\|u\otimes v\|_{\mathfrak J}=\|u\|\,\|v\|,
\]
where
\[
(u\otimes v)x=\langle x,v\rangle u.
\]
Let
\[
\Phi(X)=\sum_{j=1}^m A_jXB_j,\qquad A_j,B_j\in B(H),
\]
be a finite elementary operator acting on \(\mathfrak J\).

Then the following are equivalent:

1. \(\Phi:\mathfrak J\to\mathfrak J\) is compact;
2. \(\Phi\) is finitely strictly singular;
3. \(\Phi\) is strictly singular;
4. \(\Phi\) admits a finite representation
   \[
   \Phi(X)=\sum_{\ell=1}^r K_\ell X C_\ell
   \]
   with every \(K_\ell,C_\ell\in K(H)\).

There is also a stronger alternative behind the equivalence. If \(\Phi\) is not compact,
then \(\Phi\) is bounded below on an infinite-dimensional, 1-complemented Hilbertian
subspace of \(\mathfrak J\) consisting entirely of rank-one operators (apart from zero).
More precisely, one can find either

\[
\mathcal M_{E,v}=\{u\otimes v:u\in E\},
\]
for a closed infinite-dimensional \(E\subset H\) and a unit vector \(v\), or
\[
\mathcal N_{u,F}=\{u\otimes v:v\in F\},
\]
for a unit vector \(u\) and a closed infinite-dimensional \(F\subset H\), such that
\[
\|\Phi X\|_{\mathfrak J}\ge c\|X\|_{\mathfrak J}
\]
on that subspace for some \(c>0\).

Consequently the Bernstein numbers satisfy
\[
b_n(\Phi)\ge c\qquad(n\ge1)
\]
whenever \(\Phi\) is noncompact.

## Proof

### 1. Finite-support slices of a norm ideal are Hilbertian

If \(P\) is a finite-rank orthogonal projection of rank \(d\), every
\(X\in\mathfrak J P\) has rank at most \(d\). Using a singular-value decomposition and
the normalized rank-one norm,
\[
\|X\|\le \|X\|_{\mathfrak J}
   \le \|X\|_1
   \le \sqrt d\,\|X\|_2
   \le d\,\|X\|.
\]
Also
\[
\|X\|_2\le \sqrt d\,\|X\|
          \le \sqrt d\,\|X\|_{\mathfrak J}.
\]
Thus the \(\mathfrak J\)-norm and Hilbert-Schmidt norm are equivalent on
\(\mathfrak J P\). The same holds on \(P\mathfrak J\). In particular, these
finite-support slices are isomorphic to Hilbert spaces.

We use the standard Hilbert-space fact that a strictly singular operator between
Hilbert spaces is compact.

### 2. Strict singularity forces a representation with compact left coefficients

Let
\[
V=\operatorname{span}\{A_1,\ldots,A_m\}\subset B(H)
\]
and let \(q:B(H)\to B(H)/K(H)\) be the Calkin quotient. Choose a basis of \(V\) of
the form
\[
C_1,\ldots,C_r,K_1,\ldots,K_s,
\]
where \(K_1,\ldots,K_s\in K(H)\) and
\(q(C_1),\ldots,q(C_r)\) are linearly independent. After regrouping coefficients,
\[
\Phi(X)=\sum_{i=1}^r C_iXD_i+\sum_{\ell=1}^s K_\ell XL_\ell.
\tag{1}
\]

Fix a unit vector \(v\). The rank-one column
\[
\mathcal M_v=\{u\otimes v:u\in H\}
\]
is isometric to \(H\), and it is 1-complemented in \(\mathfrak J\) by
\(X\mapsto XP_v\). Its image under \(\Phi\) is contained in
\(\mathfrak J P_{F_v}\), where
\[
F_v=\operatorname{span}\{D_i^*v,L_\ell^*v\}.
\]
If \(\Phi\) is strictly singular, then its restriction
\[
T_v:H\longrightarrow\mathfrak J P_{F_v},
\qquad
T_vu=\Phi(u\otimes v),
\]
is strictly singular. By Step 1 it is therefore compact.

For \(z\in F_v\), the evaluation map \(Y\mapsto Yz\) is bounded because
\[
\|Yz\|\le \|Y\|\,\|z\|\le \|Y\|_{\mathfrak J}\|z\|.
\]
Hence
\[
u\longmapsto T_v(u)z
=
\sum_{i=1}^r
\langle z,D_i^*v\rangle C_i u
+
\sum_{\ell=1}^s
\langle z,L_\ell^*v\rangle K_\ell u
\]
is compact. The second sum is compact, so
\[
\sum_{i=1}^r \langle z,D_i^*v\rangle C_i
\]
is compact. Linear independence of \(q(C_1),\ldots,q(C_r)\) yields
\[
\langle z,D_i^*v\rangle=0
\qquad(1\le i\le r).
\]
Taking \(z=D_i^*v\) gives \(D_i^*v=0\). Since \(v\) was arbitrary, every \(D_i=0\).
Thus
\[
\Phi(X)=\sum_{\ell=1}^s K_\ell XL_\ell
\tag{2}
\]
with all left coefficients compact.

### 3. Strict singularity also forces compact right coefficients

Apply the same Calkin-space reduction to the span of the right coefficients in (2).
We can rewrite
\[
\Phi(X)=\sum_{i=1}^t M_iXD_i+\sum_{k=1}^q N_kXC_k,
\tag{3}
\]
where all \(M_i,N_k\) are compact, all \(C_k\) are compact, and
\(q(D_1),\ldots,q(D_t)\) are linearly independent.

Fix a unit vector \(u\). The row-type fiber
\[
\mathcal N_u=\{u\otimes v:v\in H\}
\]
is linearly isometric to the conjugate Hilbert space \(\overline H\) and is
1-complemented by \(X\mapsto P_uX\). Its image under \(\Phi\) lies in
\(P_{G_u}\mathfrak J\), where
\[
G_u=\operatorname{span}\{M_i u,N_k u\}.
\]
Strict singularity again makes this restriction compact.

For \(z\in G_u\), the map \(Y\mapsto Y^*z\) is bounded as a conjugate-linear map.
After composing with the canonical conjugate-linear identification
\(H\to\overline H\), compactness gives a compact linear operator on \(H\) of the form
\[
\sum_{i=1}^t \langle z,M_i u\rangle D_i^*
+
\sum_{k=1}^q \langle z,N_k u\rangle C_k^*.
\]
The second sum is compact. Since linear independence of the \(q(D_i)\) is equivalent
to linear independence of the \(q(D_i^*)\), all coefficients
\(\langle z,M_i u\rangle\) vanish. Taking \(z=M_i u\) gives \(M_i u=0\) for every
\(u\), hence \(M_i=0\). Therefore (3) reduces to a representation
\[
\Phi(X)=\sum_{k=1}^q N_kXC_k
\]
with compact coefficients on both sides.

This proves
\[
\Phi\text{ strictly singular}
\Longrightarrow
\Phi\text{ has a compact--compact coefficient representation}.
\tag{4}
\]

### 4. Compact coefficients give a compact superoperator

For one term \(X\mapsto KXC\) with \(K,C\in K(H)\), choose finite-rank
\(K_n\to K\) and \(C_n\to C\) in operator norm. The ideal inequality gives
\[
\|L_KR_C-L_{K_n}R_{C_n}\|_{\mathcal B(\mathfrak J)}\to0.
\]
Each \(X\mapsto K_nXC_n\) has finite-dimensional range, of dimension at most
\(\operatorname{rank}(K_n)\operatorname{rank}(C_n)\). Hence \(L_KR_C\) is compact,
and so is every finite sum of such terms.

Together with the standard implications
\[
\text{compact}\Longrightarrow\text{finitely strictly singular}
\Longrightarrow\text{strictly singular},
\]
this proves the four-way equivalence.

### 5. The rank-one witness for every noncompact elementary operator

The preceding reductions can be run with compactness of the rank-one-fiber
restrictions rather than strict singularity of \(\Phi\).

If some fixed-column restriction \(T_v\) is noncompact, then, as an operator between
Hilbert spaces up to equivalent norms, it is bounded below on an infinite-dimensional
closed subspace \(E\subset H\). Hence \(\Phi\) is bounded below on
\(\mathcal M_{E,v}\).

If every fixed-column restriction is compact, Step 2 yields a representation with
compact left coefficients. If every fixed-row restriction were also compact, Step 3
would yield compact coefficients on both sides, and Step 4 would make \(\Phi\)
compact. Therefore a noncompact \(\Phi\) must have a noncompact fixed-row restriction,
which is bounded below on an infinite-dimensional closed \(F\subset H\). This gives
\(\mathcal N_{u,F}\).

Finally,
\[
X\mapsto P_E X P_v
\quad\text{and}\quad
X\mapsto P_u X P_F
\]
are contractive projections onto the two possible witness spaces. They are therefore
1-complemented. The uniform Bernstein-number lower bound follows by taking
\(n\)-dimensional subspaces inside the infinite-dimensional witness.

## Relation to known results

Fialkow and Loebl (1984) studied elementary mappings into operator ideals, and
Apostol and Fialkow (1986) developed structural and range results for elementary
operators. The latter paper treats compactness of elementary operators on full
operator spaces and range inclusion in ideals; its searchable text contains no
occurrence of “strictly singular.” Magajna (1987) supplied a Calkin-independence
mechanism for systems of operator equations and applications to elementary operators.

Brešar and Turovskii (2007) studied compact elementary operators on Banach algebras,
including their coefficients and ranges. These compactness results are relevant to
condition (4), so no independent novelty is claimed here for every possible
compact-coefficient reformulation in the older literature.

Lindström, Saksman and Tylli (2005), and later Mathieu and Tradacete (2020), studied
strict singularity of two-sided multiplications \(S\mapsto ASB\) on \(L(X)\) for
various classical Banach spaces. Their ambient space is the full operator algebra
\(L(X)\), and the located statements concern a single two-sided multiplication rather
than finite elementary sums acting on Hilbert-space norm ideals.

Recent work of Huang, Sukochev and Yu (2026) studies general bounded operators on
operator ideals and a relative notion of \(\mathcal C_E\)-strict singularity. The
statement here concerns ordinary Banach-space strict singularity and the special
finite-elementary class.

The contribution claimed here is the collapse
\[
\text{strictly singular}
=
\text{finitely strictly singular}
=
\text{compact}
\]
within finite elementary operators on Banach norm ideals, together with the stronger
rank-one Hilbertian witness for every noncompact member of that class.

## Originality and limitations

Originality is claimed **to the best of our knowledge** only for the strict-singularity
collapse and the rank-one witness in the stated class. Exact and synonymous searches
for strictly singular elementary operators on norm ideals, Schatten ideals, finite
elementary sums, and rank-one witnesses located the neighboring literature described
above but no matching theorem.

The 1984 Fialkow--Loebl paper is particularly relevant because it concerns elementary
mappings into operator ideals; its bibliographic record and its use in later papers
were inspected, but its full text was not exhaustively checked. Older survey and
compact-elementary-operator literature was also not exhaustively inspected for an
equivalent statement under different terminology. Because the compact-coefficient
part of the theorem is close to that literature, the novelty claim is deliberately
centered on ordinary strict singularity and the complemented rank-one witness.

The result is restricted to Banach norm ideals of compact operators satisfying the
normalized ideal property above. No claim is made here for quasi-Banach ideals,
infinite elementary sums, integral elementary operators, or elementary operators on
\(B(X)\) for general Banach spaces.

## References

1. L. A. Fialkow and R. Loebl, “Elementary mappings into ideals of operators,”
   *Illinois Journal of Mathematics* 28 (1984), 555–578.
   https://doi.org/10.1215/ijm/1256045966
2. C. Apostol and L. Fialkow, “Structural Properties of Elementary Operators,”
   *Canadian Journal of Mathematics* 38 (1986), 1485–1524.
   https://doi.org/10.4153/CJM-1986-072-6
3. B. Magajna, “A System of Operator Equations,”
   *Canadian Mathematical Bulletin* 30 (1987), 200–209.
   https://doi.org/10.4153/CMB-1987-029-2
4. M. Lindström, E. Saksman and H.-O. Tylli,
   “Strictly Singular and Cosingular Multiplications,”
   *Canadian Journal of Mathematics* 57 (2005), 1249–1278.
   https://doi.org/10.4153/CJM-2005-050-7
5. M. Brešar and Y. V. Turovskii, “Compactness conditions for elementary operators,”
   *Studia Mathematica* 178 (2007), 1–18.
   https://doi.org/10.4064/sm178-1-1
6. M. Mathieu and P. Tradacete, “Strictly singular multiplication operators on
   \(\mathcal L(X)\),” *Israel Journal of Mathematics* 236 (2020), 685–709.
   https://doi.org/10.1007/s11856-020-1985-0
7. J. Huang, F. Sukochev and Z. Yu,
   “Arazy-type decomposition theorem for bounded linear operators and commutators
   on the trace class,” arXiv:2602.09579 (2026).
   https://arxiv.org/abs/2602.09579
