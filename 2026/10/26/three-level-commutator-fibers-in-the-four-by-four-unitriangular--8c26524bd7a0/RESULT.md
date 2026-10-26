# Three-level commutator fibers in the four-by-four unitriangular group

## Finding

For every prime power \(q\), let \(G=UT_4(\mathbb F_q)\) be the group of upper unitriangular \(4\times4\) matrices over \(\mathbb F_q\). Set \(t(u,v,w)=I+uE_{13}+vE_{24}+wE_{14}\), with \(u,v,w\in\mathbb F_q\). Under the convention \([g,h]=ghg^{-1}h^{-1}\), the number \(N_q(u,v,w)\) of ordered pairs satisfying \([g,h]=t(u,v,w)\) is exactly

\[
N_q(u,v,w)=\begin{cases}
q^7(q^2-1), &(u,v)\ne(0,0),\\
2q^7(q^2-1), &(u,v)=(0,0),\ w\ne0,\\
2q^7(q^2-1)+q^8, &(u,v,w)=(0,0,0).
\end{cases}
\]

The derived subgroup is \(G'=\{t(u,v,w):u,v,w\in\mathbb F_q\}\); targets outside it have no commutator representations. Thus every element of the derived subgroup is a *single* commutator, and the fiber distribution has three exact levels in every characteristic. The commuting probability and number of conjugacy classes are

\[
\operatorname{cp}(G)=\frac{2q^2+q-2}{q^5},\qquad k(G)=2q^3+q^2-2q.
\]

## Assumptions and scope

The field may be any finite field of order \(q\), with no restriction on characteristic. Tuples are ordered, and the matrices are group elements, not Lie-algebra elements. Write

\[
g=\begin{pmatrix}1&a&b&c\\0&1&d&e\\0&0&1&f\\0&0&0&1\end{pmatrix},\qquad
h=\begin{pmatrix}1&A&B&C\\0&1&D&E\\0&0&1&F\\0&0&0&1\end{pmatrix}.
\]

The cardinality of \(G\) is \(q^6\). The center is \(Z(G)=\{t(0,0,w):w\in\mathbb F_q\}\). As a subgroup \(G'\) consists precisely of matrices whose first superdiagonal is zero, hence has cardinality \(q^3\).

## Proof

**Matrix identity.** The product formula gives

\[
(gh-hg)_{13}=aD-Ad=:u,\quad(gh-hg)_{24}=dF-Df=:v,\quad
(gh-hg)_{14}=aE+bF-Ae-Bf.
\]

Because \(gh=[g,h]\,hg\), and \(hg\) has \((3,4)\)-entry \(f+F\), comparing entries yields the complete group-commutator coordinates

\[
[g,h]=t(u,v,w),\qquad
w=aE+bF-Ae-Bf-(f+F)u.
\]

No entry \(c\) or \(C\) appears; these two variables contribute \(q^2\) free choices.

**Outer parameter count.** Hold fixed \((u,v)\), and count \((a,d,f,A,D,F)\) satisfying \(aD-Ad=u\), \(dF-Df=v\). If \((d,D)\ne(0,0)\), the first constraint cuts out one affine line in the two variables \((a,A)\), and the second one affine line in \((f,F)\), giving \(q^2\) choices for each of \(q^2-1\) nonzero pairs \((d,D)\). If \((d,D)=(0,0)\), the constraints force \(u=v=0\), leaving \(q^4\) free choices. Thus the number of outer sextuples is

\[
S(u,v)=q^2(q^2-1)+\mathbf1_{u=v=0}q^4.
\]

**Last-coordinate rank.** For any fixed outer sextuple, the equation specifying \(w\) is affine linear in \((b,e,B,E)\) with linear part \(Fb-Ae-fB+aE\). It is surjective precisely when \((a,A,f,F)\ne(0,0,0,0)\), in which case there are \(q^3\) choices for any prescribed \(w\). In the exceptional case \((a,A,f,F)=(0,0,0,0)\), necessarily \(u=v=0\), and the entire expression for \(w\) vanishes; there are \(q^2\) choices for \((d,D)\), each admitting all \(q^4\) choices for \((b,e,B,E)\) only at \(w=0\). Including \((c,C)\) gives

\[
N_q(u,v,w)=q^5\big(S(u,v)-q^2\mathbf1_{u=v=0}\big)+q^8\mathbf1_{u=v=w=0}.
\]

When \((u,v)\ne(0,0)\), the result is \(q^7(q^2-1)\). When \(u=v=0\), the first term is \(2q^7(q^2-1)\), and the \(q^8\) correction appears only at \(w=0\). All three fiber counts are strictly positive. Since basic transvections generate the second superdiagonal and the center by commutators, \(G'\) has the stated shape; the displayed positive counts independently prove it is the *image* of the single-commutator map.

**Consistency and conjugacy consequence.** There are \(q^3-q\) targets with \((u,v)\ne(0,0)\), \(q-1\) nonidentity central targets, and one identity. The sum of all three fiber strata is \(q^{12}=|G|^2\). The identity fiber is the number of commuting ordered pairs. Dividing it by \(|G|^2\) gives the commuting probability; multiplying that probability by \(|G|\) gives the number of conjugacy classes, since \(\sum_{g\in G}|C_G(g)|=|G|\,k(G)\).

## Verification

The included standalone Python program `verify.py` implements group multiplication and inversion directly from six matrix coordinates. It exhaustively enumerates all \(4,096\) pairs over \(\mathbb F_2\) and all \(531,441\) pairs over \(\mathbb F_3\), comparing the full target-by-target distribution against the theorem and asserting that every commutator lies in \(G'\). It separately enumerates the outer sextuples over the nonprime field \(\mathbb F_4\), using an explicit irreducible quadratic for field multiplication, and checks the predicted target counts. The observed successful termination marker is `VERIFY_OK_UT4_COMMUTATOR_FIBERS`.

The characteristic-free theorem follows from the symbolic field counting argument above, not from finite enumeration. The \(\mathbb F_4\) stage checks the outer-sextuple count rather than exhaustively calculating the group commutator via the group law.

## Relationship to prior work

Marberg's work on superclasses and supercharacters of unitriangular pattern groups (arXiv:1005.4151) supplies a much broader representation-theoretic setting, but its stated theorems classify superclasses and supercharacters rather than furnishing the precise fiber cardinalities of the two-input group-commutator word on \(UT_4(\mathbb F_q)\). Bardakov, Vesnin, and Yadav (arXiv:1109.4710) investigate class-preserving automorphisms and their quotients, including commutator identities, not the cardinalities of all commutator fibers. Hołubowski and Stepanov (arXiv:1505.06355) classify maps preserving commutators; the available abstract does not assert fiber distributions. The complete target-refined formula above is the contribution evaluated here; known commutator identities, the existence of character-theoretic Fourier expansions for word fibers, and superclass methods are not claimed as new.

## Limitations

The result concerns ordinary group commutators, not additive matrix commutators or products of multiple commutators. The exact formula is proved only for four-by-four unitriangular matrices; extending it to larger sizes could introduce additional fiber strata. Historical priority is subject to possible implicit formulas in earlier character tables, class-number computations, and inaccessible papers; a negative search result is not proof of uniqueness.

## References

- Eric Marberg, *Superclasses and supercharacters of normal pattern subgroups of the unipotent upper triangular matrix group*, arXiv:1005.4151, first publicly submitted 22 May 2010.
- Valeriy Bardakov, Andrei Vesnin, Manoj K. Yadav, *Class preserving automorphisms of unitriangular groups*, arXiv:1109.4710, first publicly submitted 22 September 2011.
- Waldemar Hołubowski and Alexei V. Stepanov, *Bijections preserving commutators and automorphisms of unitriangular group*, arXiv:1505.06355, first publicly submitted 23 May 2015; abstract available; full text comparison remains open.
