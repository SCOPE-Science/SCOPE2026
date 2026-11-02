# A Pareto least-prime-factor law for nice integers

## Finding

Call an integer \(n>1\) *nice* if one can choose one residue class \(a_d\pmod d\) for every divisor \(d>1\) of \(n\), in such a way that two chosen classes can intersect only when their moduli are coprime. Let \(\mathcal N\) be the set of nice integers, and let \(P^-(n)\) be the least prime divisor of \(n\). Write \(\gamma\) for Euler's constant.

For real \(X\) tending to infinity, put \(L=\log\log X\) and \(H=\log L=\log\log\log X\). Then

\[
N(X):=\#\{2\le n\le X:n\in\mathcal N\}
\sim \frac{e^{-\gamma}X}{H}.
\]

More precisely, for **every fixed real \(t>0\)**,

\[
\#\{2\le n\le X:n\in\mathcal N,\ P^-(n)>L^t\}
\sim\frac{e^{-\gamma}X}{H\max\{1,t\}}.
\]

Consequently, if \(n\) is uniformly sampled from \(\mathcal N\cap[2,X]\), then \(Y_X=\log P^-(n)/H\) converges weakly to the probability distribution with cumulative distribution function

\[
F(t)=\begin{cases}
0,&t\le1,\\
1-1/t,&t>1.
\end{cases}
\]

In particular the limiting law is continuous, has density \(t^{-2}\) on \((1,\infty)\), and has no atom at the boundary \(1\).

## Assumptions and scope

All logarithms are natural. The parameter \(t>0\) is fixed before \(X\to\infty\); no uniformity when \(t\) grows with \(X\) is asserted. All counts are of positive integers, and the unit \(1\) is excluded. The statement relies on the established characterization of nice integers: for every integer \(n>1\) with least prime divisor \(p\), niceness is equivalent to \(\omega(n/p)<p\), where \(\omega\) counts **distinct**, not repeated, prime factors (Adenwalla's necessity lemma and Jia–Li's sufficiency theorem).

## Proof

**1. Uniform normal-order error bound.** For \(X\ge 3\) put \(z=\lfloor X^{1/3}\rfloor\), and for \(1\le n\le X\) define \(S(n)=\sum_{p\le z}\mathbf 1_{p\mid n}\) and \(A=\sum_{p\le z}1/p\). A positive integer \(n\le X\) has at most two *distinct* prime factors greater than \(z\); hence \(|\omega(n)-S(n)|\le2\). Counting multiples of primes and of pairs of distinct primes, **including the floor errors**, gives

\[
\sum_{n\le X}S(n)=XA+O(\pi(z)),
\qquad
\sum_{n\le X}S(n)^2=
X\left(A^2+A-\sum_{p\le z}p^{-2}\right)+O(\pi(z)^2).
\]

The classical prime reciprocal estimate gives \(A=\log\log z+O(1)=L+O(1)\). Since \(\pi(z)\le z\), the displayed identities yield

\[
\sum_{n\le X}(\omega(n)-L)^2=O(XL).
\]

Take \(\Delta=L^{3/4}\) and let \(\mathcal E_X\) consist of \(2\le n\le X\) with \(|\omega(n)-L|>\Delta/4\). Chebyshev's inequality therefore gives

\[
\#\mathcal E_X=O(XL/\Delta^2)=O(XL^{-1/2})=o(X/H).
\]

The last relation holds because \(H=\log L=o(L^{1/2})\).

**2. A sharp threshold for niceness outside the exceptional set.** Suppose \(n\notin\mathcal E_X\) and \(p=P^-(n)\). If \(p>L+\Delta\), then

\[
\omega(n/p)\le\omega(n)\le L+\Delta/4<p,
\]

so \(n\) is nice. Conversely, if \(p\le L-\Delta\), then

\[
\omega(n/p)\ge\omega(n)-1\ge L-\Delta/4-1> L-\Delta\ge p,
\]

for sufficiently large \(X\), so \(n\) is not nice. This argument treats both \(p\mid n/p\) and \(p\nmid n/p\); it never assumes \(n\) is squarefree.

**3. Exact rough-number sieve in the relevant scale.** Let \(R(X,y)=\#\{2\le n\le X:P^-(n)>y\}\). Inclusion–exclusion over primes at most \(y\) gives the exact approximation

\[
R(X,y)=X\prod_{p\le y}\left(1-\frac1p\right)
+O\!\left(2^{\pi(y)}+1\right).
\]

If \(y\to\infty\) and \(y\le L^C\) for some fixed \(C>0\), then \(2^{\pi(y)}\le 2^y=o(X/H)\), since \(\log X=e^L\) exceeds every fixed power of \(L\). Mertens' product theorem implies, throughout this scale,

\[
R(X,y)=\frac{e^{-\gamma}X}{\log y}(1+o(1))
\quad\text{whenever }\log y\asymp H.
\]

**4. Global count.** The threshold in Step 2 gives the two-sided bound

\[
R(X,L+\Delta)-\#\mathcal E_X
\le N(X)
\le R(X,L-\Delta)+\#\mathcal E_X.
\]

Because \(\Delta/L\to0\), both logarithms \(\log(L\pm\Delta)\) are \(H+o(1)\). Steps 1 and 3 therefore prove \(N(X)\sim e^{-\gamma}X/H\).

**5. Least-prime-factor tails.** Fix \(t>1\). Eventually \(L^t>L+\Delta\); by Step 2, every integer with \(P^-(n)>L^t\) outside \(\mathcal E_X\) is nice. Hence

\[
\#\{n\le X:n\in\mathcal N,\ P^-(n)>L^t\}
=R(X,L^t)+O(\#\mathcal E_X)
\sim e^{-\gamma}X/(tH).
\]

For fixed \(0<t<1\), eventually \(L^t<L-\Delta\); all nice integers outside \(\mathcal E_X\) have \(P^-(n)>L^t\). The left-hand count is therefore \(N(X)+O(\#\mathcal E_X)\), giving the factor \(1\). At \(t=1\), any nice integer outside \(\mathcal E_X\) with \(P^-(n)\le L\) lies in the thin rough-number slice \(L-\Delta<P^-(n)\le L\), whose size is

\[
R(X,L-\Delta)-R(X,L)=o(X/H)
\]

by Step 3. Thus the factor \(1\) also holds for \(t=1\). Dividing the tail asymptotics by \(N(X)\) gives convergence of tail probabilities to \(1/\max\{1,t\}\) for every \(t>0\). This identifies the continuous cumulative distribution function stated above and proves weak convergence.

## Verification

The accompanying `verify.py` uses exact integer arithmetic to check the divisibility-based first/second-moment identities, inclusion–exclusion for nine prime thresholds, and least-prime-factor membership predicates for all \(2\le n\le30000\). It checks the inequality \(|\omega(n)-S(n)|\le2\) when \(z=32\) and \(z^3>X\). A successful finite run prints `VERIFY_OK`; such finite checks support the algebra but do not prove the infinite estimates. The proof uses classical Mertens results and the previously established niceness characterization as external theorems.

## Relationship to prior work

Adenwalla proved the necessary prime-factor bound and formulated its sufficiency as a conjecture. Jia and Li proved sufficiency and gave explicit residue assignments for the divisor-moduli problem. Those papers concern existence and congruence constructions; the present statement counts all qualifying integers and determines a conditional least-prime-factor limit law. The remaining analytic inputs—Mertens' product theorem, elementary prime-divisibility moments, and inclusion–exclusion—are classical. In particular, the current counting and distributional statements are *deduced from* rather than substituted for the existing structural classification. De la Bretèche, Ford, and Vandehey study the maximal number of pairwise disjoint arithmetic progressions with arbitrary distinct moduli, not the integers whose **entire divisor families** support the present weaker overlap condition.

## Limitations

No uniformity in growing \(t\), effective finite-\(X\) error constant, or asymptotic distribution for the number of different valid residue assignments is asserted. No new proof of the Jia–Li classification or of the classical Mertens theorem is claimed. The very slow triple-logarithmic scale means finite numerical proportions need not approximate the asymptotic value closely. The originality conclusion is limited by available literature indexing and by the possibility that the counting law is an unindexed consequence of known results; external priority and independent proof audits have not been performed.

## References

1. Sarosh Adenwalla, *A Question of Erdős and Graham on Covering Systems*, arXiv:2501.15170 (2025), especially Lemma 3.1, Section 4 and Conjecture 5.1, https://arxiv.org/abs/2501.15170.
2. Zhengkun Jia and Huixi Li, *Resolving Adenwalla's conjecture related to a question of Erdős and Graham about covering systems*, arXiv:2504.09579, first posted 2025-04-13, Theorem 2 and Sections 3–4, https://arxiv.org/abs/2504.09579.
3. Régis de la Bretèche, Kevin Ford, and Joseph Vandehey, *On non-intersecting arithmetic progressions*, Acta Arithmetica 157 (2013), 381–392, https://doi.org/10.4064/aa157-4-5 (comparison of a distinct problem).
4. Classical Mertens prime-reciprocal estimate and Mertens prime-product theorem, as used explicitly in Step 3.
