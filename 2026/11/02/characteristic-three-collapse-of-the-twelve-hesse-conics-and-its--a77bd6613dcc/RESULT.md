# Characteristic-three collapse of the twelve Hesse conics and its triple-contact boundary

## Finding

Let \(R=\mathbb Z[\omega]/(\omega^2+\omega+1)\) and let \(\mathcal H_{12}(\lambda)\) be the divisor formed by the twelve explicitly indexed Hesse (Chilean) conics of Dimca–Pokora–Sticlaru [3, §5], with their original integral coefficients. Reduce at the unique prime \((3,\omega-1)\), and fix an algebraically closed field \(k\) of characteristic three and a parameter \(t\in k\setminus\{0,1\}\). The complete degree-24 special-fiber equation is, up to a nonzero scalar,

\[
\prod_{i=1}^{12}\overline f_i = Q_t^{\,9}\,r_1r_2r_3,
\quad Q_t=x^2+y^2+z^2+(t+1)(xy+xz+yz),
\]
\[
r_1=xy-tz^2,\qquad r_2=xz-ty^2,\qquad r_3=yz-tx^2.
\]

Precisely the nine conics with indices \(i\notin\{3,7,11\}\) become \(Q_t\); the remaining equations become \(r_1,r_2,-r_3\). The four reduced conics are distinct and smooth. Their union has exactly six singular points: three points

\[
A=(t:1:1),\qquad B=(1:t:1),\qquad C=(1:1:t)
\]

with three smooth branches each and pairwise intersection multiplicities \(2,2,3\), and three ordinary nodes \((1:0:0),(0:1:0),(0:0:1)\). Every three-branch point has \(\delta=7\). The reduced degree-eight curve therefore has total delta invariant \(24\), four rational irreducible components, and arithmetic genus \(21\).

The nine distinguished generic eightfold-point sections of [3, (5.2)] specialize in three groups of three at \(A,B,C\). Among the twelve remaining generic double-point sections of [3, (5.3)], nine specialize to \(P=(1:1:1)\), which is a **smooth** point of \(Q_t\) and of the reduced special fiber; the other three specialize to the coordinate vertices, one per vertex. These are collision counts of marked sections, **not** singular-scheme lengths or limits of intrinsic singularity schemes.

## Assumptions and scope

All geometric claims hold for **every** algebraically closed field \(k\) of characteristic \(3\) and **every** \(t\in k\setminus\{0,1\}\); there is no genericity assumption beyond these exclusions. Consider the published conic equations in \(R[\lambda, x,y,z]\), and, if a smooth generic twelve-conic configuration is desired, invert \(\lambda(\lambda^3-1)(\lambda^3+8)\). At the prime above three the latter exclusion becomes exactly \(t\ne0,1\). This is the reduction of an explicitly chosen integral equation, not a claim about a canonical characteristic-three Hesse configuration or its intrinsic enumerative objects.

For exact reproducibility, the twelve indexed quadratic polynomials \(f_i\) are encoded without denominators in `verify_hesse12.py`. Here are their complete published coefficients, writing \(\lambda\) for the base parameter:

\[
\begin{aligned}
f_1&=x^2+(\lambda+1)(\omega xy+\omega^2xz+yz)+\omega^2y^2+\omega z^2,\\
f_2&=x^2+(\lambda+1)(\omega^2xy+\omega xz+yz)+\omega y^2+\omega^2z^2,\\
f_3&=xy-\lambda z^2,\\
f_4&=x^2+(\omega\lambda+1)(xy+\omega xz+\omega yz)+y^2+\omega^2z^2,\\
f_5&=x^2+(\omega^2\lambda+1)(xy+\omega^2xz+\omega^2yz)+y^2+\omega z^2,\\
f_6&=x^2+(\omega\lambda+\omega^2)(xy+yz+\omega xz)+\omega y^2+z^2,\\
f_7&=xz-\lambda y^2,\\
f_8&=x^2+(\omega^2\lambda+\omega)(xy+yz+\omega^2xz)+\omega^2y^2+z^2,\\
f_9&=x^2+(\lambda+\omega^2)(xy+xz+\omega^2yz)+\omega y^2+\omega z^2,\\
f_{10}&=x^2+(\lambda+\omega)(xy+xz+\omega yz)+\omega^2(y^2+z^2),\\
f_{11}&=\lambda x^2-yz,\\
f_{12}&=x^2+(\lambda+1)(xy+xz+yz)+y^2+z^2.
\end{aligned}
\]

## Proof

**Exact specialization.** In characteristic three the Eisenstein equation becomes \((\omega-1)^2=0\), and the unique residue field map sets \(\omega\mapsto1\). Direct substitution in the twelve displayed formulas gives nine copies of \(Q_t\), together with \(r_1,r_2,-r_3\). Consequently the *scheme* (not merely its support) is the stated nonreduced divisor. The coefficient of \(x^2\) in \(Q_t\) and the distinct monomials in \(r_i\) show that these four factors are pairwise different for \(t\ne0,1\). The determinant of the Hessian matrix of \(Q_t\) is \(-(t-1)^3\) in characteristic three. Each \(r_i\) has nonzero Hessian determinant proportional to \(t\). As the characteristic is not two, all four plane conics are smooth.

**The triple contacts.** At \(A\), exactly \(Q_t,r_1,r_2\) vanish; their nonzero gradients are collinear. Cyclic symmetry gives the analogous statements at \(B,C\). In the affine chart \(z=1\), solving \(r_2=0\) gives \(x=ty^2\) and substituting into \(r_1\) gives the *exact* identity

\[
r_1\big|_{x=ty^2,z=1}=t(y^3-1)=t(y-1)^3.
\]

Since \(t\ne0\), the intersection multiplicity \(I_A(r_1,r_2)=3\). The conics \(r_1,r_2\) also meet transversely at \(E_x=(1:0:0)\). Bézout gives \(I(r_1,r_2)=4\), so these are all their intersection points. Cyclic permutation proves the corresponding statements for the other two pairs of \(r_i\).

The smooth conic \(Q_t\) meets \(r_1\) at the two distinct points \(A,B\). Tangency gives local intersection multiplicity at least two at each. Bézout forces equality at both and excludes any other intersection. Cyclically, \(Q_t\) meets \(r_2\) with multiplicity two at \(A,C\), and \(r_3\) with multiplicity two at \(B,C\). Thus the *complete* singular support is precisely \(A,B,C,E_x,E_y,E_z\). Since each reduced branch is smooth, the local delta invariant at a three-branch point is the sum of its three pairwise intersection multiplicities: \(2+2+3=7\). Each coordinate node contributes one. The arithmetic genus identity

\[
p_a(C_{\mathrm{red}})=\frac{(8-1)(8-2)}2=21=3\cdot7+3-4+1
\]

also checks the intersection accounting; it is not used in place of Bézout for completeness.

**Specialized marked sections.** The nine eightfold sections are the projective points

\[
\begin{gathered}
(t:1:1),\ (1:t:1),\ (1:1:t),\
(t:\omega:\omega^2),\ (\omega^2:t:\omega),\ (\omega:\omega^2:t),\\
(t:\omega^2:\omega),\ (\omega:t:\omega^2),\ (\omega^2:\omega:t).
\end{gathered}
\]

Setting \(\omega=1\) gives exactly three at each of \(A,B,C\). The twelve double-point sections of [3, (5.3)] consist of the three coordinate vertices and nine further points whose entries belong to \(\{1,\omega,\omega^2\}\) (one point \((1:1:1)\) included); all nine further points reduce to \(P=(1:1:1)\). At \(P\), each residual conic has equation value \(1-t\ne0\), whereas \(Q_t(P)=0\) and the gradient of \(Q_t\) is nonzero for \(t\ne1\). Thus \(P\) is a smooth special-fiber support point. Projective coordinates all contain a unit, so the marked specializations are well defined without arbitrary rescaling.

## Verification

Run `python3 verify_hesse12.py` with SymPy. It checks the twelve equation specializations identically over \(\mathbb F_3[t]\), nonzero smoothness determinants, point incidences, exact tangent identities, the cubic intersection calculation, transverse nodes, all 21 coordinate specializations, and genus arithmetic. Its success marker is `HESSE_12_CONICS_CHAR3_NINEFOLD_COMPONENT_THREE_DELTA7_TRIPLES_OK`. The exhaustive geometric conclusion comes from the explicit elimination and Bézout argument above, not from a finite-field sample or a computer timeout.

## Relationship to prior work

The 12-conic configuration and its complex geometric origins are due to Kohel–Roulleau–Sarti [1] and Dolgachev–Laface–Persson–Urzúa [2]. The twelve precise integral conic equations, the nine eightfold points, and the twelve double points are from Dimca–Pokora–Sticlaru [3, §5], whose work studies complex Alexander polynomials and complex-parameter degenerations. These inputs, and the abstract notions of Hesse configurations, are not claimed as new. The present claim is the reduction at the ramified prime above three and its complete multiplicity, local-contact, and marked-point behavior. Related complex geometry does not imply the stated characteristic-three contact multiplicity or the collision of nine originally singular labels at a smooth reduced point.

## Limitations

The theorem concerns only this explicitly indexed integral equation and only the fibers \(t\ne0,1\) in characteristic three. It does not classify other integral presentations, stable models, positive-characteristic intrinsic inflection or sextactic schemes, or all degenerations of the Halphen pencil. The marked-point collision weights are not multiplicities of the intrinsic Jacobian scheme. The historical originality comparison is based on accessible primary literature and mathematical-record searches; absence of an indexed match is not proof that no earlier calculation exists. Independent external mathematical validation has not been performed.

## References

[1] D. Kohel, X. Roulleau, A. Sarti, *A special configuration of 12 conics and generalized Kummer surfaces*, first public arXiv posting 2020-04-23, https://arxiv.org/abs/2004.11421 (particularly construction and 12-conic sections).

[2] I. Dolgachev, A. Laface, U. Persson, G. Urzúa, *Chilean configuration of conics, lines and points*, first public arXiv posting 2020-08-21, https://arxiv.org/abs/2008.09627 (the paper states that its surface geometry works in characteristic different from 2 and 3).

[3] A. Dimca, P. Pokora, G. Sticlaru, *On the Alexander polynomials of conic-line arrangements*, first public arXiv posting 2023-05-02, https://arxiv.org/abs/2305.01450, §5 (the displayed equations and the marked points).
