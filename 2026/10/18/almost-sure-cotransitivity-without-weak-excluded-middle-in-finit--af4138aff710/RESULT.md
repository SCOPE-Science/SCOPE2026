# Almost-sure cotransitivity without weak excluded middle in finite Heyting stars

## Finding

**Theorem (exact cotransitivity degree and asymptotic reversal).** Let \(m\geq1\) be an integer. Let \(P_m\) be the finite ordered set with a single least point \(r\) and exactly \(m\) pairwise incomparable maximal points above \(r\), and let \(H_m=\operatorname{Up}(P_m)\) be the finite Heyting algebra of upsets. For \(x,y\in H_m\), set
\[
 a(x,y)=\neg\bigl((x\to y)\wedge(y\to x)\bigr).
\]
Let \(C(x,y,z)\) be the cotransitivity equation
\[
 a(x,y)\to\bigl(a(x,z)\vee a(z,y)\bigr)=\top.
\]
With three independently uniform elements of \(H_m\), the exact probability of \(C\) is
\[
 \boxed{\operatorname{ds}_{H_m}(C)
 =1-\frac{(2^m-2)(2^m+3)}{(2^m+1)^3}.}
\]
For a uniformly chosen \(x\in H_m\), the exact probability of weak excluded middle, \(\neg x\vee\neg\neg x=\top\), is
\[
 \boxed{\operatorname{ds}_{H_m}(\mathrm{WEM})=\frac{3}{2^m+1}.}
\]
In particular, every \(m\geq2\) gives a finite Heyting algebra in which the displayed cotransitivity equation fails, yet
\[
 \operatorname{ds}_{H_m}(C)\longrightarrow1,
 \qquad\operatorname{ds}_{H_m}(\mathrm{WEM})\longrightarrow0.
\]
More precisely, \(1-\operatorname{ds}_{H_m}(C)=2^{-m}+O(4^{-m})\). Hence this natural three-variable cotransitivity equation has **no positive finite satisfiability gap** over the class of finite Heyting algebras.

## Assumptions and scope

An **upset** of a poset \(P\) is a subset \(U\subseteq P\) for which \(p\in U\) and \(p\leq q\) imply \(q\in U\). In \(H_m\), meet and join are intersection and union. The Heyting implication \(U\to V\) is the greatest upset \(W\) satisfying \(U\cap W\subseteq V\); \(\neg U=U\to\varnothing\). The number \(\operatorname{ds}_{H_m}(E)\) is the fraction of uniformly selected assignments to all free variables satisfying equation \(E\). The algebra contains \(2^m+1\) elements, and its top element is the *whole poset*, not the upset of all maximal points. All statements refer to this explicit finite family; no formula for other frames is asserted.

The operation \(a(x,y)\) is the canonical negated-Heyting-biconditional apartness candidate studied in the literature. Its irreflexivity and symmetry are valid in every Heyting algebra; cotransitivity is the remaining property at issue. The theorem concerns the equation \(C\), not an assertion that \(a\) is an apartness relation on \(H_m\) when \(m\geq2\). The elementary WEM count is included to quantify the contrast; the original contribution asserted here is the exact **cotransitivity** count and consequent no-gap/contrasting-limits phenomenon, not a new general WEM-counting formula.

## Proof

Let \(M=\{v_1,\ldots,v_m\}\) be the maximal points and set \(s=2^m\). Each upset is either \(U_S=S\) for a unique \(S\subseteq M\), or the distinguished top \(\top=P_m\). Write \(\pi(x)=x\cap M\). Every \(S\neq M\) has exactly one preimage under \(\pi\), while \(M\) has two: \(U_M\) and \(\top\). Thus \(|H_m|=s+1\).

**Step 1: the exact apartness values.** For any upsets \(x,y\), the maximal-point trace of \(x\to y\) consists exactly of the maximal points not belonging to \(\pi(x)\setminus\pi(y)\). Its root belongs to \(x\to y\) if and only if \(x\subseteq y\). Hence the maximal-point trace of \(x\leftrightarrow y=(x\to y)\wedge(y\to x)\) is \(M\setminus D\), where \(D=\pi(x)\mathbin{\triangle}\pi(y)\). The biconditional has the root exactly when \(x=y\). For an upset \(U_T\) lacking the root, its negation is \(\top\) when \(T=\varnothing\), and is \(U_{M\setminus T}\) otherwise. Moreover \(\neg\top=\varnothing\). Therefore
\[
 a(x,y)=\begin{cases}
 \varnothing,&D=\varnothing,\\
 U_D,&\varnothing\neq D\subsetneq M,\\
 \top,&D=M.
 \end{cases}
\]
This formula also handles the distinct elements \(U_M\) and \(\top\), which have the same maximal-point trace and apartness value \(\varnothing\).

**Step 2: a complete characterization of failed triples.** Put \(D_{xy}=\pi(x)\mathbin{\triangle}\pi(y)\). For every three traces,
\[
 D_{xy}\subseteq D_{xz}\cup D_{zy}.
\]
If \(D_{xy}\neq M\), Step 1 and this inclusion show that \(a(x,y)\leq a(x,z)\vee a(z,y)\); the case \(D_{xy}=\varnothing\) is immediate. If \(D_{xy}=M\), the left side is \(\top\), and its right side equals \(\top\) precisely when either \(D_{xz}=M\) or \(D_{zy}=M\). Because \(\pi(x)\) and \(\pi(y)\) are complementary, this happens precisely when
\[
 \pi(z)\in\{\pi(x),\pi(y)\}.
\]
Consequently a triple fails \(C\) *if and only if* \(\pi(x)\) and \(\pi(y)\) are complementary subsets of \(M\), while \(\pi(z)\) is different from both.

**Step 3: exact counting.** There are \(s-2\) ordered complementary trace-pairs for which neither trace is \(\varnothing\) or \(M\). Each lifts to one ordered pair \((x,y)\), and admits \((s+1)-2=s-1\) failing choices of \(z\). The two ordered complementary endpoint trace-pairs \((\varnothing,M)\) and \((M,\varnothing)\) each lift to two ordered pairs \((x,y)\), because \(\pi^{-1}(M)\) has two elements. For each of these four pairs, the two permitted traces for \(z\) account for three actual elements, giving \((s+1)-3=s-2\) failing choices. Thus the total number of failed triples is exactly
\[
 (s-2)(s-1)+4(s-2)=(s-2)(s+3).
\]
Dividing by the \((s+1)^3\) ordered triples proves the cotransitivity formula.

**Step 4: weak excluded middle.** One has \(\neg U_S=U_{M\setminus S}\) whenever \(S\neq\varnothing\), and \(\neg U_\varnothing=\top\). For every nonempty proper \(S\subsetneq M\), double negation returns \(U_S\), so \(\neg U_S\vee\neg\neg U_S=U_M<\top\). The only successes are \(U_\varnothing\), \(U_M\), and \(\top\). This proves the probability \(3/(s+1)\), including \(m=1\). For \(m\geq2\), \(s-2>0\), so neither WEM nor cotransitivity is universally valid (neither is an identity). Nonetheless the respective satisfaction probabilities tend to \(0\) and \(1\), and \((s-2)(s+3)/(s+1)^3=s^{-1}+O(s^{-2})\). This proves the no-gap assertion.

## Verification

An accompanying standalone Python 3 program, `verify_apartness.py`, builds the poset and all its upsets, computes each Heyting implication directly from its right-adjoint universal property rather than from the proof's trace formula, and checks cotransitivity on every ordered triple. It separately evaluates weak excluded middle. Run from the same directory:

```sh
python3 verify_apartness.py
```

For \(m=1,\ldots,7\) this checks \(2{,}463{,}045\) triples. The respective numbers of failed triples are \(0,14,66,266,1050,4154,16506\); the respective numbers of elements failing WEM are \(0,2,6,14,30,62,126\). All agree with the theorem. The arbitrary-\(m\) proof is combinatorial, and finite enumerations do not constitute its general proof.

For an explicit failure when \(m\geq2\), choose a maximal point \(v\) and set \(x=U_\varnothing\), \(y=U_M\), \(z=U_{\{v\}}\). Then \(a(x,y)=\top\), but \(a(x,z)\vee a(z,y)=U_M<\top\).

## Relationship to prior work

Kocsis, *Apartness relations between propositions* (first public preprint 2022-09-08, arXiv:2209.03920), Proposition 3.7, proves that \(a(x,y)\) is cotransitive throughout a Heyting algebra exactly when weak excluded middle holds throughout. The present theorem asks a different quantitative question: what fraction of triples satisfy cotransitivity *when it fails globally*? It proves that the local success frequency may tend to one even as almost every element fails WEM.

A previously established general weak-excluded-middle/double-negation counting formula for finite upset algebras already specializes to three WEM solutions for this one-root family; that subcount is not claimed as a novel standalone invariant. It is also verified directly in Step 4 above to make the comparison self-contained.

Bumpus and Kocsis, *Degree of Satisfiability in Heyting Algebras* (first public preprint 2021-10-21, arXiv:2110.11515), introduce the finite satisfiability gap perspective. Their Theorem 3.15 uses the same Boolean-plus-new-top Heyting family to show lack of a gap for a **different** equation, material implication. That result neither states the cotransitivity count nor implies the simultaneous near-universal failure of WEM and near-universal satisfaction of cotransitivity. This use of an established family is acknowledged; the new content is its exact cotransitivity count and the resulting contrasting limits.

## Limitations

The theorem establishes no quantitative uniform bound over all finite Heyting algebras and no classification of cotransitivity frequencies on arbitrary frames. Its assertion of no finite gap is an existential family result. It is a mathematical proof and a computational cross-check, not an independent external audit or a guarantee of publication priority. Equivalent earlier counting under different terminology remains possible.

## References

1. Z. A. Kocsis, *Apartness relations between propositions*, arXiv:2209.03920, first public version 2022-09-08; Mathematical Logic Quarterly 70 (2024), 414–428. https://arxiv.org/abs/2209.03920
2. B. M. Bumpus and Z. A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515, first public version 2021-10-21; Journal of Symbolic Logic 90 (2025), 533–551. https://arxiv.org/abs/2110.11515
