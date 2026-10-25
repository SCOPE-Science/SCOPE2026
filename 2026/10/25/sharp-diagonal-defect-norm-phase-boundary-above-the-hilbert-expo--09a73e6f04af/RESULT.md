# Sharp diagonal defect-norm phase boundary above the Hilbert exponent

## Finding

Fix any exponent \(2<p<\infty\), any integer \(n\ge2\), any nonzero Banach spaces \(X_1,\ldots,X_n\) over either \(\mathbb R\) or \(\mathbb C\), and the Banach direct sum \(X=(\bigoplus_{j=1}^n X_j)_p\). Let \(0\le d_j<1\), and define the diagonal strict contraction \(T(x_1,\ldots,x_n)=(d_1x_1,\ldots,d_nx_n)\). Its Pythagorean defect is
\[
A_T(x)=\bigl(\|x\|_X^2-\|Tx\|_X^2\bigr)^{1/2}.
\]
Write \(m=\min_j d_j\) and \(M=\max_jd_j\). The following sharp classification holds:
\[
\boxed{A_T\text{ is a norm}\quad\Longleftrightarrow\quad
(d_1=\cdots=d_n=0)\ \text{or}\ (m>0\text{ and }M^p\le m^{p-2}).}
\]
The boundary is included. For complex \(X\), the norm condition is equivalent to existence of the orthogonally complemented isometric dilation of this strict contraction in the precise sense of Jana--Pal--Roy, Theorem 7.13; this equivalence is **their prior theorem**, not a new dilation construction.

The classification follows from an independent sharp differential inequality. If all \(d_j>0\), write \(N(z)=\|z\|_p\), \(Q(z)=\|(d_jz_j)_j\|_p\) on the strictly positive scalar orthant and \(H_N=\tfrac12\nabla^2(N^2)\), \(H_Q=\tfrac12\nabla^2(Q^2)\). Then
\[
\boxed{\sup_{z\in(0,\infty)^n}\ \sup_{h\ne0}
\frac{h^{\mathsf T}H_Q(z)h}{h^{\mathsf T}H_N(z)h}
=\frac{M^p}{m^{p-2}}.}
\]
Thus \(M^p\le m^{p-2}\) is the exact global curvature-domination condition. In particular, the unequal-weight example \(p=4\), \((d_1,d_2)=(4/5,7/10)\) passes since \((4/5)^4=256/625<49/100=(7/10)^2\), whereas \((9/10,4/5)\) fails since \((9/10)^4=6561/10000>16/25=(4/5)^2\). In either case both diagonal multipliers are strictly positive and less than one. By contrast, **every nonzero diagonal multiplier with any zero entry fails above exponent two**.

## Assumptions and scope

The scalar-field choice is arbitrary between real and complex. Every Banach block \(X_j\) is nonzero, but no finite-dimensionality, smoothness, lattice structure, or reflexivity is required of a block. The number of blocks is finite, at least two, and the weights are real and nonnegative. The strict assumption \(M<1\) ensures \(A_T(x)>0\) for every \(x\ne0\). The theorem does not cover infinite diagonal decompositions, negative exponents, or arbitrary non-diagonal contractions.

In what follows the gradient/Hessian calculation is performed only in a **finite-dimensional real positive orthant** of block magnitudes; it does not posit a differentiable norm on any block. The squared functions are twice continuously differentiable there because \(p>2\). All vector inequalities are in the symmetric positive-semidefinite (Löwner) order.

## Proof

**1. Hessian inverse identity.** For \(z=(z_1,\dots,z_n)\in(0,\infty)^n\), put \(S=\sum_j z_j^p\), \(N=S^{1/p}\), and \(v_j=z_j^{p/2}/N^{p/2}\). Thus \(\|v\|_2=1\). Direct differentiation yields
\[
H_N=N^{2-p}E\bigl((p-1)I-(p-2)vv^{\mathsf T}\bigr)E,
\qquad E=\operatorname{diag}(z_j^{(p-2)/2}).
\]
The middle matrix has eigenvalue one along \(v\) and eigenvalue \(p-1\) on its perpendicular complement. It is positive definite, with inverse \((I+(p-2)vv^{\mathsf T})/(p-1)\). Multiplying out gives the exact inverse
\[
\boxed{H_N^{-1}=\frac{1}{p-1}\bigl[
N^{p-2}\operatorname{diag}(z_j^{2-p})
+(p-2)N^{-2}zz^{\mathsf T}\bigr].}
\tag{1}
\]
If all \(d_j>0\), apply (1) to \(D z=(d_jz_j)_j\), with \(D=\operatorname{diag}(d_j)\). As \(H_Q=D H_N(Dz)D\), the inverse is
\[
\boxed{H_Q^{-1}=\frac{1}{p-1}\bigl[
Q^{p-2}\operatorname{diag}(d_j^{-p}z_j^{2-p})
+(p-2)Q^{-2}zz^{\mathsf T}\bigr].}
\tag{2}
\]
These formulas require strictly positive coordinates and multipliers; the zero-multiplier case is handled separately below.

**2. Global domination and its sharp coefficient.** Set \(K=M^p/m^{p-2}\). Because \(mN\le Q\le MN\) and \(M\ge m>0\), we have \(K\ge M^2\). Subtracting (1) from \(K\) times (2) yields
\[
\begin{aligned}
(p-1)(K H_Q^{-1}-H_N^{-1})
&=\operatorname{diag}\bigl(z_j^{2-p}(KQ^{p-2}d_j^{-p}-N^{p-2})\bigr)\\
&\quad +(p-2)(KQ^{-2}-N^{-2})zz^{\mathsf T}.
\end{aligned}
\tag{3}
\]
Every diagonal entry in the first summand is nonnegative: since \(d_j\le M\), \(Q\ge mN\),
\[
KQ^{p-2}d_j^{-p}\ge (M^p/m^{p-2})(mN)^{p-2}/M^p=N^{p-2}.
\]
The second summand is positive semidefinite because \(KQ^{-2}\ge K/(M^2N^2)\ge N^{-2}\). Hence \(K H_Q^{-1}\succeq H_N^{-1}\). Inversion reverses the order on positive definite matrices and yields \(H_Q\preceq K H_N\), which is the claimed upper curvature bound.

For sharpness choose distinct indices \(i,j\) with \(d_i=M\), \(d_j=m\) (if all multipliers coincide, choose any two indices). Restrict to their positive two-coordinate plane, put \(z_j=1\), \(z_i=\varepsilon\), and take \(h=e_i\). The differentiation formula gives
\[
\frac{h^{\mathsf T}H_Q(z)h}{h^{\mathsf T}H_N(z)h}
\longrightarrow\frac{d_i^p}{d_j^{p-2}}
=K\qquad(\varepsilon\downarrow0).
\]
If \(n>2\), approach this plane through strictly positive vectors to justify taking the supremum over \((0,\infty)^n\). Thus no smaller coefficient works globally. This proves the exact Hessian ratio independently of the later norm classification.

**3. Sufficiency of the phase condition.** Assume \(m>0\) and \(K\le1\). On \(\mathbb R_+^n\) put \(G(z)=N(z)^2-Q(z)^2\). The Hessian inequality in Step 2 gives \(\nabla^2G\succeq0\) in the strictly positive orthant. Continuity extends convexity to its closure. Moreover, each partial derivative there is
\[
\partial_jG(z)=2z_j^{p-1}\left[N(z)^{2-p}-d_j^pQ(z)^{2-p}\right]\ge0,
\]
because \(Q/N\ge m\) and \(d_j^p\le M^p\le m^{p-2}\). Therefore \(G\) is convex and nondecreasing in each nonnegative coordinate. The full-even extension \(\widetilde G(z)=G(|z_1|,\ldots,|z_n|)\) is convex by coordinatewise convexity of absolute value and monotonicity/convexity of \(G\). Also \(\widetilde G(z)\ge(1-M^2)\|z\|_p^2>0\) for \(z\ne0\), it is continuous and two-homogeneous, and its unit sublevel set is closed, convex, absorbing and balanced. Its Minkowski gauge is precisely \(F(z)=\sqrt{\widetilde G(z)}\); hence \(F\) is an absolute scalar norm. As \(F\) is absolute, it is coordinatewise nondecreasing on \(\mathbb R_+^n\). For arbitrary \(x,y\in X\), coordinatewise block triangle inequalities yield
\[
\begin{aligned}
A_T(x+y)&=F(\|x_1+y_1\|,\ldots,\|x_n+y_n\|)\\
&\le F(\|x_1\|+\|y_1\|,\ldots,\|x_n\|+\|y_n\|)\\
&\le A_T(x)+A_T(y).
\end{aligned}
\]
Positivity and homogeneity were already established. This proves normability without any block smoothness assumptions, including the critical equality case \(K=1\).

**4. Necessity when all weights are positive.** If \(K>1\), choose \(i,j\) as in Step 2. The same curvature-ratio limit shows that the restriction of \(G=N^2-Q^2\) to the positive two-coordinate plane has strictly negative second derivative along \(e_i\) at some point \(z_i=\varepsilon>0,z_j=1\). Therefore \(G\) is not convex. But the square of any norm is convex: by the triangle inequality followed by convexity of \(t\mapsto t^2\), \(F((u+v)/2)^2\le(F(u)^2+F(v)^2)/2\). Choosing unit vectors from blocks \(X_i,X_j\) identifies that two-plane inside \(X\); so \(A_T\) cannot be a norm.

**5. Necessity with a zero weight.** If \(d_j=0\) and \(d_i>0\), select norm-one vectors \(u_i\in X_i\) and \(u_j\in X_j\). On the plane \(a u_i+b u_j\),
\[
A_T(\varepsilon u_i+u_j)^2=(1+\varepsilon^p)^{2/p}-d_i^2\varepsilon^2
=1-d_i^2\varepsilon^2+\frac2p\varepsilon^p+O(\varepsilon^{2p})<1
\]
for sufficiently small positive \(\varepsilon\), because \(p>2\). The same holds with \(-\varepsilon u_i\). Their midpoint \(u_j\) has defect one, violating convexity of any norm. If all \(d_j=0\) then \(A_T=\|\cdot\|_X\), as required. These cases exhaust all nonnegative weights. For comparison, at \(p=2\) the defect is the weighted \(\ell_2\)-sum with coefficients \(\sqrt{1-d_j^2}\), always a norm.

## Verification

The optional standalone `verify_diag_defect.py` uses deterministic pseudorandom samples, direct Hessian evaluations and independent inversion formulas in dimensions two and three at five non-Hilbert exponents. It checks the matrix-inverse identity, the sharp curvature upper bound against sampled tangent vectors, triangle inequalities in several subcritical cases, and an explicit midpoint violation above threshold. Running `python verify_diag_defect.py` produced `PASS 5250 Hessian inverses/Loewner bounds/positive triangles` plus a nonconvex midpoint witness. Separate exact symbolic differentiation for \(p=4\), dimension two, checked all entries of both inverse identities and yielded zero differences. All finite checks are sanity tests only; the formulas (1)--(3), curvature limit, and convexity argument prove the full theorem.

## Relationship to prior work

The March 27, 2026 preprint by Jana and Pal identifies defect normability as the condition relevant to their Banach-space dilation constructions for commuting contractions. Its Section 1 and Theorem 1.2 restate the earlier single-operator criterion, and Examples 2.6--2.7 examine other operator families; its inspected results do **not** calculate the positive anisotropic diagonal phase boundary. Jana, Pal and Roy's earlier 2024 paper (Theorem 7.13 and Examples 7.18--7.20) supplies the general single-operator dilation equivalence, a scalar \(\ell_2\)-diagonal example, and distinct non-Hilbert failures, but no exact super-Hilbert positive weighted diagonal criterion.

Two published 2026 notes, *Sharp scalar-defect thresholds on \(\ell_p\)-sums* and *Sharp defect-norm thresholds for band projections on \(L_p\)*, solve the complementary **single nonzero block multiplier / one zero band** problem, where the defect fails at every positive multiplier for \(p>2\). Their statements and proofs were inspected. The present theorem agrees with that zero-band obstruction, but adds the hitherto unclassified **all-positive nonconstant** diagonal regime, finite arbitrary Banach blocks, an exact parameter surface, and a sharp Hessian distortion law. No implication from either scalar-band theorem covers the positive unequal-weight examples given above.

Fackler and Glück's dilation theorem for positive \(L_p\)-contractions (Theorem 7.1, arXiv:1709.08547) uses contractions \(J,Q\) and an ambient invertible isometry satisfying power identities; this is a **different dilation definition** from the orthogonal-two-sum defect criterion. It does not imply defect normability: the nonzero one-band operators in Step 5 have their type of positive dilation but fail the squared defect triangle test.

## Limitations

This theorem is restricted to finite diagonal sums, \(2<p<\infty\), nonnegative strict-contraction weights, and the precise defect norm. It does not assert an Andô dilation for arbitrary commuting **pairs**: the 2026 paper imposes additional unitary-extension hypotheses for that stronger conclusion. It does not classify non-diagonal contractions, infinite multiplier spectra, or sub-Hilbert exponents. The originality check inspected the most directly related full texts and published mathematics-index records but cannot exclude unindexed equivalent convexity results. No external or independent mathematical validation is asserted.

## References

1. S. Jana and S. Pal, *On a minimal Andô dilation for a pair of strict contractions*, arXiv:2603.26321, initially public 2026-03-27, https://arxiv.org/abs/2603.26321; full text https://arxiv.org/html/2603.26321v2, Introduction, Theorem 1.2, Examples 2.6--2.7 and Theorem 2.4.
2. S. Jana, S. Pal and S. Roy, *A dilation theoretic approach to Banach spaces*, arXiv:2407.15112, initially public 2024-07-21, https://arxiv.org/html/2407.15112v2; especially Definition 1.2, Theorem 7.13 and Examples 7.18--7.20.
3. S. Fackler and J. Glück, *A Toolkit for Constructing Dilations on Banach Spaces*, arXiv:1709.08547, initially public 2017-09-25, https://arxiv.org/html/1709.08547; Definition 2.7 and Theorem 7.1.
4. *Sharp scalar-defect thresholds on \(\ell_p\)-sums*, research note, published 2026-10-11; exact scalar-coordinate classification and proof.
5. *Sharp defect-norm thresholds for band projections on \(L_p\)*, research note, published 2026-10-11; sharp one-band classification and proof.
