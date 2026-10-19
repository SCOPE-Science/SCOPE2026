# Sharp admissible ellipse and square-root obstruction frequency for tetrahedral longest-edge bisection

## Finding

Let a labeled tetrahedron be specified by its six squared edge lengths in the order \((01,02,03,12,13,23)\). Consider the affine family
\[
D(x,y)=(23+4x+4y,\ 3+x,\ 3+y,\ 20,\ 20,\ 10),
\qquad Q(x,y)=4x^2+6xy+4y^2.
\]
Use the marked three-bisection word \(W=(0\leftarrow1)(1\leftarrow2)(3\leftarrow1)\), with the final relabeling \(\sigma=(1\,2\,3)\), from Adiprasito--Kalmanovich--Solomon [1]. A bisection \((i\leftarrow j)\) replaces vertex \(i\) by the midpoint of the edge \(ij\). A bisection is *admissible* when the edge being bisected is among the longest edges; ties are permitted.

Put \(q_c=63/32\). The following is sharp for this fixed affine family and marked word.

1. For every \(q\in[0,q_c]\), every point of the closed ellipse \(Q(x,y)=q\) represents a nondegenerate tetrahedron and permits indefinite repetition of the three-step word. Every marked phase remains in a compact nondegenerate part of shape space. For \(q>0\), every such branch has infinitely many unlabeled similarity classes.
2. For every \(q>q_c\) and every starting parameter satisfying \(Q(x,y)=q\), indefinite repetition of this word cannot be an admissible longest-edge-bisection branch. This is a statement about this word, not all possible bisection choices.
3. For \(q\in[0,2]\), all formal marked iterates are nondegenerate tetrahedra, and their second and third bisections are legal. The limiting frequency of formal blocks in which the **first** prescribed bisection is illegal is, for every starting parameter on \(Q=q>0\),
\[
\Phi(q)=
\begin{cases}
0,&0<q\le q_c,\\[2pt]
\displaystyle\frac1\pi\arccos\sqrt{\frac{q_c}{q}},&q_c<q\le2.
\end{cases}
\]
These are formal returns after the first violation, not a claim that an invalid bisection remains a valid longest-edge algorithm. In particular, the onset is
\[
\Phi(q)=\frac{1}{\pi\sqrt{q_c}}\sqrt{q-q_c}+O((q-q_c)^{3/2})
\qquad(q\downarrow q_c,\ q>q_c).
\]
At \(q=q_c\), the first-step longest-edge comparison becomes an equality only at \((x,y)=(-3/8,-3/8)\). As an additional sharp shape-quality consequence, the normalized volume at every *marked block boundary* throughout the disk \(Q\le q_c\) satisfies
\[
\frac{\operatorname{vol}_3(\Delta)}{\operatorname{diam}(\Delta)^3}
\ge \frac{\sqrt{995/128}}{6\,26^{3/2}},
\]
with equality at the parameter \((3/8,3/8)\). The bound is not asserted to be sharp across the two intermediate bisection phases.

## Assumptions and scope

The phase space is the cone of Euclidean nondegenerate labeled tetrahedra modulo positive similarity. The return uses the **specified** directed bisections and relabeling, allowing any longest-edge tie. In particular this word is not required to follow the opposite-edge tie-breaking rule of [1]. The parameter \(q\) is the exact quadratic level \(Q(x,y)\), and the formal marked evolution is
\[
\binom{x_{n+1}}{y_{n+1}}=U\binom{x_n}{y_n},
\quad U=\begin{pmatrix}-3/2&-1\\1&0\end{pmatrix}.
\]
The formula for \(\Phi\) is restricted to \(q\le2\) to ensure the formal iterates are genuine nondegenerate tetrahedra with no further bisection obstruction. At \(q=0\) the central parameter is fixed, rather than quasiperiodic. Nothing is asserted about alternate admissible branches after the prescribed word ceases to be legal.

## Proof

**Invariant return.** For the edge-coordinate bisection and permutation matrices of [1, Section 4.2], direct multiplication gives
\[
M_WD(x,y)=\tfrac14 D(-\tfrac32 x-y,x)=\tfrac14D(U(x,y)).
\]
The identity is reproduced by exact rational matrix multiplication in the accompanying checker. With
\[
S=\begin{pmatrix}4&3\\3&4\end{pmatrix},
\qquad Q(u)=u^{\mathsf T}Su,
\]
one has \(U^{\mathsf T}SU=S\). The matrix \(U\) has eigenvalues \((-3\pm i\sqrt7)/4\), which are unimodular and not roots of unity: otherwise their sum \(-3/2\) would be a rational algebraic integer, which it is not. Thus on each \(Q=q>0\), the return is conjugate to an irrational circle rotation; all orbits are dense and equidistributed.

**Geometric domain.** For the Gram matrix \(G(x,y)\) reconstructed from \(D(x,y)\), direct calculation yields the leading principal minors
\[
m_1=23+4(x+y),\qquad 4m_2=240+80x-(3x+4y)^2,
\qquad m_3=25-\tfrac{35}{4}Q(x,y).
\]
For \(0\le Q\le2\), the inverse quadratic-form estimates give \(|x|,|y|\le\sqrt{8/7}<2\), \(|x+y|\le\sqrt{4/7}<1\), and \((3x+4y)^2\le4Q\le8\). Hence \(m_1>19\), \(4m_2>72\), and \(m_3\ge15/2>0\). By Sylvester's criterion, every such point is a genuine nondegenerate tetrahedron.

**The complete three-stage test.** The squared edge vectors just before the second and third bisections are, respectively,
\[
D^{(1)}(x,y)=\left(\tfrac{23}{4}+x+y,\ \tfrac{23}{4}-\tfrac x2-y,\ \tfrac{23}{4}-x-\tfrac y2,\ 20,20,10\right),
\]
\[
D^{(2)}(x,y)=\left(\tfrac34+\tfrac x4,\ \tfrac{23}{4}-\tfrac x2-y,\ \tfrac{23}{4}-x-\tfrac y2,\ 5,10,10\right).
\]
The bounds above show that, throughout \(Q\le2\), the second selected edge \(12\) is a longest edge (tied with \(13\) at squared length \(20\)), and the third selected edge \(13\) is a longest edge (tied with \(23\) at squared length \(10\)). At the first stage, the only potentially longer competitors to edge \(01\) are edges \(12\) and \(13\), both of squared length \(20\). Consequently the whole block is admissible exactly when
\[
23+4(x+y)\ge20\quad\Longleftrightarrow\quad x+y\ge-\tfrac34.
\]
Indeed, \(Q=\frac72(x+y)^2+\frac12(x-y)^2\). On \(Q=q\), the range of \(x+y\) is exactly \([ -\sqrt{2q/7},\sqrt{2q/7}]\). The inequality therefore holds on the whole ellipse exactly when \(q\le(7/2)(3/4)^2=q_c\). At equality the unique contact is \((-3/8,-3/8)\). At and below this value, compactness and preservation of the nondegenerate cone under each vertex midpoint operation give an infinite admissible branch. Its marked parameters are distinct for positive \(q\) by irrationality; projective proportionality of two vectors \(D(u)\) forces proportionality factor one because their fourth and fifth entries are both \(20\), hence forces equal parameters. A finite vertex-permutation group cannot identify infinitely many distinct labeled classes, so there are infinitely many unlabeled classes.

For \(q>q_c\), the open arc \(x+y<-3/4\) is nonempty on \(Q=q\). Every positive-level formal orbit visits it by density. If the selected word were admissible forever, the return identity would hold along the actual bisection orbit; the first bisection would eventually fail the necessary longest-edge comparison. Thus no such infinite admissible branch exists.

**Frequency and square-root onset.** For \(0<q\le2\), the failure indicator is precisely \(\mathbf1_{\{x+y<-3/4\}}\), whose only circle-boundary points have zero angular measure. On the ellipse, the observable \(x+y\) is a sinusoid of amplitude \(A=\sqrt{2q/7}\) under the circle conjugacy. Unique ergodicity of irrational rotation gives failure frequency zero for \(A\le3/4\); for \(A>3/4\), the forbidden angular interval has length \(2\arccos((3/4)/A)\). Dividing by \(2\pi\) gives \(\Phi(q)\) above. Expanding \(\arccos\sqrt{q_c/q}\) as \(q\downarrow q_c\) yields the stated square-root coefficient. Finally, \(\det G\ge995/128\) and, at marked boundaries, \(\operatorname{diam}^2=23+4(x+y)\le26\) throughout \(Q\le q_c\). Since \(\operatorname{vol}_3=\sqrt{\det G}/6\), the sharp marked-boundary shape-quality inequality follows, with equality at \((3/8,3/8)\).

## Verification

The bundled `verify_elliptic.py` uses exact rational symbolic arithmetic to check the quadratic conjugacy, six-edge return identity, two intermediate edge vectors, Gram principal minors and determinant, the critical contact, and the maximizing dual quadratic norm. It also runs a finite, independent rotation sampling diagnostic at four quadratic levels; the empirical failure fractions agree with the closed formula within the explicitly tested tolerance. Run with `python verify_elliptic.py` using Python 3 and SymPy. The inequalities, infinite-orbit existence, impossibility above threshold, and limit frequency are proved analytically above; sampled orbits are not used as infinite proofs.

## Relationship to prior work

Adiprasito--Kalmanovich--Solomon [1, Section 4.2] introduced this precise three-step word, return matrix and elliptic family, then verified admissibility only on the small sample ellipse \(Q=1/16\), explicitly choosing that level to ensure geometric and edge-order constraints. Their Section 4.3 constructs a distinct length-nine strictly tie-free word. Neither gives the maximal admissible level of this fixed length-three word or the frequency of illegal formal blocks beyond it. The current result turns the existence construction into a sharp entire-family cutoff and quantifies its square-root admissibility failure. Michaud--Korotov [2, Sections 3.2--3.4] treat finite similarity-class orbits and exploratory shape evolution under a different normalization, not this irrational three-block ellipse or its sharp cutoff. Trujillo--Suárez--Moreno-García [3] prove convexity of general sextuple bisection-pattern regions and finite-state refinement descriptions for other tetrahedral families, but do not analyze the present irrational elliptic word, its entire-orbit threshold, or the forbidden-block frequency. Generic irrational-rotation equidistribution alone supplies a frequency only **after** the new exact geometric legality threshold has been determined.

## Limitations

This result is about the *specific* affine plane and marked word of [1], with arbitrary longest-edge ties. It does not classify all longest-edge-bisection branches or the tie-free length-nine word, and does not establish global nondegeneration for all tetrahedra. Formal returns after an invalid choice are only an algebraic diagnostic. The square-root formula for forbidden-block frequency is given through \(q\le2\); for larger levels the formal affine family need not remain entirely in the physical tetrahedral cone. An equivalent cutoff hidden in other bisection analyses remains a bibliographic priority risk; no independent expert audit has been performed.

## References

[1] K. A. Adiprasito, D. Kalmanovich, Y. Solomon, *Degenerating orbits of the Longest Edge Bisection process*, arXiv:2609.08846v1 (first publicly submitted 2026-09-08), Section 4.2, especially Lemmas 4.1--4.4 and Theorem 4.5; https://arxiv.org/html/2609.08846v1 . Primary MSC2020: 37N30.

[2] J. Michaud, S. Korotov, *On the Orbits of Similarity Classes of Tetrahedra Generated by the Longest-Edge Bisection Algorithm*, arXiv:2512.07315v1 (2025-12-08), Sections 3.2--3.4; https://arxiv.org/html/2512.07315v1 .

[3] A. Trujillo, J. P. Suárez, T. Moreno-García, *Multiform Longest Edge Bisection of Tetrahedra via Sextuple Permutations*, arXiv:2609.26522v1 (2026-09-22), Sections 4--5; https://arxiv.org/abs/2609.26522 .
