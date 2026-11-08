# A binary-weight formula for all odd-parameter Proth semigroups

## Finding
For every integer \(n\ge3\) and every odd integer \(3\le m<2^n\), let
\[
P_m(n)=\left\langle m2^{n+i}+1:i\ge0\right\rangle
\]
and let \(F(P_m(n))\) be its Frobenius number (largest nonnegative integer outside the semigroup). Write \(h=s_2(m)\) for binary Hamming weight and define
\[
t=\min\{v\ge1:2v-s_2(v)\ge h\},\qquad
\delta=h-\bigl(2(t-1)-s_2(t-1)\bigr)-1.
\]
Then the *exact, all-parameter formula* is
\[
\boxed{F(P_m(n))=(m2^n)^2+(m2^n+1)(2t-1)+\delta.}
\]
In particular, \(0\le\delta\le\nu_2(t)\); the correction \(\delta\) can be arbitrarily large. If \(h=2^{r+1}-1\), then \(t=2^r\) and \(\delta=r\). For example, \(m=127\) and \(n=7\) give \(h=7\), \(t=4\), \(\delta=2\), and \(F(P_{127}(7))=264371337\).

## Assumptions and scope
The coefficient \(m\) is odd, at least \(3\), and strictly smaller than \(2^n\); the exponent satisfies \(n\ge3\). The generating set includes all indices \(i\ge0\). Put \(a=m2^n+1\), \(k=n+\lfloor\log_2m\rfloor\), and \(B_i=2^i-1\) for \(1\le i\le k\). Define \(c(j)\) as the least number of the coins \(B_1,\ldots,B_k\) representing \(j\ge0\). Binary weight \(s_2(z)\) counts ones in the ordinary base-two expansion of \(z\), with \(s_2(0)=0\). The binary valuation \(\nu_2(t)\) is the largest \(e\) with \(2^e\mid t\).

## Proof
**1. Reduction to a monotone Apéry weight.** The Apéry-set theorem of Liu--Xin--Ye--Yin (Theorem 5.2, relying on Theorem 2.10) applies because \(2^{\lfloor\log_2m\rfloor}<m<2^{\lfloor\log_2m\rfloor+1}\), \(m<2^n\), and the required auxiliary size inequality \(a\ge k+1\) follows from \(a\ge3\cdot2^n+1>2n\ge k+1\). For each \(0\le j<a\), its representative can be written
\[
N_j=a\,w(j)-j,\qquad w(j)=j+c(j).
\]
The Mersenne coins are canonical for greedy change-making (their Lemma 2.6), so \(c(j)\) is the greedy coin count. Their Lemma 2.11 implies \(w(j)\) is nondecreasing on \(0\le j<a\). The Frobenius number is therefore
\[
F(P_m(n))=\max_{0\le j<a}\{a w(j)-j\}-a.
\]
The new argument evaluates this maximum without scanning the Apéry set.

**2. Exact binary splitting criterion.** If \(j\) is represented by \(L\) Mersenne coins, then \(Y=(j+L)/2\) is a sum of \(L\) powers of two \(2^{i-1}\), each with \(1\le i\le k\). Conversely, whenever \(j+L\) is even, \(Y\) is a positive integer strictly below \(2^k\), and
\[
s_2(Y)\le L\le Y,
\]
start with the binary expansion of \(Y\) and split powers \(2^i=2\cdot2^{i-1}\) until exactly \(L\) summands remain. Each summand has exponent at most \(k-1\), so replacing it with the corresponding coin \(2^{i+1}-1\) yields \(j\) using exactly \(L\) coins. This proves the criterion in the range used below.

**3. The endpoint's exact coin count.** Let \(J=a-1=m2^n\), and set \(f(v)=2v-s_2(v)\). Since \(s_2(v+1)-s_2(v)\le1\), the function \(f\) is strictly increasing. Also \(2h-s_2(h)\ge h\), so \(t\le h\le n<2^{n-1}\). For \(0\le v\le t\), the binary blocks in \(m2^{n-1}+v\) do not overlap:
\[
s_2(m2^{n-1}+v)=h+s_2(v).
\]
An even coin count \(L=2v<2t\) cannot represent \(J\), since \(h+s_2(v)>2v\). At \(v=t\), the splitting criterion gives an exact representation with \(2t\) coins. Here \(m2^{n-1}+t<2^k\) and \(2t\le m2^{n-1}+t\), as \(m<2^{\lfloor\log_2m\rfloor+1}\) and \(t\le n<2^{n-1}\). Hence
\[
c(J)=2t,\qquad w(J)=J+2t.
\]

**4. Determine the final constant-weight plateau.** Put \(s=\delta+1=h-f(t-1)\). Strict increase of \(f\) gives \(1\le s\le h\le n\). For any \(0\le u<s\), the choice \(L=2t+u\) has
\[
(J-u+L)/2=m2^{n-1}+t,
\]
and meets the splitting criterion, so \(c(J-u)\le2t+u\). Indeed \(L\le3n-1\le3\cdot2^{n-1}\le m2^{n-1}+t=Y\), and \(Y<2^k\). Consider a smaller admissible coin count \(L<2t+u\) of the correct parity. It has the form \(L=2v+u\) with \(v<t\). If \(v\ge0\), then
\[
s_2((J-u+L)/2)=h+s_2(v),\quad
h+s_2(v)-(2v+u)\ge s-u>0,
\]
using \(f(v)\le f(t-1)\). Thus it is impossible. If \(v=-d<0\), then \(d\ge1\), \(L=u-2d\ge0\) and \(d\le u/2<n/2<2^{n-1}\). A binary borrow gives
\[
\begin{aligned}
s_2(m2^{n-1}-d)
&=s_2(m-1)+s_2(2^{n-1}-d)\\
&=h+n-2-s_2(d-1)\\
&\ge h+n-1-d>u-2d=L,
\end{aligned}
\]
again impossible. Consequently
\[
c(J-u)=2t+u,\qquad w(J-u)=J+2t\quad(0\le u<s).
\]
At \(u=s\), the choice \(L=2(t-1)+s\) has \(Y=m2^{n-1}+t-1\) and \(s_2(Y)=h+s_2(t-1)=L\), so it is representable. Thus \(w(J-s)\le J+2t-2\). This proves that the final weight plateau consists precisely of the \(s\) integers \(J-s+1,\ldots,J\).

**5. Locate the maximum.** Let \(j_*=J-s+1=a-s\), and write \(W=J+2t\). For \(j_*\le j\le J\), one has \(w(j)=W\), so \(a w(j)-j\) is largest at \(j=j_*\). For \(0\le j<j_*\), monotonicity from step 1 gives \(w(j)\le W-2\), and hence
\[
a w(j)-j\le a(W-2)-j<aW-j_*,
\]
since \(j_*-j<a<2a\). Therefore \(j_*\) is the unique maximizing index. Substituting into the Apéry formula yields
\[
F(P_m(n))=a(J+2t)-(J-s+1)-a
=J^2+a(2t-1)+s-1,
\]
as stated.

**6. Sharpness of the correction.** Since \(f(t)-f(t-1)=1+\nu_2(t)\), we have \(1\le s\le1+\nu_2(t)\), so \(0\le\delta\le\nu_2(t)\). For every \(r\ge2\), take \(h=2^{r+1}-1\), \(m=2^h-1\) and \(n=h\). Then \(t=2^r\), \(s=r+1\), and \(\delta=r\). Thus no uniform constant bound on the correction is possible.

## Verification
The accompanying `check_proth.py` separately computes the Frobenius number by Dijkstra's shortest-path algorithm on the residue graph modulo \(a\). It checks **all 119** admissible pairs with \(3\le n\le7\), involving **599039** residue classes, independently of the formula and the Apéry maximum argument. It also compares the displayed binary-weight data with full greedy Mersenne representations for an additional **2115** larger pairs. The exact program output is documented in `VERIFICATION.md`. These finite tests are not the proof of the unbounded quantifiers.

## Relationship to prior work
Srivastava--Thakkar (arXiv:2311.12462, 2023) gave an explicit Frobenius formula for the restricted family with odd coefficient \(m=2^r+1\), corresponding to one of the already known correction cases. Liu--Xin--Ye--Yin (arXiv:2306.03459, first public 6 June 2023; inspected revision v4) proved the general Apéry description and monotone greedy-weight lemma, as well as closed formulas when the first or second greedy Mersenne digit is nonzero (Theorems 5.4 and 5.5). They explicitly note the missing third-digit regime and identify the parameter \(63\) as an example. An earlier isolated-gap classification also gives the Frobenius value in the nonperfect subfamily; that is not claimed new here.

The present contribution is the *uniform explicit binary-Hamming-weight formula* including the formerly untreated longer zero-prefix regimes. Its genuinely new correction \(\delta\ge2\) occurs for infinitely many parameters, and \(\delta\) is unbounded. The expression uses earlier Apéry theory as a premise; it does not claim novelty for the general existence or algorithmic computation of Apéry representatives.

## Limitations
The theorem is about the ordinary Frobenius number, not pseudo-Frobenius sets, genus, type, or complete gap distributions. It requires odd \(m\ge3\), \(m<2^n\), and \(n\ge3\); \(m=1\), even coefficients, and smaller exponents are not asserted. The proof uses the published Apéry and monotonicity lemmas, independently checked in the stated parameter range. No independent mathematical audit has yet been performed. Priority over all unindexed literature is not established.

## References
1. F. Liu, G. Xin, S. Ye, J. Yin, *On the Frobenius Number and Genus of a Collection of Semigroups Generalizing Repunit Numerical Semigroups*, arXiv:2306.03459 (first public 2023-06-06; inspected v4, 2025), Theorem 2.10, Lemma 2.11, Theorems 5.2, 5.4, 5.5 and Section 5. https://arxiv.org/abs/2306.03459
2. P. Srivastava, D. Thakkar, *The Frobenius Problem for the Proth Numbers*, arXiv:2311.12462v1 (2023-11-21), Theorems 1, 3, 4 and 7. https://arxiv.org/abs/2311.12462
