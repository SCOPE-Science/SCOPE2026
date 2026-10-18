# A spectral counting law and Fibonacci multiplicities for the Moser–de Bruijn coefficient-three sumset

## Finding

Let \(\mathcal M\) be the Moser–de Bruijn set consisting of all nonnegative sums of distinct powers of \(4\). For \(n\ge0\), count coefficient-three representations as ordered pairs,
\[
R(n)=\#\{(a,b)\in\mathcal M^2:n=a+3b\}.
\]
Define the exact power-of-four support count \(H_k=\#\{n:0\le n<4^k,\ R(n)>0\}\) for integers \(k\ge0\). Then
\[
H_0=1,\quad H_1=3,\quad H_{k+2}=4H_{k+1}-2H_k,\qquad
H_k=\frac{(2+\sqrt2)^{k+1}+(2-\sqrt2)^{k+1}}4.
\]
With Fibonacci numbers \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\),
\[
\max_{0\le n<4^k} R(n)=F_{k+1}\quad\text{for every }k\ge0.
\]
Writing \(\alpha=\log_4(2+\sqrt2)\) and \(\beta=\log_4((1+\sqrt5)/2)\), the support counting function is \(\Theta(X^\alpha)\), whereas the maximum representation multiplicity below \(X\) is \(\Theta(X^\beta)\). In particular the support has natural density zero but unbounded representation multiplicity.

## Assumptions and scope

Every member of \(\mathcal M\) has a unique base-\(4\) expansion whose digits are drawn from \(\{0,1\}\), including the element \(0\). The pairs \((a,b)\) are ordered by their two distinct coefficient roles, not unordered summands. All bounds are exact for every integer \(k\ge0\); the real-variable asymptotic notation refers to \(X\to\infty\). Neither a uniform estimate in a variable coefficient nor a classification of all other coefficients is asserted.

## Proof

**Carry recurrence.** Fix an output \(n<4^k\) with its \(k\) base-\(4\) digits \(d_0,\ldots,d_{k-1}\), least significant first. At each position, a digit of \(a+3b\) is contributed by \(\epsilon+3\delta+c\), where \(\epsilon,\delta\in\{0,1\}\) and the incoming carry \(c\) is either \(0\) or \(1\). For any processed prefix let \(u\) and \(v\) count partial input pairs ending in carry \(0\) and carry \(1\), respectively, initially \((u,v)=(1,0)\). Direct enumeration of the four input possibilities yields, according to output digit \(d\),
\[
\begin{array}{c|cccc}
d&0&1&2&3\\\hline
(u,v)\mapsto &(u,u+v)&(u+v,v)&(v,0)&(u,0).
\end{array}
\]
No input digits above position \(k-1\) can occur in a representation of \(n<4^k\), since each summand is nonnegative. Therefore precisely those paths ending with carry \(0\) count, so \(R(n)=u\) after the full word.

**Exact support count.** The possible nonzero supports of the carry vector are \(A=\{0\}\) and \(B=\{0,1\}\); the empty support is absorbing. From \(A\), digits \(1,3\) lead to \(A\), digit \(0\) to \(B\), and digit \(2\) to the empty support. From \(B\), digits \(2,3\) lead to \(A\) and digits \(0,1\) to \(B\). Thus the numbers \(A_k,B_k\) of length-\(k\) output words ending in these respective supports obey
\[
\binom{A_{k+1}}{B_{k+1}}=\begin{pmatrix}2&2\\1&2\end{pmatrix}\binom{A_k}{B_k},\qquad(A_0,B_0)=(1,0).
\]
Every surviving support has a positive carry-\(0\) component, so \(H_k=A_k+B_k\). The matrix has characteristic polynomial \(t^2-4t+2\), yielding the stated recurrence, initial values, and closed form.

**Sharp multiplicity bound.** For every carry vector after any \(k\) digits, prove inductively
\[
\max(u,v)\le F_{k+1},\qquad\min(u,v)\le F_k.
\]
This holds for \((u,v)=(1,0)\) at \(k=0\). On digit \(0\) or \(1\), the new maximum is at most \(\max(u,v)+\min(u,v)\le F_{k+2}\), and the new minimum is at most \(F_{k+1}\). On digit \(2\) or \(3\), one component is zero and the other is an old component, so both bounds persist. Thus \(R(n)\le F_{k+1}\) whenever \(n<4^k\).

To attain equality for even \(k=2m\), choose the least-significant-first output digit word \((01)^m\). Successive paired transitions give the exact final vector \((F_{2m+1},F_{2m})\), including \(m=0\). For odd \(k=2m+1\), the word \(1\) works at \(k=1\); for \(m\ge1\), choose \(001(01)^{m-1}\), which yields \((F_{2m+2},F_{2m+1})\). All these words describe integers in \([0,4^k)\), so the upper bound is sharp.

**Arbitrary cutoffs.** The formula for \(H_k\) shows \(H_k=\Theta((2+\sqrt2)^k)\). Bracketing any \(X\ge1\) between two consecutive powers of \(4\) proves \(\#\{0\le n<X:R(n)>0\}=\Theta(X^{\alpha})\). Likewise the exact Fibonacci maximum and \(F_j=\Theta(((1+\sqrt5)/2)^j)\) prove the claimed \(\Theta(X^\beta)\) multiplicity bound. Since \(\alpha<1\), the support has density zero.

## Verification

The accompanying self-contained `verify.py` uses exact integers only. It independently enumerates all pair sums with \(k\le7\), compares every output multiplicity below \(4^k\) against the carry recurrence, and checks both exact extrema. It also explores carry vectors and explicit Fibonacci attaining witnesses for \(0\le k\le21\). Run `python3 verify.py` from the containing directory. These finite checks corroborate, but are not substitutes for, the induction and matrix argument.

## Relationship to prior work

Moser's 1962 paper proves that the same digit set gives unique representations \(n=a+2b\) and observes analogous complementary sets for other coefficients. De Bruijn (1964) investigates different signed direct decompositions by quaternary digit sets. Neither examined paper supplies the support count or maximum multiplicity for the **fixed original set** \(\mathcal M+3\mathcal M\). OEIS A000695 documents \(\mathcal M\); OEIS A007052 already records the numerical sequence \(1,3,10,34,116,\ldots\), its recurrence, and its closed form in other settings. No originality is asserted for the standalone numerical recurrence; the identification with this particular arithmetic sumset and the sharp Fibonacci multiplicity bound are the contributions. OEIS A126684 concerns the different basis \(\mathcal M\cup2\mathcal M\), whose self-sumset is all nonnegative integers. Relevant broader work on signed direct decompositions and potential unindexed equivalent descriptions leaves some literature risk.

## Limitations

The result counts all *nonnegative* coefficient-three representations with the ordered coefficient roles indicated, not canonical representations and not sums over a finite index list except when exact cutoff arguments allow it. No asymptotic pointwise distribution for the sequence \(R(n)\), no extension to an arbitrary coefficient, and no independent novelty certification are claimed. The previously known recurrence values alone are not treated as novel. Verification of a finite range cannot establish the infinite theorem.

## References

1. L. Moser, *An Application of Generating Series*, Mathematics Magazine 35(1) (1962), 37–38, DOI: 10.1080/0025570X.1962.11975291; full annotated scan: https://oeis.org/A000695/a000695.pdf.
2. N. G. de Bruijn, *Some Direct Decompositions of the Set of Integers*, Mathematics of Computation 18(88) (1964), 537–546, DOI: 10.1090/S0025-5718-1964-0167447-9; open author-institution copy: https://pure.tue.nl/ws/files/2084140/597531.pdf.
3. OEIS A000695, *Moser–de Bruijn sequence*, https://oeis.org/A000695 (including M. LeBrun's dated public comment of 2001-02-07).
4. OEIS A007052, *Number of order-consecutive partitions of n*, https://oeis.org/A007052 (already tabulates the same values and recurrence under a different interpretation).
5. OEIS A126684, *Union of A000695 and twice A000695*, https://oeis.org/A126684.
6. S. J. Eigen, Y. Ito and V. S. Prasad, *Universally Bad Integers and the 2-adics*, Journal of Number Theory 107 (2004), 322–334, DOI: 10.1016/j.jnt.2004.04.001 (abstract consulted only).
