# Fixed-binary asymptotic sharpness of the frequent-factor bound

## Finding

For a finite word \(T\), let \(\operatorname{occ}_T(U)\) be the number of starting positions at which the nonempty contiguous factor \(U\) occurs, counting overlapping occurrences, and define
\[
\Phi(T)=\#\{U\ne\varepsilon:\ U\text{ is a factor of }T,\ \operatorname{occ}_T(U)>|U|\}.
\]

**Constructive bound.** For every integer \(d\ge1\), set \(p=2^d\). For any integer \(n\ge p\), put
\[
L=\left\lfloor\frac{n-p+1}{p+1}\right\rfloor.
\]
If \(L\ge d\), there is an explicitly constructible **binary** word \(T\) of length \(n\) for which
\[
\Phi(T)\ge p(L-d+1).
\]

**Uniform consequence.** For every integer \(n\ge64\), there is a binary word \(T_n\) of length \(n\) satisfying
\[
\Phi(T_n)>n-3\sqrt{n\log_2 n}.
\]
Consequently, if \(M_2(n)=\max_{T\in\{0,1\}^n}\Phi(T)\), then
\[
\lim_{n\to\infty}\frac{M_2(n)}{n}=1.
\]
The same limit holds when the binary alphabet is replaced by any **fixed** alphabet having at least two letters.

## Assumptions and scope

All strings are finite unless explicitly described as periodic infinite strings. Distinct factors are distinguished by their contents rather than their occurrence positions. Frequencies count overlapping occurrences. Strict inequality \(\operatorname{occ}_T(U)>|U|\) is essential; replacing it with a non-strict inequality changes the counting threshold. Binary means an alphabet of exactly two available symbols, not an alphabet whose size increases with \(n\). No claims concern the smallest possible deficit \(n-M_2(n)\) beyond the displayed upper estimate.

## Proof

**1. Cyclic block.** For each \(d\ge1\), a binary de Bruijn cycle of order \(d\) is a cyclic word \(B\) of length \(p=2^d\) in which every binary length-\(d\) word occurs at exactly one cyclic starting position. Such cycles exist: construct the directed graph on binary length-\((d-1)\) words, with an edge labeled by each length-\(d\) word from its length-\((d-1)\) prefix to its length-\((d-1)\) suffix. Every vertex has indegree and outdegree two; the graph is strongly connected (append the letters of any desired target vertex). An Euler circuit spells the required cyclic edge-label sequence. This argument includes \(d=1\), where the single vertex has two loops.

**2. All phases remain distinguishable.** Let \(T\) be the first \(n\) symbols of the infinite periodic word \(BBBB\cdots\). For every \(\ell\ge d\), the length-\(\ell\) words starting at phases \(0,1,\ldots,p-1\) of the period are pairwise distinct. Indeed, equal length-\(\ell\) factors would have equal first \(d\) symbols and contradict the de Bruijn property.

**3. All these factors have high frequency up to a cutoff.** There are \(n-\ell+1\) possible starting positions for a length-\(\ell\) factor of \(T\), distributed among \(p\) residue classes modulo \(p\). Each residue class contains at least
\[
\left\lfloor\frac{n-\ell+1}{p}\right\rfloor
\]
starts. If \(\ell\le L=\lfloor(n-p+1)/(p+1)\rfloor\), then
\[
 n-\ell+1\ge p(\ell+1),\qquad
 \left\lfloor\frac{n-\ell+1}{p}\right\rfloor\ge\ell+1.
\]
Thus every one of the \(p\) distinct phase factors of length \(\ell\) occurs more than \(\ell\) times. Summing over the different lengths \(d\le\ell\le L\) proves \(\Phi(T)\ge p(L-d+1)\).

**4. Choice of order for an arbitrary length.** Fix an integer \(n\ge64\), write \(a=\log_2 n\), and take
\[
d=\left\lfloor\tfrac12\log_2(n/a)\right\rfloor,
\quad p=2^d,
\quad L=\left\lfloor\frac{n-p+1}{p+1}\right\rfloor.
\]
Then \(a\ge6\), \(d\ge1\), and
\[
\tfrac12\sqrt{n/a}<p\le\sqrt{n/a},\qquad d+1\le a.
\]
We first verify \(L\ge d\). This is equivalent to \(n\ge p(d+1)+d-1\), which follows from
\[
p(d+1)+d-1\le\sqrt{na}+\tfrac12a<n.
\]
For the last inequality, use \(a=\log_2 n\le n/8\) for every \(n\ge64\), so the preceding sum is at most \(n/\sqrt8+n/16<n\). Therefore the constructive bound applies.

Since \(\lfloor x\rfloor\ge x-1\),
\[
\begin{aligned}
n-\Phi(T)
&\le n-p(L-d+1)\\
&\le\frac{n+p(p-1)}{p+1}+pd\\
&<\frac np+p(d+1)\\
&<3\sqrt{na}=3\sqrt{n\log_2 n}.
\end{aligned}
\]
This proves the uniform assertion with an explicit word construction.

**5. Sharp limiting coefficient.** Bals, Charalampopoulos, Lachish, Pissis and Verbeek (2026, Theorem 1) prove \(\Phi(T)\le |T|\) for every finite word, using an injection from nodes of a suffix trie satisfying \(\operatorname{depth}(v)<\#\operatorname{leaves}(v)\) into the leaves. Combining that established upper bound with the binary construction gives
\[
1-3\sqrt{\frac{\log_2 n}{n}}<\frac{M_2(n)}n\le1,
\]
and the limit follows. A fixed alphabet of larger size contains a binary subalphabet, so the same lower and upper bounds apply to its maximum.

## Verification

The accompanying `verify.py` constructs binary de Bruijn cycles by the standard recursive cycle generator and computes factor occurrence counts directly for fifteen explicit constructions, including three fixed-order examples with orders three through five. It also checks the uniqueness of all order-\(d\) cyclic windows for \(1\le d\le8\), and independently checks the integer cutoff and square-root inequality for 20,919 numerical lengths. See `output.txt`. These are finite checks only; the universal quantifiers and asymptotic conclusion follow from the preceding proof.

## Relationship to prior work

Bals et al., *Text Indexing: From Reporting to Counting* (ESA 2026), prove the universal \(n\)-factor upper bound. Their Proposition 6 demonstrates asymptotic sharpness using a period of \(r\) **distinct** alphabet symbols repeated \(r\) times: the word length and the alphabet size both grow with \(r\). That proposition does not imply a fixed-binary example, because its witnesses use \(r\) distinct symbols. The present construction changes the combinatorial mechanism: phase distinctness for all factor lengths \(\ell\ge d\) is supplied by binary de Bruijn cycles, while the logarithmic threshold \(d\) is balanced against the repetition count. The universal upper bound itself and the existence of de Bruijn cycles are not claimed as new.

The literature comparisons considered frequency-above-length factors under equivalent terminology, cyclic de Bruijn blocks, and results about total distinct-substring counts. The latter count all factors without imposing \(\operatorname{occ}_T(U)>|U|\), so its asymptotics do not determine the present statistic.

## Limitations

The deficit bound \(O(\sqrt{n\log n})\) is an upper estimate for the constructed binary words, not a proved optimal order of \(n-M_2(n)\). It gives no formula for \(M_2(n)\), no classification of its maximizers, and no assertion that random strings exhibit the same behavior. Computational checks cover only finite instances. An unindexed equivalent fixed-alphabet construction remains possible; independent scientific validation has not been performed.

## References

1. B. Bals, P. Charalampopoulos, O. Lachish, S. P. Pissis, H. Verbeek, *Text Indexing: From Reporting to Counting*, ESA 2026, Article 68, DOI: 10.4230/LIPIcs.ESA.2026.68; preprint arXiv:2607.24043 (first public preprint dated 2026-07-27).
2. G. Tesler, *Multi de Bruijn Sequences*, arXiv:1708.03654 (2017). Background on cyclic coverage of finite words; no fixed-alphabet frequent-factor sharpness is attributed to this source.
3. G. Bernardini et al., *Indexing Strings with Utilities*, arXiv:2504.05917 (2025). Related frequent-substring indexing context with a different frequency objective.
