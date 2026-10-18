# The unique Jacobian-syzygy jump on a nine-line realization curve

## Finding

Consider the ordered complex projective line arrangements whose **only** non-double intersection flats, in the indicated line labels, are
\[
\{1,2,3\},\ \{1,4,5\},\ \{1,6,7\},\ \{2,4,6\},\ \{3,5,7\},\ \{3,6,8\},\ \{4,7,9\},\ \{2,5,8,9\}.
\]
Their projective-equivalence realization space, with labels retained, is the punctured affine line
\[
S=\operatorname{Spec}\mathbf C[a,a^{-1},(a-1)^{-1},(a^2-a+1)^{-1}].
\]
For the defining degree-nine product \(f_a\) of the line equations, the minimal degree \(\operatorname{mdr}(f_a)\) of a nonzero homogeneous Jacobian relation is **exactly**
\[
\operatorname{mdr}(f_a)=
\begin{cases}4,&a=2,\\5,&a\in S(\mathbf C),\ a\ne2.\end{cases}
\]
Thus the degree-four Jacobian-syzygy jump is a unique point on the full labelled, fixed-lattice realization curve, rather than merely an observed difference between two chosen realizations.

## Assumptions and scope

The base field is \(\mathbf C\). A labelled arrangement has nine distinct projective lines \(L_i\subset\mathbf P^2\); triple or higher intersections are prescribed by the eight maximal flats above and there are no others. Projective equivalence must preserve all nine labels. The invariant \(\operatorname{mdr}(f)\) is the minimum nonnegative integer \(q\) for which polynomials \(A,B,C\) homogeneous of degree \(q\), not all zero, satisfy \(Af_x+Bf_y+Cf_z=0\), with \(f\) the reduced product of its nine linear forms. Multiplication of \(f\) by a nonzero scalar or a projective coordinate change does not change this integer.

Use dual points \(p_i=(u_i:v_i:w_i)\), representing \(L_i:\ u_ix+v_iy+w_iz=0\). Every realization is equivalent to **exactly one** ordered nine-point configuration below:
\[
\begin{array}{lll}
p_1=(1:0:0),&p_2=(0:1:0),&p_3=(1:a:0),\\
p_4=(0:0:1),&p_5=(a-1:0:a),&p_6=(0:1:1),\\
p_7=(1:1:1),&p_8=(a-1:a^2:a),&p_9=(a-1:a-1:a).
\end{array}
\]
Here \(a(a-1)(a^2-a+1)\ne0\). The statement is about this labelled fixed-lattice moduli space and this degree invariant, not about all nine-line lattices, unlabelled quotient moduli, or full minimal free resolutions.

## Proof

**1. Exact realization space.** The four dual points \(p_1,p_2,p_4,p_7\) are a projective frame because none of their triples is collinear. Normalize them to the displayed coordinate points and \((1:1:1)\). The given flats force \(p_3=(1:a:0)\), \(p_5=(1:0:b)\), and, by intersecting \(p_1p_7\) and \(p_2p_4\), \(p_6=(0:1:1)\). Collinearity of \(p_3,p_5,p_7\) gives \(ab-a-b=0\); hence \(b=a/(a-1)\). Intersecting the forced dual lines \(p_3p_6\) with \(p_2p_5\) determines \(p_8\), and intersecting \(p_4p_7\) with \(p_2p_5\) determines \(p_9\). Clearing nonzero scalar denominators yields exactly the nine displayed points. In particular, the frame leaves no residual projective automorphism, so \(a\) is an intrinsic normalized parameter of the labelled realization.

Among the \(\binom{9}{3}=84\) determinants of dual triples, precisely the eleven triples contained in the eight required flats vanish identically. Factoring each of the other \(73\) nonzero determinant polynomials over \(\mathbf Q[a]\) gives only the irreducible factors \(a\), \(a-1\), and \(a^2-a+1\), up to nonzero constants. Each of these factors occurs. The excluded values \(a=0,1\), or \(a^2-a+1=0\) create coincident lines or unintended incidences; the missing projective parameter \(a=\infty\) collapses \(p_3\) onto \(p_2\). Conversely all required flats and nine distinct lines occur for every other complex \(a\). These constructions are regular on the stated principal open set, giving the asserted realization curve. The exact finite determinant identity is independently reproducible using the enclosed `verify.py`.

**2. Degree-four logarithmic derivations.** Write \(f_a=\prod_{i=1}^9\ell_i\). For a reduced line product, a derivation \(D\) satisfies \(D(f_a)\in(f_a)\) if and only if \(D(\ell_i)\in(\ell_i)\) for every \(i\). Every degree-four syzygy \((A,B,C)\) has \(C\) divisible by \(z=\ell_4\). Subtracting \((C/z)\) times the Euler derivation \(x\partial_x+y\partial_y+z\partial_z\) gives a unique degree-four logarithmic derivation whose \(\partial_z\) coefficient is zero. Conversely, if such a logarithmic derivation satisfies \(D(f_a)=Hf_a\), subtracting \((H/9)\) times the Euler derivation recovers a Jacobian syzygy. Consequently the degree-four syzygy space is identified with the space of these normalized logarithmic derivations.

Tangency to \(\ell_1=x\), \(\ell_2=y\), \(\ell_5=(a-1)x+az\), and \(\ell_6=y+z\) forces normalized derivations to have the form
\[
D=x((a-1)x+az)U\,\partial_x+y(y+z)V\,\partial_y,
\]
where \(U,V\) are homogeneous quadratic polynomials. This uses the coprimality of \(x\) and \((a-1)x+az\), and of \(y\) and \(y+z\), throughout \(S\). There are twelve coefficients, in the ordered monomial basis \((x^2,y^2,z^2,xy,xz,yz)\) for \(U\), followed by the same basis for \(V\).

**3. Exact rank certificate.** The remaining tangency requirements concern \(\ell_3,\ell_7,\ell_8,\ell_9\). For a line \(ux+vy+wz=0\), substitute
\[
(x,y,z)=(-vT-wW,uT,uW)
\]
into \(u x((a-1)x+az)U+v y(y+z)V\). All four relevant coefficients \(u\) are nonzero on \(S\), so the substitution parametrizes the entire line. Equating the five coefficients of \(T^jW^{4-j}\), for \(j=0,1,2,3,4\), produces an explicit \(20\times12\) polynomial matrix \(M(a)\), with line blocks in the order \(3,7,8,9\).

Use zero-based row indices
\[
I=(3,5,2,6,4,11,7,8,12,17,13,18).
\]
The complete exact minor calculation gives
\[
\det M(a)_{I,\,0:11}=a^{14}(a-2)(a-1)^{20}(a^2-a+1)^3.
\]
Thus the matrix has column rank \(12\) for every permitted \(a\ne2\): no degree-four Jacobian relation exists at any such realization.

At \(a=2\), the column vector
\[
v=(-1,6,4,2,3,8,9,8,8,20,16,20)^{\mathsf T}
\]
obeys \(M(2)v=0\). In addition, taking zero-based row indices
\[
J=(1,2,3,4,5,6,7,11,12,13,18)
\]
and columns \(0,1,\ldots,10\) gives the nonzero \(11\times11\) determinant \(-5898240\). Therefore \(\operatorname{rank}M(2)=11\), and its degree-four kernel is one-dimensional. A syzygy of degree at most three would have at least three linearly independent degree-four polynomial multiples, contradicting this one-dimensionality. Hence \(\operatorname{mdr}(f_2)=4\), with no smaller relation.

**4. A uniform degree-five upper bound.** Every arrangement has a point where exactly the lines \(2,5,8,9\) concur. Move this point to \((1:0:0)\) and write \(f=g(y,z)h(x,y,z)\), where \(g\) is the product of four concurrent lines and \(h\) has degree five. Euler's identities for \(g\) and \(h\) imply that
\[
(xh_x-9h,\ yh_x,\ zh_x)
\]
is a homogeneous degree-five Jacobian relation for \(f\). It is nonzero because the other five lines are not all concurrent at that point, so \(h_x\ne0\). Consequently \(\operatorname{mdr}(f_a)\le5\) everywhere. Combined with the degree-four rank certificate, this gives the stated exact dichotomy. \(\square\)

## Verification

The enclosed standalone `verify.py` (Python 3 and SymPy) constructs every one of the \(84\) dual-point determinant polynomials, verifies exactly \(11\) identically zero minors and the allowed factors of the other \(73\), rebuilds the \(20\times12\) tangency matrix directly from the linear-form coefficients, evaluates its designated symbolic determinant, tests \(M(2)v=0\), and checks the displayed nonzero \(11\times11\) minor over \(\mathbf Q\). Run `python verify.py` from the directory containing the script. These exact polynomial equalities plus the proof above are the infinite-family certificate; finite sample computations alone would not suffice.

## Relationship to prior work

Dimca and Pokora, *A nine-line counterexample to a conjecture on the minimal degree of Jacobian relations* (arXiv:2607.01985v1, first posted 2026-07-02), construct **two** arrangements with exactly the labelled flats displayed above and calculate \(\operatorname{mdr}=4\) and \(5\) for those two special examples (their Lemma 3.1 and Proposition 4.1). They do not give the full labelled realization parameter space or establish that the degree-four drop occurs at exactly one moduli point. Their *On Ziegler pairs of line arrangements: from non-existence to abundance* (arXiv:2606.20421, especially its nine-line discussion and eleven-line family section) reports the original pair and other families, not this nine-line parameter-wide rank criterion. Fei Ye, *Classification of Moduli Spaces of Arrangements of 9 Projective Lines* (arXiv:1112.4306, Theorem 3.9), gives an important broader classification of connectedness/irreducibility alternatives for nine-line realization spaces; neither this connectedness classification nor its complement-topology conclusions imply the explicit \(S\) or the sharp numerical jump locus. The improvement here is the **global, fixed-lattice classification of the Jacobian-syzygy jump**, not the previously known two examples or the fact that a generic nine-line realization family can be irreducible.

## Limitations

The claim concerns complex characteristic zero, fixed **labels**, the one specified incidence lattice, and the minimum Jacobian-syzygy degree only. It does not classify the unlabelled quotient, syzygy modules or minimal resolutions at every parameter, singular degenerations at the excluded values, or positive-characteristic behavior. The explicit determinants are checkable symbolic identities, not an externally certified computation; independent audit has not been performed. Literature comparison includes the named closest primary texts and the searched research record, but cannot rule out every unpublished or unindexed equivalent result.

## References

1. A. Dimca and P. Pokora, *A nine-line counterexample to a conjecture on the minimal degree of Jacobian relations*, arXiv:2607.01985v1 (2026-07-02), Sections 3–7; https://arxiv.org/abs/2607.01985 .
2. A. Dimca and P. Pokora, *On Ziegler pairs of line arrangements: from non-existence to abundance*, arXiv:2606.20421 (2026), nine-line comparison and Sections on realization families; https://arxiv.org/abs/2606.20421 .
3. F. Ye, *Classification of Moduli Spaces of Arrangements of 9 Projective Lines*, arXiv:1112.4306 (2011), Theorem 3.9; https://arxiv.org/abs/1112.4306 .
