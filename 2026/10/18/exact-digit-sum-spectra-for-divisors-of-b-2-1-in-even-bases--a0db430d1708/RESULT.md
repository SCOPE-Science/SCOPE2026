# Exact digit-sum spectra for divisors of \(b^2-1\) in even bases

## Finding

For every **even** integer base \(b\ge2\) and every positive divisor \(d\mid(b-1)\), put \(n=d(b+1)\). Define the set of attainable digit sums
\[
\mathcal S_{b,d}=\{s_b(kn):k\in\mathbb Z_{>0}\},
\]
where \(s_b(N)\) is the sum of the ordinary base-\(b\) digits of \(N\). Then the **entire** set is
\[
\boxed{\mathcal S_{b,d}=d\mathbb Z_{>0}\setminus\{d,3d,5d,\ldots,b-1\}.}
\]
The terminal value \(b-1\) belongs to the displayed excluded progression because \((b-1)/d\) is odd. Hence precisely \(\tfrac12((b-1)/d+1)\) positive multiples of \(d\) are unattainable; the largest is \(b-1\), independent of \(d\). The natural density of \(\mathcal S_{b,d}\) is \(1/d\).

For example, the base-ten sums of digits of positive multiples of \(33\) are exactly
\[
\{3,6,9,12,15,18,\ldots\}\setminus\{3,9\}.
\]
Thus the two exceptional positive multiples of \(3\) are \(3\) and \(9\), while \(15\) is attained by \(10329=33\cdot313\).

## Assumptions and scope

All digit sums are ordinary nonnegative integer digit sums, without repeated digit-sum reduction. The parameters range over every even \(b\ge2\) and each positive divisor \(d\mid b-1\), with positive multiples \(k\ge1\); there is no length restriction on their base-\(b\) expansions. Because \(b\) is even, \(d\) and \(b+1\) are odd and \(\gcd(d,b+1)=1\). The possible moduli are exactly those divisors of \(b^2-1\) that are multiples of \(b+1\).

## Proof

**Necessity.** Write \(N=\sum_{i\ge0}a_i b^i\), with \(0\le a_i\le b-1\), and suppose \(d(b+1)\mid N\). Set \(u=s_b(N)=\sum_i a_i\). Since \(b\equiv1\pmod d\), we have \(d\mid u\). Let \(E=\sum_{i\text{ even}}a_i\) and \(O=\sum_{i\text{ odd}}a_i\). Because \(b\equiv-1\pmod{b+1}\),
\[
E-O\equiv N\equiv0\pmod{b+1},\qquad E+O=u.
\]
If \(u\) is odd and \(1\le u\le b-1\), then \(E-O\) is a nonzero odd integer of absolute value at most \(u<b+1\), contradicting the displayed divisibility. Consequently any attainable \(u\) is a multiple of \(d\), but not an odd multiple of \(d\) at most \(b-1\). These forbidden odd multiples are exactly \(d,3d,\ldots,b-1\), because \((b-1)/d\) is odd.

**Two universal witnesses.** Define
\[
A=\sum_{j=0}^{2d-1}b^j,
\qquad
B=b^4+d b^2+(d-1)b+(b-1).
\]
The base-\(b\) expansion of \(A\) consists of \(2d\) ones, so \(s_b(A)=2d\). Its value is divisible by \(d\), since \(A\equiv2d\pmod d\); it is divisible by \(b+1\), since the alternating sum of an even number of ones is zero.

The five base-\(b\) digits of \(B\), read from the units place, are \(b-1,d-1,d,0,1\), all valid even at \(b=2,d=1\). Their sum is \(s_b(B)=b-1+2d\). Modulo \(d\), \(B\equiv s_b(B)\equiv0\); modulo \(b+1\),
\[
B\equiv (b-1)-(d-1)+d+1=b+1\equiv0.
\]
As \(d\) and \(b+1\) are coprime, both \(A\) and \(B\) are multiples of \(n=d(b+1)\).

**Sufficiency.** Concatenating base-\(b\) representations of multiples of \(n\) gives another multiple of \(n\), because a concatenation is a sum of the original blocks multiplied by powers of \(b\); its digit sum is the sum of the block digit sums. Therefore \(t\ge1\) copies of \(A\) attain every positive even multiple \(2dt\). A copy of \(B\) followed by \(t\ge0\) copies of \(A\) attains every value
\[
b-1+2d+2dt.
\]
Since \(b-1\) is itself an odd multiple of \(d\), the second progression consists of **all** odd multiples of \(d\) strictly greater than \(b-1\). Together the two progressions exhaust precisely the allowed values proved necessary. This proves the theorem. The gap count and density follow immediately.

## Verification

The accompanying standalone program `VERIFY.py` independently constructs exact finite-state digit automata, tracking residues modulo \(d(b+1)\) and digit sums up to a specified bound. It exhausts all possible positive base-\(b\) digit strings of **arbitrary length** whose digit sum is within that bound, by finite-state reachability. It verifies the theorem for every even base \(2\le b\le24\), every positive divisor \(d\mid b-1\), and every target digit sum through \(b+3d+5\). All 28 parameter pairs pass. The general theorem is proved above, not inferred from this finite parameter sweep.

Run `python3 VERIFY.py` with Python 3; no third-party packages or external data are required.

## Relationship to prior work

Phunphayap, Noppakaew and Pongsriiam introduced arithmetic-function-directed edges in 2023. Their Theorem 1 gives necessary congruences and a cofiniteness criterion; their Theorem 2 shows that all multiples of \(s_b(n)\) occur, which for this family supplies the even branch because \(n=(dd)_b\) and \(s_b(n)=2d\). Their Example 4 establishes that \(3\) is missing for base \(10\), modulus \(33\); and their Question 2 asks for exact out-neighborhoods when congruence conditions are insufficient. The theorem here determines their entire base-ten example, including the additional missing value \(9\), and uniformly answers that question for the natural divisor family \(n=d(b+1)\mid b^2-1\), with even \(b\).

Clokie, Lidbetter, Molina Lovett, Shallit and Witzman proved general attainability reductions and the ability to increase a realized digit sum by \(b-1\), but not the stated exact spectrum. Their general results provide context; they do not give the complete uniform missing-set classification without additional arguments. OEIS records examples of multiples of \(11\) with digit sum \(11\), but not this parameter-uniform characterization.

## Limitations

The result does not cover odd bases or arbitrary moduli outside the divisor family. It characterizes attainable **digit sums**, not the count or least size of integers realizing each sum. The literature comparison cannot eliminate overlap in unindexed work. 

## References

1. P. N. Phunphayap, P. Noppakaew, P. Pongsriiam, *Directed graphs of integers with arcs determined by an arithmetic function*, arXiv:2303.13017, first publicly submitted 2023-03-23. https://arxiv.org/abs/2303.13017
2. T. Clokie, T. F. Lidbetter, A. Molina Lovett, J. Shallit, L. Witzman, *Computational Aspects of Sturdy and Flimsy Numbers*, arXiv:2002.02731; published in Theoretical Computer Science 927 (2022), 65–86. https://arxiv.org/abs/2002.02731
3. OEIS A283742, *Numbers with digit sum 11 that are multiples of 11*. https://oeis.org/A283742
