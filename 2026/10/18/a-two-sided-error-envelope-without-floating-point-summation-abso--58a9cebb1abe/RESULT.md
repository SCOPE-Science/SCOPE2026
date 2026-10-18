# A two-sided error envelope without floating-point summation absorption

## Finding

Let \(p\ge3\). In ideal normalized binary precision-\(p\) arithmetic with unbounded exponents, nearest-even rounding, and positive representable inputs \(x_1,\ldots,x_m\), perform left-to-right accumulation
\[
s_1=x_1,\qquad s_i=\operatorname{RN}_p(s_{i-1}+x_i),\quad 2\le i\le m.
\]
Suppose **every update strictly advances the accumulator**, \(s_i>s_{i-1}\). Denote the computed result by \(F=s_m\) and the exact real sum by \(S=\sum_{i=1}^m x_i\). Then
\[
\boxed{\frac{F+x_1}{2}\le S\le\bigl(\frac32+2^{-p}\bigr)F-\frac{x_1}{2}.}\tag{1}
\]
In particular, counting total absorptions and observing zero does not imply small relative summation error. There are families without any absorbed addition for which the ratio \(F/S\) approaches \(2\), and other families where it approaches \(2/3\), in the successive limits described below. These two asymptotic constants are universally sharp.

## Assumptions and scope

A positive precision-\(p\) floating-point number has form \(k2^e\), with \(e\in\mathbb Z\) and a normalized \(p\)-bit significand \(k\). Exponents are unbounded, so no underflow, overflow, subnormals, or fused operations intervene. Each binary addition is correctly rounded to nearest, with ties resolved to an even significand. All \(m\ge1\) inputs are positive representable numbers. The no-absorption condition means strictly increasing *computed* partial sums; it is stronger than merely requiring a positive true sum, but can be checked from the sequence of computed updates. The upper coefficient in (1) is explicitly not asserted optimal at each fixed \(p\).

## Proof

For any representable \(v>0\), write \(g_-(v)=v-\operatorname{pred}(v)\) and \(g_+(v)=\operatorname{succ}(v)-v\). Under correct round-to-nearest, if \(v=\operatorname{RN}_p(y)\), its exact input lies between the midpoints of the two adjacent representable values:
\[
v-\tfrac12 g_-(v)\le y\le v+\tfrac12g_+(v).
\]
Endpoints can be included regardless of the tie parity; their inclusion only weakens the bounds. Set \(\Delta_i=s_i-s_{i-1}>0\). Applying the midpoint enclosure to \(y=s_{i-1}+x_i\) and \(v=s_i\) yields
\[
\Delta_i-\tfrac12g_-(s_i)\le x_i\le\Delta_i+\tfrac12g_+(s_i).\tag{2}
\]
The preceding accumulator is itself representable and strictly smaller than \(s_i\), hence \(\Delta_i\ge g_-(s_i)\). The left inequality of (2) thus gives \(x_i\ge\Delta_i/2\). Summing and using \(\sum_{i=2}^m\Delta_i=F-x_1\) proves the first half of (1).

A normalized binary float \(v\) that is not an exact power of two has equal predecessor and successor gaps: \(g_+(v)=g_-(v)\). For such \(s_i\), (2) gives \(x_i\le3\Delta_i/2\). If \(s_i=2^e\), the gap below is \(g_-(s_i)=2^{e-p}\) and the gap above is twice that; therefore
\[
x_i\le\Delta_i+g_-(s_i)\le\tfrac32\Delta_i+\tfrac12 2^{e-p}.\tag{3}
\]
Because the computed sequence increases strictly, it reaches each power of two at most once. For \(F<2^{E+1}\), the total contribution from the exceptional upper terms (3) is bounded by
\[
\frac12\sum_{2^e\le F}2^{e-p}\le 2^{E-p}\le 2^{-p}F.
\]
The geometric sum extends over all integral exponents below \(E\), including negative ones, so convergence is exact. Summing (2) and (3) proves the second half of (1). The case \(m=1\) is immediate.

To prove asymptotic sharpness, begin with \(s_1=x_1=1\) and, in each binade \([2^e,2^{e+1})\), move through **each consecutive representable float** until the terminal value \(F=2^J\), for any integer \(J\ge1\). Let \(\Delta=2^{e-p+1}\) be the spacing from the current accumulator to its immediate successor. In the first construction choose the positive representable addend
\[
x^{\rm low}=(\tfrac12+2^{-p})\Delta.
\]
This is representable using a normalized significand \(1+2^{1-p}\). Since it lies strictly above the nearest-neighbor midpoint and below the next float, it rounds the accumulator to its immediate successor. Thus every update strictly advances it, while summation of the *exact* addends gives
\[
S_{\rm low}=1+(\tfrac12+2^{-p})(2^J-1),\qquad F=2^J.\tag{4}
\]
In the second construction choose
\[
x^{\rm high}=(\tfrac32-2^{1-p})\Delta.
\]
This is another positive representable number; it lies between one and three-halves local successor gaps. For an ordinary within-binade addition, it lies strictly on the immediate-successor side of the midpoint separating that successor from the second successor. At a binade boundary the successor gap increases, making that rounding assertion even clearer. Consequently every update again rounds to the immediate successor, and
\[
S_{\rm high}=1+(\tfrac32-2^{1-p})(2^J-1),\qquad F=2^J.\tag{5}
\]
For each fixed \(p\), taking \(J\to\infty\) in (4) and (5) yields ratios \(1/(\tfrac12+2^{-p})\) and \(1/(\tfrac32-2^{1-p})\). Taking \(p\to\infty\) then yields \(2\) and \(2/3\). By (1), neither limiting leading constant can be improved uniformly in precision. These constructions use strictly positive exactly representable inputs and produce no total absorption at any addition.

## Verification

The accompanying `verify.py` implements exact rational nearest-even binary rounding without relying on a host floating-point unit. It checks that both constructed input sequences are representable and advance the accumulator one representable value at a time for multiple precisions and exponent ranges; it then checks (1), the claimed exact sums, and additional randomly generated exact additions. Run `python verify.py` (Python standard library only). All universal claims above are proved analytically; finite computation is not a substitute for the midpoint and geometric-sum arguments.

## Relationship to prior work

Mikaitis and Woolfenden (arXiv:2610.10819, first posted 7 October 2026), Sections 3–4, formalize total/near-total stagnation and instrument its detection. Their paper explicitly observes that other numerical errors can remain when few stagnations are seen, but does not in the inspected full text state the positive-addend, zero-absorption, two-sided envelope (1) with both sharp asymptotic constructions. Their more sensitive near-total-stagnation diagnostic can flag some behavior of these examples; this result addresses specifically what a zero **total-absorption count** can and cannot certify. Higham's general recursive-summation error analyses and Hallman–Ipsen's broad summation bounds precede this work; neither their general error framework nor the standard nearest-neighbor rounding fact is claimed as new. The high-precision endpoint constructions and the no-absorption constraint are the particular claims under consideration.

## Limitations

The exponent range is unbounded, while actual IEEE formats have a maximum exponent. The sharpness construction uses increasing numbers of exponent binades, so a fixed physical format only realizes a finite part of the asymptotic sequence. Results are restricted to strictly positive summands and correctly rounded binary nearest-even arithmetic. The coefficient \(3/2+2^{-p}\) is a convenient explicit bound, not an exact best constant for each fixed precision. Classical summation and machine-arithmetic literature could contain equivalent conditional bounds not identified here; independent bibliographic review has not occurred. Counting near-total or partial stagnations, or recording exact rounding residues, gives more information than merely counting totally absorbed additions.

## References

1. M. Mikaitis and W. Woolfenden, *Analysis and Detection of Stagnation in Floating-Point Summation*, arXiv:2610.10819, first version 7 October 2026; full text version 2 (9 October 2026), Sections 3–4. https://arxiv.org/html/2610.10819v2
2. N. J. Higham, *The Accuracy of Floating Point Summation*, SIAM Journal on Scientific Computing 14 (1993), 783–799. DOI: 10.1137/0914050. Publisher abstract inspected; full paper not accessed.
3. E. Hallman and I. C. F. Ipsen, *Deterministic and Probabilistic Error Bounds for Floating Point Summation Algorithms*, arXiv:2107.01604 (2021). Abstract inspected; full text not accessed.
