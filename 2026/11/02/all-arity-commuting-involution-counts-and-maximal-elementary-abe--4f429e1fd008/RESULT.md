# All-arity commuting-involution counts and maximal elementary abelian subgroups of \(UT_4(\mathbb F_{2^f})\)

## Finding
For every integer \(f\ge1\), put \(q=2^f\) and \(G=UT_4(\mathbb F_q)\). Let \(C_m(q)\) count ordered \(m\)-tuples of pairwise commuting elements of square one, including the identity, for each integer \(m\ge0\). Then
\[
C_m(q)=q^{4m}+(2q+1)q^{3m}-(q+1)^2q^{2m}+q^{m+2}.
\]
Thus the number of pairwise commuting tuples of **nonidentity involutions** is
\[
P_m(q)=(q^4-1)^m+(2q+1)(q^3-1)^m-(q+1)^2(q^2-1)^m+q^2(q-1)^m.
\]
The ordinary generating function for the first count is
\[
\sum_{m\ge0}C_m(q)z^m=\frac1{1-q^4z}+\frac{2q+1}{1-q^3z}-\frac{(q+1)^2}{1-q^2z}+\frac{q^2}{1-qz}.
\]
Exactly \(2q+2\) inclusion-maximal elementary abelian \(2\)-subgroups exist in \(G\): one of order \(q^4\), and \(2q+1\) of order \(q^3\). All are described explicitly below. In particular these are not asserted to be pairwise nonconjugate.

## Assumptions and scope
Throughout, \(k=\mathbb F_q\), \(q=2^f\) for \(f\ge1\). Write an element as \(I+N(a,b,c,d,e,h)\) where
\[
N(a,b,c,d,e,h)=\begin{pmatrix}0&a&d&h\\0&0&b&e\\0&0&0&c\\0&0&0&0\end{pmatrix}.
\]
An involution in the broad square-one sense includes the identity; a *nonidentity involution* has order exactly two. An elementary abelian subgroup is an abelian subgroup in which every element has square one, whether or not it is \(k\)-linear as a set.
Define the hyperbolic quadratic form on \(k^4\) with coordinates \((a,c,d,e)\) by \(Q(a,c,d,e)=ae+dc\); its polar form is
\[
\langle(a,c,d,e),(a',c',d',e')\rangle=ae'+a'e+dc'+d'c.
\]
Set \(W_0=\{(0,0,d,e):d,e\in k\}\), a totally singular two-plane. Write \(H\) for all \(I+N\) with \(a=c=0\); for each totally singular two-plane \(W\) define \(K_W\) to be all \(I+N\) with \(b=0\), \((a,c,d,e)\in W\), and arbitrary \(h\in k\). The inclusion-maximal elementary abelian subgroups are precisely \(H\) and the \(K_W\) for \(W\ne W_0\).

## Proof
**1. The square-one and commuting equations.** Since the characteristic is two, \((I+N)^2=I+N^2\). Direct matrix multiplication gives
\[
N^2=0\iff ab=bc=ae+dc=0.
\]
For two such matrices, multiplication in the unitriangular group is commutative exactly when
\[
ab'=a'b,\qquad bc'=b'c,\qquad ae'+dc'=a'e+d'c.\tag{1}\]
There are no further equations and the coordinate \(h\) is entirely free.

**2. Count tuples with a nonzero middle-edge coordinate.** For a commuting square-one tuple, regard \(A=(a_i)\), \(B=(b_i)\), \(C=(c_i)\) as vectors in \(k^m\). If \(B\ne0\), the first two equations of (1) imply \(A=\alpha B\), \(C=\gamma B\), since the vanishing of all two-by-two minors gives proportionality over the field. The individual constraints \(a_ib_i=b_ic_i=0\) for an index with \(b_i\ne0\) force \(\alpha=\gamma=0\). Conversely, these choices satisfy all equations for arbitrary \(d_i,e_i,h_i\). Therefore the contribution is \((q^m-1)q^{3m}\). This argument also covers \(m=0\), when the term vanishes.

**3. Count tuples with \(B=0\).** For each index, put \(w_i=(a_i,c_i,d_i,e_i)\in k^4\). Conditions (1) say precisely that every \(w_i\) is singular for \(Q\), and every pair is polar-orthogonal. The \(k\)-linear span of the \(w_i\) is then a totally singular subspace of this four-dimensional hyperbolic quadratic space. Such a subspace has dimension \(0,1\), or \(2\). Identify \(w=(a,c,d,e)\) with the matrix \(\begin{psmallmatrix}a&d\\c&e\end{psmallmatrix}\), whose determinant is \(Q(w)\) in characteristic two. The nonzero singular matrices have rank one and are parametrized by \(uv^T\), with \(u,v\ne0\), modulo the free common scaling. Thus there are \((q+1)^2\) singular projective points. Two independent rank-one matrices have every linear combination of rank at most one precisely when their images agree or their row spaces agree. Hence their maximal singular two-planes form two rulings, each with \(q+1\) members, giving \(2(q+1)\) in total.
For each fixed dimension-\(r\) subspace, the number of ordered spanning \(m\)-tuples is \(\prod_{j=0}^{r-1}(q^m-q^j)\) (the number of rank-\(r\) linear maps from \(k^m\) onto that space). Thus, including the unconstrained \(h_i\), the \(B=0\) contribution is
\[
q^m\bigl[1+(q+1)^2(q^m-1)+2(q+1)(q^m-1)(q^m-q)\bigr].\tag{2}
\]
Adding the contribution from Step 2 and expanding with \(t=q^m\) gives exactly the displayed formula for \(C_m(q)\). Expanding the right-hand side into exponentials also proves the generating function.

**4. Removing identity coordinates.** Every square-one element is either the identity or a nonidentity involution. In a commuting tuple, any position may be replaced by the identity freely. Hence \(C_m(q)=\sum_{j=0}^m\binom mj P_j(q)\). Binomial inversion, applied to each exponential term in the established expression for \(C_m(q)\), gives the formula for \(P_m(q)\). At \(m=0\) both counts equal one.

**5. All inclusion-maximal elementary abelian subgroups.** The subgroup \(H\) is elementary abelian of order \(q^4\) by (1). If an elementary abelian subgroup \(E\) contains an element with \(b\ne0\), its square-one equations force that element's \(a=c=0\), while commutation with it forces \(a=c=0\) for every element of \(E\). So \(E\subseteq H\). If every element of \(E\) has \(b=0\), its \((a,c,d,e)\) coordinates span a totally singular \(k\)-linear space, even if \(E\) was initially only \(\mathbb F_2\)-linear. Extend this span to a maximal singular two-plane \(W\); then \(E\subseteq K_W\). Every \(K_W\) is elementary abelian of order \(q^3\) by (1). Exactly the plane \(W_0\) gives \(K_{W_0}\subseteq H\); all other \(K_W\) contain an element with \(a\ne0\) or \(c\ne0\), so are not contained in \(H\). Distinct maximal singular two-planes cannot contain one another. Thus \(H\) and precisely the remaining \(2(q+1)-1=2q+1\) subgroups \(K_W\) are the complete list of inclusion-maximal elementary abelian subgroups. Their total is \(2q+2\).

## Verification
The standalone, dependency-free file `ut4_involution_checker.py` uses the exact coordinate identities and independently enumerates the finite-field models \(q=2\) and \(q=4\), where the latter is represented as \(\mathbb F_2[u]/(u^2+u+1)\). It directly tests the square-one and commuting equations for all group elements, enumerates the totally singular two-planes without invoking the ruling formula, and for \(q=2\) also checks all commuting triples and maximal cliques. Its successful terminal marker is `UT4_INVOLUTION_POLAR_CENSUS_OK`.
For \(q=2\), it finds \(C_1=28\), \(C_2=448\), \(C_3=6112\) and maximal subgroup orders \(16,8,8,8,8,8\). For \(q=4\), it finds \(C_1=496\), \(C_2=96256\), with ten totally singular two-planes. This is finite corroboration; the arbitrary-\(q\), arbitrary-\(m\) results follow from the proof above.

## Relationship to prior work
Bardakov, Vesnin and Yadav study automorphisms of unitriangular groups and give explicit conjugation formulas; these do not yield the involution-restricted tuple enumeration. Soffer studies general conjugacy and unrestricted commuting-pair upper bounds, not the square-one all-arity census. Kaur, Sharma and Singh's branching treatment of \(UT_4(q)\) concerns unrestricted commuting tuples in odd characteristic; its hypotheses exclude the characteristic-two setting. Majeed and Ramkumar study commuting graphs of \(UT_4(p)\), including maximal abelian-subgroup families. Their group-theoretic work is a close predecessor, but counting *all maximal elementary abelian* subgroups over every even extension field and *all arities* of commuting involutions is a distinct restriction and enumeration. Earlier results on maximum-order abelian subgroups are not claimed as new here. A comparable formula might remain in historical special-\(2\)-group or unitriangular literature; absence from inspected statements does not demonstrate absolute novelty.

## Limitations
The formulas concern the ordinary group \(UT_4(\mathbb F_{2^f})\) and tuples with square one, not unrestricted commuting tuples, larger unitriangular dimensions, arbitrary field characteristic, subgroup conjugacy classes or the full commuting-graph spectrum. The maximal elementary abelian count is for inclusion-maximal subgroups as distinct subsets, not their automorphism or conjugacy orbits. All counts are exact; finite computational checks alone do not establish the general claims. Full independent review and exhaustive publication-priority verification have not occurred.

## References
1. V. G. Bardakov, A. Yu. Vesnin, M. K. Yadav, *Class preserving automorphisms of unitriangular groups*, arXiv:1109.4710v1 (public September 22, 2011), https://arxiv.org/abs/1109.4710.
2. A. Soffer, *Upper bounds on the number of conjugacy classes in unitriangular groups*, arXiv:1411.5389v1 (public November 19, 2014), https://arxiv.org/abs/1411.5389.
3. J. Kaur, R. Sharma, S. Singh, *Branching rules and commuting probabilities for Triangular and Unitriangular matrices*, arXiv:2006.01493v1, https://arxiv.org/abs/2006.01493.
4. M. Majeed and P. B. Ramkumar, *Commuting Graph of Unitriangular Group UT(4;p)*, arXiv:2608.09235, https://arxiv.org/abs/2608.09235.
5. N. Snanou, *Counting formulas for certain p-subgroups of GL_n(Fp)* (2022), §§3–4. The conditions \(n\le p\) exclude \(n=4\), \(p=2\).
