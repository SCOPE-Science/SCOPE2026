# Parity-sharp bounded congruence avoidance under zero-sum shifts
## Finding
For every integer \(m\ge 2\), define
\[
B_m=\begin{cases}1,&m\text{ even},\\2,&m\text{ odd}.
\end{cases}
\]
Let \(Q\ge 1\), let \(\ell\) be an odd prime with \(\gcd(Q,\ell)=1\), and let \(x_1,\ldots,x_m,b\in\mathbb Z\). Then there exist integers \(t_1,\ldots,t_m\) such that
\[
\sum_{i=1}^m t_i=0,\qquad |t_i|\le B_m,\qquad x_i+t_iQ\not\equiv b\pmod\ell\quad(1\le i\le m).
\]
The radius \(B_m\) is best possible uniformly over all permitted data.

For finite sets \(F_1,\ldots,F_m\subseteq\mathbb Z\), put
\[
F_i^{\sharp}=\{x+tQ:x\in F_i,\ t\in\mathbb Z,\ |t|\le B_m,\ x+tQ\not\equiv b\pmod\ell\}.
\]
Then
\[
F_1+\cdots+F_m\subseteq F_1^{\sharp}+\cdots+F_m^{\sharp},\qquad
|F_i^{\sharp}|\le (2B_m+1)|F_i|,
\]
and every \(y\in F_1^{\sharp}+\cdots+F_m^{\sharp}\) has some \(y_0\in F_1+\cdots+F_m\) with
\[
|y-y_0|\le mB_mQ.
\]
Thus the universal shift radius in Chen's congruence-avoidance lemma drops from \(m+1\) to the exact parity-dependent value \(1\) or \(2\); the corresponding direct cardinality factor drops from \(2m+3\) to \(3\) or \(5\), and the displacement bound drops from \(m(m+1)Q\) to \(mQ\) or \(2mQ\).

## Assumptions and scope
The modulus \(\ell\) is an odd prime and \(Q\) is invertible modulo \(\ell\). No distributional assumption is made on the integers \(x_i\) or on the forbidden residue \(b\). The sharpness assertion is uniform: it asks for one radius that works for every admissible choice of \(\ell,Q,x_1,\ldots,x_m,b\).

The finite-set consequence uses the full family of admissible shifts with \(|t|\le B_m\). It is an immediate quantitative replacement for the corresponding finite-set construction in Lemma 2.2 of Chen's paper; it does not assert that every later constant in that paper is globally optimal.

## Proof
Since \(Q\) is invertible modulo \(\ell\), define the unique forbidden residue \(c_i\in\mathbb Z/\ell\mathbb Z\) by
\[
c_i\equiv (b-x_i)Q^{-1}\pmod\ell.
\]
It is enough to choose \(t_i\not\equiv c_i\pmod\ell\) with zero integer sum and the asserted radius.

First consider a pair of coordinates with forbidden residues \(c\) and \(d\). Among the three integers \(-1,0,1\), the condition \(s\equiv c\pmod\ell\) excludes at most one choice and the condition \(-s\equiv d\pmod\ell\) excludes at most one choice. Because \(\ell\) is odd, the three candidates are distinct modulo \(\ell\). Hence some \(s\in\{-1,0,1\}\) survives, and the pair \((s,-s)\) has sum zero, radius at most \(1\), and avoids both forbidden residues. Pairing all coordinates proves the theorem when \(m\) is even.

For odd \(m\), it remains to treat three coordinates with radius \(2\); the other \(m-3\) coordinates can be paired as above. Let
\[
Z=\{(u,v,w)\in\{-2,-1,0,1,2\}^3:u+v+w=0\}.
\]
There are
\[
|Z|=3+4+5+4+3=19
\]
such triples. If \(\ell\ge5\), a fixed forbidden residue occupies at most one integer of \([-2,2]\). In one coordinate, fixing that integer removes at most five triples from \(Z\). The three forbidden coordinate slices therefore remove at most \(15<19\) triples, leaving an admissible zero-sum triple.

It remains to handle \(\ell=3\). For coordinate \(i\), let \(A_i=(\mathbb Z/3\mathbb Z)\setminus\{c_i\}\). Each \(A_i\) has two elements, and the sum of any two two-element subsets of \(\mathbb Z/3\mathbb Z\) is all of \(\mathbb Z/3\mathbb Z\). Choose \(r_3\in A_3\), then choose \(r_1\in A_1\) and \(r_2\in A_2\) with \(r_1+r_2+r_3=0\) modulo \(3\). Represent these residues by \(u_i\in\{-1,0,1\}\). Their integer sum is a multiple of \(3\) lying between \(-3\) and \(3\), so it is \(-3\), \(0\), or \(3\). If it is \(0\), the triple is done. If it is \(3\), all three representatives are \(1\); replace one \(1\) by \(-2\), which preserves its residue and makes the integer sum zero. If it is \(-3\), replace one \(-1\) by \(2\). This proves the radius-\(2\) triple lemma and hence the odd-\(m\) upper bound.

The radii are sharp. Radius \(0\) cannot work for any \(m\): choose every \(c_i=0\), so the only allowed integer in radius \(0\) is forbidden. For odd \(m\), radius \(1\) also fails when every \(c_i=0\), because each admissible \(t_i\) must then be \(-1\) or \(1\), and an odd number of odd integers cannot sum to zero. Therefore \(B_m=1\) for even \(m\) and \(B_m=2\) for odd \(m\) are the exact uniform radii.

For the finite-set consequence, apply the just-proved selection to each tuple \((x_1,\ldots,x_m)\in F_1\times\cdots\times F_m\). The selected shifts preserve the total sum, proving the sumset inclusion. Each element of \(F_i\) has at most \(2B_m+1\) candidate shifts, which gives the cardinality bound. Finally, if
\[
y=\sum_{i=1}^m(x_i+t_iQ)\in F_1^{\sharp}+\cdots+F_m^{\sharp},
\]
then with \(y_0=\sum_i x_i\) one has
\[
|y-y_0|=Q\left|\sum_i t_i\right|\le Q\sum_i|t_i|\le mB_mQ.
\]

## Verification
The proof is infinite and does not rely on finite enumeration. The standalone script `artifacts/verify_radius.py` exhaustively checks all forbidden-residue profiles in several nontrivial finite ranges, verifies the pair and triple sublemmas, checks the lower-bound obstructions, and confirms the count \(|Z|=19\). Its recorded replay output is in `artifacts/verification_output.txt`.

The critical proof points independently of computation are: the two-coordinate exclusion count among three candidates; the \(19\)-versus-\(15\) count for \(\ell\ge5\); the explicit residue lifting for \(\ell=3\); and the parity obstruction showing sharpness for odd \(m\).

## Relationship to prior work
Shi-Qiang Chen, in Lemma 2.2 of arXiv:2609.38865v1, proves the same zero-sum congruence-avoidance task with the uniform bound \(|t_i|\le m+1\), and derives the finite-set bounds \((2m+3)|F_i|\) and \(m(m+1)Q\). The proof printed there in fact constructs one shift whose magnitude can reach \(m\); it does not state or imply the parity-sharp uniform radius \(1\) or \(2\). Lemma 2.8(ii) then propagates the \(2m+3\) cardinality factor and \(m(m+1)Q\) displacement into the paper's perturbative construction.

Searches for equivalent bounded zero-sum residue-avoidance statements, stronger uniform-radius results, and the exact parity dichotomy did not locate a covering published statement. Classical sumset facts over \(\mathbb Z/\ell\mathbb Z\) can ensure residue-level zero sums, but they do not by themselves supply the sharp bounded integer lifts used here. The present theorem is therefore a quantitative and sharp refinement of the specific perturbation mechanism used in Chen's construction.

## Limitations
This result does not improve the exponent range in Chen's main existence theorem by itself, and it makes no claim about optimality of all downstream constants after re-optimizing the full construction. The prime and invertibility assumptions are retained. Composite moduli, simultaneous avoidance of more than one residue per coordinate, and sharp radii under additional restrictions are not treated.

The bibliographic comparison is strongest against the motivating paper and targeted searches for equivalent formulations. Because the theorem is elementary, an equivalent lemma may exist under substantially different terminology; no such covering statement was found in the checked sources.

## References
1. Shi-Qiang Chen, “On a problem of Nathanson related to strongly minimal asymptotic bases of order \(h\),” arXiv:2609.38865v1, 30 September 2026. https://arxiv.org/abs/2609.38865
2. Cui-Fang Sun, “On a problem of Nathanson on minimal asymptotic bases,” Journal of Number Theory 218 (2021), 152–160. DOI: 10.1016/j.jnt.2020.07.014.
