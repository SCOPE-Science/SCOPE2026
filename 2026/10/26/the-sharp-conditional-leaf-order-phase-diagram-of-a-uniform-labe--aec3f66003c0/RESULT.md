# The sharp conditional leaf-order phase diagram of a uniform labeled tree

## Finding
Let \(T_n\) be a uniformly random labeled tree on \([n]\), with \(n\ge5\). Write \(D\) for the degree of vertex \(1\), and \(L\) for the total number of vertices of degree one (leaves). For \(1\le d\le n-1\), write \(L_d\) for a random variable with the conditional law of \(L\) given \(D=d\). Let \(X_t\) be the number of empty boxes after \(t\) independent uniform placements in \(n-1\) labeled boxes.

**Complete conditional stochastic-order classification.** The laws admit the exact representation
\[
L_d\ \overset{\mathrm d}=\ \mathbf1_{\{d=1\}}+X_{n-d-1}.
\]
Consequently, in strict first-order stochastic order,
\[
L_2<_{\mathrm{st}} L_1<_{\mathrm{st}} L_{n-1},\qquad
L_2<_{\mathrm{st}}L_3<_{\mathrm{st}}\cdots<_{\mathrm{st}}L_{n-1}.
\]
Here strict stochastic order means all upper-tail inequalities hold with at least one strict inequality. For **every** \(3\le d\le n-2\), the distributions \(L_1\) and \(L_d\) are *incomparable* in first-order stochastic order. These statements specify every pair of attainable degree values: there are no further comparisons between \(L_1\) and the interior degree classes.

Although the degree-one and degree-three conditional laws are incomparable for every \(n\ge5\), their **means cross at the sharp tree order nine**:
\[
\mathbb E[L_3]>\mathbb E[L_1]\quad(5\le n\le8),
\qquad
\mathbb E[L_3]<\mathbb E[L_1]\quad(n\ge9).
\]
For every \(4\le d\le n-1\), \(\mathbb E[L_d]>\mathbb E[L_1]\) for every permissible \(n\ge5\). Thus expectation comparisons can reverse with tree size even though stochastic incomparability persists at all interior degrees.

## Assumptions and scope
The underlying distribution is uniform on the \(n^{n-2}\) labeled Cayley trees and not the uniform recursive-tree law or the uniform unlabeled-tree law. The distinguished vertex is vertex \(1\); by exchangeability the same statements hold for any fixed distinguished vertex. Each degree class \(1\le d\le n-1\) has positive probability. A leaf is a vertex of ordinary unrooted degree one, including the distinguished vertex when \(D=1\).

For a family \(Y_1,Y_2\), write \(Y_1\le_{\mathrm{st}}Y_2\) when \(\Pr(Y_1\ge t)\le\Pr(Y_2\ge t)\) for all real \(t\). Incomparability means neither ordering holds. This statement does not concern every increasing functional of the entire tree, only its leaf count.

## Proof
**1. Exact conditional occupancy law.** By the Prüfer bijection, a uniform labeled tree corresponds bijectively to a sequence of \(n-2\) independent uniform labels in \([n]\). The degree of any vertex equals one plus the number of occurrences of its label, and a vertex is a leaf precisely when its label is absent. Conditioning on \(D=d\) forces precisely \(d-1\) occurrences of label \(1\), and the remaining \(n-d-1\) sequence positions are independent uniform draws in the other \(n-1\) labels. Hence \(L_d\overset{\mathrm d}=\mathbf1_{\{d=1\}}+X_{n-d-1}\), proving the asserted law and, in particular,
\[
\mathbb E[L_d]=\mathbf1_{\{d=1\}}+(n-1)\biggl(1-\frac1{n-1}\biggr)^{n-d-1}.
\]

**2. All stochastic comparisons.** Couple every \(X_t\) by using prefixes of one infinite independent sequence of draws. Then \(X_{t+1}\le X_t\) pathwise. For \(d\ge2\), this gives \(L_2<_{\mathrm{st}} L_3<_{\mathrm{st}}\cdots<_{\mathrm{st}}L_{n-1}\), each strict because removing one draw has positive probability of emptying a box, except that the final case remains strict since \(X_0=n-1\) and \(X_1=n-2\).

For the comparison \(d=1,2\), use the same first \(n-3\) draws in both laws, and one additional draw only for \(L_1\): deleting that additional draw increases the number of empty boxes by zero or one, so \(L_1\ge L_2\) pathwise. The inequality is strict with positive probability for \(n\ge5\), since the additional draw need not be the sole occurrence of its label. At \(d=n-1\), no other labels occur and \(L_{n-1}=n-1\) deterministically, which strictly dominates \(L_1\).

For \(3\le d\le n-2\), \(L_d\ge d\ge3\) always, whereas \(\Pr(L_1=2)>0\), realized when its \(n-2\) draws are all distinct. Thus \(L_1\not\ge_{\mathrm{st}}L_d\). Conversely \(L_d\le n-2\) always, because at least one other label must occur, while \(\Pr(L_1=n-1)>0\), realized when all its draws repeat a single other label. Thus \(L_d\not\ge_{\mathrm{st}}L_1\). This proves the complete phase diagram.

**3. Sharp degree-three mean reversal.** Set \(q=n-1\ge4\) and \(u_q=1-1/q\). The exact difference satisfies
\[
\mathbb E[L_3]-\mathbb E[L_1]
=(2-1/q)u_q^{q-3}-1=:f(q)-1.
\]
Treating \(q\) as a real variable \(q\ge4\), differentiate \(\log f(q)\):
\[
\frac{d}{dq}\log f(q)=\frac1{q(2q-1)}+\log(1-1/q)+\frac{q-3}{q(q-1)}.
\]
The elementary bound \(\log(1-z)\le-z-z^2/2\) for \(0<z<1\) gives
\[
\frac{d}{dq}\log f(q)
\le-\frac{8q^2-5q+1}{2q^2(q-1)(2q-1)}<0.
\]
Direct exact arithmetic gives \(f(7)>1\) and \(f(8)<1\); hence the sign changes exactly between \(n=8\) and \(n=9\), with no equality at an integer order.

**4. Higher-degree mean comparisons.** It is enough to show \(\mathbb E[L_4]>\mathbb E[L_1]\), since the expectation strictly increases through the degree classes \(d\ge2\). For \(q=n-1\ge4\),
\[
\mathbb E[L_4]-\mathbb E[L_1]
=\bigl(3-3/q+1/q^2\bigr)(1-1/q)^{q-4}-1.
\]
For \(q\ge11\), \(\log(1-1/q)\ge-1/(q-1)\) gives \((1-1/q)^{q-4}>e^{-1}\), while \(3-3/q+1/q^2>e\) for \(q\ge11\), making the difference positive. For the finite cases \(4\le q\le10\), substituting the rational values directly shows strict positivity (the accompanying verifier checks these cases exactly). This completes the proof.

## Verification
The enclosed `verification.py` requires only Python's standard library and independently enumerates all Prüfer words for \(n=5,6,7\). It compares the observed conditional leaf-count distributions with the exact occupancy formula, checks all stochastic relations and incomparabilities, and verifies the strict mean inequalities using rational arithmetic through \(n=40\). It separately verifies the exact mean switch at \(n=8,9\). Run `python verification.py` next to this document. Such finite computations support the exact calculations; the all-size assertions rely on the analytic proof.

## Relationship to prior work
The underlying Prüfer bijection and marginal tree-degree laws are classical. Seo and Shin (2005) give a reverse Prüfer encoding and degree/leader generating function, not a conditional comparison of total leaves across degrees. Drmota and Gittenberger (1999) investigate counts of vertices of fixed degrees in several tree models, primarily asymptotically. Addario-Berry, Donderwinkel, Maazoun, and Martin (2021) give a probabilistic tree coding and stochastic-order comparisons for distances under constrained degree sequences, a different statistic and conditioning scheme. The exact occupancy representation is elementary and is not claimed as new; the asserted contribution is the **complete conditional leaf stochastic-order/incomparability diagram and its sharp degree-three mean reversal at order nine**. Equivalent earlier statements could exist in occupancy or enumerative-tree literature, and historical priority is not independently certified.

## Limitations
This is a finite-size distributional classification only for uniform labeled Cayley trees, with a single distinguished vertex. It is not a stochastic order of full trees. The verification is finite, not an infinite proof. The novelty assessment compares specific accessible primary material and published-record searches; absence from them does not prove global uniqueness.

## References
1. S. Seo and H. Shin, *A Generalized Enumeration of Labeled Trees and Reverse Prüfer Algorithm*, arXiv:math/0601009, first posted 2005-12-31, https://arxiv.org/abs/math/0601009.
2. M. Drmota and B. Gittenberger, *The distribution of nodes of given degree in random trees*, Journal of Graph Theory 31 (1999), 227–253, https://doi.org/10.1002/(SICI)1097-0118(199907)31:3<227::AID-JGT6>3.0.CO;2-6.
3. L. Addario-Berry, S. Donderwinkel, M. Maazoun, J. Martin, *The Foata–Fuchs proof of Cayley's formula, and its probabilistic uses*, arXiv:2107.09726, first posted 2021-07-20, https://arxiv.org/abs/2107.09726.
