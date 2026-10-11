# Sharp \(\Lambda(4)\) constants for a single pair-product collision

## Finding
Let \(G\) be a compact abelian group with normalized Haar measure, and let \(\Lambda=\{\lambda_1,\ldots,\lambda_n\}\subset \widehat G\) be a finite set of distinct characters. For \(F=\sum_{\lambda\in\Lambda}a_\lambda\lambda\), define \(K_4(\Lambda)\) by
\[
\|F\|_4\le K_4(\Lambda)\left(\sum_{\lambda\in\Lambda}|a_\lambda|^2\right)^{1/2}.
\]
Consider the unordered pair-product map from two-element multisets of \(\Lambda\) to \(\widehat G\), sending \(\{\lambda,\mu\}\) to \(\lambda\mu\). Assume this map has exactly one nonsingleton fiber, and that fiber consists of exactly two distinct unordered pairs. Then exactly one of the following three collision types occurs, and the sharp fourth-power constant is as stated:

1. Two diagonal pairs, \(\lambda_0^2=\lambda_1^2\): \(K_4(\Lambda)^4=2\).
2. A diagonal pair and an off-diagonal pair, \(\lambda_1^2=\lambda_0\lambda_2\): \(K_4(\Lambda)^4=15/7\).
3. Two off-diagonal pairs, \(\lambda_0\lambda_3=\lambda_1\lambda_2\): \(K_4(\Lambda)^4=9/4\).

Characters outside the unique collision never occur in a nonzero extremizer. Writing \(S=\sum |a_\lambda|^2\), equality occurs precisely as follows, in addition to the displayed product relation. In case 1, \(|a_0|^2=|a_1|^2=S/2\) and \(a_0^2\overline{a_1^2}\) is positive real. In case 2,
\[
(|a_0|^2,|a_1|^2,|a_2|^2)=\frac{S}{7}(2,3,2),
\]
and \(a_1^2\overline{a_0a_2}\) is positive real. In case 3, the four participating squared moduli all equal \(S/4\), and \(a_0a_3\overline{a_1a_2}\) is positive real.

## Assumptions and scope
The hypothesis is combinatorial: among all unordered products \(\lambda_i\lambda_j\) with \(i\le j\), there is exactly one product represented twice and every other product is represented once. Two colliding unordered pairs cannot share exactly one index, because cancellation of the common character would force two characters of \(\Lambda\) to coincide. Hence the three cases above exhaust all possibilities according to whether the two pairs involve two, three, or four distinct characters.

The result applies to arbitrary compact abelian \(G\); no finiteness assumption on \(G\) is needed. It does not address multiple simultaneous pair-product collisions.

## Proof
Put \(x_j=|a_j|^2\) and \(S=\sum_jx_j\). By Parseval applied to \(F^2\), if all unordered pair products were distinct then
\[
\|F\|_4^4
=\sum_jx_j^2+4\sum_{i<j}x_ix_j
=2S^2-\sum_jx_j^2.
\]
The unique collision changes exactly one coefficient of \(F^2\), so it adds exactly one interference term.

For two diagonal pairs the extra term is
\[
2\operatorname{Re}(a_0^2\overline{a_1^2})\le2x_0x_1.
\]
Therefore
\[
\|F\|_4^4\le2S^2-(x_0-x_1)^2-\sum_{j\notin\{0,1\}}x_j^2\le2S^2.
\]
Both inequalities are equalities exactly under the phase and support conditions stated above.

For the diagonal/off-diagonal collision, the extra term is
\[
4\operatorname{Re}(a_1^2\overline{a_0a_2})\le4x_1\sqrt{x_0x_2}.
\]
Set \(u=x_0+x_2\), \(v=x_1\), and \(t=u+v\). Since \(x_0^2+x_2^2\ge u^2/2\) and \(\sqrt{x_0x_2}\le u/2\),
\[
-(x_0^2+x_1^2+x_2^2)+4x_1\sqrt{x_0x_2}
\le-\frac{u^2}{2}-v^2+2uv.
\]
The right side has the exact decomposition
\[
-\frac{u^2}{2}-v^2+2uv
=\frac{(u+v)^2}{7}-\frac{(3u-4v)^2}{14}
\le\frac{t^2}{7}.
\]
Consequently
\[
\|F\|_4^4\le2S^2+\frac{t^2}{7}-\sum_{j\notin\{0,1,2\}}x_j^2
\le\frac{15}{7}S^2.
\]
Equality forces all outside coefficients to vanish, \(x_0=x_2\), and \(3u=4v\), giving the ratio \(2:3:2\), together with phase alignment.

For the off-diagonal/off-diagonal collision, the extra term is
\[
8\operatorname{Re}(a_0a_3\overline{a_1a_2})
\le8\sqrt{x_0x_1x_2x_3}.
\]
If \(t=x_0+x_1+x_2+x_3\), then
\[
\sum_{j=0}^3x_j^2\ge4\sqrt{x_0x_1x_2x_3},
\qquad
\sqrt{x_0x_1x_2x_3}\le\frac{t^2}{16}.
\]
Hence the contribution beyond \(2S^2\) is at most \(t^2/4\), and
\[
\|F\|_4^4\le2S^2+\frac{t^2}{4}-\sum_{j\notin\{0,1,2,3\}}x_j^2
\le\frac94S^2.
\]
Equality in both arithmetic-mean inequalities forces the four participating squared moduli to be equal; equality in the phase bound gives the stated phase condition. Explicit coefficients with these moduli and aligned phases show all three constants are attained.

## Verification
The standalone verifier checks the exact quadratic identity used in case 2, constructs explicit finite groups realizing all three collision types, confirms that each model has exactly one nonsingleton unordered-product fiber, compares direct Haar averages of \(|F|^4\) with the Parseval collision formula on random coefficients, checks the sharp inequalities, and tests equality witnesses. Its output is:

`VERIFY_OK collision_types=3 exact_B_identities=1000 direct_checks=900 equality_witnesses=3`

These computations are regression checks only. The universal result is proved by the identities and inequalities above.

## Relationship to prior work
The terminology \(K_p(\Lambda)\) and the \(\Lambda(p)\) framework are classical. Michels studies \(\Lambda(p)\)-sets, interpolation, and operator ideals, providing the ambient harmonic-analysis framework but not this finite one-collision optimization. The present statement isolates the first combinatorial departure from pair-product uniqueness and shows that the sharp \(L^4/L^2\) constant depends on the incidence type of that single relation.

Hajela’s construction paper is closer to the combinatorics: its Proposition 3.2 bounds \(\Lambda(2n)\) constants through uniform bounds on the number of additive representations. That representation-count estimate is not an exact optimization for a single collided product and does not distinguish the three incidence types.

Sidon and \(B_2\)-type conditions are classically organized around uniqueness of pair sums or pair products. The result here quantifies the first failure of that uniqueness: one relation produces one of exactly three constants, while any characters not involved in the relation are excluded from extremizers.

## Limitations
The theorem assumes exactly one two-pair collision. It does not classify configurations with a product represented three or more times, or with several distinct collided products. It also does not claim that the three constants determine higher \(K_p\) norms. An older equivalent formulation under additive-energy, \(B_2\), or finite-dimensional \(\Lambda(4)\) terminology may exist; targeted searches did not locate one, but absence from the searched sources is not a proof of historical novelty.

## References
1. C. Michels, “\(\Lambda(p)\)-sets and the limit order of operator ideals,” arXiv:math/9904176v1, first public 1999-04-30; primary MSC 43A46.
2. D. J. Hajela, “Construction techniques for some thin sets in duals of compact abelian groups,” *Annales de l’Institut Fourier* 36 (1986), 137–166, DOI:10.5802/aif.1063.
3. C. C. Graham and K. E. Hare, *Interpolation and Sidon Sets for Compact Groups*, Springer, 2013, Chapter 6, “Sidon Sets: Introduction and Decomposition Properties,” DOI:10.1007/978-1-4614-5392-5_6.
