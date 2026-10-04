# The \(D_4\) 24-cell is lattice reduced and complete

## Finding

Let
\[
D_4=\left\{z\in\mathbb Z^4:\sum_{i=1}^4 z_i\equiv0\pmod2\right\}
\]
and let its dual lattice be
\[
\Lambda=D_4^*
=\mathbb Z^4\cup\left((1/2,1/2,1/2,1/2)+\mathbb Z^4\right).
\]
Define the regular 24-cell in its root realization by
\[
C=\operatorname{conv}\{\pm e_i\pm e_j:1\le i<j\le4\}.
\]
Then
\[
\boxed{C\text{ is simultaneously lattice reduced and lattice complete with respect to }\Lambda.}
\]

In particular, \(C\) is origin-symmetric, four-dimensional, and not a simplex. It therefore gives an affirmative answer to Codenotti--Freyer Question 5.3, which asks whether an origin-symmetric lattice reduced and lattice complete convex body exists in dimension at least three.

The key identity is
\[
\boxed{C=(V_{D_4})^*=2V_{D_4^*}},
\]
where \(V_L\) denotes the Euclidean Voronoi cell of a lattice \(L\).

## Assumptions and scope

For a full-rank lattice \(L\subset\mathbb R^d\), its Voronoi cell is
\[
V_L=\{x:x\cdot v\le \lVert v\rVert^2/2\text{ for every }v\in L\}.
\]
A convex body is lattice reduced if it has no proper convex subset of the same lattice width, and lattice complete if it has no proper convex superset of the same lattice diameter.

Codenotti and Freyer prove that \(V_L\) is complete with respect to \(L\), while \((V_L)^*\) is reduced with respect to \(L^*\). They also prove that positive homotheties preserve both properties.

The proof below establishes the needed Voronoi identities directly from coordinates. It does not assume that a pre-existing classification of the relevant vectors of \(D_4\) or \(D_4^*\) is complete.

## Proof

Put
\[
R=\{\pm e_i\pm e_j:1\le i<j\le4\}.
\]
Every vector in \(R\) belongs to \(D_4\) and has squared Euclidean norm \(2\). Consider
\[
P=\{x\in\mathbb R^4:r\cdot x\le1\text{ for every }r\in R\}.
\]
Equivalently,
\[
P=\{x:|x_i\pm x_j|\le1\text{ for all }i<j\}.
\]
Its vertices are exactly
\[
M=\{\pm e_i:1\le i\le4\}
\cup
\{(\varepsilon_1/2,\varepsilon_2/2,\varepsilon_3/2,\varepsilon_4/2):\varepsilon_i\in\{\pm1\}\}.
\]
Thus
\[
P=\operatorname{conv}M.
\]
The packaged exact-rational checker independently reconstructs these \(24\) vertices from all fourfold intersections of the \(24\) root halfspaces.

We now prove that \(P=V_{D_4}\). Since \(P=\operatorname{conv}M\), for \(z\in\mathbb R^4\),
\[
h_P(z)=\max\left\{\lVert z\rVert_\infty,\frac12\lVert z\rVert_1\right\}.
\]
Let \(0\ne z\in D_4\). Because \(z\) is integral,
\[
\frac12\lVert z\rVert_1\le\frac12\lVert z\rVert_2^2.
\]
For the other term, put \(m=\lVert z\rVert_\infty\). If at least two coordinates are nonzero, then
\[
\lVert z\rVert_2^2\ge m^2+1\ge2m.
\]
If only one coordinate is nonzero, the even-coordinate-sum condition forces \(m\ge2\), so again
\[
\lVert z\rVert_2^2=m^2\ge2m.
\]
Hence
\[
h_P(z)\le\frac12\lVert z\rVert_2^2
\]
for every nonzero \(z\in D_4\). Therefore every Voronoi halfspace associated with a vector of \(D_4\) contains \(P\). Conversely, the halfspaces associated with the roots \(R\) are exactly the defining halfspaces of \(P\), because every root has squared norm \(2\). Thus
\[
P=V_{D_4}.
\]

Since \(P\) is defined by the inequalities \(r\cdot x\le1\), \(r\in R\), polarity gives
\[
P^*=\operatorname{conv}R=C.
\]
Codenotti--Freyer Proposition 3.11 now implies that \(C=(V_{D_4})^*\) is lattice reduced with respect to \(D_4^*=\Lambda\).

It remains to prove completeness with respect to the same lattice. First, the dual lattice is exactly
\[
D_4^*=\mathbb Z^4\cup\left((1/2,1/2,1/2,1/2)+\mathbb Z^4\right).
\]
Indeed, the vectors \(e_i-e_j\in D_4\) force all dual coordinates to be congruent modulo \(\mathbb Z\), and the vectors \(e_i+e_j\in D_4\) force twice every dual coordinate to be integral. Hence either all coordinates are integral or all are half-integral; the converse inclusion is immediate from the even-sum definition of \(D_4\).

The shortest nonzero vectors of \(\Lambda\) are precisely the \(24\) vectors in \(M\), all of norm \(1\). Since \(P=\operatorname{conv}M\), the identity \(C=P^*\) yields
\[
\frac12C
=
\{x:m\cdot x\le1/2\text{ for every }m\in M\}.
\]
We show that these are already all Voronoi inequalities of \(\Lambda\). For \(y\in\mathbb R^4\), let \(a\ge b\ge c\ge d\ge0\) be the ordered absolute coordinate values. Because the vertices of \(C/2\) are the half-roots,
\[
h_{C/2}(y)=\frac{a+b}{2}.
\]
If \(0\ne y\in\mathbb Z^4\), then
\[
a+b\le\sum_{i=1}^4 y_i^2.
\]
If \(y\) is in the half-integral coset, all four absolute coordinates are at least \(1/2\), and
\[
\sum_{i=1}^4 y_i^2-(a+b)
\ge
(a-1/2)^2+(b-1/2)^2
\ge0.
\]
Therefore, for every nonzero \(y\in\Lambda\),
\[
h_{C/2}(y)\le\frac12\lVert y\rVert_2^2.
\]
So every Voronoi halfspace of \(\Lambda\) contains \(C/2\), while the inequalities from the shortest vectors \(M\) already define \(C/2\). Hence
\[
V_{D_4^*}=\frac12C.
\]
Equivalently,
\[
C=2V_{D_4^*}.
\]
By Codenotti--Freyer Proposition 3.11, \(V_{D_4^*}\) is lattice complete with respect to \(D_4^*\); positive homothety preserves completeness. Thus \(C\) is complete with respect to \(\Lambda\), completing the proof.

## Verification

The standalone `verify.py` uses exact rational arithmetic. It enumerates all four-active-root intersections of
\[
|x_i\pm x_j|\le1
\]
and recovers exactly the \(24\) vertices \(M\). It then enumerates all four-active-minimal-vector intersections of
\[
m\cdot x\le1/2
\]
and recovers exactly the \(24\) half-roots, proving the finite polar descriptions used above.

It also checks the support inequalities for all tested \(D_4\) and \(D_4^*\) lattice vectors in large bounded boxes and verifies that every root uniquely selects its corresponding vertex of \(C\). These bounded tests are consistency checks; the all-lattice inequalities are proved analytically in the preceding section.

The replay output is:

`VERIFY_OK D4 24-cell reduced-complete identity`

## Relationship to prior work

Codenotti and Freyer introduce lattice reduced and lattice complete convex bodies, prove the Voronoi-cell principle used above, and ask in Question 5.3 whether there are origin-symmetric bodies that are both reduced and complete in dimensions at least three. Their list of known simultaneous examples consists only of two-dimensional bodies and simplices, and they explicitly say that a higher-dimensional non-simplex example would already be interesting.

Their paper contains no occurrence of `24-cell` or `D4`, and it does not state the double-Voronoi identity above.

The fact that the \(D_4\) Voronoi cell is a regular 24-cell and that the 24-cell is self-dual is classical background. Those facts alone do not imply simultaneous reducedness and completeness with respect to one fixed lattice; the relevant point is the metric-lattice identity
\[
(V_{D_4})^*=2V_{D_4^*},
\]
which aligns the two halves of Proposition 3.11 on the same body and the same lattice.

Targeted searches for the exact question together with `D4`, `24-cell`, `Voronoi`, `reduced`, and `complete` did not locate a prior statement of this consequence.

## Limitations

This proves existence in dimension four. It does not produce a three-dimensional origin-symmetric example, nor does it classify all simultaneous reduced-complete bodies.

The proof depends on the Euclidean dual pair \(D_4,D_4^*\) and the special 24-cell Voronoi duality. No claim is made that an analogous construction works in every dimension.

A differently phrased or unindexed prior observation could still exist; the originality conclusion is based on the inspected primary paper, targeted public searches, and the indexed comparison search.

## References

G. Codenotti and A. Freyer, “Lattice reduced and complete convex bodies,” Journal of the London Mathematical Society 110 (2024), e12982, DOI 10.1112/jlms.12982; preprint arXiv:2307.09429, first submitted 2023-07-18.

J. H. Conway and N. J. A. Sloane, Sphere Packings, Lattices and Groups, 3rd ed., Springer, 1999. The \(D_4\) lattice and its regular 24-cell Voronoi geometry are standard material in this reference.
