# Exact labeled and state-isomorphism enumerators of binary bireversible Mealy transducers

## Finding

**Theorem (binary bireversible census).** Let \(n\geq 1\). Consider complete deterministic Mealy transducers with the **fixed, ordered** input and output alphabet \(\{0,1\}\), labeled states \(Q=\{1,\ldots,n\}\), no distinguished starting state, and a permutation of the output alphabet at each state. Write \(\delta_x\colon Q\to Q\) for the state transition upon input \(x\). A transducer is *bireversible* when the input transitions are permutations and the inverse Mealy transducer also has permutation input transitions. A transducer is *connected* when its underlying transition digraph is strongly connected.

There is a bijective normal form consisting of \(d\in S_n\), \(\pi\in S_n\), and a subset \(A\subseteq Q\) fixed setwise by \(\pi\):
\[
\delta_1=d,\qquad \delta_0=d\circ\pi,\qquad
A=\{q:\text{the state }q\text{ swaps }0\text{ and }1\}.
\]
For every \(0\leq k\leq n\), exactly \((n!)^2\) labeled bireversible transducers have \(|A|=k\). Thus there are \((n+1)(n!)^2\) in total.

Let \(U_n(t)\) count isomorphism classes under **simultaneous state relabeling alone**, weighted by \(t^{|A|}\). For a partition \(\lambda\vdash n\), let \(m_j(\lambda)\) be the multiplicity of parts of size \(j\). Then the exact all-length polynomial is
\[
U_n(t)=\sum_{\lambda\vdash n}\prod_{j\geq1}
 j^{m_j(\lambda)}m_j(\lambda)!\left(\sum_{h=0}^{m_j(\lambda)}t^{jh}\right).
\]
Only nonzero multiplicities contribute. In particular, the number of unweighted classes is
\[
U_n(1)=\sum_{\lambda\vdash n}\prod_{j\geq1}j^{m_j(\lambda)}(m_j(\lambda)+1)!.
\]

The corresponding exact connected enumerators are obtained without further case distinctions. With all expressions interpreted as **formal power series**, put
\[
F(z,t)=\sum_{n\geq0}n!\left(\sum_{k=0}^{n}t^k\right)z^n,
\qquad U(z,t)=1+\sum_{n\geq1}U_n(t)z^n.
\]
The coefficient of \(z^nt^k\) in \(n!\log F(z,t)\) is the number of **labeled connected** transducers with \(n\) states and \(k\) swapping states. The coefficient in
\[
V(z,t)=\sum_{r\geq1}\frac{\mu(r)}{r}\log U(z^r,t^r)
\]
is the number of **connected state-isomorphism classes** of that size and output type. Here \(\mu\) is the ordinary number-theoretic Möbius function. If a labeled transducer is drawn uniformly from all \((n+1)(n!)^2\) bireversible ones, then
\[
\Pr(\text{connected})=1-\frac{2}{n}+O(n^{-2})
\qquad(n\to\infty).
\]

For \(n=1,2,3,4,5,6\), the numbers of labeled connected transducers are respectively \(2,8,88,1776,55488,2446080\). The numbers of connected state-isomorphism classes are \(2,7,20,94,472,3550\). Both sequences are consequences of the all-length formulas, not extrapolations from experiments.

## Assumptions and scope

The alphabet has exactly two **distinct, fixed** letters, both for input and for output. State labels are fixed when counting labeled objects; the only equivalence in \(U_n\) and \(V\) is a common permutation of source and target state names. Alphabet relabeling, separate source/target state relabeling (isotopism), behavioral minimization, and identification of automata generating isomorphic groups are **not** included. There is no distinguished initial state. All transducers are complete. Connectedness refers to the state graph, not to transitivity on finite or infinite input words.

The index \(n=0\) in \(F\) and \(U\) is a formal empty-object term, not an additional counted transducer. The case \(n=1\) is included in every stated identity.

## Proof

**1. The bireversible normal form.** At state \(q\), the output permutation is either the identity or the swap; write its swap bit as \(\epsilon(q)\). For output letter \(y\), the incoming transition function of the inverse machine is
\[
q\longmapsto \delta_{y\oplus\epsilon(q)}(q).
\]
Under the two input-transition permutation hypotheses, this is bijective for both values of \(y\) exactly when \(\delta_0(A)=\delta_1(A)\). Indeed, for output zero its image is \(\delta_1(A)\cup\delta_0(Q\setminus A)\); because both \(\delta_x\) are permutations, this is a disjoint cover of \(Q\) precisely when the indicated images of \(A\) coincide. The output-one case is equivalent. Taking \(d=\delta_1\) and \(\pi=d^{-1}\circ\delta_0\), the condition becomes \(\pi(A)=A\), proving the claimed bijection.

**2. Labeled enumeration and the flat output-type law.** Fix \(k\) and first choose \(A\) in \(\binom nk\) ways. The arbitrary permutation \(d\) has \(n!\) choices. The permutation \(\pi\) preserving \(A\) has \(k!(n-k)!\) choices. Multiplication gives exactly \((n!)^2\), independent of \(k\).

**3. State-isomorphism enumerator.** Fix a state relabeling \(\sigma\in S_n\), having \(m_j\) cycles of size \(j\) and centralizer size \(z_\lambda=\prod_jj^{m_j}m_j!\). The pair \((d,\pi)\) is fixed precisely when both permutations commute with \(\sigma\), and \(A\) must be invariant under \(\sigma\) and \(\pi\). Once \(\pi\) is specified, \(d\) has \(z_\lambda\) choices.

A permutation \(\pi\) commuting with \(\sigma\) permutes its \(m_j\) cycles of each length \(j\) by some \(\tau_j\in S_{m_j}\), with exactly \(j^{m_j}\) lifts of each \(\tau_j\). The orbits of \(\langle\sigma,\pi\rangle\) are exactly the unions of the \(\sigma\)-cycles in one cycle of \(\tau_j\); an orbit associated to a \(\tau_j\)-cycle of length \(h\) has \(jh\) states. Therefore the choices for \(A\) contribute \(\prod_{C\in\mathrm{cyc}(\tau_j)}(1+t^{j|C|})\).

For every nonnegative \(m\) and indeterminate \(s\), double-counting permutation-invariant subsets gives
\[
\sum_{\tau\in S_m}\prod_{C\in\mathrm{cyc}(\tau)}(1+s^{|C|})
=m!\sum_{h=0}^{m}s^h:
\]
for each fixed subset size \(h\), the number is \(\binom mh h!(m-h)!=m!\). Summing over the conjugacy classes of \(\sigma\) in Burnside's lemma cancels the factor \(z_\lambda\) against the conjugacy-class denominator. The displayed formula for \(U_n(t)\) follows.

**4. Connected decompositions.** Since both \(\delta_0\) and \(\delta_1\) are permutations, their common orbits are exactly the strongly connected components of the transition digraph. Every component inherits its output bits, and a disjoint union of connected bireversible transducers is again bireversible. Thus labeled transducers form the labeled SET construction on their connected components; the weighted exponential formula gives \(\log F(z,t)\). With state labels suppressed, an object is a multiset of connected isomorphism classes. Consequently
\[
U(z,t)=\prod_{n\ge1}\prod_{k=0}^{n}(1-z^nt^k)^{-v_{n,k}},
\]
where \(v_{n,k}\) is the connected isomorphism-class count. Taking logarithms and applying Möbius inversion yields the asserted \(V(z,t)\).

**5. Connectedness asymptotic.** Uniformly among labeled bireversible transducers, \(d\) is uniform on \(S_n\), independently of \(\pi\), while \(\pi\) has probability proportional to \(2^{c(\pi)}\), where \(c(\pi)\) is its number of cycles. The normalization is \(\sum_{\pi\in S_n}2^{c(\pi)}=(n+1)!\). For \(1\le j\le n-1\), the expected number of \(j\)-subsets simultaneously invariant under \(d\) and \(\pi\) is
\[
E_j=\frac{(j+1)(n-j+1)}{(n+1)\binom nj}.
\]
To see this, a fixed \(j\)-set is fixed by \(d\) with probability \(\binom nj^{-1}\); the weighted probability that \(\pi\) preserves it is \((j+1)!(n-j+1)!/(n+1)!\). In particular, \(E_1=2/(n+1)\), \(E_2=6/(n(n+1))\), and \(E_{j+1}/E_j=(j+2)/(n-j+1)\). For \(2\le j\le\lfloor n/2\rfloor\), the sum of \(E_j\) is \(O(n^{-2})\): the \(j=2\) term is of that order, the \(j=3\) term is \(O(n^{-3})\), and the remaining at most \(n\) terms are no larger than \(E_3\) for sufficiently large \(n\). If disconnected, there is an invariant component of size at most \(n/2\), so the union bound gives \(\Pr(\mathrm{disconnected})\le2/(n+1)+O(n^{-2})\). Conversely, if \(N_1\) counts invariant singletons, then \(\mathbb E N_1=2/(n+1)\) and \(\mathbb E\binom{N_1}{2}=2/(n(n+1))\), by directly requiring two named states to be fixed by both permutations. The second-order Bonferroni bound gives \(\Pr(N_1\ge1)\ge2/(n+1)-O(n^{-2})\). Therefore \(\Pr(\mathrm{disconnected})=2/(n+1)+O(n^{-2})\), proving the asymptotic statement.

## Verification

The standalone Python 3 program `verify.py` uses only the standard library and does not assume the normal form to test bireversibility. It directly enumerates transition permutations and every swap-bit assignment for all \(1\le n\le5\), tests the inverse transition maps by output letter, and tests connectedness by graph reachability. For \(n\le4\) it independently canonicalizes all qualifying machines under every state relabeling, checking the Burnside formula and connected-isomorphism coefficients. Independently, exact integer and rational recurrences check labeled connected coefficients through \(n=12\) and unlabelled connected coefficients through \(n=10\). Executing `python3 verify.py` prints `VERIFY_OK`; its captured output is in `verification_output.txt`. `enumeration_table.csv` gives first exact counts. These finite checks corroborate the separate all-length proof; they are not used as an infinite proof.

## Relationship to prior work

Curtin and Savchuk's 2026 framework relates bireversible automata to orthogonal matrix pairs, Latin-square-like data, and isotopisms. It motivates considering complete enumerators of the special two-letter case. The available abstract and detailed review describe structural correspondences, not the precise state-relabeling orbit polynomials, connected-component generating functions, or connectedness asymptotic above. Its full 57-page primary text was unavailable for direct comparison; publication priority therefore remains subject to that specifically identified risk.

Woryna (2017) classifies groups generated by **two-state** bireversible automata over changing alphabets, which is not a census of transducers with **two input letters** and arbitrary state count. Godin and Klimann (2016) address group-theoretic consequences of connected reversible automata, not all-length enumerators. The GAP FR package documentation independently tabulates twelve labeled bireversible two-state, two-letter machines, agreeing with the \(n=2\) specialization. Its eight equivalence classes quotient by both state and alphabet permutations; the theorem deliberately fixes the alphabet and gives ten state-only classes. These small-machine tables do not supply the all-length formulas. The Burnside and labeled/unlabeled SET tools used in the derivation are classical; the specific binary normal form and combined refined enumerators are the asserted result.

## Limitations

The counts concern syntactic transducers, including ones with redundant or behaviorally equivalent states. Neither minimization nor the isomorphism type of the generated automaton group is classified. There is no corresponding result here for larger alphabets or state-and-alphabet isotopism classes. The asymptotic is for the uniform distribution on **all labeled** transducers and is not claimed for the uniform distribution on isomorphism classes. The 2026 motivating primary PDF could not be inspected in full; unindexed equivalent enumerations or formulae embedded in that paper are residual novelty risks. Independent external validation has not been performed.

## References

1. B. Curtin and D. Savchuk, *Combinatorial structures connecting Latin squares and bireversible automata*, arXiv:2607.26013v1 (first public submission 2026-07-28). https://arxiv.org/abs/2607.26013
2. A. Woryna, *On groups generated by bi-reversible automata: The two-state case over a changing alphabet*, Journal of Computer and System Sciences 86 (2017), 181–190. https://doi.org/10.1016/j.jcss.2017.01.004
3. T. Godin and I. Klimann, *Connected Reversible Mealy Automata of Prime Size Cannot Generate Infinite Burnside Groups*, MFCS 2016. https://arxiv.org/abs/1604.03270
4. The GAP FR package, *Functionally recursive groups*, Section 5.1.4 and accompanying tests, documenting bireversible binary two-state counts. https://fossies.org/linux/gap/pkg/fr/tst/chapter-5-b.tst
5. D. D'Angeli and collaborators, *On the Finiteness Problem for Automaton (Semi)Groups* (2012). https://www.researchgate.net/publication/51892951_ON_THE_FINITENESS_PROBLEM_FOR_AUTOMATON_SEMIGROUPS
