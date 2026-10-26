# Independent Frobenius splitting of twelve nodes on tetrahedral quartic K3 models

## Finding
Fix \(q=2^m\), \(m\ge1\). Let all four \(a_i\) and all six \(b_{ij}\) be nonzero elements of \(\mathbb F_q\). On the fixed coordinate tetrahedron of \(\mathbb P^3\), form
\[
Q(x)=\sum_{i=0}^{3}a_i x_i^2+\sum_{0\le i<j\le3}b_{ij}x_i x_j,\qquad X:\ x_0x_1x_2x_3+Q(x)^2=0.
\]
The geometric singular locus consists of precisely twelve ordinary nodes, two on each coordinate edge. The minimal resolution \(\widetilde X\) is a K3 surface. Define the split-edge subset
\[
S(a,b)=\left\{\{i,j\}:\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}\!\left(\frac{a_i a_j}{b_{ij}^2}\right)=0\right\},\qquad s=|S(a,b)|.
\]
Each edge in \(S(a,b)\) carries two distinct \(\mathbb F_q\)-rational nodes. Each other edge carries one Frobenius orbit of two nodes over \(\mathbb F_{q^2}\). Hence precisely \(2s\) of the twelve geometric nodes are \(\mathbb F_q\)-rational.

For every fixed subset \(S\) of the six labeled edges, with \(|S|=s\), the exact number of **coefficient-marked, product-normalized** presentations having split set \(S\) is
\[
N_S(q)=(q-1)^4\left(\frac q2-1\right)^s\left(\frac q2\right)^{6-s}.
\]
Consequently the number with exactly \(2s\) rational nodes is \(\binom6s N_S(q)\). For \(q\ge4\), every one of the 64 labeled Frobenius splitting patterns occurs. For \(q=2\), the sole permitted presentation has no rational nodes and six degree-two orbits. The formulas count presentations on the fixed ordered tetrahedron, **not** abstract projective or geometric isomorphism classes.

The node splitting also gives a complete, model-independent exceptional-divisor correction to the arithmetic of this family:
\[
\boxed{\frac{Z(\widetilde X/\mathbb F_q,T)}{Z(X/\mathbb F_q,T)}=(1-qT)^{-2s}(1-q^2T^2)^{-(6-s)}.}
\]
In particular, for every integer \(r\ge1\),
\[
\#\operatorname{Sing}(X)(\mathbb F_{q^r})=2s+2(6-s)\mathbf1_{2\mid r},\quad
\#\widetilde X(\mathbb F_{q^r})-\#X(\mathbb F_{q^r})=q^r\bigl(2s+2(6-s)\mathbf1_{2\mid r}\bigr).
\]

## Assumptions and scope
All statements concern fields of characteristic two and the literal displayed quartic with its coefficient of \(x_0x_1x_2x_3\) normalized to one, with each of its ten displayed quadratic coefficients nonzero. The four coordinate planes and six edges are labeled and fixed. In the node-count theorem the singularities are geometric, over an algebraic closure; the finite-field classifications concern descent under arithmetic Frobenius. No assertion about all possible 12-node quartics or their Newton polygons is made.

## Proof
**1. Exhaustion of the geometric singular locus.** Write \(F=x_0x_1x_2x_3+Q^2\). In characteristic two, \(\partial F/\partial x_i=\prod_{j\ne i}x_j\), so a geometric singular point must have at least two zero coordinates; it lies on a coordinate edge. The four coordinate vertices are off \(X\), because at the vertex indexed \(i\) one has \(F=a_i^2\ne0\). On the edge with coordinates \(x_i,x_j\ne0\), setting \(t=x_i/x_j\) reduces the equation to
\[
a_i t^2+b_{ij}t+a_j=0.
\]
Its derivative is \(b_{ij}\ne0\), its constant term is nonzero, and it has exactly two distinct nonzero roots over the algebraic closure. These are all geometric singular points, hence there are exactly twelve.

**2. Ordinary-double-point tangent cones.** Work near a root \(t_0\ne0\) on the edge \(\{i,j\}\), normalize \(x_j=1\), and take \(t-t_0=u\) and the other two coordinates \(v,w\) as local parameters. The quadratic part of the local equation is
\[
\bigl(b_{ij}u+\alpha v+\beta w\bigr)^2+t_0vw,
\]
for certain \(\alpha,\beta\) in the algebraic closure. Its projective conic is smooth: its partial derivatives in \(v,w\) force \(v=w=0\), after which the equation forces \(u=0\) because \(b_{ij}\ne0\). This is a smooth tangent cone, hence the singularity is of type \(A_1\). A reducible quartic surface in projective three-space has a positive-dimensional intersection of components, and would therefore have a positive-dimensional singular locus. Since the twelve singularities are isolated, \(X\) is geometrically integral; as a hypersurface with isolated singularities, it is normal. Resolution of ordinary nodes preserves the canonical class and first cohomology, so the minimal resolution of this normal quartic is a K3 surface.

**3. Exact descent criterion.** Dividing the edge equation by \(a_i\) and substituting \(t=(b_{ij}/a_i)z\) produces
\[
z^2+z+\frac{a_i a_j}{b_{ij}^2}=0.
\]
Over a field of characteristic two, an Artin–Schreier quadratic has two rational roots precisely when the constant has absolute trace zero; otherwise its roots are one conjugate pair of degree two. This proves the node splitting, including its extension-field behavior.

**4. All splitting patterns and exact coefficient counts.** First choose the four diagonal coefficients in \((q-1)^4\) ways. For each labeled edge, with \(a_i,a_j\) now fixed, the map \(b_{ij}\mapsto a_i a_j/b_{ij}^2\) is a bijection of \(\mathbb F_q^\times\) because squaring is a field automorphism. Of its nonzero values, exactly \(q/2-1\) have trace zero and \(q/2\) have trace one. The six edge choices are independent. Multiplication gives \(N_S(q)\) and summing over \(\binom6s\) subsets gives the count for \(2s\) rational nodes. For \(q\ge4\), both trace classes among the nonzero values are nonempty, yielding all 64 profiles. In the exceptional case \(q=2\), only the nonsplit profile exists.

**5. Exceptional divisors and the zeta quotient.** At each \(A_1\) node, the exceptional curve is a smooth conic over the residue field of the node. Every smooth conic over a finite field has a rational point and is isomorphic to \(\mathbb P^1\) there. Replacing one point rational over \(\mathbb F_{q^r}\) with its exceptional \(\mathbb P^1\) adds exactly \(q^r\) points. At an edge with two degree-one nodes, this happens in every extension; at an edge with one degree-two closed node, it happens only in even-degree extensions. This gives the stated difference of point counts. Inserting it into the defining exponential series for the Hasse–Weil zeta function yields a factor \((1-qT)^{-2}\) for each split edge, and \((1-q^2T^2)^{-1}\) for each nonsplit edge. The product is the stated quotient.

## Verification
The self-contained Python 3 program `verify.py` tests the field arithmetic, explicitly enumerates **all 59,049** permitted coefficient 10-tuples over \(\mathbb F_4\), confirms their assignment to all 64 splitting profiles and the exact size of each profile, and directly checks the associated rational nodes for a representative of every profile. It also realizes and directly checks all 64 profiles over \(\mathbb F_8\), and checks the unique \(\mathbb F_2\) case. Its expected final output is `VERIFY_OK`.

For \(q=4\), the counts with \(2s\) rational nodes for \(s=0,1,2,3,4,5,6\), respectively, are \(5184,15552,19440,12960,4860,972,81\). Their sum is \(59049\). These computations verify finite instances of the theorem but do **not** prove the infinite-field statements; Steps 1–5 provide the algebraic proofs.

## Relationship to prior work
Catanese and Schütt, *Singularities of normal quartic surfaces III (char=2, non-supersingular)*, arXiv:2206.03295, Example 19, introduce the general quartic architecture \(l_1l_2l_3l_4+Q^2\) and show that its general member has twelve nodes. The construction and its generic geometric assertions are prior work, not claimed as new. Catanese, *Singularities of normal quartic surfaces I (char=2)*, arXiv:2106.09988, Section 4, also studies twelve-node **symmetric** quartics. The arithmetic contribution here is the explicit six independent trace conditions over every finite field of characteristic two, the exact labeled-profile census, and the corresponding resolution-to-singular-surface zeta-function quotient. These do not require assuming any uniform supersingularity property of the resolved surfaces.

## Limitations
This result does not compute the absolute zeta function of \(X\) or of \(\widetilde X\), and does not assert that all these K3 surfaces have the same Newton polygon. The zeta quotient depends only on the Frobenius action on the exceptional nodes. Parameter counts are coefficient-marked counts rather than a moduli or isomorphism-class census. The source-literature comparison cannot exclude an earlier unindexed finite-field specialization or a previously published formulation of the same trace calculation. Independent validation has not been performed.

## References
1. F. Catanese and M. Schütt, *Singularities of normal quartic surfaces III (char=2, non-supersingular)*, arXiv:2206.03295, first submitted 7 June 2022, especially Example 19 and Remark 20. https://arxiv.org/abs/2206.03295
2. F. Catanese, *Singularities of normal quartic surfaces I (char=2)*, arXiv:2106.09988, first submitted 18 June 2021, especially Section 4. https://arxiv.org/abs/2106.09988
