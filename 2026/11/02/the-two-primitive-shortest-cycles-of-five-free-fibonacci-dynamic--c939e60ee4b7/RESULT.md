# The two primitive shortest cycles of five-free Fibonacci dynamics

## Finding
For positive integers define the five-free Fibonacci update by
\[
\mathcal F(a,b)=\frac{a+b}{5^{\nu_5(a+b)}},
\]
where \(\nu_5(m)\) is the greatest \(e\ge0\) such that \(5^e\mid m\). A positive periodic trajectory is a cyclic tuple \((a_0,\ldots,a_{L-1})\) satisfying \(a_{i+2}=\mathcal F(a_i,a_{i+1})\), with subscripts taken modulo \(L\).

**Theorem.** Every positive periodic trajectory of least period six is, up to a cyclic rotation, precisely one of
\[
 m(1,1,2,3,1,4)\qquad\text{or}\qquad m(4,3,7,2,9,11),
\]
where \(m\) is an arbitrary positive integer with \(5\nmid m\). These are the only two primitive least-period-six cycles up to rotation, and six is the smallest possible positive period of this dynamical system. The theorem does **not** classify possible longer cycles.

Both displayed primitive cycles were exhibited in Avila--Khovanova (2014); the new claim is their **exhaustiveness at period six**, with no restriction on the sizes of the starting terms or the powers of five removed at individual steps.

## Assumptions and scope
The recurrence uses positive integer terms. The valuation is the ordinary prime valuation at five; in particular the output is never divisible by five. A primitive cycle means that the gcd of all its entries is one. Equivalent cycles are identified only by cyclic rotation (not reflection), and scalar multiples are restricted by \(5\nmid m\). The claim is restricted to least period six and the absence of shorter positive cycles, not to all eventual behaviors or all longer periods.

## Proof
**1. A six-step determinant identity.** Fix an arbitrary positive periodic six-tuple. Write
\[
 5^{e_i}a_{i+2}=a_i+a_{i+1},\quad e_i=\nu_5(a_i+a_{i+1})\ge0,
 \qquad i\in\mathbb Z/6\mathbb Z,
\]
and put \(d_i=5^{e_i}\). Let \(M\) be the matrix of the six homogeneous equations: row \(i\) has entries \(-1\) in columns \(i,i+1\) and \(d_i\) in column \(i+2\), with all column indices modulo six. A nonzero six-tuple forces \(\det M=0\). Direct expansion of this six-by-six determinant gives
\[
 \prod_{i=0}^{5}d_i=
 \sum_{\substack{\varnothing\ne I\subseteq\mathbb Z/6\mathbb Z\\I\text{ contains no cyclicly adjacent pair}}}
 \prod_{i\in I}d_i. \tag{1}
\]
The right side is the nonconstant weighted independence polynomial of the six-cycle: it has six singleton, nine pair, and two triple terms. For a fully reproducible independent expansion using the signed Leibniz formula on all \(720\) column permutations, see `verify.py`. The checker confirms all \(18\) nonzero determinant monomials and their exact signs; this computation is a finite symbolic identity, not extrapolation.

**2. The division support is forced modulo five.** Some \(e_i\) must be positive, since if all are zero then equation (1) would read \(1=17\). Let \(U=\{i:e_i=0\}\). Reducing (1) modulo five, its left side vanishes, while the right side becomes the number of nonempty independent sets in the subgraph induced by \(U\) in a six-cycle. For \(|U|=1,2,3,4,5\), the possible counts are respectively
\[
 \{1\},\quad\{2,3\},\quad\{4,5,7\},\quad\{7,8,9\},\quad\{12\}.
\]
Thus, if \(U\) is nonempty, it must have exactly three vertices, inducing precisely one edge and one isolated vertex. There are twelve such labeled supports, in two classes under cyclic rotation. The case \(U=\varnothing\) is impossible: after dividing (1) by \(\prod_i d_i\), every summand is a reciprocal product involving at least three \(d_i\), so their sum is at most \(17/5^3<1\), whereas the normalized left side equals one.

**3. Every nonzero division exponent is exactly one.** The twelve possible supports are equivalent under dihedral symmetries of the six-cycle to \(U=\{0,1,3\}\). If each positive exponent is initially set to one, the corresponding vector is
\[
 (d_0,d_1,d_2,d_3,d_4,d_5)=(1,1,5,1,5,5).
\]
The weighted independence sum in (1), grouped by independent-set cardinality, is exactly
\[
 (18)+(77)+(30)=125=\prod_i d_i.
\]
Divide (1) by \(\prod_i d_i\), giving
\[
 1=\sum_{I\ne\varnothing,\ I\text{ independent}}
 \prod_{j\notin I}d_j^{-1}. \tag{2}
\]
If any positive \(e_i\) is raised above one, the right side strictly decreases: all summands are nonincreasing in \(d_i\), and at least one summand contains \(d_i^{-1}\). Therefore no exponent can exceed one. This proves that exactly three steps divide by five, each exactly once, with the twelve allowed zero-one patterns.

**4. The twelve patterns give two and only two primitive cycles.** Two representatives up to cyclic rotation are
\[
(e_0,e_1,e_2,e_3,e_4,e_5)=(0,0,1,0,1,1),
\quad (0,1,0,0,1,1).
\]
For the first, equations \(a_2=a_0+a_1\), \(a_3=a_0+2a_1\), \(5a_4=2a_0+3a_1\), and \(5a_0=a_3+2a_4\) force \(a_0=a_1\). The remaining equations then give the positive rational solution line spanned by \((1,1,2,3,1,4)\). For the second, equations \(a_2=a_0+a_1\), \(5a_3=a_0+2a_1\), and \(5a_0=2a_2+3a_3\) force \(3a_0=4a_1\); all equations then give the line spanned by \((4,3,7,2,9,11)\). Both vectors have gcd one, so all integral points on these lines are exactly their positive integer multiples.

Each displayed tuple directly obeys the six recurrence equations, and every entry is coprime to five. A scalar multiple remains a five-free trajectory precisely when its multiplier is coprime to five. The twelve patterns comprise the six rotations of each displayed tuple; there are no additional cases.

**5. Least-period minimality.** Modulo two, removal of a power of five does not change the recurrence. After dividing a periodic trajectory by its highest common power of two, its nonzero parity state evolves under the ordinary Fibonacci transition, which has period three on the three nonzero pairs over \(\mathbb F_2\). Thus every positive period is a multiple of three. A period-three trajectory with largest entry \(c\) has, after rotation, \(c=a+b\): a division by five could not produce a largest entry from two terms at most \(c\). The other two transitions must divide by positive powers, say \(5^u\) and \(5^v\), yielding \((5^u-1)a=2b\) and \((5^v-1)b=2a\). Their product implies \((5^u-1)(5^v-1)=4\), impossible for \(u,v\ge1\). Hence period six is the smallest positive period; the exhibited six-tuples have least period six. \(\square\)

## Verification
Run `python3 verify.py` using Python 3 and the standard library only. It independently expands the full signed six-step determinant, checks the independence-set identity coefficient by coefficient, enumerates all division supports modulo five, checks the sharp minimal-exponent equality, confirms that every surviving six-by-six recurrence matrix has rank five over \(\mathbb Q\), and verifies the two distinct cyclic rotation orbits by exact arithmetic. The expected output begins with `VERIFY_OK` and reports twelve signatures, two primitive classes, and rank five. These finite calculations check precisely the finite determinant and case enumeration used in the universal mathematical proof; the proof handles **all** positive integer starting values and arbitrarily large division exponents.

## Relationship to prior work
Avila and Khovanova, *Free Fibonacci Sequences* (arXiv:1403.4614, first public 2014-03-18; *Journal of Integer Sequences* 17 (2014), Article 14.8.5), introduced and studied these dynamics. Their Section 9 explicitly displays **both** primitive six-cycles and asks whether there are more; their Lemma 28 establishes the multiple-of-three period restriction for odd bases. The existence of either exhibited cycle and the parity-period argument are therefore **not** claimed as new. The present result proves that their two exhibited primitive cycles form an exhaustive classification of **all positive period-six trajectories**, including unbounded initial terms and division powers. OEIS A214684, initially authored in 2012, records the first initial-seed cycle but is not a classification across arbitrary seeds. No located paper or mathematical record gives the precise exhaustiveness conclusion; general coverage in unlocated literature remains possible.

## Limitations
This is only a shortest-period classification. It neither rules out additional primitive cycles of length nine, twelve, or higher nor proves global convergence or divergence for arbitrary starting values. The determinant argument exploits a fixed six-step relation and does not by itself classify arbitrary periods. Both explicit primitive cycles were already known; the contribution is the rigorous uniqueness statement at this natural boundary.

## References
1. B. Avila and T. Khovanova, *Free Fibonacci Sequences*, arXiv:1403.4614v1, public 2014-03-18. https://arxiv.org/abs/1403.4614 ; full text https://arxiv.org/html/1403.4614 .
2. B. Avila and T. Khovanova, *Free Fibonacci Sequences*, *Journal of Integer Sequences* **17** (2014), Article 14.8.5, Section 9, pp. 14–15. https://cs.uwaterloo.ca/journals/JIS/VOL17/Avila/avila4.pdf .
3. OEIS A214684, *Five-free Fibonacci recurrence for the initial pair \((1,1)\)*, originally submitted by John W. Layman, 2012-07-25. https://oeis.org/A214684 .
