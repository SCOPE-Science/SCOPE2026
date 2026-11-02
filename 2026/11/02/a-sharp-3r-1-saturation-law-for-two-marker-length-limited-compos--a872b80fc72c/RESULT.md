# A sharp \(3r-1\) saturation law for two-marker length-limited composition decks

## Finding

For \(n\ge2\) and \(1\le r\le n\), consider all binary *linear* words of length \(n\) containing exactly two ones. The observation consists of the unordered multiset of compositions (Hamming weights, with lengths) of every nonempty contiguous substring of length at most \(r\); multiplicities are retained, positions and substring orders are not. Let \(C_{n,r}^{(2)}\) be the number of distinct observations. The exact finite-length formula is

\[
C_{n,r}^{(2)}=\sum_{B=2}^{\min(r,n)}\min\left\{r,\left\lfloor\frac{n+2-B}{2}\right\rfloor\right\}+\sum_{A=1}^{r-1}\left(\min\{r-1,n-r+1-A\}-A+1\right)_{+}+\min\{r-1,(n-2r+1)_{+}\}+\mathbf1_{\{n\ge3r-1\}},
\]
where \((t)_{+}=\max(t,0)\) and an empty sum is zero. In particular, for every \(r\ge1\),

\[
\boxed{C_{n,r}^{(2)}=\frac{r(3r-1)}2\quad\text{for every }n\ge\max\{2,3r-1\}.}
\]
For every \(r\ge2\), at \(n=3r-2\) the count is one less, so this saturation length is sharp. This is also the exact largest zero-error code size for the stated restricted read-multiset channel, because one representative can be selected from each observation fiber.

There is a complete description of every fiber. Every input can be written uniquely as \(0^a1 0^b1 0^c\), where \(a,b,c\ge0\) and \(a+b+c+2=n\). Put \(A=a+1\), \(B=b+2\), \(D=c+1\). Define \(S_r(A,D)\) as the multiset of members of \(\{A,D\}\) strictly less than \(r\), retaining repeated values. **Two inputs give the same observation if and only if** they have equal signatures

\[
\sigma_r(a,b,c)=\begin{cases}
(B,S_r(A,D)),&B\le r,\\
(\infty,S_r(A,D)),&B>r.
\end{cases}
\]
Here \(\infty\) is a formal marker, not a numerical gap length. Thus the description determines all words in any ambiguity class without enumeration of all binary strings.

## Assumptions and scope

Each substring occurrence is counted, including overlapping occurrences. A composition records its substring length and number of ones, but not order. The source is restricted to weight exactly two; other source weights are excluded from codebook selection. The word is linear, with endpoints, not a necklace or a circular sequence. Reversal gives the same observation and remains part of a fiber. The theorem holds for all integers \(n\ge2\), \(1\le r\le n\), including \(r=1\), when there is one observation profile.

## Proof

**1. Two exact generating identities.** For \(\ell=1,\ldots,n\), let \(N_{\ell,j}\) denote the number of length-\(\ell\) substrings containing exactly \(j\) ones, where \(j\in\{0,1,2\}\). Set

\[
F(z)=\sum_{\ell=1}^{n}(N_{\ell,1}+N_{\ell,2})z^\ell,\qquad G(z)=\sum_{\ell=1}^{n}N_{\ell,2}z^\ell.
\]
A substring containing no one must lie completely in one of the three zero runs. Thus the coefficient of \(z^\ell\) in \(F\) is \(n-\ell+1-\sum_{g\in\{a,b,c\}}(g-\ell+1)_+\). The exact generating identity

\[
(1-z)^2\sum_{\ell=1}^{g}(g-\ell+1)z^\ell=gz-(g+1)z^2+z^{g+2}
\]
(with both sides zero when \(g=0\)) consequently gives

\[
(1-z)^2F(z)=2z-z^{a+2}-z^{b+2}-z^{c+2}+z^{n+2}.\tag{1}
\]
A substring containing both ones consists of both markers, some \(0\le i\le a\) zeros before the first, and some \(0\le j\le c\) zeros after the second. Its length is \(b+2+i+j\), so

\[
G(z)=z^{b+2}(1+z+\cdots+z^a)(1+z+\cdots+z^c)
\]
and hence

\[
(1-z)^2G(z)=z^{b+2}-z^{a+b+3}-z^{b+c+3}+z^{n+2}.\tag{2}
\]
All identities are polynomial equalities over the integers, with no asymptotic approximation.

**2. Complete profile equivalence.** The length-\(r\)-limited observation supplies precisely the coefficients of \(F\) and \(G\) through degree \(r\), because \(N_{\ell,0}+N_{\ell,1}+N_{\ell,2}=n-\ell+1\) is known. Since \(r\le n\), the final monomials at degree \(n+2\) in (1) and (2) cannot be seen. In (2), when \(B=b+2\le r\), the first nonzero coefficient is at degree \(B\), with coefficient \(+1\); both negative exponents are strictly larger. Thus \(B\) is recovered exactly. If \(B>r\), the truncation of (2) is zero. In either case, subtracting the known \(z^B\) contribution from (1), if visible, recovers the multiset of degrees \(a+2=A+1\) and \(c+2=D+1\) that do not exceed \(r\). This is precisely \(S_r(A,D)\). Conversely the signature determines the coefficients in both truncated identities, because all other possible monomials in (2) are controlled by \(B\) and the detected outer gap values. This proves the stated if-and-only-if fiber classification.

**3. Exact counting at arbitrary length.** If \(B\le r\), then \(2\le B\le\min(r,n)\) and \(A+D=n+2-B\). Because the signature is invariant under \(A\leftrightarrow D\), consider \(1\le A\le D\). Each \(A<r\) gives a separate signature, while all possibilities with \(A\ge r\), if any, collapse to one. Thus the number for a fixed \(B\) is

\[
\min\left\{r,\left\lfloor\frac{n+2-B}{2}\right\rfloor\right\}.
\]
If \(B>r\), put \(H=n-r+1\). The condition \(B=n+2-A-D\ge r+1\) is equivalent to \(A+D\le H\). The signatures fall into three disjoint types. If both outer values are small, then \(1\le A\le D\le r-1\) and \(A+D\le H\), giving \(\sum_{A=1}^{r-1}(\min\{r-1,H-A\}-A+1)_+\). If precisely one is small, its value ranges from \(1\) to \(\min\{r-1,(n-2r+1)_+\}\), giving that many signatures. If neither is small, a signature exists exactly when \(A,D\ge r\) and \(A+D\le H\), or \(n\ge3r-1\). Adding the disjoint counts proves the finite-length formula. Each signature is realizable by choosing the corresponding nonnegative \(a=A-1\), \(b=B-2\), \(c=D-1\), so there is no hidden integrality or graphical obstruction.

**4. Sharp saturation.** For \(n\ge3r-1\), the four summands become respectively \(r(r-1)\), \(r(r-1)/2\), \(r-1\), and \(1\). Their sum is \(r(3r-1)/2\). For \(r\ge2\) at \(n=3r-2\), the first three are already at those values, but the fourth is zero, proving a deficit of exactly one. Every summand in the finite-length formula is nondecreasing in \(n\), so no earlier length can have the saturated count. At \(r=1\), every weight-two word yields the same singleton-symbol observation, and the minimum permitted length \(n=2\) already attains the formula.

## Verification

The standalone `verify_two_marker_limited_deck.py` independently constructs all literal substring-composition multisets for every allowed pair of \(n\) and \(r\) with \(2\le n\le25\), covers 50,050 source-profile instances, checks equivalence of the observed fibers and the closed signatures in both directions, and checks the finite-length count. It also compares both exact polynomial identities against direct substring enumeration, and checks the saturation and immediate-boundary formulas at larger parameters. Run `python3 verify_two_marker_limited_deck.py` in the directory containing this document and the script. The observed output includes `VERIFY_OK both_exact_generating_polynomial_identities=True` and `VERIFY_OK full_finite_length_formula=True saturation_and_boundary=True`. These finite tests are corroboration only; the infinite-parameter claim follows from the proof above.

## Relationship to prior work

Ye and Elishco (2022, Section VIII) introduce the length-limited substring-composition observation and give Lyndon-based reconstruction codes, rather than the exact restricted weight-two observation-fiber classification and all-length capacity formula established here. Gupta and Mahdavifar (2022, Sections II–IV) study a reconstruction algorithm and codes for the **full** substring-composition multiset. Acharya and coauthors (2014, Sections 2, 5–11) study the full-composition equivalence relation; the special full-length boundary \(r=n\) is not asserted as novel here. A published exact \(r=2\) result for **all binary source words** is also compatible with the special \(r=2\) boundary in this theorem, but does not give the variable-cutoff, weight-two saturation theorem. These models are related but their quantitative statements do not imply the claimed \(r\)-dependent law without a new analysis. Searching cannot exclude all equivalent formulations.

## Limitations

The claim assumes exact multiplicities, a known length, exactly two ones, linear words, and observations of **all** substring lengths through \(r\). It does not treat corrupted or missing readings, mixtures of strands, cyclic words, larger weights, or unrestricted-source channel capacity. The sharp saturation statement is about the number of distinguishable weight-two messages, not unique recovery of all inputs. Independent scientific verification has not been performed; novelty risk remains from potentially unlocated specializations in the literature on sparse turnpike-type reconstruction.

## References

- Z. Ye and O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963 (first public 2022-08-31), especially Section VIII. https://arxiv.org/abs/2208.14963
- U. Gupta and H. Mahdavifar, *A New Algebraic Approach for String Reconstruction from Substring Compositions*, arXiv:2201.09955 (first public 2022-01-24), Sections II–IV. https://arxiv.org/abs/2201.09955
- J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, and S. Pan, *String Reconstruction from Substring Compositions*, arXiv:1403.2439 (first public 2014-03-10), full-composition setting. https://arxiv.org/html/1403.2439v1
- *Exact binary \(r=2\) length-limited composition reconstruction*, publicly indexed research note (all-weight comparison). https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-binary-r-2-length-limited-composition-reconstruction--a98561a7f27e
