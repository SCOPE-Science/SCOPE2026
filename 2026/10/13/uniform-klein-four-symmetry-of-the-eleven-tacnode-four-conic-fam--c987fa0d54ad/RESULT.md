# Uniform Klein-four symmetry of the eleven-tacnode four-conic family

## Finding

For every \(r\in\mathbb C\setminus\{0,1,-1,i,-i\}\), consider the reduced plane curve \(\mathcal A_r\) formed by the four conics
\[
\begin{aligned}
Q_0&=x^2+y^2-z^2,\\
Q_1&=x^2+r^2y^2-r^2z^2,\\
Q_+&=x^2+(r^2+1)y^2+2ryz,\\
Q_-&=x^2+(r^2+1)y^2-2ryz.
\end{aligned}
\]
Its full ambient projective stabilizer is exactly
\[
\operatorname{Stab}_{\operatorname{PGL}_3(\mathbb C)}(\mathcal A_r)
=\left\{[x:y:z]\longmapsto[\epsilon x:y:\delta z]\;:\;
\epsilon,\delta\in\{\pm1\}\right\}
\cong C_2\times C_2.
\]
This holds **for every admissible parameter**, with no exceptional symmetry jump. On the four irreducible components, this group fixes \(Q_0\) and \(Q_1\) separately and has the orbit \(\{Q_+,Q_-\}\); its image in the permutation group on components is \(C_2\).

## Assumptions and scope

Work over \(\mathbb C\) in characteristic zero. Every stabilizer consists of ambient *linear projective* transformations preserving the reduced union, not abstract automorphisms of its normalization. The excluded parameters are precisely \(r=0\), \(r^2=1\), and \(r^2=-1\); these are excluded from every universal quantifier in this result. The four conics are smooth and distinct: their quadratic-form determinants are respectively \(-1,-r^4,-r^2,-r^2\).

The family is the explicit eleven-tacnode family quoted from Megyesi's classification in Măcinic--Pokora, Theorem 3.1, four-conic case. The theorem below is independently proved for the displayed equations and does not require the classification to establish its group calculation.

## Proof

**1. Intrinsic singularity markers.** The six unordered conic pairs have the difference identities
\[
\begin{aligned}
Q_1-Q_0&=(r^2-1)(y^2-z^2),\\
Q_+-Q_0&=(ry+z)^2,&Q_--Q_0&=(ry-z)^2,\\
Q_+-Q_1&=(y+rz)^2,&Q_--Q_1&=(y-rz)^2,\\
Q_+-Q_-&=4ryz.
\end{aligned}
\]
The first five pairs meet in two distinct points each, with local intersection multiplicity \(2\) at each: both component curves are smooth and tangent. For example, \(Q_0\cap Q_1\) consists of \([0:1:1]\) and \([0:1:-1]\); \(Q_0\cap Q_+\) lies on \(z=-ry\) with \(x^2=(r^2-1)y^2\); and \(Q_1\cap Q_+\) lies on \(y=-rz\) with \(x^2=r^2(1-r^2)z^2\). The minus cases follow by changing the sign of \(z\). All these points are distinct, since \(r\neq0\) and \(r^2\neq1\); no point lies on three components.

The exceptional pair \(Q_+,Q_-\) has one tacnode
\[
p=[0:0:1]
\]
and two transverse nodes
\[
q_\pm=[\pm\lambda:1:0],\qquad \lambda^2=-(r^2+1).
\]
Indeed \(Q_+-Q_-=4ryz\): on \(y=0\) the common equation is \(x^2=0\), whereas on \(z=0\) it is \(x^2+(r^2+1)y^2=0\). Because \(r\neq0\) and \(r^2+1\neq0\), the latter roots are distinct and the conic gradients at these nodes are independent. At \(p\), the gradients of \(Q_+\) and \(Q_-\) are nonzero multiples of \((0,1,0)\), so their common tangent is \(y=0\). None of \(p,q_+,q_-\) belongs to \(Q_0\) or \(Q_1\). Thus \(\mathcal A_r\) has exactly eleven distinct tacnodes and two nodes, and \(\{Q_+,Q_-\}\) is characterized intrinsically as the **unique** pair of components whose mutual intersections include transverse nodes.

**2. Forced projective normal form.** Let \(g\in\operatorname{PGL}_3(\mathbb C)\) preserve \(\mathcal A_r\). It permutes its smooth conic components and hence must preserve the unordered pair \(\{Q_+,Q_-\}\). Consequently it fixes their unique mutual tacnode \(p\), preserves their node pair \(\{q_+,q_-\}\), and preserves both the node-secant line \(z=0\) and the common tangent at \(p\), namely \(y=0\).

A projectivity preserving these three distinct geometric markers must have the form
\[
[x:y:z]\longmapsto[a x+b y:c y:d z],\qquad acd\neq0.
\]
Its restriction to \(z=0\) permutes the two points with affine first-coordinate ratios \(\pm\lambda\). The unordered pair of images is
\[
\left\{\frac{a\lambda+b}{c},\frac{-a\lambda+b}{c}\right\}
=\{\lambda,-\lambda\}.
\]
Taking sums gives \(b=0\); taking differences, since \(\lambda\neq0\), gives \(a/c=\epsilon\in\{\pm1\}\). Write \(t=d/c\neq0\). We have reduced every possible projective stabilizer to
\[
[x:y:z]\longmapsto[\epsilon x:y:t z].
\]

**3. The remaining coefficient constraint.** Under this transformation the conic \(Q_+\) becomes
\[
x^2+(r^2+1)y^2+2rt yz.
\]
It must be either \(Q_+\) or \(Q_-\) up to scalar. Equality of the nonzero \(x^2\) coefficients fixes that scalar to \(1\); comparison of \(yz\) coefficients, using \(r\neq0\), forces \(t=1\) or \(t=-1\). Conversely the four choices \(\epsilon, t\in\{\pm1\}\) each fix \(Q_0,Q_1\) and either fix or interchange \(Q_+,Q_-\). They form a faithful Klein four subgroup of \(\operatorname{PGL}_3\). This is therefore the **entire** stabilizer, uniformly in \(r\). \(\square\)

## Verification

The accompanying `verify.py` uses only Python 3 standard-library integer arithmetic in a sparse polynomial ring \(\mathbb Z[r,x,y,z,t]\). Run `python3 verify.py`. It rechecks the six universal polynomial identities above, the four smoothness determinants, gradients at \(p\), the two-node equation, all four exhibited projectivities, and the final coefficient formula. The completeness argument in Step 2 is a geometric proof, not an inference from finite tests. There is no randomness, floating-point arithmetic, or parameter sampling.

The pair-contact graph, which marks \(Q_+,Q_-\) as the unique pair meeting at nodes, allows an abstract interchange of \(Q_0,Q_1\) as well as an interchange of \(Q_+,Q_-\). The geometric flag from \(p\), the two nodes, and the tangent proves that the first interchange is **not** realized by any ambient projectivity.

## Relationship to prior work

Megyesi, Proposition 7(b), classifies four-conic configurations with eleven tacnodes, as cited and explicitly instantiated in Măcinic--Pokora, Theorem 3.1 (four-conic case). These sources motivate the natural one-parameter family and its extremal contact combinatorics. Măcinic--Pokora computes plus-one generated exponents for the special realization \(r=2\), but its inspected theorem and surrounding discussion do **not** state the full projective stabilizer, uniformity in the parameter, or the failure of the abstract conic-pair permutation \(Q_0\leftrightarrow Q_1\) to lift projectively. Bromboszcz--Jarosławski--Pokora subsequently studies the same eleven-tacnode combinatorial type from the standpoint of syzygies, not the ambient projective action.

## Limitations

This is the ambient projective symmetry group, not the group of all abstract automorphisms of the reducible curve. No statement is made for the excluded degenerate parameter values, nor is every admissible member asserted to have identical Jacobian-syzygy exponents. The original full text of Megyesi's 2000 classification was not accessible in the literature review; an earlier discussion under equivalent coordinates remains a residual priority/overlap risk. This result does not claim a complete classification of moduli equivalences between different values of \(r\).

## References

1. A. Măcinic and P. Pokora, *On plus-one generated conic-line arrangements with simple singularities*, arXiv:2309.15228 (first posted 2023-09-26), Theorem 3.1; doi:10.4171/RLM/1044.
2. G. Megyesi, *Configurations of conics with many tacnodes*, Tohoku Math. J. **52** (2000), 555--577, Proposition 7(b); doi:10.2748/tmj/1178207755.
3. A. Bromboszcz, B. Jarosławski and P. Pokora, *On plus-one generated arrangements of plane conics*, Geom. Dedicata **220** (2026), article 10, Theorem 4.2; doi:10.1007/s10711-025-01063-w.
