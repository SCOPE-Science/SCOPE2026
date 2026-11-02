# The exact one-redundancy threshold for two-error correction of arbitrary binary-valued functions

## Finding

Let \(\kappa_1(2)\) denote the least positive integer \(K\) such that, for every integer \(k\ge K\) and every nonconstant function \(f:\mathbb F_2^k\to\mathbb F_2\), there is an **injective** encoder \(E:\mathbb F_2^k\to\mathbb F_2^{k+1}\) satisfying
\[
f(u)\ne f(v)\implies d_H(E(u),E(v))\ge5.
\]
Then
\[
\boxed{\kappa_1(2)=36.}
\]
In particular, the universal length-one-redundancy guarantee established for \(k\ge66\) by Rajput--Jagatti--Rajan can be sharpened exactly to \(k\ge36\). Sharpness holds: at \(k=35\), any two-valued function whose smaller preimage has exactly \(15{,}771{,}159{,}390\) elements admits no such one-redundancy encoder.

## Assumptions and scope

All vectors are binary. The encoder must be injective, but need not be linear or systematic. Only the function value, not the full message, is required to withstand up to two arbitrary Hamming substitutions. The quantifiers are **every** \(k\ge36\) and **every** nonconstant Boolean function on \(k\) input bits. For the counterexample, any partition into class sizes \(15{,}771{,}159{,}390\) and \(2^{35}-15{,}771{,}159{,}390\) suffices. No assumptions on the internal shape of either class are made.

Write \(I_M\) for the first \(M\) binary words of length \(n\) in simplicial order: increasing Hamming weight, then lexicographic order with \(1\) preceding \(0\) at the first differing position. For \(M=\min(|f^{-1}(0)|,|f^{-1}(1)|)\), necessarily \(1\le M\le2^{k-1}\).

## Proof

**1. Exact feasibility criterion.** Theorem 3 of Rajput--Jagatti--Rajan, based on Harper's vertex-isoperimetry and its higher-radius extension, gives the necessary and sufficient condition for an injective non-systematic code of length \(n=k+1\) correcting two function-value errors:
\[
|N_4(I_M)|\le 2^k+M.\tag{1}
\]
Indeed the smaller class can occupy \(I_M\), while the other class must fit in its radius-four complement. Isoperimetry establishes necessity for arbitrary encoders, not just this construction.

**2. Exact compressed shadow formula.** Let \(V(n,j)=\sum_{i=0}^j\binom ni\) (with \(V(n,j)=0\) for \(j<0\)). Write uniquely \(M=V(n,j-1)+m\), where \(1\le m\le\binom nj\). Then \(I_M\) contains all vectors of weights below \(j\) and the first \(m\) vectors of weight \(j\). Thus \(N_4(I_M)\) consists of every vector of weight at most \(j+3\), together with the weight-\(j+4\) vectors containing one of the selected weight-\(j\) supports.

For any \((j+4)\)-subset \(Y\), the lexicographically first \(j\)-subset of \(Y\) comprises its \(j\) largest coordinates; \(Y\) contains an initially selected \(j\)-subset if and only if this lexicographically first subset is selected. Each chosen \(j\)-subset \(X\) is first for exactly \(\binom{\min X}{4}\) supersets \(Y\), where coordinates are \(0,\dots,n-1\) and \(\min\varnothing=n\). These supersets are disjointly counted. Therefore
\[
|N_4(I_M)|=V(n,j+3)+\sum_{X\text{ among first }m\ j\text{-subsets}}\binom{\min X}{4}.\tag{2}
\]
The case \(j=0\) agrees with the radius-four ball around zero.

**3. Exact finite maximization without enumerating exponentially many sets.** Put \(w(X)=\binom{\min X}{4}-1\) and \(D_n(M)=|N_4(I_M)|-2^{n-1}-M\). By (2),
\[
D_n(M)=V(n,j+3)-2^{n-1}-V(n,j-1)+\sum_{X\text{ among first }m\ j\text{-subsets}}w(X).\tag{3}
\]
For \(j\ge1\), the ordered list of the \(j\)-subsets of \(\{0,\dots,n-1\}\) splits into blocks indexed by their largest element \(h=n-1,n-2,\dots,j-1\). In block \(h\), the remaining \((j-1)\)-subset runs through the corresponding ordered list on \(\{0,\dots,h-1\}\); all its weights are exactly the same as those of that smaller list. For \(j=0\), the singleton list has weight \(\binom n4-1\). This recursion permits exact integer computation of the sum and maximum prefix sum of each full or truncated block, by addition and maxima alone. The accompanying `verify.py` implements this recurrence directly; there is no probabilistic sampling or floating point.

Let
\[
G(k)=\max_{1\le M\le2^{k-1}}D_{k+1}(M).
\]
The exact recurrence yields
\[
\begin{aligned}
G(35)&=329{,}481{,}574 &&\text{at }M=15{,}771{,}159{,}390,\\
G(36)&=-452{,}256{,}184 &&\text{at }M=29{,}687{,}961{,}398.
\end{aligned}
\]
It also verifies \(G(k)<0\) for **each** integer \(36\le k\le65\). The largest gap over the last endpoint is \(G(65)=-9{,}158{,}393{,}403{,}190{,}660{,}545\). These are exhaustive prefix maxima obtained from the proved block recursion, not extrapolations.

For the explicit failure at \(k=35\), \(n=36\), \(j=16\), and \(m=1{,}854{,}357{,}382\). Formula (2) gives
\[
|N_4(I_M)|=47{,}494{,}802{,}618+2{,}965{,}576{,}714=50{,}460{,}379{,}332,
\]
while \(2^{35}+M=50{,}130{,}897{,}758\). Hence (1) fails by \(329{,}481{,}574\), even for unrestricted injective encoders.

**4. The infinite range.** Theorem 4 of Rajput--Jagatti--Rajan proves that every nonconstant two-valued function admits the required one-redundancy encoding for every \(k\ge\lceil\frac83(2t+1)^2\rceil-1\). At \(t=2\) this is \(k\ge66\). Combined with the exact finite verification for \(36\le k\le65\), condition (1) holds for every \(k\ge36\). Its failure at \(k=35\) makes the threshold sharp.

## Verification

Run `python3 verify.py` using the Python standard library. The program checks the full dynamic-programming recurrence, all 30 intermediate dimensions \(36\le k\le65\), and the exact boundary certificate. A separately written brute-force Hamming-ball computation checks the recurrence for every smaller-class size in every dimension \(5\le k\le10\) (ambient dimensions \(6\le n\le11\)). Its final output is `CERTIFICATE_OK`. All asserted quantities use exact integers. Formula (3) and the block decomposition are proved above; the finite checker is used only on the finite dimensions, while the infinite continuation is a cited analytic theorem.

## Relationship to prior work

Rajput, Jagatti and Rajan (2026, Theorem 3) supplied the exact isoperimetric encoding criterion and (Theorem 4) the universal guarantee \(k\ge66\) for two errors. They explicitly noted that exact thresholds for \(t\ge2\) were unknown. Their Table III and Proposition 1 settle **only** the one-error threshold \(\kappa_1(1)=10\), not the value proved here. Harper and Räty established the required vertex-isoperimetric minimizing property; neither calculates this function-code threshold. The contribution here is the new exact value \(\kappa_1(2)=36\), including a sharp obstruction and an exhaustive, polynomial-size integer shadow certificate.

## Limitations

The result is about arbitrary non-systematic, injective binary encodings and two errors in the *function value*. It does not give the exact thresholds for three or more function-value errors, for redundancy two or three, for systematic codes, or for nonbinary alphabets. The finite certificate and mathematical proof have received no independent audit. Publication-priority review remains subject to additional literature coverage beyond the inspected sources.

## References

1. C. Rajput, K. L. Jagatti and B. S. Rajan, *On Optimal Encodings and Systematicity in Function-Correcting Codes*, arXiv:2610.09011v1, first public October 6, 2026; Theorems 3–4, Definition 1, Section III and Appendix B. https://arxiv.org/abs/2610.09011
2. L. H. Harper, *Optimal numberings and isoperimetric problems on graphs*, Journal of Combinatorial Theory **1** (1966), 385–393.
3. E. Räty, *Uniqueness in Harper’s vertex-isoperimetric theorem*, Discrete Mathematics **343** (2020), article 111696.
