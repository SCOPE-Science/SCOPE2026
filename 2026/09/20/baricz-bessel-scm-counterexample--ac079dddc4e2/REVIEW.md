# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof reduces the required sign to one Bessel ratio and then certifies that ratio with exact rational inequalities.

For \(F_\nu(x)=x^{\nu+1}e^{-x}I_\nu(x)\), setting \(a=2\nu+1\) and \(r=I_{\nu+1}/I_\nu\) gives
\[
F_\nu'/F_\nu=a/x-1+r
\]
and, from the standard modified-Bessel recurrences,
\[
r'=1-(a/x)r-r^2.
\]
Differentiation yields
\[
F_\nu''/F_\nu
=2-2r-2a/x+ar/x+a(a-1)/x^2.
\]
At \((\nu,x)=(-15/16,2)\), this is
\[
841/256-(39/16)r.
\]

The series normalization at \(x=2\) was checked directly:
\[
r=16B/A,\quad
A=\sum_{k\ge0}\frac1{k!(1/16)_k},\quad
B=\sum_{k\ge0}\frac1{k!(17/16)_k}.
\]
The stated partial sums are exact. The ratio of successive \(A\)-terms is
\[
16/((k+1)(16k+1)),
\]
so after \(k=4\) it is at most \(16/325\), validating the geometric upper bound on the positive tail. Combining that upper bound for \(A\) with the lower truncation for \(B\) gives
\[
r>\frac{58189629168}{42817909615}>\frac{841}{624}.
\]
Consequently the displayed exact upper bound for \(F_\nu''(2)/F_\nu(2)\) is negative. Since \(F_\nu(2)>0\), \(F_\nu''(2)<0\), which is incompatible with complete monotonicity.

The accompanying exact-arithmetic artifact reproduces all rational values and sign checks. No numerical approximation is needed for the proof.

The continuity extension is also sound: for fixed positive \(x\), the defining hypergeometric series and its differentiated forms depend continuously on \(\nu\) on compact subsets of \((-1,\infty)\), away from gamma poles. The strict negative value at \(-15/16\) therefore persists locally.

## Originality

Baricz (2010), at the end of Section 2, explicitly asks in part (b) whether \(x^{\nu+1}e^{-x}I_\nu(x)\) is SCM for all \(\nu\in(-1,-1/2]\). The present result directly negates that universal statement.

The literature check included the exact expression and problem wording, complete-monotonicity variants, modified-Bessel ratio formulations, the source paper and later citation chains. Hornik and Grün (2013) give systematic Amos-type bounds for \(I_{\nu+1}/I_\nu\) over a range containing the counterexample order, but do not state this higher-order sign conclusion. Salazar (2026) uses Riccati reductions and exact certificates for several other modified-Bessel open problems and explicitly treats a different Baricz complete-monotonicity transfer problem; the listed resolved questions do not include Section 2(b).

The rational truncation-plus-tail device is not claimed as a new general method. The originality claim is the mathematical counterexample to the specific 2010 SCM question. To the best of our knowledge no prior counterexample was located. A differently worded or non-indexed equivalent result remains a residual risk.

## Value

This closes an explicit open yes/no question in the negative, with a short certificate at a rational order. The result is stronger than a single isolated numerical observation because the strict sign persists for an open interval of nearby orders.

## Limitations

The result does not classify the entire order interval \((-1,-1/2]\), determine the boundary of the failing region, or address Baricz's parts (a) and (c). It also does not exclude the possibility of a prior result under substantially different terminology.
