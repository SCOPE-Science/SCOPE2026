# A countable entropy-phase spectrum in finite-type covers of geometric gap shifts

## Finding
Fix an integer \(b\geq 2\). Let \(X_b\) be the two-sided binary gap shift whose successive 1s, when both present, have distances in \(\{1,b,b^2,\ldots\}\). For each integer \(n\geq1\), let \(Y_{b,n}\) be its **canonical length-\(n\) finite-type cover**: a bi-infinite binary sequence belongs to \(Y_{b,n}\) exactly when every one of its contiguous length-\(n\) words occurs in \(X_b\). Write \(h_b=h_{\mathrm{top}}(X_b)\) and \(h_{b,n}=h_{\mathrm{top}}(Y_{b,n})\), with natural logarithms.

Define \(\lambda_b\in(1,2)\) and \(S_b>0\) by
\[
\sum_{k=0}^{\infty}\lambda_b^{-b^k}=1,
\qquad S_b=\sum_{k=0}^{\infty}b^k\lambda_b^{-b^k},
\]
and let \(Q_b(n)\) be the smallest positive integer power of \(b\) not smaller than \(n\). Then the finite cover is *exactly* the gap shift allowing the return distances
\[
\mathcal D_{b,n}=\{b^k:b^k<n\}\ \cup\ \{n,n+1,n+2,\ldots\}.
\]
In particular, \(h_{b,n}=\log\lambda_{b,n}\), where \(\lambda_{b,n}\in(1,2]\) is the unique root of
\[
\sum_{b^k<n}\lambda_{b,n}^{-b^k}
+\frac{\lambda_{b,n}^{-n}}{1-\lambda_{b,n}^{-1}}=1.
\]
For every fixed \(b\ge2\), the excess entropy has the **uniform arithmetic boundary-layer law**
\[
\boxed{\displaystyle
\lambda_b^n(h_{b,n}-h_b)=
\frac{(1-\lambda_b^{-1})^{-1}-\lambda_b^{-(Q_b(n)-n)}}{S_b}
+O_b\bigl(n\lambda_b^{-n}\bigr)
}\qquad(n\longrightarrow\infty).
\]
The implicit constant depends only on \(b\), not on the location of \(n\) between consecutive powers.

Consequently the entire subsequential accumulation set of \(\lambda_b^n(h_{b,n}-h_b)\) is the **countably infinite, one-limit-point set**
\[
\boxed{\displaystyle
\left\{\frac{(1-\lambda_b^{-1})^{-1}-\lambda_b^{-t}}{S_b}:t=0,1,2,\ldots\right\}
\cup\left\{\frac{1}{(1-\lambda_b^{-1})S_b}\right\}.}
\]
It is not an interval. In addition, the cover sequence has the exact plateau rule
\[
Y_{b,n}=Y_{b,n+1}\quad\Longleftrightarrow\quad n\in\{1,b,b^2,\ldots\}.
\]
Thus the canonical approximants are never eventually constant and have isolated one-step equality stages precisely at powers of \(b\). Outside those stages their entropies decrease strictly.

## Assumptions and scope
The alphabet is \(\{0,1\}\), the phase space is two-sided, and \(\sigma\) denotes left shift. An allowed return distance \(r\) means a word of the form \(10^{r-1}1\), with no intermediate 1. The shift \(X_b\) is defined as the closure of all bi-infinite concatenations of these return blocks; infinite one-sided zero tails and the all-zero point are therefore included. The parameter \(b\) is any fixed integer at least two; \(n\) ranges over all positive integers. An expression \(O_b(\cdot)\) is uniform as \(n\to\infty\) with fixed \(b\). Entropy uses the natural logarithm.

The canonical length-\(n\) cover here agrees with the \(n\)-th SFT cover in Coles, Cyr, Kra, and Pavlov [1], which forbids all words of length at most \(n\) absent from the original language. Only gaps in a length-\(n\) word are relevant, so the two definitions coincide. The standard gap-shift entropy renewal equation is credited to prior literature [2,3]. The claimed contribution is the exact finite-cover specialization, the *uniform normalized correction*, its complete discrete accumulation spectrum, and the exact plateau positions as one cohesive quantitative description.

## Proof
**1. The canonical cover and its gap language.** A finite binary word occurs in \(X_b\) if and only if all distances between consecutive 1s within it are powers of \(b\). The forward implication is immediate from the definition. Conversely, any finite sequence of allowed gaps can be completed infinitely in both directions using gaps of length one; finite zero prefixes and suffixes pose no obstruction. Therefore its minimal forbidden words are precisely \(10^{r-1}1\) for integers \(r\ge1\) that are not powers of \(b\). Such a forbidden word has length \(r+1\). The length-\(n\) cover forbids it precisely when \(r<n\). Hence a bi-infinite sequence is in the cover if and only if each successive return distance belongs to \(\mathcal D_{b,n}\), establishing the exact equality of subshifts (including limiting zero-tail points).

**2. Entropy equations.** For the finite cover, record the number of zeros since the most recent 1, capped at \(n-1\). States are \(0,1,\ldots,n-1\). Each state has one zero transition to its successor (with a zero self-loop at \(n-1\)). A one transition from state \(j\) to state \(0\) is present when \(j+1\) is a power of \(b\), or when \(j=n-1\). At \(n=1\), the two differently labeled transitions are parallel edges. This presents the cover, with every state accessible and the graph irreducible and aperiodic, because return distance one is always allowed. Its first-return loops at state zero have exactly the lengths in \(\mathcal D_{b,n}\), one loop per length. Thus the first-return generating series is
\[
F_{b,n}(z)=\sum_{b^k<n}z^{-b^k}+\frac{z^{-n}}{1-z^{-1}}.
\]
At \(z\downarrow1\) this diverges and at \(z=2\) it is at most one, with equality exactly when every return length is permitted; strict monotonicity gives the unique root \(\lambda_{b,n}\in(1,2]\). The usual renewal/generating-matrix entropy argument [2,3] identifies \(\log\lambda_{b,n}\) as the entropy. The same standard argument on the infinite return alphabet gives \(F_b(\lambda_b)=1\), where \(F_b(z)=\sum_{k\ge0}z^{-b^k}\); its root satisfies \(1<\lambda_b<2\), because the available return lengths form a proper infinite subset of all positive integers. The derivative with respect to \(u=\log z\) at \(u_b=\log\lambda_b\) is \(F_b'(u_b)=-S_b<0\).

**3. Uniform error at the root.** For fixed \(b\), abbreviate \(\lambda=\lambda_b\), \(S=S_b\), \(Q=Q_b(n)\), and let \(u_n=\log\lambda_{b,n}\). At the exact root \(\lambda\), the difference between the finite and infinite return series equals
\[
F_{b,n}(\lambda)-1
=\frac{\lambda^{-n}}{1-\lambda^{-1}}-\sum_{b^k\ge n}\lambda^{-b^k}.
\]
The tail begins with \(\lambda^{-Q}\) and its next term is \(\lambda^{-bQ}\). Since \(bQ\ge2n\), geometric comparison gives \(\sum_{b^k\ge n}\lambda^{-b^k}=\lambda^{-Q}+O_b(\lambda^{-2n})\). Consequently
\[
F_{b,n}(\lambda)-1
=\lambda^{-n}\left(\frac1{1-\lambda^{-1}}-\lambda^{-(Q-n)}\right)+O_b(\lambda^{-2n}).
\]
The bracket is uniformly positive and bounded because \(0<\lambda^{-(Q-n)}\le1\) and \((1-\lambda^{-1})^{-1}>1\). Uniform convergence of the derivative series near \(u_b\) gives \(F_{b,n}'(u_b)=-S+O_b(n\lambda^{-n})\); the omitted derivative tail and the finite geometric tail are bounded by a constant times \(n\lambda^{-n}\). Their second derivatives are uniformly bounded in a fixed compact neighborhood of \(u_b\). The roots \(u_n\) approach \(u_b\) from above, and the mean-value theorem first yields \(u_n-u_b=O_b(\lambda^{-n})\). Taylor expansion of \(F_{b,n}(e^{u_n})=1\) at \(u_b\), using the preceding derivative and curvature bounds, then yields
\[
u_n-u_b=\frac{\lambda^{-n}}{S}\left(\frac1{1-\lambda^{-1}}-\lambda^{-(Q-n)}\right)+O_b(n\lambda^{-2n}).
\]
Multiplication by \(\lambda^n\) proves the boxed uniform law. This derivation treats every \(n\), including powers \(n=b^k\), without assuming that the gap \(Q-n\) tends to infinity.

**4. All normalized phases.** Put \(t_n=Q_b(n)-n\in\mathbb N_0\). Along any sequence \(n\to\infty\), either a subsequence has a fixed integer value \(t_n=t\), or a subsequence tends to infinity. In the first case the boxed expression tends to \(\big((1-\lambda^{-1})^{-1}-\lambda^{-t}\big)/S\), and in the second to \(1/((1-\lambda^{-1})S)\). Every fixed nonnegative integer \(t\) occurs along \(n=b^k-t\) for all sufficiently large \(k\). Taking \(n=b^k+1\) gives \(Q_b(n)-n=b^{k+1}-b^k-1\to\infty\), realizing the remaining limit. Strict monotonicity of \(\lambda^{-t}\) shows all finite-phase values are distinct and approach their unique additional limit from below. Thus the displayed set is exactly the full cluster set; no intermediate values can occur.

**5. Exact plateau positions.** The only forbidden words newly introduced in passing from \(Y_{b,n}\) to \(Y_{b,n+1}\) are the potential minimal forbidden words of length \(n+1\), hence the return word \(10^{n-1}1\). If \(n\) is a power of \(b\), that word already belongs to \(X_b\), so the two covers coincide. Otherwise the periodic sequence \((10^{n-1})^{\mathbb Z}\) lies in \(Y_{b,n}\) (all its return distances are \(n\)) but not \(Y_{b,n+1}\). Moreover the latter is a proper subshift of the mixing finite-type system \(Y_{b,n}\); the standard strict entropy decrease for proper subsystems of an irreducible SFT gives \(h_{b,n+1}<h_{b,n}\). This proves the plateau assertion and strictness.

## Verification
The included `check.py` constructs the labeled \(n\)-state automata, independently enumerates short admissible languages, solves their Perron-root return equations, and tests the scaled finite-size correction. It uses Python's standard library and is run using `python check.py`. Its completed run checked 96 automaton/root combinations with \(b\in\{2,3,4,5\}\) and \(1\le n\le24\), with short-word checks for \(n\le9\). Additional 90-digit calculations at \(b=2\) and \(b=3\), including \(n=64,127,128,190,255,256\) and \(n=80,81,100,242,243\), corroborated phase stabilization at boundaries. These are finite diagnostics, not the proof for all integers.

For \(b=2\), \(\lambda_b\approx1.7663981145501736\) and \(S_b\approx1.7041763107065920\). The normalized phase values at \(t=0\), \(t=1\), and \(t=\infty\) are approximately \(0.765651342498\), \(1.020247187183\), and \(1.352445087792\), respectively.

## Relationship to prior work
Coles, Cyr, Kra, and Pavlov [1] define canonical finite-type covers and investigate entropy stability, including its equivalence to language stability. They do not determine the cover entropy rate or its rescaled phase spectrum for geometric gap shifts. Dillon [2] gives the entropy generating-matrix/return-series method for general \(S\)-graph shifts, and Ahmadi Dastjerdi and Jangjoo [3,4], together with Ramirez and Somers [7], provide structural and entropy tools for \(S\)-gap shifts; these foundational formulas are prerequisites here, not claimed new.

Two close quantitative comparisons are relevant. The already published *Log-periodic second-order entropy law for geometric gap shifts* [5] treats **the same geometric gap shift** but maximizes invariant entropy at a prescribed marker density tending to zero, without analyzing canonical finite-type covers. The published *A Fibonacci entropy staircase and its full scaled accumulation interval* [6] does treat canonical covers but for the **Fibonacci Sturmian language**, whose unscaled entropy tends to zero and whose normalized cluster set is an interval. In contrast, the present system has positive limiting entropy, a scale \(\lambda_b^{-n}\), and an exactly **countable** cluster set. These are genuine differences of hypotheses and claims, not mere differences of terminology.

## Limitations
The result treats only fixed integer geometric bases \(b\ge2\), canonical finite-type covers, and their topological entropies. It does not assert any formula for arbitrary nongeometric gap sets, measures of maximal entropy, their convergence, or entropy at prescribed marker frequency. The renewal equation and general existence of canonical covers are previously known. Potential equivalent calculations in older symbolic approximation or coding literature cannot be excluded by search alone; independent mathematical review and bibliographic verification have not been performed.

## References
1. S. Coles, V. Cyr, B. Kra, R. Pavlov, *Stable covers of subshifts*, arXiv:2602.04097v1 (first public 2026-02-04), especially §§2.2 and 3.3. https://arxiv.org/html/2602.04097v1
2. T. Dillon, *Dynamics and entropy of S-graph shifts*, arXiv:2010.06031v3 (2022), §§1, 4. https://arxiv.org/html/2010.06031v3
3. D. Ahmadi Dastjerdi, S. Jangjoo, *Computations on Sofic S-gap Shifts*, arXiv:1108.3414v5, especially entropy equations and S-gap presentations. https://arxiv.org/html/1108.3414v5
4. D. Ahmadi Dastjerdi, S. Jangjoo, *Dynamics and Topology of S-gap Shifts*, arXiv:1108.3242v4, especially §§3–4 (an earlier version had been withdrawn; use with that bibliographic caveat). https://arxiv.org/html/1108.3242v4
5. *Log-periodic second-order entropy law for geometric gap shifts*, published research record (2026-10-11). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-log-periodic-second-order-entropy-law-for-geometric-gap-shifts--166969f68799
6. *A Fibonacci entropy staircase and its full scaled accumulation interval*, published research record (2026-10-11). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-fibonacci-entropy-staircase-and-its-full-scaled-accumulation-i--be7c0c99809f

7. C. Ramirez, A. Somers, *(S,w)-Gap Shifts and Their Entropy*, arXiv:2501.08438v1 (first public 2025-01-14), especially Theorems 1.1 and 3.3. https://arxiv.org/html/2501.08438v1
