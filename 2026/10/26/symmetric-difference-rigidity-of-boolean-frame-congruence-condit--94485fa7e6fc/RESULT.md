# Symmetric-difference rigidity of Boolean-frame congruence conditions

## Finding
Let \(B\) be an arbitrary Boolean algebra (possibly infinite), with order \(\leq\), join \(\vee\), complement \(\neg\), and symmetric difference \(x\oplus y=(x\wedge\neg y)\vee(\neg x\wedge y)\). For an arbitrary unary operation \(f:B\to B\), consider the condition
\[
 (Q)\qquad \forall x,y,z\in B:\quad x\oplus y\leq z\ \Longrightarrow\ f(x)\oplus f(y)\leq f(z).
\]
**Rigidity theorem:** \((Q)\) holds if and only if \(f\) preserves binary joins:
\[
 \forall x,y\in B:\quad f(x\vee y)=f(x)\vee f(y).
\]
There is no requirement that \(f(0)=0\). Thus \((Q)\) is precisely join-additivity, not a property strictly between join-additivity and monotonicity.

On the \(n\)-atom Boolean algebra \(B=\mathcal P([n])\), for each integer \(n\geq1\), the total number of labelled operations satisfying \((Q)\) is exactly
\[
 \boxed{(2^n+1)^n}.
\]
For a prescribed zero-value \(f(\varnothing)=C\subseteq[n]\) of cardinality \(c\), the number is exactly \(2^{n(n-c)}\). Hence exactly \(2^{n^2}\) of these operations are normal, i.e. have \(f(\varnothing)=\varnothing\).

The exceptional map discussed in Example 2.2 of Gyenis, Molnár and Öztürk, *More on modal logics and deduction* (2026), does **not** satisfy \((Q)\). On \(\mathcal P(\{1,2,3\})\) it sends \(\{1,3\}\) to \(\{1,2,3\}\) and fixes every other set. The instance \(x=\{1,3\}\), \(y=\{1\}\), \(z=\{3\}\) has \(x\oplus y=z\), but \(f(x)\oplus f(y)=\{2,3\}\nleq\{3\}=f(z)\). This is a precise counterexample to the asserted satisfaction of \((Q)\); it does not assess other claims of that paper.

## Assumptions and scope
The theorem uses only Boolean-algebra identities and is valid for every Boolean algebra, including infinite and atomless ones. It assumes neither normality, monotonicity, continuity, nor the congruence extension property in advance. “Additive” throughout means *preserving binary joins*; a normal operation additionally satisfies \(f(0)=0\). In finite enumeration, the \(n\) Boolean atoms are distinguished, all unary functions are counted on the fixed powerset carrier, and no quotient by automorphisms is taken.

## Proof
**1. The quasi-identity forces a lower bound for \(f(0)\).** Apply \((Q)\) with \((x,y,z)=(a,0,a)\). Then \(f(a)\oplus f(0)\leq f(a)\). In a Boolean algebra \(u\oplus v\leq u\) entails \(v\leq u\), so \(f(0)\leq f(a)\) for every \(a\).

**2. It forces monotonicity.** If \(a\leq b\), apply \((Q)\) to \((a,0,b)\). Then \(f(a)\oplus f(0)\leq f(b)\). Together with \(f(0)\leq f(b)\) and \(f(a)\leq(f(a)\oplus f(0))\vee f(0)\), this gives \(f(a)\leq f(b)\).

**3. It forces binary join preservation.** For arbitrary \(a,b\), let \(u=a\vee b\). Since \(u\oplus a=b\wedge\neg a\leq b\), \((Q)\) gives \(f(u)\oplus f(a)\leq f(b)\). Monotonicity yields \(f(a)\leq f(u)\), hence \(f(u)\oplus f(a)=f(u)\wedge\neg f(a)\). Therefore \(f(u)\leq f(a)\vee f(b)\). The opposite inequality follows from monotonicity, establishing equality.

**4. Join preservation implies \((Q)\).** Suppose \(f\) preserves binary joins. It is then monotone. Write \(r=x\wedge y\), \(s=x\wedge\neg y\), \(t=y\wedge\neg x\). Then \(x=r\vee s\), \(y=r\vee t\), and \(x\oplus y=s\vee t\). Using \((A\vee B)\oplus(A\vee C)\leq B\vee C\) in the target Boolean algebra,
\[
 f(x)\oplus f(y)
 = (f(r)\vee f(s))\oplus(f(r)\vee f(t))
 \leq f(s)\vee f(t)=f(x\oplus y).
\]
If \(x\oplus y\leq z\), monotonicity yields \(f(x\oplus y)\leq f(z)\). Thus \((Q)\) follows.

**5. Classification and enumeration on finite powersets.** Fix \(B=\mathcal P([n])\). For each *output atom* \(j\in[n]\), the Boolean coordinate \(\chi_j(f(U))\) of a join-preserving \(f\) is either identically one or has the form
\[
 \chi_j(f(U))=1\ \Longleftrightarrow\ U\cap S_j\neq\varnothing
\]
for a uniquely determined subset \(S_j\subseteq[n]\). Indeed, if \(j\in f(\varnothing)\), monotonicity makes it constantly present; otherwise, every \(U\) is the join of its singleton atoms and join preservation determines the coordinate as the disjunction of those singleton values. Conversely, independently choosing for each \(j\) the constant-one option or one of the \(2^n\) sets \(S_j\) yields a unique join-preserving \(f\). This gives \((2^n+1)^n\) operations. If \(f(\varnothing)=C\), every \(j\in C\) has the forced constant-one option, whereas each \(j\notin C\) has \(2^n\) choices. Therefore exactly \(2^{n(n-|C|)}\) operations have this prescribed zero-value. Summing over \(C\) recovers the total. Taking \(C=\varnothing\) gives \(2^{n^2}\).

**6. The displayed exceptional map violates the premise.** Under bitmask coding \(\{1,3\}=5\), \(\{1\}=1\), \(\{3\}=4\), it has \(f(5)=7\), \(f(1)=1\), \(f(4)=4\). Hence \(5\oplus1=4\leq4\) but \(f(5)\oplus f(1)=6\nleq4=f(4)\), as claimed.

## Verification
Run `python3 checker.py` with a standard Python 3 interpreter; no external packages are needed. The checker independently evaluates \((Q)\) over every triple of Boolean inputs and compares it with all binary join identities for **every** map on the one- and two-atom Boolean algebras. It constructs every map in the claimed coordinate normal form for one, two, and three atoms and tests all quasi-identity instances and join equations for those maps. It verifies the fixed-bottom distribution in each tested size and the explicit exceptional-map failure. The observed output ends with `ALL_CHECKS_OK`. Exhaustion at small cardinalities is only corroboration; the proof above handles all Boolean algebras.

## Relationship to prior work
Gyenis, Molnár and Öztürk (2026), Section 2, Fact 2.1, present \((Q)\) as a sufficient condition for the congruence extension property and explicitly describe it as a strict weakening of additivity. The same section provides Example 2.2 as a proposed nonadditive witness. The theorem here proves the stronger equivalence \((Q)\iff\) binary-join-preservation and gives a concrete violating triple for that example. It **does not** claim that nonadditive Boolean frames cannot have the congruence extension property: other constructions in the same paper concern that broader phenomenon independently of \((Q)\).

The standard Boolean-algebra-with-operators literature already identifies join-preserving operations as additive; the basic relational representation and the count \(2^{n^2}\) of normal relational operators are not claimed as new mathematics. The particular quasi-identity's unexpected collapse, the sharp failure of its proposed witness, and the resulting complete \((2^n+1)^n\) census are the claims assessed here. An independently published study, *Eight elements are the sharp finite CEP threshold for Boolean frames*, enumerates failures of CEP on the eight-element carrier rather than the narrower \((Q)\) property; its detailed statement and proof concern a different census and do not imply the present equivalence.

## Limitations
The result characterizes condition \((Q)\), not all Boolean-frame operations or varieties with the congruence extension property. It has no implications, without separate proofs, for the validity of other theorems in the motivating paper. The finite enumeration counts labelled functions; it does not provide a count up to permutation of atoms. The priority comparison is limited to the inspected sources, and independent review has not been performed.

## References
1. Z. Gyenis, Z. Molnár, Ö. Öztürk, *More on modal logics and deduction*, arXiv:2603.17724, first posted 2026-03-18; especially Section 2, Fact 2.1 and Example 2.2. https://arxiv.org/html/2603.17724
2. Z. Gyenis, Z. Molnár, *Varieties of modal algebras without the congruence extension property*, arXiv:2402.07293 (2024), journal version in *Notre Dame Journal of Formal Logic* 67 (2026), 159–176. https://arxiv.org/abs/2402.07293
3. *Eight elements are the sharp finite CEP threshold for Boolean frames* (2026-10-04), published mathematical research result. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-eight-elements-are-the-sharp-finite-cep-threshold-for-boolean-fr--d55c70b114c5
4. R. Goldblatt, *Mathematical Modal Logic: A View of Its Evolution* (2003), Section 3.3 on Boolean algebras with operators; standard background on additivity.
