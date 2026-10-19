# The exact runner-up spectral concentration for two-character cyclic Fourier masks

## Finding
Let \(N\ge4\) and \(2\le k\le N-2\) be integers, put \(\omega=e^{2\pi i/N}\), and let \(S\subset\mathbb Z/N\mathbb Z\) have \(|S|=k\). Write
\[
 Z(S)=\sum_{j\in S}\omega^j,\quad
 M_{N,k}=\frac{\sin(k\pi/N)}{\sin(\pi/N)},\quad
 R_{N,k}=\sqrt{M_{N,k}^{2}-4\left(\sin^{2}(k\pi/N)-\sin^{2}(\pi/N)\right)}.
\]
A *cyclic interval* is \(a+\{0,1,\ldots,k-1\}\) modulo \(N\). A *one-gap arc* is one of the two cyclic translates/reflections
\[
 a+\{0,1,\ldots,k-2,k\},\qquad
 a+\{0,2,3,\ldots,k\}.
\]
Then \(0\le R_{N,k}<M_{N,k}\), and **among all noninterval \(k\)-point sets**, the exact maximum is
\[
 \boxed{\max_{S\text{ not a cyclic interval}}|Z(S)|=R_{N,k}.}
\]
Equality holds **if and only if** \(S\) is a one-gap arc. The number of distinct labeled equality sets is \(2\) for \((N,k)=(4,2)\), \(N\) for \(k=2\) or \(k=N-2\) with \(N\ge5\), and \(2N\) otherwise.

As a Fourier-concentration statement, let \(\mathcal H\) be the two-dimensional subspace of \(\mathbb C^N\) spanned by the orthonormal Fourier characters \(N^{-1/2}\) and \(N^{-1/2}\omega^j\). For any \(k\)-point observation mask \(S\), set
\[
 \Lambda(S)=\sup_{f\in\mathcal H\setminus\{0\}}\frac{\sum_{j\in S}|f(j)|^2}{\sum_{j=0}^{N-1}|f(j)|^2}.
\]
Then \(\Lambda(S)=(k+|Z(S)|)/N\). Consequently, among **noninterval** masks,
\[
 \boxed{\max\Lambda(S)=\frac{k+R_{N,k}}N,\qquad
 \Lambda(\text{interval})-\max_{\text{noninterval }S}\Lambda(S)
 =\frac{4(\sin^{2}(k\pi/N)-\sin^{2}(\pi/N))}{N(M_{N,k}+R_{N,k})}>0.}
\]
The equality sets for this constrained maximum are exactly the one-gap arcs above. This is a sharp finite, nonasymptotic second-extremal (runner-up) concentration law, not a new claim about the previously known unrestricted maximum.

## Assumptions and scope
Indices are modulo \(N\); equality masks are *labeled subsets*, without quotienting by translations or reflection. The Fourier characters use the unitary \(\ell^2\) normalization \(N^{-1/2}\). The regime \(2\le k\le N-2\) ensures there are both intervals and nonintervals. The exceptional point \((N,k)=(4,2)\) gives \(R_{4,2}=0\). Elsewhere \(R_{N,k}>0\). No uniform sampling weights or Fourier bands of dimension exceeding two are considered.

## Proof
**Lemma (strict circular compression).** Fix \(\theta\in\mathbb R\) and weights \(w_j=\cos(2\pi j/N-\theta)\). If \(S\subset\mathbb Z/N\mathbb Z\) is nonempty, proper, and not a cyclic interval, there exist adjacent indices \(j\in S\), \(\ell\notin S\) for which \(w_\ell>w_j\). Moreover, iterating such adjacent replacements eventually yields a cyclic interval, with the sum of weights strictly increasing at every step.

*Proof.* The vertices maximizing \(w_j\) are either one vertex or two consecutive vertices. Since a noninterval set has at least two connected components in the cycle graph, select a component \(C\) containing none of these maximizers. On a regular polygon the cosine weights strictly increase along at least one edge from a vertex of maximal weight in \(C\) toward a global maximum: the cosine sequence is unimodal on either side of its maximum, including the possible two-site maximum tie. Thus take \(j\in C\) attaining \(\max_{t\in C}w_t\) and a neighbor \(\ell\) with \(w_\ell>w_j\). The neighbor is outside \(C\) by maximality; if it belonged to \(S\) it would be in the same connected component, so \(\ell\notin S\). Replacement strictly increases the total. Since there are finitely many sets of this cardinality and strict increases prevent revisitation, repeated replacements stop only at a connected subset of the cycle, i.e. a cyclic interval. \(\square\)

**From compression to the exact runner-up.** If \(S\) is a noninterval and \(Z(S)\ne0\), fix \(\theta=\arg Z(S)\). Then \(\sum_{j\in S}w_j=|Z(S)|\). Run the lemma until the *first* cyclic interval appears; let \(T\) be its immediately preceding set. Since \(T\) is noninterval, one adjacent replacement \(j\to\ell\) changes \(T\) into a cyclic interval \(I\). Necessarily \(\ell\) is an endpoint of \(I\), and \(j\) is the immediately exterior neighbor of that endpoint (because \(k\le N-2\)); hence \(T\) is a one-gap arc. If \(S\) is not already a one-gap arc, at least one strict increase precedes \(T\), whence
\[
 |Z(S)|=\sum_{j\in S}w_j<\sum_{j\in T}w_j\le|Z(T)|.
\]
If \(S\) is a one-gap arc, equality in the announced optimum follows because all such arcs are related by rotation or reflection and therefore have the same value of \(|Z|\). For \(Z(S)=0\), strict inequality against a positive one-gap value is immediate. The only zero one-gap value occurs at \((N,k)=(4,2)\), when the only noninterval masks are the two opposite pairs and the assertion follows directly. Thus all maximizers among noninterval masks are exactly the one-gap arcs.

**Exact value.** Let \(h=\pi/N\). For the reference interval,
\[
 D=\sum_{j=0}^{k-1}\omega^j=e^{i(k-1)h}\frac{\sin(kh)}{\sin h}.
\]
The reference one-gap arc replaces \(\omega^{k-1}\) with \(\omega^k\). Hence
\[
 Z=D+\omega^k-\omega^{k-1},\qquad
 \omega^k-\omega^{k-1}=2i e^{i(2k-1)h}\sin h,
\]
so by direct multiplication,
\[
 |Z|^2=|D|^2-4\sin^2(kh)+4\sin^2h=R_{N,k}^2.
\]
Since \(\sin^2(kh)-\sin^2h=\sin((k-1)h)\sin((k+1)h)>0\) on the stated range, \(R_{N,k}<M_{N,k}\). The expression is nonnegative because it is the squared modulus of the displayed sum.

**Equality-mask count.** The two orientations each give \(N\) rotations. They have no common masks for \(3\le k\le N-3\). For \(k=2\) or \(k=N-2\), their families coincide and yield \(N\) masks, except when \(N=4\), where the two opposite pairs give exactly two. This proves the counts.

**Fourier compression.** In the orthonormal basis of the two characters spanning \(\mathcal H\), the positive operator of restriction to \(S\) has Gram matrix
\[
 G_S=\frac1N\begin{pmatrix}k&Z(S)\\\overline{Z(S)}&k\end{pmatrix}.
\]
Its largest eigenvalue is \((k+|Z(S)|)/N\), and the extremal mask classification transfers immediately. Rationalization of \(M_{N,k}-R_{N,k}\) gives the gap formula. \(\square\)

## Verification
The standalone Python-standard-library file `verify.py` enumerates **every** \(k\)-subset for \(4\le N\le18\) and \(2\le k\le N-2\). Across 120 admissible parameter pairs and 522,312 noninterval subsets, it checks the exact predicted second maximum, all equality masks, and the interval maximum. The maximum observed floating-point absolute error in the runner-up norm was under \(2.7\times10^{-15}\). Reproduce with `python3 verify.py`; the expected output is in `verification_output.txt`. The finite enumeration is supplementary; the strict-compression proof establishes the theorem for all \(N\) and \(k\).

## Relationship to prior work
Marshall and Waldron (first preprint 2016) develop cyclic harmonic-frame Fourier-character models, providing the natural two-character spectral context. A published exact adversarial-erasure theorem for two-character cyclic harmonic frames gives the **unrestricted maximum** \(M_{N,k}\) and proves that intervals, and only intervals, optimize it. That result already supplies the first extremal spectral value and is explicitly credited here. The present theorem addresses the different optimization domain with all intervals excluded, calculates its new sharp value \(R_{N,k}\), proves the complete one-gap equality characterization and count, and gives the exact positive second-extremal concentration gap. The earlier maximum formula and mere strictness outside its equality class do not determine this runner-up constant or equality geometry.

Baeza-Guasch's 2023 preprint on Donoho--Stark concentration (expanded in a later revision) proves phase-alignment and interval-concentration principles for a continuous no-aliasing setting, with a polynomial analogue. That argument motivates interval extremality but does not supply the above discrete second-extremal constant. The discrete rearrangement of polygon vertices is elementary and not claimed as novel in isolation. The contribution is the global *second-best* classification under a noninterval constraint and its sharp spectral interpretation. An unindexed equivalent circle-sum optimization remains a bibliographic risk.

## Limitations
The theorem is restricted to the two-frequency space with adjacent character frequencies, unweighted spatial masks, and the full range of nontrivial cardinalities. In finite cyclic dimensions the same law holds for character pairs with a unit frequency difference after index relabeling, but no general statement is made for non-coprime differences, arbitrary multi-frequency spaces, or continuous Paley--Wiener observables. The proof is mathematical rather than externally certified. Exhaustive calculations on finitely many cyclic orders do not establish the infinite family. No quantitative robustness result for masks beyond the precise runner-up gap is claimed. The originality comparison cannot rule out unpublished or unindexed folklore.

## References
1. S. Marshall and S. Waldron, *On the number of harmonic frames*, arXiv:1611.07121v1 (first posted 2016-11-22); *Applied and Computational Harmonic Analysis* 48 (2020), 46–63. https://arxiv.org/abs/1611.07121
2. *Exact adversarial-erasure spectra for two-character cyclic harmonic frames*, published mathematical finding, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-adversarial-erasure-spectra-for-two-character-cyclic-harmo--e1e03f96b6f0 (full `RESULT.md` examined; first extremal theorem credited).
3. O. Baeza-Guasch, *On an uncertainty result by Donoho and Stark*, arXiv:2307.04558v1 (first posted 2023-07-10), later revised as *Phase symmetrization and a no-aliasing concentration principle in Paley-Wiener spaces*. https://arxiv.org/abs/2307.04558
