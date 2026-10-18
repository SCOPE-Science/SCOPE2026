# Prime-counting root monotonicity: Sun’s Conjecture 2.7(i)

## Finding

**Theorem.** Write \(\pi(x)\) for the number of primes not exceeding the real number \(x\). For every integer \(n\ge 5\) and every integer \(1\le k\le n\),
\[
\pi(kn)^{1/k}>\pi((k+1)n)^{1/(k+1)}.
\]
Equivalently, the following strict inequality of positive integers holds:
\[
\pi(kn)^{k+1}>\pi((k+1)n)^k.
\]
This resolves the *first part only* of Conjecture 2.7 in Zhi-Wei Sun, *Problems on combinatorial properties of primes* (2014), as originally formulated.

## Assumptions and scope

All logarithms are natural. The theorem concerns integer \(n\ge5\) and integer \(k\in\{1,\ldots,n\}\), without any upper bound. No assumption about a conjectural prime gap is used. We invoke two previously established results in their ordinary ranges:

1. **Brun–Titchmarsh, explicit Montgomery–Vaughan form.** For real \(x\ge y\ge2\), the number of primes in \((x,x+y]\) is at most \(2y/\log y\).
2. **Rosser–Schoenfeld bound.** For every real \(x\ge17\), \(\pi(x)>x/\log x\).

The remaining finite cases use exact integer arithmetic with a complete, executable enumeration.

## Proof

Put \(A=\pi(kn)\) and \(B=\pi((k+1)n)\). Both are positive, and \(B\ge A\). The desired inequality is equivalent to
\[
k(\log B-\log A)<\log A.
\]

**All integers \(n\ge300\).** Since \(1\le k\le n\), we have \(kn\ge300\) and \(kn\le n^2\). Applying Brun–Titchmarsh with \(x=kn\) and \(y=n\), and Rosser–Schoenfeld at \(x=kn\), gives
\[
0\le B-A\le\frac{2n}{\log n},\qquad
A>\frac{kn}{\log(kn)}.
\]
Because \(\log(1+t)\le t\) for \(t\ge0\),
\[
\begin{aligned}
k(\log B-\log A)
&=k\log\left(1+\frac{B-A}{A}\right)\\
&\le\frac{k(B-A)}{A}\\
&<\frac{2\log(kn)}{\log n}\\
&\le4.
\end{aligned}
\]
Also \(A\ge\pi(300)=62\), and \(\log 62>4\). Indeed, \(e<11/4\), since the exponential series after the quadratic term is strictly bounded by the geometric series \(\sum_{j\ge3} 1/(6\cdot3^{j-3})=1/4\); thus \(e^4<(11/4)^4=14641/256<62\). Therefore
\[
k(\log B-\log A)<4<\log A.
\]
The strict inequality follows for every \(n\ge300\).

**Every integer \(5\le n\le299\).** These are exactly \(44\,840\) ordered pairs \((n,k)\) with \(1\le k\le n\). The accompanying standalone `checker.py` builds an exact prime-count array up to \(299\cdot300=89\,700\), independently reconstructs the entire array by elementary trial division, verifies that both agree at every index, and directly checks
\[
\pi(kn)^{k+1}-\pi((k+1)n)^k>0
\]
for each of those \(44\,840\) pairs. It additionally checks \(\pi(300)=62\). All assertions succeed, and the smallest observed positive difference is \(4\), attained at \((n,k)=(6,1)\). The algorithm is a finite exhaustive proof for precisely the bounded interval to which it is applied, not extrapolation to larger integers.

The analytic argument and the exhaustive bounded certificate together cover all admissible \(n\) and \(k\). \(\square\)

## Verification

Use Python 3's standard library only and run `python3 checker.py`. The checker terminates with `certificate: PASS` after independently calculating \(\pi(j)\) for every integer \(0\le j\le89\,700\), testing all \(44\,840\) admissible small cases by **integer powers**, and checking the threshold data. The tested finite cases are exhaustive; the two external prime-counting bounds and the displayed inequalities are the mathematical proof for all \(n\ge300\). The checker does not verify those externally published analytic bounds.

## Relationship to prior work

Sun's Conjecture 2.7(i) in [1] is **exactly** the displayed strict root inequality, with the same quantifiers \(n>4\) and \(1\le k\le n\). Its companion Conjecture 2.7(ii), concerning square numbers of primes in certain intervals, is different and is not addressed here. The classic estimates [2, 3] are used as ingredients; their separate statements do not explicitly assert this simultaneous normalized-root inequality. Sun and Zhao's subsequent study [4] of values \(\pi(kn)\) investigates other arithmetic properties, not this root monotonicity. Targeted literature and mathematical-results searches did not reveal a prior statement proving the conjecture. Such a search result does not certify historical uniqueness.

## Limitations

The novelty assessment may miss unpublished, unindexed, or differently phrased prior work; in particular a more general normalized-prime-count monotonicity result could imply this theorem. The proof assumes the standard published Brun–Titchmarsh and Rosser–Schoenfeld theorems; neither is reproved here. The finite verification depends on successful execution of `checker.py`, and makes no claim beyond its explicit range. No assertion is made about Conjecture 2.7(ii), or about \(k>n\).

## References

1. Z.-W. Sun, *Problems on combinatorial properties of primes*, arXiv:1402.6641 (first publicly submitted 2014-02-25), Section 2, Conjecture 2.7(i). https://arxiv.org/abs/1402.6641 ; https://arxiv.org/pdf/1402.6641
2. H. L. Montgomery and R. C. Vaughan, *The large sieve*, Mathematika **20** (1973), 119–134, doi:10.1112/S0025579300004708. Explicit Brun–Titchmarsh interval bound.
3. J. B. Rosser and L. Schoenfeld, *Approximate formulas for some functions of prime numbers*, Illinois J. Math. **6** (1962), 64–94, doi:10.1215/ijm/1255631807. Explicit lower bound for \(\pi(x)\).
4. Z.-W. Sun and L. Zhao, *On the set \(\{\pi(kn):k=1,2,3,\ldots\}\)*, arXiv:2004.01080 (2020). https://arxiv.org/abs/2004.01080
