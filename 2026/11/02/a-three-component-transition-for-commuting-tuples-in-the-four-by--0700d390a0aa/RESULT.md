# A three-component transition for commuting tuples in the four-by-four triangular nilradical

## Finding

Let \(k\) be any field, let \(\mathfrak n_4(k)\) be the six-dimensional Lie algebra of strictly upper-triangular \(4\times4\) matrices, and for every integer \(m\ge1\) let \(\mathcal C_m\) denote the **reduced** algebraic variety of ordered, pairwise-commuting \(m\)-tuples of these matrices. The following geometric transition holds over every algebraically closed field, in **every characteristic**.

- For \(m=1\), \(\mathcal C_m\) is irreducible of dimension \(6\).
- For \(m=2\), \(\mathcal C_m\) has exactly two irreducible components, both of dimension \(9\). This two-tuple case is known in characteristic zero and is included for completeness, not claimed as new.
- For every \(m\ge3\), \(\mathcal C_m\) has **exactly three** irreducible components with dimensions \(4m\), \(3m+3\), and \(3m+3\). In particular, \(\mathcal C_3\) is equidimensional and \(\mathcal C_m\) is non-equidimensional for every \(m\ge4\).

The three components are defined explicitly in the proof, with a linear component, a generic proportional-column component, and a symplectic-isotropic component. Their descriptions hold after arbitrary field extension, so the components are geometrically irreducible and defined over the prime field.

As a companion arithmetic identity, for every prime power \(q\) and every \(m\ge1\), the number of commuting \(m\)-tuples over \(\mathbb F_q\) is
\[
\#\mathcal C_m(\mathbb F_q)=Q\bigl(Q^3+(Q-1)\bigl(q^2(2q+1)Q-q^4\bigr)\bigr),\qquad Q=q^m.
\]
The arithmetic identity is not asserted to be historically new: published unitriangular-group branching matrices already imply the odd-characteristic counts. The geometric **higher-arity component classification** is the novelty assessed here.

## Assumptions and scope

The input is a field \(k\) of arbitrary characteristic and integer \(m\ge1\); the geometric component claim is meant after extending to an algebraic closure. For \(i=1,\ldots,m\), write the matrix \(X_i\) using its six potentially nonzero entries in the ordered positions \((12),(23),(34),(13),(24),(14)\). Let the resulting six coordinate columns in \(k^m\) be denoted \(a,b,c,d,e,f\), respectively. For \(u,v\in k^m\), \(u\wedge v=0\) means that every alternating \(2\times2\) minor of the two-column matrix vanishes; the notation is valid in characteristic two. The final column \(f\) is central and free.

Commutativity of all pairs is equivalent, with no hypotheses on the characteristic, to
\[
 a\wedge b=0,\qquad b\wedge c=0,\qquad a\wedge e+d\wedge c=0.
\]
Here the last equality is an equality in \(\bigwedge^2 k^m\). Define the following closed subsets of the reduced solution locus:
\[
\begin{aligned}
 X_m&=\{a=c=0\},\\
 Z_m&=\{b=0,\ a\wedge e+d\wedge c=0\},\\
 Y_m&=\overline{\{b\ne0,\ (a,c)\ne(0,0),\ a=\alpha b,\ c=\gamma b,\ b\wedge(\alpha e-\gamma d)=0\}},
\end{aligned}
\]
where the closure is taken inside affine space and \(\alpha,\gamma\in k\); in the displayed dense set, \((\alpha,\gamma)\ne(0,0)\) is understood. These definitions are stable under base extension and all three subsets satisfy the commutation equations. The geometric classification is precisely that the maximal irreducible members of \(\{X_m,Y_m,Z_m\}\) are the components stated above.

## Proof

**1. Reduction of commutators.** The \((13)\), \((24)\), and \((14)\) matrix entries of \([X_i,X_j]\) are, respectively,
\[
 a_i b_j-a_j b_i,\quad b_i c_j-b_j c_i,\quad a_i e_j-a_j e_i+d_i c_j-d_j c_i.
\]
All other entries vanish. Hence the three exterior equations above are necessary and sufficient; the \(f_i\) coordinates are arbitrary.

**2. The linear component.** Setting \(a=c=0\) makes all equations vanish, so \(X_m\cong\mathbb A^{4m}\), with free columns \(b,d,e,f\). It is geometrically irreducible of dimension \(4m\).

**3. The generic proportional-column component.** On the open set \(b\ne0\), the first two exterior equations imply uniquely that \(a=\alpha b\) and \(c=\gamma b\). For \((\alpha,\gamma)\ne(0,0)\), the third equation becomes
\[
 b\wedge(\alpha e-\gamma d)=0.
\]
The linear map \(k^{2m}\to\bigwedge^2 k^m\), \((d,e)\mapsto b\wedge(\alpha e-\gamma d)\), has rank exactly \(m-1\) for every \(b\ne0\), because the indicated nonzero linear combination of \(d,e\) ranges over all of \(k^m\), and wedging with nonzero \(b\) has kernel \(kb\). Thus the solution space for \((d,e)\) has dimension \(m+1\). The base \((b,\alpha,\gamma)\in(k^m\setminus0)\times(k^2\setminus0)\) is irreducible of dimension \(m+2\), the solutions form a constant-rank vector bundle, and the central column \(f\) contributes \(m\) free coordinates. Its closure \(Y_m\) is therefore geometrically irreducible of dimension \(3m+3\), for \(m\ge2\). Every point in \(Y_m\) satisfies both of the closed rank conditions
\[
 \operatorname{rank}[a\ b\ c]\le1,\qquad \operatorname{rank}[b\ d\ e]\le2.
\]
The second condition follows on the dense open set since \(\alpha e-\gamma d\in kb\) with \((\alpha,\gamma)\ne(0,0)\).

**4. The symplectic component.** On the locus \(b=0\), the sole remaining equation is \(a\wedge e+d\wedge c=0\). Form vectors \(w_i=(a_i,c_i,d_i,e_i)\in k^4\) and equip \(k^4\) with the nondegenerate alternating bilinear form
\[
 \omega(w_i,w_j)=a_i e_j-a_j e_i+d_i c_j-d_j c_i.
\]
The equations say that the span of \(w_1,\ldots,w_m\) is totally isotropic. Every totally isotropic subspace of a four-dimensional symplectic space has dimension at most two and extends to a Lagrangian plane. The Lagrangian Grassmannian \(\mathrm{LG}(2,4)\) is geometrically irreducible of dimension three in every characteristic. The incidence space of a Lagrangian plane and \(m\) ordered vectors inside it is the total space of a rank-\(2m\) vector bundle over this Grassmannian, hence is irreducible of dimension \(2m+3\). Its projection onto the vector-tuples is surjective, and is generically one-to-one for \(m\ge2\): a generic tuple spans its unique Lagrangian plane. Since the base Grassmannian is proper, the image is closed; it is exactly the isotropic-tuple locus. Adding the free \(f\)-column proves that \(Z_m\) is geometrically irreducible of dimension \(3m+3\) for \(m\ge2\).

**5. Exhaustiveness.** Every solution with \(b=0\) lies in \(Z_m\). Every solution with \(b\ne0\) has \(a=\alpha b,c=\gamma b\); if both scalars vanish, it lies in \(X_m\), and otherwise it lies in the dense defining set of \(Y_m\). Hence the reduced variety is exactly \(X_m\cup Y_m\cup Z_m\).

**6. Which of the three are components?** If \(m\ge3\), the linear space \(X_m\) contains a point with \(b,d,e\) linearly independent, but this contradicts the closed rank-at-most-two condition on \(Y_m\); it also has points with \(b\ne0\), excluding containment in \(Z_m\). A generic point of \(Y_m\) has \(b\ne0\) and \((a,c)\ne(0,0)\), so \(Y_m\) lies in neither \(Z_m\) nor \(X_m\). Finally, \(Z_m\) contains points with \(b=0\), independent \(a,c\), and \(d=e=0\); these lie in neither \(X_m\) nor \(Y_m\), by the first rank condition above. Thus the three sets are precisely the irreducible components. When \(m=3\), all three dimensions equal twelve; for \(m\ge4\), \(4m>3m+3\).

For \(m=2\), the whole of \(X_2\) lies in \(Y_2\). To see this, at a point with \(a=c=0\) and \(b\ne0\), the one-dimensional quotient \(k^2/kb\) guarantees some \((\alpha,\gamma)\ne(0,0)\) with \(\alpha e-\gamma d\in kb\). Holding \(b,d,e,f\) fixed and setting \(a=t\alpha b,c=t\gamma b\) exhibits the point as a specialization from the dense defining set of \(Y_2\). At a point with \(a=b=c=0\), choose a nonzero vector \(v\in k^2\) proportional to \(e\) if \(e\ne0\), otherwise proportional to \(d\) if \(d\ne0\), otherwise arbitrary. Use \((\alpha,\gamma)=(1,0)\) in the first case or \((0,1)\) in the second, and set \(b=tv,a=t\alpha v,c=t\gamma v\). The defining equations hold for all \(t\), and the specialization at zero is the desired point. Therefore \(X_2\subset Y_2\); \(Y_2\) and \(Z_2\) do not contain one another by the same generic-point witnesses, and these are exactly the two nine-dimensional components. Finally, for \(m=1\) the commutation equations are vacuous and \(\mathcal C_1\cong\mathbb A^6\).

**7. Arithmetic companion.** Set \(Q=q^m\). Since \(f\) is arbitrary, multiply all reduced five-column counts by \(Q\). For \(b\ne0\) there are \(Q-1\) choices of \(b\). When \(\alpha=\gamma=0\), there are \(Q^2\) choices of \((d,e)\); for each of the \(q^2-1\) other pairs, the wedge equation has \(q^{m+1}=qQ\) solutions. This contributes
\[
 (Q-1)\bigl(Q^2+(q^2-1)qQ\bigr).
\]
For \(b=0\), the pair \((a,c)\) has rank \(0\), \(1\), or \(2\), in respectively \(1\), \((Q-1)(q+1)\), or \((Q-1)(Q-q)\) ways. The linear map \((d,e)\mapsto a\wedge e+d\wedge c\) has respective ranks \(0\), \(m-1\), and \(2m-3\) (the last rank is relevant only when \(m\ge2\)). Thus this locus contributes
\[
 Q^2+(Q-1)(q+1)qQ+(Q-1)(Q-q)q^3.
\]
Summing and multiplying by \(Q\) yields the displayed formula, also valid at \(m=1\) by direct inspection. Counting is for rational points of the reduced variety; nilpotent scheme structure, if any, is not asserted.

## Verification

The accompanying `verify.py` independently multiplies strictly upper-triangular matrices and exhaustively enumerates commuting ordered tuples over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\) for nine tractable configurations, including a full six-coordinate consistency check and a rank-three witness separating \(X_3\) from \(Y_3\). Genuine \(\mathbb F_4\) arithmetic is implemented with \(\mathbb F_2[z]/(z^2+z+1)\). Run `python3 verify.py` to reproduce the included `verification_output.txt`. The test marker is `UT4_COMMUTING_TUPLES_OK 9 FULL_6_COORDINATE_CHECK`. This finite enumeration supports but does not establish the infinite-family geometric theorem; the proof above is the general justification.

## Relationship to prior work

Rojas (2012, `arXiv:1211.2503v1`, primary MSC `17B10`) classifies faithful representations of six-dimensional nilpotent Lie algebras and records the strictly upper-triangular \(4\times4\) Lie algebra. Goodwin and Röhrle (2012, `arXiv:1209.1289v1`) analyze commuting *pairs* in Borel nilradicals, including type \(A_3\); their pair classification covers the characteristic-zero \(m=2\) component statement. Neither source proves the geometric classification for all \(m\ge3\).

Kaur, Sharma and Singh (2020, `arXiv:2006.01493v1`) calculate unitriangular-group branching matrices and commuting probabilities. Since commuting for unipotent matrices \(I+X\) is equivalent to commuting for their nilpotent parts \(X\), their branching matrix covers all odd-characteristic arithmetic tuple counts in principle. The closed rational-point identity above is therefore supplied for context and a characteristic-uniform check, **not** a claim of an independently novel enumeration. Guralnick and Ngo (2013, `arXiv:1308.2420v1`) treat commuting varieties inside the entire nilpotent cone, a distinct ambient object; their results do not directly imply the fixed-Borel-nilradical higher-tuple component count.

A search for descriptions phrased as higher commuting varieties, simultaneous centralizers, and nilpotent upper-triangular tuples found no earlier geometrically equivalent all-arity three-component classification. This is a best-knowledge novelty assessment, not a proof of priority.

## Limitations

The geometric claims concern **reduced** commuting varieties, not their defining schemes, nilpotent embedded components, cohomology, or intersections/multiplicities between irreducible components. The Lie algebra is specifically the six-dimensional nilradical of upper-triangular \(4\times4\) matrices. No analogous statement is made for larger matrix size. The finite-field count is not isolated as the original contribution because the literature has stronger odd-characteristic enumerative machinery. Independent mathematical checking and exhaustive historical publication-priority verification have not occurred.

## References

1. N. E. Rojas, *Faithful Representations of Minimal Dimension of 6-dimensional nilpotent Lie algebras*, `arXiv:1211.2503v1`, first public 2012-11-12, https://arxiv.org/abs/1211.2503.
2. S. M. Goodwin and G. Röhrle, *On commuting varieties of nilradicals of Borel subalgebras of reductive Lie algebras*, `arXiv:1209.1289v1`, first public 2012-09-06, https://arxiv.org/abs/1209.1289.
3. A. Kaur, S. Sharma and A. Singh, *Branching rules and commuting probabilities for Triangular and Unitriangular matrices*, `arXiv:2006.01493v1`, first public 2020-06-02, https://arxiv.org/abs/2006.01493.
4. R. M. Guralnick and N. V. Ngo, *Reducibility of nilpotent commuting varieties*, `arXiv:1308.2420v1`, first public 2013-08-11, https://arxiv.org/abs/1308.2420.
