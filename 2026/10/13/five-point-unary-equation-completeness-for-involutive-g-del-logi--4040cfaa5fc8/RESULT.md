# Five-point unary-equation completeness for involutive Gödel logic

## Finding
Let \(\mathcal G\) denote the standard algebra on \([0,1]\) with constant \(0\), Gödel meet \(a\wedge b=\min(a,b)\), Gödel implication \(a\to b=1\) when \(a\le b\) and \(a\to b=b\) otherwise, and involutive negation \(\sim a=1-a\). Consider parameter-free terms \(t(x)\) containing **at most one variable** in the signature \(\{0,\wedge,\to,\sim\}\).

**Theorem.** There are exactly \(192\) distinct unary term functions on \(\mathcal G\). For each integer \(n\ge2\), define the involution-closed equally spaced subchain
\[
V_n=\left\{\frac{j}{n-1}:0\le j<n\right\},
\]
with the induced operations, and let \(T_n\) denote its unary term-function set. Then
\[
|T_n|=\begin{cases}
4,&n=2,\\
12,&n=3,\\
64,&n\ge4\text{ even},\\
192,&n\ge5\text{ odd}.
\end{cases}
\]
Moreover, for **every** pair of such one-variable terms \(s,t\), the identity \(s(x)\approx t(x)\) holds in \(\mathcal G\) if and only if it holds in \(V_n\) **precisely when** \(n\ge5\) is odd. Thus \(V_5=\{0,\tfrac14,\tfrac12,\tfrac34,1\}\) is the smallest equally spaced finite symmetric chain that determines all these one-variable identities. The one-generated algebra of term functions of \(\mathcal G\) therefore has \(192\) elements.

## Assumptions and scope
The variable \(x\) is a single propositional truth-degree variable; all constants must be expressible from the signature. In particular, the constant \(1\) is definable by \(0\to0\). The theorem concerns **equality of term functions**, not arbitrary fuzzy consequence relations, formulas with two or more variables, quantifiers, or epistemic/modal operators. Every \(V_n\) is evaluated as a subalgebra of the real unit interval, not as a rounded arithmetic approximation.

Write \(\neg_G u=u\to0\). Define the crisp selector \(\Delta u=\neg_G(\sim u)\), which is \(1\) exactly when \(u=1\) and \(0\) otherwise. All of the following constructions are parameter-free terms in the stated language. We also use \(u\vee v=\sim(\sim u\wedge\sim v)\), the ordinary maximum.

## Proof
**1. Four possible local outputs.** Fix \(a\in[0,1]\). Structural induction on a term shows that \(t(a)\) always belongs to \(\{0,1,a,1-a\}\). This is true for the generators \(0\) and \(x\). Negation permutes these four candidates; the minimum selects one operand; and Gödel implication returns either \(1\) or its consequent. The same induction, simultaneously in the symbolic order of the four candidates, shows that on each of the five regions
\[
\{0\},\quad (0,\tfrac12),\quad\{\tfrac12\},\quad (\tfrac12,1),\quad\{1\},
\]
a term agrees throughout the region with a **single** choice from \(0,x,\sim x,1\). This follows because all pairwise order comparisons among those four symbolic functions are constant on each region. At the two endpoints there are two distinct choices, on each strict half-interval four, and at the midpoint three. Hence there are at most \(2\cdot4\cdot3\cdot4\cdot2=192\) term functions.

**2. Every symbolic choice is realizable.** Set
\[
L=\Delta(x\to\sim x),\quad R=\Delta(\sim x\to x),\quad Z=\neg_G x,\quad O=\neg_G(\sim x).
\]
Then \(L\) detects \(x\le\tfrac12\), \(R\) detects \(x\ge\tfrac12\), and \(Z,O\) detect the endpoints. The five terms
\[
C_0=Z,\quad C_-=L\wedge\neg_G R\wedge\neg_G Z,\quad
C_c=L\wedge R,\quad
C_+=R\wedge\neg_G L\wedge\neg_G O,\quad C_1=O
\]
are crisp, pairwise disjoint, and collectively equal to \(1\). Their nonzero sets are exactly the five regions listed above, in order. For any independent regionwise choices \(u_0,u_-,u_c,u_+,u_1\) from \(\{0,x,\sim x,1\}\), the term
\[
(C_0\wedge u_0)\vee(C_-\wedge u_-)\vee(C_c\wedge u_c)\vee(C_+\wedge u_+)\vee(C_1\wedge u_1)
\]
realizes the prescribed piecewise output. Taking the distinct possibilities at each region realizes all \(192\) profiles. They are pairwise distinct already on the five sample values \(0,\tfrac14,\tfrac12,\tfrac34,1\), since each region's possible outputs are distinct at its sample point. This proves the exact continuum count and shows that restriction to \(V_5\) is injective on unary term functions.

**3. Counts on finite chains.** The same selectors and local-output proof apply to every \(V_n\). A region disjoint from \(V_n\) contributes one choice rather than its continuum count; an occupied region contributes the continuum count because its four (or three or two) symbolic values are distinct at every point there. For \(n=2\), only endpoints occur, giving \(2\cdot2=4\). For \(n=3\), only endpoints and midpoint occur, giving \(2\cdot3\cdot2=12\). For even \(n\ge4\), both strict half-intervals occur but the midpoint does not, giving \(2\cdot4\cdot4\cdot2=64\). For odd \(n\ge5\), all five regions occur, giving \(192\). Distinct symbolic choices remain distinct on each occupied region; additional points in one region cannot create new choices.

**4. Exact criterion for one-variable identities.** If \(n\ge5\) is odd, \(V_n\) contains a sample of every region. If two terms agree on \(V_n\), then their regionwise symbolic selections agree (up to the unavoidable local coincidences) on every region, so they agree throughout \([0,1]\). The reverse implication holds because \(V_n\) is a subalgebra of \(\mathcal G\).

For any **even** \(n\ge2\), the midpoint detector \(C_c\) is zero everywhere on \(V_n\) but equals \(1\) at \(x=\tfrac12\) in \(\mathcal G\). Thus the identity \(C_c(x)\approx0\) holds on \(V_n\) and fails in \(\mathcal G\). For \(n=3\), the left-interior detector \(C_-\) is zero on \(V_3\) but equals \(1\) at \(x=\tfrac14\) in \(\mathcal G\); hence \(C_-(x)\approx0\) separates them. These exhaust the finite sizes outside the positive case. All claimed bounds and equivalences follow. \(\square\)

## Verification
The accompanying standalone `verify.py` enumerates the closure of the three initial unary functions (identity, constant zero, constant one) under Gödel meet, implication in both argument orders, and involutive negation. It independently constructs the symbolic five-region normal-form function set and asserts exact equality for every chain size \(2\le n\le17\). It checks the count and both sharpness witnesses, and exits only after printing `VERIFICATION_OK`. Execute with `python3 verify.py` using Python 3 and only the standard library. These exact finite computations corroborate the formulas; the continuum case and all untested chain sizes follow from the structural proof, not extrapolation.

## Relationship to prior work
Bílková, Ferguson, and Kozhemiachenko (arXiv:2510.04642, first released October 6, 2025) study epistemic Gödel logic with **the same propositional operations** and an involution, develop finitary modal semantics and terminating tableaux, and analyze modal validity complexity. Their propositional grammar and derived crisp operations motivate identifying the sharp one-variable, nonmodal equational test. The present theorem does **not** claim a finite-valued reduction for modal formulas.

Coniglio, Esteva, Gispert, and Godo (2021) study finite and standard involutive Gödel chains and, in their five-valued analysis, explicitly establish definable formulas for individual truth-value cells. That is substantial prior groundwork. Their inspected classification concerns intermediate degree-preserving consequence logics; it does not state the above full unary term-function census, parity criterion for continuum equational equivalence, or minimal five-point test. In particular, non-definability of every single high-chain truth value for larger chains is compatible with the present finite **identity** test.

Carai's study of free Gödel algebras (arXiv:2406.05480) concerns the non-involutive Heyting/Gödel signature. The free-algebra theorem for \(L_{PG}\) in *Involutive symmetric Gödel spaces, their algebraic duals and logic* (Theorem 7.5, 2023) concerns a different, richer perfect-MV/Gödel fusion signature on Chang-type chains; it neither identifies this \(192\)-function algebra nor implies the five-stratum identity test under the standard real semantics.

## Limitations
The classification is restricted to parameter-free **unary propositional** terms in the four-symbol signature and the specified standard interval semantics. Adding independent real truth constants, modal operators, or further variables can invalidate the cardinality and finite-test conclusions. The result does not establish independence from all unpublished or differently named prior work; older implicit normal-form derivations remain an originality risk. Finite-program checks cannot certify the unbounded claims or replace the argument above.

## References
1. M. Bílková, T. Ferguson, and D. Kozhemiachenko, *Tableaux for epistemic Gödel logic*, arXiv:2510.04642 (first submitted 2025-10-06); DOI 10.1007/978-3-032-13562-9_17. Full text: https://arxiv.org/pdf/2510.04642.
2. M. E. Coniglio, F. Esteva, J. Gispert, and L. Godo, *Degree-preserving Gödel logics with an involution: intermediate logics and (ideal) paraconsistency* (2021), Section 4.2, pp. 16–17. Accessible manuscript: https://www.iiia.csic.es/media/filer_public/f5/23/f52329a1-0d45-429a-bb4d-a818ac2fdc59/5644.pdf.
3. L. Carai, *Free algebras and coproducts in varieties of Gödel algebras*, arXiv:2406.05480, Section 3. Full text: https://arxiv.org/pdf/2406.05480.
4. *Involutive symmetric Gödel spaces, their algebraic duals and logic*, *Archive for Mathematical Logic* (2023), Theorem 7.5; DOI 10.1007/s00153-023-00866-6. Full text: https://link.springer.com/article/10.1007/s00153-023-00866-6.
