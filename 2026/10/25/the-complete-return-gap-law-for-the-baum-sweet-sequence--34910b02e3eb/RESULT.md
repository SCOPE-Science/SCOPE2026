# The complete return-gap law for the Baum–Sweet sequence

## Finding
Let \(b_0=1\) and, for \(n>0\), let \(b_n=1\) precisely when every maximal zero run in the ordinary base-two expansion of \(n\) has even length. Write its support as \(0=s_0<s_1<s_2<\cdots\). For each integer \(K\ge1\), let \(N_K(g)\) be the number of adjacent support pairs \((s_j,s_{j+1})\) with \(s_{j+1}<2^K\) and difference \(g\).

Let \(F_0=0,F_1=1,F_{r+2}=F_{r+1}+F_r\). For \(m\ge2\), put \(G_m=2^{m-2}+1+\mathbf1_{2\mid m}\). The **complete exact gap histogram** is
\[
N_K(g)=\mathbf1_{g=1}\left\lfloor\frac{K+1}{2}\right\rfloor+\mathbf1_{g=2}\left\lfloor\frac K2\right\rfloor+\sum_{m=2}^{K-1}\mathbf1_{g=G_m}\big(F_{K-m+2}-1\big).
\]
In particular, the infinite return-gap spectrum is exactly \(\{1,2,3,6,9,18,33,66,129,258,\ldots\}\), where \(G_2=G_3=3\) and \(G_m\) is strictly increasing for \(m\ge3\). There are \(F_{K+2}-1\) total gaps in the dyadic prefix.

Define \(P_K(g)=N_K(g)/(F_{K+2}-1)\), and let \(\varphi=(1+\sqrt5)/2\). The pointwise limiting mass function along dyadic prefixes is
\[
P(1)=P(2)=0,\qquad P(3)=\varphi^{-1},\qquad P(G_m)=\varphi^{-m}\quad(m\ge4),
\]
with mass zero elsewhere. It sums to one and has exact tail \(\Pr\{G\ge G_m\}=\varphi^{2-m}\) for every \(m\ge4\). Since \(G_m\asymp2^m\), the limiting law has a power-law tail exponent \(\log_2\varphi\) and infinite mean.

## Assumptions and scope
The canonical binary expansion of each positive integer has no leading zeros; \(0\) is included in the support by convention. A *gap* means the **difference** of consecutive support indices, so a gap of \(g\) corresponds to \(g-1\) zeros between two ones. The finite histogram counts gaps whose **both endpoints** belong to \([0,2^K)\). The limiting probability is the empirical distribution of the \(F_{K+2}-1\) gaps in this prefix as \(K\to\infty\); it is not claimed to be the spatial density of fixed gap types among all integer sites. Every stated equality is valid for all specified integer parameters.

## Proof
**1. Finite suffix language.** The valid canonical positive binary strings are exactly \(1(1\mid00)^*\). Let \(V_m\) be the increasing list of values of all strings of length \(m\) in \((1\mid00)^*\), viewed as binary integers and permitting initial `00` tokens. Then \(V_0=(0)\), \(V_1=(1)\), and, for \(m\ge2\), the ordered concatenation identity is
\[
V_m=V_{m-2}\;\Vert\;(2^{m-1}+V_{m-1}).
\]
Indeed a valid length-\(m\) token string starts with `00` or with `1`; strings of the first form have leading numerical zeroes, and their values are smaller than all numbers of the second form. Consequently, \(|V_m|=F_{m+1}\). The minimum of \(V_m\) is zero for even \(m\) and one for odd \(m\); the maximum is \(2^m-1\). These claims hold at \(m=0,1\) and follow inductively from the displayed split.

**2. Internal gaps.** Let \(W_m\) be the ordered list of successive differences within \(V_m\), with \(W_0,W_1\) empty. The unique difference between the two concatenated lists in the preceding identity is
\[
(2^{m-1}+\min V_{m-1})-\max V_{m-2}
=2^{m-2}+1+\mathbf1_{2\mid m}=G_m.
\]
Thus, as an exact concatenation of gap lists,
\[
W_m=W_{m-2}\;\Vert\;(G_m)\;\Vert\;W_{m-1}.
\]
Repeatedly expanding the token prefix of a length-\(\ell\) admissible word shows that the internal bridge \(G_m\) is produced once for each admissible prefix of token-bit length \(\ell-m\). There are \(F_{\ell-m+1}\) such prefixes for \(\ell\ge m\). This identity also follows by induction from the recurrence for \(W_m\), checking the bridge term \(\ell=m\).

**3. All binary lengths and boundary gaps.** The positive support elements with exactly \(L\) binary digits form, in increasing order, \(2^{L-1}+V_{L-1}\). Therefore the internal differences among those elements contribute \(F_{L-m}\) instances of \(G_m\) if \(L\ge m+1\), and none otherwise. Summing over \(1\le L\le K\) yields
\[
\sum_{L=m+1}^{K}F_{L-m}=F_{K-m+2}-1.
\]
The final element having \(L\) digits is \(2^L-1\), and the first having \(L+1\) digits is \(2^L+\mathbf1_{L\text{ odd}}\). Hence the boundary difference between digit lengths \(L\) and \(L+1\) is \(1+\mathbf1_{L\text{ odd}}\). Adding the initial gap \(0\to1\), among the \(K\)-bit prefix there are \(\lfloor(K+1)/2\rfloor\) gap-one boundaries and \(\lfloor K/2\rfloor\) gap-two boundaries. This proves the histogram. Moreover, the positive support count is \(\sum_{L=1}^K F_L=F_{K+2}-1\), and including zero yields \(F_{K+2}\) support positions.

**4. Spectrum and limit.** For every fixed \(m\ge2\), an internal bridge of size \(G_m\) occurs already for length \(m+1\) positive support strings; the boundary gaps also occur. Conversely the two recursion formulas exhaust all gap types. Here \(G_2=G_3=3\), and all other bridge sizes are distinct and exceed three. Using \(F_{K-r}/F_K\to\varphi^{-r}\) gives the asserted masses. Their sum is
\[
\varphi^{-2}+\varphi^{-3}+\sum_{m=4}^{\infty}\varphi^{-m}=1.
\]
The geometric-series identity gives the exact tail \(\sum_{j=m}^\infty\varphi^{-j}=\varphi^{2-m}\). The inequalities \(2^{m-2}\le G_m\le2^{m-2}+2\), together with \(2/\varphi>1\), give the stated tail exponent and divergence of the mean. This completes the proof.

## Verification
The included `verify.py` checks each complete dyadic-prefix support set for \(1\le K\le15\) by two independent algorithms: direct inspection of binary zero-run lengths, and generation from the token-language recurrence. It recomputes every exact gap histogram and each bridge recurrence, as well as numerical convergence at \(K=19\). These checks are finite corroboration; the unrestricted theorem follows from the preceding symbolic proof. Execute `python3 verify.py` using only the Python standard library.

## Relationship to prior work
The binary zero-run definition of the Baum–Sweet sequence is classical; the support appears explicitly as OEIS A060142 (Clark Kimberling, March 5, 2001), using the equivalent closure rules \(0\in S\), \(s\in S\Rightarrow2s+1,4s\in S\). That source already identifies the support and a Fibonacci-word pattern in a distinguished subsequence; neither the support nor its Fibonacci relation is claimed to be new. The contribution here is the **all-scale histogram for every return-gap value and its limiting heavy-tailed law**, derived from the known support language. OEIS A086747 is the corresponding binary indicator with a differing initial-index convention. The cited sources and available research-record summaries did not supply this particular histogram or law. A published equivalent gap enumeration not surfaced in the inspections would remove the originality claim.

## Limitations
The result concerns the canonical Baum–Sweet sequence, not arbitrary automatic sequences or gap correlations among successive returns. The limiting law samples gaps uniformly in dyadic prefixes, not sites uniformly in the integer axis. The exact histogram is elementary to calculate *once* the token decomposition is found, and priority over unindexed historical computations is not independently established. Independent mathematical review has not been conducted.

## References
1. Clark Kimberling, OEIS A060142, *Ordered set S defined by these rules: 0 is in S and if x is in S then 2x+1 and 4x are in S*, first recorded March 5, 2001. https://oeis.org/A060142
2. OEIS A086747, *Baum–Sweet sequence*, https://oeis.org/A086747
3. Jean-Paul Allouche and Jeffrey Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, Cambridge University Press, 2003; background on Baum–Sweet automaticity.
