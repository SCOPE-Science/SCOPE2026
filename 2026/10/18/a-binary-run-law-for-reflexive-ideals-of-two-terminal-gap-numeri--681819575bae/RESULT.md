# A binary-run law for reflexive ideals of two-terminal-gap numerical semigroups

## Finding

For each integer \(m\ge3\), consider the two numerical semigroups
\[
S_m^{(1)}=\{0\}\cup\{m,m+1,\ldots,2m-2\}\cup[2m,\infty)\cap\mathbb Z,
\qquad
S_m^{(2)}=\{0\}\cup\{m,m+1,\ldots,2m-3\}\cup[2m,\infty)\cap\mathbb Z.
\]
A *normalized ideal* of \(S\) is an ideal \(I\) with \(\min I=0\), equivalently \(S\subseteq I\subseteq\mathbb N\). For subsets of integers, set \(S-I=\{z\in\mathbb Z:z+I\subseteq S\}\), and call \(I\) *reflexive* (or *divisorial*, *bi-dual closed*) when \(I=S-(S-I)\).

**Theorem.** The semigroup \(S_m^{(1)}\) has exactly \(2^{m-1}+1\) normalized ideals, all reflexive. The semigroup \(S_m^{(2)}\) has exactly \(2^{m-1}+5\) normalized ideals, of which exactly \(a_{m-1}+1\) are reflexive, where \(a_n\) is the number of binary words of length \(n\) containing no isolated zero (all zero-runs have length at least two). Explicitly,
\[
a_n=\sum_{k=0}^{\lfloor(n+1)/3\rfloor}{n-k+1\choose2k},\qquad
\sum_{n\ge0}a_nz^n=\frac{1-z+z^2}{1-2z+z^2-z^3}.
\]
Thus \(a_0=a_1=1\), \(a_2=2\), and \(a_n=2a_{n-1}-a_{n-2}+a_{n-3}\) for \(n\ge3\). If \(\lambda\simeq1.754877666246693\) is the positive root of \(\lambda^3-2\lambda^2+\lambda-1=0\), the proportion of normalized ideals of \(S_m^{(2)}\) that are reflexive decays exponentially, with
\[
\frac{a_{m-1}+1}{2^{m-1}+5}\sim C(\lambda/2)^{m-1},
\quad C=-\frac{1-r+r^2}{r(-2+2r-3r^2)},\quad r=\lambda^{-1},\quad C\simeq0.7221244183.
\]

More precisely, the normalized ideals of \(S_m^{(2)}\) that contain both terminal gaps are indexed by subsets \(T\subseteq\{1,\ldots,m-1\}\). Their reflexive closure is obtained by adding precisely those absent elements of \(T\) that form singleton zero-runs. The ideal \(S_m^{(2)}\) itself is the one further reflexive ideal.

## Assumptions and scope

All sets are subsets of \(\mathbb Z\); intervals such as \([2m,\infty)\cap\mathbb Z\) contain only integers. The conductor is \(2m\) in both families, and \(S_m^{(j)}\) is closed under addition because the sum of two positive members is at least \(2m\). All ideals counted are **normalized**, not arbitrary integral ideals, translated relative ideals, or ring ideals. A binary one signifies that the corresponding low gap is included; zero signifies exclusion. The numerical result is for all integers \(m\ge3\), not a bounded enumeration.

## Proof

**1. Classification of normalized ideals.** Fix \(m\ge3\), write \(b=2m-2\), \(c=2m-1\), and \(L=\{1,\ldots,m-1\}\). The gaps of \(S_m^{(2)}\) are precisely \(L\cup\{b,c\}\). Every normalized ideal is obtained by adjoining some gaps to \(S_m^{(2)}\), provided the result is closed under addition by \(S_m^{(2)}\).

If neither \(b\) nor \(c\) is adjoined, no low gap may be adjoined: an adjoined \(x\in L\) has \(b-x\in S_m^{(2)}\) when \(x\le m-2\), or \(c-x=m\in S_m^{(2)}\) when \(x=m-1\). This gives only \(S_m^{(2)}\). If \(b\) but not \(c\) is adjoined, the only allowed low gap is \(1\), giving two ideals, since every \(2\le x\le m-1\) has \(c-x\in S_m^{(2)}\). Likewise, if \(c\) but not \(b\) is adjoined, only the low gap \(m-1\) may also be adjoined, giving two ideals. If both \(b\) and \(c\) are adjoined, every subset \(T\subseteq L\) is possible: the ideal is \(I_T=S_m^{(2)}\cup\{b,c\}\cup T\), and all sums with positive elements of \(S_m^{(2)}\) lie in \([m,\infty)\subseteq I_T\). Therefore there are \(1+2+2+2^{m-1}=2^{m-1}+5\) normalized ideals.

**2. Reduction to the two-gap-containing ideals.** Every ideal contains itself in its double dual. For a normalized ideal \(I\ne S_m^{(2)}\), the presence of a gap means \(0\notin S_m^{(2)}-I\). But \(0\in I\) implies \(S_m^{(2)}-I\subseteq S_m^{(2)}\). Thus every element of the dual is at least \(m\). It follows that \(b\) and \(c\) belong to \(S_m^{(2)}-(S_m^{(2)}-I)\), since adding them to any integer at least \(m\) gives an integer at least \(2m\) in the semigroup. Hence a reflexive ideal other than \(S_m^{(2)}\) must contain both \(b\) and \(c\). The ideal \(S_m^{(2)}\) is reflexive because \(S-S=S\).

**3. Exact dual and closure.** Fix \(I_T\), let \(t_i\in\{0,1\}\) record inclusion of \(i\in L\) and set \(t_0=t_m=1\) only as boundary conventions for the zero-run test. For \(0\le j\le m-3\), the positive semigroup element \(m+j\) belongs to the dual exactly if neither of the two low gaps that would carry its sum into \(b\) or \(c\) is present. Thus
\[
S_m^{(2)}-I_T=
\{m+j:0\le j\le m-3,\ t_{m-2-j}=t_{m-1-j}=0\}
\cup([2m,\infty)\cap\mathbb Z).
\]
There are no other dual elements: the dual is contained in \(S_m^{(2)}\), and \(I_T\) contains \(b,c\). In its second dual, all members of \(I_T\) remain, no negative integer enters (for \(x<0\) use \(z=c-x\ge2m\) in the dual and \(x+z=c\notin S_m^{(2)}\)), and no restriction concerns integers at least \(2m\). For a missing low index \(x\in L\), exclusion from the second dual is witnessed precisely when one of the adjacent indices \(x-1\) or \(x+1\) within \(L\) is also missing. Indeed the only possible forbidden sums with \(m+j\) are \(b\) and \(c\); they correspond respectively to \(j=m-2-x\), requiring \(t_x=t_{x+1}=0\), and \(j=m-1-x\), requiring \(t_{x-1}=t_x=0\). The valid range of \(j\) enforces the endpoints. Thus the double dual fills exactly the isolated missing low indices, so \(I_T\) is reflexive if and only if the binary word \((t_1,\ldots,t_{m-1})\) has no zero-run of length one.

**4. Binary-word count.** Let \(n=m-1\). A word with exactly \(k\) zero-runs of lengths at least two has minimal length \(3k-1\), from \(2k\) zeros and the \(k-1\) mandatory separating ones. Distributing the remaining \(n-3k+1\) positions among the \(2k+1\) nonnegative slack variables (zero-run extensions and the \(k+1\) one-blocks) gives \({n-k+1\choose2k}\). For \(k=0\) the all-one word contributes one. The regular-language decomposition into repetitions of either a single one or a zero-run of length at least two followed by one, with an optional final zero-run, has generating function
\[
\frac{1+z^2/(1-z)}{1-z-z^3/(1-z)}
=\frac{1-z+z^2}{1-2z+z^2-z^3}.
\]
The recurrence follows by multiplying by the denominator. The denominator has the unique root of smallest modulus \(r=1/\lambda\), where \(\lambda\) is the positive real root given above; the other two characteristic roots form a conjugate pair of modulus less than one. Partial fractions show \(a_n\sim C\lambda^n\) with the displayed positive residue constant. Since \(\lambda<2\), the density decays exponentially.

**5. Comparison with one terminal gap.** The gaps of \(S_m^{(1)}\) are \(L\cup\{c\}\). Closure under addition by \(S_m^{(1)}\) forces inclusion of \(c\) as soon as a low gap is adjoined, and any subset of low gaps can then be chosen. This gives \(2^{m-1}+1\) normalized ideals. Furthermore \(S_m^{(1)}\) is symmetric with Frobenius number \(c=2m-1\): for every integer \(x\), exactly one of \(x\) and \(c-x\) lies in \(S_m^{(1)}\). For any ideal \(I\) and any \(x\notin I\), let \(z=c-x\). For each \(i\in I\), if \(z+i\notin S_m^{(1)}\), symmetry would imply \(x-i\in S_m^{(1)}\), hence \(x\in I\), contradiction. Therefore \(z\in S_m^{(1)}-I\) but \(x+z=c\notin S_m^{(1)}\), proving \(x\notin I^v\). Hence every ideal is reflexive.

## Verification

The supplied standalone `verify_reflexive.py` enumerates **all** gap subsets for each of the two semigroup families at every integer \(3\le m\le13\). It checks ideal closure by direct addition, then computes the double dual by independently testing its defining quantified membership condition on the finite conductor window. For each of the \(22\) cases it compares total and reflexive counts to the theorem. Example results: for \(m=10\), the two-gap family has \(517\) normalized ideals, \(115\) reflexive; the one-gap family has \(513\), all reflexive. Replay using `python3 verify_reflexive.py`; a successful run ends in `VERIFY_OK`. This bounded enumeration is a reproducibility check, not the proof for arbitrary \(m\).

## Relationship to prior work

Campochiaro, D’Anna, and García-Sánchez, *Reflexive ideals of a numerical semigroup* (arXiv:2610.06426v1, first available October 5, 2026), provide the framework for numerical biduality, irreducible reflexive ideals, and Apéry formulas, and characterize reflexivity in several important semigroup classes. Their Proposition 52 gives the classical symmetric-semigroup implication used above; no exact two-terminal-gap word enumeration or exponential density law was found in the relevant manuscript sections. Spirito, *Star operations on numerical semigroups: antichains and explicit results* (arXiv:1604.02862), studies v-closure and the number of star operations, a different enumeration invariant. The present claim is the explicit two-family normalized-ideal census and local singleton-zero closure rule, **not** the general theory of reflexive ideals or the previously known symmetric case.

## Limitations

The theorem counts normalized numerical-semigroup ideals, not translated fractional ideals, ring-theoretic modules, or arbitrary numerical semigroups of conductor \(2m\). The closure rule for nontrivial ideals containing both terminal gaps does not purport to describe all other semigroup families. Literature searches do not establish absolute novelty: an equivalent formula in unindexed work, tables, or another combinatorial formulation remains possible. The independent scientific audit has not been performed.

## References

1. P. Campochiaro, M. D’Anna, P. A. García-Sánchez, *Reflexive ideals of a numerical semigroup*, arXiv:2610.06426v1 (October 5, 2026), https://arxiv.org/html/2610.06426v1.
2. D. Spirito, *Star operations on numerical semigroups: antichains and explicit results*, arXiv:1604.02862, https://arxiv.org/abs/1604.02862.
3. S. Bonzio and P. A. García-Sánchez, *The poset of normalized ideals of numerical semigroups with multiplicity three*, Communications in Algebra (2025), title/abstract used to delimit the fixed-multiplicity scope.
