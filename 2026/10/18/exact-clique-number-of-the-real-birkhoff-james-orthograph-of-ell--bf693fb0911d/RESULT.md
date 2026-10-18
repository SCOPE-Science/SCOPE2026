# Exact clique number of the real Birkhoff–James orthograph of \(\ell_\infty^n\)

## Finding
For every integer \(n\ge1\), let \(E=\ell_\infty^n(\mathbb R)\), with coordinate supremum norm, and let \(\omega_n\) denote the maximum number of distinct real projective lines whose representatives are mutually Birkhoff–James orthogonal. Then
\[
\boxed{\omega_n=\max_{1\le k\le n}\binom nk2^{k-1}=\binom n{\lfloor(2n+2)/3\rfloor}\,2^{\lfloor(2n+2)/3\rfloor-1}.}
\]
Equivalently every mutually orthogonal projective family has at most this many members, and equality is attained by the signed ternary vectors of one support size. In particular,
\[
\omega_n=\frac{3^{n+1}}{4\sqrt{\pi n}}\bigl(1+O(n^{-1})\bigr),\qquad n\to\infty.
\]
The new upper bound is valid for **all real projective directions**, not just ternary-coordinate directions; the attaining lower construction appeared previously [3].

## Assumptions and scope
For nonzero real vectors \(x,y\), the directed relation \(x\perp_B y\) means \(\|x+ty\|_\infty\ge\|x\|_\infty\) for every real \(t\). The mutual relation requires both directions. A vertex is a line \(\mathbb Rx\), so scalar multiples cannot be counted separately. Fix \(n\ge1\) throughout. The result is for real scalars; no exact complex-orthograph bound is asserted.

Normalize any nonzero representative \(x\) so \(\|x\|_\infty=1\). Its **signed active pattern** is \(a(x)=(a_i)_{i=1}^n\in\{-1,0,1\}^n\), with \(a_i=\operatorname{sign}(x_i)\) when \(|x_i|=1\) and \(a_i=0\) otherwise. Identifying a pattern with its global negation makes it intrinsic to the real projective line. The rank is the number of active coordinates.

## Proof
**1. An orthogonality obstruction.** On nonzero signed patterns modulo simultaneous negation define \([a]\preceq[b]\) if the support of \(a\) lies within the support of \(b\) and there is one common choice of global sign for which their nonzero entries agree on the support of \(a\). This is a finite ranked partial order; antisymmetry holds after quotienting by overall sign.

If \([a(x)]\preceq[a(y)]\), then \(x\not\perp_B y\). To prove this, choose the sign of \(y\) such that \(x_i=y_i\in\{-1,1\}\) on every active coordinate of the normalized \(x\). For sufficiently small \(t>0\), the entries of \(x-ty\) on these coordinates have modulus \(1-t<1\). Every other entry has modulus less than one at \(t=0\), hence remains less than one for sufficiently small \(t\) by finiteness. Thus \(\|x-ty\|_\infty<1\), contradicting directed orthogonality. In particular two distinct mutually orthogonal projective directions cannot have the same pattern, and their projective active patterns form an antichain in this signed-subset poset.

**2. A sharp projective signed LYM bound.** At rank \(k\), choose the \(k\) active positions and their signs up to global negation. The number of rank-\(k\) patterns is
\[
r_k=\binom nk2^{k-1},\qquad 1\le k\le n.
\]
Choose independently a uniformly random permutation \(\pi\) of the coordinate positions and a uniformly random full sign vector \(\sigma\in\{-1,1\}^n\). For each rank \(k\), restrict \(\sigma\) to the first \(k\) positions of \(\pi\), setting all other entries to zero, and take its class modulo overall sign. The resulting \(n\) patterns make a chain, one of each rank. Every specified rank-\(k\) projective pattern is visited with probability
\[
\frac{1}{\binom nk 2^{k-1}}=\frac1{r_k},
\]
since its support must be the first \(k\) positions and its signs need agree up to a global factor. A chain intersects an antichain \(\mathcal A\) in at most one member. By taking expectations,
\[
\sum_{a\in\mathcal A}\frac1{r_{\operatorname{rank}(a)}}\le1,
\qquad |\mathcal A|\le\max_k r_k.
\]
Applying this to the active patterns in any clique gives the universal upper bound.

**3. Attaining the upper bound.** For fixed \(k\), take all real projective lines represented by coordinate vectors in \(\{-1,0,1\}^n\) with exactly \(k\) nonzeros. Their number is \(r_k\). Two representatives with different supports of equal size each have a coordinate of magnitude one where the other vanishes, so both directed Birkhoff–James inequalities follow immediately. With equal supports, two distinct projective sign patterns contain both an agreeing and a disagreeing coordinate (after choosing a common first sign). For all real \(t\), the supremum of the two corresponding magnitudes is at least \(\max\{|1+t|,|1-t|\}\ge1\), in either orientation. Hence all these lines are mutually orthogonal and form a clique of size \(r_k\). This establishes equality with \(\max r_k\).

**4. Largest rank and asymptotics.** The ratio of successive rank sizes is \(r_{k+1}/r_k=2(n-k)/(k+1)\). It falls through one at \(k=\lfloor(2n+2)/3\rfloor\) (possibly with tied neighboring ranks). The displayed rank maximizes the formula, including \(n=1\). Moreover \(r_k=(3^n/2)\Pr\{B_n=k\}\) for \(B_n\sim\operatorname{Binomial}(n,2/3)\), so Stirling's formula at its mode gives the stated asymptotic. No probabilistic approximation is needed for the exact formula.

## Verification
The standalone Python 3 standard-library program `verify.py` can be run with `python3 verify.py` in this directory. It checks 36 signed-ternary support layers through dimension eight, independently tests every mutual-orthogonality pair (1,274,804 pairs), proves the finite candidate maxima by exact graph search on integer coordinate grids in dimensions two and three, and enumerates 384 signed permutation chains in dimension four to check the LYM frequencies. Expected output:

`VERIFY_OK layers=36 ternary_mutual_pairs=1274804 rational_grids=[(2, 8, 2), (3, 49, 6)] flags=384`

The finite program corroborates examples and sublemmas. The general theorem is proved by the four analytic steps above, not by finite checks.

## Relationship to prior work
Arambašić, Guterman, Kuzma, Rajić, and Zhilina [1] develop the symmetrized Birkhoff–James orthograph, finite-dimensional upper bounds and an explicit full-support sign family of size \(2^{n-1}\) (Example 3.7). Their real coordinate characterization (Corollary 5.7) is consistent with Step 1.

Guterman, Kuzma, Singla, and Zhilina [2] study directed projective orthographs and detection of norm properties; their results do not give a sharp mutual-orthograph clique formula. A later publicly accessible signed-ternary-support construction [3] supplies **precisely the matching lower bound** \(\omega_n\ge\max_k r_k\), but explicitly does not establish a matching upper bound: its result and limitations describe the clique count only within its constructed support layers. Thus the new content is the unrestricted upper bound via a projective signed-face antichain and sharp LYM counting; the lower bound is credited to [3]. These implications have been compared at theorem-and-proof level, not title level.

## Limitations
Only real supremum-norm spaces of finite positive dimension are covered. The proof does not characterize every extremal clique or settle the corresponding complex case. The 2022 survey on Birkhoff–James orthogonality graphs [4] could be inspected only through its accessible abstract and references, not its full chapter; equivalent unindexed literature remains a bibliographic risk. No independent mathematical audit has yet been performed.

## References
1. L. Arambašić, A. Guterman, B. Kuzma, R. Rajić, S. Zhilina, *Symmetrized Birkhoff–James orthogonality in arbitrary normed spaces*, Journal of Mathematical Analysis and Applications 502 (2021), 125203; DOI `10.1016/j.jmaa.2021.125203` (original full journal text, Sections 3 and 5).
2. A. Guterman, B. Kuzma, S. Singla, S. Zhilina, *Birkhoff–James classification of norm's properties*, arXiv `2402.13416`, first submitted 2024-02-20; Advances in Operator Theory 9 (2024), article 43; DOI `10.1007/s43036-024-00321-0` (accessible paper).
3. *Ternary-support cliques of order \(3^n/\sqrt n\) in the Birkhoff–James orthograph of \(\ell_\infty^n\)*, 2026, public result and proof at `https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-ternary-support-cliques-of-order-3-n-sqrt-n-in-the-birkhoff-jame--3cf446af3e2f` (full RESULT.md inspected; lower bound only).
4. L. Arambašić, A. Guterman, B. Kuzma et al., *Birkhoff–James Orthogonality: Characterizations, Preservers, and Orthogonality Graphs* (2022), DOI `10.1007/978-3-031-02104-6_8` (abstract/references only).
