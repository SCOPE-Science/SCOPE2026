# Four-primitive-root progressions at every step in safe-prime fields

## Finding

For a safe prime \(p=2q+1\), where \(q\) is prime, write \(N_p(d)\) for the number of \(x\in\mathbb F_p\) for which each of the four elements \(x+id\), with \(i=0,1,2,3\), has multiplicative order \(p-1\). Fix any nonzero \(d\in\mathbb F_p^\times\).

**Theorem.** Every safe prime \(p\ge47\) has \(N_p(d)\ge1\) for *every* nonzero \(d\). This safe-prime threshold is sharp: the safe prime \(p=23\) has differences for which \(N_p(d)=0\). The following exact formula determines the count for every safe prime \(p\ge11\), without enumerating primitive roots:

\[
N_p(d)=\frac{p-10-4\chi_p(2)+S_p}{16}-E_p(d),
\quad S_p=\sum_{t\in\mathbb F_p}\chi_p\bigl(t(t+1)(t+2)(t+3)\bigr),
\]

\[
E_p(d)=\sum_{j=0}^{3}\ \prod_{\substack{0\le i\le3\\i\ne j}}
\mathbf 1_{\{\chi_p(-1+(i-j)d)=-1\}},\qquad 0\le E_p(d)\le4.
\]

Here \(\chi_p\) is the quadratic character, extended by \(\chi_p(0)=0\). In particular the dependence on \(d\) is confined to four explicitly testable exceptional alignments with \(-1\).

For the complete list of safe primes below \(113\), exact minima and maxima over \(d\ne0\) are:

| \(p\) | \(\min_{d\ne0}N_p(d)\) | \(\max_{d\ne0}N_p(d)\) |
| ---: | ---: | ---: |
| 5 | 0 | 0 |
| 7 | 0 | 0 |
| 11 | 0 | 0 |
| 23 | 0 | 1 |
| 47 | 1 | 2 |
| 59 | 1 | 3 |
| 83 | 1 | 5 |
| 107 | 4 | 7 |

## Assumptions and scope

Throughout, \(p\) and \(q=(p-1)/2\) are ordinary rational primes; the common difference \(d\) and starting residue \(x\) range over the prime field. Progressions and primitivity are evaluated modulo \(p\), not as positive integer intervals. A primitive root is an element of multiplicative order \(p-1\). The exact character formula is asserted for safe primes \(p\ge11\); the smaller safe primes \(5,7\) are treated directly. The threshold statement is restricted to safe primes, without assuming that infinitely many safe primes exist.

## Proof

**1. Characterization of generators.** For \(p\ge11\) safe, \(q\) is odd, so \(p\equiv3\pmod4\); moreover \(q>3\) is prime and \(p\equiv11\pmod{12}\). Thus \(\chi_p(-1)=-1\) and \(\chi_p(3)=1\). Since the cyclic group \(\mathbb F_p^\times\) has order \(2q\), its primitive roots are exactly the quadratic nonresidues other than \(-1\): the sole non-generator among nonresidues has order two.

**2. The four-point quadratic-character count.** Let \(B_p^+\) and \(B_p^-\) be the numbers of \(t\in\mathbb F_p\) for which all four consecutive elements \(t,t+1,t+2,t+3\) are nonzero and have character respectively \(+1\) and \(-1\). The involution \(t\mapsto-3-t\) reverses and negates the four elements; hence \(B_p^+=B_p^-=B_p\), because \(\chi_p(-1)=-1\).

For either sign \(s=\pm1\), expand

\[
H_s=\frac1{16}\sum_{t\in\mathbb F_p}\prod_{i=0}^3(1+s\chi_p(t+i)).
\]

The odd-degree elementary-symmetric sums vanish by the same reflection. Each of the six pairwise sums is \(-1\): for distinct \(i,j\), the nonsquare quadratic \((t+i)(t+j)\) has character sum \(-1\). The quartic sum is \(S_p\). Therefore \(H_s=(p-6+S_p)/16\).

The product-indicator expansion is not automatically zero at the four roots of the quartic, because \((1+s\chi_p(0))/2=1/2\). At \(t=-1,-2\), the remaining factors include opposite character signs from \(1\) and \(-1\), so the product vanishes. At the two end roots \(t=0,-3\), the product vanishes unless \(\chi_p(2)=1\); if \(\chi_p(2)=1\), exactly one end root contributes \(1/2\) to \(H_s\), depending on \(s\). Consequently the root correction is precisely \((1+\chi_p(2))/4\) in each sign class, and

\[
B_p=\frac{p-6+S_p}{16}-\frac{1+\chi_p(2)}4
=\frac{p-10-4\chi_p(2)+S_p}{16}.
\]

**3. Every prescribed step and the exceptional element.** Substitute \(x=dt\). Since \(\chi_p(x+id)=\chi_p(d)\chi_p(t+i)\), requiring all four entries to be quadratic nonresidues amounts to requiring \(\chi_p(t+i)=-\chi_p(d)\) for all four indices. Step 2 gives exactly \(B_p\) such starting residues independently of \(d\). Of these, exclude progressions containing the unique nonprimitive nonresidue \(-1\). The four possible locations \(j\) of \(-1\) are disjoint because \(d\ne0\) and \(p\ge11\). If \(x+jd=-1\), the other entries equal \(-1+(i-j)d\); all must be nonresidues. Hence exactly \(E_p(d)\) progressions are removed. This proves the claimed formula and \(0\le E_p(d)\le4\).

**4. Uniform existence beyond a finite range.** The polynomial \(t(t+1)(t+2)(t+3)\) has four distinct roots and is not a square for \(p\ge11\). The standard Weil quadratic-character bound gives \(|S_p|\le3\sqrt p\). Using \(-4\chi_p(2)\ge-4\),

\[
B_p\ge\frac{p-14-3\sqrt p}{16}>4\qquad (p\ge113).
\]

The strict inequality follows because \(p-78-3\sqrt p\) is positive and increasing for real \(p\ge113\). As \(E_p(d)\le4\), this yields \(N_p(d)>0\) for every nonzero \(d\) whenever \(p\ge113\).

**5. The complete finite range.** The safe primes below \(113\) are exactly \(5,7,11,23,47,59,83,107\), by trial division of each candidate and its half-predecessor. For each prime and every \(1\le d<p\), enumerate \(0\le x<p\), computing primitivity independently by the criterion \(x^q\not\equiv1\pmod p\) and \(x^2\not\equiv1\pmod p\). The exact exhaustive counts are displayed in the table above and reproduced by the standard-library verifier. Its loops cover every admissible \(d\) and \(x\), rather than extrapolating from sampled cases. Thus \(47\) is the least safe-prime threshold that works for every \(d\), and the theorem follows.

## Verification

Run `python3 check_ap4.py` with Python 3 and no third-party modules. The program independently enumerates primitive roots using modular exponentiation, evaluates the quadratic character and exact character-sum identity, and directly checks all initial residues for all nonzero steps. The finite theorem-critical range \(p<113\) is exhaustive. The script additionally checks the formulas for every safe prime up to \(1000\); the latter tests are corroboration, not the basis for the universal assertion.

The exact finite table has \(p=23\) with eight zero-count differences and \(p=47\) with none. The proof's only infinite step is the stated Weil character-sum inequality; the finite verifier is not offered as a proof of that bound.

## Relationship to prior work

Cohen, Oliveira e Silva, and Trudgian studied consecutive primitive elements and published a four-consecutive-element conjecture in 2014 (arXiv:1410.6210). Jarso and Trudgian subsequently proved an exact exception list for *unit-step* runs of four primitive elements (arXiv:2109.11691); their theorem already covers the existence of a run of difference one in safe-prime fields \(p\ge47\). The contribution here is the stronger **every nonzero difference** assertion, its sharp safe-prime threshold, and the exact count \(N_p(d)\) with its four exceptional placements. An arbitrary multiplier does not preserve primitivity, so existence for difference one alone does not imply existence for every difference. Carella's study of fixed-offset primitive-root configurations (arXiv:1910.02308) supplies broader asymptotic context, but the inspected sections do not give this uniform sharp finite-field threshold and count. Unlocated equivalent statements remain a literature risk.

## Limitations

The bound applies only to prime fields with \(p=2q+1\) and both \(p,q\) prime. The quartic sum \(S_p\) remains in the exact formula; the theorem does not give a simpler elementary closed form for it. No bound is claimed for arbitrary primes, arbitrary progression lengths, or higher-degree extensions. The literature comparison is not a proof of novelty, and independent mathematical audit has not been performed.

## References

1. S. D. Cohen, T. Oliveira e Silva, and T. Trudgian, *On consecutive primitive elements in a finite field*, arXiv:1410.6210, first submitted 2014-10-22; https://arxiv.org/abs/1410.6210 .
2. T. Jarso and T. Trudgian, *Four consecutive primitive elements in a finite field*, arXiv:2109.11691, first submitted 2021-09-23; https://arxiv.org/abs/2109.11691 .
3. N. A. Carella, *Configurations of Consecutive Primitive Roots*, arXiv:1910.02308, first submitted 2019-10-05; https://arxiv.org/abs/1910.02308 .
4. Standard Weil bound for multiplicative character sums of squarefree degree-four polynomials over prime fields (as used, for example, in the character-sum literature cited by Reference 1).
