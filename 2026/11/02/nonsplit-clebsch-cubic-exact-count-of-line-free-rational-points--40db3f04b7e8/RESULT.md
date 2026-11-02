# Nonsplit Clebsch cubic: exact count of line-free rational points

## Finding

Let \(q\) be an odd prime power with characteristic \(p\ge7\) and \(q\equiv2\) or \(3\pmod5\). On the Clebsch diagonal cubic
\[
S:\quad\sum_{i=0}^{4}X_i=0,\qquad\sum_{i=0}^{4}X_i^3=0\quad\subset\mathbb P^4_{\mathbb F_q},
\]
let \(U\) denote the **reduced union of all 27 geometric lines**, including lines not individually defined over \(\mathbb F_q\). Then
\[
\#S(\mathbb F_q)=q^2+5q+1,\qquad
\#U(\mathbb F_q)=15q-20,
\]
and hence
\[
\boxed{\#(S\setminus U)(\mathbb F_q)=(q-3)(q-7).}
\]
The 27 lines consist of fifteen rational lines and six pairs of nonrational, mutually skew Frobenius conjugates. Consequently, for \(q=7\) all \(85\) rational points lie on the fifteen rational lines; for every other admissible \(q\) the line-free locus has rational points. For instance it has \(60\) points over \(\mathbb F_{13}\).

## Assumptions and scope

Here \(\mathbb F_q\) may be a non-prime finite field, provided \(p\ge7\) and \(q\equiv\pm2\pmod5\). A geometric line means a line on \(S\otimes\overline{\mathbb F}_q\). The count excludes points on **any** geometric line, not merely on the fifteen rational ones. Neither characteristic \(2\), characteristic \(3\), nor characteristic \(5\) is claimed; distinctness of the classical 27 lines and the smoothness argument below are established in the stated range.

## Proof

**1. Smoothness and the 27 explicit geometric lines.** On the hyperplane \(\sum X_i=0\), a singular point of the cubic would satisfy \(X_0^2=\cdots=X_4^2\). In characteristic different from \(2,3,5\), nonzero coordinates then have the form \(\pm a\); the sum of five signs is one of \(\pm1,\pm3,\pm5\), none divisible by \(p\ge7\). Thus \(S\) is smooth. By the classical line configuration on a smooth cubic surface, it has 27 geometric lines. Fifteen are the coordinate-pairing lines
\[
L_{s;ab|cd}: X_s=0,\quad X_a+X_b=0,\quad X_c+X_d=0,
\]
where \(s\) is one index and \(\{\{a,b\},\{c,d\}\}\) is an unordered perfect matching of the other four indices. All fifteen are defined over \(\mathbb F_q\).

For a primitive fifth root \(\zeta\), define Fourier vectors \(f_j=(\zeta^{0j},\zeta^{1j},\ldots,\zeta^{4j})\). The other twelve lines are the coordinate-permutation orbit of \(\mathbb P\langle f_1,f_4\rangle\). These are contained in \(S\), and together with the fifteen coordinate lines they give 27 distinct lines. Distinctness holds for all \(p\ge7\): the five Fourier vectors form a Vandermonde basis (their determinant is nonzero for distinct fifth roots), and these line equations give the classical configuration in that characteristic. This identification is also directly checkable from the equations.

**2. Nonsplit lines have no rational points.** As \(q\equiv\pm2\pmod5\), arithmetic Frobenius sends the pair of Fourier characters \(\{1,4\}\) to \(\{2,3\}\). On each orbit it exchanges \(\mathbb P\langle f_1,f_4\rangle\) and its conjugate \(\mathbb P\langle f_2,f_3\rangle\), up to a common permutation of coordinates. These lines are skew because \(f_1,f_2,f_3,f_4\) are linearly independent. Every nonrational line thus has a disjoint Frobenius conjugate. If an \(\mathbb F_q\)-point lay on such a line, it would also lie on its conjugate, a contradiction. The fifteen coordinate lines therefore contain **every** rational point of \(U\).

**3. Frobenius trace on the Picard group.** The rational Picard space of a smooth cubic surface has dimension seven with nondegenerate intersection form. Let \(G\) be the 15-by-15 Gram matrix of the fifteen rational line classes: diagonal entries are \(-1\); off-diagonal entries are one if lines meet and zero otherwise. The pairing-line equations give
\[
\det(tI-G)=t^9(t-5)(t+4)^5,
\]
so \(G\) has rank six over \(\mathbb Q\). Nondegeneracy of the seven-dimensional Picard form shows that the fifteen fixed classes span exactly a six-dimensional subspace (if they spanned dimension seven, their Gram matrix would have rank seven). The Frobenius action is nontrivial on Picard classes because it interchanges distinct exceptional curves among the other twelve. It acts with eigenvalues \(+1\) on the six-dimensional span and \(-1\) on the remaining one-dimensional orthogonal complement, hence has trace five. The standard Lefschetz/Weil point-count formula for a smooth geometrically rational projective surface now gives \(\#S(\mathbb F_q)=q^2+5q+1\).

**4. Exact union count.** Among the fifteen coordinate-pairing lines, the only nontrivial intersections are ten rational triple points represented by permutations of \((1,-1,0,0,0)\), and fifteen rational ordinary pairwise intersection points represented by permutations of \((0,1,-1,1,-1)\). More precisely, the ten points have exactly three of the fifteen lines through them, and the fifteen others exactly two. This follows by substituting the pairing-line equations and classifying their pairwise intersections; in the stated characteristics the two point types are distinct. Every rational line has \(q+1\) points. Correcting multiplicities yields
\[
\#U(\mathbb F_q)=15(q+1)-10(3-1)-15(2-1)=15q-20.
\]
Subtracting from the surface point count completes the proof. Since \(q\ge7\) and the only admissible \(q\le7\) is seven, the positivity statement follows.

## Verification

Run the included standalone standard-library program `verify_clebsch_nonsplit.py` with Python 3. It checks the exact fifteen-line intersection multiplicities and rational Picard Gram rank, enumerates all projective points in \(\mathbb F_p\) for primes \(p=7,11,13,17,19\), and checks the twelve Fourier-orbit lines in the split control field \(\mathbb F_{11}\). For nonsplit primes \(7,13,17\), all directly enumerated point counts agree with the formula. The program does **not** replace the arguments for arbitrary prime powers: the latter are proved by Frobenius descent and the Picard trace in Steps 2–3.

## Relationship to prior work

The Clebsch cubic and its 27 lines, including the fifteen coordinate-pairing lines and the twelve Fourier lines, are classical; see the cited geometric account. The Weil formula relating point counts to Frobenius trace is standard and appears in Knecht's treatment of del Pezzo surfaces. Hirschfeld's older finite-geometric account discusses cubic surfaces with **all 27 lines rational** and the exceptional case where all points lie on lines. That split assumption does not hold in the present \(q\equiv\pm2\pmod5\) case. The claim here is the exact **nonsplit** line-free-point formula, obtained by combining the quadratic Galois descent, the six-dimensional fixed line span, and the fifteen-line intersection arrangement. It is not a new formula for an arbitrary cubic surface or a new classification of 27 lines.

## Limitations

This is a same-source-style exact calculation on a classical surface, not an assertion of priority over every historic finite-geometry table. Hirschfeld's 1967 and 1981 original treatments were not both available in full during the literature comparison, and an equivalent older tabulation remains a historical-priority risk. The formula is proved only for odd \(q\) of characteristic at least seven satisfying the nonsplit congruence; characteristic two, three and five, and the split residue classes, are outside the claimed domain. 

## References

- J. W. P. Hirschfeld, *Cubic surfaces whose points all lie on their 27 lines*, in *Finite Geometries and Designs* (1981), pp. 169–171; publisher online release 2013-04-05, DOI: 10.1017/CBO9781107325579.020. The accessible account treats split 27-line configurations.
- A. Knecht, *Degree of Unirationality for del Pezzo Surfaces over Finite Fields*, arXiv:1307.3215v1 (first public 2013-07-11); later *J. Théor. Nombres Bordeaux* **27** (2015), 171–182. In particular see the Picard Frobenius point-count formula.
- J. Baez, *27 Lines on a Cubic Surface*, AMS Visual Insight, 2016-02-15, https://blogs.ams.org/visualinsight/2016/02/15/27-lines-on-a-cubic-surface/ (explicit classical Fourier and pairing description).
- A. Betten, J. W. P. Hirschfeld, F. Karaoglu, *Classification of cubic surfaces with twenty-seven lines over the finite field of order thirteen*, *European J. Math.*, first online 2017-09-27, DOI: 10.1007/s40879-017-0182-0 (split-case comparison).
