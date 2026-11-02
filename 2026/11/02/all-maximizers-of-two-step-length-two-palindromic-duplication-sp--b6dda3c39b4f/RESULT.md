# All maximizers of two-step length-two palindromic-duplication spheres

## Finding

**Theorem.** Fix any labeled alphabet \(\Sigma\) with \(|\Sigma|=q\ge 2\) and any source length \(n\ge 2\). Let \(D_2^{\mathrm{pal}}(x)\) be the set of *distinct* words obtained from \(x\in\Sigma^n\) after exactly two sequential length-two palindromic duplications, where the second duplication may overlap or copy symbols inserted by the first. Then

\[
|D_2^{\mathrm{pal}}(x)|\le S_n:=\frac{n^2+5n-8}{2},
\]

with equality **if and only if every pair of adjacent symbols of \(x\) is unequal**. Thus the number of labeled source words attaining the maximum is exactly

\[
q(q-1)^{n-1}.
\]

For any involution \(\iota:\Sigma\to\Sigma\), the analogous exact-two sphere under length-two *reverse-complement* duplication has the same maximum. Its maximizers are exactly the sources satisfying \(x_{j+1}\ne\iota(x_j)\) for each \(0\le j<n-1\), again numbering \(q(q-1)^{n-1}\). For the usual binary complement, the only reverse-complement maximizers are the two constant words.

The maximum-size formula and attainment by alternating two-symbol palindromic sources are prior results (Zabokritskiy, 2026). The contribution is the **if-and-only-if classification of all maximizers**, especially the additional non-alternating maximizing sources over larger alphabets, with their exact enumeration and transferred reverse-complement characterization.

## Assumptions and scope

Coordinates start at zero. For a word \(w\) of length \(m\ge2\) and \(0\le i\le m-2\), define the length-two PAL operation

\[
P_i(w)=w_0\cdots w_{i+1}\,w_{i+1}w_i\,w_{i+2}\cdots w_{m-1}.
\]

Thus \(D_2^{\mathrm{pal}}(x)=\{P_j(P_i(x)):0\le i\le n-2,\ 0\le j\le n\}\). Equal *outputs* count once, even when multiple histories produce them. For an involution \(\iota\), the corresponding RC operation inserts \(\iota(w_{i+1})\iota(w_i)\) instead. No algebraic structure on the alphabet is assumed. All inequalities and classifications include their length-two boundary cases.

## Proof

**1. Structural shape bound.** Label the \(n-1\) original adjacent-pair occurrences by \(E_0,\ldots,E_{n-2}\), retaining a label when its pair survives a duplication. After duplication of \(E_i\), original occurrences at starts \(j\le i\) survive at the same starts, and original occurrences at starts \(j\ge i+2\) survive at shifted starts \(j+2\). The originally adjacent occurrence \(E_{i+1}\) is destroyed. The newly created adjacent-pair occurrences have starts \(i+1\), \(i+2\), and (if \(i\le n-3\)) \(i+3\); label these \(L_i,M_i,R_i\), respectively.

Every two-step history consequently has one of these *canonical shapes*:

* a multiset \(\{E_a,E_b\}\) with \(0\le a\le b\le n-2\), whose output is obtained by duplicating the larger original start first, then the smaller (twice at the same original start when \(a=b\));
* a parent-child shape \((E_a,L_a)\) or \((E_a,M_a)\) for \(0\le a\le n-2\);
* a parent-child shape \((E_a,R_a)\) for \(0\le a\le n-3\).

Indeed, the possible second-operation starts after first duplicating \(E_i\) are exactly \(j\le i\), \(j=i+1,i+2\), \(j=i+3\) when legal, and \(j\ge i+4\). They correspond respectively to an original occurrence, one of the three newly created occurrences, or a shifted original occurrence. Two disjoint original occurrences commute, and for the pair \(E_a,E_{a+1}\) the larger one must be duplicated first. The displayed rules therefore give an output for every shape and exhaust all histories. Their total number is

\[
\binom n2+2(n-1)+(n-2)=S_n.
\]

This proves the universal upper bound, without assuming a special source word.

**2. Necessity of unequal neighbors.** Suppose \(x_a=x_{a+1}=u\). The different shapes \(\{E_a,E_a\}\) and \((E_a,L_a)\) both replace the same original \(uu\) by \(uuuuuu\), leaving all other symbols unchanged. Their outputs coincide. Hence the shape bound is strict. In particular every maximizing word has unequal neighbors.

**3. Sufficiency by separating all shapes.** Now suppose \(x_j\ne x_{j+1}\) throughout. In the canonical output for any shape whose least original start is \(a\), the earliest pair of equal consecutive symbols occurs *exactly at edge position* \(a+1\): the symbols before that edge agree with the original source and hence are pairwise different, while the first copied symbol repeats \(x_{a+1}\). Thus outputs of shapes with different least original starts cannot coincide.

Fix a least start \(a\), and abbreviate \(u=x_a\), \(v=x_{a+1}\), and, when present, \(z=x_{a+2}\), \(w=x_{a+3}\). In particular \(u\ne v\), \(v\ne z\), and \(z\ne w\) whenever the relevant symbols exist. Each canonical output has the unchanged prefix preceding \(x_a\). Its displayed initial segment starting at position \(a\) is:

\[
\begin{array}{c|l}
\text{shape}&\text{initial segment}\hline
A=\{E_a,E_a\}&u\,v\,v\,u\,v\,u\quad\text{(then original suffix)}\\
L=(E_a,L_a)&u\,v\,v\,v\,v\,u\quad\text{(then original suffix)}\\
M=(E_a,M_a)&u\,v\,v\,u\,u\,v\quad\text{(then original suffix)}\\
R=(E_a,R_a)&u\,v\,v\,u\,z\,z\,u\quad\text{(then original suffix)}\\
B_{a+1}=\{E_a,E_{a+1}\}&u\,v\,v\,u\,z\,z\,v\quad\text{(then original suffix)}\\
B_b=\{E_a,E_b\},\ b\ge a+2&u\,v\,v\,u\,z\,w\quad\text{(then continuation with the second original-pair duplication)}.
\end{array}
\]

Rows requiring a nonexistent symbol or original pair are simply absent. In the last row, the symbol \(w\) is present because \(b\le n-2\) implies \(a+3<n\). The local words result immediately from the definition of \(P_i\).

These segments distinguish the families as follows.

* The \(L\) row has \(v\) at offset three, whereas every other row has \(u\); hence \(L\) is unique.
* The \(A\) row has \(v\) at offset four, whereas \(M\) has \(u\), and each \(B_b\) and \(R\) has \(z\). These are all different from \(v\) by the stated adjacent inequalities. Thus \(A\) is unique.
* For \(M\) versus \(R\) or \(B_{a+1}\), their offset-four symbols are \(u\) and \(z\). If those are equal, their offset-five symbols are \(v\) and \(z\), which are unequal. For \(M\) versus \(B_b\) with \(b\ge a+2\), offset four separates them unless \(u=z\). In that remaining case, the \(B_b\) output has adjacent equalities at three **distinct** edges: offsets one and three and the later duplicated original-pair join at absolute edge \(b+3\ge a+5\). The \(M\) output has equalities at exactly offsets one and three, because its last copied \(v\) is followed either by the unequal original \(z\) or by the end of the word, and all later original adjacencies are unequal. So \(M\) cannot coincide with any \(B_b\).
* The \(R\) and \(B_{a+1}\) outputs differ at offset six, where their symbols are \(u\) and \(v\). For \(b\ge a+2\), the \(R\) and \(B_b\) outputs differ at offset five, which contains \(z\) in \(R\) and \(w\) in \(B_b\). Thus \(R\) is separate from every \(B_b\).
* Finally, different \(B_b\) rows are distinct. The \(B_{a+1}\) output differs from every \(B_b\) with \(b\ge a+2\) at offset five (\(z\) versus \(w\)). For \(a+2\le b<c\), the two outputs agree through the original symbol \(x_{b+1}\) but at the next coordinate the \(B_b\) output repeats \(x_{b+1}\) as the first inserted symbol, whereas \(B_c\) continues with \(x_{b+2}\). Those two symbols are unequal.

All shapes with the same least original start are therefore pairwise distinct. Combining with separation of different least starts, the shape-to-output map is injective. The upper bound is attained for every source with unequal adjacent symbols. Together with step 2 this establishes the PAL classification. Its labeled enumeration follows by choosing \(x_0\) in \(q\) ways and each succeeding symbol in \(q-1\) ways.

**4. Reverse-complement transfer.** Let \(\iota\) be any involution and let \(A_m(y)_j=\iota^j(y_j)\). The even-length conjugacy identity of Zabokritskiy (2026, Theorem 4.1) states that \(A_{m+2}(P_i^{\mathrm{rc}}(y))=P_i^{\mathrm{pal}}(A_m(y))\). It applies sequentially to both steps and preserves sphere size because each \(A_m\) is bijective. Thus \(x\) maximizes its RC sphere precisely when consecutive symbols of \(A_n(x)\) are unequal, equivalent to \(x_{j+1}\ne\iota(x_j)\) for each \(j\). There are exactly \(q-1\) choices at every next position. In the binary fixed-point-free case, avoiding the complement of the preceding bit means repeating it, leaving precisely two constant sources. This completes the proof.

## Verification

The all-length argument is the explicit shape-separation proof above, not an inference from finite testing. Two standalone Python programs are supplied. `verify_direct.py` enumerates every exact-two history directly and checks the characterization for all binary inputs through length ten, all ternary inputs through length eight, all quaternary inputs through length six, and all quinary inputs through length four. It independently tests reverse-complement duplications using fixed-point-free complements for binary lengths through ten and quaternary lengths through six.

`verify_shapes.py` constructs every canonical shape independently, tests distinctness against the adjacent-inequality condition for all binary inputs through length twelve, ternary inputs through length nine, and quaternary inputs through length seven, and checks 600 additional deterministic random proper sources at longer lengths. Both scripts use only the Python standard library; the included output files contain their actual printed results.

## Relationship to prior work

Zabokritskiy, *Coding for Multiple Reverse-Complement and Palindromic Duplications* (arXiv:2609.00779, first posted 2026-09-01), establishes the maximum exact-two sphere size for every even duplication length and constructs maximizing sources alternating between two distinct letters (Theorem 5.1). Its length-two edge-tree normal form (Lemma 5.7) provides the general shape count; its even-length conjugacy (Theorem 4.1) handles reverse complements. Those ingredients provide the starting upper bound, but **do not assert that every proper adjacent-unequal source attains it or classify all maximizers**. The present proof supplies the missing global injectivity criterion and strictness in the presence of adjacent equalities. For alphabets with at least three symbols, most of the \(q(q-1)^{n-1}\) maximizers are not alternating between a fixed pair of symbols.

Lenz, Wachter-Zeh, and Yaakobi, *Duplication-Correcting Codes* (arXiv:1712.09345, first posted 2017-12-24), calculate length-two **single-error** palindromic sphere sizes, not the present two-step equality cases. Sun and Ge, *On the Palindromic/Reverse-Complement Duplication Correcting Codes* (arXiv:2602.01151, first posted 2026-02-01), study correcting code constructions and bounds rather than this full maximizer classification. These differences are in quantifiers and implications, not merely terminology.

## Limitations

The theorem classifies **maximum source descendant-sphere sizes**, not maximum sizes of error-correcting codebooks or their reconstruction algorithms. It applies to exactly two unrestricted sequential duplications, both of block length two. It does not classify equality for three or more errors or for longer duplicated blocks. The proof verifies correctness mathematically, but independent external validation and publication-priority certification have not been performed.

## References

1. A. L. Zabokritskiy, *Coding for Multiple Reverse-Complement and Palindromic Duplications*, arXiv:2609.00779, version first posted 2026-09-01, https://arxiv.org/abs/2609.00779. Especially Theorems 4.1 and 5.1 and Lemma 5.7.
2. A. Lenz, A. Wachter-Zeh, and E. Yaakobi, *Duplication-Correcting Codes*, arXiv:1712.09345, first posted 2017-12-24, https://arxiv.org/abs/1712.09345. Especially Appendix A, Lemma 12.
3. Y. Sun and G. Ge, *On the Palindromic/Reverse-Complement Duplication Correcting Codes*, arXiv:2602.01151, first posted 2026-02-01, https://arxiv.org/abs/2602.01151.
