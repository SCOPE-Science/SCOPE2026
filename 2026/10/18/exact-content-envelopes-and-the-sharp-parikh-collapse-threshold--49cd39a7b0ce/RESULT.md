# Exact content envelopes and the sharp Parikh-collapse threshold for jumbled Simon equivalence

## Finding

Fix an alphabet \(\Sigma=\{a_1,\ldots,a_q\}\) with \(q\ge1\), an integer \(k\ge1\), and write \(p(w)=(|w|_{a_1},\ldots,|w|_{a_q})\) for the Parikh vector of a word. For words \(u,w\), \(\operatorname{LCS}(u,w)\) denotes the length of their longest common scattered subsequence. A word \(u\) is an \(\ell\)-jumbled scattered factor of \(w\) when \(p(u)\le p(w)\) componentwise and \(|u|-\operatorname{LCS}(u,w)\le\ell\). Let \(J_{\le k}(w,\ell)\) be the set of such factors of length at most \(k\), and define \(w\sim^J_{k,\ell}v\) when \(J_{\le k}(w,\ell)=J_{\le k}(v,\ell)\).

**Main theorem, part I (exact content envelope).** For a content vector \(\mathbf c=(c_1,\ldots,c_q)\in\mathbb N_0^q\), let
\[
\rho_k(w)=\max_{\substack{p(u)\le p(w)\\|u|\le k}}\bigl(|u|-\operatorname{LCS}(u,w)\bigr),
\]
where the empty pattern is allowed. Define \(F_k(\mathbf 0)=0\) and, for \(\mathbf c\ne\mathbf0\),
\[
F_k(\mathbf c)=\max_{1\le h\le\min(k,\max_i c_i)}
\left(\min\left\{k,\sum_{i=1}^q\min(c_i,h)\right\}-h\right).
\]
Then, **for every** \(\mathbf c\),
\[
\boxed{\max_{w:p(w)=\mathbf c}\rho_k(w)=F_k(\mathbf c).}
\]
Every block-sorted word \(a_1^{c_1}a_2^{c_2}\cdots a_q^{c_q}\) attains this maximum (and so does any permutation of its block order).

**Main theorem, part II (sharp equivalence-index transition).** Put
\[
\ell_*(q,k)=k-\left\lceil\frac{k}{q}\right\rceil.
\]
For every integer \(\ell\ge0\),
\[
\boxed{\bigl|\Sigma^*/{\sim^J_{k,\ell}}\bigr|=(k+1)^q
\quad\Longleftrightarrow\quad\ell\ge\ell_*(q,k).}
\]
When \(\ell\ge\ell_*(q,k)\), the equivalence relation is exactly equality of **capped Parikh vectors** \(p_k(w)=(\min(|w|_{a_i},k))_{i=1}^q\); in particular the signature has \((k+1)^q\) possible values. When \(0\le\ell<\ell_*(q,k)\), its index is strictly larger than \((k+1)^q\). The case \(q=1\) has \(\ell_*=0\) and no subthreshold regime. For example, at \(q=2\), \(k=4\), the index already reaches \(25\) at budget \(\ell=2\), before the known sufficient budget \(k-1=3\). With \(k=50\) and content \((100,1,1)\), the exact content envelope is only \(2\), whereas the worst-case three-letter threshold is \(33\).

## Assumptions and scope

All words are finite, including the empty word, and all counts are nonnegative integers. The empty pattern contributes zero to \(\rho_k\). The alphabet is fixed and ordered only to display sorted witnesses. The inequality \(p(u)\le p(w)\) is essential: LCS alone without this feasibility condition would define a different language. The result concerns the jumbled **scattered-subsequence** model, not contiguous jumbled substring indexing or Parikh-matrix equivalence. The relation above uses *all pattern lengths at most* \(k\); it is not the relation defined only by patterns of length exactly \(k\).

## Proof

**Lemma 1 (uniform host-independent bound).** Let \(u\) be an admissible pattern for a host \(w\) of content \(\mathbf c\), with \(|u|\le k\). For \(u\ne\varepsilon\), set \(h=\max_i |u|_{a_i}\). Since \(p(u)\le\mathbf c\), the host contains at least \(h\) copies of whichever letter realizes this maximum. These \(h\) copies form a common subsequence; hence \(\operatorname{LCS}(u,w)\ge h\). Also \(0<h\le\min(k,\max_i c_i)\), and
\[
|u|=\sum_i |u|_{a_i}\le\min\left(k,\sum_i\min(c_i,h)\right).
\]
Consequently \(|u|-\operatorname{LCS}(u,w)\le F_k(\mathbf c)\). The empty pattern has deficit zero. This proves \(\rho_k(w)\le F_k(\mathbf c)\) for *every* host ordering.

**Lemma 2 (matching reversed-block pattern).** Let \(w_0=a_1^{c_1}\cdots a_q^{c_q}\). Fix \(h\) from the maximizing range in the formula and put \(B_i=\min(c_i,h)\), \(T=\min(k,\sum_i B_i)\). Because some \(c_i\ge h\), one of the \(B_i\) is \(h\), and \(h\le T\le\sum_i B_i\). Choose integers \(0\le v_i\le B_i\) with \(\sum_i v_i=T\) and \(\max_i v_i=h\): first set one coordinate with \(B_i=h\) equal to \(h\), then distribute the remaining \(T-h\) units among the other coordinates up to their capacities. Such a distribution exists by \(T\le\sum_i B_i\). Set \(u=a_q^{v_q}\cdots a_1^{v_1}\). This is Parikh-feasible and has length \(T\le k\). Every common scattered subsequence of the forward-sorted \(w_0\) and reverse-sorted \(u\) uses only a *single* letter, since the order of any two distinct letters is reversed. Thus
\[
\operatorname{LCS}(u,w_0)=\max_i v_i=h,
\quad |u|-\operatorname{LCS}(u,w_0)=T-h.
\]
Taking the maximizing \(h\) and applying Lemma 1 proves the exact content-envelope formula. For \(\mathbf c=\mathbf0\), both sides are zero.

**Lemma 3 (global sharp envelope).** For any feasible nonempty \(u\) of length \(m\le k\), its most frequent letter occurs at least \(\lceil m/q\rceil\) times. Thus
\[
m-\operatorname{LCS}(u,w)\le m-\left\lceil m/q\right\rceil\le k-\left\lceil k/q\right\rceil,
\]
where the last inequality follows from monotonicity of \(m-\lceil m/q\rceil\) on nonnegative integers. Hence at budgets \(\ell\ge\ell_*\), membership in \(J_{\le k}(w,\ell)\) is **equivalent** to the componentwise Parikh-feasibility test. For all feasible patterns of length at most \(k\), feasibility is determined entirely by \(p_k(w)\).

**Lemma 4 (exact index and sharpness).** At *every* budget \(\ell\ge0\), the pure-letter probes \(a_i^r\), \(1\le r\le k\), belong to \(J_{\le k}(w,\ell)\) exactly when \(|w|_{a_i}\ge r\). They distinguish all distinct capped Parikh vectors, yielding at least \((k+1)^q\) equivalence classes. Lemma 3 yields equality for \(\ell\ge\ell_*\). Conversely suppose \(\ell<\ell_*\); then \(q,k\ge2\) and \(k>1\). Let \(r=\min(q,k)\) and take positive integers \(d_1,\ldots,d_r\) totaling \(k\) and differing by at most one (so \(\max_i d_i=\lceil k/r\rceil=\lceil k/q\rceil\)); assign zero copies to the remaining letters. Consider the two opposite-order block words
\[
w=a_1^{d_1}\cdots a_r^{d_r},\qquad v=a_r^{d_r}\cdots a_1^{d_1}.
\]
They have identical full Parikh vectors. Nonetheless, \(v\in J_{\le k}(v,\ell)\), whereas \(v\notin J_{\le k}(w,\ell)\), because \(\operatorname{LCS}(v,w)=\max_i d_i=\lceil k/q\rceil\) and \(|v|-\operatorname{LCS}(v,w)=\ell_*>\ell\). One capped-Parikh class therefore splits into at least two jumbled-Simon equivalence classes. Since no classes with different capped vectors can merge, the index is strictly greater than \((k+1)^q\). This proves the threshold theorem for all \(q,k,\ell\).

## Verification

The standalone standard-library program `checker.py` enumerates host words and feasible patterns independently, computes LCS using the two-row dynamic-programming recurrence, checks the sharp index-collapse budget on all tested pairs, and verifies that sorted hosts attain the exact content envelope. Running `python3 checker.py` reproduces the embedded `checker_output.txt`. Its printed summary is 191852 host-pattern plateau checks and 34188 content-envelope checks, across the finite ranges described in the output. The proof above, not finite enumeration, establishes the claims for all integer parameters. No external libraries, downloaded datasets, or unembedded dependencies are required.

## Relationship to prior work

Fleischmann, Huch, Kammholz, and Koß (2025, arXiv:2506.03814, initial public posting 2025-06-04) introduced the jumbled scattered-factor model, its relation to longest common scattered subsequences, and the corresponding Simon equivalence; they left a finer classification and index determination as directions for future research. The new theorem determines the exact *worst host order* for every Parikh content and the exact budget above which the entire quotient loses ordering information.

Fleischmann, Huch, Kim, Koß, and Wiards (2026, arXiv:2610.17910, subsequently posted on 2026-10-13) clarified the nonnegative-budget definition and established the capped-Parikh characterization and index \((k+1)^q\) for the special choice \(\ell=k-1\). The theorem above identifies the earliest possible threshold \(\ell_*=k-\lceil k/q\rceil\), generally strictly smaller than \(k-1\), proves its necessity, and supplies a content-dependent envelope not implied by that special case. In the original 2025 convention the empty pattern's membership needs separate treatment; this does not alter the nonempty witnesses or any equivalence-index conclusion, because the empty pattern has the same fixed status for every host.

The result is not an algorithmic claim about the minimum DFA/NFA recognizing each class, nor a claim for ordinary Simon congruence. Published equivalent work not retrieved by the searches remains possible.

## Limitations

Only the threshold and the full Parikh-collapse regime are classified: no closed formula is claimed for the number of classes at any subthreshold budget. The formula \(F_k\) is a worst-case **over host orderings with fixed content**; it need not equal \(\rho_k(w)\) for every host ordering. No independent human audit is claimed. Priority assessment is bounded by the literature and mathematical-record searches described in the accompanying review.

## References

1. P. Fleischmann, A. Huch, M. Kammholz, T. Koß, *Jumbled Scattered Factors*, arXiv:2506.03814v1 (2025-06-04). https://arxiv.org/html/2506.03814v1
2. P. Fleischmann, A. Huch, S. Kim, T. Koß, E. Wiards, *Jumbled Simon’s Equivalence and Embeddings*, arXiv:2610.17910v1 (2026-10-13); subsequently published preprint for comparison only. https://arxiv.org/html/2610.17910v1
