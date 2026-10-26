# Exact block-palindrome widths and an odd-geometric limit law for Dyck words

## Finding

Let \(\mathcal D_n\) be the set of Dyck words of semilength \(n\): binary words with \(n\) zeros and \(n\) ones and with at least as many zeros as ones in every prefix. Put \(\mathcal D_0=\{\varepsilon\}\). A nonempty **border** of a word is an equal proper prefix and suffix. A word is **unbordered** if it has no border. Let \(U_n\) count unbordered members of \(\mathcal D_n\), and put
\[
C(z)=\sum_{n\ge0}\frac{1}{n+1}\binom{2n}{n}z^n=\frac{1-\sqrt{1-4z}}{2z},\qquad
U(z)=\sum_{n\ge1}U_nz^n.
\]

The **largest block-palindrome width** \(L(w)\) is the maximum number of nonempty pieces in a factorization into identical paired blocks read from the two ends and at most one unpaired central block. For the empty word set \(L(\varepsilon)=0\). For every \(n\ge0\) and \(r\ge0\), write \(B_{n,r}=|\{w\in\mathcal D_n:L(w)=r\}|\).

The following two formal power-series identities determine **every** \(U_n\) and \(B_{n,r}\):
\[
\boxed{U(z)=C(z)-1-C(z)U(z^2)}
\]
\[
\boxed{\sum_{n,r\ge0}B_{n,r}z^nt^r
=\frac{1+tU(z)}{1-t^2U(z^2)}.}
\]
In particular, \(U_1,\ldots,U_{11}\) are
\[
1,1,4,11,36,112,378,1265,4360,15120,53236.
\]

There is also an exact limiting width law. Define the absolutely convergent constant
\[
\alpha=U(1/16)=0.067593450955121331489218327150\ldots.
\]
For a uniformly chosen word \(W_n\in\mathcal D_n\), as \(n\to\infty\),
\[
\boxed{\Pr\big(L(W_n)=2k+1\big)\longrightarrow(1-\alpha)\alpha^k \quad(k\ge0),}
\]
while for each \(k\ge1\), \(\Pr(L(W_n)=2k)\to0\). These point probabilities sum to one, so they define weak convergence to an odd-valued geometric law. Moreover,
\[
\boxed{\lim_{n\to\infty}\mathbb E[L(W_n)]
=\frac{1+\alpha}{1-\alpha}=1.1449870789182282\ldots.}
\]

## Assumptions and scope

All words are **linear** (not circular), over exactly the symbols `0` and `1`. An opening parenthesis is `0`, a closing parenthesis is `1`. Length in generating functions is **semilength**, so a Dyck word with \(2n\) symbols contributes \(z^n\). Borders compare literal binary strings, **not** Abelian equivalence of prefixes and suffixes. Block-palindrome pieces are nonempty except that the unique center may be empty. The width is the count of nonempty blocks. There is no bound on Dyck height. The formulas hold for all \(n,r\ge0\); the probability statements concern \(n\to\infty\) with each fixed \(k\).

## Proof

**1. Every ordinary border of a Dyck word is Dyck.** For any binary string \(x\), let \(h(x)=|x|_0-|x|_1\). Suppose \(b\) is a nonempty proper border of \(w\in\mathcal D_n\). Since \(b\) is a prefix of \(w\), \(h(b)\ge0\), and all prefixes of \(b\) have nonnegative height. Since \(b\) is also a suffix, write \(w=yb\). Because \(h(w)=0\) and \(h(y)\ge0\), we have \(h(b)=-h(y)\le0\). Hence \(h(b)=0\); together with prefix nonnegativity this makes \(b\) a Dyck word. If \(w=bvb\), then \(h(b)=0\) implies that \(v\) is also Dyck, by examining the portion of the height path between the two copies of \(b\).

**2. Unique shortest-border decomposition.** If a nonempty word has a shortest border \(b\), then \(b\) is unbordered: a proper border of \(b\) would also border the original word. Two occurrences of an unbordered \(b\), one at either end, cannot overlap; overlap would make a shorter border of \(b\). Thus every bordered nonempty Dyck word is uniquely \(bvb\), with \(b\) an unbordered nonempty Dyck word and \(v\) an arbitrary Dyck word. Conversely, for any such \(b,v\), the word \(bvb\) is Dyck, and no border shorter than \(b\) exists because it would border \(b\). Consequently, \(b\) is its unique shortest border. This proves a disjoint decomposition
\[
\mathcal D=\{\varepsilon\}\ \sqcup\ \mathcal U\ \sqcup\
\bigsqcup_{b\in\mathcal U}\{bvb:v\in\mathcal D\},
\]
where \(\mathcal U\) is the set of all nonempty unbordered Dyck words. Taking semilength weights gives
\[
C(z)=1+U(z)+U(z^2)C(z).
\]
Equivalently, \(U_0=0\) and, for every \(n\ge1\),
\[
U_n=\frac{1}{n+1}\binom{2n}{n}-
\sum_{j=1}^{\lfloor n/2\rfloor}U_j\frac{1}{n-2j+1}\binom{2(n-2j)}{n-2j}.
\]
This recurrence determines \(U_n\) inductively.

**3. The maximal-width decomposition is obtained by iterated shortest borders.** Here is an elementary exchange argument. Consider any factorization of a nonempty word \(w\) whose outer paired block is \(b\), so \(w=bvb\). Let \(s\) be its shortest border. If \(s=b\), the outer peel is already greedy. Otherwise \(s\) is an unbordered proper prefix and suffix of \(b\); the copies cannot overlap, so \(b=sys\) for a possibly empty word \(y\). Thus
\[
w=s\,y\,s\,v\,s\,y\,s.
\]
Peeling \(s\), then \(y\) if nonempty, and then \(s\) leaves the same center \(v\); this uses at least as many paired blocks as peeling \(b\). Repeating this exchange on the remaining center shows that successively taking shortest borders maximizes width. In the Dyck case, Step 1 makes every peeled block and every remaining center Dyck; Step 2 makes every peeled shortest border unbordered.

Consequently, every Dyck word has a **unique** maximal-width block decomposition: an arbitrary finite sequence of nonempty unbordered Dyck words, paired symmetrically around either an empty center or a single nonempty unbordered Dyck center. Conversely, any such sequence indeed follows greedy peeling because the outermost block is unbordered and therefore is the shortest border. Each paired block of semilength \(j\) contributes \(z^{2j}t^2\), and an optional nonempty center contributes \(tU(z)\). Summing the geometric series yields
\[
\sum_{n,r\ge0}B_{n,r}z^nt^r
=(1+tU(z))\sum_{k\ge0}t^{2k}U(z^2)^k.
\]

**4. Limiting distribution.** The Catalan function has the singular expansion
\[
C(z)=2-2\sqrt{1-4z}+O(1-4z)
\]
as \(z\to1/4\) in a slit neighborhood. Because \(0\le U_n\le C_n\le4^n\), \(U(z^2)\) is analytic for \(|z|<1/2\); write \(\alpha=U(1/16)\), with \(0<\alpha<C(1/16)-1<1\). Substitution into Step 2 gives
\[
U(z)=1-2\alpha-2(1-\alpha)\sqrt{1-4z}+O(1-4z).
\]
Standard square-root coefficient transfer, or direct convolution with Catalan coefficients, implies
\[
[z^n]U(z)\sim(1-\alpha)C_n.
\]
For fixed \(k\ge0\), the coefficient of \(t^{2k+1}\) in Step 3 is \(U(z)U(z^2)^k\). The analytic multiplier takes value \(\alpha^k\) at \(z=1/4\), whence
\[
[z^n]U(z)U(z^2)^k\sim(1-\alpha)\alpha^k C_n.
\]
For fixed positive \(k\), \(U(z^2)^k\) is analytic in \(|z|<1/2\), so its coefficients are exponentially smaller than \(C_n\). This proves the limiting point probabilities. The odd probabilities sum to \((1-\alpha)\sum_{k\ge0}\alpha^k=1\), leaving no escaping probability mass. Finally, differentiating the bivariate generating function at \(t=1\), where its denominator stays nonzero near \(z=1/4\), and applying the same square-root transfer yields the stated limiting mean \((1+\alpha)/(1-\alpha)\).

## Verification

Run `python3 VERIFY.py` with Python 3 and no external packages. It enumerates every Dyck word of semilength \(1\) through \(12\), computes largest block-palindrome width directly by string comparisons, and compares the complete width histograms against the independent generating-function coefficient recurrence. There are \(290511\) such nonempty words. It separately checks all coefficient identities through semilength \(80\) using exact integers. It evaluates \(\alpha\) from \(80\) exact coefficients with the rigorous tail bound \((1/4)^{81}/(1-1/4)<2.29\cdot10^{-49}\). The program reports `DYCK_BP_PASS` when every check succeeds.

The enumeration and coefficient checks are finite corroboration, **not** proofs of the infinite identities or limiting distribution; those follow from Steps 1–4.

## Relationship to prior work

Gabrić and Shallit (2023) study maximal block-palindrome width for **unrestricted fixed-alphabet words**, and describe shortest-border peeling and exact width recurrences. Their factorization machinery is a point of departure, not claimed as new. The present result establishes the previously unaddressed **Catalan/Dyck restriction**, where an ordinary border is itself constrained to be balanced, and derives its exact series and **odd-geometric limiting law**. The source's general fixed-alphabet enumeration does not give the Dyck-restricted coefficients or the parameter \(U(1/16)\).

Barcucci, Bernini, and Pinzani (2021) construct **strong non-overlapping codes consisting of selected Dyck paths**. Their work motivates studying self-overlap, but is not an enumeration of *all* unbordered Dyck words or their block widths. Mol, Rampersad, and Shallit (2023, revised 2024) study Dyck factors of automatic words and pattern avoidance, not ordinary borders of arbitrary Dyck words. Blanchet-Sadri, Chen, and Hawes (2017) analyze **Abelian borders** of arbitrary binary words via Dyck paths; Abelian equality does not imply literal equality of the border strings.

## Limitations

This theorem counts ordinary Dyck words on one parenthesis type, not multitype Dyck languages, height-restricted walks, Abelian-border factorizations, or smallest-width variants. The geometric limit is a statement about uniformly sampled Dyck words with semilength tending to infinity, not about arbitrary constrained ensembles. The mathematical argument establishes these claims, while priority against uncatalogued or alternative-terminology literature remains subject to independent examination. No independent mathematical audit has been performed.

## References

1. Daniel Gabrić and Jeffrey Shallit, *Smallest and Largest Block Palindrome Factorizations*, arXiv:2302.13147, version 1 publicly available February 25, 2023; WORDS 2023, DOI 10.1007/978-3-031-33180-0_14. https://arxiv.org/abs/2302.13147
2. Keisuke Goto, Tomohiro Itagaki, Hideo Bannai, and Shunsuke Inenaga, *Block Palindromes: A New Generalization of Palindromes*, arXiv:1806.00198 (2018). https://arxiv.org/abs/1806.00198
3. Elena Barcucci, Antonio Bernini, and Renzo Pinzani, *A Strong Non-overlapping Dyck Code*, Developments in Language Theory (DLT 2021), pages 43–53, DOI 10.1007/978-3-030-81508-0_4.
4. Lucas Mol, Narad Rampersad, and Jeffrey Shallit, *Dyck Words, Pattern Avoidance, and Automatic Sequences*, arXiv:2301.06145, version 1 January 15, 2023. https://arxiv.org/abs/2301.06145
5. Francine Blanchet-Sadri, Kun Chen, and Kenneth Hawes, *Dyck Words, Lattice Paths, and Abelian Borders*, Electronic Proceedings in Theoretical Computer Science 252 (2017), pages 56–70, DOI 10.4204/EPTCS.252.9.
