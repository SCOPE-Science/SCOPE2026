# Even Lusztig fibers for the 3-Kronecker quiver at dimension vector (2,2)

## Context

Let \(Q\) be the 3-Kronecker quiver with vertices \(0,1\) and three arrows
\(0\to1\), and let the dimension vector be \(\nu=(2,2)\).  For each flag type
\(y\in Y_\nu\), the Lusztig map
\[
\pi_y:\widetilde F_y\longrightarrow E_V=M_2^3
\]
has a projective fiber over a representation \(A=(A_1,A_2,A_3)\).

The original version of this record went further and asserted parity-perversity
and decomposition-number purity for the wild 3-Kronecker KLR algebra.  That
deduction is not justified by the cited source: Maksimau's parity-sheaf
framework and its even-quiver consequences are stated for Dynkin quivers.
This corrected record keeps the independently checkable fiber-geometry result
and does not infer modular decomposition numbers from it.

## Result

For every flag type \(y\in Y_\nu\) and every complex representation
\(A=(A_1,A_2,A_3)\in M_2^3\), the underlying topological space of the fiber
\(\pi_y^{-1}(A)\) has no odd integral cohomology and has torsion-free integral
cohomology.

More concretely, every fiber is built from one of the following types:

- empty or a finite set of points;
- a point or \(\mathbb P^1\);
- \(\mathbb P^1\times\mathbb P^1\);
- a smooth \((1,1)\)-curve, hence \(\mathbb P^1\);
- a reducible \((1,1)\)-curve consisting of one horizontal and one vertical ruling;
- at most one ruling together with finitely many residual points.

All of these spaces have \(H^{\mathrm{odd}}(-,\mathbb Z)=0\) and free abelian
integral cohomology.

The same geometric classification is characteristic-free at the level of the
incidence equations.  In particular it supplies the fiber-evenness input one
would want in a modular parity-sheaf analysis.  **No claim is made here that
all parity complexes for the wild 3-Kronecker representation space are
perverse, are reductions of characteristic-zero IC complexes, or that all
graded KLR decomposition numbers equal their characteristic-zero values.**
Those statements need additional non-Dynkin representation-theoretic input.

## Proof of the fiber classification

Because both vertex spaces have dimension two, a flag contributing to a
Lusztig fiber contains at most one nontrivial line at each vertex.  Thus every
nontrivial mixed incidence condition can be expressed using a pair of lines
\[
L_0=\langle x\rangle\in\mathbb P(V_0),\qquad
L_1=\langle y\rangle\in\mathbb P(V_1).
\]
For a matrix \(M:V_0\to V_1\), the condition \(M(L_0)\subseteq L_1\) is
\[
f_M(x,y)=\det(Mx,y)=0.
\]
The map
\[
M_2\longrightarrow H^0(\mathbb P^1\times\mathbb P^1,\mathcal O(1,1)),
\qquad M\mapsto f_M,
\]
is a linear isomorphism.

Hence the mixed fibers are common zero loci of the three \((1,1)\)-forms
\(f_{A_1},f_{A_2},f_{A_3}\).  Let \(r\) be the dimension of their span.

- If \(r=0\), the fiber is all of \(\mathbb P^1\times\mathbb P^1\).
- If \(r=1\), the unique nonzero \((1,1)\)-divisor is either a smooth
  \(\mathbb P^1\) or the union of one horizontal and one vertical ruling.
- If \(r\ge2\), two independent \((1,1)\)-forms cannot share an entire
  \((1,1)\)-curve.  Indeed a \((1,1)\)-divisor spans a one-dimensional kernel
  in the four-dimensional space of \((1,1)\)-sections.  Thus a
  positive-dimensional common component can only be a ruling.  Two distinct
  parallel rulings would force all relevant forms to vanish identically in
  that direction, so there is at most one ruling of each relevant type; the
  remaining intersection is finite.

The other flag orders impose only common-kernel or common-image conditions,
which cut out an empty set, a point, or all of \(\mathbb P^1\).

The cohomology assertion follows directly from these descriptions, for
example by Mayer--Vietoris for the reducible ruling configurations.

## Computational cross-check

`artifacts/verify_fibres.py` exhausts all \(16^3=4096\) triples of \(2\times2\)
matrices over \(\mathbb F_2\).  Its recorded rank distribution is
\[
\{0:1,\ 1:105,\ 2:1470,\ 3:2520\},
\]
and the geometric-type counts are

- whole \(\mathbb P^1\times\mathbb P^1\): 1;
- reducible \((1,1)\) wedge: 63;
- smooth \((1,1)\) curve: 42;
- ruling plus finite residual set: 252;
- finite set: 3738.

It also checks the kernel/image cases and 8000 samples over \(\mathbb F_5\).
These finite-field computations are consistency checks for the geometric
classification, not a replacement for the characteristic-free argument.

## Relation to parity-sheaf literature

Maksimau's Lemma 3.7 identifies fiber odd-cohomology vanishing with evenness of
the relevant direct image inside the setup of that paper.  However the paper
begins with a **Dynkin quiver** and its parity/canonical-basis consequences,
including the even-quiver theorem, remain in that Dynkin framework.  The
3-Kronecker quiver is wild, so those consequences cannot be imported merely
from the fiber calculation above.

This correction is important because wild quivers can have extremely general
quiver-Grassmannian geometry in larger dimension vectors.  The present
\((2,2)\) calculation is therefore a small explicit geometric case, not a
purity theorem for the whole wild KLR category.

## Originality and value

Targeted searches found no publication giving exactly this fourteen-flag
\((2,2)\) fiber classification for the 3-Kronecker Lusztig maps.  That is not
a priority proof, so the originality claim is kept modest.  The value is an
explicit low-dimensional wild-quiver evenness calculation and a reusable test
case for any future extension of parity/KLR purity machinery beyond Dynkin
type.

## Reproducibility

Run

`python3 artifacts/verify_fibres.py`

from the record directory.  The script writes
`artifacts/verify_log.txt`.

## References

- R. Maksimau, *Canonical basis, KLR-algebras and parity sheaves*,
  J. Algebra 2015, arXiv:1301.6261.
- O. Lorscheid, *Representation type via Euler characteristics and
  singularities of quiver Grassmannians*, Bull. London Math. Soc. 2019.
