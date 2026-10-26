# Positive prime classes and the correct order of the exceptional signs in a Möbius constant

## Finding

Assume GRH for every Dirichlet \(L\)-function. With the constants \(C(k,l)\) defined below, let
\[
N_+(k)=\#\{1\le l\le k:\gcd(l,k)=1,\ C(k,l)>0\}.
\]
For every fixed real \(0<c<1/2\), as integers \(k\to\infty\),
\[
\liminf_{k\to\infty}\min_{\substack{r\le c\varphi(k)\\r\text{ prime},\ r\nmid k}}\frac{\varphi(k)C(k,r)}{e^\gamma\log k}\ge\frac1c-2>0.
\]
In particular, for all sufficiently large \(k\), *every* prime \(r\le c\varphi(k)\) not dividing \(k\) has \(C(k,r)>0\). Moreover,
\[
\liminf_{k\to\infty}\frac{N_+(k)\log k}{\varphi(k)}\ge\frac12,
\qquad N_+(k)\asymp\frac{\varphi(k)}{\log k}.
\]
The upper bound in the final estimate is Thakur's Theorem 5; the uniform lower envelope and resulting matching lower order are the new assertions.

## Assumptions and scope

Let \(k\ge3\) be an integer, \(\varphi\) Euler's totient function, and \(\gamma\) Euler's constant. For primes \(p\) and real \(x\ge1\), define
\[
Z(x)=\prod_{p\le x}(1-p^{-1})^{-1},\qquad W(p)=\frac{Z(p)}p.
\]
For each reduced class \(l\pmod k\), use the convergent, ordered prime series of Thakur (2026):
\[
C(k,l)=-\frac1{\varphi(k)}+\lim_{X\to\infty}\sum_{p\le X}
\left(\mathbf{1}_{p\equiv l\pmod k}-\frac1{\varphi(k)}\right)W(p).
\]
Convergence and the truncation formula below follow from the source paper. GRH is essential to the uniform tail estimate used here. All asymptotics let \(k\) tend through **all** positive integers, not merely prime moduli. The minimum in the displayed formula is over the indicated nonempty set for sufficiently large \(k\).

## Proof

**1. Uniform truncation.** Thakur's Lemma 4, combined with his GRH character-tail estimate (equation (2), Section 4), implies for every \(X\ge k\), uniformly in the reduced residue \(l\),
\[
C(k,l)=\sum_{\substack{p\le X\\p\equiv l\pmod k}}W(p)-\frac{Z(X)}{\varphi(k)}+E_{k,l}(X),\qquad
|E_{k,l}(X)|\ll\frac{\log^2(kX)}{\sqrt X}.
\tag{1}
\]
To check the uniformity: for primes \(p>X\ge k\), none divides \(k\). Dirichlet-character orthogonality expresses each centered residue-class indicator as the average of nonprincipal characters. The source bounds the weighted tail of every such character by the right side of (1), uniformly in its character, and averaging does not increase it.

**2. Isolating the small prime.** Fix \(c\in(0,1/2)\) and any \(\delta>0\). Put \(X=k^{2+\delta}\). For any prime \(r\le c\varphi(k)\) with \(r\nmid k\), we have \(r<k\) and \(r\le X\), so the sum in (1) includes the nonnegative term \(W(r)\). Thus
\[
C(k,r)\ge W(r)-\frac{Z(k^{2+\delta})}{\varphi(k)}-O\left(\frac{\log^2 k}{k^{1+\delta/2}}\right).
\tag{2}
\]

**3. Uniform prime weight.** Mertens' product theorem states \(Z(y)=(e^\gamma+o(1))\log y\) as \(y\to\infty\). For all sufficiently large \(k\), uniformly over the primes in step 2,
\[
\frac{\varphi(k)W(r)}{e^\gamma\log k}\ge \frac1c-o(1).
\tag{3}
\]
Indeed, for large \(r\), Mertens gives \(W(r)\ge(e^\gamma-\varepsilon)\log r/r\); the function \(\log u/u\) decreases for \(u\ge3\), so its minimum for \(r\le c\varphi(k)\) occurs at the upper endpoint. The finitely many smaller primes have fixed positive weights and therefore satisfy (3) as well. Finally \(\log\varphi(k)/\log k\to1\), using the standard lower estimate \(\varphi(k)\gg k/\log\log k\).

**4. Lower envelope and counting.** Mertens and the choice of \(X\) yield
\[
\frac{Z(X)}{e^\gamma\log k}=2+\delta+o(1),\qquad
\frac{\varphi(k)\log^2(kX)}{\sqrt X\log k}\ll\frac{\log k}{k^{\delta/2}}=o(1).
\]
Multiply (2) by \(\varphi(k)/(e^\gamma\log k)\) and apply (3): the uniform liminf is at least \(1/c-(2+\delta)\). Since this holds for every fixed \(\delta>0\), the claimed bound \(1/c-2\) follows. In particular it is positive for fixed \(c<1/2\).

Each eligible prime \(r\le c\varphi(k)\) represents a different reduced residue class because \(c\varphi(k)<k\). The prime number theorem and \(\omega(k)\le\log k/\log2\) give
\[
N_+(k)\ge\pi(c\varphi(k))-\omega(k)
=(c+o(1))\frac{\varphi(k)}{\log k}.
\]
Let \(c\uparrow1/2\) *after* taking the limit inferior to obtain \(1/2\). The published Theorem 5 gives \(\#\{l:C(k,l)\ge0\}\ll\varphi(k)/\log k\), which supplies the matching upper bound for \(N_+(k)\). This completes the proof.

## Verification

The argument is analytic, not a finite search: the crucial inputs are the exact identity in the source's Lemma 4, its uniform GRH tail estimate for nonprincipal Dirichlet characters, Mertens' product theorem, the prime number theorem, and \(\varphi(k)\gg k/\log\log k\). Formula (1) checks the normalization of the original constant, including the \(-1/\varphi(k)\) term folded into \(-Z(X)/\varphi(k)\). The factor \(k^{2+\delta}\) is what makes the tail smaller than the scale \(\log k/\varphi(k)\). The proof does not depend on a numerical GRH verification or a finite parameter enumeration.

## Relationship to prior work

Deep Thakur, *On a series related to the Möbius function*, arXiv:2610.23660v1 (first publicly posted 16 October 2026), defines \(C(k,l)\), establishes its series and truncation identity (Lemma 4), and proves under GRH that the number of nonnegative constants is at most of order \(\varphi(k)/\log k\) (Theorem 5). That upper bound by itself permits the exceptional set to be empty or much smaller. The new lower envelope identifies an explicit family of positive classes and gives the reverse order bound. This deduction depends essentially on the source's analytic estimates; it is not claimed as an independent proof of them. Related work of Alladi--Johnson and Tenenbaum concerns the weighted Möbius sum rather than this sign-count lower bound.

## Limitations

All results are conditional on GRH and are asymptotic in \(k\). The method gives a lower bound, not an exact asymptotic constant for \(N_+(k)\), and does not classify the signs in the remaining reduced residue classes. The sharpness of \(1/2\) is not established. The inference may be implicit in other literature; no independent review has been conducted.

## References

1. Deep Thakur, *On a series related to the Möbius function*, arXiv:2610.23660v1 (16 October 2026), https://arxiv.org/html/2610.23660v1; especially Lemma 4, equation (2), and Theorem 5.
2. K. Alladi and J. Johnson, *Duality between prime factors and the prime number theorem for arithmetic progressions—II*, Ramanujan Journal 69 (2026), article 52 (background on the series, cited by Thakur).
3. G. Tenenbaum, *On a family of arithmetic series related to the Möbius function*, Ramanujan Journal 69 (2026), article 88 (background on partial sums, cited by Thakur).
4. Classical Mertens product theorem, prime number theorem, and totient lower bound.
