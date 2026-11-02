# All-arity anticommuting two-by-two matrix varieties and their finite-field census

## Finding

For a field \(k\) of characteristic different from two, let \(\mathcal A_m(k)\) be the **reduced** algebraic variety of ordered \(m\)-tuples \((X_1,\ldots,X_m)\) of \(2\times2\) matrices satisfying \(X_iX_j+X_jX_i=0\) for every \(i<j\). All assertions on irreducible components below are geometric (after extension to an algebraic closure). The components are defined over \(k\).

For \(m=1\), there is one component, an affine four-space. For \(m=2\), there are four components: two coordinate affine four-spaces, one four-dimensional two-support component, and one five-dimensional traceless orthogonality component. For \(m=3\), there are seven components: three coordinate affine four-spaces, three four-dimensional two-support components, and one six-dimensional traceless orthogonality component.

For every \(m\ge4\), there are exactly
\[
\binom m2+\binom m3+2m
\]
geometrically irreducible components: \(m\) coordinate affine four-spaces, \(\binom m2\) two-support components of dimension four, \(\binom m3\) traceless three-support components of dimension six, and \(m\) traceless degenerate-plane components of dimension \(m+2\). The variety is equidimensional **exactly when \(m=1\)**: at \(m=2\) dimensions four and five coexist, and for every \(m\ge3\) the four-dimensional coordinate components coexist with higher-dimensional components. In particular, for \(m=4\) there are \(4+6+4+4=18\) components, of dimensions four and six.

For each odd prime power \(q\), write \(N_m(q)=\#\mathcal A_m(\mathbb F_q)\) (and \(N_0(q)=1\)). Then for every \(m\ge0\):
\[
\boxed{N_m(q)=\bigl(q+1+m(q^2-1)\bigr)q^m-q
 +m q(q-1)(q^2-1)
 +\binom m2 q^2(q+1)(q-1)^2
 +\binom m3 q(q+1)(q-1)^4.}
\]
For each fixed odd \(q\), the sequence \(m\mapsto N_m(q)\) has a **minimal** constant-coefficient linear recurrence of order six, with characteristic polynomial
\[
\boxed{(T-q)^2(T-1)^4.}
\]
The finite-field count and minimal recurrence are genuinely arithmetic statements, not claims of previously unknown structure for the separate orthogonal-frame subvariety.

## Assumptions and scope

The base field has characteristic other than two, and tuple length is any nonnegative integer for the point-count statement and any positive integer for the geometric variety. For each \(X\in M_2(k)\), write uniquely \(X=aI+v\), where \(a=\operatorname{tr}(X)/2\) and \(v\in\mathfrak{sl}_2(k)\). Identify a trace-zero matrix with \(v=(z,x,y)\) through
\[
v=\begin{pmatrix}z&x\\y&-z\end{pmatrix},\qquad Q(v)=z^2+xy,
\qquad B(v,w)=zz'+(xy'+x'y)/2.
\]
Thus \(B\) is a nondegenerate symmetric bilinear form on a split three-dimensional quadratic space and \(v^2=Q(v)I\).

For \(m\ge4\), the traceless three-support component indexed by a three-element set \(J\) is the locus of tuples supported on \(J\), with the three trace-zero vectors pairwise \(B\)-orthogonal. The degenerate-plane component indexed by \(h\) is the closed image of the incidence variety of an isotropic projective line \(\ell\) with \(v_h\in\ell^\perp\) and \(v_i\in\ell\) for all \(i\ne h\). The latter has dimension \(1+2+(m-1)=m+2\).

The two-support component indexed by \(\{i,j\}\) is the closure of the locus with all other matrices zero, with \(a_i,a_j\ne0\), and with \(v_i=a_i u,\ v_j=-a_j u,\ Q(u)=1\). This is irreducible of dimension four, because \(Q(u)=1\) is a smooth geometrically irreducible affine quadric surface. Coordinate components consist of arbitrary matrices on exactly one allowed coordinate, other coordinates zero.

## Proof

**Reduction to a quadratic system.** Substituting \(X_i=a_iI+v_i\) and using \(v_iv_j+v_jv_i=2B(v_i,v_j)I\) shows that anti-commutation is equivalent to
\[
a_i v_j+a_j v_i=0,\qquad a_i a_j+B(v_i,v_j)=0\quad(i<j).
\]
If three distinct scalars \(a_i,a_j,a_h\) were nonzero, the first equations would give \(v_j=-(a_j/a_i)v_i\) and \(v_h=-(a_h/a_i)v_i\); the \((j,h)\)-equation then gives \(-2a_ja_hv_i/a_i=0\), hence \(v_i=v_j=v_h=0\), contradicting the scalar equations \(a_ia_j=0\). Thus at most two \(a_i\) are nonzero. If exactly one, the first equations force every other \(v_j\) to vanish. If exactly two, the equations give the stated common vector \(u\) of norm one. If all scalars vanish, the variety is exactly the orthogonal-frame variety \(H_m\) cut out by \(B(v_i,v_j)=0\).

**Traceless components.** In the split three-dimensional quadratic space, a pairwise orthogonal list has at most three linearly independent vectors. Three independent vectors must be nonisotropic and every further vector vanishes. Thus all rank-three tuples belong to a three-support \(H_3\). A nondegenerate rank-two span similarly permits exactly two nonzero vectors, hence lies in some three-support \(H_3\). A degenerate rank-two span has a unique isotropic radical line \(\ell\), is exactly \(\ell^\perp\), and at most one vector has nonzero image in \(\ell^\perp/\ell\), because the induced one-dimensional form is nondegenerate. Such a tuple therefore lies in an indexed degenerate-plane incidence image. Rank-one lists lie either in these images (isotropic line) or in a three-support \(H_3\) (anisotropic, only one vector nonzero). This proves exhaustive coverage for \(m\ge4\).

The full-rank stratum of \(H_3\) is an open locus in the successive choice of a nonisotropic \(v_1\), a nonisotropic \(v_2\in v_1^\perp\), and a nonzero \(v_3\in\langle v_1,v_2\rangle^\perp\). It is irreducible of dimension \(3+2+1=6\). It is dense in \(H_3\): for a degenerate rank-two configuration, choose a nonisotropic \(r\) and hyperbolic pair \(\ell,\ell'\) inside \(r^\perp\). If two entries have limits \(c\ell,d\ell\) with \(c,d\ne0\), replace them by \(c\ell+t\ell'\) and \(d\ell-t(d/c)\ell'\), which remain orthogonal and are independent for \(t\ne0\); retain \(r\) as the third entry. If the second radical limit is zero but the first is \(c\ell\) with \(c\ne0\), use \(c\ell+t\ell'\) and \(tc\ell-t^2\ell'\), which are independent and mutually orthogonal for \(t\ne0\). If both limits are zero, use \(t(\ell+\ell')\) and \(t(\ell-\ell')\), another independent orthogonal pair. Rank-one isotropic triples arise by first adding \(tw\) to a nonzero coordinate along \(\ell\), with \(w\in\ell^\perp\) anisotropic (and if necessary adding a second \(t\ell\) coordinate); the resulting rank-two degenerate triples tend to the original. Rank-one anisotropic triples are covered by the preceding zero-limit construction, and the zero triple is a limit of scaled orthogonal bases. Hence \(H_3\) is irreducible. Likewise \(H_2\) is the irreducible hypersurface of dimension five defined by the nondegenerate bilinear equation \(B(v_1,v_2)=0\).

For any chosen isotropic \(\ell\), the degenerate-plane incidence conditions are linear and form a rank \(m+1\) vector bundle over the smooth irreducible projective conic of isotropic lines. Its image in affine space is closed because the projective incidence projection is proper. Its general point has exactly one nonradical coordinate and at least two nonzero coordinates on \(\ell\), recovering uniquely both \(\ell\) and the distinguished index, so its image is irreducible of dimension \(m+2\). Generic three-support rank-three points lie in no such incidence image, and generic incidence points cannot lie on any three-support variety when \(m\ge4\). Nonzero scalar traces separate the two-support components from the traceless ones. The two-support components are mutually distinct, as are the coordinate components; a coordinate generic invertible matrix cannot belong to the closure of a two-support component because its matrix at that coordinate would have determinant zero there. These generic witnesses prove that the listed closed irreducible loci are precisely the maximal components. For \(m=2\) and \(m=3\), the same scalar partition together with irreducibility of \(H_2\) and \(H_3\) gives the stated classifications.

**Finite-field counts.** Let \(H_m(q)\) be the number of pairwise-orthogonal ordered \(m\)-tuples in the trace-zero quadratic three-space. Over \(\mathbb F_q\), \(q\) odd, there are \(q+1\) isotropic projective lines and \(q^2-1\) nonzero isotropic vectors. The rank-zero count is one, and the rank-one isotropic count is \((q+1)(q^m-1)\). The rank-one anisotropic count is \(m q^2(q-1)\).

An ordered pair of nonzero anisotropic orthogonal vectors has count
\[
T_2=q(q-1)^3(q+1).
\]
Indeed, the number of vectors of norm \(t\ne0\) is \(q^2+q\chi(t)\): for each \(z\), the equation \(xy=t-z^2\) has \(q-1\) or \(2q-1\) solutions according as the right side is nonzero or zero. For square \(t\), the perpendicular quadratic plane is hyperbolic and has \((q-1)^2\) anisotropic vectors, whereas for nonsquare \(t\) it is anisotropic and has \(q^2-1\). Summation over the \((q-1)/2\) values of each square class gives \(T_2\). Any independent orthogonal triple adds \(q-1\) choices for the third vector, giving \(T_3=q(q-1)^4(q+1)\).

The rank-two nondegenerate tuples contribute \(\binom m2T_2\). For a rank-two degenerate span there is a unique isotropic radical line, a unique exceptional index outside it, \(q^2-q\) choices for its vector, and \(q^{m-1}-1\) choices for the remaining line-valued list not identically zero. This contributes \(m(q+1)(q^2-q)(q^{m-1}-1)=m(q^2-1)(q^m-q)\). Rank-three tuples contribute \(\binom m3T_3\). Thus
\[
\begin{aligned}
H_m(q)={}&1+(q+1)(q^m-1)+m q^2(q-1)\\
&+\binom m2 q(q-1)^3(q+1)\\
&+m(q^2-1)(q^m-q)+\binom m3 q(q-1)^4(q+1).
\end{aligned}
\]
Exactly-one-nonzero-trace tuples contribute \(m(q-1)q^3\). Exactly-two-nonzero-trace tuples contribute \(\binom m2(q-1)^2(q^2+q)\), because \(Q(u)=1\) has \(q^2+q\) rational points. Adding to \(H_m(q)\) and simplifying yields the displayed formula for \(N_m(q)\). Finally, in that formula the \(q^m\) part has polynomial coefficient \(q+1+m(q^2-1)\) of degree one in \(m\), while the remaining \(1^m\) part has polynomial coefficient of degree three, whose leading coefficient is \(q(q+1)(q-1)^4/6\). Nonzero coefficients and linear independence of generalized exponential-polynomial sequences imply that the minimal characteristic polynomial is exactly \((T-q)^2(T-1)^4\).

## Verification

A standalone script `check.py` builds finite-field arithmetic and tests original equations directly. It checks the original trace-free bilinear equations by recursive enumeration for 16 field/arity configurations, and the original matrix-product anti-commutation equations by direct enumeration for seven configurations; a separate anticommutator linear-map rank method verifies the pair count over the nonprime field \(\mathbb F_9\). The fields are \(\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_9\), with \(\mathbb F_9\) implemented as \(\mathbb F_3[i]/(i^2+1)\). It prints `ANTICOMMUTING_M2_ALL_ARITIES_ODD_OK` on success. These finite checks support but cannot prove the arbitrary-field geometry or all-arity formula.

## Relationship to prior work

Hrubeš (2014) studies arbitrary families of anticommuting matrices, with rank bounds and Clifford-algebra motivations, but does not classify the reduced tuple varieties or count finite-field tuples. Chen and Wang (2018) completely classify the *pair* anti-commuting variety of square matrices; the \(m=2\) case above is covered and is not claimed novel. Casabella and Sammartano (2025), Theorem 5.8, classify irreducible components of the orthogonal-frame variety in arbitrary dimension; the classification of the *standalone traceless locus* \(H_m\), including its three-support and degenerate-plane components, is therefore prior work. The present claim is the combined full-matrix all-arity component classification, an explicit **exact** finite-field enumeration of all anti-commuting tuples, and the sharp minimal order-six arithmetic recurrence. The orthogonal-frame classification does not itself count points, and the 2018 pair theorem does not handle arbitrary arity. Ngo (2012) treats commuting (rather than anti-commuting) tuples. Iosevich–Senger (2008) and Vinh (2008) address asymptotic orthogonal-system counts in sufficiently large subsets, not the exact three-dimensional, all-length, unrestricted tuple census. A foundational source is Hrubeš's 2014 paper (primary MSC 15A99); the earlier orthogonality and commuting papers are contextual comparisons. No exhaustive publication-priority claim is made.

## Limitations

The statements exclude characteristic two. The geometric results apply to the **reduced** varieties, not potential nilpotent scheme structure of the raw quadratic equations. The theorem is specific to \(2\times2\) matrices; no general matrix-size classification is asserted. The geometric structure of the standalone trace-free orthogonal frames and the two-matrix case are already known, and the main incremental content should be judged against them. Independent verification and exhaustive historical priority review have not been performed.

## References

- P. Hrubeš, *On families of anticommuting matrices*, arXiv:1412.5893, first posted 2014-12-18 (primary MSC 15A99); full text includes the rank bounds and explicit dimension-two discussion.
- A. Iosevich and S. Senger, *Orthogonal systems in vector spaces over finite fields*, arXiv:0807.0592, first posted 2008-07-03.
- L. A. Vinh, *On the number of orthogonal systems in vector spaces over finite fields*, Electron. J. Combin. 15 (2008), N32; arXiv:0807.2690, first posted 2008-07-17.
- N. V. Ngo, *Commuting varieties of \(r\)-tuples over Lie algebras*, arXiv:1209.1659 (2012).
- X. Chen and W. Wang, *Anti-commuting varieties*, arXiv:1805.00378 (2018).
- L. Casabella and A. Sammartano, *The variety of orthogonal frames*, arXiv:2512.25058 (2025), especially Theorem 5.8.
