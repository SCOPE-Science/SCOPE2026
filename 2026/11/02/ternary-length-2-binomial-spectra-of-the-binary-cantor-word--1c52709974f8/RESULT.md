# Ternary-length \(2\)-binomial spectra of the binary Cantor word

## Finding
Let \(\mathbf c\) be the one-sided fixed point of \(\sigma(1)=101\) and \(\sigma(0)=000\). For every integer \(k\ge1\), set \(n=3^k\), \(B=2^k\), and, for each integer \(0\le j<B\), let
\[
 f(j)=2\sum_{i\ge0}\epsilon_i(j)3^i,
 \qquad j=\sum_{i\ge0}\epsilon_i(j)2^i,\quad\epsilon_i(j)\in\{0,1\}.
\]
For \(1\le t\le B\), define
\[
P_t=\sum_{j=0}^{t-1}(f(j)-j),\qquad a_t=f(t-1)+1,\qquad
b_t=\begin{cases}f(t),&t<B,\\n,&t=B.\end{cases}
\]
For a binary word \(w\), let \(J(w)\) count scattered subsequences equal to `01` (with multiplicity), and put \(V(w)=(|w|_1,J(w))\). Then the **entire set** of \(2\)-binomial equivalence profiles of contiguous length-\(n\) factors of \(\mathbf c\) is exactly
\[
\boxed{\{(0,0)\}\cup\bigcup_{t=1}^{B}\bigcup_{m=a_t}^{b_t}
\{(t,\,t(m-t)-P_t),\;(t,\,t(n-m)+P_t)\}.}
\]
Distinct values of \(t\) automatically give distinct profiles. Put \(g_t=b_t-a_t+1\). If \(t\nmid 2P_t\), put \(O_t=0\); otherwise, for the integer \(S_t=n+t+2P_t/t\), set
\[
O_t=\max\bigl(0,\,\min(b_t,S_t-a_t)-\max(a_t,S_t-b_t)+1\bigr).
\]
The exact \(2\)-binomial complexity at every ternary length is the finite arithmetic formula
\[
\boxed{b_{\mathbf c,2}(3^k)=2\cdot3^k+1-\sum_{t=1}^{2^k}O_t.}
\]
This formula requires \(2^k\) explicit terms and no enumeration of the length-\(3^k\) factors.

Moreover, for **every** \(k\ge3\), at least
\[
\boxed{2\cdot3^{k-3}+1}
\]
distinct \(2\)-binomial profiles are each represented by a specified pair of *different* length-\(3^k\) factors. Thus the binomial quotient has linearly many genuinely nontrivial collisions along these lengths.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\). A *factor* is contiguous, whereas a *scattered subsequence* preserves order without requiring adjacency. Two length-\(n\) factors are \(2\)-binomially equivalent when the multiplicities of all subsequences of lengths zero, one, and two coincide. Positions and all index ranges are zero-based. The formula is for each integer \(k\ge1\), with no assertion about arbitrary other lengths.

## Proof
**Binary profile reduction.** At fixed length \(n\), write \(t=|w|_1\) and \(z=n-t\). The multiplicities of `00` and `11` are \(\binom z2\) and \(\binom t2\). The multiplicities of `01` and `10` add to \(tz\). Hence \(V(w)=(t,J(w))\) determines, and is determined by, the complete length-at-most-two scattered-subsequence spectrum.

**Morphology of length-\(n\) factors.** At substitution depth \(k\), every letter `1` becomes \(C_k=\sigma^k(1)\), and every letter `0` becomes \(0^n\). Since \(\mathbf c\) contains `00`, `01`, and `10` but not `11`, every factor of length \(n\) is either \(0^n\), a suffix of \(C_k\) completed by zeros on the right, or a prefix of \(C_k\) preceded by zeros on the left. Conversely, every such length-\(n\) word occurs, because both mixed adjacent block types occur. The entire word \(C_k\) occurs as either end case.

**Ternary locations and binomial values.** The ones in \(C_k\) have precisely the positions \(f(0),\ldots,f(B-1)\), with \(f(0)=0\) and \(f(B-1)=n-1\). This follows directly by induction from the substitution. Each \(C_k\) is a palindrome. A prefix of length \(m\) has exactly \(t\) ones precisely for \(a_t\le m\le b_t\). Over that interval its `01` count is constant:
\[
\sum_{j<t}\bigl(f(j)-j\bigr)=P_t,
\]
since only appended zeros vary. The prefix preceded by \(n-m\) zeros consequently has `01` count \(t(n-m)+P_t\). By palindromicity, the suffix of length \(m\) reverses this prefix, exchanging the scattered `01` and `10` counts. Its `01` count is therefore \(t(m-t)-P_t\); appending trailing zeros adds no `01` subsequences. This proves the boxed complete-profile description.

**Exact counting.** For each \(t\), both displayed count sets are arithmetic progressions, each of cardinality \(g_t\) and common difference \(t>0\). A value from the first equals a value from the second exactly when there exist integers \(m,m'\in[a_t,b_t]\) with
\[
t(m-t)-P_t=t(n-m')+P_t,
\]
i.e. \(m+m'=n+t+2P_t/t=S_t\). The divisibility condition and the count of permissible integers \(m\) give precisely \(O_t\) above. Because the positions run from \(f(0)=0\) to \(f(B-1)=n-1\), we have \(\sum_{t=1}^B g_t=n\). Adding the single zero profile and subtracting the intersections yields \(1+2n-\sum O_t\), as claimed.

**Linear collision family.** Fix \(k\ge3\) and write \(q=3^{k-2}\), \(h=2^{k-2}\), \(t=3h\), \(n=9q\). Directly from the ternary position formula,
\[
 a_t=7q,\quad b_t=8q,\quad \sum_{j<t}f(j)=\frac{h(19q-3)}2,
 \quad S_t=\frac{46q}{3}.
\]
(The sum groups the first \(3h\) ones into three length-\(h\) ternary blocks.) For each integer \(m\in[22q/3,8q]\), the integer \(m'=46q/3-m\) also belongs to \([7q,8q]\). Thus the factors
\[
 A_m=\operatorname{suffix}_m(C_k)\,0^{n-m},\qquad
 B_{m'}=0^{n-m'}\operatorname{prefix}_{m'}(C_k)
\]
share the same \(2\)-binomial profile. They are not identical literal words: their last-one positions are respectively \(m-1\) and \(16q-m'-1\). Equality of words would force \(m+m'=16q\), whereas actually \(m+m'=46q/3\). For different \(m\), the common `01` count \(t(m-t)-P_t\) is strictly increasing, so these collisions have distinct profiles. Their number is \(8q-22q/3+1=2\cdot3^{k-3}+1\), proving the final assertion.

## Verification
Run `python3 checker.py` with only the Python standard library. It independently constructs finite substitution words and computes the full length-\(3^k\) factor-profile sets with a rolling scattered-`01` counter for \(1\le k\le7\), then compares each set with the displayed arithmetic family. The checked exact counts are \(5,17,50,154,466,1402,4210\). Separate literal-string checks exhibit all asserted pairwise distinct collision witnesses for \(3\le k\le7\). These finite checks corroborate, but are not used to extend, the all-\(k\) proof.

## Relationship to prior work
Rigo and Salimov (2013; extended 2015) developed \(k\)-binomial equivalence and complexity, with results for Sturmian and Thue–Morse words. Their general definition and elementary binary relations are background, not claimed as discoveries here. Their Parikh-constant substitution theorem does not apply to the Cantor morphism: `1` and `0` have images with different letter counts. Lejeune, Rigo and Rosenfeld established equality of the \(k\)-binomial and ordinary factor complexities for the Tribonacci word. Here the explicit Cantor-word family instead gives linearly many nontrivial equivalences. Searches did not identify a published factor-profile classification or collision family of the stated scope; an earlier equivalent result remains possible.

## Limitations
The exact count is given as an explicit \(2^k\)-term arithmetic formula, **not** as a simpler closed polynomial in \(3^k\). No unproved simplification of this sum is asserted. The construction concerns only length \(3^k\) factors of the specified one-sided Cantor word. It does not classify all equivalence-class multiplicities, all lengths, or higher-order binomial equivalence. Independent validation and exhaustive historical priority checks have not been performed.

## References
1. M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, WORDS 2013, LNCS 8079, pp. 217–228. Public preprint: https://orbi.uliege.be/handle/2268/149313 (available since 2013-05-27).
2. M. Rigo and P. Salimov, *Another generalization of abelian equivalence: binomial complexity of infinite words*, Theoretical Computer Science 601 (2015), 47–57. Public preprint: https://orbi.uliege.be/bitstream/2268/178703/1/binomial_TCS_final.pdf.
3. M. Lejeune, M. Rigo and M. Rosenfeld, *Templates for the k-binomial complexity of the Tribonacci word*, Advances in Applied Mathematics 112 (2020), 101947. Public preprint: https://orbi.uliege.be/bitstream/2268/244495/1/version_kronecker.pdf.
