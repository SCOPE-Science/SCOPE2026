# Independent mathematical audit

## correctness

PASS

Here ρ is the ratio of Gram eigenvalues, i.e. the square of the synthesis matrix's 2-norm condition number. For any nonsingular order-five sign matrix, a sign normalization followed by four row subtractions gives 16|det, and Hadamard's bound leaves 16,32,48 as the possible absolute nonzero determinants. At ρ≤9/4, the five positive Gram eigenvalues have mean 5. The curvature lower bound −1/m² for log on their range (m the smallest eigenvalue) and the range-squared/4 variance bound give log(det Gram)≥5 log 5−(5/8)(ρ−1)^2≥5 log 5−125/128. Thus det Gram>3125/3>32², forcing absolute determinant 48. A dependent five-point row set has affine dimension exactly three. Restricted characters are columns of an order-eight Walsh matrix up to signs, with identical columns modulo signs giving zero determinant; the other cases are five-minors. The inverse Walsh normalization and Jacobi identity give 8 times a complementary three-minor, whose magnitude is at most 4, excluding absolute determinant 48. For independent rows the difference-character map is surjective; sign-normalize using one column, and subtract the top row to obtain 16 times a rooted binary four-column determinant. Repeated projections imply singularity. An independent rational-elimination replay enumerated all 1820 distinct rooted four-column candidates with magnitude counts 0:880, 1:835, 2:100, 3:5. The maximizers (3,5,9,14), (3,6,10,13), (5,6,11,12), (7,9,10,12), (7,11,13,14) are the five rooted translates of S. The sixteen unrooted translates are distinct by parity, and normalization removes the dependence of singular values on the lifts. For the canonical pair the column Gram is 4I+ssᵀ with s=(1,1,1,1,−1), giving 9,4,4,4,4, so all absolute-determinant-48 Walsh minors give equality and no others do. There are 2^(d−4) choices for each quotient lift independently. Choosing an origin and four ordered independent differences gives n(n−1)(n−2)(n−4)(n−8) lists; dividing by 5! and multiplying by the partner count gives the claimed pair count, including 43,008 at d=4.

## originality

PASS

Credit the sharp minimum Riesz ratio and the equivalence of minimizing that ratio to maximizing the Walsh determinant. The underlying determinant classification, translated dual-simplex geometry and partner/pair counts have directly overlapping coverage in the inspected determinant catalogue record; they are not credited as separate new determinant results. The older finite pair count, the universal order-five maximal sign determinant and the Riesz-ratio framework are likewise known. The compared statements do not establish that matrices outside the determinant-maximizing class cannot match or improve its condition ratio.

## value

PASS

For five points the exact Gram condition ratio controls the best Riesz bounds achievable by selecting Walsh frequencies, and its value rules out an orthogonal five-character basis. The rigidity criterion decides which fixed supports admit optimal conditioning and gives all numerical bounds via a concrete Gram spectrum. The spectral necessity is useful independently of reproducing already known determinant counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
