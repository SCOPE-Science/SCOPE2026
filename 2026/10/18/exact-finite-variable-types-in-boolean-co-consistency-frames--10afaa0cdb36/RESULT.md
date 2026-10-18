# Exact finite-variable types in Boolean co-consistency frames

## Finding

For integers \(n,k\geq 1\), put \(U_n=\{1,\ldots,n\}\). Consider the **full nonzero compatibility frame**
\[
G_n=(\mathcal P(U_n)\setminus\{\varnothing\},R),\qquad A R B\iff A\cap B\neq\varnothing.
\]
Each of the \(k\) propositional variables \(p_1,\ldots,p_k\) receives an independently chosen Boolean value \(B_i\subseteq U_n\), and its forcing clause is
\[
A\models p_i\quad\Longleftrightarrow\quad A\subseteq B_i.
\]
Boolean connectives and \(\Diamond,\Box\) have classical Kripke semantics. The entire nonzero frame is present; arbitrary induced submodels are **not** part of this statement.

Assign to each atom \(a\in U_n\) its \(k\)-bit color \(c(a)\in\{0,1\}^k\), where \(c(a)_i=1\) iff \(a\in B_i\). At a pointed nonempty state \(A\) define
\[
T=\{c(a):a\in U_n\},\qquad S=\{c(a):a\in A\}.
\]
Two such pointed translated models, even over different atom counts, satisfy precisely the same modal formulas in the \(k\) named variables **if and only if** their ordered-color profiles \((T,S)\) coincide. Necessarily \(\varnothing\neq S\subseteq T\subseteq\{0,1\}^k\), and every such profile with \(|T|\leq n\) is realized on \(G_n\).

Consequently the exact number of distinct pointed \(k\)-variable modal theories occurring on \(G_n\), as both the translation values and the pointed state vary, is
\[
\boxed{N(n,k)=\sum_{j=1}^{\min(n,2^k)}\binom{2^k}{j}(2^j-1).}
\]
In particular, for \(n\ge 2^k\) this stabilizes at \(3^{2^k}-2^{2^k}\). For \(k=1\), the counts by increasing \(n\) are \(2,5,5,\ldots\); for \(k=2\), they are \(4,22,50,65,65,\ldots\).

Let \(L_{n,k}^{\mathrm{full}}\) be the set of modal formulas using only those \(k\) propositional letters which are true at every nonempty state of \(G_n\) under every choice of the Boolean values \(B_i\). For all \(1\le n<m\),
\[
\boxed{L_{m,k}^{\mathrm{full}}\subsetneq L_{n,k}^{\mathrm{full}}\quad\Longleftrightarrow\quad n<2^k.}
\]
Thus the least positive number of propositional variables separating the two full-state finite stages is exactly \(\lceil\log_2(n+1)\rceil\). Whenever separation is possible, a formula of modal depth at most three suffices.

## Assumptions and scope

Only finite Boolean powerset algebras, the nonzero **full** compatibility frame, ordinary Boolean modal connectives, and parameter translations allowing every Boolean value \(B_i\subseteq U_n\) are used. The assignment to distinct propositional letters is independent. The ability to realize every choice of values by the source's parameter translations is Lemma 5.2 of Jockwich--Tarafder--Venturi (2026).

The pointed theory of \((G_n,(B_i),A)\) is the set of formulas over precisely the allowed alphabet \(\{p_1,\ldots,p_k\}\) true at \(A\). The formulas may omit some letters. No infinite Boolean algebra, restricted parameter-free translation, or proper subset of the full nonzero frame is covered.

## Proof

### 1. Canonical color quotient and invariance

Fix a model as above and let \(T\) be its nonempty set of distinct colors. Form the canonical frame \(G_T=(\mathcal P(T)\setminus\{\varnothing\},R_T)\), where \(C R_T D\) iff \(C\cap D\neq\varnothing\). Interpret \(p_i\) at \(C\subseteq T\) exactly when every \(t\in C\) has \(t_i=1\).

The map
\[
f:\mathcal P(U_n)^+\longrightarrow\mathcal P(T)^+,\qquad f(A)=\{c(a):a\in A\}
\]
is onto. It is a bounded morphism: if \(A\cap B\neq\varnothing\) then \(f(A)\cap f(B)\neq\varnothing\) (forth). Conversely, if \(C\subseteq T\) is nonempty and meets \(f(A)\), choose an element \(a\in A\) with color in \(C\); form a state \(B\) containing that \(a\) and one arbitrary representative of each other color in \(C\). Then \(A\cap B\neq\varnothing\) and \(f(B)=C\) (back). Finally,
\[
A\subseteq B_i\iff (\forall t\in f(A))\ t_i=1,
\]
so atomic truth is preserved. Induction on every modal formula gives equivalence of truth at \(A\) and at \(f(A)\). Therefore two pointed models with the same \((T,S)\) satisfy the same formulas.

### 2. Explicit formulas distinguish every different profile

For each bit-vector \(t\in\{0,1\}^k\), let
\[
\delta_t=\bigwedge_{i:t_i=1}p_i\ \wedge\ \bigwedge_{i:t_i=0}\neg\Diamond p_i,
\]
with empty conjunctions interpreted as \(\top\). In a full nonzero frame,
\[
A\models\Diamond p_i\iff A\cap B_i\neq\varnothing.
\]
For the forward direction, a witness is a nonempty set \(C\subseteq B_i\) meeting \(A\). For the converse, an element of \(A\cap B_i\) supplies the singleton witness \(C\). Thus
\[
A\models\delta_t\iff \text{all atoms of }A\text{ have color }t.
\]
It follows that
\[
A\models\Diamond\delta_t\iff t\in S.
\]
Moreover,
\[
A\models\Diamond\Diamond\delta_t\iff t\in T:
\]
if \(t\in T\), the universal state \(U_n\), which meets every nonempty state, connects \(A\) to a singleton state of color \(t\); conversely, any witness for \(\delta_t\) entails the existence of such an atom. Consequently the formulas \(\Diamond\delta_t\) and \(\Diamond\Diamond\delta_t\) recover respectively every bit of \(S\) and every bit of \(T\) at any pointed world. Different pairs \((T,S)\) cannot have the same theory.

### 3. Exact census

An assignment to the \(k\) variables is equivalently an arbitrary coloring of the \(n\) atoms by the \(2^k\) bit-vectors. Its image \(T\) has size \(j\) for some \(1\le j\le\min(n,2^k)\), and every such \(T\) occurs. For a fixed image \(T\), the distinguished nonempty state realizes any of the \(2^j-1\) nonempty color supports \(S\subseteq T\). By Steps 1 and 2 these are exactly the distinct pointed theories, producing the displayed sum. When \(n\ge2^k\), the binomial theorem gives
\[
\sum_{j=1}^{2^k}\binom{2^k}{j}(2^j-1)=3^{2^k}-2^{2^k}.
\]

### 4. Sharp finite-variable stage hierarchy

If \(m\ge n\), a counterexample on \(G_n\) with profile \((T,S)\) can be reproduced on \(G_m\): assign at least one atom each color in \(T\), duplicate colors to fill out \(m\) atoms, and choose a state with support \(S\). By Steps 1 and 2 the same formula fails there. Thus \(L_{m,k}^{\mathrm{full}}\subseteq L_{n,k}^{\mathrm{full}}\). If \(n\ge2^k\), all profiles are already realized at \(n\), so equality follows.

Suppose \(n<2^k\). Choose \(n+1\) different bit-vectors forming \(Q\subseteq\{0,1\}^k\), and set
\[
\Psi_Q=\neg\bigwedge_{t\in Q}\Diamond\Diamond\delta_t.
\]
At every state in every translated \(G_n\)-model, at most \(n\) colors occur, so at least one conjunct fails and \(\Psi_Q\) holds. On \(G_m\) for any \(m>n\), choose values \(B_i\) whose atom colors include all vectors in \(Q\). Then every conjunct is true at every state by Step 2, and \(\Psi_Q\) fails. Hence the inclusion is strict. Since \(\delta_t\) has modal depth at most one, \(\Psi_Q\) has modal depth at most three. The smallest positive integer \(k\) satisfying \(n<2^k\) is \(\lceil\log_2(n+1)\rceil\), proving optimality of the variable count.

## Verification

The bundled standalone `check.py` directly evaluates classical modal formulas on the complete nonzero powerset frames by bitmask intersection. For \(k\le3\), \(n\le4\), it compared truth of sampled modal formulas (including conjunction, disjunction, negation, box and diamond) with an independently computed canonical color quotient: \(315{,}460\) individual formula-world comparisons passed. It also checked \(10{,}466\) choices of parameters for explicit stage-separating formulas, and directly tested the defining formula witnesses and the closed type count over \(8{,}434\) pointed parameter instances. These are reproducible checks, not a substitute for the proof for unbounded \(n,k\).

Reproduce with `python3 check.py` in the package directory. The script uses only Python's standard library, with deterministic random seed.

## Relationship to prior work

Jockwich, Tarafder, and Venturi (2026) define the nonzero full-state logic \(\operatorname{Log}^{\#}_{\mathrm{full}}(B)\) and the distinct nonzero-state submodel logic \(\operatorname{Log}^{\#}_{\subseteq}(B)\) in their Definition 6.1. Their Definition 5.1 supplies co-consistency and atomic truth; Lemma 5.2 realizes every Boolean translation value. The source paper studies several axioms and gives a hierarchy of the **submodel** logics, but its inspected sections do not provide this complete color-support classification, pointed-theory count, or sharp bound on variables for the **full-state** fragments.

An earlier published result, *Every finite stage of the internal forcing logic hierarchy is strict*, proves strictness of the unrestricted-variable **submodel** hierarchy using bounded morphisms, domatic partitions and characteristic formulas. Its constructed separating valuations also entail strictness of the full-state hierarchy when arbitrarily many variables are allowed. Thus unbounded-variable strictness is **not** presented here as novel. That result does not give the exact finite-variable cutoff, the count of pointed full-frame modal theories, or the bounded-depth color-witness formulas established above.

Another published result, *Sharp \(2^q\) atom-visibility threshold for finite Boolean algebras*, concerns first-order quantifier rank in the **pure Boolean-algebra language**. Its numerical threshold is similar, but first-order quantifier rank and the number of propositional modal letters under co-consistency translations are different invariants; neither result supplies the other's characterization. A separate classification for intuitionistic two-level forks uses upward-persistent valuations and root/leaf theories, not these full co-consistency frames.

## Limitations

The result is not about the nonzero-state **submodel** logics: omitting worlds may destroy the singleton witnesses and universal intermediate world used in Step 2. It does not supply an axiomatization of any unrestricted-variable logic, nor does it minimize formula length or modal depth. Minimality is proved only for the **number of propositional variables**; depth three is an upper bound. An unindexed equivalent statement using the language of colored intersection frames remains possible.

## References

1. Santiago Jockwich, Sourav Tarafder, and Giorgio Venturi, *The Internal Modal Logic of Forcing*, arXiv:2607.25977, first publicly posted 2026-07-28, especially Definitions 5.1 and 6.1 and Lemma 5.2.
2. *Every finite stage of the internal forcing logic hierarchy is strict*, published mathematical note, `https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-every-finite-stage-of-the-internal-forcing-logic-hierarchy-is-st--069a2c03aeb3`.
3. *Sharp \(2^q\) atom-visibility threshold for finite Boolean algebras*, published mathematical note, `https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-2-q-atom-visibility-threshold-for-finite-boolean-algebras--938cb5f89dc7`.
