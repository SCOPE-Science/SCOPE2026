# Eventual exact Hilbert norms of maximal averages on unbalanced bicliques

## Finding
Let \(a\ge2\) and \(b\ge B(a):=102400(a+1)^6\) be integers. For the centered Hardy–Littlewood maximal operator \(M_{a,b}\) on the complete bipartite graph \(K_{a,b}\), equipped with graph distance, counting measure and the ordinary \(\ell^2\) norm, put
\[
\tau_{a,b}=1+\frac{ab+1}{(a+1)^2},\qquad
\Lambda_{a,b}=\frac{\tau_{a,b}+\sqrt{\tau_{a,b}^2-4/(a+1)^2}}2.
\]
Then the **sharp nonlinear strong-type constant** is exactly
\[
\boxed{\|M_{a,b}\|_{\ell^2\to\ell^2}^{2}=\Lambda_{a,b}}.
\]
For nonnegative inputs, every maximizing vector is a positive multiple of one vector having one positive value \(x\) on the \(a\)-vertex class and one positive value \(y<x\) on the \(b\)-vertex class, where
\[
\frac yx=\frac{a}{(a+1)^2\Lambda_{a,b}-1}.
\]
For arbitrary real or complex inputs, equality holds precisely when the absolute values have that form (their signs or phases can vary). In particular, at each fixed \(a\ge2\),
\[
\boxed{\|M_{a,b}\|_{\ell^2\to\ell^2}^{2}
=\frac{ab}{(a+1)^2}+1+\frac1{(a+1)^2}-\frac1{ab}+O_a(b^{-2})}
\qquad (b\to\infty).
\]
No optimality of the explicit sufficient threshold \(B(a)\) is asserted.

## Assumptions and scope
For a graph \(G\), define \(M_G f(v)=\max_{r\ge0}|B(v,r)|^{-1}\sum_{w\in B(v,r)}|f(w)|\), where graph balls include their centers. Let \(A\) and \(D\) be the two parts of \(K_{a,b}\) of sizes \(a\) and \(b\), respectively. If \(f\ge0\), write \(f=(u,v)\), \(X=\sum_{i\in A}u_i\), \(Y=\sum_{j\in D}v_j\), \(F=X+Y\), \(\mu=F/(a+b)\). Because the diameter is two,
\[
(Mf)_i=\max\left\{u_i,\frac{u_i+Y}{b+1},\mu\right\}\quad(i\in A),
\]
\[
(Mf)_j=\max\left\{v_j,\frac{v_j+X}{a+1},\mu\right\}\quad(j\in D).
\]
The norm is \(\sup_{f\ne0}\|Mf\|_2/\|f\|_2\). It is sufficient to study nonnegative vectors because \(Mf=M|f|\). The statement concerns the unweighted centered operator, not uncentered, fractional, or weighted maximal averages.

## Proof
**Step 1: candidate singular value and attaining vector.** Define the linear operator
\[
T(u,v)=\left(u,\frac{X\mathbf1_b+v}{a+1}\right).
\]
On zero-sum vectors in \(A\), the squared singular value of \(T\) is \(1\); on zero-sum vectors in \(D\) it is \(1/(a+1)^2\). On the two-dimensional subspace of vectors constant within each part, use the orthonormal indicator basis. The representing matrix is
\[
S=\begin{pmatrix}1&0\\\sqrt{ab}/(a+1)&1/(a+1)\end{pmatrix}.
\]
The trace of \(S^*S\) is \(\tau_{a,b}\), and its determinant is \(1/(a+1)^2\); therefore \(\|T\|_2^2=\Lambda_{a,b}>1\). Its top right singular vector is simple, strictly positive, and constant \(x\) on \(A\), \(y\) on \(D\). The lower eigenvector equation yields
\[
\frac yx=\frac{a}{(a+1)^2\Lambda_{a,b}-1}<1.
\]
The inequality follows already from \(\Lambda_{a,b}\ge1+ab/(a+1)^2\). When \(x>y\) and \(b>1\), every radius-zero average wins on \(A\) and every radius-one average wins on \(D\): in the latter class, the difference between the radius-one average and the full average has positive numerator \(a(b-1)(x-y)\). Thus \(Mf=Tf\) on the top right singular vector. In particular, **for every** \(b\ge2\), \(\|M\|_2^2\ge\Lambda_{a,b}\). Alternatively, a uniform unit vector on \(A\) with zero values on \(D\) gives the convenient weaker lower bound \(\|M\|_2^2\ge1+ab/(a+1)^2\).

**Step 2: a uniform large-class estimate.** Let \(f=(u,v)\ge0\) satisfy \(\|f\|_2=1\), and put \(s=\|v\|_2\), \(c=X/(a+1)\), \(\mu=F/(a+b)\). We have \(X\le\sqrt a\), \(Y\le\sqrt b\), \(\mu\le1/\sqrt{a+b}\), and \(c\le1/2\). Every output on \(D\) lies between \(c\) and \(c+v_j+\mu\). Hence
\[
\begin{aligned}
\sum_{j\in D}(Mf)_j^2
&\le bc^2+2c(Y+b\mu)+\sum_{j\in D}(v_j+\mu)^2\\
&\le bc^2+2\sqrt b+4.
\end{aligned}
\]
Here \(Y+b\mu\le2\sqrt b\), and \(\sum(v_j+\mu)^2\le\|v\|_2^2+2\mu Y+b\mu^2\le4\). On \(A\), since \(u_i\le1\), \(Y\le\sqrt b\), and \(\mu\le1/\sqrt b\), we have \((Mf)_i\le u_i+3/\sqrt b\). Therefore
\[
\sum_{i\in A}(Mf)_i^2\le1+\frac{6\sqrt a}{\sqrt b}+\frac{9a}{b}.
\]
Together, for every integer \(b\ge1\),
\[
\boxed{\|Mf\|_2^2\le\frac{bX^2}{(a+1)^2}+20(a+1)\sqrt b.}\tag{1}
\]
This bound is uniform over the full unit sphere of nonnegative inputs; it does not presuppose an active branch.

**Step 3: every maximizer localizes on the smaller part.** Compactness of the finite-dimensional unit sphere supplies an optimizing \(f\ge0\). The elementary lower bound in Step 1 and (1) imply
\[
X^2\ge a-\Delta,\qquad\Delta:=\frac{20(a+1)^3}{\sqrt b}.
\]
Our explicit assumption \(b\ge102400(a+1)^6\) gives \(\Delta\le1/16\). Cauchy–Schwarz now yields
\[
\|v\|_2^2\le\frac\Delta a,\qquad
\left\|u-\frac Xa\mathbf1_a\right\|_2^2\le\frac\Delta a.
\]
Consequently \(v_j\le1/(4\sqrt a)\) for all \(j\in D\), whereas every \(u_i\) exceeds \(1/(2\sqrt a)\), because \(X/a\ge\sqrt{a-1/16}/a\ge(31/32)/\sqrt a\). Also \(Y\le\sqrt b/(4\sqrt a)\), and \(\mu\le1/\sqrt b\).

At every \(i\in A\), the radius-zero branch is uniquely maximal: \(Y<bu_i\) makes its value exceed the radius-one branch, and \(\mu<u_i\) follows from \(b>4a\). At every \(j\in D\), the radius-one value exceeds both \(v_j\) and \(\mu\), since
\[
\frac{X+v_j}{a+1}\ge\frac Xa\frac a{a+1}
\ge\frac{31\sqrt a}{32(a+1)}>\frac1{4\sqrt a}\ge v_j,\mu
\]
(the final bound on \(\mu\) uses \(b>16a\)). Thus **every global maximizing vector** satisfies \(Mf=Tf\). Therefore its quotient is at most \(\|T\|_2\); Step 1 gives the reverse inequality. Equality forces a top right singular vector of \(T\), which is simple and has the claimed shape.

**Step 4: second-order asymptotic.** Since \(\tau_{a,b}=ab/(a+1)^2+1+1/(a+1)^2\), a Taylor expansion of the positive root gives
\[
\Lambda_{a,b}=\tau_{a,b}-\frac{1}{(a+1)^2\tau_{a,b}}+O_a(\tau_{a,b}^{-3})
=\frac{ab}{(a+1)^2}+1+\frac1{(a+1)^2}-\frac1{ab}+O_a(b^{-2}).
\]
This proves the asserted expansion, with \(a\) fixed. Neither the finite tests nor the asymptotic expansion supplies an all-\(b\) classification below the explicit threshold.

## Verification
The independent-from-the-proof finite program `check.py` constructs all linear ball-selection matrices for six small \((a,b)\) pairs, directly checks their singular norms against the proposed candidate formula, and checks the maximizing branch on a singular vector. It also checks the exact two-dimensional trace/determinant identities and positivity of the candidate ratio over further finite cases. It reports 2,658 assertions; only the analytic inequalities above prove the universal threshold, uniqueness, and asymptotic formula. Reproduce with `python check.py` (Python 3 and NumPy are required).

## Relationship to prior work
Soria and Tradacete, arXiv:1410.6204v1 (first public version October 22, 2014), introduced sharp norm questions for the centered graph maximal operator, gave general \(0<p\le1\) results, and provided only bounds for strong \(p>1\) norms on stars. González-Riquelme and Madrid, arXiv:2005.03146, determined exact \(\ell^2\) norms for complete graphs and stars; their follow-up arXiv:2011.02630 characterized star extremizers at selected exponents. The star case \(a=1\) is specifically excluded as already solved. The present claim deals instead with nonstar bicliques \(a\ge2\), gives an explicit sufficient imbalance threshold, a closed norm and all maximizing moduli there, and derives a second-order correction. The cited primary works were checked at their theorem statements and relevant proof sections; none of the inspected statements implies the nonstar eventual biclique formula. This is a limited priority comparison, not a proof of universal historical novelty.

## Limitations
The threshold \(102400(a+1)^6\) is sufficient and deliberately not optimized; the conclusion **does not assert** the same equality for any smaller \(b\). The result is for fixed finite \(a\ge2\) with highly unbalanced \(b\), not a joint asymptotic when both parts grow. The proof is for the classical centered \(\ell^2\) maximal operator with counting measure; it does not determine \(\ell^p\) sharp norms for other exponents or analogous bounds for other graphs. Numerical finite tests are illustrative, not universal certificates. Historical priority remains subject to additional independent bibliographic scrutiny.

## References
1. J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204v1 (first submitted October 22, 2014), https://arxiv.org/pdf/1410.6204.
2. C. González-Riquelme and J. Madrid, *Sharp Inequalities for maximal operators on finite graphs*, arXiv:2005.03146, https://arxiv.org/pdf/2005.03146.
3. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, arXiv:2011.02630, https://arxiv.org/pdf/2011.02630.
