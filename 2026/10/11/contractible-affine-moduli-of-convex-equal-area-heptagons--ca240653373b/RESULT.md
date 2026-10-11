# Contractible affine moduli of convex equal-area heptagons
## Finding
Let \(\mathcal T_7\) denote the affine moduli space of cyclically marked strictly convex equal-area heptagons: the seven triangles determined by consecutive triples of vertices have one common nonzero area. Then
\[
\mathcal T_7\cong D:=\{{(x,y)\in\mathbb R_{{>0}}^2:xy>1\}},
\]
by a smooth bijection with smooth inverse. Consequently \(\mathcal T_7\) is connected and contractible. This settles the \(n=7\) case of the connectedness question posed for the spaces \(\mathcal T_n\) by Craizer, Teixeira and da Silva.

## Assumptions and scope
Vertices are cyclically marked, the polygon is strictly convex, and affine equivalence preserves the marking. The equal-area condition is the one used by Harel--Rabin and Craizer--Teixeira--da Silva: all triangles formed by three consecutive vertices have the same nonzero area. The conclusion concerns \(n=7\) only; no claim is made for \(n\ge8\).

Following Craizer--Teixeira--da Silva, write the equal-area recurrence as
\[
P_{{i+2}}-P_{{i-1}}=(3-\mu_{{i+1/2}})(P_{{i+1}}-P_i),
\]
where strict convexity gives \(\mu_{{i+1/2}}<2\). Normalize affinely to
\[
P_1=(0,0),\qquad P_2=(1,0),\qquad P_3=(0,1),
\]
and define \(x=2-\mu_{{5/2}}>0\), \(y=2-\mu_{{7/2}}>0\).

## Proof
The recurrence first determines
\[
P_4=(-1-x,1+x),
\qquad
P_5=(-x-y-xy,\,x+xy).
\]
For a heptagon, the completion construction of Proposition 3.2 of Craizer--Teixeira--da Silva uses three lines: \(r_1=P_5P_1\); \(r_2\), the line through \(P_3\) parallel to \(P_4P_5\); and \(r_3\), the line through \(P_3\) parallel to \(P_1P_2\). Thus \(r_3\) is the line of ordinate \(1\), and \(B=r_2\cap r_3=P_3\).

Let \(O=r_1\cap r_2\) and \(A=r_1\cap r_3\). Parameterizing \(r_1\) by \(tP_5\), direct solution of the two line intersections gives
\[
t_A=\frac{1}{x(1+y)},
\qquad
t_O=\frac{xy+y-1}{y(x+1)}.
\]
Hence
\[
t_O-t_A=
\frac{(xy-1)(xy+x+y)}{xy(x+1)(y+1)}.
\]
The cited completion theorem requires \(A\) to lie on the segment \(P_1O\). Since \(t_A>0\), this is equivalent here to \(xy>1\): if \(xy>1\), then \(t_O>t_A>0\); if \(xy<1\), the order is wrong; and at \(xy=1\) the relevant lines meet at \(A=O\), the strict convex completion degenerates. Thus every strictly convex heptagon yields a point of \(D\), and no point outside \(D\) can occur.

Conversely, take any \(x>0\), \(y>0\) with \(xy>1\). Then \(A\) lies strictly between \(P_1\) and \(O\). Moreover \(B=P_3\) lies on the half-line from \(A\) through \(P_3\). This is exactly case (0) in the proof of Proposition 3.2, where the relevant branch of the completion hyperbola meets \(r_3\) in exactly one point. That intersection determines \(P_7\), and the accompanying parallel-line condition determines \(P_6\), producing a unique strictly convex equal-area completion.

The construction is smooth on the open domain \(D\) by the smooth-map statement of Proposition 3.2. Its inverse is smooth because \(x=2-\mu_{{5/2}}\) and \(y=2-\mu_{{7/2}}\), and each recurrence coefficient \(3-\mu_{{i+1/2}}\) is recovered smoothly from a nondegenerate normalized polygon. Therefore \(\mathcal T_7\) is diffeomorphic to \(D\). Finally, \((x,y)\mapsto(\log x,\log y)\) identifies \(D\) with the open half-plane \(\{{(u,v):u+v>0\}}\), proving connectedness and contractibility.

## Verification
The critical algebra was independently recomputed from the normalized recurrence: the displayed formulas for \(P_4\), \(P_5\), \(t_A\), \(t_O\), and the factorization of \(t_O-t_A\) all agree exactly. The geometric existence and uniqueness step is not inferred from numerical experiments; it invokes the materially inspected hyperbola-completion argument in Proposition 3.2 of the cited 2011 preprint. No claim relies on finite enumeration.

## Relationship to prior work
Harel and Rabin give a general algebraic parametrization of equal-area polygons and work out the six-vertex case explicitly, but do not give a connectedness classification for convex equal-area heptagons. Craizer, Teixeira and da Silva introduce \(\mathcal T_n\), prove the two-branch hyperbola completion theorem, and explicitly state that they conjecture \(\mathcal T_n\) is connected. Their paper does not specialize that construction to obtain the exact \(n=7\) domain above. The present calculation identifies that domain and therefore proves the first genuinely two-parameter case of their connectedness conjecture.

## Limitations
Only cyclically marked strictly convex heptagons are classified. Quotienting by cyclic or dihedral relabeling preserves connectedness but is not asserted here to preserve the displayed diffeomorphic model. No statement is made about nonconvex equal-area heptagons or about \(\mathcal T_n\) for \(n\ge8\). The originality search cannot exclude an unindexed note or informal derivation of the same \(n=7\) specialization.

## References
1. M. Craizer, R. C. Teixeira, M. A. H. B. da Silva, “Affine Properties of Convex Equal-Area Polygons,” arXiv:1103.2722v1, first posted 2011-03-14; later Discrete & Computational Geometry 48 (2012), 580--595, DOI 10.1007/s00454-012-9448-y.
2. G. Harel, J. M. Rabin, “Polygons Whose Vertex Triangles Have Equal Area,” American Mathematical Monthly 110 (2003), 606--619, DOI 10.1080/00029890.2003.11920000.
