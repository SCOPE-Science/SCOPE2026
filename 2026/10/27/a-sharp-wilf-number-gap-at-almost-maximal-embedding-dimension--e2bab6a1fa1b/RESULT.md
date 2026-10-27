# A sharp Wilf-number gap at almost-maximal embedding dimension

## Finding
Let \(S\subseteq\mathbb N_0\) be a numerical semigroup of multiplicity \(m\ge4\) and embedding dimension \(e=m-1\). Set its conductor \(c=\min\{t:t+\mathbb N_0\subseteq S\}\), its number of left elements \(N=|S\cap[0,c)|\), and its Wilf number \(W=eN-c\). Then
\[
W\ge m-3.
\]
The bound is sharp for every \(m\ge4\). Equality holds if and only if \(S\) belongs to one of the following two families:
\[
S=\{0,m,m+r\}\cup[2m,\infty)\quad\text{for }1\le r<m/2,
\]
or
\[
S=\{0,m,2m-1,2m\}\cup[3m-1,\infty).
\]
Intervals of integers here include all integers at or above their lower endpoints. In particular, the smallest possible Wilf number in this entire embedding-dimension stratum is exactly \(m-3\).

## Assumptions and scope
A numerical semigroup is a cofinite additively closed subset of the nonnegative integers containing zero. The multiplicity is its smallest positive element, and the embedding dimension is the cardinality of its unique minimal positive generating set. We consider only \(m\ge4\), \(e=m-1\), without any restriction on conductor or genus. The Apéry set relative to \(m\) is \(\operatorname{Ap}(S,m)=\{s\in S:s-m\notin S\}\). It has one representative of each residue modulo \(m\), hence exactly \(m\) members. Every minimal generator other than \(m\) belongs to the Apéry set, and every positive primitive Apéry element is a minimal generator.

## Proof
**Step 1: the one-defect Apéry structure.** Since \(e=m-1\), exactly \(m-2\) of the \(m-1\) positive members of \(\operatorname{Ap}(S,m)\) are primitive and exactly one, say \(w\), is not. Write \(w=x+y\) with \(x,y\in S\setminus\{0\}\). Neither summand can equal \(m\) or be outside \(\operatorname{Ap}(S,m)\), since in either case \(w-m\in S\), a contradiction. Thus \(x,y\) are positive Apéry members. They are necessarily primitive, because \(w\) is the unique nonprimitive positive Apéry member and \(x,y<w\). Put \(u=\min(x,y)\). We have \(u\ge m+1\) and \(2u\le w\). The largest Apéry member is \(c+m-1\), so
\[
2u\le c+m-1.
\]
In particular \(u<c\), since \(c\ge m\).

**Step 2: a density witness.** Let \(h\ge1\) be the number of positive-residue members in the progression \(u,u+m,u+2m,\ldots\) that are strictly below \(c\). Let \(q=\lceil c/m\rceil\), the number of multiples \(0,m,2m,\ldots\) below \(c\). The two progressions have different residues, so
\[
N\ge q+h.
\]
By definition \(u+hm\ge c\). Consequently \(2c-2hm\le2u\le c+m-1\), and hence
\[
c\le(2h+1)m-1,\qquad q\le2h+1.
\]

**Step 3: the sharp bound.** Since \(e=m-1\),
\[
W=(m-1)N-c\ge(m-1)(q+h)-c.
\]
If \(q\le2h\), use \(c\le qm\) to get
\[
W\ge (m-1)h-q\ge h(m-3).
\]
If \(q=2h+1\), the sharper inequality \(c\le qm-1\) gives
\[
W\ge(m-1)h-q+1=h(m-3).
\]
As \(h\ge1\) and \(m\ge4\), this proves \(W\ge m-3\).

**Step 4: all equality cases.** Equality forces \(h=1\), because the lower bound \(h(m-3)\) grows strictly with \(h\). Thus \(q\le3\); moreover \(q\ge2\), since \(w\ge2(m+1)\) gives \(c\ge m+3\). If \(q=2\), equality in the above inequalities forces \(N=3\) and \(c=2m\), hence the left elements are exactly \(0,m,m+r\) for some \(1\le r<m\). The corresponding semigroup has embedding dimension \(m-1\) exactly when \(2r<m\): among the elements \(2m+s\), \(1\le s<m\), exactly \(s=r\) and, when \(2r<m\), \(s=2r\), fail to be new minimal generators, in addition to the generators \(m\) and \(m+r\). If \(2r\ge m\), the second cancellation is absent, giving embedding dimension \(m\). This proves the first family.

If \(q=3\), equality forces \(N=4\) and \(c=3m-1\). Since \(h=1\), we have \(u+m\ge c\), so \(u\ge2m-1\); the inequality \(2u\le c+m-1=4m-2\) gives \(u\le2m-1\). Hence \(u=2m-1\). Exactly four left elements occur: \(0,m,2m-1,2m\), producing the second family. Conversely, this family has Apéry representatives \(w_{m-1}=2m-1\), \(w_{m-2}=4m-2=2(2m-1)\), and \(w_r=3m+r\) for \(1\le r\le m-3\). Only \(4m-2\) is nonprimitive, so \(e=m-1\); its \(N=4\) and \(c=3m-1\) give \(W=m-3\). Both families are additively closed, have multiplicity \(m\), and achieve equality. This completes the classification.

## Verification
The included standalone `verify.py` enumerates all Kunz coordinate vectors with coordinate cutoffs \((m,K)=(4,7),(5,6),(6,5),(7,5),(8,4),(9,4)\), checks the necessary and sufficient Kunz inequalities, computes embedding dimension via Apéry decomposability, conductor, left-element count and Wilf number exactly, and compares every equality case against the two proposed families. It tested 29,223 numerical semigroups, including 8,098 with \(e=m-1\), and found 21 equality cases, all classified as stated. The script returned `VERIFY_OK`. This bounded check is not a proof for all multiplicities or Kunz vectors; Steps 1–4 provide the infinite proof.

## Relationship to prior work
Wilf's conjecture asks for \(eN-c\ge0\). Sammartano (2011, arXiv:1111.1863) proved it when \(2e\ge m\), encompassing the present embedding-dimension stratum, and gave broader nonnegativity criteria; the present conclusion is an exact positive gap, with all equality cases. Moscariello and Sammartano (2014, arXiv:1408.5331) studied when equality \(eN=c\) can occur and posed a structural question; this theorem quantitatively separates the almost-maximal stratum from equality. The related finite multiplicity-five, embedding-dimension-three result recorded as a published 2026 research record is on a different stratum. Search results did not establish this particular bound or classification, but absence of a matching search result alone cannot certify novelty.

## Limitations
No claim is made for embedding dimensions other than \(e=m-1\) or for \(m<4\). The algorithmic verifier covers only stated finite coordinate boxes. Full text of potentially relevant newer work on Wilf-number decompositions (arXiv:2608.12531) was unavailable in this investigation; its accessible abstract does not resolve the present precise bound, and equivalent results in other literature remain a residual originality risk. Independent mathematical audit has not been performed.

## References
- A. Sammartano, *Numerical semigroups with large embedding dimension satisfy Wilf's conjecture*, arXiv:1111.1863 (first version 2011-11-08), https://arxiv.org/abs/1111.1863.
- A. Moscariello and A. Sammartano, *On a conjecture by Wilf about the Frobenius number*, arXiv:1408.5331 (first version 2014-08-22), https://arxiv.org/abs/1408.5331.
- M. F. Marashdeh, *An upper bound for the type of a numerical semigroup, and a reduction of Wilf's conjecture*, arXiv:2608.12531 (2026, abstract only inspected), https://arxiv.org/abs/2608.12531.
