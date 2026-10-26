# Exact mean and Gaussian fluctuations of two-deletion ambiguity in sliding-window read channels

## Finding
Let \(q\ge 2\) and \(\ell\ge 2\) be fixed integers, let \(n\ge\ell+1\), and draw \(X=(X_1,\ldots,X_n)\) uniformly from the \(q\)-ary words. Set \(m=n-\ell+1\) and read the overlapping \(\ell\)-mers \(Y_i=(X_i,\ldots,X_{i+\ell-1})\), for \(1\le i\le m\). Let \(Z\) be the number of **distinct** length-\(m-2\) sequences of \(\ell\)-mers obtainable by deleting exactly two positions of \(Y\), counting a common output only once. Then, for every \(n\ge\ell+1\),

\[
\boxed{\mathbb EZ=\binom m2-m(m-2)q^{-\ell}
 +\sum_{d=1}^{m-2}(m-1-d)q^{-\ell-\min(d,\ell)}.}
\]

For the fixed parameters \(q,\ell\), put \(p=q^{-\ell}\) and
\[
 v_{q,\ell}=p(1-p)+2\sum_{d=1}^{\ell-1}
 \bigl(q^{-(\ell+d)}-q^{-2\ell}\bigr)>0.
\]
Then, as \(n\to\infty\) with \(m=n-\ell+1\),
\[
\boxed{\frac{Z-\mathbb EZ}{m^{3/2}}\ \xrightarrow{\mathrm d}\
\mathcal N\bigl(0,(1-p)^2v_{q,\ell}\bigr),\qquad
\lim_{n\to\infty}\frac{\operatorname{Var}(Z)}{m^3}=(1-p)^2v_{q,\ell}.}
\]
For a four-symbol alphabet and two-symbol read window the limiting normalized variance is exactly \(4725/65536\). The positive covariance corrections in \(v_{q,\ell}\) measure dependence between *overlapping* constant-window indicators; they are not present in the independent-run calculation for unconstrained uniformly sampled read symbols.

## Assumptions and scope
The input symbols \(X_i\) are independent and uniform on a fixed alphabet of size \(q\); the read list \(Y\) is the **noncyclic, unguarded** sliding-window sequence of all consecutive length-\(\ell\) substrings. Two entries of this list are deleted at distinct positions, with no replacement, and output sequences are distinguished by their ordered lists of whole \(\ell\)-mers. The alphabet of read symbols has size up to \(q^\ell\), but overlapping reads are correlated and cannot be treated as independent. The minimum list length \(m=2\) is allowed; then the only output is the empty list and \(Z=1\). No fixed adapter sequences or protected endpoint reads are assumed. The result is a statement about the number of possible *distinct adversarial outputs* over random input centers, not a probability distribution on deletion positions or an error-correcting code-rate bound.

## Proof
**1. A deterministic two-deletion counting identity.** For an arbitrary sequence \(y=(y_1,\ldots,y_m)\) over any alphabet, let \(R\) be its number of maximal constant runs, \(H\) the number of runs of length at least two, and \(T=\#\{i\in\{1,\ldots,m-2\}: y_i=y_{i+2}\ne y_{i+1}\}\). We prove
\[
|\mathcal D_2(y)|=\binom R2+H-T.\tag{1}
\]
Associate each distinct descendant with its unique **leftmost subsequence embedding**, hence with its canonical pair of deleted positions. If the deleted positions are nonadjacent, each must be the last element of its run: otherwise the next retained copy of the same symbol makes the embedding non-leftmost. Conversely, any two nonadjacent run ends give a leftmost embedding. Write \(e_i=\mathbf 1\{y_i\ne y_{i+1}\}\) for \(1\le i<m\) and \(e_m=1\). There are \(R\) run ends, and among the \(\binom R2\) unordered pairs exactly \(U=\sum_{i=1}^{m-1}e_ie_{i+1}=R-H-e_1\) are adjacent. Thus the nonadjacent canonical masks number \(\binom R2-U\).

If the deleted positions are adjacent, the final two positions always give a leftmost embedding. Deleting \(i,i+1\) with \(i\le m-2\) does so precisely when the next retained symbol \(y_{i+2}\) differs from both deleted symbols. Hence the number of adjacent canonical masks is
\[
A=1+\sum_{i=1}^{m-2}\mathbf1\{y_{i+2}\notin\{y_i,y_{i+1}\}\}
=1+\sum_{i=2}^{m-1}e_i-T=R-e_1-T.
\]
Adding the two cases gives (1). This canonical-embedding proof works for any alphabet and verifies all boundary cases including \(m=2\).

**2. Dependence induced by overlapping reads.** The event \(Y_i=Y_{i+1}\) is equivalent to \(X_i=X_{i+1}=\cdots=X_{i+\ell}\). Define \(C_i=\mathbf1\{Y_i=Y_{i+1}\}\) for \(1\le i\le m-1\) and \(S=\sum_i C_i\), so \(R=m-S\). Uniform independence gives
\[
\mathbb EC_i=p=q^{-\ell},\qquad
\mathbb E(C_iC_{i+d})=q^{-\ell-\min(d,\ell)}
\quad(1\le d\le m-2).\tag{2}
\]
For \(d<\ell\) the two constant-block events merge into one block, whereas for \(d\ge\ell\) their joint probability is \(p^2\). In particular,
\[
\mathbb E\binom R2=\binom m2-(m-1)^2p
+\sum_{d=1}^{m-2}(m-1-d)q^{-\ell-\min(d,\ell)}.\tag{3}
\]

A run of \(Y\) with length at least two either starts at its first entry, contributing probability \(p\), or starts at a position with a transition followed by a repeat. For each interior position this latter probability is \(p-q^{-(\ell+1)}\). Hence
\[
\mathbb EH=p+(m-2)\bigl(p-q^{-(\ell+1)}\bigr).
\]
The event \(Y_i=Y_{i+2}\ne Y_{i+1}\) imposes period two on \(\ell+2\) underlying symbols but excludes their all-equal case, so its probability is also \(p-q^{-(\ell+1)}\), and
\[
\mathbb ET=(m-2)\bigl(p-q^{-(\ell+1)}\bigr).
\]
Thus \(\mathbb E(H-T)=p\) **exactly**, with no asymptotic approximation. Combining this cancellation with (1) and (3) proves the stated expectation formula.

**3. Fluctuations.** Each \(C_i\) depends only on the underlying letters \(X_i,\ldots,X_{i+\ell}\), making the sequence stationary and finitely dependent with dependence range at most \(\ell\). Equation (2) implies
\[
\frac{\operatorname{Var}(S)}m\longrightarrow
v_{q,\ell}=p(1-p)+2\sum_{d=1}^{\ell-1}(q^{-(\ell+d)}-p^2),
\]
where all summands after the first are nonnegative and \(p(1-p)>0\). The central limit theorem for bounded stationary finitely dependent variables gives \((S-\mathbb ES)/\sqrt m\xrightarrow{\mathrm d}\mathcal N(0,v_{q,\ell})\).

Write \(\Delta=S-\mathbb ES\) and \(\mu_R=\mathbb ER=m-(m-1)p\). Expanding the quadratic in (1),
\[
Z-\mathbb EZ=-(\mu_R-\tfrac12)\Delta
 +\tfrac12(\Delta^2-\mathbb E\Delta^2)
 +\bigl[(H-T)-\mathbb E(H-T)\bigr].\tag{4}
\]
The latter bracket is a sum of bounded local functions of at most \(\ell+2\) consecutive input letters, so its variance is \(O_{q,\ell}(m)\). Bounded finite-dependence also yields \(\mathbb E\Delta^4=O_{q,\ell}(m^2)\). Thus the two remainder terms in (4) have second moments \(O_{q,\ell}(m^2)\), so divided by \(m^{3/2}\) they vanish in \(L^2\). Since \((\mu_R-1/2)/m\to1-p\), the asserted normal limit follows by Slutsky's theorem, and the second-moment control yields the stated asymptotic variance.

## Verification
The companion `verify_window_two_deletion.py` builds the actual list of overlapping reads, enumerates and deduplicates every output after deleting each of the \(\binom m2\) position pairs, and independently computes the run/alternation formula. It exhaustively checks \(294{,}061\) input words in \(48\) complete parameter grids with \(q\in\{2,3,4\}\), \(\ell\in\{2,3,4\}\), and \(\ell+1\le n\le 9\) for binary and \(n\le8\) otherwise. For each grid it compares the exact rational mean against the formula above. It separately checks positivity of the asymptotic variance coefficient for \(16\) combinations with \(2\le q,\ell\le5\), and checks \(q=4,\ell=2\) against \(4725/65536\). Run with `python3 verify_window_two_deletion.py`; the recorded output ends in `VERIFY_OK`. These finite experiments check implementations of the identities, not the all-length CLT proof.

## Relationship to prior work
Xie and Chen (first public version 2026-01-29) study deletion and edit correction after a sliding-window inter-symbol-interference channel, with known adapters and protected endpoint reads, and establish code redundancy bounds and constructions. Their theorem concerns coding rates; the present result instead concerns the exact two-deletion output-volume expectation and its limiting law for an unguarded i.i.d. read list. No coding-rate improvement or result for fixed adapters is claimed. Chee and coauthors' locally-constrained de Bruijn codes cover sequence enumeration under nearby read-repetition restrictions; this is a different question from mean and fluctuation of the number of distinct exact-two-deletion outputs. Swart and Ferreira's classical double-deletion subsequence counts, the published binary variance calculation, and an earlier all-alphabet independent-word mean/variance calculation concern uniformly sampled *read symbols*, not the strongly correlated sequence of overlapping length-\(\ell\) reads. The all-alphabet independent-word calculation is explicitly excluded from the novelty claim. Abbasian, Mirmohseni, and Nasiri Kenari study mixed edit-error ball sizes in original DNA words; their mixed-channel results do not supply this sliding-read law. These distinctions are by object and conclusion, not just vocabulary. Published equivalence or a stronger general formula not identified in the accessible searches remains possible.

## Limitations
The source strand is uniformly i.i.d., the window length and alphabet are fixed as length grows, and there are exactly two read deletions. In particular, this does **not** analyze arbitrary input distributions, fixed adapters, deletions from specified protected positions, other error types, or the probability of a randomly sampled deletion mask. The theorem gives an exact mean and an asymptotic Gaussian law with variance constant, not an exact finite-length variance or a full discrete sphere-volume distribution. An independent scientific audit has not been performed.

## References
1. H. Xie and Z. Chen, “Deletion-correcting codes for an adversarial nanopore channel,” initial arXiv version 2026-01-29; subsequently titled “First-order optimal codes for an adversarial nanopore channel,” arXiv:2601.21236 (version 3, 2026-06-17), https://arxiv.org/abs/2601.21236.
2. Y. M. Chee, T. Etzion, H. M. Kiah, S. Marcovich, A. Vardy, V. K. Vu, and E. Yaakobi, “Locally-Constrained de Bruijn Codes: Properties, Enumeration, Code Constructions, and Applications,” *IEEE Trans. Inf. Theory* **67** (2021), 7857–7870, DOI:10.1109/TIT.2021.3112300.
3. T. G. Swart and H. C. Ferreira, “A note on double insertion/deletion correcting codes,” *IEEE Trans. Inf. Theory* **49** (2003), 269–273, DOI:10.1109/TIT.2002.806155.
4. A. Abbasian, M. Mirmohseni, and M. Nasiri Kenari, “On the size of error ball in DNA storage channels,” arXiv:2410.15290 (2024-10-20), https://arxiv.org/abs/2410.15290.
