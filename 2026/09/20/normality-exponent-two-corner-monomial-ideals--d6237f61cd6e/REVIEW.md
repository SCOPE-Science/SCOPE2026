# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof reduces normality to integral closedness of the square using the Reid--Roberts--Vitulli three-variable criterion. The Newton-polyhedron inequality is then analyzed by the possible \(x\)-exponents. Cases \(i\ge2\) and \(i=0\) reduce immediately, and any obstruction with \(i=1\) can be reduced to \(0\le j<b\), \(0\le k<c\). Writing \(u=b-j\), \(v=c-k\) gives the exact criterion that \(\langle b,c\rangle\) meet
\[
[bc/2,\,bc-cu-bv]
\]
for every positive \(u,v\) with \(cu+bv\le bc/2\).

The arithmetic case split was checked separately. If \(bc\) is even, \(bc/2\) itself is in the semigroup. If \(b,c\) are odd with \(d=(b,c)>1\), the element \((bc+d)/2\) lies in \(\langle b,c\rangle\) by the two-generator Frobenius bound and lies in every required interval. If \(b,c\) are odd and coprime, exactly one of \((bc-1)/2\) and \((bc+1)/2\) belongs to \(\langle b,c\rangle\), as follows from the unique residue solving \(2cq\equiv1\pmod b\). This gives both sufficiency and the explicit non-normality witness.

The finite verification artifact compares the exact interval criterion with the closed classification throughout \(2\le b\le100\), \(2\le c\le150\) and reports zero mismatches. The computation is supportive only; the proof is symbolic and uniform.

## Originality

**PASS, to the best of our knowledge.** Cahen--Fontana--Frisch--Glaz Problem 41 asks for the full classification of triples \((a,b,c)\). Reid--Roberts--Vitulli establish the three-variable reduction to the square, derive a necessary numerical-semigroup condition in the pairwise-coprime case, and exhibit \((2,3,7)\) as non-normal. In the slice \((2,b,c)\), their necessary \(L+1\) condition becomes exactly \((bc+1)/2\in\langle b,c\rangle\) when \(b,c\) are odd and coprime; the present theorem proves that this condition is sufficient and also settles all even and non-coprime pairs.

Accessible descriptions of Coughlin's 2004 thesis identify a principal three-variable theorem for consecutive triples \((j,j+1,j+2)\), normal exactly for even \(j\). Al-Ayyoub's 2019 work gives general Newton-polyhedron criteria and transfer results, and Ataka--Matsuoka's 2026 theorem gives a sharp bound in terms of the number of minimal generators. Targeted searches for the exact exponent-two family, the midpoint condition \((bc+1)/2\in\langle b,c\rangle\), and equivalent modular-inverse formulations found no prior classification. No overlapping SCOPE record was found under the relevant objects or claim family.

Residual risk remains because the full text of Coughlin's dissertation was not inspected, and a closed specialization of an existing general criterion might be present under different terminology. This risk is material enough to record but did not produce concrete evidence of coverage.

## Value

**PASS.** The result classifies an infinite two-parameter slice of a published three-variable normality problem by an explicit arithmetic criterion. It explains the classical \((2,3,7)\) obstruction, supplies an explicit witness for every non-normal pair, and identifies a setting in which the Reid--Roberts--Vitulli necessary semigroup condition is also sufficient. The criterion is effective using only gcd, a two-generator numerical-semigroup membership test, or one modular inverse.

## Limitations

The theorem applies only when one corner exponent equals \(2\). It does not classify general triples \((a,b,c)\), and it does not imply that the Reid--Roberts--Vitulli necessary condition is sufficient outside this slice.
