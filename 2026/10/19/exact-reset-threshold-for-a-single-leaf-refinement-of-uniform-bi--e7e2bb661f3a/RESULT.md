# Exact reset threshold for a single-leaf refinement of uniform binary prefix codes

## Finding
For every integer \(m\ge2\), consider the binary complete prefix code
\[
X_m=\bigl(\{0,1\}^m\setminus\{1^m\}\bigr)\cup\{1^m0,1^m1\}.
\]
Its **literal decoding automaton** \(A_m\), whose states are the proper prefixes of the codewords and whose transitions return to the empty prefix whenever a codeword is completed, has exactly \(2^m\) states. Its exact reset threshold is
\[
\boxed{\operatorname{rt}(A_m)=m^2.}
\]
An explicit shortest reset word is
\[
\boxed{w_m=(0\,1^m)^{m-1}0.}
\]
Here a reset word maps **every** decoder state to the same state. In fact \(w_m\) maps them all to the root. The code is obtained by expanding just one leaf of the full depth-\(m\) binary tree; the unrefined equal-length code has no reset word for \(m\ge2\). The formula therefore quantifies the resynchronization created by this minimal length perturbation.

## Assumptions and scope
The alphabet is exactly \(\Sigma=\{0,1\}\), concatenation is juxtaposition, \(1^j\) denotes a run of \(j\) ones, and the parameter \(m\) is an arbitrary integer at least two. Every proper prefix of a word of \(X_m\) is a state; thus
\[
Q_m=\bigcup_{h=0}^{m-1}\Sigma^h\ \cup\ \{1^m\},\qquad |Q_m|=2^m.
\]
Writing \(\varepsilon\) for the empty prefix, the total transition function is
\[
\delta(s,c)=\begin{cases}
\varepsilon,&sc\in X_m,\\
sc,&sc\text{ is a proper prefix of an element of }X_m,
\end{cases}
\]
for all \(s\in Q_m\) and \(c\in\Sigma\). Both cases are exhaustive because \(X_m\) is complete. The reset threshold is the minimum length of a word mapping all of \(Q_m\) to a singleton (without prescribing that singleton). The result is about the literal decoder, **not** the minimized DFA recognizing \(X_m^*\).

## Proof
**Upper bound and explicit trajectory.** Put \(F=0\,1^m\), of length \(m+1\). For any proper-prefix state \(s\) with \(|s|=h\le m-2\), reading the initial zero and then the next \(m-h-1\) ones finishes a normal length-\(m\) codeword, leaving \(h+1\) ones. Hence \(\delta(s,F)=1^{h+1}\). If \(|s|=m-1\), the first zero finishes a normal codeword, and the trailing \(m\) ones leave state \(1^m\). The same final state results when \(s=1^m\), since that zero finishes a long codeword. Therefore
\[
\delta(Q_m,F)=\{1,1^2,\ldots,1^m\},\qquad
\delta(1^h,F)=1^{\min(h+1,m)}\quad(1\le h\le m).
\]
Iteration gives \(\delta(Q_m,F^{m-1})=\{1^{m-1},1^m\}\), and appending zero finishes the relevant codeword from both states. Thus \(w_m=F^{m-1}0\) resets to \(\varepsilon\) in length \((m+1)(m-1)+1=m^2\).

**A modular lower bound.** Let \(w\) be any reset word of length \(L\), and write \(f\in\{0,1,\ldots,m\}\) for the length of its common final decoder state. For each \(h\in\{0,1,\ldots,m-1\}\), run \(w\) from the state \(0^h\), with \(0^0=\varepsilon\). The combined string \(0^h w\) admits a unique greedy parsing into complete codewords followed by the common final proper prefix. Let \(K_h\) count all completed codewords and \(E_h\) count those of length \(m+1\). Since every other codeword has length \(m\),
\[
L+h=mK_h+E_h+f,\qquad E_h\equiv L+h-f\pmod m.
\]
As \(h\) traverses the \(m\) possible values, these residues traverse all classes modulo \(m\). Hence some \(h_*\) has \(E_{h_*}\ge m-1\).

If \(h_*\ge1\), the initial prefix \(0^{h_*}\) forces the **first** completed codeword to have length exactly \(m\) (because it contains a zero); it consumes \(m-h_*\) symbols of \(w\). The subsequent \(E_{h_*}\) long codewords consume at least \((m+1)(m-1)\) further input symbols. It follows that
\[
L\ge(m-h_*)+(m+1)(m-1)+f\ge m^2.
\]
Thus any hypothetical reset word with \(L<m^2\) must have \(h_*=0\). Applying the same length accounting at the root gives \(L\ge(m+1)(m-1)+f=m^2-1+f\). Consequently the **only possible** shorter reset word has \(L=m^2-1\), \(f=0\), exactly \(m-1\) long codewords and no normal codeword when parsed from the root. Necessarily
\[
w=(1^m c_1)(1^m c_2)\cdots(1^m c_{m-1}),\qquad c_j\in\{0,1\}.
\]

Now parse \(w\) starting from decoder state \(0\). Since the first input symbols are ones, the initial normal codeword \(0\,1^{m-1}\) completes after \(m-1\) symbols. Exactly \(m(m-1)\) input symbols remain. The congruence for \(h=1\) and \(L=m^2-1,f=0\) gives \(E_1\equiv0\pmod m\). Having \(E_1\ge m\) would use at least \(m(m+1)\) symbols after that first normal codeword, which is impossible. Hence \(E_1=0\). The remaining input must divide into exactly \(m-1\) normal codewords, each of length \(m\).

The \(j\)-th such length-\(m\) block, for \(1\le j\le m-1\), occupies original input positions \(jm,\ldots,(j+1)m-1\) (one-based). It contains precisely one character not prescribed to be one, namely \(c_j\), at position \(j(m+1)\). To be a normal codeword rather than the exceptional prefix \(1^m\), it must have \(c_j=0\). Therefore every \(c_j=0\), leaving only
\[
w=(1^m0)^{m-1}.
\]
However, from state \(1\), one block \(1^m0\) ends at state \(0\), and, whenever \(0\le r\le m-3\), a further block maps \(1^r0\) to \(1^{r+1}0\). Thus the complete word ends at \(1^{m-2}0\) from state \(1\), while it ends at \(\varepsilon\) from the root. (At \(m=2\), the first block already leaves state \(0\).) These states differ. This contradiction excludes \(L<m^2\), proving the theorem.

## Verification
The standalone executable file `CHECK.py` constructs the complete literal decoder from its proper-prefix states. For each \(2\le m\le9\), it performs breadth-first search of the reachable subset automaton until the first singleton image, verifies that the shortest length equals \(m^2\), tests the explicit resetting word, and checks the exact images of every power \(F^j\) with \(1\le j<m\). Its recorded output is `CHECK_OUTPUT.txt`. These finite tests independently check the small cases; the proof above establishes all \(m\).

## Relationship to prior work
Ryzhikov and Szykuła (2018, arXiv:1806.06299, especially Sections 1 and 7) study shortest reset words for literal prefix-code decoders, supply approximation methods, and conjecture a polynomial-time exact algorithm. Their displayed complete code \(0\Sigma^{m-1}\cup1\Sigma^m\) refines an entire subtree, not a single leaf, and their results do not state the threshold above. Berlinkov, Ferens, Ryzhikov, and Szykuła (arXiv:2101.05057, first publicly available 2021; journal 2026, Sections 1.4 and 3.8) prove general \(O(n\log^3 n)\)-type bounds for finite prefix-code literal automata, without a per-family exact threshold for this one-leaf refinement. Szykuła's 2026 open-problems survey (arXiv:2608.24245, first public 2026-08-25) provides the contemporary reset-threshold context. The 2009 Biskup–Plandowski work reports two families with long synchronization delays; its detailed constructions were not accessible for direct comparison, and possible unrecognized coverage is an originality risk.

## Limitations
The claim is only about the specified binary tree with the leaf \(1^m\) refined, and the literal—not minimized—decoder. It does not classify other leaf choices or prove a new general upper bound. The code has \(2^m\) decoder states, so the reset length is quadratic in the codeword depth but logarithmic-squared in the state count. Historical priority for unindexed and inaccessible earlier constructions has not been independently resolved, particularly for Biskup–Plandowski (2009). No independent scientific audit has been performed.

## References
1. M. Szykuła, *Synchronizing Automata: Open Problems*, arXiv:2608.24245, 2026-08-25; doi:10.4204/EPTCS.451.3.
2. A. Ryzhikov and M. Szykuła, *Finding Short Synchronizing Words for Prefix Codes*, arXiv:1806.06299, 2018; doi:10.4230/LIPIcs.MFCS.2018.21.
3. M. V. Berlinkov, R. Ferens, A. Ryzhikov, and M. Szykuła, *Synchronization of strongly connected partial DFAs and prefix codes*, arXiv:2101.05057, first public 2021; doi:10.46298/dmtcs.16465, 2026.
4. M. T. Biskup and W. Plandowski, *Shortest synchronizing strings for Huffman codes*, Theoretical Computer Science 410 (2009), 3925–3941; doi:10.1016/j.tcs.2009.06.005 (abstract and bibliographic information inspected; full text not accessible).
