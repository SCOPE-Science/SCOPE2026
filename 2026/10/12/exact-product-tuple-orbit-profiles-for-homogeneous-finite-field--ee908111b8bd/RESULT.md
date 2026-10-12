# Exact product tuple-orbit profiles for homogeneous finite-field bilinear spaces

## Finding
Fix a prime power \(q\). Let \(M_q\), \(M_q^{\mathrm s}\), and \(M_q^{\mathrm a}\) denote the unique countable existentially closed bilinear spaces over \(\mathbb F_q\) in the unrestricted, symmetric, and alternating fixed-field theories studied by Kamsma. For ordered \(n\)-tuples, their automorphism-orbit counts are
\[
B_n(q)=\sum_{r=0}^{n}{n\brack r}_q q^{r^2},
\]
\[
\boxed{S_n(q)=\sum_{r=0}^{n}{n\brack r}_q q^{r(r+1)/2}=\prod_{i=1}^{n}(1+q^i)},
\]
and
\[
\boxed{A_n(q)=\sum_{r=0}^{n}{n\brack r}_q q^{r(r-1)/2}=\prod_{i=0}^{n-1}(1+q^i)}.
\]
Here \({n\brack r}_q\) is the Gaussian binomial coefficient. Hence
\[
\boxed{\frac{S_n(q)}{A_n(q)}=\frac{1+q^n}{2}}\qquad(n\ge1).
\]

The linearly independent \(n\)-tuple strata have respectively \(q^{n^2}\), \(q^{n(n+1)/2}\), and \(q^{n(n-1)/2}\) orbits. If
\[
C_q=\prod_{j=1}^{\infty}(1+q^{-j}),
\]
then, for fixed \(q\),
\[
\frac{B_n(q)}{q^{n^2}}\longrightarrow1,\qquad
\frac{S_n(q)}{q^{n(n+1)/2}}\longrightarrow C_q,
\]
while
\[
\frac{A_n(q)}{q^{n(n-1)/2}}\longrightarrow2C_q.
\]
Thus dependence strata disappear asymptotically in the unrestricted bilinear orbit profile, but survive as an exact constant-factor correction in the symmetric and alternating theories.

## Assumptions and scope
The field is fixed and finite. Kamsma's language names scalar multiplication by every field element and names each value of the bilinear form. Over finite fields the positive theory is Boolean and has quantifier elimination; every existentially closed model is finitely injective, and there is a unique countable existentially closed model up to isomorphism.

The claim counts all ordered tuples, including repetitions and arbitrary linear dependence. The forms need not be nondegenerate on the span of the tuple. In characteristic two, “alternating” still means \([x,x]=0\), so an alternating matrix has zero diagonal and is determined by its entries strictly above the diagonal; the stated count remains valid.

## Proof
Let \(a=(a_1,\ldots,a_n)\) be a tuple in one of the three countable existentially closed models, and let
\[
L_a:\mathbb F_q^n\to M,\qquad e_i\mapsto a_i.
\]
Put \(K_a=\ker L_a\). The pullback form
\[
\beta_a(u,v)=[L_a(u),L_a(v)]
\]
vanishes whenever one argument lies in \(K_a\), so it descends uniquely to a bilinear form \(\bar\beta_a\) on \(\mathbb F_q^n/K_a\). It is symmetric or alternating exactly when the ambient form is.

Conversely, suppose two tuples \(a,b\) have the same kernel \(K\) and the same descended form. The coordinate map \(a_i\mapsto b_i\) is then a well-defined linear isomorphism between their finite-dimensional spans and preserves the bilinear form. Kamsma proves that quantifier-free type determines complete type, and over a finite field the theory has quantifier elimination. Equivalently, finite injectivity gives the same conclusion by back-and-forth in the unique countable model. Hence the two tuples are in the same automorphism orbit. Any pair \((K,\bar\beta)\) occurs because finite injectivity embeds the finite bilinear space \((\mathbb F_q^n/K,\bar\beta)\) into the existentially closed model.

If \(r=\dim(\mathbb F_q^n/K)\), there are \({n\brack r}_q\) possible kernels. An arbitrary bilinear form on an \(r\)-space is specified by \(r^2\) field values, a symmetric form by \(r(r+1)/2\) values, and an alternating form by \(r(r-1)/2\) values. This gives the three Gaussian-binomial sums.

For the product formulas use the finite \(q\)-binomial identity
\[
\sum_{r=0}^{n}{n\brack r}_q q^{r(r-1)/2}t^r
 =\prod_{i=0}^{n-1}(1+tq^i).
\]
It follows directly by induction from the Gaussian Pascal recurrence, so no classification of bilinear forms up to congruence is involved. Setting \(t=1\) gives the alternating product, and setting \(t=q\) gives the symmetric product. Their quotient is immediately \((1+q^n)/2\).

For the asymptotics, the two product formulas give
\[
q^{-n(n+1)/2}S_n(q)=\prod_{j=1}^{n}(1+q^{-j})\to C_q
\]
and
\[
q^{-n(n-1)/2}A_n(q)=2\prod_{j=1}^{n-1}(1+q^{-j})\to2C_q.
\]
For the unrestricted case write \(r=n-k\). Using
\[
{n\brack k}_q=q^{k(n-k)}\frac{\prod_{i=0}^{k-1}(1-q^{-(n-i)})}{\prod_{j=1}^{k}(1-q^{-j})},
\]
the normalized codimension-\(k\) contribution is at most
\[
\frac{q^{-nk}}{\prod_{j\ge1}(1-q^{-j})}.
\]
Summing over \(k\ge1\) is \(O(q^{-n})\), proving \(B_n(q)/q^{n^2}\to1\).

## Verification
A standalone verifier independently enumerates all subspaces of \(\mathbb F_2^n\) through \(n=4\) and of \(\mathbb F_3^n\) through \(n=3\), using row reduction rather than the Gaussian formula. It also enumerates small arbitrary, symmetric, and alternating matrices directly and checks their counts against the claimed exponents. Finally it evaluates the three orbit-profile sums for several fields and arities, checks both product identities and the exact ratio, and numerically checks convergence to the stated constants. It reports `VERIFY_OK 208 exact/numerical assertions`.

The finite computation is a replay of the enumerative part, not a substitute for the all-arity structural proof.

## Relationship to prior work
Kamsma proves that existentially closed fixed-field bilinear spaces are exactly the finitely injective ones, that quantifier-free type determines complete type, and that finite fields give quantifier elimination and a countable categorical theory. He observes only that finitely many tuple types occur over finite fields; the inspected paper does not enumerate them.

Kantor, Liebeck, and Macpherson provide earlier finite-field \(\aleph_0\)-categorical context. A prior comparison result for a universal homogeneous cubic space uses the analogous kernel-plus-pullback-tensor idea, but its orbit count has a cubic exponent and does not imply the bilinear product formulas or the symmetric/alternating constant-factor phenomenon. Targeted searches for bilinear tuple-orbit counts, Gaussian-binomial profiles, and the displayed products did not locate an equivalent statement.

## Limitations
The deduction is short once Kamsma's finite injectivity and quantifier-free type description are combined with the classical finite \(q\)-binomial theorem, so folklore risk is real. No claim is made that the formulas were inaccessible to earlier specialists. The result concerns the fixed finite-field one-sorted theories, not two-sorted bilinear-space theories with a varying field. It counts ordered tuple orbits, not conjugacy classes of bilinear forms under change of basis.

## References
1. Mark Kamsma, *Bilinear spaces over a fixed field are simple unstable*, arXiv:2203.04844; Annals of Pure and Applied Logic 174 (2023), 103268. DOI: 10.1016/j.apal.2023.103268.
2. W. M. Kantor, Martin W. Liebeck, and H. D. Macpherson, *\(\aleph_0\)-Categorical Structures Smoothly Approximated by Finite Substructures*, Proceedings of the London Mathematical Society 59 (1989), 439–463. DOI: 10.1112/plms/s3-59.3.439.
