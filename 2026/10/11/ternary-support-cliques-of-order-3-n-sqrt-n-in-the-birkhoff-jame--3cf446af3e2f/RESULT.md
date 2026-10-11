# Ternary-support cliques of order \(3^n/\sqrt n\) in the Birkhoff–James orthograph of \(\ell_\infty^n\)

## Finding
Let \(\mathbb F\) be either \(\mathbb R\) or \(\mathbb C\), and let \(n\ge1\). Two nonzero vectors in the normed space \(E=\ell_\infty^n(\mathbb F)\) are Birkhoff–James orthogonal, written \(x\perp_B y\), when \(\|x+\lambda y\|_\infty\ge\|x\|_\infty\) for every \(\lambda\in\mathbb F\). They are *mutually* orthogonal when both directed relations hold. The **projective mutual orthograph** has one vertex for each one-dimensional \(\mathbb F\)-linear subspace of \(E\), and joins distinct vertices when they have mutually orthogonal representatives. Homogeneity makes this definition independent of representatives. Write \(\omega_n\) for its clique number.

For each integer \(1\le k\le n\), let \(\mathcal C_{n,k}\) be the lines represented by vectors whose coordinates belong to \(\{-1,0,1\}\), whose supports have size \(k\), and whose first nonzero coordinate is \(+1\). Then \(\mathcal C_{n,k}\) is a clique of cardinality \(\binom nk2^{k-1}\). Consequently,
\[
\omega_n\ \ge\ L_n=\max_{1\le k\le n}\binom nk2^{k-1}
=\binom n{\lfloor(2n+2)/3\rfloor}2^{\lfloor(2n+2)/3\rfloor-1},
\]
and
\[
L_n=\left(1+O\!\left(\frac1n\right)\right)\frac{3^{n+1}}{4\sqrt{\pi n}}\qquad(n\longrightarrow\infty).
\]
This gives a clique lower bound of exponential base \(3\), rather than the previously published full-support sign-cube lower bound \(2^{n-1}\). The result is a lower-bound construction, not an assertion that \(\omega_n=L_n\).

## Assumptions and scope
The norm is the coordinate supremum norm, the scalar field is real or complex, and only finite positive integer dimensions are considered. Each clique vertex is a projective line, not an individual multiple of a chosen vector. All nonzero coordinates of the constructed representatives are exactly \(\pm1\). This restriction is used to prove orthogonality but is not imposed on arbitrary vertices of the full orthograph.

## Proof
**Distinct representatives.** Fix a support \(S\subseteq\{1,\ldots,n\}\) of size \(k\). There are \(2^{k-1}\) sign assignments having the first nonzero coordinate \(+1\). Representatives with different supports cannot be scalar multiples; representatives with the same support that are scalar multiples would have ratio \(\pm1\), and the fixed first sign forces ratio \(+1\), hence equality. This remains true for complex scalar multiples. Thus there are exactly \(\binom nk2^{k-1}\) different projective lines.

**Different supports.** Let \(x,y\) be representatives with different supports of the same size \(k\). There are coordinates \(i\) with \(|x_i|=1\) and \(y_i=0\), and \(j\) with \(|y_j|=1\) and \(x_j=0\). For every \(\lambda\in\mathbb F\),
\[
\|x+\lambda y\|_\infty\ge |x_i+\lambda y_i|=1=\|x\|_\infty,
\quad
\|y+\lambda x\|_\infty\ge |y_j+\lambda x_j|=1=\|y\|_\infty.
\]
Hence mutual orthogonality holds, regardless of how the supports intersect.

**Equal supports.** If \(x\ne y\) have the same support and the fixed positive first nonzero coordinate, they agree at this first coordinate and disagree at another coordinate \(j\). The corresponding two coordinates of \(x+\lambda y\) have moduli \(|1+\lambda|\) and \(|1-\lambda|\). In either scalar field,
\[
\max\{|1+\lambda|,|1-\lambda|\}^2
\ge\frac{|1+\lambda|^2+|1-\lambda|^2}{2}
=1+|\lambda|^2\ge1.
\]
The same argument applies after interchanging \(x\) and \(y\). Thus every pair of different representatives is mutually Birkhoff–James orthogonal.

**Optimal uniform support and asymptotics.** Let \(a_k=\binom nk2^{k-1}\). For \(1\le k<n\),
\[
\frac{a_{k+1}}{a_k}=\frac{2(n-k)}{k+1}.
\]
This ratio decreases strictly with \(k\), so \(k_n=\lfloor(2n+2)/3\rfloor\) is a maximizing index (two adjacent maxima occur when \(n\equiv2\pmod3\)). Since
\[
a_k=\frac{3^n}{2}\,\mathbb P\bigl(B_n=k\bigr),\qquad B_n\sim\operatorname{Binomial}(n,2/3),\]
the Stirling formula at its mode \(k_n=2n/3+O(1)\) gives
\[
\mathbb P(B_n=k_n)=\frac{3}{2\sqrt{\pi n}}\bigl(1+O(n^{-1})\bigr),
\]
and the asserted asymptotic formula follows. This is a proof for every dimension, not an inference from finite enumeration.

## Verification
Run `python3 verify.py` (Python standard library only). It counts all representatives, checks the exact real Birkhoff–James criterion for every unordered pair in all support layers through dimension six, and checks the largest layer additionally in dimensions seven and eight. It also tests the elementary layer-ratio identity. The expected final line is:

`VERIFY_OK layer_count_checks=36 mutually_orthogonal_pairs=475172 all_pairs_exact=True`

The first eight constructive lower bounds are \(1,2,6,16,40,120,336,896\), versus full-support sign-cube bounds \(1,2,4,8,16,32,64,128\). The analytic proof, including the complex case and all dimensions, is independent of these finite computations.

## Relationship to prior work
Arambašić, Guterman, Kuzma, Rajić and Zhilina (2021), Example 3.7, exhibit \(2^{n-1}\) mutually orthogonal lines from the \(\pm1\) corners with *all* \(n\) coordinates nonzero. Their dimension-dependent upper-bound theorem and its orthograph restatement do not produce this new lower bound: the present construction mixes **different equal-cardinality supports**, whose pairwise orthogonality is supplied by coordinate disappearance in both directions. For the case \(k=n\), the construction exactly recovers their earlier family.

Guterman, Kuzma, Singla and Zhilina (2024) classify information encoded by the directed Birkhoff–James orthograph, including a finite-dimensional clique criterion. Their primary results concern graph invariants and norm recognition, and do not state the layer-count clique construction or an asymptotic lower bound of base \(3\). The 2022 survey by Arambašić and collaborators is a plausible additional relevant overview, but its full chapter text was unavailable for comparison; only its abstract and references were examined.

## Limitations
No matching upper bound for the true clique number is proved. Maximality is proved **only within** the explicit one-layer family as \(k\) varies, not among arbitrary projective vectors or unions of multiple layers. A full-text comparison with the 2022 survey remains outstanding, as does exhaustive coverage of all unindexed formulations. Finite checker output corroborates specific cases but does not establish the infinite-dimensional growth formula. Neither independent audit nor independent validation has been performed.

## References
1. L. Arambašić, A. Guterman, B. Kuzma, R. Rajić, S. Zhilina, *Symmetrized Birkhoff–James orthogonality in arbitrary normed spaces*, J. Math. Anal. Appl. 502 (2021), 125203. DOI: `10.1016/j.jmaa.2021.125203`. See Example 3.7 and Theorem 4.1.
2. A. Guterman, B. Kuzma, S. Singla, S. Zhilina, *Birkhoff–James classification of norm’s properties*, Advances in Operator Theory 9 (2024), 43. DOI: `10.1007/s43036-024-00321-0`. First public version: 2024-04-26. Primary MSC 46B20.
3. L. Arambašić, A. Guterman, B. Kuzma, et al., *Birkhoff–James Orthogonality: Characterizations, Preservers, and Orthogonality Graphs*, in *Operator and Norm Inequalities and Related Topics* (2022), pp. 255–302. DOI: `10.1007/978-3-031-02104-6_8` (abstract and references examined; full chapter not obtained).
