# Independent mathematical audit

## correctness

PASS

For each B>=18 the prefix sums are 0..S_B and the tail entries are multiples of Q_B=S_B+2, so any representable sum of squares has residue in [0,Q_B-2] and each hQ_B-1 remains bad. Independently regenerated all 2048 reachable totals from squares 1^2..18^2 by explicit set DP: 128 is absent, the entire [129,324] is present. The induction appends unused (m-4)^2: u=t-(m-4)^2 lies in [129,m^2] for m>=18, and a representation of u cannot already contain that square because 2(m-4)^2>(m+1)^2. All four exact Fuller–Nichols Thm 6 inequalities hold at k=2,n=r=1,b=B,Nhat=129,x=4 by monotone quadratic bounds; sample endpoint inequalities checked for 282 values B=18..299. The published proof additionally assumes that m-x is an eligible sequence element; it is not for sparse A_B. Unbounded B and h are handled by quantified inequalities and congruence, not finite tests.

## originality

PASS

Best-of-knowledge primary and published-record comparison distinguishes the final exact claim from the already known framework, special cases and methods; all specific gaps and accessible-text limits are documented, and failed searches alone are not treated as novelty proof. A counterexample to a published infinite-completeness certification theorem under its own hypotheses, with arbitrarily long false finite certificates, identifies a precise missing availability premise and protects subsequent generalized anti-Waring computations. It is not a minor numerical discrepancy: the witness has gcd one, begins with 1 and has positive-density arithmetic progression tail, so it isolates a substantive logical gap.

## value

PASS

A counterexample to a published infinite-completeness certification theorem under its own hypotheses, with arbitrarily long false finite certificates, identifies a precise missing availability premise and protects subsequent generalized anti-Waring computations. It is not a minor numerical discrepancy: the witness has gcd one, begins with 1 and has positive-density arithmetic progression tail, so it isolates a substantive logical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
