# Two-state sphere spectrum for three-symbol permutation bursts

## Finding

Let \(q\ge 2\), \(n\ge 3\), and let \(\Sigma\) be a fixed alphabet of cardinality \(q\). A length-three permutation burst replaces **one** non-wrapping consecutive block of three symbols by any permutation of that block; the unchanged word is included. Write \(\mathcal B_3(x)\) for the set of **distinct** length-\(n\) outputs and \(B(x)=|\mathcal B_3(x)|\). Define the exact population polynomial
\[
P_{q,n}(t)=\sum_{x\in\Sigma^n}t^{B(x)}.
\]
Put
\[
M_q(t)=\begin{pmatrix}1&(q-1)t\\ t^2&t+(q-2)t^4\end{pmatrix},\quad
v_q=(q,q(q-1)),\quad w(t)=\binom{1}{t}.
\]
Then, for all such \(q,n\),
\[
\boxed{P_{q,n}(t)=t\,v_q M_q(t)^{n-2}w(t).}
\]
In particular, the **entire** population of each integer sphere size is the corresponding coefficient. Its length generating function is the rational matrix expression
\[
\sum_{n\ge3}P_{q,n}(t)z^{n-3}
=t\,v_q M_q(t)(I-zM_q(t))^{-1}w(t).
\]
For a uniformly chosen center \(X\in\Sigma^n\), the exact mean and variance are
\[
\mathbb E B(X)=1+\frac{q-1}{q}+\frac{4(q-1)^2(n-2)}{q^2},
\]
\[
\boxed{\operatorname{Var}(B(X))
=\frac{(q-1)\bigl[n(34q^2-88q+48)-75q^2+208q-128\bigr]}{q^4}.}
\]
Let \(\mu_q=4(q-1)^2/q^2\) and \(\sigma_q^2=2(q-1)(17q^2-44q+24)/q^4>0\). For fixed \(q\),
\[
\frac{B(X)-\mathbb EB(X)}{\sqrt{n\sigma_q^2}}
\Longrightarrow N(0,1)\qquad(n\to\infty).
\]
The minimum is always \(1\), attained precisely by the \(q\) constant words. For \(q\ge3\), the maximum is \(4n-6\), attained by exactly \(q(q-1)(q-2)^{n-2}\) centers. For \(q=2\), the maximum is \(\lfloor(3n-2)/2\rfloor\); precisely two centers attain it for even \(n\), and precisely \(n+3\) centers for odd \(n\).

## Assumptions and scope

The alphabet is an abstract labeled finite set, not necessarily a field. The burst window has **exactly** three positions, with no wraparound, and at most one such burst is allowed; all six permutations may be used, including the identity. The centers are uniformly distributed only for the stated moment and limit laws. The length restriction \(n\ge3\) is essential: a length-two word has no permitted three-position window.

## Proof

**Distinct-output decomposition.** Every output different from its center, obtained by permuting one block of three positions, changes exactly two or three symbol positions. If exactly two positions change, their symbols are distinct and those positions are at distance one or two; swapping a given unequal pair uniquely specifies the output. Every such pair occurs together in some length-three window because \(n\ge3\). If three positions change, they must be consecutive and contain three pairwise distinct symbols; precisely two nonidentity three-cycles change all three. Outputs arising from different changed-position sets cannot coincide. Consequently,
\[
B(x)=1+\sum_{i=1}^{n-1}\mathbf1_{\{x_i\ne x_{i+1}\}}
+\sum_{i=1}^{n-2}\mathbf1_{\{x_i\ne x_{i+2}\}}
+2\sum_{i=1}^{n-2}\mathbf1_{\{|\{x_i,x_{i+1},x_{i+2}\}|=3\}}.\tag{1}
\]
This argument also handles repeated symbols and boundary windows without multiplicity overcounting.

**Two-state enumeration.** Let \(Z(a,b,c)=\mathbf1_{a\ne b}+\mathbf1_{a\ne c}+2\mathbf1_{|\{a,b,c\}|=3}\). The right side of (1) is \(1+\sum_{i=1}^{n-2}Z(x_i,x_{i+1},x_{i+2})+\mathbf1_{x_{n-1}\ne x_n}\). Track only whether the last two symbols agree (state E) or disagree (state D). From E, the next symbol either agrees (one choice, weight \(1\), new E) or differs (\(q-1\) choices, weight \(t\), new D). From D, a new symbol equal to the previous-but-one symbol gives weight \(t\) and D; equal to the immediately preceding symbol gives weight \(t^2\) and E; and distinct from both gives \(q-2\) choices of weight \(t^4\) and D. This gives \(M_q(t)\). There are \(q\) initial equal pairs and \(q(q-1)\) unequal pairs; the final adjacent-inequality term gives \(w(t)\), and the unchanged output gives the external factor \(t\). This proves the exact polynomial and rational length series.

**Moments.** For independent uniformly distributed symbols, write \(Z_i=Z(X_i,X_{i+1},X_{i+2})\) and \(H=\mathbf1_{X_{n-1}\ne X_n}\). Directly conditioning on the equality of two shared symbols gives
\[
\begin{aligned}
\mathbb EZ_i&=\frac{4(q-1)^2}{q^2},\\
\operatorname{Var}(Z_i)&=\frac{2(q-1)(11q^2-24q+8)}{q^4},\\
\operatorname{Cov}(Z_i,Z_{i+1})&=\frac{2(q-1)(q-2)(3q-4)}{q^4},\\
\operatorname{Cov}(Z_i,Z_{i+2})&=0,\\
\operatorname{Cov}(Z_{n-2},H)&=\frac{2(q-1)(q-2)}{q^3},\\
\operatorname{Var}(H)&=\frac{q-1}{q^2}.
\end{aligned}\tag{2}
\]
To check the nontrivial adjacent covariance, condition on the shared pair \((b,c)\). The respective conditional means of \(Z(a,b,c)\) and \(Z(b,c,d)\) are \((2(q-1)/q,(q-1)/q)\) when \(b=c\), and \(((4q-6)/q,(4q-5)/q)\) when \(b\ne c\); conditionally the two scores are independent. The probabilities of these two cases are \(1/q\) and \((q-1)/q\). The other entries in (2) follow by the same three-symbol enumeration. At distance two only one symbol is shared, whose value does not change either conditional mean by relabeling symmetry, so the covariance vanishes. Covariance of \(H\) with earlier \(Z_i\) also vanishes, including the one-symbol-overlap case. Summing (2) yields, for \(n\ge3\),
\[
\operatorname{Var}(B)= (n-2)\operatorname{Var}(Z_1)
+2(n-3)\operatorname{Cov}(Z_1,Z_2)
+\operatorname{Var}(H)+2\operatorname{Cov}(Z_{n-2},H),
\]
which simplifies to the displayed exact variance. Linearity gives the mean.

**Gaussian law.** The bounded stationary sequence \((Z_i)\) is two-dependent. Its asymptotic variance per term is \(\operatorname{Var}(Z_1)+2\operatorname{Cov}(Z_1,Z_2)=\sigma_q^2\), positive for every integer \(q\ge2\). The central limit theorem for bounded stationary finite-dependent variables applies. The bounded end correction \(1+H\) is negligible after division by \(\sqrt n\).

**Sharp extrema.** Formula (1) gives \(B\le1+(n-1)+(n-2)+2(n-2)=4n-6\). For \(q\ge3\), equality is equivalent to every three consecutive letters being pairwise distinct. The first two letters have \(q(q-1)\) choices, and each later letter has \(q-2\) choices. For \(q=2\), let \(P_n=P_{2,n}\) and use the transfer matrix's characteristic polynomial to obtain
\[
P_{n+2}=(1+t)P_{n+1}+(t^3-t)P_n,
\]
where the auxiliary algebraic seed \(P_2=2t+2t^2\) is **not** interpreted as a physical length-two burst sphere and the first physical polynomial is \(P_3=2t+6t^3\). Induction on this recurrence shows that for even \(n=2m\), the degree is \(3m-1\) with leading coefficient \(2\), and for odd \(n=2m+1\), the degree is \(3m\) with leading coefficient \(2m+4=n+3\). In the even step only the \(t^3P_n\) term reaches the new highest degree; in the odd step both \(tP_{n+1}\) and \(t^3P_n\) reach it. The minimum is \(1\) exactly when all adjacent pairs agree, hence precisely for constant centers.

## Verification

`verify.py` directly generates all six permutations of each permitted window, deduplicates actual received words, independently computes the local statistic (1), and evaluates the two-state transfer recurrence. It checks every input for 33 combinations \((q,n)\): \(q=2,3,4,5,6\) up to lengths \(12,10,8,7,6\), respectively, starting at length three. This covers exactly 337,673 distinct input words. For every combination it checks the entire distribution, exact rational mean and variance, minimum count, sharp maximum and maximizer count. The complete run ends with `VERIFY_OK`. The infinite result uses the above proof, not finite extrapolation.

## Relationship to prior work

Chen and Milenkovic, *Correcting Burst Errors with Applications to DNA-Based Data Storage*, arXiv:2610.15701v1 (submitted 2026-10-11), define this non-wrapping permutation channel and supply an exact **binary pointwise** sphere-size decomposition for general burst lengths (Section II, equations (7)–(13)). Their Section V, Proposition 3 and Tables I–III classify binary length-three error patterns to build a correcting code. These established facts are not claimed as new. The present contribution is the **evaluated finite-alphabet population law** for all \(q\), with a two-state transfer matrix that accounts for three distinct changed positions, exact variance, limit law, and complete extremal population counts. The source deliberately restricts its treatment to binary alphabets; nonbinary three-cycle outputs cannot be represented by its binary two-position patterns.

Earlier related results on binary length-four substring-permutation sphere populations concern a different window length and do not imply the above ternary-and-larger population law. The classical finite-dependent-variable central limit theorem of Hoeffding and Robbins is used as a standard probabilistic tool, not claimed as new. Searches and comparison do not establish global uniqueness of the result; equivalent coverage outside indexed material remains possible.

## Limitations

Only one exact-three-position burst, non-wrapping windows, and uniformly random centers are covered. No result is claimed for multiple bursts, variable window size, or nonuniform source distributions. The result evaluates sphere sizes, not optimal code cardinalities, decoding algorithms, or experimental nanopore performance. The transferred binary pointwise formula and the general finite-dependent central limit theorem remain prior knowledge. Independent external validation has not been performed.

## References

1. Y.-P. Chen and O. Milenkovic, *Correcting Burst Errors with Applications to DNA-Based Data Storage*, arXiv:2610.15701v1, submitted 2026-10-11. https://arxiv.org/html/2610.15701v1
2. W. Hoeffding and H. Robbins, *The central limit theorem for dependent random variables*, Duke Mathematical Journal **15** (1948), 773–780. https://doi.org/10.1215/S0012-7094-48-01568-3
