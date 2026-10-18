# Exact two-cycle census for simultaneous knowing-whether on S5 matching cycles

## Finding

Let \(m\ge1\), \(W_m=\mathbb Z/(2m)\), and give \(W_m\) two \(\mathrm{S5}\) agents whose equivalence-class partitions consist of the alternating perfect matchings \(E_i=\{2i,2i+1\}\) and \(F_i=\{2i+1,2i+2\}\). For an event \(X\subseteq W_m\), write \(\Delta_E(X)\) (respectively \(\Delta_F(X)\)) for the truth set of the formula saying that the corresponding agent knows whether \(X\) holds. Consider simultaneous evaluation
\[
H(X)=\Delta_E(X)\cap\Delta_F(X).
\]
Let \(a_m=|\{X\subseteq W_m:H^2(X)=X\}|\), the number of events of temporal period dividing two. If \(\alpha_1,\alpha_2,\alpha_3\) are the complex roots of \(z^3-z-1\) and \(\beta_1,\beta_2,\beta_3\) those of \(z^3+z+1\), with multiplicities, then
\[
a_m=1+\sum_{j=1}^{3}\alpha_j^{2m}+\sum_{j=1}^{3}\beta_j^{2m}\quad(m\ge1).
\]
There is exactly one fixed event, \(W_m\); consequently the number of unordered orbits of exact period two is \((a_m-1)/2\). For \(m=1,2,3,4,5,6,7,8\), the exact event counts are \(1,5,7,5,31,11,71,85\). In particular, two-world frames have no genuine two-cycle, whereas four-world frames have two.

## Assumptions and scope

Events are arbitrary Boolean valuations of one proposition on the specified finite labeled carrier. The operators are ordinary Kripke knowing-whether operators on equivalence frames: \(w\in\Delta_G(X)\) iff \([w]_G\subseteq X\) or \([w]_G\cap X=\varnothing\). Both agents evaluate the same input event before intersection; this is not sequential composition or a public-announcement update. All counts distinguish labels and do not quotient by graph symmetries. Temporal period two refers to repeated application of the global event transformer \(H\), and not to alternation of spatial cellular-automaton rules.

## Proof

**Reduction to a radius-one map.** Identify \(X\) with its cyclic Boolean word \(x_0,\ldots,x_{2m-1}\). At vertex \(i\), the two agents inspect the pairs \(\{i-1,i\}\) and \(\{i,i+1\}\), in some order. Thus the output word \(h(x)\) satisfies
\[
h(x)_i=1\quad\Longleftrightarrow\quad x_{i-1}=x_i=x_{i+1},
\]
with all indices cyclic. This is the classical local rule numbered \(129\) in Wolfram notation; the identification is not an assertion of novelty for the local cellular-automaton rule.

**A finite presentation of period-two events.** Write a five-bit block as \(b=(b_0,b_1,b_2,b_3,b_4)\) and set \(u_j(b)=1\) exactly when \(b_j=b_{j+1}=b_{j+2}\), for \(j=0,1,2\). The central bit is unchanged after two applications if and only if
\[
b_2=\mathbf1\{u_0(b)=u_1(b)=u_2(b)\}.
\]
Of the \(32\) five-bit blocks, exactly \(16\) satisfy this condition. Define the \(16\times16\) integer matrix \(M\), with rows and columns indexed by four-bit words, by
\[
M_{(b_0,b_1,b_2,b_3),(b_1,b_2,b_3,b_4)}
=\mathbf1\{b_2=\mathbf1\{u_0(b)=u_1(b)=u_2(b)\}\},
\]
where a matrix entry is the sum of these indicators over possible compatible five-bit blocks (at most one). A cyclic word of length \(n\) satisfies \(h^2(x)=x\) if and only if each of its length-five cyclic windows is admissible. Sending such a word to its successive overlapping four-bit windows gives a bijection with closed walks of length \(n\) in the matrix graph, including \(n<5\) because cyclic indexing specifies repeated digits. Therefore
\[
|\{x\in\{0,1\}^n:h^2(x)=x\}|=\operatorname{tr}(M^n)\quad(n\ge1).
\]

**Characteristic polynomial.** Direct exact integer expansion of \(\det(zI-M)\) from the indicated \(16\)-state matrix gives
\[
\det(zI-M)=z^9(z-1)(z^3-z-1)(z^3+z+1).
\]
This identity does not depend on observed numerical terms: the standalone verifier constructs \(M\) from the admissibility predicate and independently computes the characteristic polynomial using the integer Newton trace identities, with exact division at each coefficient. The standard eigenvalue trace identity gives \(\operatorname{tr}(M^n)=1+\sum_j\alpha_j^n+\sum_j\beta_j^n\) for every positive \(n\). Apply it to \(n=2m\).

**Fixed events.** If \(h(x)=x\) and some bit equals one, the displayed local rule forces both its neighbors to equal one; connectedness of the cyclic graph forces all bits to be one. If no bit equals one, then \(x\) is all zero, but \(h(x)\) is all one, a contradiction. Hence the all-one event is the unique fixed event. Every other element of the finite set \(\{x:h^2(x)=x\}\) belongs to a two-cycle; dividing its cardinality minus one by two proves the orbit count.

## Verification

Run `python3 verify_period2.py` with a standard Python 3 interpreter. The script builds the \(16\times16\) integer transfer matrix from all \(32\) local blocks, checks exactly \(16\) admitted blocks, reconstructs the full characteristic polynomial through exact Newton trace identities, and compares \(\operatorname{tr}(M^{2m})\) with a completely direct census of every Boolean valuation for \(m=1,\ldots,8\). It independently checks that the Kripke two-agent conjunction equals the local unanimity rule on all \(87{,}380\) valuations and that exactly one fixed valuation occurs. The expected counts are \(1,5,7,5,31,11,71,85\). The proof establishes the all-\(m\) result; finite exhaustion is corroboration, not an extrapolation argument.

## Relationship to prior work

Wang and Zenger (2026) develop proof theory for non-contingency, the modal operator interpreted as knowing whether. Fan et al. (2020/2021) analyze commonly knowing whether and explicitly treat nested multi-agent formulas, but their examined results concern logical expressivity and axiom systems, not a finite-cycle two-period census. Ganikhodjaev, Saburov, and Mohamad Asimoni (2016) study spatially period-two cellular automata, meaning automata commuting with the square of the spatial shift; that is a different use of “period two” from temporal solutions of \(h^2(x)=x\), even though their examples use rule \(129\). Known databases also record the evolution of a single seed under rule \(129\), which is not a census of all cyclic events of bounded temporal period. The local rule, the transfer-matrix method, and the cubic polynomials themselves are not claimed as new independently; the claimed result is their exact joint enumeration in the specified modal frame family.

## Limitations

The census applies to the alternating matching-cycle frames, to Boolean propositions, and to periods dividing two only. It does not enumerate longer periods, arbitrary \(\mathrm{S5}\) frames, or non-Boolean semantics. Further comparison with specialized cellular-automaton periodic-point literature may reveal an earlier equivalent formulation; this remains an originality risk. The 2026 motivating preprint could be inspected at the bibliographic/abstract level but not in full text during this assessment, so no whole-document noncoverage claim about that work is made.

## References

1. Y. Wang and L. Zenger, *Proof Theory for Non-Contingency Logic*, arXiv:2609.38975 (first posted 2026-09-30).
2. J. Fan, D. Grossi, B. Kooi, X. Su, and R. Verbrugge, *Commonly Knowing Whether*, arXiv:2001.03945 (2020), ICLA 2021 proceedings, pp. 55–59.
3. J. Fan, Y. Wang, and H. van Ditmarsch, *Contingency and Knowing Whether*, Review of Symbolic Logic 8 (2015), 75–107, DOI:10.1017/S1755020314000343.
4. N. Ganikhodjaev, M. Saburov, and N. R. Mohamad Asimoni, *Periodic Cellular Automata of Period-2*, Malaysian Journal of Mathematical Sciences 10(S) (2016), 131–142.
5. OEIS A267440 and A267441: single-seed evolution for elementary cellular automaton rule \(129\) (background, not a period-two census).
