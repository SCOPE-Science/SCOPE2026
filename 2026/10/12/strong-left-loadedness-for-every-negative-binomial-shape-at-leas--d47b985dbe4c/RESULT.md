# Strong left-loadedness for every negative-binomial shape at least three

## Finding

**Theorem.** Let \(r\ge3\) and \(t\ge1\) be arbitrary integers. Define the nonnegative-integer-valued random variable \(X\) by
\[
\Pr(X=k)=\binom{k+r-1}{r-1}\left(\frac{t}{t+1}\right)^k\left(\frac1{t+1}\right)^r,\qquad k=0,1,2,\ldots.
\]
Its expectation is \(m=rt\). For every integer \(1\le i\le m\), put
\[
\alpha_i=\Pr(X\le m-i)-\Pr(X\ge m+i).
\]
Then \(\alpha_1>0\), \(\alpha_m<0\), and there is an integer \(1\le \ell<m\) such that \(\alpha_i\ge0\) for \(1\le i\le\ell\) and \(\alpha_i\le0\) for \(\ell<i\le m\). Thus every such law satisfies condition \(L_1\) of the left-loadedness definition in Fokkink–Papavassiliou–Pelekis. In particular the result covers every integer shape at least three when the failure probability equals the reciprocal of an integer at least two.

## Assumptions and scope

The negative-binomial convention counts successes before the \(r\)-th failure; a single trial has success probability \(t/(t+1)\). There are no asymptotic limits in the theorem. Both \(r\) and \(t\) are arbitrary *integers* within the stated ranges, and no assertion is made for noninteger shape parameters, arbitrary success probabilities, or shifted/nonintegral centers.

The result is strictly stronger than the center-tail inequality \(\alpha_1>0\): it proves one ordered sign crossing for the *entire* vector of \(rt\) comparisons. For example, when \((r,t)=(3,1)\), the exact values are \(\alpha_1=5/32\), \(\alpha_2=11/128\), and \(\alpha_3=-5/256\).

## Proof

**1. Shape of the entire tail-difference vector.** Write \(w_k=\Pr(X=k)\), \(m=rt\), and for \(0\le i\le m\) set \(\beta_i=w_{m+i}/w_{m-i}\). All these ratios are well defined. For \(0\le i<m\), canceling successive probability masses gives
\[
\frac{\beta_{i+1}}{\beta_i}=\frac{t^2}{(t+1)^2}\frac{(m+i+r)(m-i+r-1)}{(m+i+1)(m-i)}.
\]
The difference between the positive cross-multiplied numerator and denominator is exactly
\[
 t^2(m+i+r)(m-i+r-1)-(t+1)^2(m+i+1)(m-i)
 =(2t+1)\bigl(i(i+1)-rt(t+1)\bigr).
\]
As \(i\) increases, the last factor increases strictly. Hence \(\beta_i\) first decreases and then increases (one of these phases may be empty). Since \(\beta_0=1\) and \(\beta_1<1\), the sign of \(\beta_i-1\) can switch at most once, and only from negative to nonnegative. Furthermore,
\[
\alpha_{i+1}-\alpha_i=w_{m+i}-w_{m-i}=w_{m-i}(\beta_i-1)\quad (1\le i<m).
\]
It follows that \((\alpha_1,\ldots,\alpha_m)\) is U-shaped: first nonincreasing, then nondecreasing. This remains true if the increasing phase is absent.

**2. A strict mean-based balance identity.** For every nonnegative integer-valued law of *integer* mean \(m\), summation of discrete tail probabilities gives
\[
\sum_{i=1}^{m}\alpha_i=\mathbb E[(X-2m)_+].
\]
Indeed, the first part of the sum equals \(\mathbb E[(m-X)_+]\), the second equals \(\mathbb E[\min((X-m)_+,m)]\), and \(\mathbb E[(m-X)_+]=\mathbb E[(X-m)_+]\). Our law has positive mass at every nonnegative integer, so this sum is strictly positive. It remains to establish the nontrivial endpoint inequality
\[
\Pr(X\ge2rt)>\Pr(X=0)=(t+1)^{-r}. \tag{1}
\]
It then gives \(\alpha_m<0\). A U-shaped sequence with positive total sum and a negative final value has positive first value and can cross zero only from positive to negative: if the first term were nonpositive, every term would be nonpositive because every term of a U-shaped sequence is bounded above by the maximum of its two endpoints. This completes the sign argument once (1) is proved.

**3. A uniform endpoint proof.** For positive integers \(r,t\), introduce
\[
 R_{r,t}=\frac{\Pr(X=2rt)}{\Pr(X=0)}=\binom{(2t+1)r-1}{r-1}\left(\frac{t}{t+1}\right)^{2tr},
\quad
 A_{r,t}=(2t+1)R_{r,t}=\binom{(2t+1)r}{r}\left(\frac{t}{t+1}\right)^{2tr}.
\]
Vandermonde's identity, selecting one term in its nonnegative sum, yields
\[
 A_{r+s,t}\ge A_{r,t}A_{s,t}\qquad(r,s,t\ge1). \tag{2}
\]
Whenever \(R_{r,t}>1\), the single atom at \(2rt\) already proves (1).

For \(t=3,4,5\), direct exact arithmetic gives both \(A_{1,t}>1\) and \(R_{3,t}>1\). Inequality (2), starting at \(r=3\) and incrementing \(r\) by one, then proves \(R_{r,t}>1\) for all \(r\ge3\). For \(t=2\), exact arithmetic gives \(A_{2,2}=1280/729>1\) and \(R_{4,2}>1\), \(R_{5,2}>1\). Incrementing the shape by two covers all \(r\ge4\). The exception \((r,t)=(3,2)\) satisfies \(\Pr(X\ge2rt)/\Pr(X=0)=167936/59049>1\). For \(t=1\), exact arithmetic gives \(A_{3,1}=21/16>1\) and \(R_{6,1},R_{7,1},R_{8,1}>1\). Incrementing the shape by three covers \(r\ge6\). The three remaining cases have exact tail-to-zero ratios
\[
\frac{\Pr(X\ge2r)}{\Pr(X=0)}
 =\begin{cases}37/32,&r=3,\\29/16,&r=4,\\1471/512,&r=5.\end{cases}
\]
These are all strictly greater than one. No exhaustive enumeration over shapes is presumed: the base cases propagate to *every* integer shape through (2).

For \(t\ge6\), write \(X\) as a sum of \(r\) independent geometric counts with individual tail probability \(\Pr(G\ge k)=(t/(t+1))^k\). Then
\[
\Pr(X\ge2rt)\ge\Pr(G_1\ge2t,\ldots,G_r\ge2t)
=\left(\frac{t}{t+1}\right)^{2tr}.
\]
To compare this with \((t+1)^{-r}\), define for real \(u\ge6\)
\[
 h(u)=\log(u+1)+2u\log\frac{u}{u+1}.
\]
With \(z=1/(u+1)\), the elementary logarithmic series inequality
\(\log(1-z)\ge-z-z^2/[2(1-z)]\) gives
\[
 h'(u)=3z+2\log(1-z)\ge\frac{z(1-2z)}{1-z}>0.
\]
Also \(\exp(h(6))=6^{12}/7^{11}=2176782336/1977326743>1\). Therefore \(h(t)>0\) for all real \(t\ge6\), proving (1) in this last regime.

Combining the four regimes proves (1), the U-shape, and the asserted ordered sign crossing for all stated integer parameters. \(\square\)

## Verification

The accompanying self-contained Python script `verify_negative_binomial.py` runs with the standard library alone:

```sh
python3 verify_negative_binomial.py
```

It checks the exact rational endpoint base cases, 105 pairs with \(3\le r\le17\) and \(1\le t\le7\), 2,142 rational adjacent-quotient identities, and 343 finite instances of the combinatorial supermultiplicativity condition. A successful reference run prints `VERIFY_OK exact_tail_sign_cases=105 adjacent_quotients=2142 finite_vandermonde=343`. The infinite-range theorem is established by the algebraic identities, Vandermonde induction, and the analytic bound, not by the finite checks.

## Relationship to prior work

Fokkink, Papavassiliou and Pelekis introduce left-loadedness, prove the tail-comparison transfer theorem, and establish Poisson examples. The public arXiv line began on 2020-11-23, and the final journal paper dated 2022 discusses the integer-parameter negative-binomial analogue as numerical expectation rather than a proved \(L_1\) theorem. Their Lemma 3.3 addresses a *different* property (right-skewness around the mode), which does not imply the complete centered-tail sign pattern proved here. Perrin and Redside establish Simmons-type *center-tail* inequalities for several families; that one-index inequality does not logically determine the signs of all \(\alpha_i\).

As a direct application of the already-published transfer theorem, these negative-binomial laws may now serve as its left-loaded increment for any independent nonnegative-integer-valued right-skewed variable with mode at least \(rt\). The transfer theorem itself is not claimed as a new result.

## Limitations

The integer-reciprocal failure-probability and integer-shape hypotheses are used materially by the endpoint argument; no extension to arbitrary parameters is established. The zero-crossing index \(\ell\) is proved to exist but is not evaluated in closed form. The proof is self-contained modulo elementary Vandermonde summation and logarithmic-series bounds. A relevant older three-page article by Perrin and Redside was available in abstract form but not in full; possible alternative-formulation coverage is a bibliographic residual risk, not a claim of independently certified novelty.

## References

1. R. Fokkink, S. Papavassiliou and C. Pelekis, *Some inequalities on Binomial and Poisson probabilities*, arXiv:2011.11795, version 1 publicly submitted 2020-11-23; revised title *On the monotonicity of tail probabilities*, *Probability and Mathematical Statistics* 42 (2022), 133–141, DOI:10.37190/0208-4147.00050. Relevant published material: Definition 1.2, Lemma 3.3, Section 3 and the paragraph before Conjecture 4.1.
2. O. Perrin and E. Redside, *Generalization of Simmons' theorem*, *Statistics & Probability Letters* 77 (2007), 604–606, DOI:10.1016/j.spl.2006.09.006 (abstract consulted; full text not obtained).
