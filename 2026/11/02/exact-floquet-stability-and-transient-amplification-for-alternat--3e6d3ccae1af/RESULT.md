# Exact Floquet stability and transient amplification for alternating-step Adams–Bashforth three

## Finding

Consider the genuine third-order interpolatory Adams–Bashforth (AB3) method on the scalar decay equation \(y'=-\lambda y\), \(\lambda>0\), with positive step sizes \(h_1,h_2,h_1,h_2,\ldots\). Put
\[
 s=\lambda(h_1+h_2)>0,\qquad q=\frac{h_1h_2}{(h_1+h_2)^2}\in(0,1/4],\qquad r=h_2/h_1>0.
\]
For every fixed \(r\), every starting triple tends to zero **if and only if**
\[
 \boxed{0<s<\frac{6}{5+2q}.}
\]
At equality the two-step Floquet matrix has a simple multiplier \(+1\) and its other two multipliers lie strictly inside the unit disk; above equality it has a real multiplier strictly greater than one.

The resulting complete ratio phase diagram is as follows. If \(0<s<12/11\), every positive ratio is strictly stable. If \(s=12/11\), every ratio except \(r=1\) is strictly stable. If \(12/11<s<6/5\), write
\[
 q_c=\frac{6/s-5}{2},\qquad
 r_{\pm}=\frac{1-2q_c\pm\sqrt{1-4q_c}}{2q_c}.
\]
Strict stability occurs precisely for \(0<r<r_-\) or \(r>r_+\), two disjoint regions satisfying \(r_-r_+=1\). For \(s\ge6/5\), no finite positive ratio is strictly stable. For example, at \(s=7/6\) the stable ratios are exactly \(r<6-\sqrt{35}\) or \(r>6+\sqrt{35}\).

The largest possible **mean normalized** negative-real stability step is the nonattained supremum \(3/5\), compared with \(6/11\) for equal steps: a sharp factor \(11/10\). However spectral stability does not provide contrast-uniform one-step robustness. At any fixed \(s\in(0,6/5)\), if the large step follows the small one and \(r\to\infty\), its history-state transfer satisfies
\[
 \boxed{\lim_{r\to\infty}\frac{\|T(h_2,h_1)\|_2}{r}=\frac{5\sqrt2}{6}s.}
\]
Thus arbitrarily large one-step amplification of arbitrary initial-history perturbations coexists with strictly decaying two-step Floquet multipliers.

## Assumptions and scope

Time steps are positive, exactly two-periodic and interpreted through polynomial interpolation of the **actual nonuniform time nodes**, not through frozen equal-step AB3 coefficients. A history state is \(Y_n=(y_n,y_{n-1},y_{n-2})^\mathsf T\), with freely specified real or complex initial triple. Stability means \(Y_n\to0\) as \(n\to\infty\) for every initial triple with a fixed positive ratio and step scale. Norms in the amplification assertion are Euclidean induced matrix norms. The negative test eigenvalue is real; no claims are made for arbitrary complex eigenvalues, nonlinear equations, or general time-step sequences.

## Proof

**1. Genuine variable-step transfer.** Measure time in units of \(\lambda^{-1}\). If the proposed normalized step is \(x>0\) and the immediately preceding step is \(y>0\), two-periodicity means the earlier step is \(x\). To form the order-three Adams–Bashforth increment, interpolate \(f\) at the relative nodes \(0,-y,-(x+y)\) by its quadratic Lagrange polynomial and integrate over \([0,x]\). Since \(f=-\lambda y\), direct exact integration produces
\[
 T(x,y)=\begin{pmatrix}
 1-\dfrac{x(5x^2+12xy+6y^2)}{6y(x+y)}&\dfrac{x(5x+3y)}{6y}&-\dfrac{x(2x+3y)}{6(x+y)}\\
 1&0&0\\0&1&0
 \end{pmatrix}.
\]
When \(x=y\), its first row is \((1-23x/12,4x/3,-5x/12)\), the standard AB3 recurrence. One two-step period has matrix \(M=T(b,a)T(a,b)\), where \(a=\lambda h_1\), \(b=\lambda h_2\). The cyclically reversed product has the same characteristic polynomial.

**2. Exact Floquet polynomial.** With \(s=a+b\), \(q=ab/s^2\), expansion and cancellation give
\[
 \det(zI-M)=z^3-Az^2+Bz-C,
\]
where
\[
 A=1-\frac{2-q}{3}s+\frac{30+12q+q^2}{36}s^2,\quad
 B=\frac{1+q}{3}s+\frac{q(3+q)}{18}s^2,\quad
 C=\frac{q(6+q)}{36}s^2.
\]
The key cancellation is the exact identity
\[
 \det(I-M)=1-A+B-C=s\left(1-\frac{5+2q}{6}s\right).
\]
This is an identity for **all** \(a,b>0\), not a small-step approximation.

**3. No hidden earlier stability boundary.** For the real monic cubic \(z^3-Az^2+Bz-C\), strict Schur stability is equivalent to the four inequalities
\[
 C<1,\qquad 1-A+B-C>0,\qquad 1+A+B+C>0,\qquad 1-B+AC-C^2>0,
\]
with \(C>0\). Suppose \(0<s<6/(5+2q)\). Then \(s<6/5\) and \(0<q\le1/4\). The coefficients \(B,C\) are positive and satisfy the explicit bounds
\[
 B\le\frac{113}{200}<1,\qquad C\le\frac1{16}<1.
\]
Also \(A>0\), because \(A\ge1-2s/3+5s^2/6>0\). Finally
\[
 A-C=1-\frac{2-q}{3}s+\frac{5+q}{6}s^2>0,
\]
since the quadratic has discriminant \((q^2-10q-26)/9<0\). Therefore \(1+A+B+C>0\) and \(1-B+AC-C^2=1-B+C(A-C)>0\). The remaining Schur inequality is precisely \(s<6/(5+2q)\), proving sufficiency.

At equality, \(z=1\) is a root, and \(\det(zI-M)=(z-1)(z^2+(1-A)z+C)\). Here \(C<1\), \(A+C>0\), and \(2-A+C>0\); for the last inequality, the bounds \(q\le1/4\), \(s\le6/5\) imply \(A\le 1-7s/12+529s^2/576\le649/400<2\). The quadratic Schur test places both remaining roots strictly inside the disk, and \(2-A+C>0\) makes the unit root simple. If \(s>6/(5+2q)\), the polynomial is negative at \(z=1\) and tends to \(+\infty\) on the positive real axis, so it has a real zero greater than one. This proves necessity and the boundary assertions.

**4. Ratio classification.** The identity \(q=r/(1+r)^2\) has maximum \(1/4\), attained uniquely at \(r=1\), and approaches zero at either contrast extreme. Consequently the critical \(s=6/(5+2q)\) ranges from \(12/11\) up to the excluded supremum \(6/5\). For intermediate \(s\), solving \(q<q_c\) yields the two intervals defined above. At \(s=7/6\), \(q_c=1/14\), hence \(r_{\pm}=6\pm\sqrt{35}\). Dividing the critical \(s\) by two gives the mean-step limit and the factor \((3/5)/(6/11)=11/10\).

**5. Transient amplification.** At fixed \(s>0\), set \(a=s/(1+r)\), \(b=sr/(1+r)\). Entrywise,
\[
 \lim_{r\to\infty}\frac{T(b,a)}r=
 \begin{pmatrix}-5s/6&5s/6&0\\0&0&0\\0&0&0\end{pmatrix}.
\]
The rank-one limit has spectral norm \(5\sqrt2s/6\), proving the exact amplification asymptotic by continuity of the matrix norm. For \(s<6/5\), sufficiently extreme finite contrasts remain Floquet-stable by the established criterion, so this divergence cannot be dismissed as instability above the threshold.

## Verification

The self-contained `verify_ab3_alternating.py` reconstructs the Lagrange weights symbolically, checks the entire characteristic polynomial and critical cancellation exactly, compares with standard equal-step AB3, verifies 50 rational critical ratios, independently computes 1000 random transfer pairs from Vandermonde integration (998 used away from the transition tolerance), and checks three transient asymptotic matrices. Run with `python verify_ab3_alternating.py` using Python, SymPy and NumPy. The recorded replay passed; the analytical Schur and limit arguments above, rather than finite random tests, establish the quantified result.

## Relationship to prior work

The classical AB3 formula and its equal-step stability region are standard. Grote and Mitkova (2011, arXiv:1109.4480, Section 3.1) explicitly present the constant-step AB3 coefficients and construct a different Adams–Bashforth-based local substepping method; that is not the two-periodic variable-node recurrence above. Hadjimichael, Ketcheson, Lóczi and Németh (2015, arXiv:1504.04107, Sections 2–3) optimize strong-stability-preserving variable-step *formulae* under monotonicity constraints, rather than calculate the real-negative Floquet spectrum of this fixed classical AB3 interpolation formula. Marciniak and Jankowska (2019, DOI 10.1007/s11075-019-00774-y, Sections 2–7) derive interval Adams–Bashforth enclosures under varying steps without the present sharp periodic negative-axis stability classification.

The older closely relevant articles of Gear–Tu (1974), Skeel–Jackson (1983) and Calvo–Lisbona–Montijano (1989) study stability under changes of Adams/Nordsieck grids. Their accessible abstracts establish broad results about step variation, not the displayed negative-real two-periodic Floquet phase law. In particular the 1989 full text was not obtained; it remains a material priority risk rather than evidence of noncoverage. The explicit cubic Schur criterion is classical and is used as a proof tool, not claimed as new. No claim of historical uniqueness or independent publication priority is made.

## Limitations

Only the scalar real-negative test equation and exactly two-periodic positive steps are covered. A favorable Floquet spectral radius does not imply stepwise monotonicity, SSP, transient norm control uniformly in the ratio, stability for arbitrary nonperiodic grids, or general PDE convergence. The extremal improvement \(3/5\) is only a supremum as the ratio tends to zero or infinity; neither degeneracy is an admissible positive finite ratio. Numerical checks are finite supplementary evidence. Historical overlap remains possible because several older specialist full texts were inaccessible; independent mathematical validation has not been performed.

## References

1. M. J. Grote and T. Mitkova, *High-order explicit local time-stepping methods for damped wave equations*, arXiv:1109.4480 (first public 2011-09-21). https://arxiv.org/abs/1109.4480
2. Y. Hadjimichael, D. Ketcheson, L. Lóczi and A. Németh, *Strong stability preserving explicit linear multistep methods with variable step size*, arXiv:1504.04107 (first public 2015-04-16). https://arxiv.org/abs/1504.04107
3. A. Marciniak and M. A. Jankowska, *Interval methods of Adams-Bashforth type with variable step sizes*, Numerical Algorithms (2019 online), DOI:10.1007/s11075-019-00774-y. https://doi.org/10.1007/s11075-019-00774-y
4. M. Calvo, F. Lisbona and J. Montijano, *On the Stability of Interpolatory Variable-Stepsize Adams Methods in Nordsieck Form*, SIAM J. Numer. Anal. 26 (1989), 946–962, DOI:10.1137/0726052. https://doi.org/10.1137/0726052
5. R. D. Skeel and L. W. Jackson, *The Stability of Variable-Stepsize Nordsieck Methods*, SIAM J. Numer. Anal. 20 (1983), 840–853, DOI:10.1137/0720056. https://doi.org/10.1137/0720056
6. C. W. Gear and K. W. Tu, *The Effect of Variable Mesh Size on the Stability of Multistep Methods*, SIAM J. Numer. Anal. 11 (1974), 1025–1043, DOI:10.1137/0711079. https://doi.org/10.1137/0711079
