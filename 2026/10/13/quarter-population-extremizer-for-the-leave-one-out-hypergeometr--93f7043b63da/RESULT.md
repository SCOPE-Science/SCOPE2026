# Quarter-population extremizer for the leave-one-out hypergeometric/binomial density ratio
## Finding
For every integer \(N\ge 3\), set
\[
K_N=\left\lfloor\frac{N+1}{4}\right\rfloor.
\]
For each nondegenerate population composition \(1\le L\le N-1\), let
\[
Q_{N,L}=\operatorname{Hyp}(N,L,N-1),\qquad
P_{N,L}=\operatorname{Bin}(N-1,L/N),
\]
and write \(\rho(Q,P)\) for the maximal point-mass ratio of \(Q\) to \(P\). Then
\[
\max_{1\le L\le N-1}\rho(Q_{N,L},P_{N,L})
=
\frac{N^{N-1}}{
\binom{N}{K_N}K_N^{K_N}(N-K_N)^{N-K_N-1}},
\]
and the only maximizing compositions are \(L=K_N\) and \(L=N-K_N\).

Thus, when sampling without replacement omits exactly one member of the population, the worst binomial approximation in maximal density ratio is not an edge composition: the maximizing success fraction tends to \(1/4\) or \(3/4\).

## Assumptions and scope
The population size is an integer \(N\ge3\), the number of successes is an integer \(L\in\{1,\ldots,N-1\}\), and the sample size is exactly \(N-1\). The hypergeometric and binomial laws use the same success fraction \(p=L/N\). The discrepancy is the non-symmetric maximal density ratio
\[
\rho(Q,P)=\max_k\frac{Q\{k\}}{P\{k\}},
\]
with the usual convention that only points with positive \(Q\)-mass matter here. The statement does not claim the optimizer for other sample sizes.

## Proof
Put \(p=L/N\) and \(q=1-p\). Sampling \(N-1\) objects without replacement is equivalent to omitting one uniformly chosen population member. Hence a hypergeometric variable \(X\sim Q_{N,L}\) has only two possible values:
\[
\Pr\{X=L-1\}=p,\qquad \Pr\{X=L\}=q.
\]
Let \(Y\sim P_{N,L}\). Define the binomial mass at the integer mean of a \(\operatorname{Bin}(N,p)\) law by
\[
M_N(L)=\binom NL p^Lq^{N-L}.
\]
The identities
\[
\binom{N-1}{L-1}=p\binom NL,
\qquad
\binom{N-1}{L}=q\binom NL
\]
give
\[
\Pr\{Y=L-1\}=M_N(L),\qquad
\Pr\{Y=L\}=M_N(L).
\]
Therefore
\[
\rho(Q_{N,L},P_{N,L})=
\frac{\max\{p,q\}}{M_N(L)}.
\]
The expression is invariant under \(L\mapsto N-L\), so it suffices to take \(1\le L\le\lfloor N/2\rfloor\), where \(q\ge p\). Write
\[
H_N(L)=\rho(Q_{N,L},P_{N,L})
=
\frac{N^{N-1}}{\binom NL L^L(N-L)^{N-L-1}}.
\]
For \(1\le k<\lfloor N/2\rfloor\), direct cancellation yields
\[
\frac{H_N(k+1)}{H_N(k)}
=
\left(\frac{k}{k+1}\right)^k
\left(\frac{N-k}{N-k-1}\right)^{N-k-2}.
\]
Set
\[
A_k=\left(1+\frac1k\right)^k,
\qquad
C_m=\left(1+\frac1m\right)^{m-1}.
\]
With \(m=N-k-1\), the last ratio is \(C_m/A_k\).

We now locate its sign exactly. First, \(C_m\) is strictly increasing in \(m\ge1\). Indeed, for real \(x\ge1\),
\[
g(x)=(x-1)\log\left(1+\frac1x\right)
\]
has derivative
\[
g'(x)=\log\left(1+\frac1x\right)-\frac{x-1}{x(x+1)}>\frac1{x+1}-\frac{x-1}{x(x+1)}>0.
\]
Second,
\[
C_{3k+1}<A_k.
\]
After taking \(k\)-th roots this is equivalent to
\[
\left(\frac{3k+2}{3k+1}\right)^3<\frac{k+1}{k},
\]
and cross multiplication leaves the positive difference \(2k+1\).

Third,
\[
C_{3k+2}>A_k.
\]
Put \(z=1/(3k+2)\) and \(r=3+1/k\). Since \(r>3\) and \(z>0\), Taylor's formula with positive third derivative gives
\[
(1+z)^r>1+rz+\frac{r(r-1)}2z^2.
\]
Moreover,
\[
rz+\frac{r(r-1)}2z^2-\frac1k
=
\frac{k+1}{2k^2(3k+2)^2}>0.
\]
Thus \(C_{3k+2}^{1/k}>1+1/k=A_k^{1/k}\).

Monotonicity of \(C_m\) now gives the exact adjacent comparison
\[
H_N(k+1)>H_N(k)
\quad\Longleftrightarrow\quad
N\ge4k+3,
\]
and
\[
H_N(k+1)<H_N(k)
\quad\Longleftrightarrow\quad
N\le4k+2.
\]
There are no ties. Consequently \(H_N\) increases up to
\[
K_N=\left\lfloor\frac{N+1}{4}\right\rfloor
\]
and decreases afterwards on \(1\le L\le\lfloor N/2\rfloor\). This proves uniqueness there. Reflection \(L\mapsto N-L\) gives exactly the two global maximizers \(K_N\) and \(N-K_N\), and substituting \(K_N\) into \(H_N\) gives the displayed sharp value.

## Verification
The proof is analytic and covers every integer \(N\ge3\). The accompanying `verify.py` is only a finite regression check: it evaluates the density-ratio formula exactly with rational arithmetic for \(3\le N\le300\), checks the adjacent-sign criterion, and confirms the predicted maximizers. It is not used to infer the infinite statement.

A direct replay of the packaged checker returns `VERIFY_OK N=3..300`.

## Relationship to prior work
Dümbgen, Samworth, and Wellner introduced and developed maximal density-ratio bounds for this exact hypergeometric-to-binomial approximation problem. Their Theorem 2 proves that, when the sample size satisfies \(n-1\le N/2\), the outer maximization over population composition is attained at \(L=1\) or \(L=N-1\). Their proof also derives the exact pointwise density-ratio expression and locates its maximizing count for fixed \((N,L,n)\).

The present result treats the opposite canonical endpoint \(n=N-1\), which lies outside that theorem's half-sample hypothesis for every \(N\ge4\). In this leave-one-out regime, the composition optimizer moves from the population edge to \(L\sim N/4\). The earlier total-variation comparisons cited by Dümbgen, Samworth, and Wellner concern a different discrepancy and do not imply this exact maximal-ratio composition law.

## Limitations
Only the leave-one-out sample size \(n=N-1\) is classified. No claim is made about the complete optimizer as a function of intermediate sample size \(n\), so a possible transition from the edge regime of the published theorem to the quarter-population endpoint remains open here. The originality search did not find a published equivalent, but an equivalent elementary calculation could exist under older relative-error, likelihood-ratio, or finite-population sampling terminology.

## References
1. L. Dümbgen, R. J. Samworth, and J. A. Wellner, *Bounding distributional errors via density ratios*, arXiv:1905.03009, first public version 2019-05-08; Bernoulli 27(2), 2021, 818–852, doi:10.3150/20-BEJ1256.
2. W. Ehm, *Binomial approximation to the Poisson binomial distribution*, Statistics & Probability Letters 11 (1991), 7–16. Cited in the primary source for total-variation comparison.
3. S. Holmes, *Stein's method for birth and death chains*, in *Stein's Method: Expository Lectures and Applications*, IMS Lecture Notes–Monograph Series 46 (2004), 45–67. Cited in the primary source for total-variation comparison.
