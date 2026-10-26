# The rational first-order probability spectrum of uniform layered permutations

## Finding

Let \(\mathcal L_n=\operatorname{Av}_n(231,312)\) denote the layered permutations on \(n\ge1\) elements, sampled uniformly, and regard a permutation as a structure with its two strict total orders, position order \(<_P\) and value order \(<_V\). For every first-order sentence \(\varphi\) in this two-order language, the limit
\[
 p_\varphi=\lim_{n\to\infty}\frac{|\{\pi\in\mathcal L_n:\pi\models\varphi\}|}{2^{n-1}}
\]
exists, is a rational number, and is effectively computable from \(\varphi\). Conversely, **for every rational \(r\in[0,1]\), there is a first-order two-order sentence with limiting probability exactly \(r\)**. Thus the complete spectrum is
\[
 \bigl\{p_\varphi:\varphi\text{ a first-order two-order sentence}\bigr\}=\mathbb Q\cap[0,1].
\]
Moreover, each prescribed \(r=m/q\), with integers \(0\le m\le q\) and \(q\ge1\), is realized constructively by a sentence whose probability at each finite \(n\) is \(m/q\) times the probability that one of \(q\) fixed binary patterns appears among the consecutive inter-layer cut indicators. The latter probability approaches \(1\) exponentially fast.

## Assumptions and scope

A layered permutation is a direct sum of nonempty decreasing blocks. Such a permutation is uniquely specified by the set of cuts between successive positions. Equivalently, it is specified by a binary word \(b_1\cdots b_{n-1}\) with \(b_i=1\) if a new decreasing block starts after position \(i\); the \(n-1\) cut bits are independent fair bits under the uniform distribution on \(\mathcal L_n\). There are exactly \(2^{n-1}\) layered permutations. We use *full first-order logic with the two strict total orders*, rather than successor-only logic, monadic second-order logic, or arbitrary permutation classes.

Write \(S_P(x,y)\) for the first-order formula saying that \(y\) immediately follows \(x\) in position order. Then the cut predicate is first-order definable by
\[
 C(x)\quad\Longleftrightarrow\quad \exists y\,[S_P(x,y)\wedge x<_V y].
\]
For two distinct positions, belonging to the same decreasing block is equivalent to the absence of a cut between them. This equivalence permits reconstruction of the value order from position order and cut bits by first-order formulas. The terminal position serves as a fixed endmarker and is not one of the \(n-1\) cut-bit positions.

## Proof

**1. Uniform word interpretation.** Each subset of the \(n-1\) adjacencies partitions the position order into maximal consecutive blocks; assign consecutive values in reverse order within each block. This is a bijection from \(\{0,1\}^{n-1}\) onto \(\mathcal L_n\). If \(x<_P y\), the same-block formula is
\[
 B(x,y)\ \Longleftrightarrow\ \forall z\,[\,(x\le_P z<_P y)\Rightarrow\neg C(z)\,].
\]
For arbitrary distinct \(x,y\), write \(E(x,y)\) for \(B(x,y)\) if \(x<_P y\), and for \(B(y,x)\) if \(y<_P x\). Then
\[
 x<_V y\ \Longleftrightarrow\
 [x<_P y\wedge\neg E(x,y)]\ \vee\ [y<_P x\wedge E(x,y)].
\]
All displayed relations are first-order definable using the linearly ordered cut word with one terminal sentinel. Conversely, \(C(x)\) is definable from the two orders by the displayed adjacency formula. Thus each two-order first-order sentence transfers effectively to a first-order sentence about the finite binary cut word (with a definable terminal sentinel), and the reverse transfer holds for fixed binary-pattern occurrences and order comparisons.

**2. Rationality of every limit.** Fix \(\varphi\). Its finite binary cut words form a regular language: first-order-definable word languages are regular (indeed star-free), and adding or eliminating one terminal sentinel preserves regularity. Hence the number \(a_t\) of accepted words of length \(t\) has an ordinary generating function \(F(z)=\sum_{t\ge0}a_tz^t\in\mathbb Q(z)\), effectively obtained from a finite automaton with integer transition matrices. Since \(\varphi\) has a first-order convergence law for uniformly random layered permutations, the sequence \(a_t/2^t\) converges to \(p_\varphi\) (Braunfeld--Kukla). The elementary Abel limit theorem gives
\[
 p_\varphi=\lim_{s\uparrow1}(1-s)\sum_{t\ge0}(a_t/2^t)s^t
 =\lim_{s\uparrow1}(1-s)F(s/2).
\]
The last expression is a rational function with rational coefficients, having a finite limit at \(s=1\); cancellation and evaluation at the rational argument \(1\) show \(p_\varphi\in\mathbb Q\). This also gives an algorithm for its exact evaluation: construct the finite automaton, form \(F\), cancel the removable singularity in \((1-s)F(s/2)\), and evaluate at \(s=1\). No assumption about aperiodicity beyond the cited first-order convergence theorem is needed.

**3. A family of mutually nonoverlapping codewords.** Fix \(q\ge1\). Choose an integer \(h\ge1\) large enough that at least \(q\) length-\(h\) binary words contain no substring `00`. Choose \(q\) distinct such words \(u_1,\dots,u_q\) and define equally long markers
\[
 w_j=001u_j1\qquad(1\le j\le q),\qquad \ell=h+4.
\]
Every marker begins with `00`, has no other occurrence of `00`, and ends in `1`. Therefore, for any pair \(i,j\) and every proper overlap length \(1\le a<\ell\), the length-\(a\) suffix of \(w_i\) differs from the length-\(a\) prefix of \(w_j\). Indeed, for \(a=1\), the former is `1` and the latter `0`; for \(a\ge2\), the latter starts `00` and the former does not. This includes self-overlaps.

**4. Exact symmetry of the first marker.** For a finite binary word \(v\), let \(H_j(v)\) mean that some marker occurs and the earliest starting position among all occurrences of the \(q\) markers carries \(w_j\). The events \(H_j\) are disjoint. If \(H_i(v)\) holds with earliest start \(t\), replace the length-\(\ell\) block \(w_i\) starting at \(t\) by \(w_j\). A new marker starting before \(t\) would overlap the replacement and require a forbidden proper suffix-prefix overlap; occurrences entirely before \(t\) are unchanged. Thus the earliest start remains \(t\), now with marker \(j\), and swapping back is the inverse. This is a bijection between \(H_i\) and \(H_j\) at every word length. For an independent fair binary word \(V_t\) of length \(t\),
\[
 \Pr(H_j(V_t))=\frac1q\Pr(H(V_t)),
 \qquad H=\bigcup_{i=1}^q H_i.
\]
Inspecting the disjoint \(\lfloor t/\ell\rfloor\) contiguous length-\(\ell\) windows shows
\[
 1-\Pr(H(V_t))\ \le\ (1-q2^{-\ell})^{\lfloor t/\ell\rfloor}\ \longrightarrow 0.
\]
Here \(q2^{-\ell}\le1\) because the markers are distinct, and if equality happens the bound is interpreted in the elementary obvious way. Thus for \(0\le m\le q\), the event \(H_1\vee\cdots\vee H_m\) has probability exactly \((m/q)\Pr(H)\) at every length and limiting probability \(m/q\).

**5. First-order realizability.** Because \(\ell\) and the marker list are fixed once \(q\) is fixed, occurrence of \(w_j\) starting at \(x\) is a first-order formula: existentially specify \(\ell\) consecutive nonterminal elements beginning at \(x\), and test \(C\) or \(\neg C\) at each. The condition that \(x\) is the least starting point of any marker is a first-order formula using \(<_P\). Consequently, the assertion that the earliest marker belongs to \(\{w_1,\dots,w_m\}\) is a first-order two-order sentence. Its limit is \(m/q\), including the endpoint cases \(m=0\) and \(m=q\), completing both inclusions of the asserted spectrum.

## Verification

The accompanying standalone `checker.py` enumerates mutually nonoverlapping marker families for \(1\le q\le18\); verifies every labelled layered permutation/cut-word bijection through size \(12\); and exhaustively verifies equality of the finite-length first-marker counts for \(q\in\{2,3,4,5\}\) across multiple word lengths. Its successful execution prints `LAYERED_RATIONAL_EXACT_OK 22147 code_families 18 q_tested [2, 3, 4, 5]`. The code checks finite instances only. The general rationality, first-hit bijection, nonoverlap and asymptotic bound are proved above, not inferred from experiments.

For example, the three codewords `001011`, `001101`, `001111` are mutually nonoverlapping. The first-codeword construction realizes the first-order limiting probability \(1/3\), illustrating that the spectrum is strictly larger than the dyadic rationals.

## Relationship to prior work

Braunfeld and Kukla (first public version 2021, journal version 2022) proved the first-order convergence law for layered permutations and related convex ordered structures; this is the convergence theorem invoked above, **not a new result**. Markström and Räty (first public version October 15, 2026) proved rational generating functions and first-order convergence for all small permutation classes using regular-language representations. Their published theorem implies rationality for this specific class by the rational-pole argument, but the inspected results do not give the converse realization of **every** rational limit by explicit two-order first-order sentences.

The contribution here is the exact arithmetic *spectrum* and constructive first-marker symmetry, not the known regular-language correspondence or convergence law. The newer paper mentions a separate 2026 manuscript by Falgas--Ravry, Markström, Skerman and Räty proving density of limiting probabilities in exponential-growth classes; its full manuscript was not located, so stronger special-case coverage remains a stated priority risk.

## Limitations

The exact spectrum applies only to uniform layered permutations in full first-order logic of two linear orders. The result does not describe monadic-second-order modular limit spectra, other pattern-avoiding permutation classes, nonuniform cut probabilities, or rate bounds for every arbitrary first-order sentence. The first-marker construction supplies exponential convergence for the specially constructed sentences, not a universal rate. Publication priority, especially relative to the separately cited 2026 manuscript, has not been independently established. The checks performed are mathematical and computational same-author scrutiny; no independent validation is claimed.

## References

1. S. Braunfeld and M. Kukla, *Logical Limit Laws for Layered Permutations and Related Structures*, Enumerative Combinatorics and Applications **2** (2022), #S4PP2, DOI: 10.54550/ECA2022V2S4PP2; first public preprint arXiv:2111.06307 (November 11, 2021). The journal article lists MSC2020 03C13 as primary.
2. K. Markström and E. Räty, *Logical isomorphism and logical limit laws for small permutation classes and regular languages*, arXiv:2610.22218v1 (October 15, 2026), subsequently revised.
3. V. Falgas--Ravry, K. Markström, F. Skerman and E. Räty, *On first-order limiting probabilities for small permutation classes*, manuscript cited by reference 2 (2026); full text not inspected.
4. W. Thomas, *Languages, automata, and logic*, Handbook of Formal Languages, Vol. 3 (1997), 389--455 (regularity of first-order-definable word languages).
