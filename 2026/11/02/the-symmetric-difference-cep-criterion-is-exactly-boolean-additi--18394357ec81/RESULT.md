# The symmetric-difference CEP criterion is exactly Boolean additivity

## Finding

Let \(B=(B,\wedge,\vee,\neg,0,1)\) be **any Boolean algebra**, finite or infinite, and write \(u\triangle v=(u\wedge\neg v)\vee(v\wedge\neg u)\). For a map \(f:B\to B\), consider
\[
(\ast)\qquad\forall x,y,z\in B\quad
x\triangle y\le z\ \Longrightarrow\ f(x)\triangle f(y)\le f(z).
\]
Then **\((\ast)\) is equivalent to finite-join additivity**:
\[
\forall x,y\in B,\qquad f(x\vee y)=f(x)\vee f(y).
\]
Here “additivity” means preservation of binary joins, **not** the stronger requirement \(f(0)=0\). In particular, there is no non-join-additive unary operation satisfying \((\ast)\) on any Boolean algebra.

For the labelled powerset algebra \(B=\mathcal P([n])\) with \(n\ge1\), the exact number of unary maps satisfying \((\ast)\) is
\[
\boxed{(2^n+1)^n}.
\]
The number also satisfying \(f(0)=0\) is \(\boxed{2^{n^2}}\). The first unrestricted counts, for \(n=1,2,3,4\), are \(3,25,729,83521\).

A concrete source-critical consequence is that the eight-element Boolean-frame operation in Example 2.2 of Gyenis–Molnár–Öztürk [1] does **not** satisfy \((\ast)\), contrary to the assertion made immediately after its definition. That conclusion only concerns the asserted quasi-equation; it does **not** claim that the example lacks the congruence extension property or that the paper's other main existence theorems are false.

## Assumptions and scope

All inequalities are in the Boolean order. The symmetric difference \(u\triangle v\) is the Boolean term \((u\wedge\neg v)\vee(v\wedge\neg u)\). The binary-join condition does not require normality. The exact census assumes a *fixed labelled* atomic carrier, without quotienting by permutations. There are no restrictions on the size of the Boolean algebra in the equivalence theorem.

## Proof

Assume \((\ast)\). First, applying it to \(x=t,y=0,z=t\) yields
\[
f(t)\triangle f(0)\le f(t),
\]
which entails \(f(0)\le f(t)\): for Boolean elements \(a,b\), the condition \(a\triangle b\le a\) forces \(b\le a\).

Next, let \(s\le t\). Since \(s\triangle0=s\le t\), the quasi-equation gives \(f(s)\triangle f(0)\le f(t)\). Combined with \(f(0)\le f(t)\), the Boolean identity \(u\le(u\triangle v)\vee v\) yields \(f(s)\le f(t)\). Thus \(f\) is monotone.

Fix arbitrary \(a,b\in B\), and put \(c=a\vee b\). Since \(a\le c\), monotonicity gives \(f(a)\le f(c)\). Moreover,
\[
a\triangle c=b\wedge\neg a\le b.
\]
Applying \((\ast)\) with \(x=a,y=c,z=b\) gives
\[
f(a)\triangle f(c)\le f(b).
\]
Using \(f(a)\le f(c)\), we obtain
\[
f(c)=f(a)\vee(f(a)\triangle f(c))\le f(a)\vee f(b).
\]
The opposite inequality follows from monotonicity and \(a,b\le c\). Hence \(f(a\vee b)=f(a)\vee f(b)\).

Conversely, suppose \(f\) preserves binary joins. Then it is monotone. If \(x\triangle y\le z\), Boolean order implies \(x\le y\vee z\) and \(y\le x\vee z\). Therefore
\[
f(x)\le f(y)\vee f(z),\qquad f(y)\le f(x)\vee f(z).
\]
These two inequalities imply \(f(x)\triangle f(y)\le f(z)\), proving \((\ast)\).

For the finite census, fix an output atom \(j\in[n]\) and define the Boolean-valued coordinate \(h_j(S)=1\) if and only if \(j\in f(S)\). Join preservation is equivalent, coordinatewise, to \(h_j(S\cup T)=h_j(S)\lor h_j(T)\). If \(h_j(\varnothing)=1\), monotonicity makes \(h_j\) constantly \(1\). Otherwise \(h_j(\varnothing)=0\), and \(h_j\) is determined by an arbitrary chosen subset \(I_j\subseteq[n]\):
\[
h_j(S)=1\quad\Longleftrightarrow\quad S\cap I_j\ne\varnothing.
\]
There are \(2^n+1\) choices per output atom, independently, giving \((2^n+1)^n\). Under \(f(0)=0\) the constant-one choice is excluded, giving \(2^{n^2}\).

Finally, in [1, Example 2.2] take \(B=\mathcal P(\{1,2,3\})\), with \(f(\{1,3\})=\{1,2,3\}\) and \(f(S)=S\) for all other sets. Put
\[
x=\{1\},\qquad y=\{1,3\},\qquad z=\{3\}.
\]
Then \(x\triangle y=\{3\}\subseteq z\), whereas
\[
f(x)\triangle f(y)=\{2,3\}\not\subseteq f(z)=\{3\}.
\]
This directly refutes the example's asserted satisfaction of \((\ast)\). An even shorter reason is that the example is visibly non-additive, and the equivalence just proved excludes it.

## Verification

The accompanying standalone `checker.py` tests every Boolean-valued operation on the powerset algebras with one through four atoms (not every vector-valued operation, which is unnecessary because the condition separates output coordinates). For each it checks the full quasi-equation by enumerating all triples, then independently checks binary-join preservation. The two predicates agree in all tested cases, with \(3,5,9,17\) admissible scalar maps respectively. It also checks the source example's explicit failing triple. Execute `python3 checker.py`. These finite checks corroborate but do not replace the all-Boolean-algebra proof.

## Relationship to prior work

Gyenis, Molnár and Öztürk [1, Fact 2.1 and Example 2.2, Section 2] use \((\ast)\) as a purported *strictly weaker than additive* sufficient hypothesis for congruence extension, asserting that their non-additive eight-element operation satisfies it. The present equivalence shows that the advertised strict distinction does not occur under the displayed quantifiers and Boolean-algebra definitions. Fact 2.1's implication from \((\ast)\) to congruence extension remains valid (it reduces to the standard additive case); what fails is the claimed strict separation and the application of this premise to that example.

The related complete census of the first finite carrier where CEP can fail [2] concerns the **CEP property itself**, not the class cut out by \((\ast)\). It neither states nor implies this equivalence or the displayed \((2^n+1)^n\) formula. Standard descriptions of join-preserving maps motivate the counting argument but do not settle the specific incorrect separation asserted in [1].

## Limitations

This result concerns the quasi-equation *as printed* in [1]. It does not determine whether a modified inequality might be strictly weaker than additivity and still imply CEP. The equality of \((\ast)\) with binary additivity does **not** assert that CEP itself is equivalent to additivity. No conclusion is drawn here about the truth of [1, Theorems 2.3 or 2.6] independent of their quoted use of \((\ast)\); alternative arguments may establish their conclusions. Earlier literature under a different formulation of Boolean nonexpansiveness may contain the equivalence; a full historical-priority guarantee is not made.

## References

[1] Zalán Gyenis, Zalán Molnár and Övge Öztürk, “More on modal logics and deduction,” arXiv:2603.17724v1, first publicly posted 18 March 2026. Section 2, especially Fact 2.1, Example 2.2 and Theorem 2.6. https://arxiv.org/html/2603.17724v1

[2] “Eight elements are the sharp finite CEP threshold for Boolean frames,” published mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-eight-elements-are-the-sharp-finite-cep-threshold-for-boolean-fr--d55c70b114c5
