# The sharp first nonzero Kreisel–Putnam defect in finite Heyting algebras

## Finding
For a finite nontrivial Heyting algebra \(H\) of cardinality \(h\), let
\[
K(a,b,c)=(\neg a\to(b\vee c))\to((\neg a\to b)\vee(\neg a\to c)),
\qquad
F_{\mathrm{KP}}(H)=|\{(a,b,c)\in H^3:K(a,b,c)\ne\top\}|.
\]
Every positive defect satisfies \(F_{\mathrm{KP}}(H)\ge8\). There is no nonvalid algebra of order below \(9\); the unique nonvalid isomorphism class of order \(9\) is \(J(A_3\oplus A_1)\), and its defect is \(24\).

For **every** integer \(h\ge11\), the bound \(8\) is attained by
\[
H_h=J\left(\bigl((A_1\oplus A_2)\sqcup A_1\bigr)\oplus C_{h-10}\right).
\]
Here \(A_k\) is a \(k\)-point antichain, \(C_t\) is a \(t\)-point chain, \(\sqcup\) is disjoint union, and \(\oplus\) is ordinal sum. Accordingly, for \(h\ge11\), the largest degree of satisfaction of the Kreisel–Putnam equation among nonvalid size-\(h\) algebras is exactly \(1-8/h^3\). This conclusion does not assert attainability for order \(10\).

## Assumptions and scope
All posets and Heyting algebras are finite; the Heyting algebra is nontrivial. By finite distributive-lattice representation, write \(H=J(P)\), the lattice of downsets of a finite poset \(P\). A downset \(A\subseteq P\) is a subset closed under passage to smaller points. Negation, implication, and disjunction are computed in \(J(P)\), not as ordinary set complement or material implication. All triples are ordered and sampled uniformly from \(H^3\). This is the equational Kreisel–Putnam axiom, not the syntactic admissibility of a rule.

## Proof
**1. A local exact failure criterion.** For downsets \(D,E\subseteq P\),
\[
D\to E=\{x\in P:\downarrow x\cap D\subseteq E\},
\qquad
\neg D=P\setminus\uparrow D.
\]
Fix \(A,B,C\in J(P)\). An implication \(X\to Y\) is below top exactly when some \(x\in X\setminus Y\) exists. Thus the displayed Kreisel–Putnam equation fails precisely when there is \(x\in P\) such that, with \(Q=\downarrow x\cap\neg A\),
\[
Q\subseteq B\cup C,\qquad Q\not\subseteq B,\qquad Q\not\subseteq C. \tag{1}
\]
The set \(Q\) is a downset. If it were empty or principal \(\downarrow y\), then \(Q\subseteq B\cup C\) would force \(Q\subseteq B\) or \(Q\subseteq C\), contradicting (1). Consequently \(Q\) has two distinct incomparable maximal points \(u,v\). Moreover \(x\notin\neg A\), since otherwise \(Q=\downarrow x\). The latter gives \(A\cap\downarrow x\ne\varnothing\). Choose a minimal point \(s\) of that set: because \(A\) is a downset, \(s\) is minimal in \(P\), lies in \(A\), and is not in \(Q\). Both \(u\) and \(v\) are incomparable with \(s\) (an element in \(\neg A\) has no predecessor in \(A\), while a predecessor of an element in \(A\) belongs to \(A\)). All three points are below \(x\).

**2. Eight distinct counterexamples.** Hold this fixed antecedent \(A\) and witness \(x\). Set \(B_0=Q\setminus\{u\}\) and \(C_0=\downarrow u\). Both are downsets in \(P\), their union is \(Q\), and neither contains all \(Q\): \(u\notin B_0\), \(v\notin C_0\). Because \(s\) is minimal and outside \(Q\), adding \(s\) independently to \(B_0\) and \(C_0\) preserves downsethood and (1). The two orientations of the ordered pair \((B_0,C_0)\) and its reversal, together with the four independent choices of whether to add \(s\) to each coordinate, produce \(2\cdot2\cdot2=8\) **different** bad ordered triples. Hence every nonzero defect is at least eight.

**3. Sharp smallest carrier.** The four elements \(s,u,v,x\) form an induced subposet \(A_3\oplus A_1\): the first three are mutually incomparable, each lies strictly below \(x\). Restriction \(J(P)\to J(\{s,u,v,x\})\) is surjective (a downset of the induced subposet extends to its generated downset in \(P\)). Since \(J(A_3\oplus A_1)\) has exactly \(2^3+1=9\) elements, a nonvalid \(H\) has at least nine elements. If equality holds, the restriction is a lattice isomorphism, and by the uniqueness of the poset of join-irreducibles \(P\cong A_3\oplus A_1\). Here the only bad antecedents are the three singleton minimal-point downsets. For each there are exactly two opposite ways of distributing the other two minimal points between the consequents, with two independent choices for including the antecedent's minimal point. Therefore \(F_{\mathrm{KP}}(J(A_3\oplus A_1))=3\cdot2\cdot2^2=24\).

**4. Eight failures at every order above ten.** Let \(\ell=h-10\ge1\), and let \(R=(A_1\oplus A_2)\sqcup A_1\). Label the fork points \(r<u,r<v\), and call the isolated minimal point \(s\). Put a chain of \(\ell\) points above all of \(R\). There are \(5\cdot2=10\) downsets of \(R\), and precisely one additional downset for each upper-chain point, so \(|J(R\oplus C_\ell)|=10+\ell=h\).

Every possible downset antecedent \(A\) is one of four types: \(A=\varnothing\), \(A=\{s\}\), \(r\in A, s\notin A\), or \(r,s\in A\). In those cases respectively, \(\neg A=P\), \(\neg A=\{r,u,v\}\), \(\neg A=\{s\}\), or \(\neg A=\varnothing\). When \(\neg A\) is empty or a singleton, (1) is impossible; if \(A=\varnothing\), then \(\neg A=P\), so (1) is impossible because \(Q=\downarrow x\) is principal. Hence only \(A=\{s\}\) can fail. For this antecedent (1) is possible only when \(x\) lies in the upper chain, where \(Q=\{r,u,v\}\). Necessarily \(B\) and \(C\) include \(r\) and distribute \(u,v\) one to each, with independent optional inclusion of \(s\); neither can contain a chain point. There are exactly \(2\cdot2^2=8\) bad triples. Therefore every \(h\ge11\) has a nonvalid algebra attaining eight, and its uniform satisfaction fraction is \(1-8/h^3\). This completes the proof.

## Verification
The standalone program `verify_kp_first_defect.py` enumerates all \(5{,}231\) naturally labeled finite posets on up to six points. It directly computes the Heyting implication and ordered Kreisel–Putnam failures; on posets through five points it independently checks the local condition (1). Its observed numbers of nonvalid labeled posets by ground-set size \(1,2,3,4,5,6\) are \(0,0,0,1,38,1212\). It checks that the unique nine-element bad algebra from four points has 24 failures. It also checks the explicit all-size family for \(11\le h\le30\), finding exactly eight bad triples in each case. Run `python3 verify_kp_first_defect.py` with standard Python 3. Finite tests support but do not replace the proof of the universal statements.

## Relationship to prior work
Bumpus and Kocsis, *Degree of Satisfiability in Heyting Algebras* (first public preprint 2021-10-21, arXiv:2110.11515) initiate quantitative satisfiability questions for Heyting algebras and study multiple classical principles. Chagrov and Zakharyaschev's *Modal Logic* (1997), Exercise 2.10, treats the **qualitative** frame condition for the Kreisel–Putnam axiom. Pezlar's *Constructive validity of a generalized Kreisel–Putnam rule* (arXiv:2311.15376) analyzes proof-theoretic admissibility and constructive validity of a related rule. These established frameworks and qualitative facts are not being claimed as new. The quantitative eight-failure lower bound, the nine-element boundary with 24 failures, and the sharp all-carrier-size family are the present assertions.

## Limitations
No extremal assertion is made for carrier size ten. Results concern *finite* Heyting algebras and the equational axiom, not rule admissibility, infinite structures, weighted sampling, or complete numerical distributions of defect counts. The computational census is finite; no independent mathematical audit has been performed. Exact historical priority under alternative algebraic/semantical formulations remains uncertain, and inaccessible specialist sources could contain equivalent count bounds.

## References
1. B. M. Bumpus and Z. A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515, first public 2021-10-21, https://arxiv.org/abs/2110.11515.
2. A. Chagrov and M. Zakharyaschev, *Modal Logic*, Oxford Logic Guides 35, Clarendon Press, 1997, Exercise 2.10.
3. I. Pezlar, *Constructive validity of a generalized Kreisel–Putnam rule*, arXiv:2311.15376, first public 2023-11-26, https://arxiv.org/abs/2311.15376.
