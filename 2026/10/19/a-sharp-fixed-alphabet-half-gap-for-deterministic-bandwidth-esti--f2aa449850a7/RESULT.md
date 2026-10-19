# A sharp fixed-alphabet half-gap for deterministic bandwidth estimators

## Finding
Let \(\Sigma\) be a finite alphabet with \(q=|\Sigma|\geq 2\). Let \(L\subseteq\Sigma^*\) be finite and contain a nonempty word. In the *useful minimal partial DFA* for \(L\), write \(H_i\) for the set of residual states reached by prefixes of accepted words of length \(i\), \(h_i=|H_i|\), and \(D=\max\{|w|:w\in L\}\). The position-unfolding upper estimator and residual-ball lower estimator of Cho--Fazekas--Wiedenhöft are
\[
U(L)=\max_{1\leq i\leq D}(h_{i-1}+h_i-1),\qquad
B(L)=\max_{p,\,\ell\geq1}\left\lceil\frac{|B_\ell(p)|-1}{\ell}\right\rceil,
\]
where \(B_\ell(p)\) contains all distinct residual states reachable from \(p\) by a word of length at most \(\ell\). Then
\[
\boxed{B(L)\leq\max\left\{q,\left\lceil\frac{2U(L)+1}{3}\right\rceil\right\}.}
\]
In particular, if \(U(L)>\max\{q,3\}\), the two estimators **cannot coincide**. More strongly, for each fixed \(q\geq2\), the sharp asymptotic envelope satisfies
\[
\boxed{\lim_{M\to\infty}\ \sup_{\substack{L\subseteq\Sigma^*\text{ finite},\,D\geq1\\ U(L)\geq M}}\frac{B(L)}{U(L)}=\frac12.}
\]
(The supremum is nonempty for all sufficiently large \(M\).) The constant \(1/2\) is attained as a limit by an explicit binary family.

## Assumptions and scope
A residual is the nonempty left quotient \(u^{-1}L\) represented by a reachable, co-reachable state; no dead sink is included. A defined edge has a useful target. The alphabet has a fixed finite size \(q\), but letters need not all occur in the language. An accepted empty word is allowed provided some nonempty word is also accepted. For \(i>D\), set \(h_i=0\). The estimator \(B(L)\) is the residual-ball bound, **not** the unknown exact minimum bandwidth of a partial DFA accepting \(L\). The two inequalities \(B(L)\leq\operatorname{bw}_{\mathrm{DFA}}(L)\leq U(L)\) are previously known; the quantitative comparison and its sharp fixed-alphabet asymptotic are the findings here.

## Proof
**1. One-layer lifting of balls.** Choose any useful residual state \(p\) and any accepted-prefix length \(j\) witnessing \(p\in H_j\). Every state reachable from \(p\) in exactly \(t\) transitions is also reachable by an accepted prefix of length \(j+t\): prepend the chosen prefix for \(p\) and use co-reachability to extend the path to an accepted word. By assigning each state of \(B_\ell(p)\setminus\{p\}\) a shortest positive-length path, we obtain
\[
|B_\ell(p)|-1\leq\sum_{t=1}^{\ell} h_{j+t}.
\]
Since \(h_0=1\), the defining maximum for \(U=U(L)\) gives \(h_i\leq U\) for all \(i\geq0\) and \(h_i+h_{i+1}\leq U+1\) for all \(i\geq0\), including beyond \(D\) after adjoining zeros.

**2. The finite inequality.** If \(\ell=1\), determinism and \(q\) available letters imply \(|B_1(p)|-1\leq q\). If \(\ell=2m\) with \(m\geq1\), pairing consecutive layer sizes yields
\[
\frac{|B_{2m}(p)|-1}{2m}\leq\frac{m(U+1)}{2m}=\frac{U+1}{2}
\leq\frac{2U+1}{3}.
\]
If \(\ell=2m+1\) with \(m\geq1\), pairing the first \(2m\) layers and bounding the remaining one gives
\[
\frac{|B_{2m+1}(p)|-1}{2m+1}
\leq\frac{m(U+1)+U}{2m+1}
\leq\frac{2U+1}{3}.
\]
The last inequality is exactly \((m-1)(U-1)\geq0\). Taking integer ceilings and the maximum over all states and radii gives the first assertion. For integer \(U\geq4\), \(\lceil(2U+1)/3\rceil\leq U-1\); if additionally \(U>q\), then \(B<U\).

**3. Upper asymptotic envelope.** Fix \(q\) and an integer cutoff \(R\geq2\). At radii \(1\leq\ell<R\), at most \(q^t\) states can be reached by words of length \(t\), so
\[
\frac{|B_\ell(p)|-1}{\ell}\leq\sum_{t=1}^{R-1}q^t,
\]
a constant depending only on \(q,R\). For \(\ell\geq R\), the even-radius bound above and the odd-radius bound with the unpaired layer give uniformly
\[
\frac{|B_\ell(p)|-1}{\ell}\leq
\frac{U+1}{2}+\frac{U-1}{2R}.
\]
The ceiling changes this by at most one. Dividing the maximum of these two bounds by \(U\) and letting \(U\to\infty\), we obtain a limsup at most \(1/2+1/(2R)\). Letting \(R\to\infty\) proves that the envelope is at most \(1/2\).

**4. Binary witnesses and sharpness.** For each integer \(d\geq1\) and \(T\geq1\), let
\[
L_{d,T}=\{x0^T x:x\in\{0,1\}^d\},\qquad k=2^d.
\]
For each \(0\leq i<d\), distinct length-\(i\) prefixes give \(2^i\) distinct residuals. At depths \(d\leq i\leq d+T\), the \(k\) residuals are the singleton languages \(\{0^{d+T-i}x\}\), one for each \(x\); they remain distinct even across different depths because their words have different lengths. After \(s\) letters of the second copy of \(x\), \(1\leq s\leq d\), there are exactly \(2^{d-s}\) residuals. Consequently,
\[
h_i=\begin{cases}
2^i&0\leq i<d,\\
k&d\leq i\leq d+T,\\
2^{d-s}&i=d+T+s,\quad1\leq s\leq d,
\end{cases}\qquad U(L_{d,T})=2k-1.
\]
The radius-\(d+T\) ball centered at the initial residual contains its center and every one of the \(k(T+1)\) distinct singleton residuals appearing at depths \(d,d+1,\ldots,d+T\). Thus
\[
B(L_{d,T})\geq\left\lceil\frac{k(T+1)}{d+T}\right\rceil.
\]
Set \(T=d^2\) and let \(d\to\infty\). This lower bound divided by \(U(L_{d,T})\) tends to \(1/2\). Together with part 3, it proves that the fixed-alphabet envelope is exactly \(1/2\) over the binary alphabet. For larger fixed alphabets, keep the same binary words and leave the extra letters unused. This proves the claimed sharpness for every \(q\geq2\).

## Verification
The standalone script `check.py`, using only the Python standard library, independently constructs minimal residual automata for literal finite languages and computes both estimators. It checked \(24\) distinct binary witness languages \(L_{d,T}\) for \(1\leq d\leq4\) and \(T\in\{1,2,3,5,8,10\}\), including their exact layer profiles; it also checked \(1000\) seeded random finite languages over binary or ternary alphabets. All \(1024\) cases satisfy the proved inequality. The largest upper estimator among the random tests was \(52\). A preserved output transcript appears in `CHECK_OUTPUT.txt`. These finite checks are independent corroboration; the proofs above establish all quantifiers.

## Relationship to prior work
Cho, Fazekas, and Wiedenhöft introduced and compared the position-unfolding and residual-ball estimators for deterministic automata accepting finite languages [1, Sections 5--6]. They proved \(B\leq\operatorname{bw}_{\mathrm{DFA}}\leq U\), gave a matching-bounds example over an alphabet growing with the example parameter, and explicitly raised the fixed-alphabet matching-bounds question. Their paper neither states the finite separation inequality above nor derives the sharp half-gap limit. The present result shows that equality with unbounded estimator value is impossible over any fixed alphabet, even though equality for bounded estimator values is not excluded. Earlier work [2] defines bandwidth for NFAs and proves the finite-language hierarchy, but does not address this comparison between the two *deterministic residual estimators*.

## Limitations
The theorem does not determine the exact minimum deterministic bandwidth \(\operatorname{bw}_{\mathrm{DFA}}(L)\); that value can lie strictly between the two estimators. It does not prohibit infinite fixed-alphabet families with equal estimators of bounded size. The asymptotic is over a class of languages with diverging \(U(L)\), not over a uniform random word model. Unindexed equivalent descriptions of this estimator comparison remain a historical-priority risk. Independent scientific validation has not been performed.

## References
[1] D.-J. Cho, Sz. Zs. Fazekas, M. Wiedenhöft, *Deterministic Bandwidth of Finite Languages*, arXiv:2608.24246, first publicly submitted 25 August 2026, especially Sections 3, 5 and 6. https://arxiv.org/abs/2608.24246

[2] D.-J. Cho, Sz. Zs. Fazekas, D. Ise, S. Seki, W. Tamehira, M. Wiedenhöft, *Bandwidth of Nondeterministic Finite Automata*, arXiv:2606.00663, first publicly submitted 30 May 2026. https://arxiv.org/abs/2606.00663
