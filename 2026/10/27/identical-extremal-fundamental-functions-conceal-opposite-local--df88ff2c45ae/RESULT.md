# Identical extremal fundamental functions conceal opposite local decay of weighted norms

## Finding
On an infinite-measure interval, two weighted \(L^1\) target spaces can have exactly the same minimal and maximal fundamental functions yet behave oppositely with respect to localized norm decay from one fixed weighted \(L^2\) source. Both target configurations satisfy the necessary extremal-fundamental-function ratio in Proposition 4.1(ii) of Mihula–Pándy [1]. In one configuration, the sharp local norm modulus is asymptotic to \(\sqrt a\log(1/a)/(4\log2)\); in the other the modulus is infinite at every positive scale. Thus the missing datum is **relative spatial alignment**, not any distributional statistic of either space in isolation.

## Assumptions and scope
Work on \(R=(0,\infty)\) with Lebesgue measure and real or complex scalar functions. For each integer \(n\ge1\), let
\[
d_n=16^{-n},\qquad I_n=(4n,4n+d_n),\qquad J_n=(4n+1,4n+1+d_n).
\]
These are pairwise disjoint measurable intervals, and \(|I_n|=|J_n|=d_n\). Define strictly positive weights by
\[
w(x)=\begin{cases}16^n/n^2,&x\in I_n,\\1,&x\notin\bigcup I_n,\end{cases}
\quad
v_0(x)=\begin{cases}4^n,&x\in I_n,\\1,&\text{otherwise},\end{cases}
\quad
v_1(x)=\begin{cases}4^n,&x\in J_n,\\1,&\text{otherwise}.\end{cases}
\]
Set \(X=L^2(R,w\,dx)\), \(Y_i=L^1(R,v_i\,dx)\) for \(i\in\{0,1\}\). For a Banach function space \(Z\), let
\[
\varphi_Z^{\min}(a)=\inf_{|E|=a}\|\mathbf1_E\|_Z,\qquad
\varphi_Z^{\max}(a)=\sup_{|E|=a}\|\mathbf1_E\|_Z,\qquad a>0.
\]
The localized norm modulus is
\[
\mathcal A_i(a)=\sup_{\|f\|_X\le1}\sup_{|E|\le a}\|f\mathbf1_E\|_{Y_i}\in[0,\infty].
\]
Following [1, Definition 1.1], \(X\overset{*}{\hookrightarrow}_{\mathrm{loc}}Y_i\) means precisely \(\mathcal A_i(a)\to0\) as \(a\downarrow0\). There is no assumption that the unlocalized inclusion \(X\to Y_i\) is bounded.

## Proof
**1. The spaces are genuine Banach function spaces.** All weights are at least one and finite almost everywhere. Their excess masses satisfy
\[
\int_R(w-1)\,dx=\sum_{n\ge1}(1/n^2-16^{-n})<\infty,
\qquad
\int_R(v_i-1)\,dx=\sum_{n\ge1}(4^{-n}-16^{-n})<\infty.
\]
Thus the weighted norms of indicators of arbitrary finite-measure sets are finite. The lattice, monotone-convergence and completeness axioms are standard for weighted \(L^p\); the local integration axiom follows from \(w,v_i\ge1\) and Hölder's inequality. In particular, these are not examples relying on a failure of the Banach-function-space axioms.

**2. The one-space extremal data agree, and their necessary ratio vanishes.** Because the weights are at least one and equal one on an infinite-measure complement,
\[
\varphi_X^{\min}(a)=\sqrt a,
\qquad\varphi_{Y_0}^{\min}(a)=\varphi_{Y_1}^{\min}(a)=a.
\]
The measure-preserving involution that interchanges \(I_n\) and \(J_n\) by translations and fixes their complement carries \(v_0\) into \(v_1\). Consequently, \(\varphi_{Y_0}^{\max}=\varphi_{Y_1}^{\max}\), pointwise for all \(a>0\), while the source's extremal functions are unchanged.

For \(16^{-N}\le a<16^{-(N-1)}\), where \(N\ge2\), split the integral against \(v_i\) into indices below and above \(N\). For every measurable \(E\) of measure \(a\),
\[
\int_Ev_i\,dx\le 4^{N-1}a+\sum_{n\ge N}4^n16^{-n}
\le \frac{16}{3}\,4^{-N}.
\]
On the other hand, the union of the source intervals \(I_n\) with \(n\ge N+1\) has measure \(16^{-N}/15\le a\). Enlarge it to measure \(a\) if necessary to obtain
\[
\bigl(\varphi_X^{\max}(a)\bigr)^2
\ge\sum_{n\ge N+1}(16^n/n^2)16^{-n}
=\sum_{n\ge N+1}\frac1{n^2}\ge\frac1{N+1}.
\]
Therefore
\[
0\le \frac{\varphi_{Y_i}^{\max}(a)}{\varphi_X^{\max}(a)}
\le \frac{16}{3}\sqrt{N+1}\,4^{-N}\longrightarrow0,
\quad i=0,1.
\]
Thus both configurations satisfy the necessary condition in [1, Proposition 4.1(ii)].

**3. The exact localized norm formula.** For any positive measurable weights \(w,v\) with \(w>0\) almost everywhere, weighted Cauchy–Schwarz and its equality case give
\[
\sup_{\|f\|_{L^2(w)}\le1}\|f\mathbf1_E\|_{L^1(v)}
=\left(\int_E\frac{v^2}{w}\,dx\right)^{1/2},
\]
with the extended value \(\infty\) allowed (using finite truncations when the integral diverges). Thus \(\mathcal A_i(a)^2=\sup_{|E|\le a}\int_E h_i\,dx\), where \(h_i=v_i^2/w\). This joint quotient, unlike the individual fundamental functions, changes under rearrangement of \(v_i\) relative to \(w\).

**4. Aligned spikes give the exact decay constant.** For \(i=0\), the quotient is \(h_0=n^2\) on \(I_n\) and \(h_0=1\) elsewhere. Since \(h_0-1\) is integrable, its integrals are uniformly absolutely continuous on small-measure sets; therefore \(\mathcal A_0(a)\to0\).

More precisely, choose \(N\ge2\) so that \(16^{-N}\le a<16^{-(N-1)}\). The set \(\bigcup_{n\ge N-1}I_n\) has measure greater than \(a\) and satisfies \(h_0\ge (N-1)^2\), yielding
\[
(N-1)^2a\le \mathcal A_0(a)^2.
\]
Pointwise one also has
\[
h_0\le(N-1)^2+\sum_{n\ge N}\bigl(n^2-(N-1)^2\bigr)\mathbf1_{I_n}.
\]
Writing \(n=N+k\), the sum of its positive excess integrals is
\[
16^{-N}\sum_{k\ge0}(k+1)(2N+k-1)16^{-k}\le 3N16^{-N}\le3Na.
\]
It follows that
\[
(N-1)^2\le\frac{\mathcal A_0(a)^2}{a}\le(N-1)^2+3N.
\]
As \(4(N-1)\log2<\log(1/a)\le4N\log2\), this proves the sharp limit
\[
\boxed{\lim_{a\downarrow0}\frac{\mathcal A_0(a)}{\sqrt a\log(1/a)}=\frac1{4\log2}.}
\]

**5. Separated spikes destroy every local bound.** On each \(J_n\), the source weight equals one while the new target weight is \(4^n\), so \(h_1=16^n\) and
\[
\int_{J_n}h_1\,dx=16^n16^{-n}=1.
\]
For any \(a>0\), choose \(N\) with \(\sum_{n\ge N}|J_n|=16^{-N}(16/15)<a\). Every finite union \(E_m=\bigcup_{n=N}^{N+m-1}J_n\) then has measure less than \(a\), but \(\int_{E_m}h_1\,dx=m\). The exact localized norm formula gives \(\mathcal A_1(a)\ge\sqrt m\) for every positive integer \(m\); hence \(\mathcal A_1(a)=\infty\). The simpler normalized witnesses \(f_n=4^n\mathbf1_{J_n}\) already have \(\|f_n\|_X=\|f_n\|_{Y_1}=1\) and shrinking supports, establishing failure of localized decay without reliance on an extended-valued norm.

## Verification
The proof is analytic; no finite numerical experiment is used as a substitute. All coefficients and sums are explicit. For the upper estimate in Step 4, the geometric identities \(\sum_{k\ge0}(k+1)16^{-k}=256/225\) and \(\sum_{k\ge0}k(k+1)16^{-k}=512/3375\) give the displayed \(3N\) bound for \(N\ge2\). The same displayed intervals and weights suffice to reproduce every bound. The modular norm formula is checked by weighted Cauchy–Schwarz and its equality case, including truncated finite unions for the separated configuration.

## Relationship to prior work
Mihula and Pándy [1] introduce minimal and maximal fundamental functions for non-rearrangement-invariant function spaces, and Proposition 4.1(ii) gives a necessary vanishing quotient for localized uniform norm decay. The present counterexample satisfies that quotient for both configurations, and preserves the *entire individual marginal functions* (not merely their asymptotic orders) while changing the localized embedding behavior. Their unweighted Lebesgue/Lorentz examples do not imply this spatial-rearrangement dichotomy. Earlier work by Slavíková [2] formulates almost-compact embeddings and their link to compactness; Edmunds, Gogatishvili and Nekvinda [3] treat variable-exponent almost-compact embeddings. Neither of those general frameworks is used here as a novelty argument by title alone; this contribution is the concrete equal-invariants/opposite-local-decay construction and its sharp positive modulus.

## Limitations
The example concerns weighted \(L^2\)-to-weighted \(L^1\) localized norm decay on a nonatomic infinite-measure interval. It does not give a universal classification of non-rearrangement-invariant function spaces, nor a compactness criterion for a specified differential operator. Global inclusion of the two weighted spaces is not asserted. The exact originality comparison is subject to possible unindexed older weighted-embedding constructions; the mathematical statement is explicit and can be checked independently.

## References
[1] Z. Mihula and M. Pándy, *Uniform decay of function norms*, arXiv:2511.19000v1 (first public submission 24 November 2025), https://arxiv.org/html/2511.19000.

[2] L. Slavíková, *Almost-compact embeddings*, Math. Nachr. 285 (2012), 1500–1516, https://doi.org/10.1002/mana.201100286.

[3] D. E. Edmunds, A. Gogatishvili and A. Nekvinda, *Almost-compact and compact embeddings of variable exponent spaces*, Studia Math. 268 (2023), 187–211; arXiv:2101.00182, https://arxiv.org/abs/2101.00182.
