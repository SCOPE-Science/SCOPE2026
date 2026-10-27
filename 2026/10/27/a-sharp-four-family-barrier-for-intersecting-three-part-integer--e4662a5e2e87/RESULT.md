# A sharp four-family barrier for intersecting three-part integer partitions

## Finding

Let \(P_{n,3}\) denote the partitions of the positive integer \(n\) into exactly three positive parts, with the order of parts ignored. Two partitions intersect when they share a part value, even if that value occurs in different positions. An intersecting family is **nontrivial** when no single part value occurs in every member.

**Theorem.** For every integer \(n\ge 3\):

1. Every nontrivial intersecting family \(\mathcal F\subseteq P_{n,3}\) has at most four members. This bound is attained for every \(n\ge8\).
2. The largest intersecting-family size is
   \[
   M(n)=\begin{cases}
   4,&n=8,\\
   \lfloor(n-1)/2\rfloor,&n\ne8.
   \end{cases}
   \]
3. For odd \(n\ge11\), the unique largest family is the full star of partitions containing \(1\). For even \(n\ge12\), the only largest families are the full stars centered at \(1\) and \(2\). At \(n=8\) the unique largest family is
   \[
   \{(1,2,5),(1,3,4),(2,2,4),(2,3,3)\}.
   \]

The theorem determines the previously open three-part, one-intersection case of the fixed-length question in Borg's 2016 work, including its exceptional order \(8\). It does not address other lengths or higher intersection parameters.

## Assumptions and scope

The parts are strictly positive integers. A partition is identified with its nondecreasing triple, but in proofs we may permute its entries. For a partition \(\lambda\), write \(S(\lambda)\) for the set of its distinct part values. Distinct partitions \(\lambda,\mu\in P_{n,3}\) satisfy
\[
|S(\lambda)\cap S(\mu)|\le1.
\]
Indeed, fixing any two distinct shared values and the total \(n\) fixes the third part and hence the partition; if one partition has a repeated part, a different partition with the same two distinct values would have a different multiplicity and thus a different sum. This **linearity property** is the key hypothesis that would fail for arbitrary triple systems.

## Proof

**1. A triangle of intersections.** Suppose \(\mathcal F\) is nontrivial and intersecting. If one member is \((a,a,a)\), then every other member contains \(a\), a contradiction. Consequently all members have two or three distinct part values. Pick two members meeting in the value \(a\). As \(\mathcal F\) has no common value, some third member avoids \(a\). Its intersections with the first two members are at distinct values \(b,c\); equality would contradict the linearity property. We obtain three members whose pairwise intersections have three distinct values \(a,b,c\). We call these the base triangle.

**2. Base triangle with three distinct values in each member.** Denote its support sets by
\[
E_1=\{a,b,u\},\quad E_2=\{a,c,v\},\quad E_3=\{b,c,w\}.
\]
Here the six displayed values are pairwise distinct, by linearity. The fixed-sum condition gives
\[
a+b+u=a+c+v=b+c+w=n.\]
A fourth member cannot avoid all of \(a,b,c\). If it did, it would have to contain the three values \(u,v,w\), and hence \(u+v+w=n\). Adding the three base equations gives \(2(a+b+c)+(u+v+w)=3n\), so \(a+b+c=n\); then \(u=c\), contradicting distinctness.

Every additional member therefore contains exactly one of \(a,b,c\), since containing two would share two values with a base member. An additional member containing \(a\) must also contain \(w\) to meet \(E_3\), and is uniquely determined because it contains the pair \(\{a,w\}\). Counting multiplicities, its third part must be \(b+c-a\), even when that third part equals \(a\) or \(w\). Likewise, any additional member through \(b\) must contain \(v\), and its third part is \(a+c-b\). By linearity these two additional members could meet only if their third parts agreed, which would imply \(a=b\). This is impossible. The same argument, by symmetry, excludes two additional members attached at any two different base vertices. Thus at most one member lies outside the base triangle.

**3. Base triangle containing a repeated-part member.** Choose such a member as the base edge. Its distinct values are \(a,b\), and after exchanging these two names we can write it as \((a,a,b)\), so \(n=2a+b\) and \(a\ne b\). Nontriviality yields members meeting it at \(a\) but not \(b\), and at \(b\) but not \(a\). Call these \(E_2,E_3\). They meet at a further value \(c\), and thus form the base triangle.

Every additional member must meet the first member at \(a\) or \(b\). An additional member through \(a\) must meet \(E_3\) at a value other than \(c\); likewise, an additional member through \(b\) must meet \(E_2\) at a value other than \(c\). If either \(E_2\) or \(E_3\) has just two distinct values, the corresponding other-side additional member is impossible, so there is at most one additional member in total.

Otherwise write \(E_2=\{a,c,u\}\) and \(E_3=\{b,c,v\}\) with three distinct values each. At most one new member can be attached at \(a\), and it must have parts \((a,v,r)\); at most one can be attached at \(b\), and it must have parts \((b,u,s)\). The five fixed-sum equations imply
\[
u=a+b-c,\quad v=2a-c,\quad r=b-a+c,\quad s=a-b+c.\]
The two new members could intersect only if \(r=s\): every other possible shared value would give two shared values with one of the three base members. Yet \(r=s\) implies \(a=b\), a contradiction. Hence at most one additional member exists. Steps 2 and 3 prove \(|\mathcal F|\le4\) for every nontrivial family.

**4. Sharpness of four.** At \(n=8\) the four partitions displayed in the theorem are distinct, pairwise intersecting, and have no common part. For every \(n\ge9\), the family
\[
\mathcal Q_n=\{(1,2,n-3),(1,3,n-4),(2,3,n-5),(1,4,n-5)\}
\]
consists of four distinct positive-part partitions. Its pairwise intersections follow successively from shared values \(1,2,3,n-5\), and it has no common value. The bound is sharp for every \(n\ge8\).

**5. Largest families.** A full star centered at a part \(j\ge1\) has exactly \(\lfloor(n-j)/2\rfloor\) members when \(n-j\ge2\): deleting one occurrence of \(j\) bijects its members with unordered pairs of positive integers summing to \(n-j\). The largest such stars have size \(\lfloor(n-1)/2\rfloor\). For \(n\ge11\), this size is at least five, while every nontrivial family has size at most four. Thus every maximum family is a largest full star. The centered-star formula shows that only \(j=1\) works for odd \(n\ge11\), and only \(j\in\{1,2\}\) for even \(n\ge12\).

For \(3\le n\le7\), direct listing of \(P_{n,3}\) gives maxima \(1,1,2,2,3\) respectively, agreeing with \(\lfloor(n-1)/2\rfloor\). The five partitions of \(8\) are \((1,1,6),(1,2,5),(1,3,4),(2,2,4),(2,3,3)\). The first is disjoint from each of the final two, while the other four pairwise intersect; this proves both the value four and the uniqueness of its largest family. At \(n=9,10\), the full \(1\)-star attains four, as does the nontrivial family \(\mathcal Q_n\). This completes the proof.

## Verification

Run `python3 verify.py` using only Python's standard library. It constructs all three-part partitions and exhaustively enumerates maximal intersecting subfamilies for \(3\le n\le20\), checking maxima, nontrivial maxima, and the complete maximum-star classification at those orders. It also checks the explicit nontrivial witnesses for \(8\le n\le100\). The obtained output ends with `VERIFY_OK`. These finite checks support the boundary cases; the infinite assertions follow from the preceding proof, not from extrapolation.

## Relationship to prior work

Borg's *Intersecting integer partitions* (2016), Problem 1.3 and Conjecture 1.6, asks for the largest intersecting subfamilies of \(P_{n,k}\). Remark 1.5 already gives the four-family exception at \((n,k)=(8,3)\); neither that exception nor its uniqueness is asserted here as newly discovered. Borg's Theorem 1.8 establishes a star optimum at sufficiently large \(n\) (for \(t=1,k=3\), the displayed criterion \(n\ge3k^5\)), without the present sharp constant-size nontrivial bound, exact threshold, or maximum-family classification for all \(n\). Person and Schweser's *Intersecting integer partitions: star bounds and counterexamples at every scale* (2026, arXiv:2610.01747v1) improves the large-\(k\) range and constructs additional counterexamples, while explicitly leaving the fixed-small-\(k\) case outside its asymptotic quantifiers. Its discussion of the \((8,3)\) exception is prior, not a novel contribution of this theorem. The present finite-length proof isolates the additive constraint that rules out a second extension of the base triangle.

## Limitations

The result treats only three-part partitions and intersection in at least one part; it does not imply the general Borg conjecture, which is false in other parameter ranges. The four-member nontrivial bound is sharp, but this note does not classify all four-member nontrivial families at every order. The enumeration through order \(20\) does not establish any infinite assertion independently of the proof. Scientific priority beyond the sources explicitly compared has not been independently audited.

## References

1. P. Borg, *Intersecting integer partitions*, Australasian Journal of Combinatorics 66(2) (2016), 265–275. https://ajc.maths.uq.edu.au/pdf/66/ajc_v66_p265.pdf
2. Y. Person and T. Schweser, *Intersecting integer partitions: star bounds and counterexamples at every scale*, arXiv:2610.01747v1 (first public version 2026-10-01). https://arxiv.org/html/2610.01747v1
3. P. Borg, *Strongly intersecting integer partitions*, Discrete Mathematics 336 (2014), 80–84. https://www.um.edu.mt/library/oar/handle/123456789/54963 (the stronger positional notion is distinct).
