# Exact five-support binary lunar prime counts

## Finding

For every integer \(m\ge4\), consider the binary integers whose highest nonzero digit is in position \(m\), whose units digit is one, and whose binary expansion has exactly five ones. Write \(C_m\) for the number of these integers that factor into two nonunit factors under binary lunar multiplication (digitwise AND for multiplication and OR for addition), and \(P_m\) for the number that are lunar primes. Then

\[
C_m=2\left\lfloor\frac{m-1}{2}\right\rfloor
+\mathbf1_{2\mid m}\left(\frac m2-1\right)
-2\mathbf1_{3\mid m}-2\mathbf1_{4\mid m},
\qquad
P_m=\binom{m-1}{3}-C_m.
\]

Equivalently, \(C_m=m-1-2\mathbf1_{3\mid m}\) for odd \(m\), while \(C_m=3m/2-3-2\mathbf1_{3\mid m}-2\mathbf1_{4\mid m}\) for even \(m\). Thus the composite count is a linear quasipolynomial of period dividing twelve, the composite population has order \(m\) with two parity-dependent slopes, and \(P_m/\binom{m-1}{3}\longrightarrow1\), with composite proportion \(\Theta(m^{-2})\). The first composite counts, for \(m=4,5,\ldots,15\), are \(1,4,4,6,7,6,12,10,11,12,18,12\).

The theorem also classifies *all* composite digit supports. For \(m\ge4\), each five-point composite support \(S\subseteq\{0,1,\ldots,m\}\) with \(0,m\in S\) belongs to at least one of these two families:
\[
\mathcal F_1:\quad S=\{0,x,2x,y,x+y\},\qquad
\mathcal F_2:\quad S=\{0,x,y,x+y,y+2x\},
\]
where the five displayed elements must be distinct, \(x,y\) are positive integers, and \(\max S=m\). The overlap between the families is exactly the single five-term arithmetic progression \(\{0,t,2t,3t,4t\}\) when \(4\mid m\) (where \(t=m/4\)), and it is empty otherwise.

## Assumptions and scope

A binary lunar integer \(N\) is encoded by the Boolean polynomial \(f_N(X)=\bigvee_{j\in S}X^j\), where \(S\) is the set of nonzero binary digit positions, Boolean addition is OR, and Boolean multiplication is AND, extended by convolution. Consequently the digit support of a lunar product is precisely the Minkowski sum \(A+B=\{a+b:a\in A,b\in B\}\). The multiplicative unit is the one-digit integer \(1\), with support \(\{0\}\). A *nontrivial factorization* has both factors different from the unit. Since the counted numbers are odd, a factorization into binary factors necessarily has \(0\in A\cap B\). All support sets are finite subsets of nonnegative integers. This result concerns exactly five occupied digit positions, not all lunar integers of the same bit length.

## Proof

**1. Reduction to a two-point times three-point sumset.** Suppose \(S=A+B\), with \(0\in A,B\) and \(|A|,|B|\ge2\). For finite nonempty integer sets, the elementary sumset bound is \(|A+B|\ge|A|+|B|-1\). The equality case, when both sets have at least two elements, forces both sets to be arithmetic progressions with the same step: this follows by arranging both sets increasingly and checking equality in the nested chains of ordered pair sums (the one-dimensional critical-pair lemma). As \(|S|=5\), the unordered size possibilities are \((2,2)\), \((2,3)\), \((2,4)\), and \((3,3)\). The first cannot have five output elements; in the last two equality forces \(S=\{0,t,2t,3t,4t\}\), which also admits the \((2,3)\) factorization \(\{0,t\}+\{0,t,3t\}\). Hence every composite \(S\) admits a factorization \(\{0,x\}+\{0,y,z\}\) with \(x>0\), \(0<y<z\).

**2. Two structural families.** This last sumset is the union of \(B=\{0,y,z\}\) and \(B+x\). It has exactly five elements if and only if the two three-point sets intersect in exactly one point. A positive difference between two elements of \(B\) is one of \(y,z,z-y\); hence the only possible values are \(x=y\), \(x=z\), or \(x=z-y\). If two such equalities hold simultaneously, then \(B=\{0,x,2x\}\) and the union has just four elements. The cases \(x=y\) and \(x=z\) therefore produce \(\mathcal F_1\); the case \(x=z-y\) produces \(\mathcal F_2\), with exactly the exclusions stated in the finding.

**3. Count the first family.** If \(0<y<x\), the maximum is \(2x=m\), so there are \(m/2-1\) parameter pairs when \(m\) is even and none otherwise. If \(y>x\), the maximum is \(x+y=m\), so \(1\le x\le\lfloor(m-1)/2\rfloor\), excluding \(y=2x\), which occurs precisely when \(3\mid m\). Each branch separately gives distinct sets: its parameter \(x\) or \(y\) is recovered from the ordered support. A set from the first branch can also occur in the second only when its five elements form \(\{0,t,2t,3t,4t\}\); in that case the two descriptions are \((x,y)=(2t,t)\) and \((x,y)=(t,3t)\). To see this, compare the second and third smallest elements of the two ordered presentations: in the second branch the second is always \(x\), and the third is either \(2x\) or \(y\), while in the first branch the second is \(y\) and the third is \(x=m/2\). Their coincidence forces \(x=m/4\). Therefore
\[
|\mathcal F_1|=\left\lfloor\frac{m-1}{2}\right\rfloor-
\mathbf1_{3\mid m}+\mathbf1_{2\mid m}\left(\frac m2-1\right)-\mathbf1_{4\mid m}.
\]

**4. Count the second family.** Its maximum is \(y+2x=m\). Thus \(1\le x\le\lfloor(m-1)/2\rfloor\), with \(y=m-2x>0\), and the only degeneration occurs at \(y=x\), equivalent to \(3\mid m\). Every permitted parameter \(x\) determines a distinct support. Indeed, if \(y>x\), its second-smallest element is \(x\); if \(y<x\), its second-smallest element is \(y\). A support occurring in both parameter regimes would force simultaneously \(m=y+2x\) and \(m=x+2y\) after interchanging the second and third elements, hence \(x=y\), which is forbidden. It follows that
\[
|\mathcal F_2|=\left\lfloor\frac{m-1}{2}\right\rfloor-\mathbf1_{3\mid m}.
\]

**5. Their intersection.** The sorted forms of members of \(\mathcal F_1\), according as \(y<x\), \(x<y<2x\), or \(y>2x\), are respectively
\[
(0,y,x,x+y,2x),\quad(0,x,y,2x,x+y),\quad(0,x,2x,y,x+y).
\]
The sorted forms in \(\mathcal F_2\), according as \(y<x\) or \(y>x\), are respectively
\[
(0,y,x,x+y,y+2x),\quad(0,x,y,x+y,y+2x).
\]
Equating the five coordinates in the six pairwise comparisons shows that the only feasible common set is \(\{0,t,2t,3t,4t\}\): in the first regime of \(\mathcal F_1\), the comparison forces \(x=2y\); in its middle regime no comparison is feasible; in its last regime the comparison forces \(y=3x\). Conversely these arithmetic progressions occur in both families. Hence \(|\mathcal F_1\cap\mathcal F_2|=\mathbf1_{4\mid m}\). Inclusion–exclusion gives the claimed expression for \(C_m\).

**6. Primes and limiting proportion.** The three nonzero interior positions can be chosen in \(\binom{m-1}{3}\) ways. Because both endpoints are nonzero, all nontrivial lunar factorizations are exactly the sumset decompositions already counted. Subtracting gives \(P_m\). Since \(C_m\) grows linearly and \(\binom{m-1}{3}\sim m^3/6\), the prime proportion tends to one with the stated sharp order \(m^{-2}\).

## Verification

The included `verify_lunar_five.py` performs independent integer-set enumeration of all possible \((2,3)\) factors with union of size five for each \(m\) from \(4\) through \(130\), compares the distinct-support counts with the explicit formula, and separately enumerates all \((2,2)\), \((2,3)\), \((2,4)\), and \((3,3)\) factor pairs for \(4\le m\le14\), checking that the reduction does not omit any composite. The output is `VERIFY_OK: 127 degrees m=4..130; independent 2-by-3 enumeration; all factor shapes m<=14; closed counts.` This is finite corroboration, not a replacement for steps 1–6 of the proof.

## Relationship to prior work

Applegate, LeBrun, and Sloane (2011) introduced the binary dismal/lunar prime arithmetic and enumerated prime totals without the exact five-one support census given here. Gross (2019) studied maximally decomposable integer sumsets and their lunar divisor interpretation, not a fixed-five-support prime count. Baily and collaborators (2025) established almost-everywhere indecomposability for broad classes of lunar polynomials, but their unrestricted degree asymptotic does not by itself give this exact fixed-weight quasipolynomial or the two explicit support families. OEIS A087636 is an early public record of the lunar prime counting problem (entry dated 2003-10-26). A separate previously described divisor-count identity for sparse block supports concerns a particular indexed family, not the full five-support census. Comparison is by mathematical implication and scope, not by matching words.

## Limitations

The theorem applies to odd binary lunar numbers with exactly five one digits and degree at least four. It does not classify factorization multiplicities, other digit weights, or bases above two. The count of degree-\(m\) five-one primes is not the same as the total degree-\(m\) prime count. The proof is complete within its stated hypotheses, while definitive absence of an unindexed equivalent enumeration in the broader additive-combinatorics literature remains a priority limitation. Independent external mathematical review has not been performed.

## References

1. OEIS Foundation, *A087636: Number of n-digit lunar primes*, contributed by M. LeBrun and N. J. A. Sloane, 2003-10-26. https://oeis.org/A087636
2. D. Applegate, M. LeBrun and N. J. A. Sloane, *Dismal Arithmetic*, Journal of Integer Sequences 14 (2011), Article 11.9.8; arXiv:1107.1130. https://arxiv.org/abs/1107.1130
3. G. Gross, *Maximally Additively Reducible Subsets of Integers*, arXiv:1908.05220 (2019). https://arxiv.org/abs/1908.05220
4. B. Baily, J. Dell, H. L. Fleischmann, F. Jackson, S. J. Miller, E. Pesikoff and L. Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7. https://cs.uwaterloo.ca/journals/JIS/VOL28/Jackson/jackson5.pdf
