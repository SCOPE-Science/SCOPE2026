# Graph-isomorphism classification for compressed zero-divisor graphs of short Gorenstein local rings

## Finding
Let \(R\) be a finite commutative Gorenstein local ring with maximal ideal \(\mathfrak m\), \(\mathfrak m^3=0\ne\mathfrak m^2\), residue field \(k=\mathbb F_q\), and \(d=\dim_k(\mathfrak m/\mathfrak m^2)\ge2\). Let \(B\) be the nonsingular symmetric \(k\)-bilinear multiplication pairing on \(V=\mathfrak m/\mathfrak m^2\), with values identified with \(k\) through a nonzero socle generator. Write \(\Gamma_E(R)\) for the simple compressed zero-divisor graph whose vertices are the distinct annihilator classes of nonzero zero divisors and in which two *distinct* classes are adjacent precisely when their product vanishes.

**Classification theorem.** Two such rings \(R,S\) have isomorphic compressed graphs if and only if their residue-field orders and embedding dimensions are equal and their multiplication forms are *similar* (equivalent after an invertible linear change of variables and multiplication by a nonzero scalar). The graph itself recovers all of these data. Thus the classification applies without assuming the rings contain coefficient fields.

For \(N=(q^d-1)/(q-1)\) and \(Q=(q^{d-1}-1)/(q-1)\), let \(I\) be the number of isotropic points of the projective multiplication form. Its value is
\[
I=\begin{cases}
Q,&q\text{ odd},\ d\text{ odd},\\
Q+\chi((-1)^{d/2}\det B)q^{(d-2)/2},&q\text{ odd},\ d\text{ even},\\
N,&q\text{ even and }B\text{ alternating},\\
Q,&q\text{ even and }B\text{ nonalternating}.
\end{cases}
\]
Here \(\chi\) is the quadratic character of \(\mathbb F_q^\times\). The graph has \(N+1\) vertices. One socle vertex has degree \(N\); precisely \(I\) other vertices have degree \(Q\), and the remaining \(N-I\) vertices have degree \(Q+1\). Its edge count is
\[
|E(\Gamma_E(R))|=N+\frac{NQ-I}{2}.
\]
In embedding dimension two the graph is a bouquet of \((N-I)/2\) triangles and \(I\) pendant edges sharing the socle vertex. Its Tutte polynomial and number of spanning trees are respectively
\[
T(x,y)=x^I(x^2+x+y)^{(N-I)/2},\qquad \tau=3^{(N-I)/2}.
\]

The graph classification does **not** classify the rings: the characteristic-two ring \(\mathbb F_2[x,y]/(x^2,y^2)\) and the characteristic-four ring \((\mathbb Z/4\mathbb Z)[t]/(t^2)\) are nonisomorphic but both have compressed graph \(K_{1,3}\).

## Assumptions and scope
All rings are commutative with identity. The residue field is finite; \(\mathfrak m^2\) is nonzero, \(\mathfrak m^3=0\), the socle is one-dimensional over the residue field, and embedding dimension is at least two. No equal-characteristic, coefficient-field, or restriction on characteristic is imposed. Graphs are simple, so self-orthogonal vertices do not have loops. The theorem is an isomorphism classification *within this stated ring family*, not for arbitrary finite local rings.

## Proof
**1. Socle and annihilator classes.** Since \(\mathfrak m^3=0\), \(\mathfrak m^2\subseteq\operatorname{Soc}(R)\). The Gorenstein condition forces equality and identifies \(\mathfrak m^2\) with the one-dimensional \(k\)-space. Products \(\mathfrak m\cdot\mathfrak m\) therefore induce the symmetric bilinear form \(B\) on \(V=\mathfrak m/\mathfrak m^2\). If its radical contained a nonzero class represented by \(a\in\mathfrak m\setminus\mathfrak m^2\), then \(a\mathfrak m=0\), placing \(a\) in the socle; contradiction. Thus \(B\) is nonsingular.

Every nonzero zero divisor lies in \(\mathfrak m\). An element of \(\mathfrak m^2\setminus\{0\}\) has annihilator \(\mathfrak m\), so all such elements form one vertex. If \(a\notin\mathfrak m^2\), then \(\operatorname{Ann}(a)\cap\mathfrak m\) is exactly the inverse image of \(\bar a^\perp\subseteq V\), and no unit annihilates \(a\). By nonsingularity, two such annihilator ideals agree if and only if their nonzero classes in \(V\) span the same one-dimensional subspace. Hence other graph vertices are \(\mathbb P(V)\), and two distinct projective vertices are adjacent exactly when \(B(a,b)=0\); the socle vertex is adjacent to every projective vertex. This projective description uses the bilinear-form and annihilator lemmas established by Kadu (2020), which we credit as antecedents.

**2. Degrees and isotropic census.** For each projective point \([a]\), the hyperplane \(a^\perp\) contains exactly \(Q\) projective points. If \([a]\) is isotropic, one of these is \([a]\) itself and is discarded in the simple graph; the socle neighbor therefore gives degree \(Q\). If anisotropic, all \(Q\) are distinct neighbors, yielding degree \(Q+1\). Summing the degrees gives the stated edge formula.

When \(q\) is even, \(B(v,v)\) is the square of a linear functional because finite fields are perfect. The functional vanishes identically exactly when \(B\) is alternating, yielding \(I=N\), and otherwise its kernel is a codimension-one subspace, yielding \(I=Q\). When \(q\) is odd, diagonalization and the standard one-variable quadratic Gauss-sum identity count nonzero solutions to \(B(v,v)=0\), giving \(q^{d-1}-1\) if \(d\) is odd and \(q^{d-1}-1+(q-1)\chi((-1)^{d/2}\det B)q^{(d-2)/2}\) if \(d\) is even. Dividing by \(q-1\) gives the displayed formula for \(I\).

**3. Recovering the parameters from the unlabelled graph.** The socle vertex is the unique vertex of degree \(N\), since \(Q+1<N\) whenever \(d\ge2\). Thus the graph recovers \(N\) and the degrees of the remaining projective vertices. If the latter degrees are unequal, the smaller is \(Q\), its multiplicity is \(I\), and \(q=(N-1)/Q\). If they all agree, the quadratic-form census yields exactly three possibilities: (a) degree one, which forces \(d=2\), even \(q\), and an alternating form; (b) degree two, which forces \(d=2\), odd \(q\), and an anisotropic form; or (c) degree at least three, which forces even \(q\), \(d\ge4\), and an alternating form. In the first two cases \(q=N-1\); in the last case \(Q\) is that common degree and \(q=(N-1)/Q\). In every case \(d\) is uniquely determined by \(N=1+q+\cdots+q^{d-1}\). The graph also recovers \(I\).

**4. Similarity and converse.** Standard finite-field classification of nonsingular symmetric bilinear forms says that for odd \(q\), forms of fixed dimension are similar in odd dimension and, in even dimension, precisely when the square-class of their determinant agrees. In even characteristic they are similar precisely when they have the same dimension and are both alternating or both nonalternating. The isotropic-count formula distinguishes the two even-dimensional odd-characteristic determinant classes, and, in even characteristic, distinguishes alternating from nonalternating forms. Thus equal \((q,d,I)\) is equivalent to similarity of the multiplication pairings. A similitude maps projective orthogonality to projective orthogonality and fixes the socle vertex, proving the converse and the classification.

**5. Binary projective case and non-rigidity.** When \(d=2\), orthogonal complementation on projective lines is an involution. Its fixed points are the \(I\) isotropic lines; all other lines occur in transposed pairs and each such pair, together with the universal socle vertex, forms a triangle. The claimed bouquet structure and Tutte/spanning-tree formulas follow by one-vertex gluing. Both displayed nonisomorphic rings have \(q=2\), \(d=2\), and alternating nonsingular multiplication form; their characteristics differ, but their compressed graphs are both the three-leaf star.

## Verification
The accompanying `verify.py` constructs projective orthogonality graphs for 25 finite-field/form configurations over field sizes \(2,3,4,5,7\). It checks vertex degrees, isotropic counts, and edge totals against the formulas. In 12 configurations it also enumerates all nonzero radical elements, computes their complete annihilator signatures, forms the genuine compressed graph, and compares its order, degree distribution, and edge number with the projective construction. Finally it enumerates all elements of both explicit sixteen-element rings in the non-rigidity example, computes their annihilator classes, and verifies both compressed graphs are \(K_{1,3}\). Run `python3 verify.py`; the reproducible success marker is `VERIFY_OK 25 polar-field configurations plus direct annihilator computations`. The all-parameter assertion is proved algebraically above; finite computation is a check, not a substitute for proof.

## Relationship to prior work
Kadu, *On the problem of the finiteness of the clique number of compressed zero-divisor graphs of Artinian rings* (first posted October 2020), Proposition 3.6 and Lemma 3.7, explicitly established the underlying multiplication-form/annihilator/projective-orthogonality connection. Consequently that geometric reduction is **not** claimed as new. Kadu and Tanpure, *Zero-divisors of Gorenstein rings* (first posted September 28, 2026), establish the comparison of compressed and associate-class zero-divisor graphs and the Gorenstein characterization. Neither inspected work gives the graph-isomorphism **classification between arbitrary pairs of finite short Gorenstein local rings**, the graph-theoretic recovery of the finite-field order, embedding dimension and similarity type, or the full isotropic degree formula and binary Tutte specialization. The classification here refines these prior geometric and graph-comparison results; it is not a theorem about general zero-divisor graph reconstruction outside the hypotheses.

## Limitations
The result requires \(\mathfrak m^3=0\ne\mathfrak m^2\), a one-dimensional socle, and finite residue field; higher nilpotency, degenerate pairings and nonlocal rings are not classified. The compressed graph does not distinguish ring characteristic or other extension data. A previously unknown equivalent finite-polar-graph reconstruction theorem in unindexed literature remains a possible bibliographic overlap. Independent mathematical audit has not been performed.

## References
1. G. S. Kadu and V. B. Tanpure, *Zero-divisors of Gorenstein rings*, arXiv:2609.36021, version 1 dated September 28, 2026, Sections 2–6. https://arxiv.org/html/2609.36021v1
2. G. S. Kadu, *On the problem of the finiteness of the clique number of compressed zero-divisor graphs of Artinian rings*, arXiv:2010.06924, original version posted October 2020, Proposition 3.6, Lemma 3.7 and Section 2. https://arxiv.org/html/2010.06924v1
3. L. C. Grove, *Classical Groups and Geometric Algebra*, AMS Graduate Studies in Mathematics 39 (2002), finite-field bilinear-form classification (cited in Kadu 2020).
