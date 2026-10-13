# A three-summand counterexample to Juškevičius's variance-equalization concentration conjecture
## Finding
Let \(\mathcal Q_2(X)=\sup_{x\in\mathbb R}\Pr\{X\in(x,x+2]\}\) be the length-two concentration function, and let \(T(\alpha)\) be the extremal family defined by Juškevičius. Conjecture 6.1 in the cited source predicts that replacing independent \(T(\alpha_i)\) by independent copies of a common \(T(\alpha_*)\) with the same total variance cannot decrease concentration.

The prediction fails for three summands. Take
\[
(\alpha_1,\alpha_2,\alpha_3)=\left(1,\frac12,\frac25\right).
\]
Then \(T(1)\) is degenerate at \(0\), \(T(1/2)\) is uniform on \(\{-1,1\}\), and \(T(2/5)\) is uniform on \(\{-2,-1,0,1,2\}\). Their variances are respectively \(0\), \(1\), and \(2\), so the total variance is \(3\). The unique common parameter with variance \(1\) is \(\alpha_*=1/2\). Nevertheless,
\[
\mathcal Q_2\!\left(T(1)+T(1/2)+T(2/5)\right)=\frac25
>\frac38
=\mathcal Q_2\!\left(T(1/2)+T(1/2)+T(1/2)\right).
\]
Hence Conjecture 6.1 is false, with exact violation gap \(1/40\).

## Assumptions and scope
All displayed summands are independent. For \(k\in\mathbb N\), let \(\nu_k\) denote the uniform law on the \(k\)-term arithmetic progression \(\{-k+1,-k+3,\ldots,k-1\}\). For \(\alpha\in[1/(k+1),1/k]\), the source defines
\[
T(\alpha)\sim(1-\tau)\nu_{k+1}+\tau\nu_k,
\qquad \tau=k(k+1)\alpha-k.
\]
The claim concerns only Conjecture 6.1 for this family and the source's length-two concentration convention. It does not assert an optimal three-summand violation or classify all counterexamples.

## Proof
The variance of \(\nu_k\) is \((k^2-1)/3\). Thus, on \(\alpha\in[1/(k+1),1/k]\),
\[
v(\alpha):=\operatorname{Var}T(\alpha)
=\frac{k(k+2)-(2k+1)\tau}3.
\]
Since \(\tau=k(k+1)\alpha-k\), this is strictly decreasing in \(\alpha\) on each interval, and the formulas agree at the endpoints. Therefore \(v\) is strictly decreasing on \((0,1]\). In particular, \(v(1/2)=1\), so \(1/2\) is the unique common parameter whose three copies have total variance \(3\).

At \(\alpha=1\), one has \(T(1)=\nu_1=0\). At \(\alpha=1/2\), one has \(T(1/2)=\nu_2\), the Rademacher law on \(\{-1,1\}\). At \(\alpha=2/5\), one has \(k=2\) and \(\tau=2/5\), hence
\[
T(2/5)\sim\frac35\nu_3+\frac25\nu_2.
\]
The three atoms of \(\nu_3\) are \(-2,0,2\), each receiving mass \(1/5\), while the two atoms of \(\nu_2\) are \(-1,1\), also each receiving mass \(1/5\). Therefore \(T(2/5)\) is uniform on five consecutive integers and has variance \(2\).

Let \(S=T(1)+T(1/2)+T(2/5)\). Its probability masses at \(-3,-2,-1,0,1,2,3\) are respectively
\[
\frac1{10},\frac1{10},\frac15,\frac15,\frac15,\frac1{10},\frac1{10}.
\]
Any half-open interval of length \(2\) contains at most two adjacent integer atoms, and the largest adjacent mass sum is \(2/5\). Hence \(\mathcal Q_2(S)=2/5\).

For the variance-equalized sum \(S_*=T(1/2)+T(1/2)+T(1/2)\), the support is \(\{-3,-1,1,3\}\) with masses \(1/8,3/8,3/8,1/8\). Distinct support points are separated by \(2\), so a half-open interval of length \(2\) contains at most one support point. Consequently \(\mathcal Q_2(S_*)=3/8\), and
\[
\mathcal Q_2(S)-\mathcal Q_2(S_*)=\frac1{40}>0.
\]
This is the opposite of the conjectured inequality.

## Verification
The accompanying verifier reconstructs the three exact rational probability laws, checks their variances, performs exact convolutions, computes the length-two concentration by enumerating all possible adjacent lattice windows, and asserts the values \(2/5\), \(3/8\), and \(1/40\). The symbolic proof above is complete; the computation is a replay check, not a substitute for an infinite argument.

## Relationship to prior work
Juškevičius formulates Conjecture 6.1 as a variance-matching equalization principle for the full extremal family \(T(\alpha)\). The present tuple uses \(T(2/5)\), which is the first genuinely five-point uniform example below the \(\alpha=1/2\) boundary, so it lies outside the symmetric three-point regime.

Mattner and Roos analyze symmetric three-point convolutions and record failure of a broad Schur-concavity assertion outside its valid parameter cube. That literature does not cover this counterexample: \(T(2/5)\) has five support points and is not a symmetric three-point law. Candidate-specific searches for the exact parameters, variance-matched formulation, and equivalent concentration-language formulations found no statement implying the displayed \(2/5>3/8\) comparison.

## Limitations
This result disproves the stated general conjecture but does not determine the largest possible three-summand violation, classify all violating triples, or address substitute inequalities under additional restrictions. The originality comparison is limited by ordinary indexing and terminology risk; an equivalent elementary counterexample could exist under different notation.

## References
1. T. Juškevičius, “The sharp form of the Kolmogorov--Rogozin inequality and a conjecture of Leader--Radcliffe,” arXiv:2201.09861; *Bulletin of the London Mathematical Society* 56 (2024), 3289--3299, doi:10.1112/blms.13132.
2. L. Mattner and B. Roos, “A shorter proof of Kanter's Bessel function concentration bound,” arXiv:math/0603522; *Probability Theory and Related Fields* 139 (2007), 191--205, doi:10.1007/s00440-006-0043-0.
