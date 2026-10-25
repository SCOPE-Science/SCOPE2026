# Inverse-branch law for the four-digit Kaprekar map in every base

## Finding

For each integer base \(b\ge2\), consider the map \(K_b\) on the \(b^4\) four-digit strings (leading zeros permitted): arrange the four digits descending, subtract the ascending arrangement, and retain four positions. The image has exactly
\[
\frac{(b-1)(b+2)}2+1
\]
distinct elements, including zero. For positive outputs, put
\[
Y_b(u,v)=(b^3-1)u+(b^2-b)v,\quad 1\le u\le b-1,\quad 0\le v\le u.
\]
These are **all** positive outputs and they are distinct. The number \(F_b(u,v)\) of four-digit inputs mapping to \(Y_b(u,v)\) is exactly
\[
F_b(u,v)=(b-u)\begin{cases}12u-4,&v=0,\\24(u-v),&0<v<u,\\6,&v=u.\end{cases}
\]
The output zero has exactly \(b\) preimages (constant-digit strings). Among positive outputs, the greatest inverse-fiber size is \(8\) for \(b=2\), and
\[
24\left\lfloor\frac{(b-1)^2}{4}\right\rfloor\quad(b\ge3).
\]
For odd \(b\ge3\), one positive output attains this maximum; for even \(b\ge4\), exactly two outputs do.

There is also a universal *limiting inverse-branch distribution*. Choose uniformly from the positive elements of the image of \(K_b\) and let \(Q_b\) be its number of preimages divided by \(b^2\). Then \(Q_b\) converges in distribution to a random variable \(Q\) supported on \([0,6]\), with the exact upper-tail function for \(0<y<6\)
\[
\Pr(Q\ge y)=\sqrt{1-y/6}-\frac{y}{12}\log\left(\frac{1+\sqrt{1-y/6}}{1-\sqrt{1-y/6}}\right).
\]
At \(y=0\), the tail is \(1\); at \(y=6\), it is \(0\).

## Assumptions and scope

The input set comprises all ordered four-tuples of digits \((a_3,a_2,a_1,a_0)\in\{0,\ldots,b-1\}^4\), including strings beginning in zero. Strings with all digits equal are retained as the \(b\) preimages of zero. All fibers count ordered strings rather than multisets. The limiting law samples a **uniform image output**, not a uniformly chosen input; these are different distributions. The theorem concerns *one application* of the map only and makes no assertion about future cycles or attraction times.

## Proof

Write the ordered digits of an input as \(A\ge B\ge C\ge D\). Set \(u=A-D\) and \(v=B-C\). If the digits are not all equal, \(1\le u\le b-1\) and \(0\le v\le u\); subtraction gives
\[
K_b=(b^3-1)u+(b^2-b)v.
\]
Every permitted pair is realizable: take \(D=C=0\), \(B=v\), and \(A=u\). Equality of two expressions implies \(u\equiv u'\pmod b\), because \(b^3-1\equiv-1\pmod b\) while \(b^2-b\equiv0\pmod b\). Since \(u,u'\) lie in \([1,b-1]\), they coincide; then \(v=v'\). Summing \(u+1\) over \(1\le u\le b-1\) establishes the image cardinality.

For a specified \((u,v)\), choose the minimum digit \(D\) in \(b-u\) ways. Then \(A=D+u\), \(C=D+s\), \(B=D+s+v\), where the integer \(s\) ranges through \(0,1,\ldots,u-v\). Count the permutations of each four-multiset:

* If \(v=0\), the two endpoint values of \(s\) give triples of equal digits, with four permutations each. Each of the \(u-1\) interior choices gives one equal pair, with twelve permutations. This totals \(12u-4\).
* If \(0<v<u\), each endpoint gives one equal pair and twelve permutations; the \(u-v-1\) interior choices have four distinct digits and twenty-four permutations. The total is \(24(u-v)\).
* If \(v=u\), there is only \(s=0\), with two pairs of equal digits, giving six permutations.

Multiplying by \(b-u\) proves the complete formula. For \(b\ge3\), the largest middle-branch fiber occurs at \(v=1\), with \(u-1\) and \(b-u\) as equal as possible; its size is the claimed maximum and it has one or two maximizers according to parity. For \(u\ge2\), the \(v=0\) branch has size \((b-u)(12u-4)\le24(b-u)(u-1)\), and for \(u=1\) it has size \(8(b-1)\le24(b-2)\) when \(b\ge3\). The diagonal branch \(v=u\) is smaller. The base-two case is direct.

For the limit law, all except \(O(b)\) of the positive output pairs satisfy \(0<v<u<b\). Under the uniform distribution on output pairs, the scaled coordinates \((u/b,v/b)\) converge by two-dimensional Riemann sums to the uniform distribution (density \(2\)) on \(0<v<u<1\). On the interior, the scaled fiber size is
\[
\frac{F_b(u,v)}{b^2}=24(1-u/b)(u/b-v/b).
\]
Under the change of coordinates \(s=1-u\), \(t=u-v\), the limiting pair is uniform on the triangle \(s>0,t>0,s+t<1\), and \(Q=24st\). With \(z=y/24\) and \(0<z<1/4\), the domain \(st\ge z\) has \(s\) between \((1\pm\sqrt{1-4z})/2\) and area
\[
\int_{s_-}^{s_+}(1-s-z/s)\,ds.
\]
Twice this area equals \(\sqrt{1-4z}-2z\log((1+\sqrt{1-4z})/(1-\sqrt{1-4z}))\), yielding the asserted upper-tail formula. The boundary limits give the endpoint values.

## Verification

The standalone file `verify_inverse.py` independently enumerates all ordered four-digit strings for bases \(2\) through \(22\), constructs the subtraction map from the actual sorted digits, and compares the entire image-to-fiber dictionary against the explicit formulas. It checks the output count, total input mass, maximum and number of maximizing fibers. The recorded result is `VERIFY_OK`. The analytic limit follows from the Riemann-sum argument, not from finite tests.

## Relationship to prior work

The classical Kaprekar process and its nonzero decimal fixed point predate this result. The difference-coordinate representation of the four-digit transformation is also established in the literature, including Walden's computational framework and Hanover's analysis; it is therefore not claimed as new. This finding concerns the *complete inverse-fiber multiplicity function for arbitrary bases* and its universal continuous limit law under uniform selection of an image output. The inspected sources focus on terminal cycles, fixed points, and empirical forward trajectory lengths rather than providing these precise inverse-branch formulas. A prior equivalent not located by accessible searches remains possible.

## Limitations

This theorem does not classify eventual cycles or prove convergence in four-digit dynamics. The full text of some early primary sources could not be obtained; publication priority remains subject to further literature review. The self-review is not independent validation. The limit law is for outputs uniformly distributed over the image, **not** for outputs generated by uniform random inputs.

## References

1. D. R. Kaprekar, "Another Solitaire Game," *Scripta Mathematica* 15 (1949), 244–245.
2. OEIS Foundation, A099009, "Fixed points of the Kaprekar map," original entry dated 2004-09-22: https://oeis.org/A099009 .
3. B. L. Walden, "Searching for Kaprekar's constants: algorithms and results," *Integers* 5 (2005), A8.
4. D. Hanover, "The Base Dependent Behavior of Kaprekar's Routine," arXiv:1710.06308 (2017): https://arxiv.org/pdf/1710.06308 .
5. Z. Wang and W. Lu, "On 2-digit and 3-digit Kaprekar's Routine," arXiv:2101.09708 (2021): https://arxiv.org/pdf/2101.09708 .
6. A. Yamagami and Y. Matsui, "On Some Formulas for Kaprekar Constants," *Symmetry* 11 (2019), 885: https://doi.org/10.3390/sym11070885 .
