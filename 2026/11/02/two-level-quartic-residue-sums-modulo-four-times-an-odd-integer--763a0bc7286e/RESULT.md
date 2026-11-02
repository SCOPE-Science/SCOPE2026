# Two-level quartic residue sums modulo four times an odd integer

## Finding
Let \(q>1\) be any odd integer, put \(m=4q\) and \(e=2q-1\), and let \(\omega(q)\) count distinct prime divisors. Consider the collection \(\mathcal H(q)\) of cyclic subgroups \(H\le(\mathbb Z/m\mathbb Z)^\times\) with \(|H|=4\) and with unique involution represented by \(e\). Define the least-positive-residue sum \(S(H)=\sum_{h\in H}\langle h\rangle_m\), where \(\langle h\rangle_m\in\{1,\ldots,m-1\}\).

**Theorem.** The collection \(\mathcal H(q)\) is nonempty if and only if every prime dividing \(q\) is congruent to \(1\pmod4\). When nonempty, it contains exactly \(2^{\omega(q)}\) subgroups and its residue sums take precisely two values, each with multiplicity \(2^{\omega(q)-1}\):
\[
 \#\{H\in\mathcal H(q):S(H)=m\}
 =\#\{H\in\mathcal H(q):S(H)=2m\}
 =2^{\omega(q)-1}.
\]
In particular, exactly half are sum-centered in the sense \(S(H)=m|H|/2=2m\), although none contains \(-1\).
For example, at \(q=5\) the two qualifying subgroups modulo \(20\) are \(\{1,3,7,9\}\) with sum \(20\) and \(\{1,9,13,17\}\) with sum \(40\). This realizes both levels and a centered subgroup lacking complement-pairing by \(-1\).

## Assumptions and scope
The integer \(q\) can be composite, have repeated prime factors, and have any number of distinct prime divisors. The unique involution is specified by its residue \(e=2q-1\) modulo \(4q\); it is not the element \(-1\). The assertion concerns only cyclic subgroups with this specified involution, not all cyclic subgroups of order four and not the stronger condition that every multiplicative coset have a centered residue sum. The cases where \(q=1\) or \(q\) is even are excluded.

## Proof
1. **Roots and local existence.** Since \(e\equiv1\pmod4\) and \(e\equiv-1\pmod q\), the congruence \(x^2\equiv e\pmod{4q}\) is equivalent to \(x\) being odd and \(x^2\equiv-1\pmod q\). The latter is solvable at a prime power \(p^a\parallel q\) precisely when \(p\equiv1\pmod4\); Fermat's theorem supplies the necessity and cyclicity of the prime-field multiplicative group the sufficiency. There are exactly two roots modulo \(p\), and each lifts uniquely to a root modulo \(p^a\), since the derivative \(2x\) is prime to \(p\). The Chinese remainder theorem yields \(2^{\omega(q)}\) roots modulo \(q\), and each has two odd lifts modulo \(4q\); thus there are \(2^{\omega(q)+1}\) solutions modulo \(m\).

2. **The subgroup count.** Because \(e^2\equiv1\pmod m\) and \(e\not\equiv1\pmod m\) for \(q>1\), any solution of \(x^2\equiv e\pmod m\) has multiplicative order exactly four. Conversely, both generators \(x\) and \(x^3\) of a cyclic group in \(\mathcal H(q)\) solve this congruence, and every solution generates such a group. Each group has exactly two generators. The number of groups is therefore \(2^{\omega(q)}\).

3. **Only two sums.** Write \(u=\langle x\rangle_m\). Since \(x\) is odd, \(2qx\equiv2q\pmod{4q}\). Consequently \(x^3\equiv ex\equiv2q-u\pmod{4q}\), whose least-positive representative is \(2q-u\) if \(u<2q\) and \(6q-u\) if \(u>2q\). Equality \(u=2q\) is impossible because \(u\) is a unit. As the four elements of the group are \(1,x,e,x^3\), their least-positive representatives have sum
\[
S(\langle x\rangle)=1+(2q-1)+u+\langle x^3\rangle_m
=\begin{cases}4q=m,&u<2q,\\8q=2m,&u>2q.\end{cases}
\]
Both generators of the same group lie in the same half of the residue interval, by the preceding formulas.

4. **Equal multiplicities.** Send \(\langle x\rangle\) to \(\langle x+2q\rangle\), with addition taken modulo \(4q\). We have \((x+2q)^2\equiv x^2\pmod{4q}\), so this is again a generator of order four with square \(e\). It is well defined on subgroups: replacing \(x\) by \(x^3=ex\) replaces \(x+2q\) by \(e(x+2q)\), which is its cube, because \(e(2q)\equiv2q\pmod{4q}\). The map is an involution and interchanges the two open halves \((0,2q)\) and \((2q,4q)\). It has no fixed subgroup, since a fixed group would require \(x+2q\equiv x\) or \(x+2q\equiv x^3\pmod{4q}\); the first contradicts \(2q\not\equiv0\pmod{4q}\), and the second gives \(2x\equiv0\pmod{4q}\), impossible for a unit \(x\). It pairs every sum-\(m\) group with a sum-\(2m\) group. The count follows.

Finally \(e=2q-1\not\equiv-1\pmod{4q}\), and \(e\) is the only element of order two in each of these cyclic groups; hence none contains \(-1\). \(\square\)

## Verification
Run `python3 verify.py` with standard Python 3. The checker enumerates every odd \(q\) from \(3\) to \(1999\), constructs every quadratic root of \(e\) modulo \(4q\), deduplicates the resulting cyclic subgroups, and checks the asserted nonemptiness condition, counts, two possible exact sums, absence of \(-1\), and the fixed-point-free pairing. It reports 999 tested odd moduli, 764 empty cases, and 638 qualifying subgroups. All checks use integer arithmetic. These finite checks corroborate the proof; the universal quantifier over all odd \(q>1\) follows from the argument above.

## Relationship to prior work
Ma, Merca and Zhang (2026), arXiv:2610.29608v1, study sum-centering of multiplicative cyclic subgroups for moduli that are products of **two distinct odd primes**. Their original results and appendix/supplementary descriptions address odd semiprimes, local quartic characters, and mixed half-order involutions; they do not state the present even-modulus \(4q\) two-level theorem or the precise \(2^{\omega(q)-1}\) counts for arbitrary odd \(q\). This theorem addresses the same invariant, but a different and explicitly delimited local fiber of quartic groups.

Pomerance and Ulmer (2012), arXiv:1204.6705v1, study the stronger property that **every** multiplicative coset has equally many elements in the two halves of the unit group. Their character criterion and small-order results do not state the present first-moment classification on the subgroup itself. In fact, their Theorem 3.1 implies that for sufficiently large \(4q\), these groups cannot satisfy the stronger condition: they contain neither \(-1\) nor \(2q+1\). Thus a centered sum here should not be confused with their full-coset balance.

Girstmair's 1997 paper develops a general distribution-vector framework for arbitrary moduli, and his recent survey focuses on prime-modulus power residues. The 1997 complete article was not accessible during the present comparison. Its abstract alone cannot rule out an earlier specialization, which is an explicit residual priority risk.

## Limitations
The statement is restricted to the involution \(2q-1\) and does not classify all quartic subgroups of \((\mathbb Z/4q\mathbb Z)^\times\). The theorem is elementary and gives no new estimates for higher-order cyclic subgroups or the distribution of noncentered sums in other local fibers. The proof is complete as written, but publication priority is not independently verified. The closed-form counts do not require numerical computation.

## References
1. H. Ma, M. Merca, and W. Zhang, *Residue Sums Modulo Products of Two Distinct Odd Primes*, arXiv:2610.29608v1, first submitted 2026-10-21. https://arxiv.org/abs/2610.29608
2. C. Pomerance and D. Ulmer, *On Balanced Subgroups of the Multiplicative Group*, arXiv:1204.6705v1 (2012). https://arxiv.org/abs/1204.6705
3. K. Girstmair, *Class number factors and distribution of residues*, Abh. Math. Sem. Univ. Hamburg 67 (1997), 65–104. DOI: 10.1007/BF02940820. Full text not inspected.
4. K. Girstmair, *Power Residues, Digit Expansions, and Relative Class Numbers*, arXiv:2509.21094v1 (2025). https://arxiv.org/abs/2509.21094
