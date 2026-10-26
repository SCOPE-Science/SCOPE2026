# Pseudo-Frobenius elements and Padovan type of Lucas-shift numerical semigroups

## Finding
Let \(L_0=2\), \(L_1=1\), and \(L_{j+2}=L_{j+1}+L_j\). For every integer \(a\ge5\), consider the numerical semigroup
\[
S_a=\langle L_a,\ L_a+L_n:n\ge0\rangle.
\]
Write \(T_0=1\), \(T_1=2\), and \(T_i=L_i\) for \(i\ge2\). For every \(0\le x<L_a\), let \(x=\sum_{i=0}^{a-1}b_iT_i\) be its unique Lucas digit expansion, with \(b_i\in\{0,1\}\), \(b_ib_{i+1}=0\), and \(b_0b_2=0\), and let \(\beta(x)=\sum b_i\). Define \(\mathcal M_n\) as the maximal independent subsets of a path on \(n\) successive vertices, and \(P_n=|\mathcal M_n|\), with \(P_0=P_1=1\), \(P_2=2\), \(P_n=P_{n-2}+P_{n-3}\) for \(n\ge3\).

The complete set of pseudo-Frobenius elements of \(S_a\) is
\[
\operatorname{PF}(S_a)=\{\,\beta(x)L_a+x-L_a:x\in X_a\,\},
\]
where \(X_a\) is the **disjoint** union of the following digit-word classes:

1. \(b_0=1\), \(b_1=b_2=0\), and \(\{i\in[3,a-1]:b_i=1\}\) is a maximal independent set of the path \(3,4,\ldots,a-1\).
2. \(b_0=b_2=0\), \(b_1=b_3=1\), and \(\{i\in[3,a-1]:b_i=1\}\) is a maximal independent set of the same path containing vertex \(3\).
3. If \(a\) is odd, the two exceptional integers \(x=L_a-1\) and \(x=L_a-2\).

In particular, the Cohen–Macaulay type of the numerical-semigroup ring (equivalently, the number of pseudo-Frobenius elements) is exactly
\[
\boxed{\operatorname{type}(S_a)=P_{a-3}+P_{a-5}+2\mathbf1_{a\text{ odd}}}\qquad(a\ge5).
\]
The exact small cases are \(\operatorname{type}(S_2)=2\), \(\operatorname{type}(S_3)=3\), and \(\operatorname{type}(S_4)=2\). Consequently the type grows on the scale of the plastic constant to the power \(a\), where the plastic constant is the largest positive root of \(z^3-z-1\).

## Assumptions and scope
All semigroups and integers are over \(\mathbb N_0\), and the pseudo-Frobenius definition is \(\operatorname{PF}(S)=\{g\notin S:g+s\in S\ \forall s\in S\setminus\{0\}\}\). The distinguished Lucas ordering \(1,2,3,4,7,11,\ldots\) is essential. The original 2022 Lucas-shift semigroup theorem gives (i) the stated unique legal digit expansions and their minimum number of Lucas summands, and (ii) the Apéry-set formula \(\operatorname{Ap}(S_a,L_a)=\{\beta(x)L_a+x:0\le x<L_a\}\), with minimal generators \(L_a\) and \(L_a+T_i\) for \(0\le i<a\). These facts are stated and proved in the primary cited preprint; the novel steps below start from them.

## Proof
Put \(m=L_a\). For each \(x<m\), denote its Apéry representative by \(w_x=\beta(x)m+x\). The Apéry maximality criterion states that \(w_x-m\) is pseudo-Frobenius exactly when \(w_x+T_i\in S_a\) for every \(0\le i<a\). Equivalently, for \(y=x+T_i\) and \(e=\lfloor y/m\rfloor\in\{0,1\}\),
\[
\beta(y-em)\le\beta(x)+e.\tag{1}
\]
Indeed \(w_x+T_i=\beta(x)m+y\), and membership is exactly comparison against \(w_{y-em}\). We use the following elementary *coin-bound criterion*. If \(x+T_i\) can be expressed with at most \(\beta(x)\) Lucas coins, then (1) follows. For \(y<m\), this is the minimum-coin property. For \(m\le y<m+T_{a-1}=L_{a+1}\), the canonical Lucas expansion begins with one \(L_a\) and has the canonical expansion of \(y-m<T_{a-1}\) below it; hence its minimum coin count equals \(1+\beta(y-m)\). The claimed implication follows. The strict inequality \(y<m+T_{a-1}\) holds because \(x<m\) and \(T_i\le T_{a-1}\).

**Necessity: isolated vacant digits.** Let \(b\) be a legal word. If a vacant digit \(i\) has no occupied neighbor on the path \(0-1-2-\cdots-(a-1)\) and (for \(i=0,2\)) no occupied digit at the other endpoint of the extra edge \(0-2\), then placing a \(1\) at digit \(i\) produces another legal Lucas word. It represents \(x+T_i<m\), and has coin minimum \(\beta(x)+1\), contradicting (1). Thus every candidate legal word is a maximal independent set in this path-plus-extra-edge graph.

If \(b_0=1\), necessarily \(b_1=b_2=0\), and the occupied vertices among \(3,\ldots,a-1\) must be a maximal independent set of that upper path: this gives class 1. If \(b_0=0,b_1=1,b_3=1\), we likewise get class 2. The remaining graph-maximal candidates begin either with \(b_0=b_1=0,b_2=1\), or with \(b_0=0,b_1=1,b_2=b_3=0\). We show that only the two stated endpoints survive.

For the first remaining case, assume that consecutive even digits \(2,4,\ldots,j\) are occupied, \(j\) even, and either \(j+2<a\) is vacant or \(j=a-2\) (the top index is odd). By choosing the *last* even index of the initial uninterrupted even run, the digit \(j+1\) exists, and adding \(T_j\) converts the doubled even run into the legal digit set \(1,3,5,\ldots,j+1\), leaving the higher originally occupied digits unchanged. This follows by repeated use of \(2T_i=T_{i+1}+T_{i-2}\) for even \(i\ge4\) and \(2T_2=T_3+T_1\). No new pair is adjacent: the higher old digits begin at \(j+3\) or later, because digit \(j+2\) is vacant. The new word has \(\beta(x)+1\) digits and value \(x+T_j<m\) (it is a legal word of length \(a\)); hence (1) fails. Therefore this case survives only when \(a\) is odd and all even digits \(2,4,\ldots,a-1\) are occupied, which is exactly \(x=m-1\).

In the second remaining case, upper-path maximality requires \(b_4=1\). Suppose the initial run \(4,6,\ldots,j\) of occupied even positions stops before the top, where \(j\) is even. Repeatedly rewriting \(2T_i=T_{i+1}+T_{i-2}\), and using \(T_2+T_1=T_3+T_0\), transforms the digits \(1,4,6,\ldots,j\) plus one extra \(T_j\) into the legal set \(0,3,5,\ldots,j+1\), leaving higher digits unchanged. This again has \(\beta(x)+1\) coins and stays below \(m\), contradicting (1). The only survivor has \(a\) odd and digits \(1,4,6,\ldots,a-1\); its value is \(m-2\). This proves that all pseudo-Frobenius codes belong to the three stated classes.

**Sufficiency: maximal-independent upper path.** Consider a word in class 1 or 2, and add any \(T_i\). If \(b_i=0\), then the occupied neighbors guaranteed by maximality permit merging \(T_i\) with a selected neighboring coin into one coin. The only special bottom cases are \(T_0+T_1=T_2\) and \(T_0+T_2=T_3\); in class 1 the vacant digit \(2\) is handled by selected \(0\), while in class 2 the vacant digits \(0,2\) are handled by selected \(1,3\), respectively. Thus the new sum has at most \(\beta(x)\) coins.

If \(b_i=1\), propagate the duplicate downward using \(2T_i=T_{i+1}+T_{i-2}\) for \(i\ge4\). Successive occupied vertices of a maximal independent set of a path are separated by gaps of \(2\) or \(3\). A gap of \(2\) transmits the duplicate downward; a gap of \(3\) produces an adjacent pair, which merges and reduces the number of coins by one. The process necessarily reaches a gap of \(3\) or the bottom: in class 1 the bottom is \(b_0=1\), with first upper occupied digit \(3\) or \(4\); in class 2 it is \(b_1=b_3=1\). At these bottoms the identities
\[
2T_0=T_1,\quad 2T_1=T_3,\quad 2T_3=T_4+T_0,\quad 2T_4=T_5+T_2,\quad T_0+T_2=T_3,\quad T_0+T_1=T_2
\]
terminate the reduction with at most \(\beta(x)\) coins. In class 2, doubling \(T_1\) first produces \(T_3\), where the same reduction applies. Hence the coin-bound criterion gives (1) for every \(i\). Every word in classes 1 and 2 is pseudo-Frobenius.

**Exceptional endpoints.** When \(a\) is odd, the words for \(m-1\) and \(m-2\) have the same number \((a-1)/2\) of coins. Thus their Apéry representatives differ by one and are the two largest representatives; the first equals the maximum Apéry element by the cited Frobenius formula. Their gaps are \(F(S_a)\) and \(F(S_a)-1\), respectively. Since the multiplicity is \(m\ge11\), adding any positive semigroup element to either gap exceeds \(F(S_a)\); both are pseudo-Frobenius.

**Counting.** Class 1 is counted by \(P_{a-3}\). Class 2 consists of maximal independent sets of the upper path containing its first vertex; that vertex forces the second out, leaving an arbitrary maximal independent set on the remaining \(a-5\) vertices, hence \(P_{a-5}\). Class 3 contributes two exactly for odd \(a\). The decomposition is disjoint and exhaustive, yielding the formula. The recurrence \(P_n=P_{n-2}+P_{n-3}\) follows by splitting maximal independent sets according to the first vertex, and gives growth at the plastic-constant rate. The three smaller values follow by direct Apéry calculation.

## Verification
Run `python3 verify_lucas_type.py` (standard library only). For \(5\le a\le21\), it independently builds all legal digit words, computes minimum coin counts via dynamic programming, determines pseudo-Frobenius codes using (1), and compares the exact sets to the three stated classes. For \(5\le a\le13\), it also independently recomputes all Apéry representatives via a weighted shortest-path algorithm on residues, rather than relying on the coin-count formula. Finite checking cannot establish the infinite theorem, which follows from the proof above.

## Relationship to prior work
Robles-Pérez and Rosales, arXiv:2211.01436 (first posted 2022-11-02), determine generators, canonical Lucas representations, Apéry sets, Frobenius number, genus, and related invariants for this precise Lucas-shift family. They do not classify its pseudo-Frobenius gaps or Cohen–Macaulay type. The later work on **shifted \(r\)-Fibonacci** semigroups (arXiv:2503.01266) calculates types for different generator families; the special \(0-2\) Lucas digit restriction prevents directly identifying those families with the present one. Related general work on numerical-semigroup type and maximal Apéry elements supplies tools, but not the stated Lucas classification in inspected material. The new theorem deliberately takes the 2022 Apéry identities as input and computes a distinct invariant.

## Limitations
The formula assumes the exact unshifted Lucas sequence with the specified special initial ordering. It does not assert the same result for general \(r\)-Fibonacci, altered Lucas initial conditions, or arbitrary semigroups. The 2022 preprint was inspected as the public full text; an unindexed theorem, implicit derivation from more general results, or a later inaccessible journal-only addition could affect publication priority. The computational tests are finite and not a substitute for the proof. No independent audit has been performed.

## References
1. A. M. Robles-Pérez and J. C. Rosales, *The extended Frobenius problem for Lucas series incremented by a Lucas number*, arXiv:2211.01436, first public 2022-11-02, https://arxiv.org/abs/2211.01436.
2. *The extended Frobenius problem for r-Fibonacci sequences shifted by r-Fibonacci numbers*, arXiv:2503.01266, https://arxiv.org/abs/2503.01266 (comparison only; distinct semigroup family).
3. Standard Apéry maximality characterization of pseudo-Frobenius elements: \(\operatorname{PF}(S)=\{w-m:w\text{ maximal in }\operatorname{Ap}(S,m)\text{ for the semigroup order}\}\).
