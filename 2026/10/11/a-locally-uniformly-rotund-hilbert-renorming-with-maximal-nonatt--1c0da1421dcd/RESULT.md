# A locally uniformly rotund Hilbert renorming with maximal nonattained \(C\)-symmetry defect
## Finding
There is a norm on real Hilbert sequence space, equivalent to its standard Hilbert norm by a factor at most \(\sqrt2\), for which both the resulting space and its dual are separable, reflexive, Gâteaux smooth, and locally uniformly rotund, and **every nonzero point is \(C\)-approximately left- and right-symmetric**, but **neither space is globally \(C\)-approximately symmetric** for Birkhoff--James orthogonality.

For a real Banach space \(Z\) and a nonzero \(z\), let
\[
J_Z(z)=\{f\in S_{Z^*}:f(z)=\|z\|\}.
\]
Define the extended global Chmieliński defect by
\[
\sigma_C(Z)=\sup_{\substack{u,v\in S_Z\\u\perp_Bv}}\inf_{g\in J_Z(v)}|g(u)|\in[0,1].
\tag{1}
\]
We produce one explicit space \(X\) such that
\[
\boxed{\sigma_C(X)=\sigma_C(X^*)=1,}
\tag{2}
\]
while for every individual admissible ordered pair \((u,v)\), its reverse residual is strictly less than one. Thus neither supremum in (2) is attained, and neither space admits a single parameter \(\varepsilon<1\) making \(u\perp_Bv\Rightarrow v\perp_B^\varepsilon u\) hold for all pairs. Every fixed unit vector nevertheless has suitable parameters strictly below one for both local directions.

## Assumptions and scope
All spaces and functionals are real. For \(n\ge1\), put
\[
p_n=n+2,\qquad q_n=\frac{p_n}{p_n-1},
\]
and take
\[
X=\left(\bigoplus_{n\ge1}\ell_{p_n}^2\right)_{\ell_2},
\qquad
\|z\|_X=\left(\sum_{n\ge1}\bigl(|z_{n,1}|^{p_n}+|z_{n,2}|^{p_n}\bigr)^{2/p_n}\right)^{1/2}.
\tag{3}
\]
Its dual is isometrically identified, under coordinate pairing, with
\[
X^*=\left(\bigoplus_{n\ge1}\ell_{q_n}^2\right)_{\ell_2}.
\tag{4}
\]
The comparison Hilbert norm is
\[
\|z\|_H=\left(\sum_{n\ge1}(|z_{n,1}|^2+|z_{n,2}|^2)\right)^{1/2}.
\]
Since \(p_n\ge2\), for each two-coordinate block
\[
\|z_n\|_{p_n}\le\|z_n\|_2\le2^{1/2-1/p_n}\|z_n\|_{p_n};
\]
consequently
\[
\boxed{\|z\|_X\le\|z\|_H\le\sqrt2\,\|z\|_X.}
\tag{5}
\]
Thus \(X\) is a separable reflexive Hilbert-renormable Banach space.

Recall that \(u\perp_Bv\) means \(\|u+\lambda v\|\ge\|u\|\) for all real scalars \(\lambda\); equivalently some \(f\in J_Z(u)\) satisfies \(f(v)=0\). Chmieliński \(C\)-approximate orthogonality satisfies
\[
v\perp_B^\varepsilon u\quad\Longleftrightarrow\quad \exists g\in J_Z(v): |g(u)|\le\varepsilon\|u\|,
\quad 0\le\varepsilon<1.
\tag{6}
\]
For \(x\in S_Z\), \(C\)-approximate **left** symmetry at \(x\) means that a single \(\varepsilon_x<1\) works for all \(y\in S_Z\) with \(x\perp_By\), reversing the relation in (6); **right** symmetry at \(x\) means a single \(\varepsilon'_x<1\) works for all \(y\perp_Bx\), reversing the order. These parameters may depend on the fixed point.

## Proof
**Step 1: duality and local uniform rotundity.** Every two-dimensional \(\ell_{p_n}^2\) and \(\ell_{q_n}^2\) is smooth and strictly convex. The \(\ell_2\)-sum of these spaces is Gâteaux smooth, strictly convex and LUR. For clarity, here is a proof of the LUR assertion for a general \(\ell_2\)-sum of finite-dimensional strictly convex spaces \(E_n\). Suppose \(a\in S_{(\oplus E_n)_2}\), \(b^k\in S_{(\oplus E_n)_2}\), and \(\|a+b^k\|\to2\). Put \(A_n=\|a_n\|\) and \(B_n^k=\|b_n^k\|\). The norm inequalities
\[
\|a+b^k\|\le\|A+B^k\|_{\ell_2}\le2
\]
show \(\|A-B^k\|_{\ell_2}\to0\). Moreover the nonnegative coordinate defects
\[
(A_n+B_n^k)^2-\|a_n+b_n^k\|^2
\]
have sum tending to zero, hence tend to zero for each fixed \(n\). If \(A_n>0\), this forces \(\|a_n+b_n^k\|\to2A_n\), so finite-dimensional strict convexity (equivalently LUR in finite dimension) yields \(b_n^k\to a_n\). If \(A_n=0\), the convergence \(B_n^k\to0\) does the same. Finally \(\|B^k-A\|_{\ell_2}\to0\) uniformly controls the tails, promoting coordinatewise convergence to \(\|b^k-a\|\to0\). This proves LUR. The dual representation (4) gives LUR and smoothness on both \(X\) and \(X^*\). The norm on \(X\) is nevertheless **not uniformly convex**: in the \(n\)-th \(p_n\)-block take \(a_n=2^{-1/p_n}(1,1)\) and \(b_n=2^{-1/p_n}(1,-1)\), and extend them by zero. Then \(\|a_n\|=\|b_n\|=1\), while \(\|a_n-b_n\|=2^{1-1/p_n}\to2\) and \(\|(a_n+b_n)/2\|=2^{-1/p_n}\to1\). Thus no positive modulus of convexity can exist for any fixed \(0<\varepsilon<2\).

**Step 2: LUR guarantees both pointwise uniform symmetry bounds.** We prove a lemma valid for any real LUR Banach space \(Z\), without requiring smoothness. If \(a,b\in S_Z\) and \(a\perp_Bb\), then
\[
\|a-b\|\ge1\quad\text{and}\quad\|a+b\|\ge1,
\tag{7}
\]
because a norming functional at \(a\) vanishes on \(b\). Fix \(a\in S_Z\). If the left local \(C\)-symmetry bound failed, there would be \(b^k\in S_Z\) with \(a\perp_Bb^k\) and
\[
\inf_{g\in J(b^k)}|g(a)|\to1.
\]
Choosing \(g_k\in J(b^k)\), and passing to a subsequence with the sign of \(g_k(a)\) fixed, LUR at \(a\) gives \(b^k\to a\) or \(b^k\to-a\), because \(\|a\pm b^k\|\ge|g_k(a)\pm g_k(b^k)|\to2\). This contradicts (7). Hence the left bound is strictly less than one. For the right local bound, if \(b^k\perp_Ba\) and \(\inf_{g\in J(a)}|g(b^k)|\to1\), choose \(g_k\in J(a)\) and use the same LUR argument to obtain \(b^k\to\pm a\), again contrary to (7) applied in reverse order. Thus **every unit vector in any LUR space is individually \(C\)-approximately left- and right-symmetric.** This lemma applies to \(X\) and to \(X^*\).

**Step 3: explicit asymptotically maximal reverse defects.** Let \(p>2\),
\[
t_p=1-p^{-1/2},\qquad
A_p=(1+t_p^p)^{1/p},\qquad
B_p=(1+t_p^{p(p-1)})^{1/p},
\]
and define normalized two-coordinate vectors
\[
u_p=\frac{(1,t_p)}{A_p},\qquad
v_p=\frac{(-t_p^{p-1},1)}{B_p}.
\tag{8}
\]
The unique norming functional of a unit vector \((s,t)\) in \(\ell_p^2\) is
\[
j_p(s,t)=\big(\operatorname{sgn}(s)|s|^{p-1},\operatorname{sgn}(t)|t|^{p-1}\big).
\]
Therefore
\[
j_p(u_p)(v_p)=\frac{-t_p^{p-1}+t_p^{p-1}}{A_p^{p-1}B_p}=0,
\tag{9}
\]
while
\[
\boxed{j_p(v_p)(u_p)=r_p
=\frac{t_p-t_p^{(p-1)^2}}{(1+t_p^p)^{1/p}(1+t_p^{p(p-1)})^{(p-1)/p}}.}
\tag{10}
\]
In particular \(u_p\perp_Bv_p\). Since \(1-s\le e^{-s}\) for \(s\ge0\),
\[
0<t_p^p\le e^{-\sqrt p},\qquad
0<t_p^{(p-1)^2}\le e^{-(p-1)^2/\sqrt p}.
\]
The denominator in (10) equals \(1+O(e^{-\sqrt p})\), so
\[
 r_p=1-p^{-1/2}+O(e^{-\sqrt p}),
 \qquad \boxed{\sqrt p\,(1-r_p)\longrightarrow1.}
\tag{11}
\]
Embed \(u_{p_n},v_{p_n}\) into the \(n\)-th block of \(X\), setting all other blocks to zero. Their global norming functionals have the same single-block support, so (9)--(11) hold unchanged. Consequently \(\sigma_C(X)=1\).

**Step 4: no pair attains the global defect.** In any strictly convex real Banach space, for unit \(a,b\) with \(a\perp_Bb\) no \(g\in J(b)\) can satisfy \(|g(a)|=1\): otherwise strict convexity of the exposed face implies \(a=\pm b\), contradicting \(a\perp_Bb\). Hence every reverse residual is strictly less than one, and the supremum for \(X\) is not attained.

**Step 5: the dual has the same failure.** Because \(X\) is reflexive, smooth, and strictly convex, the duality mapping \(j_X:S_X\to S_{X^*}\) is bijective with inverse \(j_{X^*}\) after the canonical embedding into \(X^{**}\). If \(u\perp_Bv\) in \(X\), put \(U=j_X(v)\) and \(V=j_X(u)\). Then
\[
 j_{X^*}(U)(V)=v(j_X(u))=j_X(u)(v)=0,
\]
so \(U\perp_BV\) in \(X^*\), and its reverse defect is
\[
 j_{X^*}(V)(U)=u(j_X(v))=j_X(v)(u).
\tag{12}
\]
Thus the same sharp witness sequence transfers to \(X^*\), proving \(\sigma_C(X^*)=1\); strict convexity of \(X^*\) again excludes attainment. This completes the result.

## Verification
The supplementary standalone `verify.py` evaluates (8)--(10), checks the exact rational support cancellation for square exponents \(p\), verifies exact normalization identities via their \(p\)-th powers, and compares the large-\(p\) reverse defect and its predicted \(p^{-1/2}\) deficit. The finite test is **not** an infinite-dimensional proof; (5), the LUR lemma, and (9)--(12) give the analytic result without numerical extrapolation.

The code requires only Python's standard library and can be run as `python verify.py` from the same package directory. A successful run emits `VERIFY_OK` and the checked dimensions/exponents.

## Relationship to prior work
Chmieliński, Khurana and Sain (arXiv:2012.08162v1, first public 15 December 2020, primary MSC 46B20) study global and local \(C\)- and \(D\)-approximate Birkhoff--James symmetry. Their Section 3 establishes local properties and a compact-set uniformity theorem, and explicitly cites Chmieliński--Wójcik (2018), Example 3.7, as an **already known infinite-dimensional smooth example** lacking global \(C\)-approximate symmetry. No novelty is claimed for a merely smooth counterexample.

The additional distinction proved here is a specific Hilbert-equivalent \(\ell_2\)-sum whose **primal and dual are both LUR and smooth**, whose **every individual vector admits both uniform local direction bounds**, and whose **global unit defect is approached at an explicit rate but never attained**. Smoothness alone does not yield those strengthened properties. The full 2020 arXiv text was examined through its definitions, Section 3, the infinite-dimensional precedent, and the compact-set result. The 2018 defining predecessor is available in abstract/bibliographic form only for this comparison, making potential prior coverage of the stronger structural package a real originality risk.

A published 2026 result, “Zero Birkhoff saturation without an extremal pair in a reflexive strictly convex space”, studies the space \(Y=(\bigoplus_{k\ge2}\ell_{1+1/k}^2)_{\ell_2}\), **isometric to the present dual \(X^*\) after reindexing**. It proves nonattained saturation for an orthogonality-constrained James constant using coordinate vectors. Those coordinate pairs have *zero* reverse \(C\)-defect, and the published result does not compute global \(C\)-asymmetry, local left/right bounds, or the rate in (11). This is an exact same-space comparison with a logically different invariant, not merely a title distinction. Exact Dragomir-symmetry calculations concern another approximate-orthogonality relation. Previously tabulated regular-polygon \(C\)-symmetry parameters and the cubic plane \(C\)-symmetry parameter concern individual finite-dimensional spaces and do not imply this infinite-dimensional pointwise/global separation.

## Limitations
The example is a specially chosen equivalent norm on a separable real Hilbert space, not a claim about the usual Hilbert norm or about every reflexive/LUR norm. It is not uniformly convex in this norm, which is consistent with known positive global \(C\)-symmetry results for uniformly convex spaces. The statement does not claim failure of approximate symmetry in Dragomir's different sense, or a sharp universal function of the Banach--Mazur distortion. The 2018 article containing the earlier smooth counterexample was not available as verified full text; independent comparison of its Example 3.7 against the LUR, dual, local-parameter, and quantitative features remains a bibliographic risk.

## References
1. J. Chmieliński, D. Khurana, D. Sain, “Local approximate symmetry of Birkhoff--James orthogonality in normed linear spaces,” arXiv:2012.08162v1 (15 December 2020), *Results in Mathematics* 76 (2021), article 136, doi:10.1007/s00025-021-01437-y (primary MSC 46B20).
2. J. Chmieliński and P. Wójcik, “Approximate symmetry of Birkhoff orthogonality,” *Journal of Mathematical Analysis and Applications* 461 (2018), 625--640, doi:10.1016/j.jmaa.2018.01.031 (abstract and secondary discussion inspected; full text unavailable).
3. J. Chmieliński, T. Stypuła and P. Wójcik, “Approximate orthogonality in normed spaces and its applications,” *Linear Algebra and its Applications* 531 (2017), 305--317, doi:10.1016/j.laa.2017.06.001 (support-functional characterization).
4. “Zero Birkhoff saturation without an extremal pair in a reflexive strictly convex space”, published mathematical research record (2026); original public RESULT.md inspected for its exact \(\ell_2\)-sum construction and orthogonality-constrained James constant.
