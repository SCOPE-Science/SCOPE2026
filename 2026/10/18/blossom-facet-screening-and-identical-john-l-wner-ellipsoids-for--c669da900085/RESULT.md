# Blossom-facet screening and identical John–Löwner ellipsoids for integral and fractional one-factor polytopes

## Finding
For every even integer \(N\ge 6\), let \(E=\binom{[N]}2\), let \(B\in\mathbb R^{N\times |E|}\) be the unsigned vertex-edge incidence matrix of the complete graph \(K_N\), and use the standard coordinate Euclidean metric on \(\mathbb R^E\). Define the integral and fractional perfect-matching polytopes
\[
Q_N=\operatorname{conv}\{\mathbf1_M:M\text{ is a perfect matching of }K_N\},\qquad
F_N=\{x\in\mathbb R^E:Bx=\mathbf1_N,\ x_e\ge0\text{ for all }e\in E\}.
\]
These are *distinct*, full-dimensional polytopes in the common affine space \(H_N=\{x:Bx=\mathbf1_N\}\), of dimension \(d=N(N-3)/2\), yet **both have exactly the same unique John ellipsoid and exactly the same unique Löwner ellipsoid**. Both ellipsoids are Euclidean balls in \(H_N\), centered at \(c=(N-1)^{-1}\mathbf1_E\), with exact squared radii
\[
\boxed{r_N^2=\frac1{(N-1)(N-3)},\qquad R_N^2=\frac{N(N-2)}{2(N-1)}.}
\]
Precisely the \(|E|=N(N-1)/2\) nonnegativity facets of \(Q_N\) touch its John ball; *no blossom/odd-cut facet* touches it. All integral perfect-matching vertices, and no other points of \(F_N\), touch the enclosing Löwner sphere. The ratio of the radii is
\[
\frac{R_N}{r_N}=\sqrt{\frac{N(N-2)(N-3)}2}\sim 2^{1/4}d^{3/4}.
\]
The intrinsic Euclidean volumes are \(\pi^{d/2}r_N^d/\Gamma(1+d/2)\) and \(\pi^{d/2}R_N^d/\Gamma(1+d/2)\), respectively.

## Assumptions and scope
All statements are for *even* \(N\ge6\). Coordinate vectors have one coordinate for each unordered edge. For each edge \(e=\{u,v\}\), the corresponding column of \(B\) is \(\mathbf e_u+\mathbf e_v\). A perfect matching contains \(N/2\) edges. Inner and outer ellipsoids are taken in the Euclidean metric of the affine hull \(H_N\), not in the ambient space where they have zero ambient volume. For a set of vertices \(S\), \(\delta(S)\) is the edge cut with exactly one endpoint in \(S\). The standard complete-graph perfect-matching description (Edmonds; Lindzey, Corollaries 6.3–6.4) is
\[
Q_N=\{x\in H_N:x_e\ge0\ \forall e,\quad \sum_{e\in\delta(S)}x_e\ge1\ \forall\ S\subset[N]\text{ odd},\ 3\le|S|\le N-3\}.
\]
Its listed coordinate and nontrivial odd-cut inequalities are facets; the dimension is \(|E|-N\). The latter source is used for this established polyhedral description, not for the ellipsoid claim.

## Proof
**1. The affine metric and orthogonal projection.** Each vertex has \(N-1\) neighbors, and any two distinct vertices have one common edge. Thus
\[
BB^{\mathsf T}=(N-2)I_N+J_N,\quad
P=I_E-B^{\mathsf T}(BB^{\mathsf T})^{-1}B
\]
is the orthogonal projector onto the \(d\)-dimensional tangent space \(W=\ker B\). Since \((BB^{\mathsf T})^{-1}=(N-2)^{-1}(I_N-J_N/(2(N-1)))\), for edges \(e,f\)
\[
P_{ef}=\mathbf1_{e=f}-\frac{|e\cap f|-2/(N-1)}{N-2},\qquad
P_{ee}=p:=\frac{N-3}{N-1},\qquad P\mathbf1_E=0.
\]
The uniform vector \(c=(N-1)^{-1}\mathbf1_E\) satisfies \(Bc=\mathbf1_N\).

**2. The coordinate facets fix the John radius.** The distance from \(c\) within \(H_N\) to \(x_e=0\) is \(c_e/\|P\mathbf e_e\|=1/\sqrt{(N-1)(N-3)}=r_N\). Its orthogonal foot is
\[
q_e=c-\frac1{N-3}P\mathbf e_e.
\]
This has \(q_e(e)=0\); on edges \(f\ne e\) sharing a vertex with \(e\), \(q_e(f)=1/(N-2)\); on edges disjoint from \(e\), \(q_e(f)=(N-4)/((N-2)(N-3))>0\). Consequently \(q_e\) is in the relative interior of its coordinate facet once odd-cut inequalities are verified below.

**3. Every genuine blossom facet is strictly farther away.** For an odd set \(S\subset[N]\) with \(3\le s=|S|\le N-3\), write \(t=s(N-s)=|\delta(S)|\) and \(a_S=\mathbf1_{\delta(S)}\). An exact substitution into the projector gives
\[
\|Pa_S\|^2=\frac{2t(t-N+1)}{(N-1)(N-2)},\qquad
\langle a_S,c\rangle-1=\frac{t-N+1}{N-1}.
\]
Its affine-hull supporting-hyperplane distance from \(c\) is therefore
\[
\delta_S^2=\frac{(N-2)(t-N+1)}{2t(N-1)},\qquad
\frac{\delta_S^2}{r_N^2}=
\frac{(N-2)(N-3)(t-N+1)}{2t}.
\]
For \(3\le s\le N-3\), \(t\ge3(N-3)\). Since \((t-N+1)/t\) is increasing in \(t\),
\[
\frac{\delta_S^2}{r_N^2}\ge\frac{(N-2)(N-4)}3\ge\frac83>1.
\]
Thus the closed radius-\(r_N\) ball about \(c\) satisfies *every* odd-cut inequality strictly and is contained in \(Q_N\subset F_N\). Its only facet contacts with \(Q_N\) are the coordinate feet \(q_e\).

**4. A positive global John certificate.** Put \(u_e=(q_e-c)/r_N=-P\mathbf e_e/\sqrt p\), with \(\|u_e\|=1\). Assign the strictly positive John weight \(\lambda_e=p\) to each edge. Then, as operators on \(W\),
\[
\sum_{e\in E}\lambda_e u_e= -\sqrt p\,P\mathbf1_E=0,\quad
\sum_{e\in E}\lambda_e u_eu_e^{\mathsf T}
=\sum_e(P\mathbf e_e)(P\mathbf e_e)^{\mathsf T}=P=I_W.
\]
These are the exact first- and second-moment conditions characterizing the *global* unique John ellipsoid. In particular the result does not follow merely from maximizing a symmetric inscribed ball.

**5. The sharp outer ball and its global Löwner certificate.** Any \(x\in F_N\) has \(0\le x_e\le1\) (each edge belongs to two degree equations) and \(\sum_e x_e=N/2\). Hence
\[
\|x-c\|^2=\sum_ex_e^2-\frac{N}{2(N-1)}
\le\frac N2-\frac{N}{2(N-1)}
=\frac{N(N-2)}{2(N-1)}=R_N^2.
\]
Equality holds precisely when every coordinate is zero or one, which together with \(Bx=\mathbf1_N\) means \(x\) is a perfect-matching vertex. Thus both polytopes are enclosed by this ball, with exactly these contacts.

For a uniform random perfect matching \(M\), write \(v_M=\mathbf1_M\). Edge inclusion probabilities are \(1/(N-1)\); two distinct incident edges cannot both occur; disjoint edges both occur with probability \(1/((N-1)(N-3))\). Comparing all three orbit cases to the explicit entries of \(P\) gives
\[
\mathbb E[v_M]=c,\qquad
\mathbb E[(v_M-c)(v_M-c)^{\mathsf T}]=\frac{R_N^2}{d}P.
\]
Let \(z_M=(v_M-c)/R_N\), which are unit vectors in \(W\). Assign each perfect matching weight \(d/(N-1)!!>0\). The first weighted moment is zero and the second is \(P=I_W\); the outer Löwner contact criterion proves the ball is the *global* unique minimal-volume enclosing ellipsoid of both polytopes.

**6. The polytopes genuinely differ.** Put weight \(1/2\) on the three edges of each of two vertex-disjoint triangles, weight \(1\) on an arbitrary perfect matching of the remaining \(N-6\) vertices, and zero elsewhere. This lies in \(F_N\) but violates the odd-cut inequality of either triangle (the corresponding cut sum is zero). Thus \(Q_N\subsetneq F_N\) for every even \(N\ge6\). The two distinct convex bodies therefore have exactly the same two canonical ellipsoids.

## Verification
The included standard-library Python file `verify.py` reconstructs the incidence projection with exact rational arithmetic. For \(N=6,8,10\), it checks the projector identities, all coordinate-foot coordinates and norms, every permitted odd-cut hyperplane distance, the strict blossom gap, every perfect matching's outer-sphere norm, and the complete first/second moment conditions from all perfect matchings. It independently constructs a feasible fractional point violating a blossom inequality while lying strictly inside the Löwner sphere. These finite checks are reproducibility evidence, **not a proof for all** \(N\); the proof above is the infinite-family argument. Run `python verify.py` using Python 3 and its standard library only.

## Relationship to prior work
Gartsman and Linial (arXiv:2305.02113v1; publicly posted 2023-04-19) determine John and Löwner ellipsoids of the **metric polytope**, not the integral complete-graph perfect-matching polytope or the relaxation-invisibility statement here. Their study motivates applying exact intrinsic ellipsoidal geometry to other natural graph polytopes. Edmonds' classical perfect-matching description and Lindzey's explicit complete-graph dimension/facet corollaries are the polyhedral inputs. Behrend (arXiv:1301.7356v1) characterizes the **fractional** perfect matching polytopes' faces and vertices; that combinatorial description does not assert equality of the integral and fractional canonical ellipsoids. An ellipsoid computation for a polar model of the fractional one-factor polytope, even when available, concerns the relaxation and **does not show that the additional odd-cut facets fail to shrink the integral John ellipsoid**. The explicit strict blossom-distance estimate and integral contact certificate resolve that additional issue.

## Limitations
The assertion is confined to complete graphs of even order at least six, with the **intrinsic ambient-edge Euclidean normalization** above. It is not claimed for arbitrary noncomplete graphs, unequal edge weights, other norms, or all matching polytopes. The inequality-based analysis depends on the established complete-graph perfect-matching facet theorem and the standard John–Löwner contact characterizations. Searches of matching-polytope, optimal-design, and ellipsoid terminology and inspection of the cited primary mathematical texts have not established that no earlier equivalent computation exists. No independent publication-priority audit or independent proof validation is represented.

## References
1. Raziel Gartsman and Nati Linial, *On the Löwner-John Ellipsoids of the Metric Polytope*, arXiv:2305.02113v1, first public 2023-04-19, https://arxiv.org/abs/2305.02113 .
2. Nathan Lindzey, *Erdős–Ko–Rado for Perfect Matchings*, arXiv:1409.2057v1, first public 2014-09-06, Section 6, especially Corollaries 6.3–6.4, https://arxiv.org/abs/1409.2057 .
3. Roger E. Behrend, *Fractional Perfect b-Matching Polytopes. I: General Theory*, arXiv:1301.7356v1, first public 2013-01-30, https://arxiv.org/abs/1301.7356 .
4. Jack Edmonds, *Maximum matching and a polyhedron with 0,1-vertices*, Journal of Research of the National Bureau of Standards B 69B (1965); classical blossom/odd-set description. 
5. Fritz John, *Extremum problems with inequalities as subsidiary conditions* (1948), standard inner/outer ellipsoid contact criteria.
