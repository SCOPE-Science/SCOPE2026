# Strict prime-exponent majorization for ordered factorizations and sum systems

## Finding

For an integer \(n>1\), let \(c_j(n)\) count its ordered factorizations into exactly \(j\) integer factors greater than one. For \(2\le m\le\Omega(n)\), let \(\mathcal N_m(n)\) be the number of **ordered** \(m\)-part sum systems of \(\{0,1,\ldots,n-1\}\), with all component cardinalities greater than one and unique representations. Write \(n=\prod_{i=1}^r p_i^{a_i}\), where the primes are distinct, each \(a_i\ge1\), \(r=\omega(n)\), and \(k=\Omega(n)=\sum_i a_i\).

**Theorem (strict simultaneous majorization).** Fix \(k\ge2\), \(2\le r\le k\), and any positive integer exponent vector \(\mathbf a=(a_1,\ldots,a_r)\) summing to \(k\). If \(a_u\ge a_v+2\) for distinct indices \(u,v\), and \(\mathbf a'\) is obtained by decreasing \(a_u\) by one and increasing \(a_v\) by one, then **simultaneously**
\[
 c_j(\mathbf a')>c_j(\mathbf a)\quad(2\le j\le k),\qquad
 \mathcal N_m(\mathbf a')>\mathcal N_m(\mathbf a)\quad(2\le m\le k).
\]
Here the counts depend only on the exponent vector and not on which distinct primes realize it. The length-one count is always \(c_1=1\).

**Complete extremizers.** At fixed \((k,r)\), each \(c_j\) with \(2\le j\le k\) and each \(\mathcal N_m\) with \(2\le m\le k\) has its unique minimum exponent multiset at
\[
 (k-r+1,\underbrace{1,\ldots,1}_{r-1}),
\]
and its unique maximum exponent multiset at
\[
 (\underbrace{q+1,\ldots,q+1}_{s},\underbrace{q,\ldots,q}_{r-s}),
 \qquad k=qr+s,\quad0\le s<r.
\]
The uniqueness is modulo permutation of exponent coordinates. For \(r=1\) or \(r=k\), there is only one possible exponent multiset. Allowing the support size to vary between \(1\) and \(k\), the unique minimum exponent multiset is \((k)\), and the unique maximum is \((1,\ldots,1)\).

Thus the whole vector of ordered-factorization counts, and the whole vector of ordered sum-system counts, increase strictly at every nontrivial exponent-balancing step: their extrema agree **in every length and every number of parts**, rather than only after summing over lengths.

## Assumptions and scope

All integer factorizations are counted **with order**; the prime factors \(p_i\) are distinct, but their actual magnitudes are irrelevant. A sum system is an ordered tuple \((A_1,\ldots,A_m)\) of finite subsets of nonnegative integers, all \(|A_i|>1\), such that each integer in \(\{0,\ldots,n-1\}\) occurs **exactly once** as \(a_1+\cdots+a_m\) with \(a_i\in A_i\). If \(m>\Omega(n)\), the number is zero, and strict comparison is not asserted. Permuting the underlying prime bases does not alter any count; uniqueness concerns exponent *multisets*, not actual integers. The theorem has no limiting or probabilistic assumption.

The explicit formulas, useful for computing both extrema without enumerating integers, are
\[
 c_j(\mathbf a)=\sum_{t=0}^{j}(-1)^{j-t}\binom jt
 \prod_{i=1}^{r}\binom{a_i+t-1}{a_i},\qquad
 \mathcal N_m(\mathbf a)=m!\sum_{j=m}^{k}S(j-1,m-1)c_j(\mathbf a),
\]
where \(S(\cdot,\cdot)\) is the Stirling number of the second kind, with the ordinary binomial convention (so the summand at \(t=0\) is zero). The second identity is a **previously published formula**, not a new claim. Substituting either displayed extremal vector yields the corresponding exact minimum and maximum values.

## Proof

**1. Prime-exponent assignments.** An ordered factorization into \(j\) nonunit factors is exactly an \(r\)-by-\(j\) matrix of nonnegative integers whose \(i\)-th row sums to \(a_i\) and with no identically zero column. The number without the nonzero-column condition is \(\prod_i\binom{a_i+j-1}{a_i}\). Inclusion--exclusion on zero columns proves the formula for \(c_j\) above. In particular \(c_1=1\) and \(c_j=0\) for \(j>k\).

**2. Two-variable positivity lemma.** Let \(L\ge2\) and \(h\ge2\). Put
\[
 H(x,y)=\frac1{(1-x)(1-y)}=\sum_{d\ge0}h_d(x,y),\qquad
 h_d(x,y)=\sum_{v=0}^{d}x^{d-v}y^v.
\]
For any subset \(R\subseteq\{1,\ldots,h\}\) with \(|R|\le L\), consider the homogeneous component of degree \(L\) of
\[
 F_R(x,y)=\prod_{i\notin R}H(x,y)\prod_{i\in R}(H(x,y)-1).
\]
Each degree-\(L\) component is a sum of products \(\prod_{i=1}^{h}h_{d_i}(x,y)\), with \(\sum_i d_i=L\) and \(d_i\ge1\) when \(i\in R\). Every such product is Schur-positive, by the Pieri rule for products of complete homogeneous symmetric polynomials. In two variables its degree-\(L\) Schur expansion takes the form
\[
 \sum_{\ell=0}^{\lfloor L/2\rfloor}\beta_\ell
 s_{(L-\ell,\ell)}(x,y),\quad\beta_\ell\ge0,
\]
where
\[
 s_{(L-\ell,\ell)}(x,y)
 =\sum_{v=\ell}^{L-\ell}x^{L-v}y^v.
\]
For integers \(a\ge b+2\) with \(a+b=L\), the coefficient difference between the monomials \(x^{a-1}y^{b+1}\) and \(x^ay^b\) therefore equals \(\beta_{b+1}\ge0\). Strict positivity of \(\beta_{b+1}\) for one product holds whenever its sorted positive degree profile \(\mu\) is dominated by \((L-b-1,b+1)\). By the standard Kostka positivity criterion (Young's rule), this is equivalent, for a two-row shape, to \(\max_i d_i\le L-b-1\). We will now find such a term, which avoids relying only on a non-strict Schur-concavity conclusion.

**3. Strict balancing at each factorization length.** Fix an exponent pair \((a,b)\) with \(a\ge b+2\), write \(L=a+b\), and set \(S\) equal to the sum of the remaining prime exponents. Fix \(h\), \(2\le h\le k=L+S\). Distribute the remaining prime exponents among the \(h\) factor slots in any allowed way, temporarily allowing a slot to have no factor from these other primes. Let \(R\) be exactly the slots receiving no other prime. For that fixed distribution, the two selected primes must fill every slot in \(R\) nontrivially, and their contribution is
\[
 [x^ay^b]F_R(x,y).
\]
Distributing the \(S\) other prime factors so that as many slots as possible are occupied gives a legitimate assignment with
\[
 |R|=q_0=\max(0,h-S)\le L.
\]
Set \(\ell=b+1\), so \(1\le\ell\le\lfloor L/2\rfloor\) and \(L-\ell=a-1\). If \(q_0\le1\), choose two slot degrees \(L-\ell\) and \(\ell\), placing a positive one at the mandatory slot if there is one. If \(q_0\ge2\), put positive degrees in exactly the \(q_0\) mandatory slots, as evenly as possible, totaling \(L\). This is possible because \(q_0\le L\), and their maximum is \(\lceil L/q_0\rceil\le\lceil L/2\rceil\le L-\ell\). In either case, the chosen degree profile satisfies \(\max_i d_i\le L-\ell\); by Young's rule its product contributes a strictly positive \(s_{(L-\ell,\ell)}\) coefficient. Hence the fixed outsider distribution has strictly more configurations of selected-prime exponents \((a-1,b+1)\) than of \((a,b)\). All other distributions have nonnegative differences by Schur positivity. Summing them yields
\[
 c_h(a-1,b+1,\mathbf a_{\mathrm{other}})-c_h(a,b,\mathbf a_{\mathrm{other}})>0.
\]
This holds separately for every \(h\in\{2,\ldots,k\}\), completing the strict factorization part.

**4. Sum systems and extremizers.** The published identity (Huxley--Lettington--Schmidt, Theorem 5.1 and Remark 5.2) is
\[
 \mathcal N_m(n)=m!\sum_{j=m}^{k}S(j-1,m-1)c_j(n).
\]
Every coefficient is nonnegative, and the term with \(j=m\) has coefficient \(m!>0\). By Step 3, every \(\mathcal N_m\) therefore increases strictly under balancing. Repeated exchanges from a larger part to a part at least two smaller terminate exactly at the balanced exponent profile, proving the unique maximum. Conversely, in every non-spike profile having at least two parts exceeding one, moving one unit from a smaller positive part \(\ge2\) to a larger part strictly decreases each count; this process terminates at the spike \((k-r+1,1,\ldots,1)\), proving the unique minimum. The edge cases \(r=1\) and \(r=k\) are immediate.

To compare different support sizes, replace one prime exponent \(u+v\ge2\) by distinct-prime exponents \(u,v\ge1\). Each old ordered factorization of length \(h\) injects into the new set by splitting the old prime exponent across its slots using a deterministic greedy allocation of the first \(u\) exponent units, with the remaining \(v\) units assigned to the other prime. Original slot exponents recover the old factorization, so the map is injective. For \(2\le h\le k\), an old factorization can be chosen with **at least two different slots containing a positive exponent** of the prime being split: put one copy of it in each of two slots, then distribute all remaining \(k-2\) prime-factor copies so that the other \(h-2\) slots are nonempty, which is possible since \(h\le k\). For the resulting positive slot capacities, the number of bounded allocations of the \(u\) new-prime units is at least two whenever \(1\le u\le u+v-1\): one can transfer a unit between two slots with positive capacities, or equivalently view the allocations as coefficients of a product of at least two nonconstant interval polynomials. The greedy injection chooses only one of these allocations for this original factorization. Thus the inequality is strict for each \(h\ge2\). Strictness transfers to the \(\mathcal N_m\) by the positive formula. Iterated splitting shows that the prime-power profile is the unique all-support minimum and the squarefree profile the unique all-support maximum, at fixed \(k\).

## Verification

The standalone program `verify.py` uses only the Python standard library. It computes \(c_j\) by exact integer inclusion--exclusion, computes \(\mathcal N_m\) by the published Stirling transform, and verifies the **strict inequalities individually for all factorization lengths and all part counts** across every positive integer composition of \(k\le12\) and every legal one-unit balancing transfer. Additional independent small-case checks compare inclusion--exclusion with direct exponent-allocation matrices, and test strictness under prime-support splitting. Run `python3 verify.py` in the folder containing this file. Finite tests are not a substitute for Steps 1--4's proof for all integers.

## Relationship to prior work

Huxley, Lettington and Schmidt (2026) define the divisor-function polynomials and give the **already known** positive sum-system transform, plus Dirichlet-series identities (their Theorem 5.1, Remark 5.2, and Theorem 5.3). The new assertion is the **simultaneous strict ordering of every individual coefficient** under prime-exponent majorization, and the consequent complete extremizer classification for all ordered sum-system dimensions; it does not assert novelty for the transforms or binomial formulas. Law, Lettington and Schmidt (2025), and Hylock, Lettington and Schmidt (2026), enumerate multifactorizations and colored-path encodings but do not establish this exponent-balancing theorem. Lettington and Schmidt (2020) develop nontrivial divisor functions and joint sum systems. Fink (2023) derives hypergeometric and divisor-count formulas for the total ordered-factorization function \(K(n)\), whereas the theorem here concerns **every fixed length** and simultaneously all sum-system part counts. Classical Schur positivity and Kostka dominance are used, not presented as newly proved representation-theoretic facts.

## Limitations

Counts depend only on exponent shapes, so this does **not** compare the integer magnitudes of distinct exponent profiles or assert ordering at fixed numerical size. The strict range is \(2\le j,m\le\Omega(n)\); length-one counts are constant, and counts with too many factors or parts are zero. The result is a same-document mathematical argument and finite reproducibility check, not an independent audit. Potential prior implicit coverage by a general theorem on multiset occupancy or symmetric-function dominance remains a residual novelty risk; no claim of exhaustive literature coverage is made.

## References

1. M. N. Huxley, M. C. Lettington and K. M. Schmidt, *On Divisor Function Polynomials and Dirichlet Series* (2026), arXiv:2610.13864, Theorem 5.1 and Remark 5.2. https://arxiv.org/html/2610.13864v1
2. A. D. Law, M. C. Lettington and K. M. Schmidt, *Multifactorisations and divisor functions*, *Utilitas Mathematica* **125** (2025), 43–60. DOI 10.61091/um125-03. https://combinatorialpress.com/article/um/volume%20125/multifactorisations-and-divisor-functions.pdf
3. H. G. Hylock, M. C. Lettington and K. M. Schmidt, *On c-polynomial factorisations* (2026), arXiv:2609.38567. https://arxiv.org/abs/2609.38567
4. M. C. Lettington and K. M. Schmidt, *Divisor functions and the number of sum systems*, *Integers* **20** (2020), A61. https://orca.cardiff.ac.uk/id/eprint/133889/8/u61.pdf
5. T. M. A. Fink, *Number of ordered factorizations and recursive divisors* (2023 preprint), arXiv:2307.16691. https://arxiv.org/html/2307.16691v1
6. Classical Pieri rule and Young's rule/Kostka dominance criterion, as in I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., Chapter I.
