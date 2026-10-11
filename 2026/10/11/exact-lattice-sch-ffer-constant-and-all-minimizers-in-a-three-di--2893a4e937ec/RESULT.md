# Exact lattice Schäffer constant and all minimizers in a three-dimensional separating example

## Finding
Let \(X=\mathbb R^3\), with the coordinatewise lattice order and the absolute norm
\[
N(x,y,z)=\max\left\{|x|+\frac{|z|}{2},\ |y|+\frac{|z|}{2},\ \frac{2|x|+2|y|+|z|}{3},\ \frac{5(|x|+|y|)}{6}\right\}.
\]
The lattice Schäffer constant and the complete set of its minimizing pairs are
\[
\lambda^+(X)=\inf_{\substack{u,v\in X_+\\N(u)=N(v)=1}}
\max\{N(u+v),N(u-v)\}=\frac43,
\]
where every minimizing ordered pair, up to swapping \(u\) and \(v\), has the form
\[
u=(a,0,2(1-a)),\qquad v=(0,b,2(1-b)),\qquad a\ge\frac23,\quad b\ge\frac23,\quad a+b\le\frac85.
\]
The parameter domain is the filled triangle with vertices
\((2/3,2/3)\), \((14/15,2/3)\), \((2/3,14/15)\).
For the published disjoint companion invariant \(\beta(X)=15/11\), the sharp quantitative separation is
\[\beta(X)-\lambda^+(X)=\frac1{33},\qquad \frac{\beta(X)}{\lambda^+(X)}=\frac{45}{44}.\]

## Assumptions and scope
Scalars are real. Positivity means coordinatewise nonnegativity. The two vectors are independently normalized to norm one; no disjointness condition is imposed in \(\lambda^+\). The stated equality-case classification is exhaustive in this specified three-dimensional normed lattice. No assertion is made that the displayed separation is maximal among all Banach lattices.

## Proof
For \(w=(x,y,z)\ge0\), denote the four positive linear norm facets by
\[
f_1(w)=x+z/2,\quad f_2(w)=y+z/2,\quad f_3(w)=(2x+2y+z)/3,\quad f_4(w)=5(x+y)/6.
\]
Then \(N(w)=\max_i f_i(w)\). The coefficientwise inequalities
\[
f_3\ge\frac23 f_1,\qquad f_3\ge\frac23 f_2,\qquad f_3\ge\frac23 f_3,\qquad f_3\ge\frac23 f_4\]
hold on the entire positive cone. In particular
\[f_3(w)\ge\frac23N(w)\quad(w\ge0).\]
As \(u,v\ge0\), the lattice absolute-value inequality gives \(N(u-v)\le N(u+v)\). Therefore, for \(N(u)=N(v)=1\),
\[
N(u+v)\ge f_3(u+v)=f_3(u)+f_3(v)\ge\frac43.
\]
For \(u=(4/5,0,2/5)\) and \(v=(0,4/5,2/5)\), direct substitution gives \(N(u)=N(v)=1\) and \(N(u+v)=4/3\). Thus the constant is exactly \(4/3\).

We now classify **all** minimizing pairs. Equality in the displayed lower bound forces
\(f_3(u)=f_3(v)=2/3\). For every nonzero positive \(w\), the coefficientwise comparisons with \(f_3\) and \(f_4\) are strict after multiplication by \(2/3\), whereas
\[
f_3-\frac23f_1=\frac23 y,\qquad f_3-\frac23f_2=\frac23x.
\]
Consequently, \(N(w)=1\) and \(f_3(w)=2/3\) imply one of exactly two types:
\[
w=(a,0,2(1-a))\quad\text{or}\quad w=(0,a,2(1-a)),\qquad 0\le a\le1.
\]
Each such vector is indeed a positive unit vector with \(f_3(w)=2/3\). If both \(u,v\) are represented on the same type of face, then that face's functional evaluates to \(2\) on \(u+v\), so they cannot minimize. Thus, after possibly interchanging them, write
\[
u=(a,0,2(1-a)),\qquad v=(0,b,2(1-b)),\qquad 0\le a,b\le1.
\]
For their sum, direct exact calculation gives
\[
f_1(u+v)=2-b,\quad f_2(u+v)=2-a,\quad f_3(u+v)=\frac43,\quad f_4(u+v)=\frac56(a+b).
\]
Hence \(N(u+v)=4/3\) holds if and only if \(a\ge2/3\), \(b\ge2/3\), and \(a+b\le8/5\). These inequalities already imply \(a,b\le14/15<1\); this proves necessity, sufficiency and the exact triangular equality domain.

Finally, the previously established value \(\beta(X)=15/11\) yields the exact gap and ratio by subtraction and division, without recomputing the disjoint extremal problem.

## Verification
The standalone file `verify_lattice.py` uses only Python's standard-library rational arithmetic. Run `python3 verify_lattice.py`. It exactly checks the four coefficientwise facet dominations, strictness of the other two faces, the three vertices of the triangular minimizer set, the original example's pair, and the gap arithmetic. The printed success token is `LATTICE_SCHAFFER_EXACT_DOMINANCE_AND_EXTREMAL_TRIANGLE_OK`. The universal quantifiers and the exhaustive equality classification are proved analytically above; these finite rational checks are auxiliary, not substitutes.

## Relationship to prior work
Rincón-Villamizar and Oikhberg introduced the norm used here in Example 3.5 of their lattice Schäffer paper [1]. They established \(\beta(X)=15/11\) and exhibited one pair proving \(\lambda^+(X)\le4/3\), sufficient for a strict separation. The missing reverse inequality for the specific example and the entire minimizing triangle are provided here. Their general results on lattice Schäffer constants, positive lattice geometry and monotonicity do not specify these equality cases or the exact number for this example. This result does not claim to introduce the norm, the invariant, the strict-separation phenomenon, or the original upper-bound pair.

## Limitations
The explicit norm and coordinatewise lattice order are essential. This result does not determine extremizers for arbitrary three-dimensional Banach lattices, nor the maximal possible gap between the two invariants. It is an exact evaluation and equality classification for the natural published benchmark, not a global sharpness theorem. Independent external validation has not been conducted.

## References
[1] M. A. Rincón-Villamizar and T. Oikhberg, *The lattice Schäffer constant*, arXiv:2505.16775v1 (first posted 2025-05-22), especially Example 3.5 and Remark 3.7. https://arxiv.org/abs/2505.16775
