# Sharp multiplicity gaps for evil–odious additive decompositions

## Finding
For each nonnegative integer \(n\), let \(s_2(n)\) be its number of ones in binary and put \(t(n)=(-1)^{s_2(n)}\). Let \(R(n)\) be the number of ordered pairs \((e,o)\) of nonnegative integers satisfying \(e+o=n\), \(t(e)=1\), and \(t(o)=-1\). Thus \(e\) is evil and \(o\) is odious, with the order fixed by parity type.

The precise complete classification is as follows.

1. If \(n=4^k-1\) for an integer \(k\ge0\), then \(R(n)=0\).
2. If \(n=2\cdot4^k-1\) for an integer \(k\ge0\), then \(R(n)=(n+1)/2\).
3. For every other nonnegative integer \(n\),
   \[
   \frac{n+1}{10}\le R(n)\le\frac{2(n+1)}5.
   \]
   Equality in the lower bound occurs precisely for \(n=10\cdot4^k-1\), \(k\ge0\), and equality in the upper bound occurs precisely for \(n=5\cdot4^k-1\), \(k\ge0\).

In particular, the only integers without an evil–odious sum representation are \(4^k-1\), and every other integer outside the second exceptional class has at least a tenth of the theoretically available \(n+1\) pairs in this orientation. The sharp constants are attained infinitely often.

Equivalently, define the signed self-convolution
\[
 C(n)=\sum_{j=0}^n t(j)t(n-j).
\]
At \(n=2^k-1\) one has \(C(n)=(-1)^k(n+1)\), whereas at every other \(n\),
\[
 |C(n)|\le \frac35(n+1).
\]
In the latter inequality equality occurs **if and only if** \(n=5\cdot2^j-1\) for some integer \(j\ge0\), and its normalized sign then equals \((-1)^{j+1}\).

## Assumptions and scope
All variables are ordinary nonnegative integers; zero is permitted as an evil summand. Each representation consists of one evil integer and one odious integer and is counted exactly once (the two parity types distinguish the entries). The result is about unrestricted additive decompositions, not decompositions into primes or positive summands only. The normalizing denominator \(n+1\) counts all ordered decompositions of \(n\) into nonnegative integers. No asymptotic approximation is used in the inequalities or equality classifications.

## Proof
**1. Signed generating function.** From the binary digit-sum identities \(t(2j)=t(j)\) and \(t(2j+1)=-t(j)\), the formal series \(T(z)=\sum_{n\ge0}t(n)z^n\) satisfies \(T(z)=(1-z)T(z^2)\). Its square has coefficients \(C(n)\), so
\[
 C(0)=1,\quad C(2m)=C(m)+C(m-1)\ (m\ge1),\quad C(2m+1)=-2C(m)\ (m\ge0).
\]
These are identities of formal power series and need no convergence hypothesis.

**2. Uniform sharp bound at even indices.** Applying the recurrence once more yields, for \(m\ge1\),
\[
 C(4m)=C(m)-C(m-1),\qquad C(4m+2)=C(m-1)-C(m).
\]
Each summand in \(C(j)\) is a sign; hence \(|C(j)|\le j+1\). Consequently
\[
 |C(4m)|\le2m+1\le\frac35(4m+1),
\]
where the *second* inequality is an equality only for \(m=1\), and
\[
 |C(4m+2)|\le2m+1<\frac35(4m+3).
\]
The remaining even index \(n=2\) has \(C(2)=-1\), also satisfying the strict bound. At \(n=4\) one has \(C(4)=-3\). Therefore every positive even index satisfies the three-fifths bound, and equality occurs precisely at \(n=4\).

**3. Removing a terminal run of ones.** The odd recurrence shows
\[
 \frac{C(2m+1)}{2m+2}=-\frac{C(m)}{m+1}.
\]
Every nonnegative integer uniquely has the form \(n=(q+1)2^j-1\) with \(q\) even and \(j\ge0\): simply remove all trailing binary ones, permitting \(q=0\) when every digit is one. Iterating gives
\[
 \frac{C(n)}{n+1}=(-1)^j\frac{C(q)}{q+1}.
\]
If \(q=0\), then \(n=2^j-1\) and \(C(n)/(n+1)=(-1)^j\). Otherwise \(q\) is a positive even integer. Step 2 gives the three-fifths bound, and equality forces \(q=4\); thus \(n=5\cdot2^j-1\), with sign \((-1)^{j+1}\). Conversely all such indices attain the bound by the recurrence.

**4. Mixed representations.** The indicator functions of evil and odious integers are \((1+t(j))/2\) and \((1-t(j))/2\). Their convolution gives
\[
 R(n)=\frac14\sum_{j=0}^n(1+t(j))(1-t(n-j))
 =\frac{n+1-C(n)}4.
\]
The two linear sign sums cancel after replacing \(j\) by \(n-j\). For \(n=2^j-1\), Step 3 gives \(R(n)=0\) if \(j\) is even and \(R(n)=(n+1)/2\) if \(j\) is odd. These two cases are respectively \(n=4^k-1\) and \(n=2\cdot4^k-1\). For non-Mersenne indices, Step 3 gives the exact displayed lower and upper inequalities. The lower equality corresponds to \(C(n)/(n+1)=3/5\), which occurs at \(n=5\cdot2^j-1\) with odd \(j=2k+1\), namely \(n=10\cdot4^k-1\). The upper equality corresponds to even \(j=2k\), namely \(n=5\cdot4^k-1\). Every integer satisfies exactly one case, completing the proof.

## Verification
The included `verify.py` computes \(C(n)\) from its exact dyadic recurrence for every \(0\le n<524288\), independently recomputes both the signed self-convolution and the mixed representation count directly from binary digit parity for every \(0\le n\le2048\), and checks all claimed exceptional values, bounds and equality families in its range. It prints `VERIFIED` on successful completion. The finite tests are checks of the implementation and special cases, not the basis of the all-index proof.

To reproduce, run `python3 verify.py` with standard Python 3 (no third-party dependencies).

## Relationship to prior work
Gawron, Miska and Ulas study the coefficients of powers of the Thue–Morse generating product; their twofold coefficients are precisely \(C(n)\), and dyadic recurrences, valuations and extremal coefficient behavior are part of that earlier theory. Allouche and Shallit study the additive properties of the evil and odious sequences and establish results about equal-parity two-sums and larger numbers of summands. The present claim concerns the complementary mixed-parity representation function and gives a **uniform sharp normalized coefficient gap at all non-Mersenne indices**, including the complete exceptional, lower-extremal and upper-extremal classes. Neither cited paper is claimed as newly defining the sequences, signed convolution or recurrence. OEIS A106407 records the signed squared-product coefficients; a known coefficient table by itself does not assert the infinite sharp inequality and equality classification.

## Limitations
The claim is only for sums of nonnegative numbers in different binary parity classes. It does not imply analogous bounds for restricted prime summands, higher convolutions, or other bases. Literature comparisons do not establish formal publication priority: unindexed or inaccessible earlier results may exist. The mathematical reasoning and computational replay here have not received an independent audit.

## References
- M. Gawron, P. Miska and M. Ulas, *Arithmetic properties of coefficients of power series expansion of \(\prod_{n\ge0}(1-x^{2^n})^t\)*, arXiv:1703.01955v1 (first public March 6, 2017), https://arxiv.org/abs/1703.01955.
- J.-P. Allouche and J. Shallit, *Additive Properties of the Evil and Odious Numbers and Similar Sequences*, arXiv:2112.13627v1 (first public December 27, 2021), https://arxiv.org/abs/2112.13627.
- OEIS Foundation, A106407, *Expansion of \(x\prod_{k\ge0}(1-x^{2^k})^2\)*, https://oeis.org/A106407 (coefficient indexing differs by a shift).
