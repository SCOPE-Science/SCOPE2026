# Repdigit rigidity and a Pell spectrum of Gaussian digit-square fixed points

## Finding

**Theorem.** Fix an integer base \(B\ge2\). For any integer length \(m\ge1\), integers \(a,t\) with \(|a|<B\) and \(0<|t|<B\), define
\[
R_m(B)=\sum_{j=0}^{m-1}B^j,\qquad z=a+i tR_m(B).
\]
For the signed-coordinate Gaussian base-\(B\) digit-square map \(S_B\), the point \(z\) is fixed if and only if
\[
m=2,\qquad a=\frac{B+1}{2},\qquad B^2-8t^2=1.
\]
Thus the only possible length of a nonzero constant imaginary repdigit in a fixed point with a single real digit is two. All the solutions, including the two signs of the imaginary coordinate, are
\[
B_n+t_n\sqrt8=(3+\sqrt8)^n,\qquad
z_n^{\pm}=\frac{B_n+1}{2}\pm i t_n(B_n+1),\quad n=1,2,\ldots .
\]
The first base/point pairs are \(B=3\), \(2\pm4i\); \(B=17\), \(9\pm108i\); \(B=99\), \(50\pm3500i\); and \(B=577\), \(289\pm117912i\). For real \(X\ge2\), the exact number of bases \(B\le X\) admitting this digit pattern is
\[
N(X)=\left\lfloor\frac{\operatorname{arcosh}X}{\log(3+\sqrt8)}\right\rfloor,
\]
so \(N(X)=\log(X)/\log(3+\sqrt8)+O(1)\). These are not asserted to be the only bases containing *other* kinds of nonreal fixed points.

## Assumptions and scope

For \(B\ge2\), write a Gaussian integer in its unique componentwise signed base-\(B\) expansion \(w=\sum_{j\ge0}(u_j+i v_j)B^j\), with integer digits satisfying \(|u_j|,|v_j|\le B-1\), the nonzero digits of each component having its component's sign. Define \(S_B(w)=\sum_{j\ge0}(u_j+i v_j)^2\), including \(S_B(0)=0\), as in Baker Swart--Crook--Grundman--Hall-Seelig. A **nonzero imaginary repdigit** is \(tR_m(B)\), with the same signed nonzero digit \(t\) at exactly \(m\) positions. A **single real digit** means an integer \(a\) satisfying \(|a|<B\), permitting a zero or negative real coordinate. The classification is over all bases, lengths, and signed digit choices in this precise digit-pattern family.

## Proof

The expansion of \(z=a+i tR_m(B)\) has Gaussian low digit \(a+it\) and \(m-1\) further digits \(it\), so direct squaring gives the exact identity
\[
S_B(z)=(a+it)^2+(m-1)(it)^2=(a^2-mt^2)+2at\,i.
\]
Since \(t\ne0\), the imaginary coordinate of \(S_B(z)=z\) requires \(2a=R_m(B)\); its real coordinate requires \(a(a-1)=mt^2\). For \(m=1\), \(2a=1\) has no integral solution. For every \(m\ge3\), \(R_m(B)\ge B^2+B+1>2(B-1)\ge2a\), an impossibility. Hence \(m=2\), and \(2a=B+1\). Substituting this into \(a(a-1)=2t^2\) gives \(B^2-8t^2=1\). Conversely, any nonzero integral \(t\) satisfying this equation and \(a=(B+1)/2\) satisfies both coordinates of the fixed-point equation. These conditions automatically give admissible digits: \(B\ge3\) is odd, \(1\le a<B\), and \(0<|t|<B\).

For completeness, the positive integral solutions of \(B^2-8t^2=1\), with \(B\ge2\) and \(t>0\), are exactly the powers of the fundamental unit \(3+\sqrt8\). Indeed, \((3+\sqrt8)^n=B_n+t_n\sqrt8\) is integral, positive and of norm one for every \(n\ge1\). For the reverse direction, if \(t=1\), then \(B=3\). If \(t\ge2\), multiply \(B+t\sqrt8\) by \(3-\sqrt8\) to obtain
\[
B'=3B-8t,\qquad t'=3t-B.
\]
The inequalities \(\sqrt8\,t<B<3t\) for \(t>1\) give \(B'>0\), \(t'>0\); moreover \(B>2t\) gives \(t'<t\), and the norm remains one. Repeating this strict positive-integer descent reaches \((B,t)=(3,1)\), whose inverse image is \((1,0)\). Thus every solution is the indicated unique power; replacing \(t\) by \(-t\) gives its conjugate. Finally, with \(\lambda=3+\sqrt8\), the identity \(B_n=(\lambda^n+\lambda^{-n})/2=\cosh(n\log\lambda)\) and monotonicity of \(\cosh\) on nonnegative arguments establish the stated exact counting formula.

## Verification

The self-contained integer checker `verify.py` implements the signed-component digit expansion independently of the algebraic reduction. It checks all possible signed \(a,t\), lengths \(1\le m\le4\), and bases \(2\le B\le120\), finding exactly the six predicted fixed points at bases \(3\), \(17\), and \(99\), with both signs. It also generates the first twelve Pell solutions by the recurrence and directly checks \(S_B(z_n^\pm)=z_n^\pm\), verifying all digit bounds. Run `python3 verify.py`; successful output ends in `VERIFY_OK`. Exhaustive finite verification is a cross-check and is not used to prove the all-base claim.

## Relationship to prior work

Baker Swart, Crook, Grundman and Hall-Seelig introduced this Gaussian digit-square map and classified all fixed points for bases \(2\le B\le10\) in Theorem 6 and Tables 1--2 of their open 2021 preprint. In particular, their base-\(3\) table already contains \(2\pm4i\), the first member of this family. Their Theorem 7 instead constructs two **real** fixed points in every odd base. The present claim classifies a naturally distinguished **nonreal repdigit-pattern family across all bases**; it neither reclaims the known base-\(3\) point nor asserts a classification of all nonreal fixed points. The Pell equation and its classical positive solutions are also known independently; the new mathematical assertion is their exact occurrence, digit-length rigidity, and base spectrum under this Gaussian digit-square map.

A search of related literature and published mathematical-result records, including equivalent formulations involving square-triangular numbers and the Pell equation, did not identify a result covering this digit-pattern classification. A later journal version of the originating article was not available in complete text for a separate comparison; its publicly available 2021 preprint was inspected in full.

## Limitations

The theorem concerns fixed points, **not** Gaussian numbers whose iterates reach \(1\): these nonunit fixed points are not happy numbers in that latter sense. It does not classify fixed points with multiple real digits or a nonconstant imaginary digit string, nor periods exceeding one. The verified family of bases has logarithmic counting growth, but other bases may have nonreal fixed points of different digit shapes.

## References

1. B. Baker Swart, S. Crook, H. G. Grundman, and L. L. Hall-Seelig, *Gaussian Happy Numbers*, arXiv:2101.00560v1 (first publicly posted 2021-01-03), especially Definition 1, Theorems 4, 6 and 7, and Tables 1--2. https://arxiv.org/pdf/2101.00560
2. Same authors, *Gaussian Happy Numbers*, Rocky Mountain Journal of Mathematics 52 (2022), 415--429, DOI: 10.1216/rmj.2022.52.415. Bibliographic and abstract comparison; the separate journal full text was not inspected.
3. Classical Pell equation \(B^2-8t^2=1\) / square-triangular number correspondence (used only as established arithmetic background; classification under the Gaussian map is the claim here).
