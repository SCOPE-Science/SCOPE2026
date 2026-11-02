# An exact arithmetic criterion for negative association of shifted gcds

## Finding

For an integer \(n\geq 1\), let \(U\) be uniformly distributed over the reduced residue classes modulo \(n\). Fix any integer \(r\geq2\) and arbitrary integer shifts \(a_1,\ldots,a_r\). Define
\[
X_i=\gcd(U-a_i,n)\qquad(1\leq i\leq r).
\]
The convention at \(n=1\) is the unique residue class, so every \(X_i=1\).

A real function on a finite Cartesian product of positive divisors of \(n\) is **divisibility-nondecreasing** when enlarging any input by divisibility cannot decrease its value. The family \((X_i)_{i=1}^r\) is **negatively associated for the divisor order** if, for every pair of disjoint nonempty index sets \(I,J\subseteq\{1,\ldots,r\}\) and every such nondecreasing \(F,G\),
\[
\operatorname{Cov}(F((X_i)_{i\in I}),G((X_j)_{j\in J}))\leq0.
\]
All expectations are finite.

**Theorem.** This full negative association holds **if and only if** both arithmetic conditions are satisfied:

1. For every odd prime \(p\mid n\), the residues modulo \(p\) of the shifts not divisible by \(p\) are pairwise distinct.
2. If \(4\mid n\), the residues modulo \(4\) of the odd shifts are pairwise distinct (hence there are at most two such shifts).

There is no restriction from the prime \(2\) when its exponent in \(n\) is exactly one. Equivalently, **every pair** \((X_i,X_j)\) is negatively associated in the two-variable sense if and only if the entire family is negatively associated; this equivalence is specific to these shifted-gcd variables.

**Illustration.** Taking \(r=2\) and shifts \(1,-1\), the condition always holds, including at powers of two. Put \(X=\gcd(U-1,n)\) and \(Y=\gcd(U+1,n)\). For \(n=2^k m\), with \(m\) odd and \(k\geq0\), their exact mixed mean is
\[
\mathbb E[XY]=\bigl(4k\text{ if }k\geq1;\,1\text{ if }k=0\bigr)\prod_{p^e\parallel m}(2e+1).
\]
Equivalently this is \(\tau(n^2)\) for odd \(n\), and \(\tau(n^2)+\tau((n/2)^2)\) for even \(n\). Classical Menon identities and polynomial gcd-sum methods already imply this mean calculation; it is recorded to illustrate the stronger dependence statement, **not as an originality claim**. Since \(\mathbb EX=\mathbb EY=\tau(n)\), their covariance is strictly negative for \(n\geq3\) and zero for \(n\in\{1,2\}\).

## Assumptions and scope

The modulus \(n\) is any positive integer (not necessarily squarefree), the number of shifts \(r\) is any finite integer at least two, and shifts may repeat or be nonunits. The shared random residue \(U\) ranges **only over units modulo \(n\)**. The order on divisors is the partial order \(d\preceq e\) exactly when \(d\mid e\), not ordinary numerical order. For vector arguments the order is coordinatewise. A family is negatively associated if every disjoint pair of coordinate groups satisfies the displayed covariance inequality, regardless of the signs of the test functions (monotonicity is essential).

## Proof

**Step 1: a local lemma.** Consider a random vector \((Z_1,\ldots,Z_r)\) in a finite product of partially ordered sets, with a deterministic coordinatewise lower bound \(b=(b_1,\ldots,b_r)\), and suppose that in each realized vector at most **one coordinate** is strictly above its lower bound. For disjoint nonempty coordinate groups \(I,J\), set
\[
H=F(Z_I)-F(b_I),\qquad K=G(Z_J)-G(b_J).
\]
For any coordinatewise nondecreasing real-valued \(F,G\), both \(H,K\) are nonnegative. Their product vanishes pointwise because changes above baseline cannot occur in both disjoint groups. Therefore
\[
\operatorname{Cov}(F(Z_I),G(Z_J))=-\mathbb EH\,\mathbb EK\leq0.
\]
This proves local full negative association. Constant coordinates are allowed.

**Step 2: analyze a prime power.** Fix \(p^e\parallel n\), and let \(U_p\) be uniform over units modulo \(p^e\). Set
\[
Z_{i,p}=\gcd(U_p-a_i,p^e).
\]
If \(p\mid a_i\), then \(Z_{i,p}=1\) for every unit \(U_p\). For an odd prime \(p\), any shift not divisible by \(p\) has baseline \(1\), and \(Z_{i,p}>1\) implies \(U_p\equiv a_i\pmod p\). Under condition 1 the nonzero shift residues are all distinct, so at most one local coordinate exceeds baseline \(1\); Step 1 applies.

For \(p=2\), an even shift gives the constant \(Z_{i,2}=1\), while an odd shift gives \(Z_{i,2}\geq2\) for each odd \(U_2\). If \(e=1\), all these coordinates are constant. If \(e\geq2\), then \(Z_{i,2}>2\) precisely when \(U_2\equiv a_i\pmod4\). Under condition 2, at most one such coordinate can exceed its baseline. Again Step 1 applies with baselines \(1\) for even shifts and \(2\) for odd shifts. This proves local full negative association at every prime power.

**Step 3: combine prime powers.** The Chinese remainder theorem makes the vectors \((Z_{i,p})_{i=1}^r\) independent as \(p\) varies. Each global shifted gcd is their coordinatewise product:
\[
X_i=\prod_{p^e\parallel n}Z_{i,p}.
\]
For completeness, negative association is preserved when independent negatively associated vectors are concatenated: by the law of total covariance, the covariance of two nondecreasing functions on disjoint groups of concatenated coordinates is the sum of (a) a nonpositive conditional covariance from the first group and (b) the nonpositive covariance of their nondecreasing conditional means on the second. Induction gives the assertion for any finite set of independent prime-power vectors. Taking the coordinatewise product of each coordinate's prime-power factors is a nondecreasing function of **that coordinate's own factors**; these factor sets are disjoint between different global coordinates. Applying the definition to the resulting disjoint input groups proves the full global negative association.

**Step 4: necessity, including every boundary.** Suppose condition 1 fails. Then for some odd \(p\mid n\) there are distinct indices \(i,j\) with \(p\nmid a_i a_j\) and \(a_i\equiv a_j\pmod p\). The two divisibility-increasing indicators
\[
\boldsymbol{1}_{\{p\mid X_i\}},\qquad\boldsymbol{1}_{\{p\mid X_j\}}
\]
are identical to the nonconstant event \(U\equiv a_i\pmod p\), which has probability \(1/(p-1)\) among units. Their covariance is its strictly positive variance, contradicting negative association.

If condition 2 fails, then \(4\mid n\), and two odd shifts are congruent modulo \(4\). The two increasing indicators \(\boldsymbol{1}_{\{4\mid X_i\}}\) and \(\boldsymbol{1}_{\{4\mid X_j\}}\) are identical to the event \(U\equiv a_i\pmod4\), whose probability is \(1/2\). Their covariance is \(1/4>0\). Thus each displayed arithmetic condition is necessary. Necessity uses **two coordinates only**, proving the pairwise-to-full equivalence.

**Step 5: opposite-shift illustration.** At an odd prime \(p\), \(U-1\) and \(U+1\) cannot both be divisible by \(p\). If \(p^e\parallel n\), the local gcds therefore satisfy \(Z_{1,p}Z_{2,p}=Z_{1,p}+Z_{2,p}-1\). Menon's identity gives each mean \(e+1\) because the shifts \(1,-1\) are units; hence \(\mathbb E[Z_{1,p}Z_{2,p}]=2e+1\). For \(2^k\parallel n\), \(k\geq1\), both local gcds are at least \(2\) and one is exactly \(2\), so \(Z_{1,2}Z_{2,2}=2Z_{1,2}+2Z_{2,2}-4\); their means are both \(k+1\), yielding \(4k\). CRT and multiplication of these expectations give the stated formula. The strict covariance assertion follows from \((e+1)^2>2e+1\) for \(e\geq1\), \((k+1)^2\geq4k\) with equality only at \(k=1\), and the fact that products of local means dominate products of local mixed means. The case \(n=1\) is constant.

## Verification

The standalone script `verify.py` uses only the Python standard library. It enumerates all increasing upper-set indicators for **3,751** pairs \((n,a,b)\) with \(1\leq n\leq31\) and \(-5\leq a,b\leq5\), and matches the sharp local criterion. It also tests **1,250** three-shift triples with \(1\leq n\leq10\) and shifts between \(-2\) and \(2\); in accepted cases it checks **62,484** inequalities over all relevant upper-set events for disjoint coordinate groups, while in rejected cases it locates a pairwise obstruction. Finally it verifies the opposite-shift mixed mean directly for every \(1\leq n<200\). Test functions on each finite divisor poset are controlled by upper-set indicator inequalities via the layer-cake representation. These finite checks are corroboration, **not** a proof for arbitrary modulus or shift count; Steps 1–5 give the general proof.

## Relationship to prior work

Menon's classical theorem gives the one-shift gcd mean. Tóth's archival study of gcd-sum functions treats multiplicative average identities and generalizations of Menon's formula, not full negative association of multiple shifts sampled at the **same** unit residue [1]. Tóth's later survey explains polynomial gcd-sum identities and separately multivariable sums with independent residue coordinates [2, Sections 4.4, 4.13]. The exact mixed mean in the opposite-shift illustration is already covered by elementary local averaging and related polynomial Menon identities; **that corollary is not the claimed novelty**.

Joag-Dev and Proschan established the general concept and closure principles of negative association [3]. That framework supplies the general probabilistic mechanism, not the sharp number-theoretic congruence criterion at every prime—including the exceptional threshold from \(2\) to \(4\)—nor its pairwise-to-full consequence for shifted gcd families. Searches for equivalent formulations, stronger theorems and database claims did not identify a prior classification of these precise shifted-gcd variables. This is a best-knowledge originality assessment, not a guarantee of uniqueness.

## Limitations

The theorem concerns only a **uniform reduced residue** and the divisor partial order. It does not claim ordinary real-order negative association for arbitrary nonmonotone observables, nor classify random residues without the coprimality restriction. Failure of the criterion guarantees an explicit increasing-event **positive** covariance, but does not assert that the covariance of the raw scalar gcd values must always be positive. The moment illustration is not new. Literature coverage, particularly for specialized probability-arithmetic work not located by the searches, remains a residual originality risk. Independent mathematical audit has not been performed.

## References

[1] L. Tóth, *Another generalization of the gcd-sum function*, arXiv:1306.1020, first public version June 5, 2013, https://arxiv.org/abs/1306.1020 .

[2] L. Tóth, *Proofs, generalizations and analogs of Menon's identity: a survey*, arXiv:2110.07271v4, 2023, Sections 4.4 and 4.13, https://arxiv.org/html/2110.07271v4 .

[3] K. Joag-Dev and F. Proschan, *Negative Association of Random Variables with Applications*, Annals of Statistics 11 (1983), 286–295, https://doi.org/10.1214/aos/1176346079 .
