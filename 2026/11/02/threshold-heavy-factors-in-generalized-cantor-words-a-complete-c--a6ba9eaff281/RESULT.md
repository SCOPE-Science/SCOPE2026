# Threshold-heavy factors in generalized Cantor words: a complete carry-free classification

## Finding

Fix an integer \(b\ge4\). Write \(C_b\) for the infinite binary word with a \(1\) exactly at zero-based positions whose base-\(b\) digits lie in \(\{0,b-1\}\). For every integer \(j\ge0\), write \(\varepsilon_r(j)\in\{0,1\}\) for its \(r\)-th binary digit and define
\[
E_b(j)=(b-1)\sum_{r\ge0}\varepsilon_r(j)b^r.
\]
Thus the one-positions of \(C_b\), in increasing order, are exactly \(E_b(0),E_b(1),\ldots\). All intervals and factors below are contiguous and one-sided, not cyclic.

**Threshold-heavy-factor theorem.** For every integer \(k\ge1\) let
\[
j=k-1,\qquad h=\lceil\log_2 k\rceil,\qquad L_b(k)=E_b(j)+1,
\]
with \(h=0\) when \(k=1\). Then:

1. \(L_b(k)\) is the *least* factor length admitting \(k\) ones. Every factor of exactly that length with \(k\) ones begins at a position \(E_b(i)\) for which the binary bitwise conjunction of \(i\) and \(j\) is zero; conversely every such starting position works. No factor of that length contains more than \(k\) ones.
2. These extremal factors are distinct exactly according to the residue \(a=i\bmod2^h\). The complete set is represented by the words \(W_{b,k,a}\), for \(0\le a<2^h\) with \(a\mathbin{\&}j=0\), whose length is \(L_b(k)\) and whose ones are exactly at offsets
\[
\{E_b(a+r)-E_b(a):0\le r\le j\}.
\]
Consequently the **exact number** of distinct threshold-heavy factors is
\[
\boxed{H_b(k)=2^{h-s_2(j)},}
\]
where \(s_2(j)\) is the binary digit sum. Every represented factor occurs infinitely often.
3. \(C_b\) is \(1\)-prefix-normal: at each length the initial factor has the greatest possible number of ones. Let \(\Psi_b(n)\) denote the number of Abelian (letter-count) equivalence classes of length-\(n\) factors. Then, for every integer \(n\ge1\),
\[
\boxed{\Psi_b(n)=1+\#\{j\ge0:E_b(j)<n\}.}
\]

In particular, \(H_b(2^m)=1\) but \(H_b(2^m+1)=2^m\), for all \(m\ge1\). The multiplicity of maximal-weight *distinct words*, as opposed to the maximal weight itself, therefore has arbitrarily large adjacent threshold jumps.

For illustration in base \(4\), the pairs \((k,L_4(k),H_4(k))\) begin \((1,1,1)\), \((2,4,1)\), \((3,13,2)\), \((4,16,1)\), \((5,49,4)\), \((8,64,1)\), \((9,193,8)\), and \((16,256,1)\).

## Assumptions and scope

The alphabet is \(\{0,1\}\); factors are finite contiguous blocks starting at nonnegative integer positions. All one-positions are ordered increasingly, starting at \(E_b(0)=0\). An Abelian class is determined by the number of ones. The base assumption \(b\ge4\) specifies the new infinite family; the proofs also hold when \(b=3\), the classical Cantor case, for which maximum-weight and Abelian-complexity statements were previously studied. The bitwise operation \(\mathbin{\&}\) is on nonnegative integers. The empty factor is not counted in Abelian complexity.

## Proof

**1. Carry identity and exact equality.** In binary addition of integers \(u,v\ge0\), let \(c_r\in\{0,1\}\) indicate a carry from bit \(r\) to bit \(r+1\). If \(u_r,v_r,d_r\in\{0,1\}\) are the input and output bits, the column equation is \(u_r+v_r+c_{r-1}=d_r+2c_r\), with \(c_{-1}=0\). Multiply by \((b-1)b^r\), sum all columns and rearrange to obtain the exact finite carry formula
\[
E_b(u+v)-E_b(u)-E_b(v)
=(b-1)(b-2)\sum_{r\ge0}c_rb^r.
\]
It follows that \(E_b\) is superadditive, and equality holds precisely when no binary carry occurs, or equivalently when \(u\mathbin{\&}v=0\). All coefficients are strictly positive because \(b\ge4\).

**2. Threshold and permitted starts.** Suppose an interval of length \(n\) contains at least \(k\) ones. Select its first \(k\) ones; they occur at \(E_b(i),\ldots,E_b(i+j)\) for some \(i\ge0\). By the carry identity,
\[
n-1\ge E_b(i+j)-E_b(i)\ge E_b(j).
\]
Therefore \(n\ge L_b(k)\). The prefix of length \(L_b(k)\) contains the first \(k\) ones and no further one, so the bound is attained. At equality \(n=L_b(k)\), both inequalities must be equalities. The start of the interval must be \(E_b(i)\), and the carry identity forces \(i\mathbin{\&}j=0\). Conversely any \(i\) satisfying that condition gives \(E_b(i+j)-E_b(i)=E_b(j)\), so the length-\(L_b(k)\) block beginning at \(E_b(i)\) contains exactly the consecutive \(k\) ones. The previously established minimum for \(k+1\) ones prohibits an extra one.

**3. Classification and injectivity.** Put \(h=\lceil\log_2 k\rceil\), so \(0\le j<2^h\). Every admissible \(i\) decomposes uniquely as \(i=a+2^ht\) with \(0\le a<2^h\), \(a\mathbin{\&}j=0\), and \(t\ge0\). Since the bits of \(a\) and \(j\) are disjoint, \(a+j=a\mathbin{|}j<2^h\), and hence \(a+r<2^h\) for every \(0\le r\le j\). Thus
\[
E_b(i+r)=E_b(a+r)+b^hE_b(t),\qquad
E_b(i)=E_b(a)+b^hE_b(t).
\]
Subtracting proves that the factor depends only on the allowed residue \(a\), and that each residue gives infinitely many occurrences as \(t\) varies.

It remains to show distinct residues give distinct words. For \(k=1\) there is only the residue zero. Assume \(k\ge2\) and let \(a\ne a'\) be two allowed residues. Let \(q<h\) be the least bit in which they differ. Their residues modulo \(2^q\) agree. Set \(r=2^q-(a\bmod2^q)\), where this gives \(r=2^q\) when the remainder is zero. Then \(1\le r\le2^q\le j\), and \(a+r\) and \(a'+r\) are divisible by \(2^q\) but have opposite bits at position \(q\). Consequently one has \(2\)-adic valuation exactly \(q\), and the other has valuation strictly greater than \(q\). Directly from the binary digit expansion,
\[
E_b(s)-E_b(s-1)=(b-2)b^{\nu_2(s)}+1\qquad(s\ge1).
\]
The consecutive-one gap between offsets \(r-1\) and \(r\) in the two words is therefore different, so the factors are distinct. Exactly \(h-s_2(j)\) low binary digits of \(a\) are free, giving \(H_b(k)=2^{h-s_2(j)}\). The final threshold-jump identities follow by substituting \(j=2^m-1\) and \(j=2^m\), respectively.

**4. Prefix normality and Abelian complexity.** For an arbitrary length \(n\), let \(k\) be the number of one-positions \(E_b(j)\) smaller than \(n\). The argument in step 2 shows that no length-\(n\) interval can have \(k+1\) ones. Thus the prefix is maximum-weight. Since
\[
E_b(2^m)-E_b(2^m-1)=(b-2)b^m+1\longrightarrow\infty,
\]
there are arbitrarily long all-zero factors, so the minimum weight at each fixed length is zero. Slide the length-\(n\) window from the prefix to a long zero run: its weight changes by at most one each step, hence every integer weight from zero to \(k\) occurs. Therefore the number of Abelian classes is exactly \(k+1\), as claimed.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter. The verifier generates each finite generalized-Cantor prefix directly from base-\(b\) digits, separately derives the predicted threshold patterns from binary-to-base encoding, enumerates every window and compares the complete distinct maximum-weight pattern sets. It also verifies that one symbol fewer cannot contain \(k\) ones and checks many maximizing start positions. The included check ran successfully on 102 base-and-threshold cases for bases \(3\) through \(7\), including 364 distinct predicted pattern instances and 465 checked starting positions. The base-\(3\) cases are a benchmark only. These are finite confirmations; the all-length conclusion rests on the explicit carry and injectivity arguments above.

## Relationship to prior work

Chen, Lü and Wu's work [1] proves the maximal-weight prefix property for the classical base-\(3\) Cantor word (Lemma 2) and derives its Abelian-complexity recurrence (Proposition 1). The present finding does **not** claim those classical base-\(3\) results as novel. Its new statement concerns the complete threshold-heavy word classification, the exact count \(2^{h-s_2(j)}\), and the unrestricted base family \(b\ge4\). The paper's base-\(3\) gap recurrences do not state the complete distinct maximizing-factor profile for every base.

Cicalese, Lipták and Rossi [2] study prefix-normal infinite words and the general connection to Abelian complexity. They do not compute this generalized Cantor family's threshold-heavy factor multiplicities. Lü, Chen and Wen [3] prove regularity assertions for \(2\)-Abelian complexity of generalized Cantor sequences under assumptions; the publication abstract was accessible, but its full text could not be inspected. That produces a residual coverage risk, especially for ancillary Abelian-complexity assertions, but the exact threshold-factor classification is not stated in the available material. The new distinction concerns ordinary distinct words of extremal weight, not merely their common Parikh vector.

## Limitations

The complete theorem is for the explicit two-digit-support Cantor family \(b\ge4\); it does not classify all generalized Cantor substitutions or all words sharing their Abelian profiles. It counts **distinct factors** at the first length attaining weight \(k\), not the number of occurrences or all maximal-weight factors at arbitrary lengths. An unindexed or inaccessible equivalent source could affect originality; no independent external audit has been conducted. The finite test range does not independently certify the infinite theorem.

## References

[1] J. Chen, X. Lü and W. Wu, *On the \(k\)-Abelian Complexity of the Cantor Sequence*, arXiv:1703.04063 (first public version March 12, 2017), https://arxiv.org/abs/1703.04063.

[2] F. Cicalese, Z. Lipták and M. Rossi, *On Infinite Prefix Normal Words*, arXiv:1811.06273 (first public version November 15, 2018), https://arxiv.org/abs/1811.06273; journal DOI: 10.1016/j.tcs.2021.01.015.

[3] X.-T. Lü, J. Chen and Z.-X. Wen, *On the 2-Abelian Complexity of Generalized Cantor Sequences*, Theoretical Computer Science **936** (2022), 172–183, https://doi.org/10.1016/j.tcs.2022.09.025.
