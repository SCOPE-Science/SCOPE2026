# Assouad dimension is inf-harmonic under holomorphic motions

**Same-model review: passed. Cross-model review: not yet performed.**

## Main result

Let
\[
f:\mathbb D\times\widehat{\mathbb C}\to\widehat{\mathbb C}
\]
be a normalized holomorphic motion and let \(E\subset\mathbb C\) be bounded. Write
\(E_\lambda=f_\lambda(E)\).

### Theorem A

Either
\[
\dim_A(E_\lambda)=0\qquad(\lambda\in\mathbb D),
\]
or
\[
\boxed{\lambda\longmapsto \frac1{\dim_A(E_\lambda)}
\quad\text{is inf-harmonic on }\mathbb D.}
\]

Thus Question 1.11 of Menssen--Younsi, arXiv:2609.19522v1, has an affirmative answer.

The theorem is stronger than the already known planar quasiconformal Harnack-type distortion inequality for Assouad dimension: that inequality records only a two-point consequence of inf-harmonicity, whereas Theorem A identifies the full parameter dependence as a lower envelope of positive harmonic functions.

The key point is that the obstruction encountered for quasi-Assouad dimension disappears for full Assouad dimension once one uses a variable-radius packing characterization adapted to the unrestricted scale range.

## A variable-radius characterization of Assouad dimension

For a bounded nonempty \(F\subset\mathbb R^d\), \(x\in F\), \(R>0\), and a finite packing \(\mathcal B\) by pairwise disjoint closed balls whose centers lie in
\(\overline B(x,R)\cap F\) and whose radii are at most \(R\), define
\[
\mathcal P_t(\mathcal B;x,R)
   :=\sum_{B\in\mathcal B}
      \left(\frac{\operatorname{diam}B}{2R}\right)^t .
\]

### Lemma 1

For every bounded nonempty \(F\subset\mathbb R^d\),
\[
\boxed{
\dim_A F
=
\inf\left\{
t>0:
\sup_{x,R,\mathcal B}\mathcal P_t(\mathcal B;x,R)<\infty
\right\}.
}
\]
Equivalently, if \(t<\dim_A F\), then the normalized \(t\)-sums above are unbounded, while if \(t>\dim_A F\), they are uniformly bounded.

### Proof

If \(t<\dim_A F\), the equal-radius packing formulation of Assouad dimension implies that, for every \(M>0\), there exist \(x\in F\), \(0<r<R\), and an \(r\)-packing of
\(\overline B(x,R)\cap F\) with cardinality \(N\) satisfying
\[
N>M(R/r)^t.
\]
For that packing,
\[
\mathcal P_t=N(r/R)^t>M.
\]

Conversely, let \(t>\dim_A F\) and choose
\[
\dim_A F<s<t.
\]
There is a constant \(C_s\) such that every \(\rho\)-packing of
\(\overline B(x,R)\cap F\), \(0<\rho<R\), has at most
\[
C_s(R/\rho)^s
\]
balls. Given an arbitrary variable-radius packing \(\mathcal B\), place its balls into dyadic classes
\[
\mathcal B_j
=
\left\{
B\in\mathcal B:
2^{-j-1}R<r(B)\le 2^{-j}R
\right\},
\qquad j\ge0.
\]
Because the original balls are disjoint, the centers of the balls in
\(\mathcal B_j\) are separated by more than \(2^{-j}R\). Hence the same centers support an equal-radius \(2^{-j-1}R\)-packing, and therefore
\[
\#\mathcal B_j\le C_s\,2^{(j+1)s}.
\]
It follows that
\[
\mathcal P_t
\le
C_s2^s\sum_{j=0}^\infty 2^{-j(t-s)}
<\infty.
\]
This proves the criterion. \(\square\)

This lemma is an elementary consequence of the standard equal-radius characterization and is not claimed as an independent originality contribution.

## Proof of Theorem A

The proof adapts the inf-harmonic machinery of Menssen--Younsi, but the full Assouad scale range eliminates the most delicate scale-transfer step in their quasi-Assouad argument.

Assume
\[
d_0:=\dim_A(E_{\lambda_0})>0
\]
at some \(\lambda_0\in\mathbb D\). Fix \(p\in(|\lambda_0|,1)\) and work first on
\(\mathbb D(0,p)\). Set
\[
g_\lambda=f_\lambda\circ f_{\lambda_0}^{-1}.
\]
Uniform quasiconformality on \(\mathbb D(0,p)\) and quasisymmetry give a constant
\(c\ge1\), depending only on \(p\) and \(\lambda_0\), with the following property. If
\(x\in\mathbb C\), \(R>0\), \(y\in\partial B(x,2R)\), and \(z\in B(x,2R)\), then
\[
|g_\lambda(z)-g_\lambda(x)|
\le
c\,|g_\lambda(y)-g_\lambda(x)|.
\tag{1}
\]

Choose \(d_n\uparrow d_0\), with \(0<d_n<d_0\). By the equal-radius packing characterization of Assouad dimension, there are \(x_n\in E_{\lambda_0}\),
\(0<r_n<R_n\), and an \(r_n\)-packing \(\mathcal B_n\) centered in
\(\overline B(x_n,R_n)\cap E_{\lambda_0}\) such that
\[
\sum_{B\in\mathcal B_n}
\left(\frac{\operatorname{diam}B}{2R_n}\right)^{d_n}>n.
\tag{2}
\]
Every \(B\in\mathcal B_n\) lies in \(B(x_n,2R_n)\). Fix
\(y_n\in\partial B(x_n,2R_n)\) and put
\[
L_n(\lambda)
=
|g_\lambda(y_n)-g_\lambda(x_n)|.
\]
From (1),
\[
\operatorname{diam}g_\lambda(B)\le 2cL_n(\lambda).
\tag{3}
\]

For \(B\in\mathcal B_n\), define
\[
a_{n,B}(\lambda)
=
\frac{\operatorname{diam}g_\lambda(B)}
     {4cL_n(\lambda)}.
\]
Then \(0<a_{n,B}\le1/2\). The diameter-ratio lemma for holomorphic motions
(Menssen--Younsi, Lemma 4.1) shows that
\[
\lambda\mapsto \log\frac1{a_{n,B}(\lambda)}
\]
is inf-harmonic. Define \(s_n(\lambda)>0\) implicitly by
\[
\sum_{B\in\mathcal B_n}a_{n,B}(\lambda)^{s_n(\lambda)}
=
\sum_{B\in\mathcal B_n}a_{n,B}(\lambda_0)^{d_n}.
\tag{4}
\]
Because \(a_{n,B}\in(0,1)\), the inf-harmonic implicit-function theorem of
Fuhrer--Ransford--Younsi, in the form quoted as Menssen--Younsi Theorem 2.9,
gives that \(1/s_n\) is inf-harmonic. Since \(g_{\lambda_0}\) is the identity and
\(|y_n-x_n|=2R_n\),
\[
s_n(\lambda_0)=d_n.
\]
The compactness theorem for inf-harmonic functions therefore provides, after passing to a subsequence,
an inf-harmonic limit \(u\) on \(\mathbb D(0,p)\) satisfying
\[
u(\lambda_0)=\frac1{d_0}.
\tag{5}
\]

We claim
\[
u(\lambda)\ge \frac1{\dim_A(E_\lambda)}
\qquad(\lambda\in\mathbb D(0,p)).
\tag{6}
\]
Fix \(\lambda\) and \(0<b<1/u(\lambda)\). For large \(n\), \(s_n(\lambda)>b\), hence
\[
\sum_{B\in\mathcal B_n}a_{n,B}(\lambda)^b
\ge
\sum_{B\in\mathcal B_n}a_{n,B}(\lambda)^{s_n(\lambda)}.
\tag{7}
\]
At \(\lambda_0\),
\[
a_{n,B}(\lambda_0)
=
\frac{\operatorname{diam}B}{8cR_n}
=
\frac1{4c}\frac{\operatorname{diam}B}{2R_n}.
\]
Combining (2), (4), and (7), and using \(d_n\le2\), gives
\[
\sum_{B\in\mathcal B_n}a_{n,B}(\lambda)^b
\longrightarrow\infty.
\tag{8}
\]

A uniform quasiconformal inscribed-ball estimate supplies, inside each
\(g_\lambda(B)\), a closed disk \(B^\ast\) centered at a point of \(E_\lambda\)
whose diameter is at least a fixed positive constant times
\(\operatorname{diam}g_\lambda(B)\). Since the sets \(g_\lambda(B)\) are mutually disjoint,
the disks \(B^\ast\) form a packing. By (1), all of them lie in
\[
B(g_\lambda(x_n),R_n'),\qquad
R_n':=cL_n(\lambda),
\]
and each has radius at most \(R_n'\). Consequently, for a constant
\(\kappa=\kappa(p,\lambda_0)>0\),
\[
\sum_{B^\ast}
\left(\frac{\operatorname{diam}B^\ast}{2R_n'}\right)^b
\ge
\kappa^b
\sum_{B\in\mathcal B_n}a_{n,B}(\lambda)^b
\longrightarrow\infty.
\tag{9}
\]
Lemma 1 gives \(\dim_A(E_\lambda)\ge b\). Letting
\(b\uparrow1/u(\lambda)\) proves (6).

The same conclusion also shows that positivity of Assouad dimension propagates from one parameter to every parameter. Letting \(p\uparrow1\) and using compactness once more gives a global inf-harmonic majorant touching
\(1/\dim_A(E_\lambda)\) at the arbitrary point \(\lambda_0\). Taking the pointwise infimum of these touching majorants over \(\lambda_0\) yields exactly
\[
\lambda\mapsto\frac1{\dim_A(E_\lambda)},
\]
which is therefore inf-harmonic. This proves Theorem A. \(\square\)

### Why the full Assouad case is simpler than the quasi-Assouad case

Menssen--Younsi must preserve an additional relation between the packing-ball radii and the ambient radius in order to treat quasi-Assouad dimension. This requires their Hölder-scale estimate in the middle of Lemma 4.2. For full Assouad dimension there is no such scale-gap restriction: after transfer, it is enough that the target balls form a packing with radii at most the target ambient radius. Lemma 1 converts exactly that information into an Assouad lower bound.

## Symmetric strengthening

The same simplification also upgrades the symmetric theorem in Menssen--Younsi.

### Theorem B

Let \(E\subset\mathbb R\) be bounded and let
\[
f:\mathbb D\times\widehat{\mathbb C}\to\widehat{\mathbb C}
\]
be a holomorphic motion symmetric with respect to the real line:
\[
f(\lambda,z)
=
\overline{f(\overline\lambda,\overline z)}.
\]
Then either \(\dim_A(E_\lambda)=0\) for all \(\lambda\), or
\[
\boxed{
\lambda\longmapsto\frac1{\dim_A(E_\lambda)}
\quad\text{is inf-sym-harmonic.}
}
\]

### Proof

Repeat the proof of Theorem A using the symmetric diameter-ratio lemma and symmetric implicit-function theorem of Menssen--Younsi, Section 5. For a source packing disk \(B\), replace its diameter in the implicit function by
\[
\operatorname{diam}\!\left(B\cap f_{\lambda_0}(\mathbb R)\right).
\]
Because \(B\) is centered on the unbounded curve \(f_{\lambda_0}(\mathbb R)\),
\[
\operatorname{diam}\!\left(B\cap f_{\lambda_0}(\mathbb R)\right)
\ge \frac12\operatorname{diam}B.
\]
Thus the source normalized sums still diverge up to a fixed factor. The target quasiconformal image of \(B\) contains an inscribed disk whose diameter controls from below the image diameter of this curve intersection. Lemma 1 again converts the resulting variable-radius target packing into a full Assouad lower bound. The touching-majorant argument is unchanged, with inf-sym-harmonic functions replacing inf-harmonic functions. \(\square\)

## Consequence for quasicircles

Combining Theorem B with the symmetric holomorphic motion and symmetric Harnack estimate used by Smirnov and by Menssen--Younsi gives the full-Assouad analogue of their Corollary 1.14:

### Corollary

If \(\Gamma\) is a \(k\)-quasicircle, then
\[
\boxed{\dim_A\Gamma\le 1+k^2.}
\]

Indeed, the reduction used in Menssen--Younsi writes a relevant arc of \(\Gamma\) as
\(f_{ik}([a,b])\) for a symmetric holomorphic motion. With
\[
u(\lambda)=\frac1{\dim_A(E_\lambda)},\qquad
v=u-\frac12,
\]
Theorem B makes \(v\) inf-sym-harmonic. The symmetric Harnack inequality gives
\[
v(ik)\ge
\frac{1-k^2}{1+k^2}v(0)
=
\frac12\frac{1-k^2}{1+k^2},
\]
because \(\dim_A[a,b]=1\). Rearrangement gives the stated bound; finite stability of Assouad dimension handles the whole quasicircle.

The numerical \(1+k^2\) bound is presented here as a consequence of Theorem B. The originality assessment of this record does not rely on a separate priority claim for that numerical corollary.

## Relation to prior work and originality boundary

Menssen and Younsi, *Holomorphic motions, Assouad dimension and quasiconformal mappings* (arXiv:2609.19522v1, submitted 17 September 2026), prove the corresponding inf-harmonic and inf-sym-harmonic theorems for quasi-Assouad dimension. Their Question 1.11 explicitly asks whether their main theorem remains true for full Assouad dimension and states that they were unable to prove it.

Chrontsios Garitsis and Tyson had already established sharp planar quasiconformal distortion inequalities for Assouad dimension. Menssen--Younsi explicitly note that the Harnack-type consequence of their quasi-Assouad theorem is therefore already known for full Assouad dimension. That prior two-point distortion theorem does not imply the inf-harmonic variation asserted here.

The originality claim is restricted to the affirmative solution of Menssen--Younsi Question 1.11, the symmetric full-Assouad strengthening, and the variable-radius transfer mechanism proving these statements. No originality is claimed for the standard equal-radius packing definition, quasiconformal inscribed-ball estimates, inf-harmonic compactness/implicit-function machinery, or Smirnov's symmetric-motion argument.

## Limitations

- The result concerns bounded planar sets under holomorphic motions of the sphere. It does not resolve the still-open holomorphic-motion questions for Hausdorff or upper Minkowski dimension.
- The variable-radius packing lemma is elementary and may be regarded as folklore; its use here is the relevant point.
- No endpoint regularity, quantitative modulus beyond what follows from inf-harmonicity, or higher-dimensional analogue is asserted.
- The principal source preprint was submitted only one day before this record. A contemporaneous observation not yet indexed remains a residual originality risk.
- The quasicircle corollary is not used as the sole basis for the originality verdict.

## References

1. K. Menssen and M. Younsi, *Holomorphic motions, Assouad dimension and quasiconformal mappings*, arXiv:2609.19522v1 (2026). https://arxiv.org/abs/2609.19522
2. A. Fuhrer, T. Ransford and M. Younsi, *Holomorphic motions, dimension, area and quasiconformal mappings*, J. Math. Pures Appl. 177 (2023), 455--483. https://doi.org/10.1016/j.matpur.2023.07.009
3. E. K. Chrontsios Garitsis and J. T. Tyson, *Quasiconformal distortion of the Assouad spectrum and classification of polynomial spirals*, Bull. Lond. Math. Soc. 55 (2023), 282--307. https://doi.org/10.1112/blms.12727
4. S. Smirnov, *Dimension of quasicircles*, Acta Math. 205 (2010), 189--197. https://doi.org/10.1007/s11511-010-0053-8
5. J. M. Fraser, *Assouad Dimension and Fractal Geometry*, Cambridge Tracts in Mathematics 222, Cambridge University Press (2021). https://arxiv.org/abs/2005.03763
