# Paired saddle three-cycles across a sharp border collision in the noninvertible planar normal form

## Finding

A complete primitive-period-three orbit classification holds throughout a four-parameter, two-saddle, noninvertible border-collision family with both branch determinant magnitudes below one. Let \(0<d,q<1\), \(\ell>1+d\), and \(s>1-q\). Define
\[
K=(d+\ell)(s-1)-(1-d)(1+q),\qquad
s_*=1+\frac{(1-d)(1+q)}{d+\ell}.
\]
For the continuous piecewise-affine map defined below, the number of **distinct primitive period-three orbits**, counting a cycle once irrespective of its starting point, is exactly zero if \(s<s_*\), exactly one if \(s=s_*\), and exactly two if \(s>s_*\).

At equality the unique period-three orbit visits the switching line exactly once. Above equality the two orbits have strict symbolic itineraries \(LLR\) and \(LRR\), up to cyclic permutation; both are saddles. The \(LLR\) cycle has one multiplier below \(-1\) and one in \((0,1)\); the \(LRR\) cycle has one multiplier above \(1\) and one in \((0,1)\). In particular, no strict attracting period-three orbit occurs in this entire parameter family. The threshold lies strictly above \(1\), independently of the two-saddle right-branch admissibility lower bound \(1-q\).

## Assumptions and scope

The phase space is all of \(\mathbb R^2\). The map is
\[
F(x,y)=\begin{cases}
(\ell x+y+1,-dx),&x\le0,\\
(-sx+y+1,qx),&x\ge0.
\end{cases}
\]
Both formulae agree on the line \(x=0\). The parameters are real and satisfy \(0<d,q<1\), \(\ell>1+d\), and \(s>1-q\). Its left and right branch matrices are
\[
L=\begin{pmatrix}\ell&1\\-d&0\end{pmatrix},\qquad
R=\begin{pmatrix}-s&1\\q&0\end{pmatrix}.
\]
The branch determinants have opposite signs, so this is a noninvertible orientation-mixing case. The parameter inequalities make both fixed points saddles. We classify **all**, not merely attracting or numerically visible, prime-three orbits; the word for an orbit is read from the signs of its successive first coordinates. A switching-line orbit is counted only once.

## Proof

Write \(z_j=F^j(z_0)\) and denote the first coordinate of \(z_j\) by \(x_j\). Every primitive three-word using two letters is, up to rotation, either \(LLR\) or \(LRR\). For an all-one-letter word the relevant affine branch has no eigenvalue that is a nontrivial cubic root of unity (both branch matrices have real hyperbolic eigenvalues under the assumptions). Consequently an all-one-letter solution of the third-iterate equation is only a fixed point, not a primitive three-cycle.

Introduce the polynomials
\[
\begin{aligned}
B&=dq+d+\ell q+\ell s+s-1,\\
C&=d^2+d\ell-d+\ell^2+\ell+1,\\
H&=q^2+qs+q+s^2-s+1,\\
D_L&=d^2q-d\ell+ds-\ell^2s+\ell q-1,\\
D_R&=dq^2-ds-\ell q-\ell s^2+qs+1.
\end{aligned}
\]
Solving the two affine three-cycle equations gives the following first-coordinate triples, starting at the left point:
\[
LLR:\quad (x_0,x_1,x_2)=\frac{(B,K,-C)}{D_L},\qquad
LRR:\quad (x_0,x_1,x_2)=\frac{(H,-K,-B)}{D_R}.
\]
The second coordinate of \(z_0\) is \(q x_2\) in both words. These expressions follow by multiplying the branch matrices and solving the associated two-by-two linear system; direct substitution into three original-map updates also verifies them. When \(D_L=0\) or \(D_R=0\), the corresponding affine system is inconsistent, because the uncancelled first-coordinate numerator \(B\) or \(H\) is strictly positive. Such singular algebraic cases therefore create no additional or continuous families of period-three points.

We check all denominator and itinerary signs, including the boundary. First \(C>0\) and \(H>0\), while \(B\) is increasing in \(\ell,s\) and at their lower limits satisfies \(B=(1-q)+d(2+q)>0\). The exact identity \(K=(d+\ell)(s-s_*)\) shows that \(K\) has the sign of \(s-s_*\), and \(s_*>1\). If \(K\ge0\), then \(s\ge s_*>1\). In this range \(D_L<0\): it decreases with \(s\), and at \(s=1\) it is bounded above by \(d^2-d\ell+d-\ell^2+\ell-1<0\), using \(q<1\) and \(\ell>1+d\). Also
\[
D_R\big|_{s=s_*}=
\frac{(1+q)(dq-\ell)(d^2+d\ell-d+\ell^2+\ell+1)}{(d+\ell)^2}<0,
\]
and \(D_R\) decreases for \(s\ge s_*>1\), because its derivative with respect to \(s\) is \(-d-2\ell s+q<0\). Thus for \(K>0\) both candidate triples have exactly their prescribed strict signs and give two distinct cycles. For \(K<0\), the \(LLR\) candidate violates the itinerary either at \(x_0\) (if \(D_L\ge0\)) or at \(x_1\) (if \(D_L<0\)); the same argument with \(D_R\) applies to \(LRR\). At \(K=0\), both give the same genuine orbit with \(x_0<0\), \(x_1=0\), and \(x_2>0\). To verify that the two formulas describe **one**, not two, switching orbits, direct expansion gives
\[
\begin{aligned}
B D_R-H D_L&=K(-dqs-d+\ell q^2-\ell s-q-s^2),\\
-C D_R+B D_L&=K(d^2+d\ell s+dq-\ell^2q+\ell+s).
\end{aligned}
\]
Both denominators are strictly negative at equality, so the initial and third first coordinates agree for the two candidate expressions; because the initial second coordinate is \(qx_2\), the entire initial points coincide. This proves the complete census.

For the spectra of the two strict cycles, their three-step derivatives are, up to cyclic order, \(RL^2\) and \(R^2L\). Their traces and determinants are
\[
\begin{array}{c|cc}
&\operatorname{tr}&\det\\ \hline
LLR &-d\ell+ds-\ell^2s+\ell q&-d^2q\\
LRR &ds+\ell q+\ell s^2-qs&dq^2.
\end{array}
\]
For \(LRR\), its characteristic polynomial at \(1\) equals \(D_R<0\), its trace is positive, and its determinant belongs to \((0,1)\). Thus one multiplier exceeds \(1\), with the other strictly between \(0\) and \(1\).

For \(LLR\), write \(P_L(-1)=1+\operatorname{tr}(RL^2)-d^2q\). The function \(P_L(-1)\) is decreasing in \(s\), since its slope is \(d-\ell^2<0\). At \(s=s_*\), put \(u=\ell-1-d>0\), \(v=1-q>0\). Direct polynomial expansion gives
\[
\begin{aligned}
(d+\ell)P_L(-1)\big|_{s=s_*}
={}&-1+d-5d^2-4d^3\\
&-(4+6d+5d^2)u-(4+3d)u^2-u^3\\
&-vd\big[(3+d-d^2)+(3+d)u+u^2\big]<0.
\end{aligned}
\]
The strict inequality uses only \(0<d<1\), \(u>0\), and \(v>0\). Hence for \(s>s_*\) the characteristic polynomial of \(RL^2\) is negative at \(-1\). Its determinant lies in \((-1,0)\), giving a negative multiplier below \(-1\) and a positive multiplier in \((0,1)\). At the switching equality \(s=s_*\), ordinary derivative multipliers are not asserted because the orbit visits the nonsmooth line. This completes the proof.

## Verification

The accompanying `verify_period3.py` uses only standard-library exact rational arithmetic. It checks both proposed cycle-coordinate formulas against three applications of the original map, the two trace/determinant identities and their strict spectral inequalities, and the unique switching orbit at the threshold. It verifies 444 exact candidate identities on a deterministic rational parameter grid, including below, at and above the threshold. The universal classification and inequalities are established by the preceding algebra, not by finite sampling. Reproduce with `python3 verify_period3.py`.

## Relationship to prior work

The map itself and its four-parameter border-collision setting are established; see Ghosh–McLachlan–Simpson (2024), especially Eq. (1.1), Secs. 3–4, and Sec. 8. Their study focuses on chaotic-attractor component bifurcations, renormalization, and some period-two and period-four solutions, rather than a complete primitive-three census in the above determinant-sign regime. Their Proposition 10.1 gives a skew-tent reduction on a special equal-stable-eigenvalue locus, which can imply low-period statements on that lower-dimensional locus but not on the full open four-parameter domain. Glendinning–Simpson (2020), Sec. 8, records a pair of period-three itineraries for the **orientation-preserving** slice \(\delta_L=\delta_R=0.3\); that statement does not cover the present opposite-sign determinants or its exact no-one-two saddle classification. Fatoyinbo–Simpson (2022) studies noninvertible border-collision period-three regions, including an \(LRR\) boundary formula in its Appendix A, with a different forcing/sign configuration and without the above four-parameter, two-saddle pairing and spectral theorem. These sources establish essential context and overlapping methods; the claimed contribution is solely the stated complete sharp classification in this domain, not symbolic-itinerary calculations generally.

## Limitations

The exact result assumes determinant magnitudes strictly below one and both branch fixed points saddle; it does not classify parameters on or beyond these boundaries. The statement covers primitive period three only, not higher-period or chaotic attractors. The collision orbit is not claimed differentiably hyperbolic. An equivalent statement in an unindexed analysis or in broader general formulas remains a publication-priority risk. Independent mathematical validation has not been performed.

## References

1. I. Ghosh, R. I. McLachlan, and D. J. W. Simpson, *The bifurcation structure within robust chaos for two-dimensional piecewise-linear maps*, arXiv:2402.05393v1 (public 2024-02-08), https://arxiv.org/html/2402.05393v1 .
2. H. O. Fatoyinbo and D. J. W. Simpson, *A synopsis of the non-invertible, two-dimensional, border-collision normal form with applications to power converters*, arXiv:2210.14445v1 (2022-10-26), https://arxiv.org/abs/2210.14445 .
3. P. A. Glendinning and D. J. W. Simpson, *Robust chaos and the continuity of attractors*, *Transactions of Mathematics and Its Applications* **4** (2020), tnaa002; arXiv:1906.11974v1, https://doi.org/10.1093/imatrm/tnaa002 .
4. D. J. W. Simpson, *Border-Collision Bifurcations in \(\mathbb R^N\)*, *SIAM Review* **58** (2016), 177–226, https://doi.org/10.1137/15M1006982 .
