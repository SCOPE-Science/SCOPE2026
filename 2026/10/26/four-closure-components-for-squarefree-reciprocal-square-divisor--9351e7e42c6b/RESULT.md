# Four closure components for squarefree reciprocal-square divisor sums

## Finding

Let \(\mathcal Q\) be the set of squarefree positive integers, and define
\[
 f(n)=\sigma_{-2}(n)=\sum_{d\mid n}d^{-2}.
\]
The closure of \(f(\mathcal Q)\) in \(\mathbb R\) is exactly
\[
\boxed{\begin{aligned}
 &[1,\tfrac{54}{5\pi^2}]\;\cup\;[\tfrac{10}{9},\tfrac{12}{\pi^2}]\\
 &\quad\cup\;[\tfrac54,\tfrac{27}{2\pi^2}]\;\cup\;[\tfrac{25}{18},\tfrac{15}{\pi^2}].
\end{aligned}}
\]
The four intervals are pairwise disjoint, so the closure has exactly four connected components.

## Assumptions and scope

The domain is \(\mathcal Q=\{n\in\mathbb N: n\text{ is squarefree}\}\). The closure is taken in the usual topology of \(\mathbb R\). For squarefree \(n\), multiplicativity gives
\[
 f(n)=\prod_{p\mid n}(1+p^{-2}),
\]
where the product is over prime divisors of \(n\). The claim is only about this squarefree restriction at exponent parameter \(2\); it does not classify the closure of the unrestricted divisor-function range or other parameters.

## Proof

Write \(p\) and \(q\) for primes, and for every prime \(p\ge5\) put
\[
 a_p=\log(1+p^{-2}),\qquad T=\sum_{p\ge5}a_p.
\]
The sum converges because \(0<a_p\le p^{-2}\) and \(\sum_{m\ge2}m^{-2}<\infty\).

We first prove that
\[
 a_p\le\sum_{q>p}a_q\qquad\text{for every prime }p\ge5. \tag{1}
\]
For the eight primes \(p\in\{5,7,11,13,17,19,23,29\}\), it suffices to exhibit a finite set \(Q_p\) of primes larger than \(p\) for which
\(\prod_{q\in Q_p}(1+q^{-2})>1+p^{-2}\). Exact rational checks give the following certificates:

| \(p\) | \(Q_p\) | \(\prod_{q\in Q_p}(1+q^{-2})\) | \(1+p^{-2}\) |
|---:|:---|---:|---:|
| 5 | \(7,11,13,17,19\) | \(6403780000/6149280137\) | \(26/25\) |
| 7 | \(11,13,17,19\) | \(128075600/125495513\) | \(50/49\) |
| 11 | \(13,17\) | \(2900/2873\) | \(122/121\) |
| 13 | \(17,19\) | \(104980/104329\) | \(170/169\) |
| 17 | \(19,23\) | \(191860/190969\) | \(290/289\) |
| 19 | \(23,29\) | \(446260/444889\) | \(362/361\) |
| 23 | \(29,31\) | \(810004/808201\) | \(530/529\) |
| 29 | \(31,37\) | \(35620/35557\) | \(842/841\) |

Taking logarithms proves (1) for these primes.

For every real \(x\ge20.5\), the Rosser--Schoenfeld prime-counting bound gives
\[
 \pi(2x)-\pi(x)>\frac{3x}{5\log x},
\]
where \(\pi(x)\) counts primes not exceeding \(x\). For a prime \(p\ge31\), the right side is greater than \(5\), so there are at least six primes \(q\) in \((p,2p]\). For such \(q\), the elementary inequality \(\log(1+y)\ge y-y^2/2\), for \(0\le y\le1\), yields
\[
 a_q\ge\frac{1}{4p^2}-\frac{1}{32p^4}.
\]
Consequently
\[
 \sum_{q>p}a_q\ge6\left(\frac{1}{4p^2}-\frac{1}{32p^4}\right)
 =\frac{3}{2p^2}-\frac{3}{16p^4}>\frac1{p^2}>a_p.
\]
This proves (1) for all remaining primes.

We use the following subsum lemma. If \((b_j)_{j\ge1}\) is a positive summable sequence and \(b_j\le\sum_{k>j}b_k\) for every \(j\), then the set of all subsums \(\sum_j\varepsilon_jb_j\), with \(\varepsilon_j\in\{0,1\}\), is the full interval \([0,\sum_jb_j]\). Indeed, at each step the intervals \([0,\sum_{k>j}b_k]\) and \([b_j,b_j+\sum_{k>j}b_k]\) overlap and cover \([0,\sum_{k\ge j}b_k]\); recursively choosing one of the two intervals represents any target in the total interval. The remaining tail tends to zero. Finite subsums are dense in this interval by truncating any infinite subsum.

Apply the lemma to the primes \(p\ge5\), ordered increasingly, using (1). Thus the closure of the finite products \(\prod_{5\le p\mid m}(1+p^{-2})\), with \(m\) squarefree and coprime to \(6\), is \([1,B]\), where
\[
 B=\prod_{p\ge5}(1+p^{-2}).
\]
The Euler product identity \(\prod_p(1+p^{-2})=\zeta(2)/\zeta(4)=15/\pi^2\) gives
\[
 B=\frac{15/\pi^2}{(1+2^{-2})(1+3^{-2})}=\frac{54}{5\pi^2}.
\]
Every squarefree integer has a unique form \(n=2^e3^fm\), where \(e,f\in\{0,1\}\) and \(m\) is squarefree and coprime to \(6\). Therefore the full closure is the union of \([c,cB]\) for
\[
 c\in\left\{1,\frac{10}{9},\frac54,\frac{25}{18}\right\}.
\]
Multiplying out the endpoints gives the four intervals in the finding. They are ordered and disjoint: \(54/(5\pi^2)<10/9\), \(12/\pi^2<5/4\), and \(27/(2\pi^2)<25/18\); each follows from \(\pi>3.14\). This completes the proof.

## Verification

The included exact-rational checker `verify.py` verifies the eight finite product certificates and the rational endpoint-separation inequalities. The infinite tail bound is proved using the stated Rosser--Schoenfeld estimate, not by finite enumeration. The subsum lemma proves the interval-filling step. No numerical range scan is used as evidence for an infinite statement.

## Relationship to prior work

Defant introduced the restricted-domain functions \(\sigma_{-r,k}\), whose domain consists of integers with each prime exponent at most \(k\), and proved a necessary-and-sufficient criterion for density of their ranges. For \(k=1\), this is precisely the squarefree restriction considered here. The paper's final section asks for the parameter values at which the closure has a specified number of disjoint interval components; it does not state the four-interval formula above for \(k=1\), \(r=2\).

Defant also studies an alternating divisor-function variant with local factors \(\sum_{j=0}^{\alpha}(-p^{-2})^j\) over unrestricted prime exponents. That function is not \(f\): here every local factor is positive, and the squarefree restriction permits only exponents zero or one. Neither inspected paper states the interval formula proved here.

## Limitations

The result treats only the squarefree domain and the fixed exponent \(2\). It does not determine component counts for other parameters or for the unrestricted range of \(\sigma_{-2}\). The finite rational table covers only the eight primes below \(31\); all larger primes are handled by the cited explicit prime-counting estimate.

## References

1. Colin Defant, *On the Density of Ranges of Generalized Divisor Functions with Restricted Domains*, arXiv:1507.02663 (first posted 9 July 2015), especially Theorem 2.3 and §3. https://arxiv.org/abs/1507.02663
2. J. Barkley Rosser and Lowell Schoenfeld, “Approximate Formulas for Some Functions of Prime Numbers,” *Illinois Journal of Mathematics* 6 (1962), 64–94, Corollary 3. https://doi.org/10.1215/ijm/1255631807
