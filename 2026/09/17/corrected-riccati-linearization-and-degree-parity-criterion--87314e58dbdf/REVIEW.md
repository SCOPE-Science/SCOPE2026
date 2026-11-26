# Independent mathematical audit

## correctness

PASS

Theorem 4.20 of Wu–Hong concerns a nonzero Virasoro parameter, polynomial C and both off-diagonal entries nonzero; it gives the displayed rational Riccati condition. Differentiating gamma=-z'/(pz) produces +p'z'/(p^2 z); the squared logarithmic derivative cancels the -p gamma^2 term. Multiplication by -pz gives z''+(d-p'/p)z'-pq z=0. On domains where the substitution is defined the converse follows by solving z'=-p gamma z. Setting z=rho w removes the first derivative precisely when 2rho'+P rho=0, P=d-p'/p; it gives w''=(pq+P'/2+P^2/4)w. Both printed omissions in Remark 4.21 were checked. For p=q=x, d=0, gamma=1 solves the Riccati equation; the corresponding z=exp(-x^2/2) satisfies the corrected equation but has residual -z in the printed equation. Example 4.22 has p=1, q=x, d=0 and is unaffected. For the parity test, u=w'/w=-p gamma+P/2 would be rational and satisfy u'+u^2=pq+P'/2+P^2/4. At infinity p'/p=O(1/x); d=0 or 2 deg d<deg p+deg q ensures the right-hand side has leading degree M=deg p+deg q, positive and odd, from pq alone. A rational u of nonpositive degree makes the left side bounded at infinity; a rational u of positive degree has even leading degree 2 deg u. Both are impossible. This independently proves the polynomial sufficient test, including d=0, and does not assert absence of general Liouvillian solutions.

## originality

PASS

The distinct contribution is the explicit diagnosis and correction of the two errors in Wu–Hong v1 Remark 4.21, with a variable-coefficient counterexample and the exact scope of the repair. The transformations and the degree obstruction are classical, and the module criterion is directly implied by combining Kovacic's case-1 necessary condition with Wu–Hong Theorem 4.20 and the corrected normalization. Credit the criterion as a useful worked application, not as a new Riccati obstruction or independently novel general theorem. No separate source-specific correction was found in the checked statements; no first-discovery claim is made.

## value

PASS

The error changes the actual computational test for nonconstant c21, not only notation. In the record's concrete p=q=x example, the incorrect equation z''=x²z does not even admit a rational logarithmic derivative: such a derivative u would solve u'+u²=x², its finite poles would be simple with residue 1, and its polynomial part would be ±x with zero constant term by the x coefficient. With N finite poles, the constant coefficient of u'+u² would then be ±(1+2N), impossible. Thus the uncorrected equation can wrongly suggest absence of the rational solution relevant to reducibility. Correcting the recipe and explaining the unaffected theorem is worthwhile; the covered parity application illustrates use rather than adding the novelty on its own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
