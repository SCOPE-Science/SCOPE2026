# Sharp \(2m+2\)-world modal mirages: rigid normal forms and exact extremal counts

## Finding

For every integer \(m\geq 1\), consider the variable-free modal formulas
\[
\alpha_0=\top,\qquad \alpha_{j+1}=\Box\Diamond\alpha_j.
\]
Over all nonempty finite **arbitrary** Kripke frames (normal modal logic \(\mathsf K\)), the minimum number of worlds in a frame having a world satisfying \(\alpha_m\) but not \(\alpha_{m+1}\) is exactly
\[
\boxed{2m+2}.
\]
Every separating frame of this minimum size has a **unique** separating world, is rigid (has no nonidentity automorphism), and contains a spanning directed path of length \(2m+1\). Its relation has the complete normal form below. Put
\[
E_m=2m^2+2m+1,\qquad n_m=2m+2.
\]
There are exactly \(2^{E_m}\) isomorphism types, \(n_m!\,2^{E_m}\) binary accessibility relations on a fixed labelled \(n_m\)-element carrier that separate the formulas somewhere, and \((n_m-1)!\,2^{E_m}\) relations that separate them at a preselected world. The exact edge-count polynomial for labelled minimal separators is
\[
\boxed{n_m!\,z^{2m+1}(1+z)^{E_m}}.
\]
In particular, for \(m=1,2\) the unlabelled counts are \(32\) and \(8192\), and the labelled counts are \(768\) and \(5{,}898{,}240\).

## Assumptions and scope

A frame is a pair \(F=(W,R)\) with \(W\) finite and nonempty and \(R\subseteq W\times W\) arbitrary. Loops and dead ends are allowed. Write \(R(w)=\{v:wRv\}\). As the formulas contain no propositional variables, their truth values do not depend on any valuation. Let
\[
A_j=\{w\in W:F,w\models\alpha_j\},\qquad
N_j=W\setminus A_j,\qquad P_j=\{w:R(w)\subseteq N_j\},
\]
with \(N_0=\varnothing\), \(P_{-1}=\varnothing\). The abbreviation \(\operatorname{pre}(S)=\{w:R(w)\cap S\ne\varnothing\}\) denotes the existential predecessor. The operator \(\Box\Diamond\) is monotone, hence \(A_{j+1}\subseteq A_j\), so \(N_j\) and \(P_j\) are increasing sequences. An \(m\)-separator is a frame in which \(A_m\setminus A_{m+1}\ne\varnothing\), equivalently \(N_{m+1}\setminus N_m\ne\varnothing\).

## Proof

**1. Two disjoint rank filtrations.** Directly from the semantics,
\[
N_{j+1}=\operatorname{pre}(P_j),\qquad
P_j=\{w:R(w)\subseteq N_j\}.
\]
For all indices \(i,j\geq0\), the sets \(N_i\) and \(P_j\) are disjoint. Indeed, suppose \(w\in N_i\cap P_j\) and choose such a pair with \(i+j\) minimal. The cases \(i=0\) and \(j=0\) are impossible: \(N_0\) is empty, while a point in \(P_0\) has no successors and can never enter any \(N_i\). For \(i,j\geq1\), membership in \(N_i=\operatorname{pre}(P_{i-1})\) yields a successor \(v\in P_{i-1}\), while membership of \(w\) in \(P_j\) implies every successor, including \(v\), belongs to \(N_j\). Thus \(v\in N_j\cap P_{i-1}\) contradicts minimality of \(i+j\).

**2. Sharp lower bound.** If \(w\in N_{m+1}\setminus N_m\), then \(w\) has a successor in \(P_m\setminus P_{m-1}\). Every \(v\in P_j\setminus P_{j-1}\), for \(j\geq1\), has a successor in \(N_j\setminus N_{j-1}\): all its successors lie in \(N_j\), but not all lie in \(N_{j-1}\). Iterating these two facts shows that each of the \(m+1\) sets
\[
N_i\setminus N_{i-1}\quad(1\leq i\leq m+1)
\]
and each of the \(m+1\) sets
\[
P_j\setminus P_{j-1}\quad(0\leq j\leq m)
\]
is nonempty. They are pairwise disjoint by nesting within each filtration and Step 1 across the filtrations. Hence \(|W|\geq2m+2\). The directed path of \(2m+2\) worlds, with its last point a dead end, attains equality: along a directed path, \(\alpha_j\) fails exactly at positions with an odd number of remaining edges \(1,3,\ldots,2j-1\). At the initial world there are \(2m+1\) remaining edges, so \(\alpha_m\) holds and \(\alpha_{m+1}\) fails. This path construction is Lemma 2 of Alpay and Basaran (2026), not a new claim here.

**3. Exhaustive equality structure.** Suppose \(|W|=2m+2\) and the frame separates. The preceding \(2m+2\) disjoint nonempty layers must all be singletons and exhaust \(W\). Denote them by
\[
N_i\setminus N_{i-1}=\{a_i\}\quad(1\leq i\leq m+1),\qquad
P_j\setminus P_{j-1}=\{b_j\}\quad(0\leq j\leq m).
\]
The accessibility relation necessarily and sufficiently obeys these three rules:

1. \(R(b_0)=\varnothing\).
2. For \(1\leq j\leq m\), one has \(a_j\in R(b_j)\subseteq\{a_1,\ldots,a_j\}\); every other edge from \(b_j\) to an earlier \(a_i\) is optional.
3. For \(1\leq i\leq m+1\), one has \(b_{i-1}\in R(a_i)\), no edge \(a_iRb_j\) for \(j<i-1\), and every edge from \(a_i\) to an \(a_\ell\), or to a \(b_j\) with \(j\geq i\), is optional.

Necessity follows from the definitions of each first-entry layer. Conversely, assume these rules on the indicated \(2m+2\) distinct vertices. Then \(P_0=\{b_0\}\) and \(N_1=\{a_1\}\); by induction, \(P_j=\{b_0,\ldots,b_j\}\) and \(N_j=\{a_1,\ldots,a_j\}\) for all \(0\leq j\leq m\), and \(N_{m+1}=\{a_1,\ldots,a_{m+1}\}\). Thus \(a_{m+1}\) is the unique separating world. The forced edges contain the spanning directed path
\[
a_{m+1}\to b_m\to a_m\to b_{m-1}\to\cdots\to a_1\to b_0.
\]

**4. Rigidity, counts, and edge polynomial.** The \(2m+2\) singleton layers are intrinsically definable from \(R\), so every automorphism fixes each vertex; every minimum separator is rigid, and distinct optional-edge patterns represent different isomorphism types. There are \(2m+1\) forced edges. The freely selectable edges number
\[
\underbrace{(m+1)^2}_{a_i\to a_\ell}
+\underbrace{\frac{m(m+1)}2}_{a_i\to b_j,\ j\geq i}
+\underbrace{\frac{m(m-1)}2}_{b_j\to a_i,\ i<j}
=2m^2+2m+1=E_m.
\]
Therefore there are \(2^{E_m}\) isomorphism types, each having \((2m+2)!\) distinct labelings. There is exactly one separating vertex per labelled frame, giving the preselected-root count upon division by \(2m+2\). Multiplying a factor \(z\) for each forced edge and \(1+z\) for each optional edge yields the stated polynomial and completes the proof.

## Verification

Run `python3 checker.py` using the included standard-library-only file. It independently evaluates the two modal operators as outgoing bitmask operations, builds the \(N/P\) predecessor strata separately, and compares their membership on **all** directed relations on carriers of sizes \(1\), \(2\), \(3\), and \(4\). These are respectively \(2^1\), \(2^4\), \(2^9\), and \(2^{16}\) relations. The exhaustive count of four-world minimal separators is \(768\), with \(192\) separating a preselected world. The checker also enumerates all \(2\), \(32\), and \(8192\) allowed canonical optional-edge patterns for \(m=0,1,2\), verifies every layer and truth value, tests rigidity for the four-world normal forms, samples \(2002\) eight-world patterns, and checks the directed-path witnesses through \(m=12\). The executed artifact returned `ALL_CHECKS_OK`. None of these bounded computations substitutes for Steps 1–4 of the proof.

## Relationship to prior work

Alpay and Basaran (2026), Proposition 5, prove that \(\alpha_2\) and \(\alpha_3\) first separate at six worlds. Their Lemma 2 supplies a \(2m+2\)-world path separator for every \(m\geq1\) but explicitly does **not** establish its universal minimality; their Table 3 verifies minimality by SAT only for \(m=1,2,3\). The new statement is the uniform lower bound for **all** \(m\), plus the exhaustive extremal normal form, rigidity, and exact labelled/unlabelled edge enumeration. Elementary win/lose retrograde stratification is standard background and is not claimed as new. The two-filtration argument here is a self-contained way to obtain the uniform sharp bound and complete extremizers directly from modal semantics.

## Limitations

The theorem is for the variable-free pair \(\alpha_m,\alpha_{m+1}\) on **arbitrary** finite \(\mathsf K\)-frames. It does not describe minimum countermodels for arbitrary formulas, finite frames larger than \(2m+2\), or additional restrictions such as seriality or reflexivity (under seriality all the \(\alpha_j\) hold). The classification concerns relations, not arbitrary valuations or pointed-model bisimulation types. The count and all-order minimality have not undergone independent mathematical review. An equivalent result under impartial-game remoteness or retrograde-rank terminology is a residual historical-priority possibility.

## References

1. F. Alpay and B. Basaran, *GPU-Accelerated Search and Certification of Bounded Indistinguishability in Finite Kripke Semantics*, arXiv:2606.15437 (first public version 2026-06-13), especially Proposition 5, Lemma 2, Table 3 and Section 11. https://arxiv.org/abs/2606.15437
2. C. Comin and R. Rizzi, *Linear-Time Safe-Alternating DFS and SCCs*, arXiv:1610.09679 (2016). Related background on graph-game reachability and decomposition; it does not supply the modal extremal census. https://arxiv.org/abs/1610.09679
