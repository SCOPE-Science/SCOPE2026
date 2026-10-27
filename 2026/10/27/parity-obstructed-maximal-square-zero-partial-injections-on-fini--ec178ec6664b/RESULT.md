# Parity-obstructed maximal square-zero partial injections on finite fences

## Finding

Let \(n\ge4\), and let \(T_n\) be the inverse monoid of order-preserving, up-fence-preserving, inverse up-fence-preserving, and parity-preserving partial injections on \([n]=\{1,\ldots,n\}\). Here \(0\) is the empty partial injection. Define
\[
\rho_n=\max\{ |\operatorname{dom} f|:f\in T_n,\ f^2=0\}.
\]
Then
\[
\boxed{\rho_n=\lfloor n/2\rfloor-\mathbf 1_{\{n\equiv2\pmod4\}}.}
\]
Each integer \(0\le r\le\rho_n\) occurs as the domain size of a square-zero element. Moreover, for \(n=4k\) with \(k\ge1\), **exactly \(2^k\) elements attain rank \(2k\)**. Their domains and images partition \([4k]\). Encoding domain by 0 and image by 1, the complete list of words is
\[
0^{2a_1}1^{2a_1}\cdots0^{2a_j}1^{2a_j},
\quad\text{or}\quad
1^{2a_1}0^{2a_1}\cdots1^{2a_j}0^{2a_j},
\]
where \(j\ge1\), all \(a_i\) are positive integers, and \(a_1+\cdots+a_j=k\). Each word specifies a unique map by matching the increasing domain enumeration with the increasing image enumeration.

## Assumptions and scope

The up-fence has strict comparabilities \(i\prec i+1\) for odd \(i\), and \(i+1\prec i\) for even \(i\); there are no other distinct comparable pairs. In \(T_n\), a partial map is injective, strictly increasing as a map of the natural chain, preserves this fence relation in both directions on its domain and image, and maps each integer to an integer of the same parity. Rank means \(|\operatorname{dom} f|=|\operatorname{im}f|\), **not** the minimal number of monoid generators. The result holds for all integers \(n\ge4\); no asymptotic or complete count at every nonmaximal rank is asserted.

## Proof

**1. Square-zero criterion.** A partial injection \(f:D\to E\) has \(f^2=0\) if and only if \(D\cap E=\varnothing\). If \(E\cap D\ne\varnothing\), choose \(x\in D\) mapping to an element of \(D\); then \(f^2(x)\) is defined. Conversely disjointness makes every second evaluation undefined. Consequently \(2|D|\le n\).

**2. Parity obstruction.** Let \(n=4k+2\). If \(|D|=2k+1=n/2\), disjointness forces \(D\sqcup E=[n]\). Parity preservation gives \(|D\cap O|=|E\cap O|\), where \(O\) is the set of odd vertices. But \(|O|=2k+1\) is odd and must equal twice an integer, impossible. Thus \(|D|\le2k=n/2-1\).

**3. Sharp constructions in every residue class.** An even integer translation on a finite interval preserves chain order, fence comparabilities in both directions, and parity. For \(n=4k\), put \(D=[1,2k]\) and \(f(i)=i+2k\). For \(n=4k+2\), put \(D=[1,2k]\) and \(f(i)=i+2k+2\), so \(E=[2k+3,4k+2]\). For odd \(n=2m+1\), let \(D=[1,m]\) and \(f(i)=i+s\), where \(s=m\) if \(m\) is even and \(s=m+1\) otherwise. In each case \(s\) is even, \(D\cap(D+s)=\varnothing\), and \(D+s\subseteq[n]\). Thus every bound is attained. Restricting such a map to any subset of its domain preserves all defining properties and square-zero, realizing each lower rank.

**4. Enumeration of full-rank extremizers when \(n=4k\).** For \(f^2=0\) of rank \(2k\), its domain \(D\) and image \(E\) partition \([4k]\). There is precisely one chain-order-preserving bijection \(D\to E\). A fundamental element characterization for \(T_n\) [1, Proposition 1] says that the successive domain gaps are 1 exactly when the corresponding image gaps are 1, and corresponding points have the same parity. Hence the ordered lists of lengths of maximal consecutive runs in \(D\) and \(E\) coincide. In the complementary 0/1 word, runs alternate. Equality of the run counts forces the first and final colors to differ, so the word has form \(0^{b_1}1^{b_1}\cdots0^{b_j}1^{b_j}\) or its color swap.

The first matched points of each successive pair of runs differ by \(b_i\), because the preceding run-pairs contain \(2(b_1+\cdots+b_{i-1})\) positions. Parity preservation therefore forces every \(b_i\) to be even. Conversely, any paired word with even run lengths yields a strictly increasing domain-to-image bijection that matches equal-length runs and pointwise parities, so it belongs to \(T_{4k}\) by the characterization (or by checking both fence relations directly), and its square is empty. Writing \(b_i=2a_i\), the \(a_i\) form an ordered composition of \(k\). There are \(2^{k-1}\) such compositions and two choices for the starting color, producing exactly \(2^k\) extremizers. \(\square\)

## Verification

The standalone file `verify.py` checks the theorem independently from the cited successive-gap criterion. It enumerates every disjoint source/image pair, matches them monotonically, and tests parity plus both directed fence-relation implications directly. It compares complete rank histograms for all \(2\le n\le12\) against explicitly stored results, verifies all attainable ranks and the maximal-rank formula, and compares the sets of extremizer words against the paired-composition classification for \(n=4,8,12\). A separate complementary-domain enumeration tests the extremizers for \(n=16\). Run `python3 verify.py` (standard library only); see `verification_output.txt` for actual output. The \(n=2,3\) tests are ancillary and do not enlarge the stated theorem scope. These are finite checks; the four-step argument above establishes the theorem for every \(n\ge4\).

## Relationship to prior work

Sareeto and Koppitz [1, Proposition 1] provide the necessary and sufficient description of the monoid's elements and establish its **semigroup generating rank**, not a square-zero maximum or top-rank count. Their later papers [2,3] establish a monoid presentation and describe ideals/maximal subsemigroups. Dimitrova and Koppitz [4] study the larger fence-preserving inverse semigroup without this particular joint order/parity restriction. The present claim uses [1]'s element characterization as an explicitly credited premise, then proves the modular obstruction and exact extremizer classification. The same natural invariant in cycle partial-isometry monoids or multipartite partial-isometry monoids does not imply this statement because those monoids require metric preservation rather than the simultaneous chain, fence, and parity constraints.

## Limitations

Only the largest square-zero rank, its gap-free support, and the complete extremizer classification when \(n\equiv0\pmod4\) are proved. The counts of extremizers in other residue classes and the full square-zero rank polynomial are not determined here. The equivalence of partial injections to ordered source/image pairs is standard and the cited element criterion is prior art; no new classification of all monoid elements is claimed. Although targeted comparisons found no equivalent square-zero extremizer result, broader partial-injection enumerations could contain equivalent implicit formulas; independent validation and a comprehensive bibliographic priority determination are not provided.

## References

[1] A. Sareeto and J. Koppitz, *The rank of the semigroup of order-, fence-, and parity-preserving partial injections on a finite set*, arXiv:2208.03202 (initial public submission 2022-08-05). https://arxiv.org/abs/2208.03202

[2] A. Sareeto and J. Koppitz, *A presentation for a submonoid of the symmetric inverse monoid*, arXiv:2310.15809 (2023). https://arxiv.org/abs/2310.15809

[3] A. Sareeto and J. Koppitz, *The maximal subsemigroups of the ideals on a monoid of partial injections*, arXiv:2403.06957 (2024). https://arxiv.org/abs/2403.06957

[4] I. Dimitrova and J. Koppitz, *On the semigroup of all partial fence-preserving injections on a finite set*, arXiv:2111.14432 (2021). https://arxiv.org/abs/2111.14432
