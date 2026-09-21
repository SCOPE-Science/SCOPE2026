# Flat s-number and strict-singularity profiles of relative Toeplitz Schur multipliers

## Statement

Let \(\Gamma\) be an infinite discrete group and let \(\varnothing\ne\Lambda\subseteq\Gamma\).
Set
\[
I_\Lambda=\{(r,c)\in\Gamma\times\Gamma:rc^{-1}\in\Lambda\}.
\]
For \(1\le p<\infty\), let
\[
X_p=S_p^{I_\Lambda}
\]
be the closed subspace of \(S_p(\ell_2\Gamma)\) spanned by the matrix units
\(e_{r,c}\) with \((r,c)\in I_\Lambda\). For \(p=\infty\), use the convention
\(S_\infty=K(\ell_2\Gamma)\) and let \(X_\infty=S_\infty^{I_\Lambda}\).

Let \(m:\Lambda\to\mathbb C\), and suppose the relative Toeplitz Schur multiplier
\[
T=M_m:X_p\to X_p,\qquad
M_m(e_{r,c})=m(rc^{-1})e_{r,c},
\]
is bounded.

Then for every \(n\ge1\),
\[
\boxed{
a_n(T)=c_n(T)=d_n(T)=b_n(T)=\|T\|
}
\]
for the approximation, Gelfand, Kolmogorov and Bernstein numbers, respectively.

Moreover,
\[
\boxed{
\operatorname{dist}(T,\mathcal K(X_p))
=
\operatorname{dist}(T,\mathcal{FSS}(X_p))
=
\operatorname{dist}(T,\mathcal{SS}(X_p))
=
\|T\|
},
\]
so in particular the essential norm satisfies
\[
\|T\|_{\mathrm e}=\|T\|.
\]
If \(\chi(T)\) denotes the Hausdorff measure of noncompactness of \(T(B_{X_p})\),
then
\[
\boxed{\chi(T)=\|T\|}.
\]

Consequently, a relative Toeplitz Schur multiplier of this form is strictly singular,
finitely strictly singular, or compact **if and only if it is zero**.

For the full pattern \(\Lambda=\Gamma\), this applies in particular to every bounded
Toeplitz Schur multiplier on \(S_p(\ell_2\Gamma)\) (and on
\(K(\ell_2\Gamma)\) when \(p=\infty\)). Thus every nonzero Herz--Schur multiplier,
viewed through its Toeplitz Schur action on these Schatten classes, is maximally
noncompact and is at norm distance from the strictly singular operators.

## Proof

Write \(N=\|T\|\). The case \(N=0\) is immediate, so assume \(N>0\).

### 1. A near-norm finite block has infinitely many disjoint translates

Fix \(\varepsilon\in(0,N)\). Finite-support matrices are dense in \(X_p\) for every
\(1\le p\le\infty\) under the convention above. Hence there is a finite-support
\(x\in X_p\) with
\[
\|x\|_p=1,\qquad
\|Tx\|_p>N-\varepsilon.
\]
Choose finite \(R,C\subset\Gamma\) such that
\[
\operatorname{supp}x\subset R\times C,
\]
and put \(F=R\cup C\).

For \(g\in\Gamma\), let \(V_g\) be the unitary permutation
\[
V_g e_h=e_{hg},
\]
and define
\[
\alpha_g(z)=V_gzV_g^*.
\]
Then
\[
\alpha_g(e_{r,c})=e_{rg,cg}.
\]
Since
\[
(rg)(cg)^{-1}=rc^{-1},
\]
both the pattern \(I_\Lambda\) and the multiplier symbol are invariant:
\[
\alpha_g(X_p)=X_p,\qquad T\alpha_g=\alpha_gT.
\]

Because \(F\) is finite and \(\Gamma\) is infinite, a greedy choice produces
\(g_1,g_2,\ldots\in\Gamma\) such that the sets \(Fg_j\) are pairwise disjoint.
Indeed, after \(g_1,\ldots,g_k\) have been chosen, only finitely many \(g\) can make
\(Fg\) meet one of the previously chosen translates.

Set
\[
x_j=\alpha_{g_j}(x),\qquad y_j=Tx_j=\alpha_{g_j}(Tx),
\qquad r=\|Tx\|_p.
\]
Thus \(r>N-\varepsilon\). The initial spaces \(Cg_j\) are pairwise orthogonal, and
so are the final spaces \(Rg_j\).

### 2. The translated block span is an exact \(\ell_p\) or \(c_0\) copy

For every finitely supported scalar sequence \((a_j)\), the operators \(a_jx_j\)
form mutually orthogonal rectangular blocks. Their singular values concatenate.
Hence, for \(1\le p<\infty\),
\[
\left\|\sum_j a_jx_j\right\|_p
=
\left(\sum_j|a_j|^p\right)^{1/p},
\]
while for \(p=\infty\),
\[
\left\|\sum_j a_jx_j\right\|_\infty
=
\max_j|a_j|.
\]
The identical calculation for \(y_j\) gives
\[
\left\|\sum_j a_jy_j\right\|_p
=
r\left(\sum_j|a_j|^p\right)^{1/p}
\quad(1\le p<\infty),
\]
and
\[
\left\|\sum_j a_jy_j\right\|_\infty
=
r\max_j|a_j|.
\]

Let
\[
E=\overline{\operatorname{span}}\{x_j:j\ge1\}.
\]
Then \(E\) is isometric to \(\ell_p\) for \(p<\infty\), and to \(c_0\) for
\(p=\infty\), and
\[
\boxed{\|Tz\|_p=r\|z\|_p\qquad(z\in E)}.
\tag{1}
\]
The constant \(r\) can be made arbitrarily close to \(N\).

### 3. Exact distance to strictly singular, FSS and compact operators

Let \(S\in\mathcal{SS}(X_p)\). Since \(E\) is infinite-dimensional,
\(S|_E\) is not bounded below. Therefore, for every \(\delta>0\), there is
\(z\in E\) with \(\|z\|_p=1\) and
\[
\|Sz\|_p<\delta.
\]
By (1),
\[
\|T-S\|
\ge \|(T-S)z\|_p
\ge r-\delta.
\]
Letting \(\delta\downarrow0\), then \(\varepsilon\downarrow0\), yields
\[
\operatorname{dist}(T,\mathcal{SS}(X_p))\ge N.
\]
The reverse inequality follows by comparing with the zero operator. Hence
\[
\operatorname{dist}(T,\mathcal{SS}(X_p))=N.
\]
Since
\[
\mathcal K(X_p)\subseteq\mathcal{FSS}(X_p)\subseteq\mathcal{SS}(X_p)
\]
and all three classes contain zero, all three distances equal \(N\).

### 4. Bernstein, approximation and Gelfand numbers

For every \(n\), the \(n\)-dimensional space
\[
E_n=\operatorname{span}\{x_1,\ldots,x_n\}
\]
satisfies \(\|Tz\|=r\|z\|\). Therefore
\[
b_n(T)\ge r.
\]
As always \(b_n(T)\le\|T\|=N\); letting \(\varepsilon\downarrow0\) gives
\[
b_n(T)=N.
\]

Every operator of rank \(<n\) is strictly singular, so the distance result gives
\[
a_n(T)\ge N.
\]
The zero operator has rank \(0<n\), whence \(a_n(T)\le N\). Thus
\[
a_n(T)=N.
\]

Now let \(M\subset X_p\) have finite codimension. Then \(E\cap M\) is
infinite-dimensional. By (1),
\[
\|T|_M\|\ge r.
\]
Taking the infimum over subspaces of codimension \(<n\) and then
\(\varepsilon\downarrow0\) gives
\[
c_n(T)=N.
\]

### 5. Kolmogorov numbers: finite-dimensional targets cannot follow escaping blocks

Let \(L\subset X_p\) be finite-dimensional. Define the rectangular compression
\[
Q_j(z)=P_{Rg_j}\,z\,P_{Cg_j},
\]
where the \(P\)'s are the corresponding coordinate projections on \(\ell_2\Gamma\).
Each \(Q_j\) is contractive on \(S_p\), and
\[
Q_jy_j=y_j.
\]

For every fixed \(z\in X_p\),
\[
\|Q_jz\|_p\longrightarrow0.
\tag{2}
\]
Indeed, \(P_{Cg_j}\to0\) strongly along the pairwise disjoint coordinate sets, and
every \(z\in X_p\) is compact; finite-rank approximation gives
\(\|zP_{Cg_j}\|_p\to0\) (with operator norm when \(p=\infty\)).
Since \(L\) is finite-dimensional, compactness of its unit sphere upgrades (2) to
\[
\|Q_j|_L\|\longrightarrow0.
\tag{3}
\]

If \(\ell\in L\) has \(\|\ell\|_p>2r\), then
\[
\|y_j-\ell\|_p>r.
\]
For \(\|\ell\|_p\le2r\), contractivity and (3) give
\[
\|y_j-\ell\|_p
\ge
\|Q_j(y_j-\ell)\|_p
\ge
r-2r\|Q_j|_L\|.
\]
Hence
\[
\operatorname{dist}(y_j,L)\longrightarrow r.
\]
Since every \(x_j\) is a unit vector,
\[
\|Q_LT\|\ge r,
\]
where \(Q_L:X_p\to X_p/L\) is the quotient map. Taking the infimum over
\(\dim L<n\), followed by \(\varepsilon\downarrow0\), yields
\[
d_n(T)=N.
\]

### 6. Hausdorff measure of noncompactness

Let \(\rho<r\), and let \(z_1,\ldots,z_k\in X_p\) be arbitrary prospective centers.
By (2), choose \(j\) so large that
\[
\|Q_jz_i\|_p<r-\rho
\qquad(1\le i\le k).
\]
Then, for every \(i\),
\[
\|y_j-z_i\|_p
\ge
\|Q_j(y_j-z_i)\|_p
\ge
r-\|Q_jz_i\|_p
>\rho.
\]
Thus \(T(B_{X_p})\) cannot be covered by finitely many balls of radius
\(\rho<r\). Therefore
\[
\chi(T)\ge r.
\]
Since \(T(B_{X_p})\) is contained in the ball of radius \(N\),
\[
\chi(T)\le N.
\]
Letting \(\varepsilon\downarrow0\) proves
\[
\chi(T)=N.
\]

Combining the preceding steps proves every asserted equality.

## Relation to known results

Bennett's classical 1977 work developed the theory of Schur multipliers and, in the
Toeplitz setting on \(B(\ell_2)\), identified boundedness through Fourier--Stieltjes
data. Aleksandrov and Peller developed a detailed boundedness theory of Hankel and
Toeplitz--Schur multipliers.

Hladnik (2000) characterized compact Schur multipliers on \(B(H)\) using the Haagerup
tensor product \(c_0\otimes_h c_0\). This is directly relevant to compactness but has
a different ambient operator space and does not supply the flat
approximation/Gelfand/Kolmogorov/Bernstein profiles above.

Oikhberg (2010) computed approximation, Gelfand, Kolmogorov and Bernstein-type
quantities for **elementary** Schur multipliers with rank-one symbols
\(\phi_{ij}=a_ib_j\), including compact cases. The theorem above instead concerns
translation-invariant Toeplitz symbols \(m(rc^{-1})\), including relative patterns,
and gives a constant nondecaying profile for every bounded member of that class.

Neuwirth and Ricard (2011) developed transference between relative Fourier
multipliers and relative Toeplitz--Schur multipliers on Schatten--von Neumann--Orlicz
classes. In particular, their setup defines the relative spaces used here and records
finite-rectangle norm localization. Their paper focuses on transference, lacunarity,
unconditionality and multiplier norms rather than strict singularity or noncompact
\(s\)-number profiles.

Recent work on translation-invariant operators on Banach sequence/function spaces
(Karlovych and Shargorodsky, 2024) and on Wiener--Hopf operators (2026) establishes
maximal noncompactness in commutative function/sequence settings. Those results are
close in mechanism but do not treat Schur multipliers on Schatten classes. Work on
completely compact Herz--Schur multipliers of dynamical systems studies compactness
on reduced group \(C^*\)-algebraic objects rather than the Schatten-space operator
considered here.

## Originality and limitations

Originality is claimed **to the best of our knowledge** for the simultaneous
conclusions that bounded relative Toeplitz Schur multipliers on \(S_p\) have

- all four classical \(s\)-number sequences \(a_n,c_n,d_n,b_n\) identically equal
  to the operator norm;
- exact norm distance to the compact, finitely strictly singular and strictly
  singular operator classes; and
- Hausdorff measure of noncompactness equal to the norm.

Targeted searches for Toeplitz/Herz--Schur multipliers combined with strict
singularity, essential norm, approximation numbers, Gelfand numbers, Kolmogorov
numbers, Bernstein numbers and maximal noncompactness located the neighboring
literature above but no statement matching this package of conclusions.

The full text of Hladnik's 2000 paper was not available in the sources inspected,
so an equivalent consequence hidden there remains a residual originality risk.
Broad older Schur-multiplier and \(s\)-number literature was not exhaustively checked
theorem by theorem. Because noncompactness alone is close to established compact
Schur-multiplier theory, the novelty claim is deliberately centered on the exact flat
\(s\)-number profiles and the norm-distance-to-strict-singularity statement.

The theorem requires an infinite discrete group, a right-diagonally invariant
Toeplitz pattern \(I_\Lambda\), and a bounded multiplier on the indicated Schatten
space. It is stated only for Banach Schatten classes \(1\le p<\infty\) and
\(S_\infty=K\); no claim is made for quasi-Banach \(0<p<1\), arbitrary Schur symbols,
or complete \(s\)-number analogues.

## References

1. G. Bennett, “Schur multipliers,” *Duke Mathematical Journal* 44 (1977),
   603–639. https://doi.org/10.1215/S0012-7094-77-04426-X
2. A. B. Aleksandrov and V. V. Peller, “Hankel and Toeplitz-Schur multipliers,”
   *Mathematische Annalen* 324 (2002), 277–327.
   https://doi.org/10.1007/s00208-002-0339-z
3. M. Hladnik, “Compact Schur multipliers,” *Proceedings of the American
   Mathematical Society* 128 (2000), 2585–2591.
   https://doi.org/10.1090/S0002-9939-00-05708-7
4. T. Oikhberg, “Restricted Schur multipliers and their applications,”
   *Proceedings of the American Mathematical Society* 138 (2010), 1739–1750.
   https://doi.org/10.1090/S0002-9939-10-10203-2
5. S. Neuwirth and É. Ricard, “Transfer of Fourier multipliers into Schur
   multipliers and sumsets in a discrete group,” *Canadian Journal of Mathematics*
   63 (2011), 1161–1187. https://doi.org/10.4153/CJM-2011-053-9
6. W. He, I. G. Todorov and L. Turowska, “Completely Compact Herz-Schur
   Multipliers of Dynamical Systems,” *Journal of Fourier Analysis and Applications*
   28 (2022). https://doi.org/10.1007/s00041-022-09942-6
7. O. Karlovych and E. Shargorodsky, “Discrete Riesz transforms on
   rearrangement-invariant Banach sequence spaces and maximally noncompact
   operators,” *Pure and Applied Functional Analysis* 9 (2024), 195–210.
8. O. Karlovych and E. Shargorodsky, “Maximal noncompactness of Wiener-Hopf
   operators,” *Journal of Mathematical Sciences* 298 (2026), 438–447.
   https://doi.org/10.1007/s10958-025-08167-4
