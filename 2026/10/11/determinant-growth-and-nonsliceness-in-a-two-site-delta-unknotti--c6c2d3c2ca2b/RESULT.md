# Determinant growth and nonsliceness in a two-site delta-unknotting family
## Finding
For every integer \(b\ge -1\), define
\[
K_b=M(0;(3b+5,-3),(8b+13,8),(8b+13,8)).
\]
Nakamura's construction gives \(u(K_b)=u^{{\Delta}}(K_b)=1\) and two distinct Type-I tangle regions on which a delta-move produces the unknot. In addition,
\[
\det(K_b)=(8b+13)(24b+41).
\]
The determinant is strictly increasing with \(b\) and is never a square. Hence the \(K_b\) are pairwise nonisotopic and none is algebraically slice; therefore none is topologically slice.

## Assumptions and scope
The parameter range is exactly the integer half-line \(b\ge -1\). In this range \(3b+5\ge2\) and \(8b+13\ge5\), so the displayed Montesinos presentation uses positive denominator parameters in the convention of the source. The coprimality conditions hold because \(\gcd(3b+5,3)=1\) and \(\gcd(8b+13,8)=1\). The delta-unknotting and ordinary unknotting statements are inherited from Nakamura's Example 3.1 and the theorem immediately preceding it; the determinant, distinctness, and nonsliceness conclusions are the new part established here.

## Proof
Write \(p=3b+5\) and \(q=8b+13\). For a three-branch Montesinos knot with integer parameter zero, the standard determinant formula is
\[
\det M(0;(lpha_1,eta_1),(lpha_2,eta_2),(lpha_3,eta_3))
=
\left|lpha_1lpha_2lpha_3\left(rac{eta_1}{lpha_1}+rac{eta_2}{lpha_2}+rac{eta_3}{lpha_3}ight)ight|.
\]
Baker--Moore record this formula as Lemma 5, obtained from the first homology of the double branched cover. Substitution gives
\[
\det(K_b)=\left|pq^2\left(-rac3p+rac8q+rac8qight)ight|
=\left|-3q^2+16pqight|
=q(24b+41),
\]
because both factors are positive for \(b\ge-1\). Thus
\[
\det(K_b)=(8b+13)(24b+41).
\]
Moreover,
\[
\det(K_{{b+1}})-\det(K_b)=384b+832>0
\]
for every \(b\ge-1\), so the determinant strictly distinguishes the family.

To rule out squares, set \(r=24b+41\). Then \(q\) and \(r\) are odd and
\[
\gcd(q,r)=\gcd(q,r-3q)=\gcd(q,2)=1.
\]
If \(qr\) were a square, coprimality would force both \(q\) and \(r\) to be squares. But
\[
r\equiv2\pmod3,
\]
which is impossible for an integer square. Therefore \(\det(K_b)\) is never a square.

An algebraically slice knot satisfies the Fox--Milnor factorization \(\Delta_K(t)\doteq f(t)f(t^{{-1}})\). Evaluating at \(t=-1\) shows that its determinant is a square. Since \(\det(K_b)\) is nonsquare, each \(K_b\) is not algebraically slice. Every topologically slice knot is algebraically slice, so topological sliceness is excluded as well.

## Verification
The arithmetic was replayed directly for a finite sanity range \(-1\le b\le19\), checking the closed determinant formula, positivity, coprimality, residue class modulo three, nonsquareness, and strict growth. The finite replay is not the proof of the infinite statement; the proof is the symbolic argument above. The included verifier reproduces the sanity check without external packages.

## Relationship to prior work
Nakamura proves the delta-unknotting statement for the displayed family and notes that it gives infinitely many further examples with distinct unknotting delta-moves, but the inspected text does not compute this determinant formula or derive pairwise distinction and algebraic/topological nonsliceness from it. Baker--Moore provide the general determinant formula for Montesinos knots, not this specialization. Saurabh recalls the Fox--Milnor implication from algebraic sliceness and uses it for a different pretzel family. Targeted semantic literature searches for the exact parameter family, determinant factorization, and Fox--Milnor consequence found no statement equivalent to the theorem above.

## Limitations
The theorem concerns the subfamily \(b\ge-1\) in the displayed sign convention. It does not classify all of Nakamura's signed parameter variants, does not determine concordance order, and does not claim that determinant alone detects the inequivalence of the two delta-moves. The source paper's delta-move analysis supplies that local-move statement; the new argument concerns determinant growth and sliceness obstruction.

## References
1. K. Nakamura, *Montesinos Knots with Delta-Unknotting Number One*, arXiv:2609.39565v1 (2026), especially Theorem 1.3 and Example 3.1.
2. K. L. Baker and A. H. Moore, *Montesinos knots, Hopf plumbings, and L-space surgeries*, arXiv:1404.7585v1; Journal of the Mathematical Society of Japan 70 (2018), Lemma 5.
3. S. Saurabh, *Exceptional pretzel knots are not algebraically slice*, arXiv:2609.34522v1 (2026), introduction for the Fox--Milnor condition and the implication from topological to algebraic sliceness.
