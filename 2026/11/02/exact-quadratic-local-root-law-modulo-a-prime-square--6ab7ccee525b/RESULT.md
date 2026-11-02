# Exact quadratic local root law modulo a prime square

## Finding

Let \(p\) be **any prime**, including \(p=2\). Choose uniformly a nonzero coefficient vector \((a,b,c)\in(\mathbb Z/p^2\mathbb Z)^3\setminus\{(0,0,0)\}\), put \(g(t)=at^2+bt+c\), and let
\[
R_p(g)=\#\{t\bmod p^2:g(t)\equiv0\pmod{p^2}\}.
\]
Set
\[
S_0=\frac{p(p-1)^2}{2}+p-1,\quad
S_1=2p(p-1),\quad S_2=\frac{p(p-1)^2}{2},
\]
and define
\[
\begin{aligned}
A_0&=(p^3+1)S_0+p^3(p-1)^2,\\
A_1&=p^4(p-1),\\
A_2&=p^3S_2,\\
A_p&=p^3(p-1)+S_1,\\
A_{2p}&=S_2.
\end{aligned}
\]
Then the **entire probability generating function**, with coincident exponents combined, is
\[
\boxed{\mathbb E\,z^{R_p}=\frac{A_0+A_1z+A_2z^2+A_pz^p+A_{2p}z^{2p}}{p^6-1}.}
\]
In particular, \(R_p\in\{0,1,2,p,2p\}\). For \(p=2\), exponents \(2\) and \(p\) coincide, as expected; the formula remains valid without adjustment.

For every integer \(k\ge1\),
\[
\boxed{\mathbb E\,R_p^k=\frac{A_1+2^kA_2+p^kA_p+(2p)^kA_{2p}}{p^6-1}.}
\]
The first two moments simplify to
\[
\mathbb E\,R_p=\frac{p^6-p^2}{p^6-1},\qquad
\mathbb E\,R_p^2=\frac{3p^6-2p^5-p^4}{p^6-1}.
\]
As primes \(p\to\infty\), the law of \(R_p\) converges to equal point masses at \(0\) and \(2\), but its second moment tends to \(3\), not the second moment \(2\) of that weak limit. For every **fixed integer** \(k\ge3\),
\[
\boxed{\mathbb E\,R_p^k\sim p^{k-2}.}
\]
Thus the general local estimate \(O_k(1+p^{k-2})\) is attained to leading constant \(1\) in quadratic degree, and the failure of second-moment convergence is caused by rare singular Hensel lifts.

## Assumptions and scope

All assertions are exact for every prime \(p\). Polynomials are **coefficient vectors** of degree at most two over \(\mathbb Z/p^2\mathbb Z\), not polynomial functions counted up to equality as functions. The zero coefficient vector is excluded, matching the squarefree-content local coefficient space in Simhi's paper. There is no separability, monicity or nonzero-leading-coefficient assumption. The convergence statements run through primes tending to infinity, with \(k\) held fixed. No uniformity in growing \(k\) is asserted.

## Proof

**1. Classification modulo the prime.** Write \(S_0\) for the number of reductions with no roots, \(S_1\) for the number of reductions with one root (simple linear or singular quadratic), and \(S_2\) for the number of quadratics with two distinct simple roots. The all-zero polynomial is a separate class of size one. For \(p=2\), the last two classes both have two roots, so their counts must eventually be combined; the class labels are not disjoint root-count values in that characteristic. Nonzero linear polynomials contribute \(p(p-1)\) triples having one simple root, and the \(p-1\) nonzero constant polynomials have no roots. The zero polynomial has \(p\) roots.

Among quadratics with nonzero leading coefficient, those having two distinct roots have the form \(a(t-r)(t-s)\), with \(a\ne0\) and \(r\ne s\), and number \(p(p-1)^2/2\). Those having one singular root number \(p(p-1)\). For odd \(p\) they are exactly \(a(t-r)^2\). In characteristic two, they are precisely \(t^2+c\), for both \(c\in\mathbb F_2\): each has one root with vanishing derivative. Subtracting these two classes from all \(p^2(p-1)\) quadratics leaves \(p(p-1)^2/2\) quadratics with no roots. Hence
\[
S_0=\frac{p(p-1)^2}{2}+p-1,\quad
S_1=2p(p-1),\quad
S_2=\frac{p(p-1)^2}{2},\quad S_p=1.
\]
Here \(S_1\) incorporates both linear simple-root and quadratic singular-root cases. For \(p=2\), \(S_2\) counts the unique quadratic with two simple roots, separately from the zero polynomial, whose root count is also \(2\).

**2. Lifts of each nonzero reduction.** Every coefficient triple modulo \(p\) has exactly \(p^3\) lifts modulo \(p^2\). A polynomial with no roots modulo \(p\) has no roots modulo \(p^2\). A polynomial with exactly one simple root has exactly one lifted root modulo \(p^2\), by the linear Hensel step. A polynomial with two distinct simple roots has exactly two lifted roots. These classes therefore contribute, respectively, \(p^3S_0\) to \(R_p=0\), \(p^4(p-1)\) to \(R_p=1\), and \(p^3S_2\) to \(R_p=2\).

For a quadratic reduction with one singular root \(r\bmod p\), the derivative vanishes at \(r\). For any lifted polynomial \(g\) and any \(u\bmod p\), Taylor expansion gives
\[
g(r+pu)\equiv g(r)\pmod{p^2}.
\]
The condition \(g(r)\equiv0\pmod{p^2}\) imposes one nontrivial linear equation on the three second-digit coefficient choices (varying the constant digit already varies the value), so exactly \(p^2\) of the \(p^3\) lifts satisfy it. Each successful lift has precisely \(p\) roots modulo \(p^2\); every unsuccessful lift has none. Since there are \(p(p-1)\) singular quadratic reductions, they contribute \(p^3(p-1)\) lifts with \(R_p=p\), and \(p(p-1)(p^3-p^2)=p^3(p-1)^2\) lifts with \(R_p=0\).

**3. Lifts of the zero reduction.** The \(p^3\) triples with all coefficients divisible by \(p\) are uniquely \(g=ph\pmod{p^2}\) for coefficient triples \(h\bmod p\). Every root of \(h\bmod p\) lifts to \(p\) roots of \(g\bmod p^2\). Their contributions to \(R_p=0,p,2p,p^2\) are therefore \(S_0,S_1,S_2,1\), respectively.

**4. The exclusion and exact generating function.** Add the counts from Steps 2 and 3. Over all \(p^6\) coefficient triples, the respective contributions are \(A_0,A_1,A_2,A_p,A_{2p}\), plus the one zero coefficient triple giving \(R_p=p^2\). Removing this **one coefficient triple**, without erroneously removing other polynomials with the same root count when \(p=2\), gives exactly the asserted probability generating function on \(p^6-1\) vectors. The sum of its five numerator coefficients is \(p^6-1\). Collisions between exponents are automatically combined in characteristic two.

**5. Moments and limiting behavior.** Differentiating the generating function (or directly summing its five masses) yields the all-order moment formula. Alternatively, for the uniform law on **all** \(p^6\) triples, linearity gives \(\mathbb E R_p=1\): each evaluation is uniform modulo \(p^2\). For the second moment, count ordered pairs of evaluation points: equal pairs contribute \(1\); distinct pairs incongruent modulo \(p\) contribute \(1-1/p\); pairs distinct modulo \(p^2\) but congruent modulo \(p\) contribute another \(1-1/p\). The respective joint zero-event probabilities are \(p^{-2},p^{-4},p^{-3}\). Thus \(\mathbb E R_p^2=3-2/p\) before excluding the zero triple. Subtraction of its contributions \(p^2\) and \(p^4\), followed by division by \(p^6-1\), proves the displayed exact means and second moments.

Finally, \(A_0/(p^6-1)\to1/2\), \(A_2/(p^6-1)\to1/2\), while all other masses vanish. This proves weak convergence to the equally weighted \(\{0,2\}\) distribution. Yet the second moment tends to \(3\). For fixed \(k\ge3\), the contribution of the singular-lift mass \(A_pp^k/(p^6-1)\sim p^{k-2}\) dominates the other three nonzero masses, which are \(O_k(1+p^{k-3})\). This completes the proof.

## Verification

The standalone program `verify.py`, using only Python's standard library, exhaustively enumerates **all coefficient triples**, evaluates every residue modulo \(p^2\), and checks the distribution and first two moments for \(p=2,3,5,7\). It then removes exactly the zero coefficient triple and checks the conditional totals and moments. Run `python3 verify.py`; the expected output is `VERIFY_OK primes=4 coefficient_vectors=134067 full_root_enumeration=yes`. This enumeration confirms these four cases but is not used as a substitute for the uniform proof above.

## Relationship to prior work

Simhi, *Squarefree values of random polynomials are Gaussian mixtures* (2026), defines the local space of nonzero coefficient vectors modulo \(p^2\) and obtains the general upper bound \(\mathbb E\rho_g(p^2)^k\ll_{d,k}1+p^{k-2}\) in Lemma 3.4. Appendix Lemma A.2 also isolates the rare singular-root event with probability of order \(p^{-2}\). The proof and bound are prior results. The present quadratic-degree theorem gives instead the **complete exact local distribution at every prime**, sharp leading constants for high moments, and the quantified failure of second-moment convergence. No new global Gaussian-mixture theorem is claimed.

Sofos's 2026 work on counting squarefree values of random polynomials treats mean and variance in the global arithmetic problem, not this exact conditional local law. Bhargava, Cremona, Fisher and Gajović (2022), and Caruso (2022), investigate random \(p\)-adic **field roots** and their locations; the number of residue roots modulo \(p^2\), including singular roots that need not lift indefinitely, is a different invariant. Hakami's studies of solutions of quadratic forms over finite rings concern multivariable forms, boxes and lower bounds, rather than this distribution across all univariate coefficient triples.

## Limitations

This theorem concerns degree at most two and modulus exactly \(p^2\); it does not describe higher degrees, higher prime powers, or a global density of squarefree values. The coefficient model is not monic and is conditioned only on the nonzero coefficient vector modulo \(p^2\). The high-moment asymptotic holds separately for each fixed \(k\). A general exact finite-ring root-count distribution theorem not located in the checked literature could imply the special case, so historical priority remains a genuine residual risk.

## References

1. O. Simhi, *Squarefree values of random polynomials are Gaussian mixtures*, arXiv:2610.29911v1 (first public 21 October 2026), Lemmas 3.3–3.4 and Appendix Lemma A.2. https://arxiv.org/html/2610.29911v1
2. E. Sofos, *Counting square-free values of random polynomials*, arXiv:2601.19319v1 (27 January 2026). https://arxiv.org/html/2601.19319v1
3. M. Bhargava, J. Cremona, T. Fisher and S. Gajović, *The density of polynomials of degree n over the p-adic integers having exactly r roots in the p-adic numbers*, Proceedings of the London Mathematical Society (2022), DOI:10.1112/plms.12438. https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/plms.12438
4. X. Caruso, *Where are the zeroes of a random p-adic polynomial?*, Forum of Mathematics, Sigma (2022). https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/where-are-the-zeroes-of-a-random-padic-polynomial/0244BCEFD452D02D70D4ED4CE66B46FB
5. A. H. Hakami, *Lower Bounds on Solutions of Quadratic Polynomials Defined over Finite Rings* (2015), DOI:10.1155/2015/305730. https://onlinelibrary.wiley.com/doi/10.1155/2015/305730
