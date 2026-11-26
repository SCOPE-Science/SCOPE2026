# Independent mathematical audit

## correctness

PASS

For the repaired result, all four binary bigrams occur in f(0); their images therefore occur in the fixed point. A length-n factor with n no larger than the shortest level-k block lies in at most two consecutive level-k blocks. Thus all factors for n <= 25 can be extracted exactly from the four f^3(ab) words, giving 37 palindromes and no palindrome of length 24 or 25; these two absences bound every longer palindrome by its center. The same factor identity at level four (minimum block length 500) covers all length-172 windows. The repair's standalone exact verifier tested all 4316 starting windows against all 37 palindromes; every test succeeded. The substring of f^4(00) at zero-based offset 325 of length 171 omits 01100101001110010100110 while belonging to the fixed point, a strict lower-bound witness. Independently checking maximal avoidance factors via consecutive occurrence starts also gave 171. Hence precisely 172 is the least universal saturation length, and the inclusion of the empty palindrome yields D(v)=|v|-37 for all longer factors and at the threshold.

## originality

PASS

Pass applies only to the repaired sharp uniform threshold, not to the reproduced palindrome catalogue or a coarse eventual defect law. The strongest directly comparable indexed catalogue establishes membership and its level-three certificate, not the sharp avoidance lengths. Focused comparison found no matching exact threshold in the sources inspected; this is not a claim of historical priority or exhaustive literature coverage.

## value

PASS

The repair determines a sharp natural recurrence invariant for an established example: the worst length of a factor still missing a palindrome. This is the exact transition to the uniform defect law over all positions. It is not a better but arbitrary sufficient constant; the explicit length-171 obstruction and global length-172 guarantee identify the true boundary. Knowing the palindrome membership list alone does not give that boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
