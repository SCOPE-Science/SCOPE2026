# A two-scale 2-adic valuation law for Stirling differences with fifteen blocks

## Finding

Let \(S(N,k)\) denote a Stirling number of the second kind, and let \(\nu_2\) be the usual \(2\)-adic valuation of a nonzero integer. For every integer \(n\ge10\) and every pair of integers \(a>b\ge1\), put
\[
\alpha=n+1+\nu_2(a-b),\qquad \beta=b2^n-5.
\]
Then
\[
\nu_2\big(S(a2^n,15)-S(b2^n,15)\big)
=\min(\alpha,\beta)\quad\text{whenever }\alpha\ne\beta.
\]
At the sole resonance \(\alpha=\beta\), the difference satisfies the rigorous lower bound
\[
\nu_2\big(S(a2^n,15)-S(b2^n,15)\big)\ge\alpha+1.
\]
In particular, for every fixed pair \(a>b\ge1\), the exact valuation is \(n+1+\nu_2(a-b)\) for all sufficiently large \(n\). The theorem makes no claim of an exact valuation on the resonance locus.

## Assumptions and scope

The parameters \(n,a,b\) are integers in the ranges just given. The Stirling number counts partitions into exactly fifteen nonempty unlabeled blocks. No primality or parity assumption is imposed on \(a\) or \(b\). The claimed first-public source date pertains to the motivating literature, not to publication of this finding.

## Proof

Write \(N=2^n\), \(c=a-b\), and use the inclusion--exclusion formula
\[
15!\,S(x,15)=\sum_{j=1}^{15}(-1)^{15-j}\binom{15}{j}j^x.
\]
Subtract its values at \(x=aN\) and \(x=bN\); denote its odd-index and even-index subsums by \(O\) and \(E\), respectively. As \(\nu_2(15!)=11\), the desired valuation is \(\nu_2(O+E)-11\).

**Odd-index contribution.** For odd \(j\) put \(d_j=j^N-1\), with \(d_1=0\). The elementary lifting-the-exponent identity gives \(\nu_2(d_j)\ge n+2\) for \(n\ge1\); indeed this is immediate for odd \(j>1\) from \(j^{2^n}\equiv1\pmod{2^{n+2}}\). Set
\[
M_n=\sum_{\substack{1\le j\le15\\j\ \mathrm{odd}}}\binom{15}{j}d_j.
\]
The finite modular certificate is
\[
M_{10}\equiv2^{22}\pmod{2^{23}}.
\]
It is reproduced by `verify.py` using just eight modular exponentiations. The identity \(d_{j,n+1}=2d_{j,n}+d_{j,n}^2\) yields
\[
M_{n+1}=2M_n+\sum_{j\ \mathrm{odd}}\binom{15}{j}d_{j,n}^2.
\]
Every correction summand is divisible by \(2^{2n+4}\); since \(2n+4\ge n+14\) for \(n\ge10\), induction on the certificate proves
\[
\nu_2(M_n)=n+12\qquad(n\ge10).
\]

Next, for any positive integer \(c\) and any \(d\in2^{n+2}\mathbb Z\), the binomial identity \(\binom ch=(c/h)\binom{c-1}{h-1}\) shows
\[
(1+d)^c-1=cd+R_c(d),\qquad
\nu_2(R_c(d))\ge\nu_2(c)+2n+3.
\]
For \(h\ge2\), this follows by comparing \(h(n+2)-\nu_2(h)\) with \(2n+3\). Multiplication by \((1+d)^b\) changes the leading \(cd\) by a term divisible by \(2^{\nu_2(c)+2n+4}\). Consequently
\[
(1+d)^b\big((1+d)^c-1\big)=cd+R_{b,c}(d),\qquad
\nu_2(R_{b,c}(d))\ge\nu_2(c)+2n+3.
\]
Summing with the odd binomial coefficients gives \(O=cM_n+R\). Its error has valuation at least \(\nu_2(c)+2n+3>\nu_2(c)+n+12\), because \(n\ge10\). Therefore
\[
\nu_2(O)=n+12+\nu_2(a-b).
\]

**Even-index contribution.** Since \(15-j\) is odd when \(j\) is even,
\[
E=\sum_{\substack{2\le j\le14\\j\ \mathrm{even}}}
\binom{15}{j}\big(j^{bN}-j^{aN}\big).
\]
For \(j\) divisible by four, \(j^{bN}\) vanishes modulo \(2^{bN+7}\), since \(bN\ge1024\). For the four remaining indices \(j=2,6,10,14\), factor out \(2^{bN}\). The higher-power contributions \(j^{aN}\) also vanish modulo \(2^{bN+7}\), because \(cN\ge1024\). Thus
\[
\frac{E}{2^{bN}}\equiv
105+5005\,3^{bN}+3003\,5^{bN}+15\,7^{bN}
\equiv105+5005+3003+15=8128=64\cdot127\pmod{128}.
\]
The second congruence uses \(3^{bN}\equiv5^{bN}\equiv7^{bN}\equiv1\pmod{128}\), which follows from \(n\ge10\). Hence
\[
\nu_2(E)=b2^n+6.
\]

**Combination.** The two contributions have valuations \(\alpha+11\) and \(\beta+11\). If these are unequal, the ultrametric valuation of the sum is the smaller. If they are equal, their quotient by their common power of two consists of two odd integers, whose sum is even. Dividing by \(15!\), whose \(2\)-adic valuation is eleven, proves both assertions. For fixed \(a,b\), \(\beta\) grows exponentially in \(n\) while \(\alpha\) grows linearly, proving the final consequence.

## Verification

`verify.py` checks the modular base certificate, the even-index coefficient sum, additional exact modular samples, and a genuine high-valuation resonance example. Run `python3 verify.py`; success prints `VERIFY_OK`. The computations are finite checks; the preceding induction and valuation argument prove the infinite statements.

## Relationship to prior work

Zhao, Zhao and Hong's 2014 work establishes the exact two-adic difference formula for non-Mersenne block counts; its main statements also settle the Mersenne counts three and seven, and provide a special adjacent-doubling result for all Mersenne counts. Their discussion explicitly leaves the general two-parameter problem with at least fifteen blocks open. The present result supplies a two-scale, nonadjacent two-parameter theorem at the first omitted Mersenne count. The earlier special adjacent-doubling formula is contained in the present theorem's \(\alpha<\beta\) region; it is not claimed as new. Davis's partial-Stirling analysis and Miska's local-analytic work are relevant broader contexts; their accessible statements do not explicitly give this two-scale formula.

## Limitations

The exponent range begins at \(n=10\), and an exact valuation is not established when \(\alpha=\beta\); only the stated strict improvement is proved there. The result addresses exactly fifteen blocks rather than all Mersenne block counts. No independent mathematical verification or comprehensive priority certification has been undertaken. General \(2\)-adic analytic principles might implicitly yield part of the result; published-source comparisons were based on the materials identified below.

## References

1. W. Zhao, J. Zhao and S. Hong, *The 2-adic valuations of differences of Stirling numbers of the second kind*, arXiv:1407.8443v1 (first posted July 31, 2014). https://arxiv.org/abs/1407.8443
2. J. Zhao, S. Hong and W. Zhao, *Divisibility by 2 of Stirling numbers of the second kind and their differences*, Journal of Number Theory (2014), DOI:10.1016/j.jnt.2014.01.005.
3. D. M. Davis, *2-adic partial Stirling functions and their zeros* (2014), preprint.
4. P. Miska, *A note on p-adic locally analytic functions with application to behavior of valuations of Stirling numbers*, arXiv:1803.04533 (2018).
