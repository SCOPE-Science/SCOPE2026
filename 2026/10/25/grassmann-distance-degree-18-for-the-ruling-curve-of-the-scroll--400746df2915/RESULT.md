# Grassmann distance degree \(18\) for the ruling curve of the scroll \(S(2,3)\)

## Finding

Let \(\mathcal S\subset\operatorname{pGr}(2,7)\) be the curve of lines ruling the rational normal scroll \(S(2,3)\subset\mathbb P^6_\mathbb C\), with the standard symmetric-bilinear projection embedding. For a general rank-two symmetric idempotent data matrix \(Q\in\operatorname{pGr}(2,7)\), the chordal-distance objective on \(\mathcal S\) has exactly **18 distinct complex critical points away from the algebraic cut locus**. Thus

\[
\operatorname{GDdeg}(\mathcal S)=18=\operatorname{EDdeg}(\mathcal S).
\]

The equality is specific to this curve. In general, restricting the data matrix from the entire vector space of symmetric matrices to the rank-two projection Grassmannian can strictly reduce the critical-point count.

## Assumptions and scope

Work over \(\mathbb C\), with matrix transpose rather than conjugate transpose when complexifying. Let

\[
v_1(t)=(1,t,t^2),\qquad v_2(t)=(1,t,t^2,t^3)
\]

occupy disjoint coordinate blocks of dimensions \(3\) and \(4\), respectively. The line of the scroll indexed by \(t\in\mathbb P^1\) is the two-dimensional vector subspace spanned by these vectors. In the affine chart in which \(s_1(t)s_2(t)\ne0\), its symmetric projection matrix is

\[
P(t)=\operatorname{diag}\!\left(\frac{v_1(t)^\top v_1(t)}{s_1(t)},\frac{v_2(t)^\top v_2(t)}{s_2(t)}\right),
\quad s_1(t)=1+t^2+t^4,\quad s_2(t)=1+t^2+t^4+t^6.
\]

Here \(\operatorname{pGr}(2,7)=\{Q=Q^\top:Q^2=Q,\operatorname{tr}Q=2\}\). The objective is \(\operatorname{tr}(P(t)Q)\), equivalent to minimizing squared Frobenius/chordal distance because \(\|P-Q\|_F^2=4-2\operatorname{tr}(PQ)\). The Grassmann distance (GD) degree counts generic complex critical points on the smooth curve excluding the algebraic cut locus \(\operatorname{cut}(Q)=\{P:\operatorname{rank}(QP)<2\}\), in the sense of Friedman--Hoşten--Rosana, Definition 4.2.

The model is smooth: its Plücker coordinates include all monomials of degrees \(0,\ldots,5\) in the ruling parameter, yielding a rational normal quintic in its Plücker span. The projection chart deletes finitely many parameter values at which one of the \(s_i\) vanishes.

## Proof

**1. Universal critical-point bound.** For any symmetric data matrix \(Q\), let \(Q_1,Q_2\) be its two diagonal blocks. Then

\[
F_Q(t)=\operatorname{tr}(P(t)Q)=\frac{f_1(t)}{s_1(t)}+\frac{f_2(t)}{s_2(t)},
\qquad f_i(t)=v_i(t)Q_i v_i(t)^\top,
\]

with \(\deg f_1\le4\) and \(\deg f_2\le6\). A Euclidean-algorithm calculation gives \(\gcd(s_1,s_2)=1\). Hence the common denominator \(L=s_1s_2\) has degree \(10\), and \(F_Q=G_Q/L\) with \(\deg G_Q\le10\). The derivative numerator

\[
H_Q(t)=G_Q'(t)L(t)-G_Q(t)L'(t)
\]

has degree at most \(18\), because its potentially degree-\(19\) leading terms cancel. Thus every data matrix for which this derivative is not identically zero has at most \(18\) distinct finite critical points off the poles. We next give a genuine projection data matrix realizing all \(18\), simply and away from the cut locus.

**2. Rank-two projection witness.** Put \(a=(1,2,3)^\top\) and \(b=(1,2,3,4)^\top\), and take

\[
Q_0=\operatorname{diag}\!\left(\frac{aa^\top}{14},\frac{bb^\top}{30}\right).
\]

Since \(a^\top a=14\) and \(b^\top b=30\), the two blocks are rank-one symmetric idempotents on orthogonal coordinate subspaces. Consequently \(Q_0^2=Q_0\), \(Q_0^\top=Q_0\), and \(\operatorname{tr}Q_0=2\); in particular, this is a valid real (and complex) data point of \(\operatorname{pGr}(2,7)\), not an unrestricted symmetric matrix. Define

\[
p_1(t)=1+2t+3t^2,\qquad p_2(t)=1+2t+3t^2+4t^3.
\]

Then

\[
F_{Q_0}(t)=\frac{p_1(t)^2}{14s_1(t)}+\frac{p_2(t)^2}{30s_2(t)},\quad
G(t)=\frac{p_1(t)^2s_2(t)}{14}+\frac{p_2(t)^2s_1(t)}{30}.
\]

Exact polynomial arithmetic yields \(\deg H=18\), leading coefficient \(-58/35\), and the following identities in \(\mathbb Q[t]\):

\[
\gcd(G,L)=1,\qquad \gcd(H,L)=1,\qquad
\gcd(H,H')=1,\qquad \gcd(H,p_1p_2)=1.
\]

The accompanying self-contained standard-library Python program computes the complete polynomial \(105H\) and verifies all four identities by exact Euclidean division; these are rational identities, not floating-point tests. It also checks the nonzero leading coefficient. Consequently, \(H\) has exactly \(18\) distinct complex roots, none lying at the poles of \(P(t)\). As \(\deg H=18\), the parameter \(t=\infty\) is not a critical point either: in local coordinate \(u=1/t\), the first derivative of \(F_{Q_0}\) at \(u=0\) is nonzero.

**3. Exclusion of the algebraic cut locus.** Because both matrices are block diagonal and each block of \(P(t)\) has rank one, \(\operatorname{rank}(Q_0P(t))=2\) precisely when \(p_1(t)p_2(t)\ne0\), provided \(s_1(t)s_2(t)\ne0\). The verified \(\gcd(H,p_1p_2)=1\) places all 18 critical points outside \(\operatorname{cut}(Q_0)\), as required by the *GD* definition. This distinction is essential: the ordinary ED derivative count alone would not establish GD degree.

**4. Passage to general projection data.** The degree-\(18\) leading coefficient, the squarefree condition for \(H_Q\), and the absence of critical points at poles or in the cut locus are each nonvanishing conditions on polynomial expressions in the entries of \(Q\), after clearing the fixed denominators. For the cut-locus condition, use the polynomial \(\det(A(t)Q A(t)^\top)\), where the two rows of \(A(t)\) are \(v_1,v_2\) in their respective blocks. Indeed, for any rank-two symmetric projection \(Q=BB^\top\) with \(B^\top B=I_2\), one has \(\det(AQA^\top)=\det(AB)^2\), and rank \(AB\) is the rank of \(P(t)Q\) on this chart. Thus this determinant vanishes exactly at the cut locus. The witness proves that all these conditions hold simultaneously on a nonempty Zariski-open subset of the rank-two projection Grassmannian. This Grassmannian is irreducible, being the nondegenerate-subspace open locus of \(\operatorname{Gr}(2,7)\). Hence a general \(Q\) has precisely \(18\) distinct finite critical points outside the cut locus. This proves the displayed GD degree.

## Verification

The file `verify_gd_scroll.py` uses only Python's standard library. Run `python3 verify_gd_scroll.py` from the same directory. It constructs \(L,G,H\) with exact rational coefficients, checks the coefficient list of \(105H\), and verifies \(\gcd(L,G)=\gcd(L,H)=\gcd(H,H')=\gcd(H,p_1p_2)=1\). Its success message is `VERIFY_OK`. All the required geometric conclusions are justified in the proof above; the program certifies the explicit nontrivial polynomial identities and does not substitute numerical sampling for the genericity argument.

## Relationship to prior work

Friedman, Hoşten, and Rosana (arXiv:2610.02018, first publicly posted 2026-10-01), Example 2.1 and Theorem 2.2, introduce this family of ruling curves and compute their **ED** degree. For \(S(2,3)\), their formula gives \(2\deg\operatorname{lcm}(s_1,s_2)-2=18\). Their Definition 4.2 imposes the stronger restriction that the generic data point lie on the projection Grassmannian, and their Theorem 4.4 describes equality of ED and GD degrees as expected in low-dimensional settings rather than giving a GD computation for scroll ruling curves. The present result verifies equality for a canonical first asymmetric scroll by exhibiting admissible rank-two projection data with all 18 critical points outside the cut locus.

Friedman, Rosana, and Sturmfels (arXiv:2601.22843, 2026-01-30) introduce the GD framework for lines and analyze other families. The exact \(S(2,3)\) ruling-curve count is not present in the material inspected. A reported result on line-distortion scrolls treats flat limits and degrees of scroll surfaces; it does not count critical points of projection-matrix distance on their ruling curves.

## Limitations

The claim is confined to the ruling curve of \(S(2,3)\) and to the algebraic chordal/projection-matrix metric. It does not classify GD degrees of all rational normal scrolls, nor count critical points of intrinsic geodesic distance. The proof gives the **generic complex** count; it does not say that all 18 critical points are real for generic real data. Literature searches cannot certify absolute novelty; implicit coverage in unindexed sources is a residual risk. No independent validation has been performed.

## References

1. H. Friedman, S. Hoşten and A. Rosana, *Euclidean Distance Optimization Within the Grassmannian*, arXiv:2610.02018 (first submission October 1, 2026), especially Example 2.1, Theorem 2.2, Definition 4.2 and Theorem 4.4. https://arxiv.org/html/2610.02018v2
2. H. Friedman, A. Rosana and B. Sturmfels, *Distance Optimization in the Grassmannian of Lines*, arXiv:2601.22843 (January 30, 2026), especially the introduction and GD definition. https://arxiv.org/pdf/2601.22843
