# Exact projective symmetry of the XR conic-line arrangement
## Finding
Let \(\mathcal{XR}\subset\mathbb P^2_{\mathbb C}\) be the arrangement in Măcinic–Pokora, Example 2.8. Write its six conic components as \(C_1,\ldots,C_6\) in the order printed in the source, and write its six line components as
\[
L_1:y=0,\quad L_2:x+z=0,\quad L_3:x+y-z=0,
\]
\[
L_4:x+y+z=0,\quad L_5:x-z=0,\quad L_6:2x+y=0.
\]
Then
\[
\operatorname{Aut}_{\mathbb P^2}(\mathcal{XR})\cong S_3.
\]
One choice of generators is
\[
s[x:y:z]=[x+y:-y:-z],\qquad
t[x:y:z]=[x+y:-x-y+z:-x].
\]
They satisfy \(s^2=t^3=(st)^2=1\) in \(\operatorname{PGL}_3\), and they generate all projective symmetries of the arrangement.

The six-line skeleton has a larger projective stabilizer of order \(24\), isomorphic to \(S_4\). Its four triple-concurrency classes are
\[
\{L_1,L_2,L_4\},\quad
\{L_1,L_3,L_5\},\quad
\{L_2,L_3,L_6\},\quad
\{L_4,L_5,L_6\}.
\]
The conics break this \(S_4\)-symmetry exactly to the subgroup fixing the last class. Hence the line components have the two \(S_3\)-orbits
\[
\{L_1,L_2,L_3\},\qquad \{L_4,L_5,L_6\},
\]
and the conics have the two orbits
\[
\{C_1,C_3,C_4\},\qquad \{C_2,C_5,C_6\}.
\]

There is a direct consequence for the two addition examples singled out in the source. The free added line \(z=0\) has orbit
\[
z=0,\qquad x=0,\qquad x+y=0,
\]
so each of these three lines gives a projectively equivalent free enlargement of \(\mathcal{XR}\). The plus-one generated added line \(x+2y+4z=0\) has orbit represented by
\[
\begin{aligned}
&x-y-4z=0, &&6x+2y-z=0, &&5x+y-2z=0,\\
&x+2y+4z=0, &&6x+4y+z=0, &&5x+4y+2z=0.
\end{aligned}
\]
Thus all six corresponding enlargements are projectively equivalent plus-one generated arrangements with exponents \((5,14,17)\).

## Assumptions and scope
The ground field is \(\mathbb C\), as in the source. The statement concerns projective automorphisms of the reduced plane arrangement itself. Since projective maps preserve component degree, every automorphism must permute the six line components among themselves and the six conic components among themselves. Each displayed conic is smooth because its symmetric quadratic matrix has nonzero determinant.

The result does not assert that these are all abstract automorphisms of the complement or all automorphisms of any logarithmic bundle. It is specifically the stabilizer inside \(\operatorname{PGL}_3(\mathbb C)\).

## Proof
Represent a line by its dual point. After harmless rescaling, the six dual points are
\[
[0:1:0],\ [1:0:1],\ [1:1:-1],\ [1:1:1],\ [1:0:-1],\ [2:1:0].
\]
Exactly four triples among them are collinear, namely the duals of the four triple-concurrency classes listed above. Their incidence structure is the six-edge, four-vertex incidence structure of \(K_4\). Therefore every projective stabilizer of the six-line skeleton acts faithfully on these four classes, giving an injection into \(S_4\).

For completeness, the exact finite calculation in `verify.py` reconstructs every projectivity from the image of a projective frame of four dual points. There are \(72\) ordered four-point frames in this six-point set. Exhaustive exact rational reconstruction yields exactly \(24\) projectivities preserving all six dual points, and their induced permutations on the four collinear triples are all \(24\) elements of \(S_4\). Hence the line-skeleton stabilizer is exactly \(S_4\).

Now encode each conic \(C_i\) by its symmetric matrix \(Q_i\), so that its equation is \(X^TQ_iX=0\). If a point transformation is represented by \(A\) and its dual action on line covectors is \(B=A^{-T}\), then the image of \(Q_i\) is represented by
\[
B Q_i B^T.
\]
Testing the \(24\) exact line-skeleton symmetries against the unordered set \(\{Q_1,\ldots,Q_6\}\) leaves exactly six transformations. Their permutations of the four triple-concurrency classes fix \(\{L_4,L_5,L_6\}\) and realize all permutations of the other three classes. Thus they form the point stabilizer \(S_3<S_4\).

The two displayed matrices \(s\) and \(t\) are among these six transformations. Exact multiplication gives \(s^2=I\), \(t^3=-I\), and \((st)^2=I\), so their projective classes satisfy the standard \(S_3\) presentation and generate the six surviving transformations. Their induced component permutations give the orbit decompositions stated above.

Finally, projective equivalence preserves freeness, plus-one generatedness, and the exponents of the associated derivation module. Acting with the six stabilizer elements on the two source lines \(z=0\) and \(x+2y+4z=0\) gives exactly the three- and six-element line orbits displayed in the finding, proving the addition corollary.

## Verification
The standalone verifier uses only exact rational arithmetic from the Python standard library. It checks: the six conics are nondegenerate; the six-line skeleton has exactly the four stated triple-concurrency classes; the projective-frame enumeration has exactly \(24\) line-set stabilizers; conic preservation cuts these to exactly \(6\); the surviving transformations fix exactly one concurrency class and induce all of \(S_3\) on the other three; the displayed generators satisfy the required relations; the line and conic orbit decompositions are exact; and the two added-line orbits have sizes \(3\) and \(6\) with the stated representatives.

Reproduce with `python3 verify.py`. A clean replay from the packaged artifact path returns `VERIFY_OK`.

## Relationship to prior work
Măcinic–Pokora introduce the explicit arrangement \(\mathcal{XR}\), state that it has nine ordinary sixfold points and twelve double points, and compute that it is free with exponents \((4,13)\). They further state that adjoining \(x+2y+4z=0\) produces a plus-one generated arrangement with exponents \((5,14,17)\), while adjoining \(z=0\) produces a free arrangement. The inspected source does not state a projective stabilizer, a symmetry group, or symmetry orbits of these added lines.

The closest semantic published-finding corpus hit concerns a different, much smaller arrangement of two conics and three lines whose stabilizer is also \(S_3\). That statement neither contains nor implies the present \(12\)-component calculation. Targeted searches using the exact source equation, the name \(\mathcal{XR}\), stabilizer/automorphism terminology, the \(S_4\)-to-\(S_3\) symmetry breaking, and the added-line orbit representatives returned no covering record.

## Limitations
The originality check cannot exclude an unindexed computation of the same stabilizer in private notes, software output, or literature using different notation. The proof establishes only the projective stabilizer of this explicit embedded arrangement and the symmetry consequences for the two source addition examples; it does not classify all possible added lines by freeness or plus-one generatedness.

## References
1. A. Măcinic and P. Pokora, *On plus-one generated conic-line arrangements with simple singularities*, arXiv:2309.15228v1, first public 2023-09-26; later DOI:10.4171/RLM/1044. Example 2.8 contains the defining equation and the two addition examples.
2. EMS Press metadata for DOI:10.4171/RLM/1044, listing primary MSC 14H50 and secondary MSC 32S25.
