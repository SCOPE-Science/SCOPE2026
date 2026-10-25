# Linear induced saturation for a five-point layered poset

## Finding

Let \(P\) have five elements \(a,b,x_1,x_2,x_3\), with \(a\parallel b\), \(a<x_1\), \(b<x_1\), and \(x_1<x_2<x_3\). Thus its successive layer sizes are \((2,1,1,1)\). For every integer \(n\ge4\),

\[
 n+2\le \operatorname{sat}^*(n,P)\le 2n+2,
\]

so \(\operatorname{sat}^*(n,P)=\Theta(n)\). Here \(\operatorname{sat}^*(n,P)\) is the minimum size of an induced-\(P\)-saturated family in the Boolean lattice \(2^{[n]}\).

## Assumptions and scope

All posets are finite. A family \(\mathcal F\subseteq2^{[n]}\) is induced-\(P\)-saturated if it contains no induced copy of \(P\), but adding any missing subset of \([n]\) creates an induced copy of \(P\). The claim concerns this one five-element layered poset and all \(n\ge4\); it does not determine the exact value or the best linear coefficient.

## Proof

For \(n\ge4\), define

\[
\mathcal F_n=\{\varnothing,[n]\}\cup\bigl\{\{i\}:i\in[n]\bigr\}\cup\bigl\{[n]\setminus\{i\}:i\in[n]\bigr\}.
\]

The displayed families are pairwise disjoint for \(n\ge4\), hence \(|\mathcal F_n|=2n+2\).

First, \(\mathcal F_n\) is induced-\(P\)-free. In any induced copy of \(P\), two incomparable sets must lie strictly below the first member of a chain of three strict inclusions. In \(\mathcal F_n\), every incomparable pair is of one of these forms: two distinct singletons; a singleton and the co-singleton omitting its element; or two distinct co-singletons. In the first case, every common strict upper member of \(\mathcal F_n\) is a co-singleton or \([n]\); a co-singleton has only \([n]\) strictly above it in \(\mathcal F_n\), and \([n]\) has no strict upper member. In the other two cases, the union of the incomparable pair is \([n]\), so their only common strict upper member in \(\mathcal F_n\) is \([n]\). Thus no such pair can sit below a chain of three strict inclusions, and \(\mathcal F_n\) contains no induced copy of \(P\).

Next, let \(S\subseteq[n]\) be missing from \(\mathcal F_n\). Then \(2\le |S|\le n-2\). Choose distinct \(i,j\in S\) and \(k\in[n]\setminus S\). The five sets

\[
\{i\},\quad \{j\},\quad S,\quad [n]\setminus\{k\},\quad [n]
\]

induce \(P\): the two singletons are incomparable, both are strictly contained in \(S\), and

\[
S\subsetneq[n]\setminus\{k\}\subsetneq[n].
\]

All five sets are distinct because \(2\le|S|\le n-2\). Therefore adding any missing \(S\) creates an induced copy of \(P\), proving \(\mathcal F_n\) is induced-\(P\)-saturated and giving \(\operatorname{sat}^*(n,P)\le2n+2\).

For the lower bound, \(P\) has legs: \(a,b\) are incomparable and lie below \(x_1\), and each other element \(x_2,x_3\) lies above \(x_1\). The published legs theorem states that for every poset with legs and every \(n>3\), \(\operatorname{sat}^*(n,P)>n+1\). Hence \(\operatorname{sat}^*(n,P)\ge n+2\) for \(n\ge4\). Combining the bounds proves the claim.

## Verification

The upper bound is an explicit all-\(n\) construction. The proof checks both defining conditions of induced saturation: absence of \(P\) in \(\mathcal F_n\), and construction of a copy containing every missing set. The lower bound is a direct application of the cited legs theorem, with its hypothesis verified for \(P\). No finite computation is used as an infinite proof. The exact value of \(\operatorname{sat}^*(n,P)\) is not claimed.

## Relationship to prior work

Ivan and Jaffe formulate a conjecture that every complete layered poset with at least one layer of size greater than one has linear induced saturation. Their linear upper-bound theorem covers layered posets with no two consecutive singleton layers, and their conclusion explicitly identifies consecutive singleton layers as a remaining obstacle. The layer pattern \((2,1,1,1)\) is outside that theorem, while the construction above supplies a linear upper bound for this particular five-element case. Freschi, Piga, Sharifzadeh, and Treglown supply the matching-order lower bound through their general theorem for posets with legs. A later classification establishes the bounded-linear dichotomy only for posets with at most four elements, so it does not cover this five-element poset.

## Limitations

The bounds establish linear growth but do not determine the exact saturation number or optimal leading constant. The lower bound depends on a published theorem rather than a new proof of that theorem. Literature searches cannot certify absolute priority; the claim is limited to the specific layer pattern \((2,1,1,1)\).

## References

1. M.-R. Ivan and S. Jaffe, *Gluing Posets and the Dichotomy of Poset Saturation Numbers*, arXiv:2503.12223v1 (first public posting 2025-03-15), especially Theorem 10 and Conjecture 15.
2. A. Freschi, S. Piga, M. Sharifzadeh, and A. Treglown, *The Induced Saturation Problem for Posets*, arXiv:2207.03974v4, Theorem 1.5 (posets with legs).
3. M.-R. Ivan and S. Jaffe, *The Bounded-Linear Dichotomy Holds for all 4 Point Posets*, arXiv:2610.06527v1 (2026-10-05).
