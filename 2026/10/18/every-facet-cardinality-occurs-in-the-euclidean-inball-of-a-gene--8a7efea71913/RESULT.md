# Every facet cardinality occurs in the Euclidean inball of a generalized parking-function polytope

## Finding
For every integer \(n\ge 2\) and every vector \(\mathbf b=(b_1,\ldots,b_n)\in\mathbb Z_{>0}^{n}\), let \(\mathfrak X_n(\mathbf b)\) be the convex hull in \(\mathbb R^n\) of all \(\mathbf b\)-parking functions. Put
\[
S_j=\sum_{i=1}^{j}b_i,\qquad
U_k=\sum_{j=n-k+1}^{n}S_j,\qquad
R_k=\frac{U_k-k}{k+\sqrt{k}}\quad(1\le k\le n).
\]
The exact ambient-Euclidean inradius and its **unique** incenter are
\[
\boxed{r(\mathfrak X_n(\mathbf b))=\min_{1\le k\le n}R_k,\qquad
c=(1+r(\mathfrak X_n(\mathbf b)))\mathbf 1.}
\]
Write \(K(\mathbf b)=\{k: R_k=\min_jR_j\}\). The inball is tangent to all \(n\) lower-coordinate facets \(x_i=1\), and, for every \(k\in K(\mathbf b)\), to **every** upper subset facet \(\sum_{i\in I}x_i=U_k\) with \(|I|=k\); it is tangent to no other facets. Thus the total number of distinct tangent facets is \(n+\sum_{k\in K(\mathbf b)}\binom nk\). If \(b_1=1\), the redundant upper inequalities with \(k=n-1\) are not active.

Every cardinality occurs genuinely: for **every** fixed \(n\ge2\) and every \(k\in\{1,\ldots,n\}\) there exists a strictly positive integral vector \(\mathbf b\) with \(K(\mathbf b)=\{k\}\). In particular, interior sizes can uniquely control the inball, unlike the endpoint-only phase behavior of the two-parameter specialization.

## Assumptions and scope
A \(\mathbf b\)-parking function is a positive integer vector whose increasingly reordered coordinates \(\beta'_j\) satisfy \(\beta'_j\le S_j\). The inradius is the supremum of \(r\ge0\) such that a closed standard Euclidean ball \(c+rB_2^n\) is contained in the polytope. All \(b_i\) are strictly positive integers, and \(n\ge2\); this ensures full dimension. No statement is made here about other norms, nonintegral parameter vectors, or the degenerate single-point case.

The known complete halfspace description (Bayer et al., Theorem 2.3(c), first released in March 2024) consists of
\[
x_i\ge1\quad(1\le i\le n),\qquad
\sum_{i\in I}x_i\le U_{|I|}\quad(\varnothing\ne I\subseteq[n]).
\]
Every upper subset inequality is facet-defining except those of size \(n-1\) if \(b_1=1\), when they are redundant. The formula uses all sizes, including redundant inequalities; this does not change the polytope or the minimum.

## Proof
**1. Universal bound.** If a Euclidean ball of radius \(r\) centered at \(c\) is contained in \(\mathfrak X_n(\mathbf b)\), the lower coordinate halfspaces force \(c_i\ge1+r\) for every \(i\), hence \(\sum_i c_i\ge n(1+r)\). For any fixed \(k\), the upper halfspaces and the Euclidean norm \(\|\mathbf 1_I\|_2=\sqrt{k}\) give
\[
\sum_{i\in I}c_i+r\sqrt{k}\le U_k\quad\text{for every }I\subseteq[n],\ |I|=k.
\]
Averaging over all \(\binom nk\) such subsets gives \(k\sum_i c_i/n+r\sqrt{k}\le U_k\), and consequently
\[
(k+\sqrt{k})r\le U_k-k.
\]
Thus \(r\le R_k\) for each \(k\).

**2. Attainment.** Let \(r_* =\min_k R_k\) and \(c_*=(1+r_*)\mathbf1\). For the proposed ball, every lower halfspace is met exactly at distance \(r_*\). For every upper subset of cardinality \(k\),
\[
\sum_{i\in I}(c_*)_i+r_*\sqrt{k}
=k+(k+\sqrt{k})r_*\le U_k.
\]
The complete halfspace description therefore proves \(c_*+r_*B_2^n\subseteq\mathfrak X_n(\mathbf b)\), meeting the bound.

**3. Uniqueness and contacts.** If \(c\) centers any optimal ball and \(k\in K(\mathbf b)\), both bounds in step 1 are equalities. Since every \(c_i\ge1+r_*\) and their average is at most \(1+r_*\), all coordinates must equal \(1+r_*\). This proves uniqueness. At this center, each lower facet lies at distance \(r_*\), and an upper facet indexed by size \(k\) lies at distance \((U_k-k(1+r_*))/\sqrt{k}\), equal to \(r_*\) precisely when \(R_k=r_*\). A supporting hyperplane at distance \(r_*\) touches the contained ball at a point of the polytope, hence the claimed facets really contact it. For \(b_1=1\), the identity \(U_n-n=U_{n-1}-(n-1)>0\) and the strictly larger denominator \(n+\sqrt n\) show \(R_n<R_{n-1}\); therefore a redundant upper inequality never contributes a spurious contact.

**4. Realization of every contact size.** First consider auxiliary nonnegative parameters \(b_1=1+u\), \(b_2=\cdots=b_{n-1}=0\), \(b_n=B\) with \(u,B>0\) (for \(n=2\), the middle list is empty). Then \(U_j-j=ju+B\) and
\[
R_j=\frac{ju+B}{j+\sqrt j}.
\]
For \(1\le j<n\), consecutive values are equal exactly when
\[
\frac Bu=T_j:=\frac{\sqrt{j(j+1)}}{1+\sqrt j+\sqrt{j+1}}.
\]
The sequence \(T_j\) strictly increases, since \(T_j^{-1}=j^{-1/2}+(j+1)^{-1/2}+(j(j+1))^{-1/2}\) strictly decreases. Also \(R_{j+1}<R_j\) precisely when \(B/u>T_j\). For target \(k=1\), choose \(0<B/u<T_1\); for \(1<k<n\), choose \(T_{k-1}<B/u<T_k\); and for \(k=n\), choose \(B/u>T_{n-1}\). The values \(R_j\) then strictly decrease up to \(j=k\) and strictly increase afterward, so \(K=\{k\}\).

The strict inequalities persist after replacing the auxiliary middle zeros by sufficiently small positive rational entries. Choose rational \(u,B\) within the specified open intervals, choose positive rational middle entries small enough, and multiply \(u\), \(B\), and the middle entries by a common positive integer to obtain integer parameters \(b_1=1+u\), \(b_i>0\) for all \(i\). Because all quantities \(U_j-j\) scale by this common factor, the unique active cardinality remains \(k\). This completes the construction.

For a small explicit interior example, \(n=3\) and \(\mathbf b=(100,3,50)\) have
\[
R_1=76,\qquad R_2=\frac{254}{2+\sqrt2},\qquad R_3=\frac{353}{3+\sqrt3},
\]
and \(K(\mathbf b)=\{2\}\).

## Verification
The standalone file `verify_b_parking_inball.py` uses only Python's standard library. It checks the exact integer vertex supports and 60-digit Decimal inequality slacks for a finite parameter grid; it also constructs explicit integer parameters realizing every single contact size in dimensions two through twelve. The verifier reports: 360 parameter grids, 120 full vertex-support checks, 5,892 enumerated vertices, 98,616 subset-support evaluations, and 77 distinct size-realization tests. These checks are corroboration, **not** a proof for arbitrary dimension; the four analytic steps above establish the theorem.

## Relationship to prior work
Hanada, Lentfer, and Vindas-Meléndez introduced the parking-function polytope framework and developed its two-parameter specialization. Bayer and collaborators subsequently supplied the complete arbitrary-parameter facet theorem and studied generalized permutahedra, polymatroids, and combinatorial/circuit diameters. The present result concerns the standard-Euclidean inscribed ball and its complete facet-contact phases, not graph/circuit distance or enumeration. In the two-parameter specialization the minimizing upper cardinalities lie at endpoints; arbitrary parameters permit any intermediate contact size, a genuinely different geometric behavior.

## Limitations
This is an exact standard-Euclidean classification for \(n\ge2\) and positive integral parameters; no independent verification or universal priority determination is claimed. The proof uses the published polyhedral halfspace theorem as a premise. Very near contact-phase boundaries, floating-point calculations may misclassify ties; exact symbolic comparison of the explicitly stated radicals determines the true active set. The limiting auxiliary vectors in step 4 have zero entries but **are not** claimed to be admissible parking parameters; the proof perturbs them into strictly positive integral vectors.

## References
1. M. Hanada, J. Lentfer, and A. R. Vindas-Meléndez, *Generalized parking function polytopes*, arXiv:2212.06885, first posted 13 December 2022; https://arxiv.org/abs/2212.06885.
2. M. M. Bayer, S. Borgwardt, T. Chambers, S. Daugherty, A. Dawkins, D. Deligeorgaki, H.-C. Liao, T. McAllister, A. Morrison, G. Nelson, and A. R. Vindas-Meléndez, *Combinatorics of generalized parking-function polytopes*, arXiv:2403.07387, first posted 12 March 2024, Theorem 2.3(c); https://arxiv.org/html/2403.07387v1.
