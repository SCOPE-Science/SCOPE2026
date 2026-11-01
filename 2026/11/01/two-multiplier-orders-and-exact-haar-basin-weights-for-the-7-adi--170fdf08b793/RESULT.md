# Two multiplier orders and exact Haar basin weights for the 7-adic quadratic map

## Finding
For \(f(x)=x^2+1\) on \(\mathbb Z_7\), let \(\alpha\equiv3\pmod7\) and \(\beta\equiv5\pmod7\) be its two fixed points, and normalize Haar measure by \(\mu(\mathbb Z_7)=1\). For \(m\ge1\) and \([u]\in\mathbb F_7^\times/\{\pm1\}\), define
\[
 A_{m,[u]}=(\alpha+7^m u+7^{m+1}\mathbb Z_7)\cup(\alpha-7^m u+7^{m+1}\mathbb Z_7),\qquad
 B_m=(\beta+7^m\mathbb Z_7)\setminus(\beta+7^{m+1}\mathbb Z_7).
\]
These are exactly the non-singleton minimal invariant clopen sets. On each \(A_{m,[u]}\), the map is an adding machine of cycle structure \((2,2\cdot7,2\cdot7^2,\ldots)\); on each \(B_m\), it is an adding machine of cycle structure \((6,6\cdot7,6\cdot7^2,\ldots)\). The only periodic points are \(\alpha,\beta\).

Write \(\mathcal B(S)=\{x:\exists j\ge0\ f^j(x)\in S\}\). The exact basin measures are
\[
 \mu(\mathcal B(A_{m,[u]}))=\frac4{7^{m+1}},\qquad
 \mu(\mathcal B(B_1))=\frac{31}{49},\qquad
 \mu(\mathcal B(B_m))=\frac{24}{7^{m+1}}\quad(m\ge2).
\]
Except for the countable preimages of \(\alpha,\beta\), these basins partition \(\mathbb Z_7\); their total masses around \(\alpha\) and \(\beta\) are \(2/7\) and \(5/7\), respectively.

## Assumptions and scope
The field has the usual \(7\)-adic absolute value, the system is the forward polynomial map on all of \(\mathbb Z_7\), and the minimality assertion refers to nonempty closed forward-invariant subsets of these clopen sets. The roots exist uniquely by Hensel's lemma because \(x^2-x+1\) has two simple roots \(3,5\) modulo seven. The notation \(u\) in a ball denotes any integer representative of its nonzero residue class. Basin mass is measured **before** iteration (not merely as the invariant mass of a component).

## Proof
**1. Residue dynamics and branches.** Modulo seven, \(0\mapsto1\mapsto2\mapsto5\), \(6\mapsto2\mapsto5\), \(4\mapsto3\mapsto3\), and \(5\mapsto5\). Thus every orbit reaches one of the two fixed residue balls. On each nonzero residue ball, \(f'(x)=2x\) is a unit; hence the corresponding step is a bijective isometry onto its target residue ball. The \(\alpha\)-residue ball therefore has exactly two equimeasurable first-entry branches (residues three and four). The \(\beta\)-residue ball has four isometric first-entry branches (residues five, two, six and one), plus the critical residue-zero ball.

**2. Neutral fixed points and local rotations.** Solving the fixed-point equation modulo \(49\) gives \(\alpha\equiv31\) and \(\beta\equiv19\pmod{49}\). The multipliers \(\lambda_r=2r\) have orders \(e_\alpha=2\), \(e_\beta=6\) in \(\mathbb F_7^\times\), and
\[
 \lambda_\alpha^2\equiv22\pmod{49},\qquad \lambda_\beta^6\equiv15\pmod{49}.
\]
In particular, \(v_7(\lambda_r^{e_r}-1)=1\). Put \(h=f^{e_r}\), and write \(y=x-r\). The coefficient of \(y^2\) in \(h(r+y)-r\) modulo seven equals \(\lambda_r^{e_r-1}\sum_{i=0}^{e_r-1}\lambda_r^i=0\), since \(\lambda_r\ne1\) and has exact order \(e_r\). Higher-degree terms have integral coefficients. For \(v_7(y)=m\ge1\), therefore
\[
 v_7(h(r+y)-(r+y))=m+1,
 \quad h'(r+y)\equiv1\pmod7.
\]
Indeed the linear displacement has valuation \(m+1\), the quadratic displacement has valuation at least \(2m+1\), and all terms of degree at least three have valuation at least \(3m>m+1\) except potentially \(m=1\), when \(3m=3>2\).

**3. Persistence of growing cycles.** We use the following elementary odd-prime lifting lemma. If an integral-coefficient polynomial \(g\) and a point \(x\) satisfy \(v_7(g(x)-x)=s\ge2\) and \(g'(x)\equiv1\pmod7\), then
\[
 v_7(g^7(x)-x)=s+1,\qquad (g^7)'(x)\equiv1\pmod7.
\]
For completeness, write \(\delta=g(x)-x\). Taylor expansion shows that along seven iterates the successive increments are congruent to \(\delta\) modulo \(7^{s+1}\), while their total is congruent to \(7\delta\) modulo \(7^{s+2}\): first-order variations contribute multiples of \(7^{s+1}\) whose sum has an additional factor seven, and the quadratic remainders have valuation at least \(2s\ge s+2\); for \(s=2\) the quadratic terms have order at least four and the needed congruence modulo \(7^{s+2}\) follows directly from the seven-step binomial sum. The derivative congruence follows by the chain rule. Applying this to \(h=f^{e_r}\), starting at every point in a depth-\(m\) shell, and then inducting, shows that its finite residue cycle at precision \(7^{m+j+1}\) has length exactly \(e_r7^j\) for every \(j\ge0\). Initial \(e_r\)-cycles split precisely according to the multiplier orbits on \(\mathbb F_7^\times\): three sign-pairs for \(r=\alpha\), and one six-element orbit for \(r=\beta\). All subsequent lifts grow, so each indicated clopen set is minimal and conjugate to the stated inverse-limit odometer. In particular there are no other periodic points in these shells.

**4. Critical branch and exact basin weights.** The critical residue-zero ball maps under three updates into \(5+49\mathbb Z_7\), since \(x\equiv0\pmod7\) implies \(f(x)\equiv1\), \(f^2(x)\equiv2\), \(f^3(x)\equiv5\pmod{49}\). As \(\beta\equiv19\pmod{49}\), this image lies entirely in \(B_1\). No other critical branch occurs. The measure of each \(A_{m,[u]}\) is \(2/7^{m+1}\), and its one additional isometric residue-four branch doubles this to \(4/7^{m+1}\). The measure of \(B_m\) is \(6/7^{m+1}\) and its four isometric branches contribute \(24/7^{m+1}\); for \(m=1\), the critical residue-zero ball contributes another \(1/7\), giving \(24/49+7/49=31/49\). All points enter a fixed residue ball in at most three steps; inside that ball, they lie in a unique shell or at its fixed root. Preimages of the two roots are countable and Haar null. Summation gives \(\sum_{m\ge1}\sum_{[u]}4/7^{m+1}=2/7\) and \(31/49+\sum_{m\ge2}24/7^{m+1}=5/7\).

## Verification
The standalone exact-integer script `verify.py` independently enumerates the entire functional graph of \(f\) modulo \(7^k\) for \(k=2,3,4,5\) (up to 16,807 residues), checking all shells, eventual classes, cycle lengths, branch masses, root congruences and multiplier congruences. The recorded output is `verify_output.txt`. Finite tests corroborate but do not replace the all-depth lifting proof above.

## Relationship to prior work
Fan and Liao's 2010 general minimal-decomposition theorem for polynomial maps of \(\mathbb Z_p\) establishes a qualitative decomposition and possible odometer types; the growing-cycle mechanism here uses its standard ideas. The claim here is the explicit global \(x^2+1\), \(p=7\) **complete shell-by-shell and preimage-basin Haar census**, notably the critical-branch jump from \(24/49\) to \(31/49\) for the first \(\beta\) shell, and the different two- versus six-cycle odometer types. A treatment of the squaring map \(x\mapsto x^2\) does not directly cover the translated quadratic \(x\mapsto x^2+1\). No universal novelty assertion is made.

## Limitations
The formulas are confined to the exact polynomial \(x^2+1\) on \(\mathbb Z_7\), not a parameter neighborhood or all odd primes. The orbit conjugacies are topological; no mixing or real-valued statistical limit is asserted. The source comparison may miss unindexed calculations of this specific example; independent validation is not performed.

## References
Fan, A.-H. and Liao, L.-M. *On minimal decomposition of \(p\)-adic polynomial dynamical systems* (first public arXiv version, 2010-10-27), arXiv:1010.5583, https://arxiv.org/abs/1010.5583. General decomposition, cycle-lifting and odometer context.

Fan, A.-H. and Liao, L.-M. *Dynamics of squaring map on \(p\)-adic integers* (2015). Comparison of a different quadratic dynamical system.
