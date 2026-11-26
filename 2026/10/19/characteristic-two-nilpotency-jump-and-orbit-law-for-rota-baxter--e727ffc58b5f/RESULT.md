# A sharp nilpotency probability for Rota–Baxter operators on square-zero local algebras

## Finding

Fix a finite field \(\mathbb F_q\) of characteristic two. Let \(V=\mathbb F_q^n\), and give \(A=\mathbb F_q1\oplus V\) its unital algebra structure with \(V^2=0\). Choose a weight-zero Rota–Baxter operator \(P:A\to A\) uniformly among all \(\mathbb F_q\)-linear operators satisfying the identity. Write \(n=2m+\epsilon\), with \(\epsilon\in\{0,1\}\), and put
\[
c_k(q)=\prod_{i=1}^k(1-q^{-i}),\qquad
W_{\epsilon,j}(q)=\frac{q^{-2j(j+\epsilon)}}{c_{2j+\epsilon}(q)}.
\]
Then, for each fixed parity \(\epsilon\),
\[
\Pr(P^2=0)=q^{-m}\bigl(C_{q,\epsilon}+o(1)\bigr),\qquad
C_{q,\epsilon}=\frac{\sum_{j\ge0}q^jW_{\epsilon,j}(q)}{\sum_{j\ge0}W_{\epsilon,j}(q)}.
\]
Both sums converge absolutely and the constant is positive. For \(q=2\) the constants are approximately \(1.41971069618\) for even \(n\) and \(1.08804625772\) for odd \(n\). Since \(P^3=0\), this is the sharp equivalent for the proportion of operators whose nilpotency index is less than three.

## Assumptions and scope

The weight-zero convention is \(P(x)P(y)=P(P(x)y+xP(y))\). The sample space counts individual maps, not conjugacy classes. The limit holds for fixed \(q\) as the radical dimension \(n\) increases; it does not assert an estimate uniform in \(q\). The structural description and finite counts below are established inputs, not separate originality claims.

## Proof

For completeness, the scalar part of \(P(v)\) for \(v\in V\) vanishes by applying the Rota–Baxter identity at \((v,v)\); its square equals zero because \(2=0\). The same comparison at \((1,1)\) gives \(P(1)\in V\). Thus \(P(a1+v)=au+T(v)\), with \(u\in V\) and \(T:V\to V\). The identity at \((1,v)\) now gives \(T^2(v)=0\). Conversely, those conditions suffice: the product of two images is zero, and the image under \(P\) of the argument on the right is \(T^2(aw+bv)\) for \(x=a1+v, y=b1+w\), the two \(ab u\) terms cancelling. As \(P^2(a1+v)=aT(u)\), the event in question is \(u\in\ker T\), and \(P^3=0\).

For rank \(r\le\lfloor n/2\rfloor\), the square-zero \(T\)'s are counted by choosing the flag \(\operatorname{im}T\subseteq\ker T\) and the quotient isomorphism \(V/\ker T\to\operatorname{im}T\). Hence their number is
\[
B_{n,r}(q)={n\brack r}_q{n-r\brack r}_q|\mathrm{GL}_r(q)|
=q^{2r(n-r)}\frac{c_n(q)}{c_r(q)c_{n-2r}(q)}.
\]
The second equality follows by expanding the Gaussian coefficients and \(|\mathrm{GL}_r(q)|=q^{r^2}c_r(q)\). Conditional on any \(T\), the vector \(u\) is uniform on \(V\), and the chance that \(T(u)=0\) is \(q^{-r}\). Thus
\[
\Pr(P^2=0)=\frac{\sum_r B_{n,r}(q)q^{-r}}{\sum_r B_{n,r}(q)}.
\]

Set \(r=m-j\). The rank weight normalized by \(q^{2m(m+\epsilon)}\) is
\[
b_{m,j}=q^{-2j(j+\epsilon)}\frac{c_{2m+\epsilon}(q)}{c_{m-j}(q)c_{2j+\epsilon}(q)}\quad(0\le j\le m),
\]
and set \(b_{m,j}=0\) for \(j>m\). For each fixed \(j\), the ratio \(c_{2m+\epsilon}/c_{m-j}\) tends to 1 because both terms converge to the same positive infinite product \(c_\infty\). That ratio is at most 1, and \(c_{2j+\epsilon}\ge c_\infty\), so \(b_{m,j}\) and \(q^jb_{m,j}\) are dominated respectively by \(q^{-2j(j+\epsilon)}/c_\infty\) and \(q^{j-2j(j+\epsilon)}/c_\infty\). Both bounds are summable. Since \(q^{-r}=q^{-m}q^j\), dominated convergence in the numerator and denominator of the scaled probability gives the asserted constant; the limiting denominator has a positive \(j=0\) term.

## Verification and limitations

The proof establishes the limit. To reproduce the displayed constants, set \(c_0=1\), obtain \(c_k\) by multiplying successively by \(1-q^{-k}\), and sum the indicated numerator and denominator through \(j=40\). For \(q=2\), \(c_\infty>1/4\) (split off the first two factors and bound the remaining product below by one minus the sum of the omitted fractions). The tails for either parity are bounded by \(4\sum_{j\ge41}2^{j-2j^2}\). The retained supporting script also compares the scaled finite-dimensional probabilities with the series for \(q=2,4\) at \(n=80,81\); such checks do not replace the proof.

## Relationship to prior work

The characteristic-two operator description, rank enumeration and nilpotency-index split are already given in [*Characteristic-two index-three Rota–Baxter operators on split square-zero local algebras*](https://github.com/Resultary/2026/tree/main/2026/10/12/SCOPE-characteristic-two-index-three-rota-baxter-operators-on-split-sq--daddf5c855da), including a marked-vector orbit classification not needed here. Farooq's [arXiv:2605.15670v1](https://arxiv.org/abs/2605.15670v1), Theorem 3.4, treats the same square-zero algebra in characteristic zero, where all the operators square to zero. The contribution here is the parity-resolved equivalent for the exceptional event in characteristic two, not the existence or exact finite number of index-three operators. An equivalent asymptotic also appears in [*Characteristic-two Rota–Baxter index jump and sharp finite-field asymptotics*](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-characteristic-two-rota-baxter-index-jump-and-sharp-finite-field--53e204e73dd6), §3; the catalog comparison does not settle historical priority. Equivalent earlier work under the language of finite-field square-zero rank distributions may exist.
