# Cototient-derivative rigidity for an even two-prime support

## Finding

For each odd prime \(p\) and all integers \(a,b\ge1\), put \(n=2^a p^b\). The equation
\[
D(n-\varphi(n))=n
\]
holds **if and only if** \(a=2\), \(b=1\), and precisely one of the following mutually exclusive conditions holds, with \(p+1=2^t u\) and \(u\) odd:

1. \(t=1\), \(p=2u-1\) prime, \(u\ge3\) odd, and \(D(u)=u-1\).
2. \(t=2\), \(p=4u-1\) prime, \(u\ge1\) odd, and \(2D(u)=u-1\).

In either branch, \(u\) must be squarefree. Thus all solutions on this prime support have shape \(n=4p\), and none has \(p\equiv7\pmod8\). The observed instances \(n=12,44,332\) come from \(u=1,3,21\) in the second branch.

## Assumptions and scope

The arithmetic derivative \(D\) is uniquely defined on positive integers by \(D(1)=0\), \(D(q)=1\) for primes \(q\), and \(D(xy)=xD(y)+yD(x)\). Thus \(D(m)=m\sum_{q\mid m}\nu_q(m)/q\) for \(m\ge1\). The function \(\varphi\) denotes Euler's totient. Here \(p\) ranges over every odd prime and \(a,b\) independently range over all positive integers; no upper bound is imposed. The result concerns **exactly** the numbers with prime support \(\{2,p\}\), not odd integers, powers of two, or integers with three or more distinct prime factors.

## Proof

The cototient has the exact factorization
\[
m=n-\varphi(n)=2^{a-1}p^{b-1}(p+1).
\]
Write \(p+1=2^t u\) with \(t\ge1\) and \(u\ge1\) odd. Dividing the equation \(D(m)=n\) by \(m\) yields
\[
\frac{2p}{p+1}=\frac{a-1+t}{2}+\frac{b-1}{p}+\frac{D(u)}{u}.\tag{1}
\]
All terms on the right are nonnegative, because \(D(u)\ge0\) for every positive integer \(u\).

**First, \(b=1\).** If \(b\ge2\), apply the product rule to the displayed factorization of \(m\), cancel \(p^{b-2}\), and reduce modulo \(p\). Since \(p\nmid2^{a-1}(p+1)\), this gives \(p\mid b-1\). Hence \((b-1)/p\ge1\). Since the left side of (1) is strictly below \(2\), necessarily \(a-1+t=1\), so \(a=t=1\). The same strict inequality implies \((b-1)/p<3/2\), and its positive integral value must therefore equal \(1\); thus \(b=p+1\).

Now \(m=p^p(p+1)\). By the product rule, \(D(m)=p^p((p+1)+D(p+1))\). Matching \(n=2p^{p+1}\) forces \(D(p+1)=p-1\). But \(t=1\) gives \(p+1=2u\) with \(u\) odd, so \(D(p+1)=u+2D(u)\) is odd, whereas \(p-1\) is even. This contradiction proves \(b=1\).

**Next, \(a=2\) and \(t\in\{1,2\}\).** With \(b=1\), let \(s=a-1+t\). Because \(m=2^s u\), its derivative is \(2^{s-1}(su+2D(u))\). The equation becomes
\[
su+2D(u)=2^{2-t}p.\tag{2}
\]
For \(t\ge3\) the right-hand side is nonintegral, a contradiction since \(p\) is odd. If \(t=1\), then \(s=a\), \(p=2u-1\), and (2) reads \(au+2D(u)=4u-2\). Parity forces \(a\) even, and \(D(u)\ge0\) forces \(a<4\). Hence \(a=2\) and \(D(u)=u-1\). Because \(p=2u-1\) is odd prime, \(u\ge3\).

If \(t=2\), then \(s=a+1\), \(p=4u-1\), and (2) reads \((a+1)u+2D(u)=4u-1\). Since \(u\) is odd, parity forces \(a\) even. Nonnegativity forces \(a+1<4\), so \(a=2\); then \(2D(u)=u-1\), allowing \(u=1\). Both implications can be reversed in (2), proving sufficiency.

Finally, in either branch the equality takes the form \(cD(u)=u-1\) with \(c=1\) or \(2\). If an odd prime \(q\) occurred at least twice in \(u\), then the product rule would imply \(q\mid D(u)\), and thus \(q\mid u-1\), impossible because \(q\mid u\). Therefore \(u\) is squarefree.

For squarefree \(u\ge3\), the first auxiliary equality is equivalent to \(\sum_{q\mid u}1/q+1/u=1\), the defining equation of an odd primary pseudoperfect number. The second is equivalent to \(\sum_{q\mid u}1/q+1/(2u)=1/2\) (also valid for \(u=1\) by the empty-sum convention). These reciprocal forms explain the relation to existing literature but do not presume either family is exhausted. This completes the proof.

## Verification

A self-contained standard-library Python checker named `verify.py` independently enumerates the equation and the two-branch characterization for all \(2\le n\le200000\) with support \(\{2,p\}\). It also enumerates both auxiliary identities for odd \(u\le50000\). Its replay output is:

```text
VERIFY_OK complete_n=200000 two_support_checked=21172 two_support_hits=[12, 44, 332]
ODD_U_CHECK_OK u_le=50000 half_port=[1, 3, 21, 903, 23529] primary_odd=[1]
```

The value \(u=1\) is a formal solution of \(D(u)=u-1\) but excluded from the first branch because \(2u-1=1\) is not prime. These computations check examples and implementation only: the proof above, not the finite run, supplies the unrestricted conclusion.

## Relationship to prior work

OEIS A248817 (first attributed October 15, 2014) records the full equation and a list beginning with \(12,32,44,332\); in particular, \(32\) lies outside our two-prime-support domain. Its table is not a classification of all \(2^a p^b\). The arithmetic derivative formula is classical and appears in Dahl–Olsson–Loiko (2011). OEIS A054377 and the work of Butske–Jaje–Mayernik record primary pseudoperfect numbers, corresponding here only to the first auxiliary branch after the prime condition. Wang (2026) studies general Egyptian-fraction port equations including the second branch's type, but that does not by itself imply the collapse \(a=2,b=1\) in the cototient-derivative equation. A superficially close statement about \(D(n)-(n-\varphi(n))\) concerns a different expression from \(D(n-\varphi(n))\).

## Limitations

The theorem does **not** assert that \(12,44,332\) are the only solutions on this support. It proves an exact reduction to the two auxiliary prime-constrained equations, whose global enumeration remains open. The existence of an odd primary pseudoperfect integer is unresolved in the cited literature. Other prime supports and the unrestricted equation remain outside scope. The literature search cannot rule out an unindexed earlier derivation; an older paper on primary pseudoperfect numbers was compared through its publicly accessible abstract, not its inaccessible full text.

## References

- OEIS Foundation, *A248817: Numbers that are equal to the arithmetic derivative of their cototient*, https://oeis.org/A248817 (attribution date 2014-10-15).
- OEIS Foundation, *A054377: Primary pseudoperfect numbers*, https://oeis.org/A054377.
- Niklas Dahl, Jonas Olsson and Alexander Loiko, *Investigations on the properties of the arithmetic derivative*, arXiv:1108.4762 (2011), https://arxiv.org/abs/1108.4762.
- William Butske, Lynda M. Jaje and Daniel R. Mayernik, *On the equation \(\sum_{p\mid N}1/p+1/N=1\), pseudoperfect numbers, and perfectly weighted graphs*, Mathematics of Computation 69 (2000), 407–420, DOI:10.1090/S0025-5718-99-01088-1.
- Han Wang, *Port Fillings for Primary Pseudoperfect Numbers*, arXiv:2605.21518 (2026), https://arxiv.org/abs/2605.21518.
