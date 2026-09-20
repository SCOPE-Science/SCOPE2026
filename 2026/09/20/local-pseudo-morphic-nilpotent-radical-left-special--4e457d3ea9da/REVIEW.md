# Review: local left pseudo-morphic rings with nilpotent radical

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** Let \(n\) be minimal with \(J^n=0\) and choose
\(0\ne a\in J^{n-1}\) with \(Ra=\ell(c)\). The proof has four key points.

First, \(\ell(a)=J\): elements of \(J\) kill \(a\), while every element outside
\(J\) is a unit in a local ring. Hence \(Ra\cong R/J\) is simple and lies in
\(J^{n-1}\).

Second, \(Ra=\ell(c)\) is nonzero proper, so \(0\ne c\in J\). Therefore
\(J^{n-1}c=0\), giving \(J^{n-1}\subseteq\ell(c)=Ra\); the reverse inclusion was
already known. Thus \(J^{n-1}=Ra=\ell(c)\) is simple.

Third, right multiplication by \(c\) is left \(R\)-linear with kernel
\(J^{n-1}\). Its restriction to \(J^i\) yields
\[
J^i/J^{n-1}\cong J^ic\subseteq J^{i+1}.
\]
Downward induction from the simple module \(J^{n-1}\) proves finite left
composition length for \(J\) and then for \(R\).

Fourth, \(R/J^{n-1}\cong Rc\). Because both \(J^{n-1}\) and \(R/J\) are simple,
\(Rc\) and \(J\) have the same finite length. Since \(c\in J\), \(Rc\subseteq J\),
so \(Rc=J\). Nilpotence of \(J\) makes \(c\) nilpotent, and the standard
left-special equivalence applies.

The argument was checked for sidedness: maps \(r\mapsto ra\) and \(r\mapsto rc\)
are homomorphisms of left modules; powers \(J^i\) are two-sided ideals; and
\(J^ic\subseteq J^{i+1}\). The case \(J=0\) is separately harmless because a
local semiprimitive ring is a division ring and has \(J=R0\).

## Originality

**PASS, to the best of our knowledge.** Camillo--Nicholson (2015) explicitly ask
whether a local left pseudo-morphic ring with nilpotent Jacobson radical must be
left special, equivalently whether \(J=Rc\) for some \(c\). The theorem proves a
stronger statement: only one nonzero element of the last radical power needs to be
left pseudo-morphic.

The journal's citation list for the 2015 paper and targeted searches under
pseudo-morphic, principal-annihilator, CEFR, local-ring, nilpotent-radical and
left-special terminology were checked through current literature. Alkan--Nicholson--Özcan
(2018) obtain related structure results for the stronger comorphic condition. Quynh--Koşan--Žemlička
(2025) study a stronger property (P) within the pseudo-morphic family and derive
chain-type structure under additional hypotheses. Neither accessible statement
covers the theorem above.

The main unresolved originality risk is Neishabouri--Tolooei--Bagheri (2023).
Its accessible abstract identifies left pseudo-morphic rings with CEFR left regular
modules and states that further properties are obtained, but the full text was not
inspected. An equivalent local nilpotent-radical theorem phrased in CEFR language
would supersede the originality claim. Searches using both terminologies did not
locate such a statement in indexed material.

The Camillo--Nicholson corrigendum changes Lemma 5.6 and Theorem 5.7 in the
semiprime part of the 2015 paper. It does not alter Question 1, the definition of
left pseudo-morphic rings, or the left-special equivalence used here.

## Value

**PASS.** The result gives a short affirmative solution to an explicit published
question and strengthens it to a one-witness criterion in the last nonzero radical
layer. The proof also shows that finite left length, not assumed a priori, is forced
by nilpotence together with that single annihilator representation. The conclusion
places the whole local nilpotent-radical left pseudo-morphic class inside the
well-understood left-special/uniserial finite-length class.

## Scientific limitations

Originality remains qualified by the inaccessible full text of the 2023 CEFR paper
and by the possibility of an equivalent result under different annihilator/module
terminology. No independent formalization is supplied. The result concerns local
rings with nilpotent Jacobson radical and does not address local left pseudo-morphic
rings with non-nilpotent radical or nonlocal rings.

## Sources checked

- V. Camillo and W. K. Nicholson, *On Rings Where Left Principal Ideals Are Left Principal Annihilators*, IEJA 17 (2015), DOI 10.24330/ieja.266221.
- V. Camillo and W. K. Nicholson, corrigendum, IEJA 18 (2015), DOI 10.24330/ieja.266208.
- W. K. Nicholson and E. Sánchez Campos, *Principal Rings with the Dual of the Isomorphism Theorem*, Glasgow Math. J. 46 (2004), DOI 10.1017/S0017089503001654.
- M. Alkan, W. K. Nicholson and A. Ç. Özcan, *Comorphic rings*, J. Algebra Appl. 17 (2018), DOI 10.1142/S0219498818500755.
- P. Neishabouri, Y. Tolooei and S. Bagheri, *On modules in which every finitely generated submodule is a kernel of an endomorphism*, Comm. Algebra 51 (2023), DOI 10.1080/00927872.2022.2115504; abstract inspected, full text not inspected.
- T. C. Quynh, M. T. Koşan and J. Žemlička, *A new member of Nicholson's morphic folks*, J. Algebra 664 (2025), DOI 10.1016/j.jalgebra.2024.10.009.
