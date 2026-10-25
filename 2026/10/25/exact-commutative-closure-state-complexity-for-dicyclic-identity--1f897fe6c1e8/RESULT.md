# Exact commutative-closure state complexity for dicyclic identity languages

## Finding
For every integer \(m\ge2\), the commutative closure of the identity word language of the dicyclic group \(\operatorname{Dic}_m\) with its two standard **positive** generators has exactly \(7m-1\) states in its minimal complete deterministic finite automaton (DFA). The underlying group language has exactly \(4m\) states. The increase comes from a strict finite threshold at \(m\) copies of the cyclic generator and from distinguishing the zero-count axis from positive counts of the other generator.

The theorem includes an exact Parikh membership criterion and an explicit classification of all right quotients, for every \(m\ge2\). It does not assert a worst-case bound over all group languages or all generating sets.

## Assumptions and scope
Let
\[
G_m=\operatorname{Dic}_m=\langle a,b\mid a^{2m}=1,\ b^2=a^m,\ b^{-1}ab=a^{-1}\rangle,\qquad m\in\mathbb Z,\quad m\ge2.
\]
This is the standard dicyclic group of order \(4m\), with normal forms \(a^k b^e\), where \(0\le k<2m\) and \(e\in\{0,1\}\). At \(m=2\), it is the ordinary quaternion group of order eight. Here the alphabet consists of the **two letters** \(a,b\) (not their inverses); these are interpreted by their namesake group elements. Write
\[
W_m=\{w\in\{a,b\}^*:w=1\text{ in }G_m\},\qquad
L_m=\operatorname{perm}(W_m).
\]
The operator \(\operatorname{perm}\) closes a language under arbitrary permutations of the letter positions. Since the language is commutative, membership depends only on \(r=|w|_a\) and \(s=|w|_b\). We count complete, accessible, pairwise inequivalent DFA right-quotient states, and include the empty word. These conventions matter for the number of states.

## Proof
**1. Membership from normal forms.** When \(s=0\), the sole product is \(a^r\), so an identity occurs exactly when \(2m\mid r\). When \(s>0\), we may move all occurrences of \(b\) to the right using \(ba=a^{-1}b\). By placing exactly \(t\) of the \(r\) occurrences of \(a\) immediately after the first \(b\) and before every subsequent \(b\), for arbitrary \(0\le t\le r\), one realizes the normal form \(a^{r-2t}b^s\). Conversely, every ordering produces some exponent of this form because an occurrence of \(a\) picks up either a plus or a minus sign as it passes the \(b\)'s. Thus the complete set of possible exponents is \(r,r-2,\ldots,-r\).

An odd \(s\) leaves an element in the coset \(\langle a\rangle b\) and cannot yield the identity. For \(s\equiv0\pmod4\), we have \(b^s=1\), and a zero exponent exists exactly when \(r\) is even. For \(s\equiv2\pmod4\), we have \(b^s=a^m\); among exponents congruent to \(m\pmod{2m}\), the least possible absolute value is \(m\). Hence an identity exists exactly when \(r\ge m\) and \(r\equiv m\pmod2\). Therefore, with \(P_m(r,s)\) denoting membership, the exact rule is
\[
P_m(r,s)=\begin{cases}
[2m\mid r],&s=0,\\
0,&s\text{ odd},\\
[r\equiv0\pmod2],&s>0,\ s\equiv0\pmod4,\\
[r\ge m]\,[r\equiv m\pmod2],&s\equiv2\pmod4.
\end{cases}
\]
Square brackets are zero-one indicators; all counts range over nonnegative integers.

**2. Explicit right-quotient labels.** At Parikh coordinate \((r,s)\), the complete right quotient is the Boolean function \((u,v)\mapsto P_m(r+u,s+v)\) on nonnegative integer suffix counts. Define labels as follows:
\[
\begin{aligned}
&s=0,\ 0\le r\le m-2: &&A_{\mathrm{low},r};\\
&s=0,\ r\ge m-1: &&A_{\mathrm{res},\,r\bmod2m};\\
&s>0,\ 0\le r\le m-2: &&B_{\mathrm{low},r,\,s\bmod4};\\
&s>0,\ r\ge m-1: &&B_{\mathrm{high},\,s\bmod2,\,\beta_m(r,s)},
\end{aligned}
\]
where \(\beta_m(r,s)=r+m\lceil s/2\rceil\pmod2\). Each label family is entirely reachable, because each displayed coordinate is reachable by a positive word. Their sizes are respectively \(m-1,2m,4(m-1),4\), totaling \(7m-1\).

**3. Equal labels imply equal quotients.** On the \(s=0\) axis, adding a suffix with \(v=0\) gives the \(2m\)-periodic indicator \([2m\mid r+u]\); a suffix with \(v>0\) uses only the rule for the positive \(b\)-count. If \(r\ge m-1\), the threshold test in that rule is redundant whenever the required parity holds: at \(r=m-1\), the parity required for the \(s+v\equiv2\pmod4\) branch is wrong until at least one more \(a\) arrives. It follows that \(r\) and \(r+2m\) induce exactly the same quotient when both are at least \(m-1\). For the low-axis labels, \(r\) itself is fixed and equality is immediate.

For positive \(s\) and \(r\le m-2\), the label determines \(r\) exactly and \(s\bmod4\), which plainly determine the quotient. For positive \(s\) and \(r\ge m-1\), a suffix with \(s+v\) odd is rejected; otherwise the threshold is redundant by the preceding parity observation, and membership becomes
\[
P_m(r+u,s+v)=
\big[u+r+m\lceil s/2\rceil+m\lfloor v/2\rfloor\equiv0\pmod2\big]
\]
when \(s+v\) is even. This depends only on \(s\bmod2\) and \(\beta_m(r,s)\). Hence all equal labels are equivalent.

**4. Distinct labels give distinct quotients.** Consider first the positive-\(s\) region. For any \(v\ge0\), let \(h(v)\) denote the smallest \(u\ge0\) with \(P_m(r+u,s+v)=1\), setting \(h(v)=\infty\) if no such \(u\) exists. In any four consecutive values of \(v\), exactly two give finite values. Of those two, one corresponds to \(s+v\equiv0\pmod4\), with \(h(v)=r\bmod2\in\{0,1\}\). The other corresponds to \(s+v\equiv2\pmod4\), with \(h(v)=m-r\ge2\) if \(r\le m-2\), and \(h(v)\in\{0,1\}\) if \(r\ge m-1\). Consequently the four-value vector \((h(0),h(1),h(2),h(3))\) distinguishes all low labels, determines each low value of \(r\) and the residue \(s\bmod4\), and distinguishes any low label from all high labels. For high labels, \(s\bmod2\) determines which suffix parities can be accepted, and \(\beta_m(r,s)\) determines which parity of \(u\) is accepted for sufficiently large \(u\). The four high labels are therefore distinct.

For axis states with \(s=0\), using only suffixes with \(v=0\) distinguishes all \(2m\) residue labels and forces any potentially equivalent pair to have the same \(r\bmod2m\). In the sole remaining possibility, one coordinate has \(r\le m-2\) and the other is at least \(m-1\) with the same residue. Taking \(v=2\), the low coordinate's first accepted \(u\) is \(m-r\ge2\), whereas the high one's first accepted \(u\) is at most one; so this pair is distinguished. Finally, no axis state can equal any positive-\(s\) state: with \(v=0\), an axis state accepts exactly one residue class of \(u\bmod2m\), while a positive-\(s\) state either accepts no suffixes at all (odd \(s\)) or accepts every second sufficiently large \(u\) (even \(s\)). Because \(m\ge2\), these sets are different.

Thus the \(7m-1\) labels are exactly the Myhill–Nerode classes, and \(\operatorname{sc}(L_m)=7m-1\). The original identity language has \(4m\) states: right multiplication on the \(4m\) group elements gives an accessible DFA, and distinct elements are separated by positive words representing their inverses (every inverse is a positive power in a finite group). This concludes the proof. \(\square\)

## Verification
A self-contained file `verify.py` implements the dicyclic normal-form multiplication and calculates all possible products for each pair of generator counts by an independent dynamic program. It compares the dynamic-program membership with the closed criterion; it also checks that canonical labels are stable under both letter transitions, that the number of labels is exactly \(7m-1\), and that all their tested representative pairs are distinguishable. The script prints `VERIFY_OK` for every parameter \(2\le m\le10\) and a finite grid of counts and suffixes. Run `python3 verify.py` from the extracted artifact directory. The mathematical proof in Sections 1–4 is uniform in \(m\) and does not rely on bounded experimentation.

## Relationship to prior work
Hoffmann's 2020 paper on state complexity of commutative closures of group languages proves effective regularity and a general upper bound depending on the input permutation automaton's state size and letter orders; it does **not** furnish the exact dicyclic-family quotient calculation above. Applied to the regular action of \(G_m\) on itself with generator orders \(2m\) and \(4\), its general bound permits as many as \(128m^3\) states, whereas this theorem identifies exactly \(7m-1\). Hoffmann's further work on shuffle expressions and on product-form minimal automata studies broader closure operations and structural subclasses, not this family's exact minimal quotient partition. The 2013 result of Cano, Guaiana, and Pin establishes regularity for broad language classes under commutation, without a published family-specific count identified here. A separate dihedral-group calculation is not a substitute: the dicyclic relation \(b^2=a^m\) produces the threshold \(r\ge m\) absent from its dihedral quotient, and state-minimality does not transfer along a group quotient.

## Limitations
The statement concerns only the standard two positive generators of the dicyclic groups, not symmetric generating alphabets, arbitrary accepting subsets, or arbitrary presentations. The literature searches and the primary full-text comparisons did not identify an earlier equivalent exact classification, but they cannot establish uniqueness of publication; unindexed and inaccessible treatments remain a residual originality risk. No independent scientific audit is claimed. The computational replay is finite and is not an exhaustive validation of all \(m\).

## References
1. S. Hoffmann, *State Complexity Bounds for the Commutative Closure of Group Languages*, first posted 2020-04-24, arXiv:2004.11772, https://arxiv.org/abs/2004.11772.
2. S. Hoffmann, *The Commutative Closure of Shuffle Expressions over Group Languages is Regular*, first posted 2020-08-12, arXiv:2008.05420, https://arxiv.org/abs/2008.05420.
3. S. Hoffmann, *Commutative Regular Languages with Product-Form Minimal Automata*, first posted 2021-11-26, arXiv:2111.13523, https://arxiv.org/abs/2111.13523.
4. A. Cano, G. Guaiana, and J.-É. Pin, *Regular languages and partial commutations*, Information and Computation 230 (2013), 76–96, https://doi.org/10.1016/j.ic.2013.07.003.
