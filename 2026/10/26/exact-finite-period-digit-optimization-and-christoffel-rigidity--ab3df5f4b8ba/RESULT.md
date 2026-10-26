# Exact finite-period digit optimization and Christoffel rigidity in Sturmian beta-shifts

## Finding

For every irrational \(0<\alpha<1\) and integer \(q\ge1\), consider the Sturmian beta-shift \(Y_\alpha\) and the digit observable \(\Phi(x)=x_0\). The best mean of \(\Phi\) among points with \(\sigma^q x=x\) is exactly
\[
\max_{\substack{x\in Y_\alpha\\\sigma^q x=x}}\frac1q\sum_{j=0}^{q-1}x_j
=\frac{\lfloor q\alpha\rfloor}{q},
\qquad
\alpha-\max\frac1q\sum_{j=0}^{q-1}x_j=\frac{\{q\alpha\}}q.
\]
Every period \(q\) has a maximizer: the infinite periodic repetition of the rational upper mechanical word with slope \(\lfloor q\alpha\rfloor/q\).

There is a further *rigidity window*. Put \(p=\lfloor q\alpha\rfloor\). If \(q\ge2\), \(1\le p<q\), \(\gcd(p,q)=1\), and
\[
0<\alpha-\frac pq<\frac1{q^2},
\]
then the complete collection of maximizing \(q\)-periodic points is **exactly the \(q\) cyclic rotations of the rational upper mechanical word**. In particular, this is one orbit of least period \(q\), with no other maximizing periodic orbit of period dividing \(q\). Every irrational slope has infinitely many such rigid periods, because its lower continued-fraction convergents satisfy these hypotheses.

## Assumptions and scope

Use the one-sided binary shift \(\Sigma=\{0,1\}^{\mathbb N_0}\), with the usual lexicographic order and left shift \(\sigma\). Define the infinite maximal Sturmian word by
\[
a_j(\alpha)=\lceil(j+1)\alpha\rceil-\lceil j\alpha\rceil,\qquad j\ge0,
\]
and the shift-invariant closed set
\[
Y_\alpha=\{x\in\Sigma:\sigma^k x\le_{\mathrm{lex}}a(\alpha)\ \text{for every }k\ge0\}.
\]
Here the q-periodic set means \(\mathrm{Fix}(\sigma^q)\), so it includes points of minimal period properly dividing \(q\). For integers \(0\le p<q\), the rational upper mechanical block is
\[
U(p,q)_j=\left\lceil\frac{(j+1)p}{q}\right\rceil-\left\lceil\frac{jp}{q}\right\rceil,
\qquad 0\le j<q.
\]
Write \(U(p,q)^\infty\) for infinite periodic repetition; when \(p=0\), this is the zero fixed point. No bounded-type or Diophantine restriction is imposed on \(\alpha\) for the all-period optimum. The extra close-rational condition is needed only for the asserted uniqueness.

## Proof

**1. Upper bound on the digit count.** Huang–Jenkinson–Xu–Zhang, Proposition 4.6, establishes
\[
\sum_{j=0}^{n-1}x_j\le n\alpha+1
\quad(n\ge1,\ x\in Y_\alpha).
\]
For any \(x\in\mathrm{Fix}(\sigma^q)\), put \(d=\sum_{j=0}^{q-1}x_j\). Apply the inequality with \(n=Nq\), for each positive integer \(N\). Because the word repeats, \(Nd\le Nq\alpha+1\). Letting \(N\to\infty\) gives \(d\le q\alpha\), so integer \(d\le\lfloor q\alpha\rfloor\).

**2. Construction attaining the bound for each \(q\).** Put \(p=\lfloor q\alpha\rfloor\) and \(r=p/q<\alpha\). The block \(U(p,q)\) has exactly \(p\) ones and repeats with period dividing \(q\). For any cyclic rotation, every prefix of positive length \(k\) has at most \(\lceil kr\rceil\) ones: the block count is a difference of two ceilings with arguments differing by \(kr\). Moreover \(\lceil kr\rceil\le\lceil k\alpha\rceil\), the digit count in the first \(k\) entries of \(a(\alpha)\). If a rotated mechanical sequence first exceeded \(a(\alpha)\) lexicographically at coordinate \(k-1\), their preceding symbols would agree and the new digit would have to be 1 rather than 0, giving its length-\(k\) prefix one more 1 than the length-\(k\) prefix of \(a(\alpha)\), a contradiction. Thus *every* shift of \(U(p,q)^\infty\) lies in \(Y_\alpha\). Its q-block frequency is \(p/q\), attaining the bound. Subtract from \(\alpha\) to obtain the stated exact deficit.

**3. Classical cyclic extremality.** Assume now \(\gcd(p,q)=1\) with \(1\le p<q\). A binary word \(w\) of length \(q\) containing \(p\) ones must be primitive. Denote by \(\operatorname{MaxRot}(w)\) its lexicographically greatest cyclic rotation. Its bitwise complement \(\bar w\) has \(q-p\) ones. The least cyclic rotation of \(\bar w\) is a Lyndon word. By the Borel–Laubie theorem (see De Luca–Fici, Proposition 14), among Lyndon words with exactly \(p\) zeros and \(q-p\) ones, the primitive lower Christoffel word is uniquely greatest. Complementing reverses lexicographic order and transforms that lower Christoffel word into \(U(p,q)\). Therefore
\[
\operatorname{MaxRot}(w)\ge_{\mathrm{lex}}U(p,q),
\]
with equality if and only if \(w\) is a cyclic rotation of \(U(p,q)\). For clarity, the complementary lower mechanical block satisfies
\[
1-\left(\left\lfloor\frac{(j+1)(q-p)}q\right\rfloor-\left\lfloor\frac{j(q-p)}q\right\rfloor\right)=U(p,q)_j,
\]
so the identification follows directly from the standard Christoffel construction.

**4. Excluding every other maximizing block in the rigidity window.** Put \(\delta=\alpha-p/q\), so \(0<\delta<1/q^2\). For every integer \(1\le k<q\), the fractional part of \(kp/q\) is at most \(1-1/q\), since \(p,q\) are coprime, and \(k\delta<1/q\). Hence
\[
\lceil k\alpha\rceil=\lceil kp/q\rceil\qquad (1\le k<q).
\]
It follows that the first \(q-1\) symbols of the irrational upper word \(a(\alpha)\) and \(U(p,q)\) agree. Suppose an admissible \(q\)-periodic point with the maximum digit count \(p\) has block \(w\) not conjugate to \(U(p,q)\). Step 3 gives \(\operatorname{MaxRot}(w)>_{\mathrm{lex}}U(p,q)\). Their first unequal bit must occur at one of positions \(0,\ldots,q-2\): they have the same total of \(p\) ones, so two such length-\(q\) words cannot first differ only in the final position. At that position the greatest rotation has 1 while \(U(p,q)\), and therefore \(a(\alpha)\), has 0. It thus violates the lexicographic defining inequality for \(Y_\alpha\). This contradiction leaves exactly the \(q\) rotations of \(U(p,q)\), all admissible by Step 2. Coprimality ensures all rotations are distinct and have least period \(q\).

**5. Infinitely many rigid periods.** Every irrational \(\alpha\in(0,1)\) has infinitely many reduced continued-fraction convergents \(p/q\) from below. These satisfy \(0<\alpha-p/q<1/q^2\), and eventually \(1\le p<q\). The rigidity conclusion applies to all those denominators.

## Verification

The accompanying standalone `verify.py` checks two independent finite aspects using integer arithmetic. First, for every coprime \(1\le p<q\le13\), it exhaustively enumerates all binary words with \(p\) ones, proving by computation over that finite range that the greatest cyclic rotation is at least the rational upper word and that equality occurs precisely for its rotations. Second, for \(\alpha=(\sqrt5-1)/2\), it constructs the first 260 mechanical digits without floating point via integer square roots and exhaustively tests all words of periods \(1\) through \(13\) against those finite lexicographic prefixes. It confirms the claimed maximal q-block counts and the rigid lower-approximation denominators \(q=2,5,13\).

These bounded tests are not exhaustive membership certificates for every irrational slope or an infinite-time proof. The universal theorem follows from the five proof steps above and the explicitly cited mathematical inputs.

## Relationship to prior work

Huang, Jenkinson, Xu and Zhang (2026, §4, Proposition 4.6) established the global maximal digit frequency \(\alpha\) and exhibited first-return loops with lower rational digit frequencies. The present theorem concerns a different and more specific constraint: **every exact length \(q\)** and uniqueness of a maximizing orbit for infinitely many reduced rational approximations. Their global upper bound is used explicitly, not presented as new.

The Borel–Laubie ordering theorem for Christoffel words is a crucial historical ingredient, as documented in De Luca–Fici (2024, Proposition 14). The newly combined argument uses prefix stability of the *irrational* Sturmian ceiling to turn that fixed-content word order into a dynamical exclusion of every competing period-\(q\) maximizer. Sidorov (2011) surveys other balanced-word optimization problems, including cyclic numeral products, not the present finite-period lexicographic beta-shift constraint.

## Limitations

The exact value of the maximizing frequency holds for all positive periods and every irrational slope, but the uniqueness claim is restricted to the stated coprime close-approximation window. Other periods can have several maximizing orbits. The proof does not give a complete classification of multiplicities for arbitrary \(q\), an optimization theorem for observables other than the digit function, or a published-priority guarantee. Classical equivalent applications of Christoffel word extremality may not be indexed by the searched terminology. The included finite enumerations do not certify the infinite result.

## References

1. W. Huang, O. Jenkinson, L. Xu and Y. Zhang, *Sturmian beta-shifts do not have typical periodic optimization*, arXiv:2610.03619v1 (2026), especially §1.2, §1.5, and Proposition 4.6. https://arxiv.org/html/2610.03619v1
2. A. De Luca and G. Fici, *Some Results on Digital Segments and Balanced Words*, arXiv:2211.09417v3 (2024), especially Proposition 14 (Borel–Laubie). https://arxiv.org/pdf/2211.09417
3. N. Sidorov, *Optimizing Properties of Balanced Words*, Electronic Proceedings in Theoretical Computer Science 63 (2011), 240–246, arXiv:1108.3639. https://arxiv.org/pdf/1108.3639
