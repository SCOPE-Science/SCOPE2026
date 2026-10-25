# A bounded-genus wedge theorem from a finite genus-one locus

## Finding

Let \(C\subset S^3\) be a Cantor set whose local genus \(g_p(C)\) is bounded by a finite integer \(B\), and let
\[
F=\{p\in C:g_p(C)=1\}
\]
be finite. Let \(\{X_s:s\in I\}\) be an uncountable family of pairwise inequivalently embedded rigid generalized Bing–Whitehead Cantor sets in \(S^3\), with simply connected complements and \(g_q(X_s)=1\) at every \(q\in X_s\). Such a family is supplied by Garity, Repovš, and Wright (2014).

Fix any \(x\in C\) and, for each \(s\), a point \(y_s\in X_s\). Form the wedge \(Y_s=(C,x)\vee(X_s,y_s)\) by placing supported copies in tame 3-cells and identifying the marked boundary points. Then:
1. \(\pi_1(S^3\setminus Y_s)\cong\pi_1(S^3\setminus C)\) for every \(s\).
2. Every point of \(Y_s\) has local genus at most \(B+1\).
3. The family \(\{Y_s:s\in I\}\) is uncountable and pairwise inequivalently embedded.

The distinguishing invariant is explicit. Write \(L_1(Y_s)=\{p\in Y_s:g_p(Y_s)=1\}\), and let \(L_1(Y_s)'\) denote the derived set (the points that are non-isolated in \(L_1(Y_s)\), with its subspace topology). Then
\[
\overline{L_1(Y_s)'}^{\,Y_s}=X_s.
\]
Indeed, the wedge point has local genus \(g_x(C)+1\). Away from it, local genus is unchanged. The genus-one locus contributed by \(C\) is finite, so its points are isolated within \(L_1(Y_s)\); the genus-one points of \(X_s\) are dense in \(X_s\). If \(g_x(C)=0\), the wedge point itself belongs to the derived set; otherwise it is omitted from \(L_1(Y_s)\), but is in the closure of \(X_s\setminus\{x\vee y_s\}\). Thus the displayed closure recovers the \(X_s\)-factor. Any ambient equivalence between two \(Y_s\) must consequently induce an ambient equivalence between their \(X_s\)-factors, which is impossible for distinct members of the chosen family. If \(C\) is rigid as well, this recovery also shows that every ambient self-homeomorphism of \(Y_s\) fixes both factors pointwise, so \(Y_s\) is rigid.

## Assumptions and scope

Local genus is the embedding invariant defined using defining sequences of compact 3-manifolds with boundary. “Bounded by \(B\)” means \(g_p(C)\le B\) for every \(p\in C\), with \(B<\infty\). The theorem assumes that \(F\) is finite; it does not assume that \(C\) is rigid or that its complement group is nontrivial. The family \(X_s\) is taken from the published genus-one rigid generalized Bing–Whitehead construction.

## Proof

**Complement group.** The wedge theorem of Garity and Repovš (2013, Theorem 4.7) states that if the complement of the second wedge factor is simply connected, then the fundamental group of the wedge complement is isomorphic to that of the first factor. Its proof applies Seifert–van Kampen to two overlapping open sets: the overlap has fundamental group \(\mathbb Z\), and its inclusion into the simply connected side is trivial. Since \(S^3\setminus X_s\) is simply connected, \(\pi_1(S^3\setminus Y_s)\cong\pi_1(S^3\setminus C)\).

**Bounded local genus.** The local-genus wedge theorem (Garity–Repovš 2013, Theorem 5.4) gives \(g_p(Y_s)=g_p(C)\) for \(p\in C\setminus\{x\}\), \(g_q(Y_s)=g_q(X_s)=1\) for \(q\in X_s\setminus\{y_s\}\), and \(g_{x\vee y_s}(Y_s)=g_x(C)+g_{y_s}(X_s)=g_x(C)+1\). The latter is at most \(B+1\), so all local genera of \(Y_s\) are at most \(B+1\).

**Recovery and inequivalence.** Let \(w_s=x\vee y_s\). The local-genus-one points of \(Y_s\) consist of the genus-one points inherited from \(C\setminus\{x\}\), the points of \(X_s\setminus\{y_s\}\), and also \(w_s\) exactly when \(g_x(C)=0\). Because \(F\) is finite and \(C\) and \(X_s\) meet only at \(w_s\), every inherited genus-one point from \(C\setminus\{x\}\) is isolated in \(L_1(Y_s)\). In contrast, every point of \(X_s\setminus\{y_s\}\) is non-isolated in \(L_1(Y_s)\), since \(X_s\) is perfect and every point of \(X_s\) has local genus one. If \(g_x(C)=0\), then \(w_s\) is also non-isolated in \(L_1(Y_s)\); if \(g_x(C)\ge1\), then \(w_s\notin L_1(Y_s)\). In both cases, the closure of the derived set is exactly \(X_s\). Local genus is preserved by ambient equivalence, so any equivalence \(Y_s\to Y_t\) would carry \(\overline{L_1(Y_s)'}\) onto \(\overline{L_1(Y_t)'}\), giving an equivalence \(X_s\to X_t\). The \(X_s\) were chosen pairwise inequivalent, hence so are the \(Y_s\).

If \(C\) is rigid, an ambient self-homeomorphism of \(Y_s\) preserves the intrinsically recovered \(X_s\) and therefore also \(C\). Rigidity of both factors then forces the homeomorphism to fix every point of \(Y_s\).

## Verification

The proof has three independent steps: the published wedge fundamental-group theorem, the published local-genus formula for wedges, and the derived-set recovery argument above. The genus-one family used here is stated to be rigid, to have simply connected complement, and to have local genus one at every point in the 2014 source; its inequivalence follows from that paper’s Lemma 4.3 and Theorem 4.4. No computational experiment is used as a proof.

## Relationship to prior work

Garity and Repovš (2013) prove that under a finite-local-genus-value condition there are uncountably many inequivalent Cantor sets with the same complement fundamental group. Their Question 8.1 asks whether such examples can be arranged so that the local genera of all sets involved are bounded; their construction uses an increasing sequence of genus values and does not provide that boundedness. Garity, Repovš, and Wright (2014) subsequently provide an uncountable family of rigid genus-one generalized Bing–Whitehead Cantor sets with simply connected complements. The present theorem combines that genus-one family with the earlier wedge and local-genus results and uses the derived set of the genus-one locus to recover the attached factor, yielding a bounded-genus family under the stated finite-locus hypothesis.

## Limitations

This is a conditional theorem, not a construction of a base Cantor set \(C\) with nontrivial complement group and finite genus-one locus. It therefore gives a sufficient condition and a bounded-genus extension for that class, but does not by itself settle the full bounded-genus question for arbitrary nontrivial complement groups. If the genus-one locus of \(C\) is infinite, the recovery argument given here need not work. Independent audit has not been performed.

## References

1. D. J. Garity and D. Repovš, “Inequivalent Cantor Sets in \(\mathbb R^3\) Whose Complements Have the Same Fundamental Group,” *Proceedings of the American Mathematical Society* 141 (2013), no. 8, 2901–2911. arXiv:1307.8111v1. DOI: 10.1090/S0002-9939-2013-11911-8.
2. D. J. Garity, D. Repovš, and D. Wright, “Simply Connected Open 3-Manifolds with Rigid Genus One Ends,” *Revista Matemática Complutense* 27 (2014), 291–304. arXiv:1411.3514v1. DOI: 10.1007/S13163-013-0117-3.
