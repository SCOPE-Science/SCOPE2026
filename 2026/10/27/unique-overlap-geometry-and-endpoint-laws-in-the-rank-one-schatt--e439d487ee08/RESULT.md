# Unique overlap geometry and endpoint laws in the rank-one Schatten comparison

## Finding
For any real exponent \(1<p<2\), and every complex matrix size \(d\ge2\), consider two rank-one matrices \(A,B\in M_d(\mathbb C)\) with \(\|A\|_{S_p}=\|B\|_{S_p}>0\). Let
\[
K_p=\sup_{d\ge2}\ \sup_{A,B}\frac{\|A+B\|_{S_p}}{\||A|+|B|\|_{S_p}},\qquad |A|=(A^*A)^{1/2}.
\]
Set \(k=p/(2-p)\). The scalar equation
\[
\tanh z+\tanh(kz)=2\tanh(pz)
\tag{1}
\]
has exactly one solution \(z_p>0\). The optimal constant is
\[
\boxed{K_p=\left[\frac{\cosh(z_p)^{p/2}\cosh(kz_p)^{1-p/2}}{\cosh(pz_p)}\right]^{1/p}>1.}
\tag{2}
\]
The extremizers are exactly those with aligned Gram phases and the two ray overlaps
\[
|\langle v,t\rangle|=\tanh z_p,\qquad |\langle u,w\rangle|=\tanh(kz_p),
\tag{3}
\]
when \(A=uv^*\) and \(B=wt^*\) have unit factor vectors after removing their common positive singular value. In particular real \(2\times2\) rank-one pairs attain \(K_p\).

Let \(z_0>0\) denote the unique positive solution of \(z_0\tanh z_0=1\). Then
\[
\boxed{K_p=1+\frac{z_0^2-1}{2}(p-1)^2+o((p-1)^2)}\quad(p\downarrow1),
\tag{4}
\]
where \((z_0^2-1)/2=0.219614419945\ldots\). At the other endpoint,
\[
\boxed{\lim_{p\uparrow2}K_p=\sqrt{\frac{1+\sqrt2}{2}}},\qquad
\lim_{p\uparrow2}\tanh z_p=\sqrt2-1.
\tag{5}
\]

## Assumptions and scope
The matrices may have any common finite dimension at least two and arbitrary complex entries, but each must have rank one and the same positive singular value. No positivity or commutation of their moduli is assumed. Scaling both matrices equally removes the common singular value; the assertion is an exact sharp inequality **within this balanced rank-one class**. For different nonzero singular values, higher rank, or unrestricted pairs, (2) is only an attained lower bound for the possible universal constant, not its claimed value. The theorem's primary subject is Schatten norm inequality optimization (MSC2020 47A30).

## Proof
**Step 1 (Gram reduction and phases).** Normalize the two nonzero singular values to one; write \(A=uv^*\), \(B=wt^*\), with unit \(u,w,v,t\). Put \(c=|\langle v,t\rangle|\) and \(d=|\langle u,w\rangle|\). The squared nonzero singular values of \(A+B\) are eigenvalues of the product of its two-by-two input/output Gram matrices. Their sum is \(2+2\operatorname{Re}(\langle u,w\rangle\langle t,v\rangle)\), and their product is \((1-c^2)(1-d^2)\). At fixed product, the sum of their positive \(p/2\)-powers is strictly increasing in their sum: for eigenvalues \(\lambda_+>\lambda_-\), the derivative with respect to the trace equals \((p/2)(\lambda_+^{p/2}-\lambda_-^{p/2})/(\lambda_+-\lambda_-)\), with the coincident-eigenvalue case obtained by continuity. Thus the maximal numerator at given \(c,d\) requires phase alignment, for which these two eigenvalues are \((1+c)(1+d)\) and \((1-c)(1-d)\). The denominator's positive eigenvalues are \(1+c\) and \(1-c\). Consequently the quotient raised to the \(p\)-th power is at most
\[
F_p(c,d)=\frac{[(1+c)(1+d)]^{p/2}+[(1-c)(1-d)]^{p/2}}{(1+c)^p+(1-c)^p},\quad 0\le c,d\le1,
\tag{6}
\]
with equality realized by phase-aligned real rank-one matrices.

**Step 2 (unique conditional optimizer).** Write \(r=p/2\in(1/2,1)\) and let \(c=\tanh z\), \(d=\tanh w\), where initially \(z,w\ge0\). At fixed \(c\in(0,1)\), the numerator of (6) is a strictly concave function of \(d\in[0,1]\), hence has at most one maximizer. Equivalently its logarithmic derivative in \(w\) has the sign of \(\tanh(r(z+w))-\tanh w\), so the unique maximum occurs at
\[
w=\frac{r}{1-r}z=\frac{p}{2-p}z=kz.
\tag{7}
\]
For \(c=0\) or \(c=1\), optimization gives the quotient one. Inserting (7) into (6), the exact optimized \(p\)-th power is
\[
H_p(z)=\frac{\cosh z^{\,p/2}\cosh(kz)^{\,1-p/2}}{\cosh(pz)},\qquad z\ge0.
\tag{8}
\]
Here the notation \(\cosh z^{\,p/2}\) means \((\cosh z)^{p/2}\), as in (2).

**Step 3 (positivity and uniqueness of the global maximum).** We have \(H_p(0)=1\) and \(H_p(z)\to1\) as \(z\to\infty\). The weighted mean identity \((p/2)\cdot1+(1-p/2)k=p\), together with strict convexity of \(a\mapsto\log\cosh(az)\) for each \(z>0\), gives \(H_p(z)>1\) for every finite \(z>0\). Differentiation yields
\[
\frac{d}{dz}\log H_p(z)=\frac p2\big[\tanh z+\tanh(kz)-2\tanh(pz)\big].
\tag{9}
\]
For \(z>0\) set
\[
R_p(z)=\frac{\tanh(pz)-\tanh z}{\tanh(kz)-\tanh(pz)}
=\frac{\int_1^p\operatorname{sech}^2(az)\,da}{\int_p^k\operatorname{sech}^2(az)\,da}.
\tag{10}
\]
For \(z_2>z_1>0\), the likelihood ratio \(\operatorname{sech}^2(az_2)/\operatorname{sech}^2(az_1)\) is strictly decreasing in \(a>0\), because its logarithmic derivative is \(-2z_2\tanh(az_2)+2z_1\tanh(az_1)<0\). Integrating the strictly ordered ratios over \([1,p]\) and \([p,k]\) proves \(R_p(z_2)>R_p(z_1)\). Moreover \(R_p(0+)=(p-1)/(k-p)=1/k<1\); Laplace endpoint estimates \(\operatorname{sech}^2(az)\sim4e^{-2az}\) give \(R_p(z)\to\infty\). Hence equation \(R_p(z)=1\), equivalent to (1), has exactly one positive root; by (9) it is the unique global maximizer of \(H_p\). The overlaps (3), including phase alignment, are therefore necessary and sufficient for equality.

**Step 4 (trace-norm endpoint).** Put \(\varepsilon=p-1\), so \(k=(1+\varepsilon)/(1-\varepsilon)\). Uniformly for \(z\) on any compact positive interval,
\[
\tanh z+\tanh(kz)-2\tanh(pz)
=2\varepsilon^2 z\operatorname{sech}^2z\,(1-z\tanh z)+O(\varepsilon^3).
\tag{11}
\]
The function \(z\tanh z\) is strictly increasing from zero to infinity. Bracketing the unique root in (11) on either side of \(z_0\) yields \(z_p\to z_0\). A second uniform compact Taylor expansion gives
\[
\log H_p(z)=\frac{\varepsilon^2}{2}z^2\operatorname{sech}^2z+O(\varepsilon^3).
\tag{12}
\]
Combining (12), \(K_p=H_p(z_p)^{1/p}\), and \(\tanh z_0=1/z_0\) proves (4).

**Step 5 (Hilbert endpoint).** For fixed positive \(z\), as \(p\uparrow2\) the expression in (9) tends to \(\tanh z+1-2\tanh(2z)\). Writing \(t=\tanh z\), its unique positive zero has \(t=\sqrt2-1\); sign bracketing and uniqueness from Step 3 give \(z_p\to\operatorname{artanh}(\sqrt2-1)\). In the same limit (8) becomes \(\cosh z\,e^z/\cosh(2z)=(1+t)/(1+t^2)\). At \(t=\sqrt2-1\), this is \((1+\sqrt2)/2\); taking the square root proves (5).

## Verification
The auxiliary file `verify_schatten_pair.py` uses only Python's standard library. It verifies the positive critical equation by bisection, checks equality between the two-dimensional Gram formula and (2), samples 6,000 feasible phase/overlap configurations for several exponents, and tests both endpoint coefficients against near-endpoint cases. The recorded run passed all 6,004 checks; numerical sampling is not used to establish the universal inequality or the uniqueness lemma, which are proved above.

For an explicit extremal construction, set \(v=u=(1,0)^T\), \(t=(c_p,\sqrt{1-c_p^2})^T\) and \(w=(d_p,\sqrt{1-d_p^2})^T\), then take \(A=uv^T\), \(B=wt^T\). Its singular values follow from the two Gram matrices in Step 1.

## Relationship to prior work
Qiu's August 2026 preprint (Section 5) already reduces balanced rank-one comparisons to a two-overlap formula and computes the **output-overlap optimum with fixed input overlap**. That reduction is credited; it does not establish the unique **remaining** input-overlap optimum, an explicit globally sharp constant for the balanced-rank-one class, or the two endpoint laws. Zeng–Liu–Ratnavelu prove a low-exponent counterexample and the sharp rank-one theorem on the opposite \(p\ge2\) side. Tang–Zhang formulated the unrestricted conjecture; Pang established additional counterexamples. This finding determines only the balanced rank-one envelope and is compatible with stronger higher-dimensional counterexamples to the unrestricted inequality.

## Limitations
This theorem is restricted to equal-norm rank-one pairs. Its value can be strictly below the unrestricted supremum for \(1<p<2\), as indicated by Qiu's three-dimensional constructions. It does not solve the general sharp-constant problem. Originality comparisons covered accessible full texts of the most directly relevant 2026 preprints and related indexed claims. Pang's closely related 2026 work was available only at abstract level, and independent publication-priority assessment has not been performed. No numerical check certifies the infinite family of exponents.

## References
1. Hongsen Qiu, *Sharp Quasi-Reverse Minkowski Inequality for Schatten Norms*, arXiv:2608.17565v1, first public 2026-08-18, especially Section 5.
2. Zijian Zeng, Houde Liu, Kurunathan Ratnavelu, *A Counterexample to the Tang Zhang Schatten Norm Conjecture and Sharp Positive Results*, arXiv:2608.15558v1, first public 2026-08-16.
3. Quanyu Tang and Shu Zhang, *Generalizing Lee's Conjecture on the Sum of Absolute Values of Matrices*, arXiv:2510.16846, first public 2025-10-19.
4. Zhekai Pang, *Counterexamples to a Conjectured Schatten Norm Inequality*, arXiv:2608.18112 (abstract inspected only).
