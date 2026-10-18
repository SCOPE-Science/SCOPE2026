# Sharp finite-path variation for unimodal data and peak-location rigidity

## Finding
For every integer \(n\ge3\), let \(P_n\) be the path with ordered vertices \(0,\ldots,n-1\), endowed with counting measure and its graph metric. Its centered Hardy--Littlewood maximal operator is
\[
(Mf)(j)=\max_{0\le r\le n-1}\frac{1}{|B(j,r)|}\sum_{i\in B(j,r)}f(i),\qquad B(j,r)=\{i:0\le i<n,\ |i-j|\le r\}.
\]
Suppose \(f:P_n\to[0,\infty)\) is unimodal: for some \(p\in\{0,\ldots,n-1\}\),
\[
f(0)\le\cdots\le f(p)\ge\cdots\ge f(n-1).
\]
Write \(\operatorname{Var}(f)=\sum_{j=0}^{n-2}|f(j+1)-f(j)|\), \(h=f(p)\), \(A=h-f(0)\) and \(B=h-f(n-1)\). Then \(Mf\) is unimodal with the **same permissible peak index** \(p\), and
\[
\boxed{\operatorname{Var}(Mf)\le\left(1-\frac1n\right)\operatorname{Var}(f).}
\]
The constant \(1-1/n\) is sharp on this unimodal class for every \(n\). More precisely, the following peak-location deficit is nonnegative:
\[
\boxed{\left(1-\frac1n\right)\operatorname{Var}(f)-\operatorname{Var}(Mf)
\ \ge A\left(\frac1{p+1}-\frac1n\right)+B\left(\frac1{n-p}-\frac1n\right).}
\]
For nonconstant nonnegative unimodal \(f\), equality in the sharp factor bound occurs **if and only if** \(f\) consists of a constant baseline and one strictly higher *endpoint* value. Constant data give the trivial zero-variation equality. In particular, nonconstant unimodal data with a genuinely interior peak are strictly subextremal. Consequently, any counterexample to the full, unrestricted finite-path conjecture must have at least two separated peaks in its absolute-value profile; one-peak profiles cannot be counterexamples.

## Assumptions and scope
The maximal operator uses centered graph balls of all integer radii and equal vertex weights, not arbitrary intervals or uncentered balls. The variation is edge \(1\)-variation. Nonnegativity is part of the sharp equality classification; an arbitrary real input \(g\) whose modulus \(|g|\) is unimodal also obeys the inequality because \(Mg=M|g|\) and \(\operatorname{Var}(|g|)\le\operatorname{Var}(g)\). No equality classification is asserted for signed data. The index \(p\) may be any point on a plateau of maxima, and the stated deficit holds separately for every permissible such index.

## Proof
**1. Preservation of the rising branch.** Fix \(j<p\). Let \(r\) realize \(Mf(j)\) (the maximum is over finitely many radii). If \(Mf(j)\le f(j+1)\), then \(Mf(j+1)\ge f(j+1)\ge Mf(j)\). Otherwise \(Mf(j)>f(j+1)\), so \(r\ge1\). The ball \(B(j+1,r-1)\) is a nonempty subset of \(B(j,r)\): its right endpoint is unchanged, and its left endpoint moves right by at most two sites. Every removed site has index at most \(j\), hence its value is at most \(f(j+1)\) by monotonicity up to \(p\). Removing entries strictly below the original average cannot decrease that average. It follows that
\[
Mf(j+1)\ge \frac1{|B(j+1,r-1)|}\sum_{i\in B(j+1,r-1)}f(i)
\ge Mf(j).
\]
Reflecting the path gives \(Mf(j)\ge Mf(j+1)\) for \(j\ge p\). This establishes unimodality of \(Mf\). Since \(f(p)=h\) is the global maximum, the singleton ball and the upper bound on all averages give \(Mf(p)=h\).

**2. Telescoping variation.** Since both profiles increase to \(p\) and decrease thereafter,
\[
\operatorname{Var}(f)=2h-f(0)-f(n-1)=A+B,
\]
\[
\operatorname{Var}(Mf)=2h-Mf(0)-Mf(n-1).
\]
The endpoint differences \(Mf(0)-f(0)\) and \(Mf(n-1)-f(n-1)\) therefore sum to \(\operatorname{Var}(f)-\operatorname{Var}(Mf)\).

**3. Endpoint uplift.** The ball centered at \(0\) with radius \(p\) is the prefix \(\{0,\ldots,p\}\). Since every entry in this prefix is at least \(f(0)\), and its last entry is \(h\),
\[
Mf(0)\ge f(0)+\frac{h-f(0)}{p+1}=f(0)+\frac{A}{p+1}.
\]
The symmetric suffix ball centered at \(n-1\), of radius \(n-1-p\), gives
\[
Mf(n-1)\ge f(n-1)+\frac{B}{n-p}.
\]
Subtract \((A+B)/n\) from the sum of these endpoint uplifts to obtain exactly the displayed deficit bound. Its right side is nonnegative because \(p+1\le n\) and \(n-p\le n\).

**4. Sharpness and equality.** If \(0<p<n-1\), both reciprocal differences in the deficit bound are strictly positive; since \(A+B>0\) for nonconstant data, sharp equality is impossible. If \(p=0\) (the opposite endpoint follows by reflection), then \(A=0\) and \(Mf(n-1)\) is at least the global mean. Equality requires
\[
\frac1n\sum_{j=0}^{n-1}f(j)=f(n-1)+\frac{h-f(n-1)}n.
\]
Because \(f(0)=h\) and every intermediate term is at least \(f(n-1)\), this forces \(f(1)=\cdots=f(n-1)\). Conversely, if \(f(0)=a>b=f(1)=\cdots=f(n-1)\), then \(Mf(0)=a\), \(Mf(n-1)=b+(a-b)/n\), and \(Mf\) is decreasing. Therefore
\[
\operatorname{Var}(Mf)=a-b-\frac{a-b}{n}=\left(1-\frac1n\right)\operatorname{Var}(f),
\]
proving sharpness and classifying nontrivial equality.

## Verification
The accompanying standalone program `verify.py` uses only Python's standard library and exact rational arithmetic. It enumerates every unimodal sequence with entries in \(\{0,1,2,3\}\) of length \(3\) through \(10\) (13,652 profiles), verifies the pointwise unimodality of the maximal output, the sharp coefficient, the peak-location deficit, and equality classification, and checks four further rational profiles. Run with `python verify.py` from the extracted artifact directory. The checker is a finite consistency test, not a proof for all \(n\) or all real data; that proof is the preceding analytic argument.

## Relationship to prior work
González-Riquelme, Kovač and Madrid (arXiv:2603.12462v1; first public 12 March 2026) conjecture the same sharp constant for **every** finite-path input, prove other finite-graph results, and give path evidence through ten vertices. Their Conjecture 5, graph definitions and path-section formulas do not provide this all-orders unimodal case. The full conjecture is not resolved here.

A separately published result, *Monotone data attain the conjectured path-graph variational constant* (public identifier `2ae83e2401fb`), already proves the constant and equality cases for purely nonincreasing or nondecreasing input; these **monotone cases are prior work, not an originality claim here**. The present statement genuinely includes arbitrarily shaped **nonmonotone** single-hump data, establishes preservation of a single peak under *centered* finite-path averaging, and supplies a peak-location quantitative deficit and exact equality rigidity on the enlarged class. Neither theorem implies the other by merely reversing a monotone profile, because unimodal data can rise and then fall.

Bilz and Weigt (arXiv:2107.12404, first public 2021; journal 2025) show sharp constant \(1\) for certain one-dimensional centered maximal variation inequalities, including indicator functions and data satisfying a pointwise attachment condition. Their setting and assumptions do not give the finite-\(n\) factor \(1-1/n\) for arbitrary strictly positive, nonconstant unimodal graph data.

## Limitations
The input class requires at most one direction change in \(|f|\), and the result is for edge \(1\)-variation and counting-measure paths. It neither establishes the full path conjecture nor determines sharp \(p\)-variation constants for other exponents or irregularly weighted paths. The quantitative deficit displayed above is guaranteed, but its two peak-location coefficients are not claimed individually optimal. Extensive but bounded literature and index searches cannot rule out equivalent older results under other terminology; no independent scientific audit has been performed.

## References
1. C. González-Riquelme, V. Kovač, J. Madrid, *Sharp variational inequalities for the Hardy--Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462v1, 12 March 2026, https://arxiv.org/abs/2603.12462.
2. *Monotone data attain the conjectured path-graph variational constant*, published mathematical finding with opaque identifier `2ae83e2401fb` (2026).
3. C. Bilz, J. Weigt, *The one-dimensional centred maximal function diminishes the variation of indicator functions*, arXiv:2107.12404 (2021), J. Geom. Anal. 35 (2025), 256, https://doi.org/10.1007/s12220-025-01965-x.
