# The l-order likelihood-ratio conjecture holds for six exponential components
## Finding
Let \(X_i\) be independent exponential lifetimes with ordered positive hazard rates \(0<\lambda_1\le\cdots\le\lambda_6\), and let \(T(\lambda)=\max_i X_i\). A basic l-vector \(v=(v_1,\ldots,v_6)\) has \(v_1=1\), entries before a cutoff in \(\{0,1\}\), entries after it in \(\{0,-1\}\), and at least as many \(+1\)'s as \(-1\)'s. An l-vector is a nonnegative linear combination of basic l-vectors, and \(\lambda\succeq_l\mu\) means that \(\mu-\lambda\) is an l-vector.

For six components,
\[
\lambda\succeq_l\mu\quad\Longrightarrow\quad T(\lambda)\ge_{\mathrm{lr}}T(\mu).
\]
Hence the l-order conjecture of Wang and Cheng holds for \(n=6\), extending their theorem from \(n\le5\).

## Assumptions and scope
The component lifetimes are independent exponentials and both hazard vectors are positive and sorted in nondecreasing order. Likelihood-ratio order is the usual order induced by a monotone density ratio. The l-order is exactly the order introduced by Wang and Cheng. The result is only for six components; it does not settle the conjecture for arbitrary \(n\).

## Proof
Wang and Cheng reduce likelihood-ratio ordering to monotonicity, in every l-vector direction, of
\[
U(x_1,\ldots,x_n)=\frac{\sum_i b(x_i)d(x_i)}{\sum_i b(x_i)},\qquad
b(x)=\frac{x}{e^x-1},\qquad d(x)=\frac{xe^x}{e^x-1},
\]
for \(0<x_1\le\cdots\le x_n\). Their proof already handles every basic l-vector containing no \(-1\), for arbitrary dimension, and every sign pattern that remains after suppressing zeros with at most five nonzero coordinates. Therefore, at \(n=6\), only the three full-support patterns
\[
v_p=(\underbrace{1,\ldots,1}_{p},\underbrace{-1,\ldots,-1}_{6-p}),\qquad p\in\{3,4,5\},
\]
remain.

For a basic vector containing negative entries, their derivative formula writes the sign of \(\nabla_{v_p}U\) as the sign of a positive weighted sum of quantities \(R(j)\). Because \(-b'(x)\) is decreasing and \(p\ge6-p\), the coefficient making \(R(j)\) vary with \(d(x_j)\) has the required sign; since \(d\) is increasing, it is enough to prove \(R(1)\ge0\).

Fix \(x_1\) and define
\[
G(y)=b(y)d'(y)+b'(y)\bigl(d(y)-d(x_1)\bigr).
\]
Then
\[
R(1)=\sum_{i=1}^{p}G(x_i)-\sum_{i=p+1}^{6}G(x_i).
\]
The source's Lemma A.1 states that, as a function of \(y\), \(G(y)\) has a unique zero; it is positive and decreasing before that zero and negative afterwards.

If \(G(x_{p+1})>0\), every positive value in the last block is at most \(G(x_{p+1})\), while each of the first \(p\) values is at least \(G(x_{p+1})\). Negative values in the last block only increase \(R(1)\). Thus
\[
R(1)\ge \bigl(p-(6-p)\bigr)G(x_{p+1})\ge0.
\]

If \(G(x_{p+1})\le0\), then every value in the negative block is nonpositive, so it remains to prove \(\sum_{i=1}^{p}G(x_i)\ge0\). Choose \(y\in\{x_2,\ldots,x_p\}\) at which \(G\) is minimal. Then
\[
\sum_{i=1}^{p}G(x_i)\ge G(x_1)+(p-1)G(y).
\]
The source's Lemma A.2 defines
\[
P_{a,c}(x,y)=b(x)d'(x)+a b(y)d'(y)+c b'(y)\bigl(d(y)-d(x)\bigr)
\]
and proves \(P_{a,c}(x,y)\ge0\) for, among other pairs, \((a,c)=(2,2),(3,3),(4,4)\). Therefore, for \(p=3,4,5\),
\[
G(x_1)+(p-1)G(y)=P_{p-1,p-1}(x_1,y)\ge0.
\]
So \(R(1)\ge0\) for all three new full-support directions.

Every basic six-coordinate l-vector is now covered: zero-containing negative patterns reduce to the already proved at-most-five-nonzero cases, nonnegative patterns are covered by the source's dimension-free argument, and the three full-support negative patterns are covered above. Linearity gives nonnegative directional derivative for every l-vector. Since the line segment between two ordered hazard vectors remains ordered, integration along that segment gives monotonicity of \(U\), and the source's reversed-hazard-ratio reduction yields the stated likelihood-ratio order.

## Verification
The proof is analytic and its only nonstandard imported ingredients are the source's reduction to \(U\), Lemma A.1, and the three cases \((2,2),(3,3),(4,4)\) of Lemma A.2. Their statements and proofs were inspected in the full author-hosted article. A standalone numerical checker additionally verifies the identity used above, stress-tests the three Lemma A.2 inequalities on a deterministic grid, and stress-tests all three new full-support directional derivatives on 20,000 ordered six-tuples. It returns `VERIFY_OK`. These computations are supplementary; the infinite statement follows from the analytic argument.

## Relationship to prior work
Wang and Cheng introduced l-order, conjectured that it implies likelihood-ratio order for exponential parallel systems, and proved the conjecture for \(n\le5\). Their discussion explicitly leaves general \(n\) open and reports only simulations beyond five components. The present argument uses their own auxiliary lemmas to cover exactly the new full-support sign patterns appearing at six components. Earlier sufficient conditions such as d-larger or weak-majorization orders concern different hazard-vector orders and do not state the six-component l-order implication.

## Limitations
No claim is made for \(n\ge7\). The proof depends on the published auxiliary inequalities in Wang and Cheng; in particular, the six-component closure uses only the already proved parameter pairs through \((4,4)\). Literature and published-finding index searches found no statement of the \(n=6\) extension, but an unindexed or differently phrased equivalent result remains a residual originality risk.

## References
J. Wang and B. Cheng, “Likelihood ratio ordering for parallel systems with exponential components,” *Communications in Statistics—Theory and Methods* 51 (2022), 6741–6759. DOI: 10.1080/03610926.2020.1866205. Published online 2021-01-06.

J. Wang and P. Zhao, “On likelihood ratio ordering of parallel systems with exponential components,” *Mathematical Methods of Statistics* 25 (2016), 145–150. DOI: 10.3103/S1066530716020058.
