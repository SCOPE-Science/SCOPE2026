# Left-loadedness for the shape-two negative-binomial family
## Finding
For every integer \(n\ge2\), let \(X_n\) have probability mass function
\[
\Pr(X_n=k)=(k+1)\left(1-\frac1n\right)^k\frac1{n^2},\qquad k=0,1,2,\ldots.
\]
Its mean is \(m=2(n-1)\). For \(1\le i\le m\), define
\[
\alpha_i=\Pr(X_n\le m-i)-\Pr(X_n\ge m+i).
\]
Then \(X_n\) satisfies condition \(L_1\) of Fokkink, Papavassiliou and Pelekis and hence is left-loaded. For \(n=2\), both terms of the sequence are positive. For every \(n\ge3\), the sequence \(\alpha_1,\ldots,\alpha_m\) changes sign exactly once from positive to negative.

## Assumptions and scope
The parameterization is the one used in the motivating negative-binomial discussion: with \(p=1-1/n\) and \(q=1/n\), the shape-two law is \(\Pr(X_n=k)=(k+1)p^kq^2\). The claim covers every integer \(n\ge2\), not only a numerical range. It concerns left-loadedness through condition \(L_1\); it does not claim the stronger condition \(L_2\) or any result for shapes \(r\ge3\).

## Proof
Put \(p=(n-1)/n\), \(q=1/n\), \(m=2n-2\), and \(a_k=(k+1)p^kq^2\). Summing the differentiated geometric series gives, for every integer \(K\ge0\),
\[
T_K:=\Pr(X_n\ge K)=p^K\frac{K+n}n.
\]
In particular,
\[
\alpha_1=1-T_m-T_{m+1}
=1-p^{2n-2}\left(6-\frac6n+\frac1{n^2}\right).
\]
For \(n=2,3,4,5\), direct exact substitution gives respectively \(3/16\), \(137/729\), \(12319/65536\), and \(1835769/9765625\), all positive. For \(n\ge6\), write \(x=n-1\ge5\). The integer sequence \((1+1/x)^x\) is strictly increasing, because every fixed term in its binomial expansion is increasing in \(x\), with an additional positive final term after incrementing \(x\). Hence
\[
\left(1+\frac1x\right)^{2x}\ge\left(\frac65\right)^{10}>6>6-\frac6n+\frac1{n^2},
\]
which is equivalent to \(\alpha_1>0\).

At the other endpoint,
\[
\alpha_m=a_0-T_{2m}
=\frac1{n^2}-p^{4n-4}\frac{5n-4}n.
\]
For \(n=2\), this is \(1/16\). For \(n\ge3\), negativity is equivalent, with \(x=n-1\), to
\[
\left(1+\frac1x\right)^{4x}<(x+1)(5x+1).
\]
For \(x=2\) and \(x=3\), this is checked exactly by \((3/2)^8<33\) and \((4/3)^{12}<64\). For \(x\ge4\), the elementary inequality \((1+1/x)^x<e<3\) gives a left-hand side below \(81\), while the right-hand side is at least \(105\). Thus \(\alpha_m<0\) for every \(n\ge3\).

It remains to control the shape of the sequence. For \(1\le i\le m\), set
\[
\beta_i=\frac{a_{m+i}}{a_{m-i}}
=\frac{m+i+1}{m-i+1}p^{2i}.
\]
Then \(\beta_1=(n-1)/n<1\), and for \(i<m\),
\[
\frac{\beta_{i+1}}{\beta_i}
=p^2\frac{(m+i+2)(m-i+1)}{(m+i+1)(m-i)}.
\]
After clearing positive denominators, the numerator of the difference from one is
\[
(2n-1)\bigl(i(i+1)-2n(n-1)\bigr).
\]
This expression is strictly increasing in \(i\). Therefore \(\beta_i\) first decreases and then increases, with at most one crossing of the level \(1\) because \(\beta_1<1\). Consequently
\[
b_i:=a_{m-i}-a_{m+i}=a_{m-i}(1-\beta_i)
\]
is nonnegative and then possibly nonpositive, with at most one sign change.

Finally,
\[
\alpha_{i+1}=\alpha_i-b_i.
\]
Hence \(\alpha_i\) first decreases and then possibly increases. For \(n\ge3\), it starts positive and ends negative. On a possible increasing final segment every term is at most the negative endpoint \(\alpha_m\), so the sequence can cross zero only once, necessarily from positive to negative. For \(n=2\), the exact values are \(\alpha_1=3/16\) and \(\alpha_2=1/16\). This proves condition \(L_1\) in every case.

## Verification
Every quantified step is analytic. The tail formula follows from a convergent geometric-series identity; the endpoint inequalities are exact or reduced to elementary inequalities; and the single-crossing argument uses an explicit consecutive-ratio sign polynomial. No finite enumeration is used to infer an infinite statement.

## Relationship to prior work
The motivating paper defines left-loadedness and remarks that the negative-binomial family with parameter \(p=1-1/n\) appears to have the property, but it does not prove that statement. The present result settles the complete shape-two subfamily, which is the first non-geometric negative-binomial shape. Earlier negative-binomial extensions of Simmons-type inequalities concern near-mean tail comparisons and do not, from the inspected material, supply the full \(L_1\) sign sequence proved here.

## Limitations
The proof is specific to shape two. It does not establish left-loadedness for arbitrary negative-binomial shape, nor does it establish condition \(L_2\). An older equivalent formulation under different negative-binomial tail terminology remains a literature risk.

## References
1. Fokkink, Papavassiliou and Pelekis, “On the monotonicity of tail probabilities,” arXiv:2011.11795v1, first public version 2020-11-23; DOI:10.37190/0208-4147.00050.
2. “Generalization of Simmons' theorem,” Statistics & Probability Letters, DOI:10.1016/j.spl.2006.09.006. The inspected abstract indicates a negative-binomial Simmons-type extension; it is used only as a comparison source.
