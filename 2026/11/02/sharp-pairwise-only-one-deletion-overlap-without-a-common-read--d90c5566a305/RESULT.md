# Sharp pairwise-only one-deletion overlap without a common read

## Finding

For an integer \(n\geq 3\) and a binary word \(w\in\{0,1\}^n\), let \(D(w)\) be the **set** (not multiset) of length-\(n-1\) words obtained by deleting exactly one coordinate of \(w\). Define \(H(n)\) as the maximum cardinality of a family \(\mathcal C\subseteq\{0,1\}^n\) for which every two distinct members have intersecting one-deletion sets, but no single read is compatible with the entire family:

\[
\forall x\ne y\in\mathcal C,\quad D(x)\cap D(y)\ne\varnothing,\qquad
\bigcap_{x\in\mathcal C}D(x)=\varnothing.
\]

**Theorem.** For every \(n\ge3\), the exact sharp value is

\[
\boxed{H(n)=n+1.}
\]

The extremal families are explicit and deterministic. Thus a maximum-cardinality clique in the binary one-deletion confusability graph need not be the insertion neighborhood of a single read: even the largest pairwise-consistent family may be globally inconsistent.

## Assumptions and scope

Words are ordinary finite *linear* strings with labeled positions and binary alphabet; there are no cyclic identifications. One deletion means removing exactly one position, and repeated reads from equal symbols count only once. The empty intersection is over the sets of **one-deletion descendants**, not over insertions or longer subsequences. The theorem holds for every integer \(n\ge3\) and makes no assertion about classification of all extremizers. The restriction \(n\ge3\) is essential to the non-Helly phenomenon; no pairwise-intersecting family with empty total intersection occurs at length \(1\) or \(2\).

For a word \(u\) of length \(m\), write \(I(u)=\{w\in\{0,1\}^{m+1}:u\in D(w)\}\). An elementary run count gives \(|I(u)|=m+2\) because inserting a zero gives \(\#_1(u)+1\) distinct strings and inserting a one gives \(\#_0(u)+1\) distinct strings.

## Proof

### 1. The universal upper bound

Fix a length-\(n-1\) read \(r\). To each length-\(n\) binary word assign its Varshamov–Tenengolts checksum \(s(w)=\sum_{i=1}^n i w_i\pmod{n+1}\).

Represent an insertion into \(r\) by its position \(p\in\{1,\ldots,n\}\) and inserted symbol \(a\in\{0,1\}\); an insertion before position \(p\) shifts the original suffix to the right. If \(p<q\) and the inserted symbols are \(a,b\), the *integer* checksum difference is

\[
\Delta=p a-q b+\sum_{i=p}^{q-1}r_i.
\]

If \(a=b=0\), the difference is the number of ones in the intervening substring; if \(a=b=1\), it is minus the number of zeros. In these equal-symbol cases, distinct resulting strings require a nonzero difference of absolute value at most \(n-1\) (a zero difference means insertion at two places within one constant run and hence the same result). If \((a,b)=(1,0)\), then \(1\le\Delta\le n\); if \((a,b)=(0,1)\), then \(-n\le\Delta\le-1\). If \(p=q\), distinct insertions of different symbols have \(\Delta=\pm p\) with \(1\le p\le n\). Consequently all **distinct** words in \(I(r)\) have distinct residues modulo \(n+1\).

If \(\mathcal C\) is pairwise one-deletion confusable, its words form a clique in the confusability graph, so they have pairwise distinct checksums. There are only \(n+1\) checksum values. Hence \(|\mathcal C|\le n+1\).

### 2. A two-common-supersequence lemma

**Lemma.** For distinct binary words \(u,v\) of a common length \(m\ge1\), one has \(|I(u)\cap I(v)|\le2\).

**Proof.** Take any common length-\(m+1\) supersequence \(z\). Let \(p\) be the coordinate deleted to obtain \(u\), and \(q\) the one deleted to obtain \(v\) (zero-indexed). As \(u\ne v\), \(p\ne q\). Let \(h\) be the first position at which \(u\) and \(v\) disagree. When \(p<q\), the words agree before \(p\), and from \(p\) up to \(h\) the symbols of \(z\) are all equal to \(v_h\); hence \(z\) is **uniquely** obtained from \(u\) by inserting \(v_h\) directly before coordinate \(h\). When \(p>q\), the symmetric argument uniquely determines \(z\) by inserting \(u_h\) before coordinate \(h\) of \(v\). There is at most one candidate for each ordering, proving the lemma. \(\square\)

### 3. Sharp examples at lengths three and four

At length \(3\), use \(\mathcal C_3=\{001,010,100,101\}\). At length \(4\), use \(\mathcal C_4=\{0001,0010,0100,1000,1001\}\). Direct deletion shows all pairs have a common descendant, but each whole-family intersection is empty. Both sizes are \(n+1\).

### 4. An infinite construction

At length \(5\), set

\[
u_5=0010,\qquad v_5=01001,\qquad x_5=00110,\qquad t_5=0.
\]

For \(n\ge5\), define recursively

\[
u_{n+1}=u_nt_n,\quad v_{n+1}=v_nt_n,\quad x_{n+1}=x_nt_n,\quad t_{n+1}=1-t_n,
\]

where juxtaposition denotes concatenation of a bit and a word, while \(1-t_n\) denotes the complementary bit. Form

\[
\mathcal C_n=\bigl(I(u_n)\setminus\{x_n\}\bigr)\cup\{v_n\}.
\]

At the base, \(x_5\in I(u_5)\), \(v_5\notin I(u_5)\), and the five words of \(I(u_5)\setminus\{x_5\}\) are

\[
00010,\ 00100,\ 00101,\ 01010,\ 10010.
\]

They all delete to \(u_5\). The extra word \(v_5=01001\) shares, respectively, the reads \(0001,0100,0001,0100,1001\) with these five words; it does not delete to \(u_5\). Thus \(\mathcal C_5\) is pairwise confusable. Since five different members of its star all have the read \(u_5\), and by the lemma at most two distinct length-four reads can have two prescribed distinct length-five supersequences, their common deletion set must be \(\{u_5\}\); adjoining \(v_5\) makes the intersection empty. Its cardinality is \(6\).

For the induction, if \(t\) is one bit and \(u\) a word, the exact identity

\[
I(ut)=\{wt:w\in I(u)\}\cup\{ut(1-t)\}
\]

holds as a disjoint union. Moreover, the recursion preserves the invariant

\[
v_n=(u_n\text{ with its first bit removed})\,t_n(1-t_n).
\]

Thus the new word \(z_n=u_nt_n(1-t_n)\) (the extra member of \(I(u_{n+1})\)) has the one-deletion descendant \(v_n\) after its first symbol is removed, while \(v_{n+1}=v_nt_n\) has the same descendant by deleting its final symbol. Every other member of \(\mathcal C_{n+1}\) is an old member of \(\mathcal C_n\) with bit \(t_n\) appended. Such appended words inherit their pairwise common-read relations; each also shares the deletion read \(u_nt_n\) with \(z_n\). Hence the new family is pairwise confusable.

The induction keeps \(x_n\in I(u_n)\) and \(v_n\notin I(u_n)\): the first follows by appending the same bit to a one-insertion, while the second follows from the disjoint-union identity, since \(v_nt_n\) cannot equal the extra word ending in \(1-t_n\). Consequently \(|\mathcal C_n|=(n+1)-1+1=n+1\). Because \(n\ge5\), any three distinct members of the star \(I(u_n)\setminus\{x_n\}\) have only \(u_n\) as a common deletion read, by the lemma. The exceptional word \(v_n\notin I(u_n)\) removes that final common read. Therefore the family has empty total intersection for every \(n\ge5\).

Combining the induction with the two small bases and the checksum upper bound completes the proof. \(\square\)

## Verification

The included standalone `verify.py` uses only Python's standard library and literal deletion/insertion operations. It checks the sharp construction at every length \(3\le n\le250\), checks VT-syndrome distinctness for all binary words through length \(13\), and exhaustively checks the two-common-supersequence bound through read length \(8\). Running `python3 verify.py` produces `VERIFY_OK`. Finite checks corroborate but are not substitutes for the preceding infinite proofs.

## Relationship to prior work

The checksum coloring and the definition of single-deletion confusability are classical; see Sloane's survey [1]. Nguyen, Cai and Siegel [2] study more efficient binary and nonbinary single-deletion/burst-deletion code constructions; their 2023 work is a starting point for questions about ambiguity beyond uniquely decodable codes. Wang, Nguyen, Chee and Vu [3] enumerate triangles in a graph defined on permutations; their vertices have distinct symbols and the result does not transfer to the binary repeated-symbol setting by substitution. The present assertion concerns the exact maximum size of a **pairwise-intersecting family whose entire one-deletion intersection is empty**, which is neither an independent-set size nor a triangle count. The upper bound alone is classical, while the sharp non-Helly construction is the asserted additional result.

## Limitations

No claim is made that all maximum cliques are classified, that the exact number of non-Helly extremizers is known, or that similar sharpness holds for larger alphabets or multiple deletions. The source comparisons cannot exclude an equivalent unpublished or unindexed formulation in deletion-hypergraph or sequence reconstruction literature. An independent audit has not been conducted.

## References

1. N. J. A. Sloane, *On Single-Deletion-Correcting Codes*, arXiv:math/0207197, first submitted July 22, 2002. https://arxiv.org/abs/math/0207197
2. T. T. Nguyen, K. Cai, P. H. Siegel, *A New Version of q-ary Varshamov-Tenengolts Codes with More Efficient Encoders: The Differential VT Codes and The Differential Shifted VT Codes*, arXiv:2311.04578, first submitted November 8, 2023. https://arxiv.org/abs/2311.04578
3. S. Wang, T. Nguyen, Y. M. Chee, K. Vu, *Permutation and Multi-permutation Codes Correcting Multiple Deletions*, arXiv:2406.16656, first submitted June 24, 2024. https://arxiv.org/abs/2406.16656
