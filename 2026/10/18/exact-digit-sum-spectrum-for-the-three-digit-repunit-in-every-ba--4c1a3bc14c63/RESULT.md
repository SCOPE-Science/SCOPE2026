# Exact digit-sum spectrum for the three-digit repunit in every base

## Finding

Let \(b\ge 2\) be any integer base, let \(m=b^2+b+1\), and let \(s_b(N)\) be the usual base-\(b\) digit sum. The complete set of positive digit sums of positive multiples of \(m\) is
\[
\mathcal S_b(m):=\{s_b(km):k\in\mathbb Z_{>0}\}
=\big\langle 3,\ b+2,\ 2b+1\big\rangle\setminus\{0\},
\]
where brackets mean the additive monoid of nonnegative integer combinations of the listed generators.

If \(b\equiv 1\pmod 3\), this spectrum is exactly \(3\mathbb Z_{>0}\). If \(b\not\equiv 1\pmod 3\), the Apéry set of the monoid with respect to \(3\) is \(\{0,b+2,2b+1\}\); its Frobenius number is \(2b-2\), conductor \(2b-1\), and genus (number of missing positive digit sums) is \(b\). Thus, in the latter case, **every positive integer at least \(2b-1\) occurs**, and the bound is sharp.

For example, for base \(5\) and modulus \(31\), the missing positive digit sums are exactly \(\{1,2,4,5,8\}\). For base \(10\) and modulus \(111\), the possible positive digit sums are exactly the multiples of \(3\).

## Assumptions and scope

The base \(b\) ranges over *all* integers at least \(2\); there are no parity or primality assumptions. Multipliers \(k\) range over all positive integers, with no upper bound on their size or their number of digits. The theorem concerns digit sums, not the set of multipliers and not the minimal multiplier realizing each sum. The Frobenius number, conductor, and finite genus are asserted only in the branch \(b\not\equiv1\pmod3\). In the other branch infinitely many positive digit sums are excluded.

## Proof

**Lemma 1 (three-class digit reduction, in both directions).** Since \(b^3-1=(b-1)m\), we have \(b^3\equiv1\pmod m\). For a positive integer \(N\) with base-\(b\) digits \(d_j\), set
\[
A=\sum_{j\equiv0\ (3)}d_j,\quad
B=\sum_{j\equiv1\ (3)}d_j,\quad
C=\sum_{j\equiv2\ (3)}d_j.
\]
Then \(A,B,C\ge0\), \(s_b(N)=A+B+C\), and
\[
N\equiv A+bB+b^2C\pmod m.
\]
Conversely, any triple of nonnegative integers \((A,B,C)\) with positive sum yields a positive integer \(N\) having precisely this digit sum and residue: place \(A\) digits equal to \(1\) at exponents \(0,3,6,\ldots,3(A-1)\), place \(B\) ones at exponents \(1,4,7,\ldots,3(B-1)+1\), and place \(C\) ones at exponents \(2,5,8,\ldots,3(C-1)+2\), omitting a class when its count is zero. All positions are distinct; the construction is carry-free even for \(b=2\). Therefore \(s\ge1\) belongs to \(\mathcal S_b(m)\) if and only if there exist \(A,B,C\in\mathbb Z_{\ge0}\) satisfying
\[
A+B+C=s,\qquad A+bB+b^2C\equiv0\pmod m.
\]

**Lemma 2 (attainability).** The triples \((1,1,1)\), \((1,b+1,0)\), and \((b+1,b,0)\) have coordinate sums \(3\), \(b+2\), and \(2b+1\), respectively. Their weighted sums are all exactly \(m\). Their nonnegative componentwise sums still satisfy the divisibility congruence. Lemma 1 shows that every positive element of \(\langle3,b+2,2b+1\rangle\) belongs to \(\mathcal S_b(m)\).

**Lemma 3 (sharp small-sum exclusion).** Suppose \(s\in\mathcal S_b(m)\) and \(1\le s\le2b+1\). Choose \((A,B,C)\) from Lemma 1. Subtract \(t=\min(A,B,C)\) from all three coordinates. Since \(1+b+b^2=m\), this preserves the congruence and reduces their sum by \(3t\). If the resulting triple is zero, \(s=3t\). Otherwise it has at least one zero coordinate. Multiplication of the weighted sum by \(b\) modulo \(m\) cyclically permutes \((A,B,C)\), because \(b^3\equiv1\pmod m\); hence we may arrange that the zero coordinate is \(C=0\). The reduced positive sum \(S=A+B\) satisfies \(S\le s\le2b+1\). As
\[
0<A+bB\le b(A+B)\le b(2b+1)<2(b^2+b+1)=2m,
\]
and \(m\mid A+bB\), necessarily \(A+bB=m\). Thus
\[
A=m-bB\ge0\quad\Longrightarrow\quad B\le b+1,
\]
while
\[
A+B=m-(b-1)B\le2b+1\quad\Longrightarrow\quad B\ge b.
\]
Therefore \(B=b\) or \(b+1\), yielding \(S=2b+1\) or \(b+2\), respectively. Before the subtraction, \(s\) was thus of one of the three forms \(3t\), \(3t+b+2\), \(3t+2b+1\). In every case it lies in the stated monoid.

**Theorem (completion for all sums).** If \(b\equiv1\pmod3\), then \(\gcd(b-1,m)=3\) and the standard digit-sum congruence \(s_b(N)\equiv N\pmod{b-1}\) forces \(3\mid s_b(N)\) for every multiple of \(m\). Conversely all positive multiples of \(3\) occur by Lemma 2. This gives the first branch.

If \(b\not\equiv1\pmod3\), the three numbers \(0\), \(b+2\), and \(2b+1\) lie in distinct residue classes modulo \(3\): the latter two are the two nonzero classes, in some order. Consequently every integer \(s>2b+1\) belongs to the monoid by subtracting whichever of those three representatives has the same residue and then using nonnegative multiples of \(3\). Lemma 3 excludes all sums not in the monoid up to \(2b+1\), while Lemma 2 provides all monoid elements. This proves the spectrum identity in all cases.

To compute the finite invariants, in this second branch the distinct residue representatives \(\{0,b+2,2b+1\}\) are indeed *minimal* in their respective residue classes: below each representative there is no smaller positive attainable value in that class by Lemma 3. This is the Apéry set of the monoid with respect to its multiplicity \(3\). The largest missing integer in a residue class is its Apéry representative minus \(3\); hence the Frobenius number is \((2b+1)-3=2b-2\), the conductor is \(2b-1\), and the genus is
\[
\frac{0+(b+2)+(2b+1)}3-\frac{3-1}2=b.
\]
All assertions follow.

## Verification

The included standalone `verify.py` constructs, independently of the three-class proof, a finite-state automaton over all possible base-\(b\) digits, with state consisting of partial digit sum, residue modulo \(m\), and next exponent modulo \(3\). Zero digits and arbitrary word lengths are allowed. It compares the complete reachable digit-sum sets against additive-semigroup dynamic programming for \(18\) bases and \(1,162\) base/sum pairs, traversing \(551,625\) finite states; all comparisons passed. The script also checks the exact genus, Frobenius number, and modular case distinctions for these bases. The infinite theorem is established in the preceding proof, not by these finite tests. Reproduce using `python3 verify.py` from the extracted package directory.

## Relationship to prior work

Phunphayap, Noppakaew, and Pongsriiam (2023), Theorems 1–3 and Questions 2 and 4, study \(\mathrm{Out}(s_b,n)=\{s_b(kn):k\ge1\}\), its congruence obstruction, cofiniteness, and general full-spectrum questions. Their Theorem 2 already implies that all positive multiples of \(3=s_b(m)\) occur. For \(b\equiv1\pmod3\), their Theorems 1–2 together already imply the branch \(\mathcal S_b(m)=3\mathbb Z_{>0}\); **this branch is background, not separately novel**. Their Theorem 1 also implies existence of a finite complement when \(b\not\equiv1\pmod3\), but does not give the exact exceptional set, first omitted tail, Frobenius number, or genus for \(m=b^2+b+1\). The new substantive statement is the full uniform monoid description and sharp finite invariants in that coprime branch.

Clokie, Lidbetter, Molina Lovett, Shallit, and Witzman (2020), Theorems 3–4, give the distinct-powers criterion and a general method that raises a realized digit sum by \(b-1\); Corollary 8 recognizes repunits as sturdy. Thus the minimal digit sum \(3\), elementary constructions of larger digit sums, and the existence of certain arithmetic progressions are **not** claimed as new. Their results do not determine the excluded sums for the cyclotomic three-digit repunit. The current proof separates the easy inclusion from the sharp exclusion by an exact three-class congruence reduction.

## Limitations

The result does not determine minimum multipliers, the distribution of multiplier sizes, or output multiplicities; it concerns existence of digit sums only. No assertion is made about repunits of length other than three. The finite-genus formula does not apply to bases congruent to \(1\) modulo \(3\). A systematic literature and mathematical-record comparison did not identify an equivalent theorem, but unindexed literature and independent duplication remain possible. Independent mathematical validation has not been performed.

## References

1. Phakhinkon Napp Phunphayap, Passawan Noppakaew, and Prapanpong Pongsriiam, *Directed graphs of integers with arcs determined by an arithmetic function*, arXiv:2303.13017, first public version March 23, 2023. https://arxiv.org/abs/2303.13017 . Relevant material: Theorems 1–3, Examples 4–5, Questions 1–4.
2. Trevor Clokie, Thomas F. Lidbetter, Antonio Molina Lovett, Jeffrey Shallit, and Leon Witzman, *Computational Aspects of Sturdy and Flimsy Numbers*, arXiv:2002.02731, first public version February 7, 2020. https://arxiv.org/abs/2002.02731 . Relevant material: Theorems 3–4 and Corollary 8.
