# Complete equality classification at the ternary \(\mathtt{xyx}\cdot y^{R}\) obstruction
## Finding
For the formula with reversal
\[
\psi_1=\mathtt{xyx}\cdot y^R,
\]
the published maximum length of a ternary avoiding word is \(14\). Exactly six ternary words attain that maximum:
\[
\begin{aligned}
&\mathtt{01200112200120},\qquad
\mathtt{02100221100210},\\
&\mathtt{10211002211021},\qquad
\mathtt{12011220011201},\\
&\mathtt{20122001122012},\qquad
\mathtt{21022110022102}.
\end{aligned}
\]
They are precisely the six alphabet relabelings of
\[
\mathtt{01200112200120}.
\]
The same six-word set is closed under reversal.

## Assumptions and scope
An occurrence of a formula with reversal is a nonerasing morphism respecting reversal such that the image of every fragment is a factor of the ambient word. Thus an occurrence of \(\mathtt{xyx}\cdot y^R\) is determined by nonempty words \(X,Y\) for which both
\[
XYX
\quad\text{and}\quad
Y^R
\]
occur as factors.

The claim concerns ternary words over a labeled three-letter alphabet. Alphabet permutations preserve avoidance. The maximum length \(14\) is prior work; the new statement is the complete equality set and its symmetry structure.

## Proof
Avoidance of a formula is factorial, so exhaustive prefix extension is complete.

Two direct occurrence tests were used. The first enumerates every factor \(F\), every nonempty border \(X\) of \(F\), writes \(F=XYX\), and checks whether \(Y^R\) is also a factor. The second independently enumerates all nonempty factors \(X,Y\) and checks simultaneously whether \(Y^R\) and \(XYX\) are factors.

Prefix generation over the ternary alphabet gives identical level sets for both tests. The exact numbers of avoiding words at lengths \(0,1,\ldots,15\) are
\[
1,3,9,18,30,42,54,54,54,48,42,36,24,12,6,0.
\]
Hence exactly six words survive at length \(14\), and none survives at length \(15\). Since avoidance is factorial, no longer avoider exists.

The six length-\(14\) survivors are the words listed above. Applying all six permutations of the alphabet to \(\mathtt{01200112200120}\) yields exactly this set, proving that the equality layer is one alphabet-permutation orbit. Direct reversal of the six words permutes the same set.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier reconstructs the complete prefix tree through length \(15\) twice, using the two independent direct occurrence tests described above. It checks equality of every level, the complete count vector, the six exact extremizers, and emptiness at length \(15\).

It then reconstructs the six alphabet relabelings of the representative and independently checks reversal closure.

## Relationship to prior work
Currie, Mol, and Rampersad determine an avoidance basis for formulas with reversal on two variables. Their Table 1 records \(\mathtt{xyx}\cdot y^R\) as the unique basis formula there having avoidability index \(4\), and states that a longest ternary avoiding word has length \(14\).

The source gives the scalar maximum but does not enumerate all length-\(14\) avoiders or identify their symmetry class. It also notes the equivalent formulation \(yx^Ry\cdot x\), which was included in the literature comparison.

Later work on doubled patterns with reversal cites this formula family but does not supply the six-word equality classification. Targeted searches under the formula, its equivalent form, the notation \(\psi_1\), the exact maximum length, and the representative strings did not locate a published complete equality list.

## Limitations
The result classifies only the length-\(14\) equality layer for this ternary formula. It does not strengthen the published avoidability-index theorem or classify shorter avoiding words up to symmetry.

The original maximum was established with a finite computation, so unpublished search output or an unindexed auxiliary file could contain the same equality list. No such published or indexed classification was located.

## References
1. J. D. Currie, L. Mol, and N. Rampersad, “Avoidance bases for formulas with reversal,” arXiv:1711.08025v1, first public version 2017-11-21; Theoretical Computer Science 736 (2018), 26–37, DOI 10.1016/j.tcs.2018.04.039.
2. P. Ochem, “Doubled patterns with reversal are 3-avoidable,” arXiv:2105.04673, 2021.
