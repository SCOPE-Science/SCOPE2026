# Uniform primorial obstructions for primitive two-generator Frobenius numbers

## Finding

For positive coprime integers \(a,b\ge2\), let \(G(a,b)\) be the largest nonnegative integer that cannot be written \(ax+by\) with \(x,y\in\mathbb Z_{\ge0}\) and \(\gcd(x,y)=1\). Finiteness is established in the cited literature.

Let \(p_1=2,p_2=3,\ldots\) be the increasing primes. For every integer \(k\ge2\), set \(M_k=\prod_{i=1}^{k-1}p_i\). **For every coprime pair satisfying \(\min(a,b)>M_k\)**, there are explicitly constructible integers \(1\le c,d\le M_k\) for which
\[
N=k ab-ac-bd>0,
\]
is not primitively representable. In particular,
\[
\boxed{G(a,b)\ge k ab-M_k(a+b).}
\]

Writing \(H=\min(a,b)\), the prime number theorem consequently gives the uniform bound
\[
\boxed{\liminf_{\substack{\gcd(a,b)=1\\H\to\infty}}
\frac{G(a,b)\log\log H}{ab\log H}\ge1.}
\]
The assertion is uniform over *all* coprime pairs with both parameters growing, not merely a specially selected subsequence. In particular, \(G(a,b)/(ab)\to+\infty\) uniformly as \(\min(a,b)\to\infty\).

As an explicit finite-scale consequence, for all coprime integers \(a,b\ge413\),
\[
\boxed{G(a,b)>4(ab-a-b).}
\]
This numerical cutoff is sufficient, not asserted optimal.

## Assumptions and scope

All integers \(a,b\) are positive, coprime, and the multipliers \(x,y\) must be nonnegative and relatively prime (allowing a zero multiplier only when the other is one). The theorem is about the largest exception, not the classical unrestricted Frobenius number \(ab-a-b\). The lower bound applies whenever \(\min(a,b)>M_k\), with no restriction on common factors of \(a\) or \(b\) with \(M_k\), and no conditional analytic hypotheses.

## Proof

**Exact finite construction.** Fix \(k\ge2\) and \(M=M_k<\min(a,b)\). For each \(t=1,\ldots,k-1\), impose the two congruences
\[
c\equiv tb\pmod{p_t},\qquad d\equiv(k-t)a\pmod{p_t}.
\]
The moduli \(p_t\) are pairwise coprime. By the Chinese remainder theorem each system admits exactly one representative in \([1,M]\). Take these representatives as \(c,d\), and put \(N=kab-ac-bd\). Since \(c<b\) and \(d<a\), one has \(N>(k-2)ab\ge0\), so \(N\) is positive. Also \(N\ge kab-M(a+b)\).

Suppose \(ax+by=N\) with \(x,y\ge0\). Reduction modulo \(b\), together with \(\gcd(a,b)=1\), gives \(x\equiv-c\pmod b\); hence \(x=tb-c\) for some integer \(t\). Substitution yields \(y=(k-t)a-d\). Because \(0<c<b\) and \(0<d<a\), nonnegativity is **equivalent** to \(1\le t\le k-1\). For each such \(t\), the prescribed congruences give
\[
p_t\mid tb-c=x,\qquad p_t\mid(k-t)a-d=y.
\]
Thus \(\gcd(x,y)\ge p_t>1\) for *every* nonnegative representation. No primitive representation exists, proving \(G(a,b)\ge N\ge kab-M(a+b)\).

**Uniform logarithmic growth.** Let \(H\to\infty\) through the minimum of any coprime \(a,b\), and fix \(0<\varepsilon<1\). Choose
\[
k=\left\lfloor(1-\varepsilon)\frac{\log H}{\log\log H}\right\rfloor.
\]
For sufficiently large \(H\), this is at least \(2\). The prime number theorem, in the equivalent standard form \(\log\prod_{i=1}^{m}p_i=(1+o(1))m\log m\), implies
\[
M_k=H^{1-\varepsilon+o(1)}=o(H).
\]
Hence \(M_k<H\), and dividing the finite inequality by \(ab\) gives
\[
\frac{G(a,b)}{ab}\ge k-M_k\left(\frac1a+\frac1b\right)
\ge k-\frac{2M_k}{H}.
\]
Multiplying by \(\log\log H/\log H\) and taking the lower limit yields at least \(1-\varepsilon\). Let \(\varepsilon\downarrow0\). All error terms depend only on \(H\), so the bound is uniform in the pair \((a,b)\).

**Explicit fourfold threshold.** Take \(k=5\), when \(M_k=2\cdot3\cdot5\cdot7=210\). For \(a,b\ge413\), \(ab/(a+b)\ge\min(a,b)/2\ge413/2>206\). Therefore
\[
5ab-210(a+b)>4ab-4(a+b)=4(ab-a-b).
\]
The proved obstruction gives the strict result.

## Verification

The accompanying standalone \(\texttt{verify.py}\) uses only Python standard-library exact arithmetic. It checks \(464\) Chinese-remainder witnesses, including distinct prime factors of every nonprimitive representation, and independently enumerates all representations for \(150\) small configurations (\(222\) candidate representations). It also checks five illustrative pairs against the explicit fourfold threshold. Expected output:

```text
VERIFY_OK crt_cases=464 independent_exhaustive_cases=150 nonprimitive_representations=222 threshold_pairs=5
```

Finite checks are diagnostic, not an infinite proof. The universal claims follow from the displayed CRT argument and the classical prime number theorem.

## Relationship to prior work

Ding, Wang and Zhang [1] introduced and studied the primitive-multiplier Frobenius invariant; their Theorem 1.6 proves \(ab\le G(a,b)\ll ab(\log ab)^2\), and Theorem 1.7 establishes a logarithmic lower-growth phenomenon for a **fixed first generator** along a selected infinite sequence of second generators. Neither statement yields a lower bound growing uniformly with \(\min(a,b)\) for *every* coprime pair. Their Section 4 uses Jacobsthal estimates and a different congruence construction for that fixed-parameter subsequence. The present proof covers every index in the short solution interval with a prescribed distinct prime and obtains a new all-pairs lower bound.

Jaffe [2] independently treats this same invariant using Farey and Stern sequences; Section 7 conjectures a global fourfold lower bound. The result above supplies that proposed inequality for all pairs with \(\min(a,b)\ge413\), but does not resolve the conjecture when one generator is smaller. The bound and asymptotic presented here are not asserted to be present in either paper. The classical unrestricted two-coin formula, Jacobsthal estimates, the Chinese remainder theorem, and the prime number theorem are established ingredients, not claimed as new.

## Limitations

The argument is a **lower bound only**; it neither calculates \(G(a,b)\) exactly nor proves that the logarithmic constant \(1\) is optimal. The explicit cutoff \(413\) is not optimized and does not settle small-generator cases of the fourfold conjecture. A literature search cannot rule out an implicit or differently named prior CRT construction. The proof makes no claim for pairs with \(\min(a,b)\le M_k\) at a chosen \(k\).

## References

[1] Y. Ding, W. Wang and H. Zhang, *The Diophantine Frobenius Problem revisited*, arXiv:2509.08599v1 (first publicly submitted 2025-09-10), especially Theorems 1.3, 1.6, 1.7 and §4. https://arxiv.org/pdf/2509.08599

[2] G. N. Jaffe, *Denominators in the Farey Sequence, the Stern Sequence, and the Frobenius Problem with Relatively Prime Multipliers*, arXiv:2610.17267v1 (2026-10-12), especially Theorem 2.1, §6 and Conjecture 7.2. https://arxiv.org/html/2610.17267v1

[3] The prime number theorem, in its standard primorial asymptotic \(\log\bigl(\prod_{i\le m}p_i\bigr)\sim m\log m\).
