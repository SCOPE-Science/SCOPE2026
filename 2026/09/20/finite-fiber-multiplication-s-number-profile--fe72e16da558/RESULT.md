# Exact s-number profiles for finite-fiber multiplication operators

## Statement

Let \((\Omega,\Sigma,\mu)\) be a sigma-finite measure space. Modulo null sets, write
\[
\Omega=\Omega_c\sqcup\bigsqcup_{j\ge1}A_j,
\]
where \(\Omega_c\) is nonatomic and the \(A_j\) are the (at most countably many) atoms. Fix \(1<p<\infty\) and finite-dimensional Euclidean spaces \(\mathbb C^d\) and \(\mathbb C^m\). Let
\[
A:\Omega\longrightarrow M_{m\times d}(\mathbb C)
\]
be measurable and essentially bounded, and let
\[
M_A:L_p(\Omega;\mathbb C^d)\to L_p(\Omega;\mathbb C^m),
\qquad (M_Af)(\omega)=A(\omega)f(\omega).
\]

On every atom \(A_j\), the matrix field is almost everywhere constant; denote this matrix by \(A_j\). Put \(q=\min\{m,d\}\), and write
\[
s_1(A_j)\ge\cdots\ge s_q(A_j)\ge0
\]
for its singular values. Define the nonatomic floor
\[
\gamma:=\operatorname*{ess\,sup}_{\omega\in\Omega_c}\|A(\omega)\|,
\]
with \(\gamma=0\) if \(\Omega_c\) is null. For \(n\ge1\), let
\[
\beta_n:=\inf_{\substack{F\subset \mathbb N\times\{1,\dots,q\}\\ |F|<n}}
\ \sup_{(j,k)\notin F}s_k(A_j),
\]
where \(\sup\varnothing=0\), and set
\[
\alpha_n:=\max\{\gamma,\beta_n\}.
\]
Thus \((\beta_n)\) is the nonincreasing rearrangement, with multiplicity, of all singular values of the atomic matrices.

**Theorem.** For every \(n\ge1\),
\[
\boxed{
 a_n(M_A)=b_n(M_A)=c_n(M_A)=d_n(M_A)=\alpha_n,
}
\]
where \(a_n,b_n,c_n,d_n\) are respectively the approximation, Bernstein, Gelfand and Kolmogorov numbers with the standard rank/dimension/codimension convention \(<n\).

Consequently, if
\[
\beta_\infty:=\lim_{n\to\infty}\beta_n,
\qquad
\rho:=\max\{\gamma,\beta_\infty\},
\]
then
\[
\boxed{
\operatorname{dist}(M_A,\mathcal K)
=\operatorname{dist}(M_A,\mathcal{FSS})
=\operatorname{dist}(M_A,\mathcal{SS})
=\rho.
}
\]
In particular,
\[
M_A\text{ compact}
\iff M_A\text{ finitely strictly singular}
\iff M_A\text{ strictly singular}
\iff \rho=0.
\]
Equivalently, compactness/strict singularity holds exactly when \(A=0\) almost everywhere on \(\Omega_c\) and \(\|A_j\|\to0\) along the atomic part.

## Proof

### 1. Atomic reduction and the upper approximation bound

A scalar measurable function is almost everywhere constant on an atom; applying this entrywise gives the matrices \(A_j\). Since the measure is sigma-finite, every non-null atom has finite measure and there are at most countably many atoms.

Fix \(n\) and \(\varepsilon>0\). Choose a finite set
\(F\subset\mathbb N\times\{1,\dots,q\}\), \(|F|<n\), such that
\[
\sup_{(j,k)\notin F}s_k(A_j)\le \beta_n+\varepsilon.
\]
For every atomic block occurring in \(F\), retain precisely the singular-vector rank-one terms indexed by \(F\), and set the approximant equal to zero on the nonatomic part. This produces a global finite-rank operator \(R\) with \(\operatorname{rank}R< n\). Because the Bochner \(L_p\) norm is an \(\ell_p\)-sum over disjoint atoms,
\[
\|M_A-R\|
\le \max\{\gamma,\beta_n+\varepsilon\}.
\]
Hence \(a_n(M_A)\le\alpha_n\).

### 2. Lower witnesses

Let \(t<\alpha_n\).

If \(t<\gamma\), then
\[
E_t:=\{\omega\in\Omega_c:\|A(\omega)\|>t\}
\]
has positive measure. Choose a countable dense subset of the unit sphere of \(\mathbb C^d\). Since
\(\|A(\omega)\|=\sup_v\|A(\omega)v\|\), one fixed unit vector \(v\) and a positive-measure nonatomic set \(E\subset E_t\) satisfy
\[
\|A(\omega)v\|>t\qquad(\omega\in E\text{ a.e.}).
\]
Therefore the infinite-dimensional subspace
\[
Y=\{\varphi v:\varphi\in L_p(E)\}
\]
satisfies \(\|M_Ay\|\ge t\|y\|\) for all \(y\in Y\).

If instead \(t<\beta_n\), then at least \(n\) atomic singular modes have singular value greater than \(t\). The corresponding right singular vectors, placed in their atomic blocks, span an \(n\)-dimensional subspace \(Y_n\) on which
\[
\|M_Ay\|\ge t\|y\|.
\]
(The modes remain orthogonal inside each Euclidean fiber and form disjoint \(\ell_p\)-blocks across distinct atoms.)

Thus, in either case, there is an \(n\)-dimensional subspace on which \(M_A\) is bounded below by \(t\) (using any \(n\)-dimensional subspace of the nonatomic witness when necessary). Hence
\[
b_n(M_A)\ge t.
\]
Also, every operator of rank \(<n\) has a nonzero kernel vector on this witness, giving \(a_n(M_A)\ge t\); and every subspace of codimension \(<n\) meets the witness nontrivially, giving \(c_n(M_A)\ge t\). Letting \(t\uparrow\alpha_n\), and using the standard inequalities \(b_n,c_n\le a_n\), yields
\[
a_n(M_A)=b_n(M_A)=c_n(M_A)=\alpha_n.
\]

### 3. Kolmogorov numbers

Let \(p'\) be conjugate to \(p\), and consider
\[
S=M_{A^*}:L_{p'}(\Omega;\mathbb C^m)\to L_{p'}(\Omega;\mathbb C^d).
\]
Since \(1<p<\infty\), the usual Bochner duality identifies \(S'\) with \(M_A\). The atomic singular values of \(A_j^*\) equal those of \(A_j\), and the nonatomic norm floor is unchanged. Thus the preceding argument gives
\(c_n(S)=\alpha_n\). The standard duality identity
\[
d_n(S')=c_n(S)
\]
then gives \(d_n(M_A)=\alpha_n\).

### 4. Exact distances to compact and singular ideals

Let \(t>\rho\). Only finitely many atomic singular modes exceed \(t\). Keeping those modes gives a finite-rank operator \(R_t\) such that
\[
\|M_A-R_t\|\le t.
\]
Letting \(t\downarrow\rho\) proves
\[
\operatorname{dist}(M_A,\mathcal K)\le\rho.
\]

Conversely, if \(t<\rho\), then either \(t<\gamma\), which gives the infinite-dimensional nonatomic witness above, or infinitely many atomic singular modes exceed \(t\), whose closed span is an \(\ell_p\)-type subspace on which \(M_A\) is bounded below by \(t\). Let \(Y\) be such a subspace. If \(S\) is strictly singular, then \(S|_Y\) is not bounded below, so for every \(\varepsilon>0\) there is \(y\in Y\), \(\|y\|=1\), with \(\|Sy\|<\varepsilon\). Therefore
\[
\|M_A-S\|\ge \|(M_A-S)y\|\ge t-\varepsilon.
\]
Hence \(\operatorname{dist}(M_A,\mathcal{SS})\ge t\), and letting \(t\uparrow\rho\) gives the lower bound \(\rho\). Since
\[
\mathcal K\subset\mathcal{FSS}\subset\mathcal{SS},
\]
all three distances equal \(\rho\).

## Context and comparison with known results

The scalar nonatomic endpoint is classical. Plichko and Shevchik proved for multiplication operators on rearrangement-invariant spaces over their atomless setting that compactness and strict singularity coincide and force the multiplication operator itself to be zero. The present theorem recovers that rigidity as the case with no atoms, and additionally identifies every finite approximation/Bernstein/Gelfand/Kolmogorov scale with the operator norm.

The purely atomic scalar theory is also classical: Hutton, Morrell and Retherford studied diagonal operators, approximation numbers and Kolmogorov diameters, and later work on vector-valued sequence spaces gives approximation results and compactness/approximability criteria for block-diagonal matrix transformations. In particular, Gupta and Acharya proved that a diagonal map on their vector-valued sequence spaces is approximable exactly when its component maps are approximable and the component norms tend to zero. These results are prior art and are not claimed as new here.

Duru, Kitover and Orhon characterize scalar multiplication operators on vector-valued Köthe-Bochner spaces. Heymann's 2015 thesis develops multiplication operators on Bochner spaces and Banach fibre spaces, and Budde and Heymann later study operator-valued multiplication operators and their extrapolation spaces on Bochner \(L_p\)-spaces. The contribution claimed here is the simultaneous, exact, \(p\)-independent formula for four classical s-number scales for finite Euclidean fibers on an arbitrary mixed sigma-finite measure space, together with the exact norm distance to the compact, finitely strictly singular and strictly singular classes.

To the best of our knowledge, the inspected literature did not identify this combined matrix-valued mixed-measure statement. The Hilbert-space case \(p=2\) is closely related to standard decomposable-operator/spectral arguments and is not claimed separately as a novel phenomenon.

## Limitations

- The theorem assumes fixed finite-dimensional Euclidean fibers and \(1<p<\infty\). Infinite-dimensional fibers can contribute genuinely compact or strictly singular fiber behavior not captured by a finite singular-value multiset.
- Endpoints \(p=1,\infty\) are not included; the proof of the Kolmogorov-number identity uses reflexive Bochner duality.
- The originality claim is to the best of our knowledge. Hutton--Morrell--Retherford (1976), Pietsch's classical operator-ideal monographs, Heymann's 2015 thesis, and older direct-integral/decomposable-operator literature were not all exhaustively inspected in full. Those sources are the principal residual risk for an equivalent statement under different terminology.
- Gupta--Acharya (2011) provides vector-valued diagonal approximation theory and an approximability criterion, so novelty is not claimed for the bare compactness criterion on a purely atomic block-diagonal space.

## References

1. A. Plichko and V. Shevchik, *On Restriction Properties of Multiplication Operators*, Z. Anal. Anwend. 18 (1999), 27--35. https://doi.org/10.4171/ZAA/867
2. C. V. Hutton, J. S. Morrell and J. R. Retherford, *Diagonal operators, approximation numbers, and Kolmogoroff diameters*, J. Approx. Theory 16 (1976), 48--80. https://doi.org/10.1016/0021-9045(76)90095-2
3. M. Gupta and L. R. Acharya, *Approximation numbers of matrix transformations and inclusion maps*, Tamkang J. Math. 42 (2011), 193--203. https://doi.org/10.5556/j.tkjm.42.2011.193-203
4. H. Duru, A. Kitover and M. Orhon, *Multiplication operators on vector-valued function spaces*, Proc. Amer. Math. Soc. 141 (2013), 3501--3513. https://doi.org/10.1090/S0002-9939-2013-11603-5
5. R. Heymann, *Multiplication operators on Bochner spaces and Banach fibre spaces*, PhD thesis, Eberhard-Karls-Universität Tübingen (2015). https://doi.org/10.15496/publikation-5350
6. C. Budde and R. Heymann, *Extrapolation of operator-valued multiplication operators*, Quaest. Math. 45 (2022), 347--356. https://doi.org/10.2989/16073606.2020.1859639
7. T. Ullrich, *Inequalities between s-numbers*, Adv. Oper. Theory 9 (2024). https://doi.org/10.1007/s43036-024-00386-x
