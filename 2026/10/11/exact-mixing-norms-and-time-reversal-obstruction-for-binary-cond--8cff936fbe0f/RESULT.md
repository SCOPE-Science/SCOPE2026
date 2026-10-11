# Exact mixing norms and time-reversal obstruction for binary conditional-expectation chains

## Finding

Let \((\Omega,\mathcal F,\mu)\) be a probability space, \(1<p<\infty\), \(q=p/(p-1)\), and \(m\ge2\). For measurable events \(A_1,\ldots,A_m\) of strictly intermediate probability put
\[
a_i=\mu(A_i),\quad \alpha_i=a_i(1-a_i),\quad u_i=\mathbf 1_{A_i}-a_i,
\quad d_i=\mu(A_i\cap A_{i+1})-a_i a_{i+1}\ (1\le i<m).
\]
Write \(P_i f=\mathbf E(f\mid\sigma(A_i))\), \(Ef=\int f\,d\mu\) (viewed as a constant function), and \(W=P_m\cdots P_1\), acting on real \(L^p(\mu)\). For \(s>1\) define
\[
h_s(a)=\left(a(1-a)^s+(1-a)a^s\right)^{1/s},\qquad
c=\frac{\prod_{i=1}^{m-1}d_i}{\prod_{i=1}^m\alpha_i},\qquad
\vartheta=c\big(\mu(A_m\cap A_1)-a_ma_1\big).
\]
Then the *entire centered operator and every periodic error norm* are given exactly by
\[
(W-E)f=c\,u_m\int u_1f\,d\mu,\qquad
\boxed{\ \|W^k-E\|_{L^p\to L^p}
=|\vartheta|^{k-1}|c|\,h_p(a_m)h_q(a_1)\quad(k\ge1).\ }
\]
Here the zeroth power in the case \(k=1\) is defined as one, even when \(\vartheta=0\). In particular, \(W=E\) if and only if some adjacent covariance \(d_i\) vanishes. When \(c\ne0\) but the endpoint covariance vanishes, \(W\ne E\) yet \(W^2=E\).

For the reversed word \(W^{\mathrm{rev}}=P_1\cdots P_m\), if \(c\ne0\) its centered norm ratio is
\[
\boxed{\ \frac{\|W-E\|_p}{\|W^{\mathrm{rev}}-E\|_p}
=\frac{h_p(a_m)h_q(a_1)}{h_p(a_1)h_q(a_m)}.\ }
\]
The same ratio holds for \(k\)-th powers whenever \(\vartheta\ne0\). For every sequence of such events the ratio equals one when \(p=2\). Conversely, for every fixed \(p\ne2\), **no finite constant depending only on \(p\)** compares the two oriented centered norms for *all ordered pairs* of binary conditional expectations; this already occurs on three-atom probability spaces. The same failure holds for every fixed positive iterate of these two-product words.

## Assumptions and scope

All assertions apply to arbitrary probability spaces, without finiteness or non-atomicity assumptions, real-valued \(L^p\), every integer \(m\ge2\), and every exponent \(1<p<\infty\). The displayed formula measures \(W^k-E\), not \(W^k\), and makes no assertion that the common fixed-point projection is always \(E\). If \(|\vartheta|<1\), the formula yields sharp operator-norm convergence to \(E\); if \(\vartheta=0\), the second iterate equals \(E\). The case of identical or complementary event sigma-algebras may have \(|\vartheta|=1\).

## Proof

For \(0<a_i<1\), conditioning on an event and its complement gives the exact rank-one decomposition
\[
P_i=E+\frac{1}{\alpha_i}\,u_i\otimes\ell_i,
\qquad \ell_i(f)=\int u_if\,d\mu.
\]
The cross-products with \(E\) vanish because \(Eu_i=0\) and \(\ell_i(1)=0\); composing adjacent rank-one terms introduces \(\ell_{i+1}(u_i)=d_i\). Induction therefore gives \(W-E=c\,u_m\otimes\ell_1\), including the case when a covariance vanishes.

The dual norm of \(\ell_1\) on real \(L^p\) is \(\|u_1\|_q=h_q(a_1)\), and \(\|u_m\|_p=h_p(a_m)\). Hölder's equality is achieved by a scalar multiple of \(\operatorname{sgn}(u_1)|u_1|^{q-1}\), so the norm is exactly \(|c|h_p(a_m)h_q(a_1)\), not merely bounded by it. Since \(E(W-E)=(W-E)E=0\) and \((W-E)^2=\vartheta(W-E)\), expanding \(W^k\) gives the asserted iterate formula.

Reversing the word changes neither \(\prod_i d_i\) nor \(\prod_i\alpha_i\); it exchanges the endpoint vectors in the rank-one representation. This proves the ratio. At \(p=2\), \(h_2(a)=\sqrt{a(1-a)}\), so the endpoint ratio is one.

For sharp failure when \(p\ne2\), on three atoms assign probabilities \(\varepsilon,1/2-\varepsilon,1/2\) with \(0<\varepsilon<1/2\). Let \(A\) be the first atom and \(B\) the first two. Then \(\mu(A)=\varepsilon\), \(\mu(B)=1/2\), and \(\operatorname{Cov}(\mathbf1_A,\mathbf1_B)=\varepsilon/2\ne0\). For \(W=P_A P_B\), the ratio against \(P_B P_A\) is \(h_p(\varepsilon)/h_q(\varepsilon)\), since \(h_s(1/2)=1/2\) for every \(s>1\). As \(\varepsilon\downarrow0\), \(h_s(\varepsilon)\sim\varepsilon^{1/s}\), hence the ratio is asymptotic to \(\varepsilon^{2/p-1}\). It diverges for \(p>2\); for \(p<2\), reverse the order. Both words have the same nonzero eigenvalue \(\varepsilon/(1-\varepsilon)\) away from constants, so their iterated centered-norm ratio remains unchanged for every \(k\ge1\). No uniform comparison is possible at a non-Hilbert exponent.

Finally, on four equiprobable atoms \((X,Y)\in\{0,1\}^2\), take \(A_1=\{X=1\}\), \(A_2=\{X=1\text{ or }Y=1\}\), and \(A_3=\{Y=1\}\). Both adjacent covariances equal \(1/8\), while the two endpoints are independent. Thus \(c=4/3\ne0\) and \(\vartheta=0\). The three-factor word differs from \(E\), but its square is exactly \(E\).

## Verification

The accompanying `verify_binary_products.py` uses only the Python standard library. On a four-atom rational probability space it exhaustively checks the matrix identity and its square for all \(14^3=2744\) ordered triples of nontrivial events, using exact rational arithmetic. It checks equality in the norm formula against a Hölder-extremizing vector at two non-Hilbert exponents, then verifies the three-atom orientation examples and an exact nilpotent four-atom instance. Run `python verify_binary_products.py` and expect `BINARY_EXPECTATION_EXACT_IDENTITIES_OK 2744`. These finite tests check implementation and boundary examples only; the argument above proves the result for arbitrary probability spaces and all indicated exponents and word lengths.

## Relationship to prior work

Zaharopol (1990) proves strong \(L^p\)-convergence of arbitrary finite products of conditional expectations to the expectation onto the intersection of the sigma-algebras. The present theorem works in the two-cell filtration subclass, but supplies *exact operator norms of all iterates* and the unbounded reversal obstruction; the qualitative convergence theorem does not give these conclusions. Akcoglu--Sucheston (1987) is a historical predecessor on alternating procedures in \(L^p\), not an established source of the displayed binary-word formula. Shargorodsky--Sharia (2022) determine sharp bounds for a single centered conditional-expectation operator \(I-P\), a different operator from \(P_m\cdots P_1-E\). For \(m=2\), putting \(\rho=d_1/\sqrt{\alpha_1\alpha_2}\) specializes the Hilbertian formula to \(\|(P_2P_1)^k-E\|_{2\to2}=|\rho|^{2k-1}\), consistent with the classical alternating-projection angle law. The rank-one decomposition and Hölder duality are elementary ingredients and are not claimed individually as novel.

## Limitations

The result does not provide non-binary sigma-algebra norm formulas, optimal estimates for products of arbitrary contractions, or universal convergence to constants without an appropriate spectral condition. It excludes the endpoint exponents \(p=1\) and \(p=\infty\). The historical general alternating-procedure literature is extensive; an equivalent previously unindexed formula or reversal example cannot be ruled out. Bibliographic access to the 1987 full text was unavailable, and its abstract alone cannot establish absence of overlap.

## References

1. M. A. Akcoglu and L. Sucheston, *An alternating procedure for operators on \(L^p\) spaces*, Proceedings of the American Mathematical Society **99** (1987), 555–558. DOI: `10.1090/S0002-9939-1987-0875396-0`.
2. R. Zaharopol, *On products of conditional expectation operators*, Canadian Mathematical Bulletin **33** (1990), 257–260. DOI: `10.4153/CMB-1990-041-3` (full primary text inspected).
3. E. Shargorodsky and T. Sharia, *Sharp estimates for conditionally centered moments and for compact operators on \(L^p\) spaces*, Mathematische Nachrichten **296** (2023), 368–381, first publicly posted 2022-12-18. DOI: `10.1002/mana.202100217` (primary HTML inspected).
