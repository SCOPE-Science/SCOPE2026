# Positive critical periodic content for the \(\{\rho,\rho^2\}\) contraction pair
## Finding
Let \(\mathcal F=\{f_0,f_1\}\) be a self-similar iterated function system on \(\mathbb R^d\) satisfying the strong separation condition, with contraction ratios
\[
r_0=\rho,\qquad r_1=\rho^2,\qquad 0<\rho<1.
\]
Write \(E_{\mathcal F}\) for its attractor, \(T_{\mathcal F}\) for the inverse expanding map, and \(s=s_{\mathcal F}\) for the similarity dimension, so
\[
\rho^s+\rho^{2s}=1.
\]
Then
\[
\mathfrak P^s(E_{\mathcal F},|\cdot|,T_{\mathcal F})>0.
\]
In fact, if
\[
\delta_{\mathcal F}:=\operatorname{dist}\bigl(f_0(E_{\mathcal F}),f_1(E_{\mathcal F})\bigr)>0,
\qquad \varphi:=\frac{1+\sqrt5}2,
\]
and \(F_k\) is the Fibonacci sequence normalized by \(F_1=F_2=1\), then for each \(n\ge2\) there is a primitive periodic point \(x_n\) satisfying
\[
\#\mathcal O_{x_n}=F_{n+1},
\qquad
\eta(\mathcal O_{x_n})\ge \delta_{\mathcal F}\rho^{n-1}.
\]
Therefore
\[
\liminf_{n\to\infty}\#\mathcal O_{x_n}\,\eta(\mathcal O_{x_n})^s
\ge
\delta_{\mathcal F}^s\frac{\varphi^2}{\sqrt5}>0.
\]
This gives an affirmative answer to the recent inhomogeneous critical-content question for the natural first commensurable non-homogeneous contraction pair \(\{\rho,\rho^2\}\).

## Assumptions and scope
The result applies in every ambient dimension and permits arbitrary orthogonal parts and translations, subject only to the strong separation condition and the two contraction ratios \(\rho\) and \(\rho^2\). It does not claim the corresponding statement for arbitrary inhomogeneous contraction vectors.

Let \(\Sigma=\{0,1\}^{\mathbb N}\). The symbolic metric associated with \(\mathcal F\) is
\[
d_{\mathcal F}(\mathbf i,\mathbf j)=r_{\mathbf i\wedge\mathbf j}.
\]
For the present ratios this equals \(\rho^{W(\mathbf i\wedge\mathbf j)}\), where symbol \(0\) has weight \(1\) and symbol \(1\) has weight \(2\). The coding map from \(\Sigma\) to \(E_{\mathcal F}\) is bi-Lipschitz under the strong separation condition; in particular,
\[
|\pi(\mathbf i)-\pi(\mathbf j)|\ge \delta_{\mathcal F}d_{\mathcal F}(\mathbf i,\mathbf j).
\]

## Proof
Fix \(n\ge2\). Consider cyclic binary words of length \(n\) having no adjacent pair \(11\), including across the cyclic boundary. These are exactly the period-\(n\) words of the Golden-Mean shift.

Construct a directed overlap graph whose edges are those cyclically admissible length-\(n\) words and whose vertices are their length-\((n-1)\) prefixes and suffixes. For a vertex \(v=v_1\cdots v_{n-1}\), an appended bit \(a\) gives an outgoing edge precisely when the resulting word is cyclically admissible. The bit \(a=1\) is allowed exactly when \(v_1=v_{n-1}=0\); otherwise only \(a=0\) is allowed. The same criterion governs incoming edges, so every vertex has equal indegree and outdegree. Appending zeros repeatedly gives a path from every vertex to \(0^{n-1}\), and starting at \(0^{n-1}\) and appending the symbols of any target vertex gives a path to that target. Hence the graph is strongly connected and Eulerian.

An Eulerian circuit therefore gives a cyclic Golden-Mean de Bruijn word \(B_n\): every cyclically admissible binary word of length \(n\) occurs exactly once as a cyclic factor. In particular, all length-\(n\) factors starting at distinct bit positions of \(B_n\) are distinct.

Parse \(B_n\) cyclically using the variable-length code
\[
0\longmapsto 0,
\qquad
1\longmapsto 10.
\]
The parsing is unique: every binary \(1\) must be paired with the following \(0\), and every remaining \(0\) forms a singleton codeword. Let \(w_n\) be the resulting cyclic word over the original two-symbol alphabet. The number of codewords is the number of zeroes in \(B_n\). Because each bit position of \(B_n\) corresponds to one distinct cyclically admissible length-\(n\) factor, the zero positions are in bijection with cyclically admissible length-\(n\) words whose first bit is \(0\). Removing that first zero leaves an arbitrary linear binary word of length \(n-1\) with no adjacent ones, of which there are \(F_{n+1}\). Thus
\[
|w_n|=F_{n+1}.
\]

The cyclic word \(w_n\) is primitive. Otherwise its binary expansion would give \(B_n\) a nontrivial cyclic period, forcing two different bit positions of \(B_n\) to have the same length-\(n\) factor, contrary to the de Bruijn property. Hence the periodic symbolic point \(\mathbf w_n=w_n^\infty\) has orbit cardinality exactly \(F_{n+1}\).

Take two distinct points in this symbolic orbit. They start at two distinct codeword-boundary positions of \(B_n\). If their common original-symbol prefix had total weight at least \(n\), then the binary expansions of those prefixes would agree for at least their first \(n\) bits. That would give the same length-\(n\) cyclic factor of \(B_n\) at two distinct positions, again impossible. Therefore the common-prefix weight is at most \(n-1\), and
\[
\eta\bigl(\mathcal O_{\mathbf w_n}\bigr)\ge \rho^{n-1}
\]
in the symbolic metric.

Project by the coding map \(\pi\). The conjugacy preserves orbit cardinality, while the lower bi-Lipschitz estimate gives
\[
\eta\bigl(\mathcal O_{\pi(\mathbf w_n)}\bigr)
\ge
\delta_{\mathcal F}\rho^{n-1}.
\]
Set \(x_n=\pi(\mathbf w_n)\).

Finally, if \(\varphi=(1+\sqrt5)/2\), then \(t=\rho^s\) is the positive root of \(t+t^2=1\), so \(\rho^s=\varphi^{-1}\). Binet's formula gives
\[
F_{n+1}\varphi^{-(n-1)}\longrightarrow \frac{\varphi^2}{\sqrt5}.
\]
Consequently
\[
\liminf_{n\to\infty}
\#\mathcal O_{x_n}\,\eta(\mathcal O_{x_n})^s
\ge
\delta_{\mathcal F}^s\frac{\varphi^2}{\sqrt5}>0.
\]
The periodic-content characterization from the primary source then yields \(\mathfrak P^s(E_{\mathcal F},|\cdot|,T_{\mathcal F})>0\).

## Verification
The proof is infinite and does not rely on finite enumeration. A standard-library checker, `artifacts/verify_golden_mean.py`, independently constructs the Eulerian Golden-Mean de Bruijn cycles for \(2\le n\le10\), verifies that every cyclically admissible length-\(n\) word occurs exactly once, checks that the parsed orbit length is \(F_{n+1}\), confirms primitivity, and confirms the claimed common-prefix bound. It prints `VERIFY_OK` on success.

The source's symbolic metric and its lower coding estimate were checked directly against Lemma 3.2. The source's Theorem 2.3 was checked for the equivalence between positive periodic content and a periodic-orbit sequence with positive lower normalized gap.

## Relationship to prior work
Kong, Wang and Yu introduced periodic content and proved that for a self-similar IFS satisfying strong separation, the periodic dimension equals the similarity dimension. They prove positive critical periodic content in the homogeneous case by ordinary de Bruijn cycles, but explicitly state that positivity at the critical dimension is unknown for inhomogeneous systems and pose this as Question 5.1. Their inhomogeneous proof establishes only the subcritical statement by approximating with homogeneous subsystems.

The present argument replaces ordinary fixed-length de Bruijn words by a Golden-Mean universal cycle adapted to the weights \(1\) and \(2\). Restricted-language de Bruijn cycles have an established combinatorial literature; Moreno's work treats de Bruijn sequences for restricted languages and subshifts of finite type. The new step here is the weighted coding back to the inhomogeneous self-similar symbolic metric and the exact critical normalization.

## Limitations
The proof is specific to the contraction pair \(\rho,\rho^2\). It does not establish positivity for arbitrary commensurable ratios \(\rho^{a_i}\), because a naive expansion to a general variable-length edge shift need not inherit the balanced universal-cycle structure used above. It also does not address incommensurable contraction ratios. The originality assessment cannot exclude an unindexed or subsequently posted independent solution of this special case.

## References
1. D. Kong, Z. Wang and D. Yu, *Asymptotic separation of periodic orbits and fractal dimension*, arXiv:2609.16296v1, first posted 2026-09-14.
2. E. Moreno, *De Bruijn sequences and De Bruijn graphs for a general language*, Information Processing Letters 96 (2005), 214-219, DOI 10.1016/j.ipl.2005.05.028.
