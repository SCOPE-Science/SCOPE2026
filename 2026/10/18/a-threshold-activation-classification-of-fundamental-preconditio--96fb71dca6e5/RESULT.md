# A threshold–activation classification of fundamental preconditionals on long pentagon lattices

## Finding

For each integer \(m\ge 2\), let \(L_m\) be the bounded lattice with elements
\[
0<c_1<c_2<\cdots<c_m<1,\qquad 0<u<1,
\]
where \(u\) is incomparable with every \(c_i\). Thus \(u\wedge c_i=0\) and \(u\vee c_i=1\), and \(L_2\) is the five-element nondistributive pentagon \(N_5\).

A fundamental \(\mathsf F\)-preconditional is a binary operation \(\to\) satisfying the five preconditional axioms, conditional identity, semicomplementation, and double-negation inflation recalled below. The number of such operations on the fixed labelled lattice \(L_m\) is exactly
\[
\boxed{A_m=m!+\sum_{j=1}^{m}(m-j+1)^j(m-j)!}.
\]
In particular \(A_2=5\), \(A_3=17\), \(A_4=75\), and \(A_5=407\). These are also isomorphism-class counts because the bounded lattice \(L_m\) has no nonidentity automorphisms for \(m\ge2\).

More precisely, every operation is uniquely described by a threshold \(j\in\{0,\ldots,m\}\) and independently chosen activation times
\[
\tau_s\in\{\max(j+1,s+1),\ldots,m,m+1\}
\quad (1\le s<m).
\]
Here \(m+1\) signifies that \(c_s\) is never fixed by a non-top antecedent. The resulting operation is explicitly described in the proof. The threshold \(j\) is recovered from the negation \(\neg a:=a\to0\). The case \(j=0\) contributes \(m!\) operations; each \(j\ge1\) contributes \((m-j+1)^j(m-j)!\).

## Assumptions and scope

We use the preconditional axioms of Holliday and Chen, with lattice order \(\le\), minimum \(0\), and maximum \(1\):
\[
\begin{array}{ll}
\mathrm{(P1)}&1\to b\le b,\\
\mathrm{(P2)}&a\wedge b\le a\to b,\\
\mathrm{(P3)}&a\to b\le a\to(a\wedge b),\\
\mathrm{(P4)}&a\to(b\wedge c)\le a\to b,\\
\mathrm{(P5)}&a\to((a\wedge b)\to c)\le(a\wedge b)\to c.
\end{array}
\]
The additional \(\mathsf T\) axioms are \(a\to a=1\) and \(a\wedge(a\to0)=0\). The \(\mathsf F\) axiom is \(a\le\neg\neg a\), where \(\neg a=a\to0\). All axioms quantify over every element of \(L_m\).

From (P3), (P4), and (P2), the standard consequences are
\[
a\to b=a\to(a\wedge b),\qquad b\le c\Longrightarrow a\to b\le a\to c.
\]
Indeed (P4) gives one comparison with \(a\wedge b\), and (P3) gives the other. These facts, rather than any assumption of distributivity, are used throughout.

## Proof

**Step 1: the possible negations.** By conditional identity and monotonicity in the consequent, \(0\to b=1\) for all \(b\); by (P1), (P2), \(1\to b=b\). Hence \(\neg0=1\), \(\neg1=0\). The negation map is antitone: for \(a\le b\), (P5) with outer antecedent \(b\), inner antecedent \(a\), and consequent \(0\) says \(b\to(a\to0)\le a\to0\). Consequent monotonicity and \(0\le a\to0\) give \(b\to0\le b\to(a\to0)\). Therefore \(\neg b\le\neg a\).

Semicomplementation forces \(\neg c_i\in\{0,u\}\) for \(1\le i\le m\), and \(\neg u\in\{0,c_1,\ldots,c_m\}\). If \(\neg u=0\), double-negation inflation forbids \(\neg c_i=u\), since then \(c_i\le\neg\neg c_i=\neg u=0\). Hence every \(\neg c_i=0\): this is \(j=0\).

If \(\neg u=c_j\) for \(j\ge1\), double-negation inflation for \(u\) requires \(u\le\neg c_j\), hence \(\neg c_j=u\). By antitonicity, every \(i<j\) has \(\neg c_i\ge\neg c_j=u\), hence \(\neg c_i=u\). For \(i>j\), double-negation inflation excludes \(\neg c_i=u\), because it would imply \(c_i\le\neg u=c_j<c_i\). We have exactly
\[
\neg u=\begin{cases}0&j=0,\\c_j&1\le j\le m,\end{cases}
\qquad
\neg c_i=\begin{cases}u&i\le j,\\0&i>j.\end{cases}
\]

**Step 2: rows outside the chain tail.** For every \(a\), \(a\to b=a\to(a\wedge b)\) and conditional identity imply \(a\to b=1\) when \(a\le b\). For the row \(u\), the only possible meets are \(0,u\), so
\[
u\to b=\begin{cases}1&u\le b,\\c_j&u\nleq b,\ j>0,\\0&u\nleq b,\ j=0.\end{cases}
\]
For \(i\le j\), \(c_i\to0=u\). Whenever \(0<c_s<c_i\), (P2) gives \(c_s\le c_i\to c_s\), and consequent monotonicity gives \(u=c_i\to0\le c_i\to c_s\). The only joint upper bound of \(c_s\) and \(u\) is \(1\). Therefore
\[
c_i\to b=\begin{cases}u&c_i\wedge b=0,\\1&c_i\wedge b\ne0\end{cases}
\quad (i\le j).
\]
The zero and top antecedent rows are fixed as above.

**Step 3: the remaining chain rows.** For every \(i>j\), \(c_i\to0=0\), \(c_i\to b=1\) whenever \(c_i\le b\), and for \(0<c_s<c_i\) the value lies in the chain interval \([c_s,1]\): it cannot be \(u\), because that would violate (P2). The consequent map on \([0,c_i]\) is extensive and monotone. Apply (P5) with the same antecedent twice to obtain
\[
c_i\to(c_i\to b)\le c_i\to b.
\]
If the right side is below \(1\), it is a chain point below \(c_i\) (above \(c_i\) the row is constantly \(1\)), and extensivity supplies the reverse inequality. If it is \(1\), equality is immediate. Thus the row is idempotent. Let
\[
F_i=\{s:1\le s<i,\ c_i\to c_s=c_s\}.
\]
The row is exactly the ceiling operation
\[
c_i\to b=\begin{cases}
0&c_i\wedge b=0,\\
1&c_i\wedge b=c_i,\\
c_t&t=\min\{h\in F_i:h\ge s\}\text{ exists},\ c_i\wedge b=c_s,\\
1&\text{otherwise}.
\end{cases}
\]
For \(j<i<k\), (P5) with outer \(c_k\), inner \(c_i\), and consequent \(c_s\) shows \(F_i\subseteq F_k\): if \(s\in F_i\), then \(c_k\to c_s\le c_s\), while (P2) gives the reverse inequality.

Conversely, for each threshold \(j\) take any nested family
\[
F_{j+1}\subseteq F_{j+2}\subseteq\cdots\subseteq F_m,
\qquad F_i\subseteq\{1,\ldots,i-1\},
\]
and define the rows exactly as above. (P1)–(P4), conditional identity, semicomplementation and double-negation inflation are immediate from the explicit rows. To check (P5), write \(d=a\wedge b\) and \(y=d\to c\). The inequality to check is \(a\to y\le y\). If \(d=0\) then \(y=1\); if \(a=1\), the outside row is the identity. If \(d=u\), then \(a\) is \(u\) or \(1\), and the row is idempotent on its only possible values \(0,c_j,1\). If \(d=c_k\) with \(k\le j\), then \(y\in\{u,1\}\); any eligible outer chain row with index \(>j\) sends \(u\) to \(0\), and any special outer chain row sends \(u\) to \(u\), so the inequality holds. If \(d=c_k\) with \(k>j\), then \(y\in\{0,1\}\cup\{c_s:s\in F_k\}\); the outside row is either the same chain row or a later chain row, which fixes \(0\), \(1\), and by nesting every \(c_s\) that \(d\to c\) fixes. This proves (P5).

**Step 4: independent activations and count.** Each index \(1\le s<m\) may first enter the nested fixed-point families in row \(i\ge\max(j+1,s+1)\), or never. Encode never by \(\tau_s=m+1\); all these times are independent. For \(j=0\) there are \(m-s+1\) choices for each \(s\), hence \(m!\) operations. For \(1\le j\le m\), there are \(m-j+1\) choices for each \(s\le j\), and \(m-s+1\) choices for each \(s>j\), giving \((m-j+1)^j(m-j)!\). Different thresholds have different negations, and different activations have different row fixed points, establishing uniqueness and the formula.

## Verification

The standalone Python program `verify_pentagon_preconditionals.py` tests the original five quantified axioms and all three \(\mathsf F\)-conditions on the constructed tables for \(1\le m\le5\). It separately generates *all* binary operations compatible with the necessary row-monotonicity, meet-dependence, identity and semicomplementation constraints, checks every remaining axiom, and compares complete table sets for \(1\le m\le4\). The raw exhaustive searches and the normal-form constructions coincide exactly. The observed counts \(2,5,17,75,407\) agree with the formula; the m=1 Boolean boundary is included as a control, not part of the new family theorem. The output ends `LONG_PENTAGON_PRECONDITIONAL_VERIFY_OK`.

The proof above is for every \(m\ge2\); finite experiments do not establish its infinite family claim.

## Relationship to prior work

Chen [1] defines the fundamental \(\mathsf K/\mathsf T/\mathsf F\) hierarchy and proves completeness and finite-model properties. Holliday [2] studies preconditional representations and associated negation properties. Neither inspected source states the threshold–activation classification on the long pentagon \(L_m\) or the count \(A_m\). Published classifications [3,4] treat finite **chains**, where all comparable lower consequences behave differently, rather than lattices with an incomparable atom; their factorial formulas are not a classification of \(L_m\).

The first nonmodular member \(L_2=N_5\), and the full family retains exactly one non-chain arm while varying the other arm's height. Its additional negation threshold and consequent-closure activations explain how the nonmodular obstruction changes the conditional algebra. No claim of absolute historical priority is made: an older general finite-lattice characterization could imply the formula without using this terminology.

## Limitations

The result counts labelled \(\mathsf F\)-preconditional operations on \(L_m\); it does not count arbitrary \(\mathsf K\)-preconditionals, relational presentations, or expansions of all nondistributive lattices. The operation is uniquely determined by its threshold and activation data, but no general complexity result or previously unknown logical axiom is claimed. Novelty comparisons cannot exclude uncatalogued older algebraic characterizations. No independent audit has been performed.

## References

[1] Zhicheng Chen, “Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations,” arXiv:2607.20221 (first public version 2026-07-22), https://arxiv.org/abs/2607.20221.

[2] Wesley H. Holliday, “Preconditionals,” arXiv:2402.02296 (2024-02-03), https://arxiv.org/abs/2402.02296.

[3] “Fixed-point normal form for finite-chain preconditionals,” https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-fixed-point-normal-form-for-finite-chain-preconditionals--3d55c0067825.

[4] “Factorial classification of preconditionals on finite chains,” https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-factorial-classification-of-preconditionals-on-finite-chains--cbc434a2c6a0.
