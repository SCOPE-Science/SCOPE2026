# The exact output-length spectrum and binomial volume law of a single substring edit

## Finding
Fix an integer alphabet size \(q\ge 2\) and integers \(n\ge k\ge 1\). A single \(k\)-substring edit replaces a consecutive substring of \(d\) letters of a center \(x\in\Sigma_q^n\) by an arbitrary word of \(i\) letters at the same position, allowing \(0\le d,i\le k\) and the empty word. Let \(E_k(x)\) be the set of distinct received words and let \(B_{k,\delta}(x)\) denote the subset of received length \(n+\delta\), for every integer \(-k\le\delta\le k\). Write \(r=n-k\), and put
\[
A_{q,n,k}=\bigl(q+r(q-1)\bigr)\frac{q^k-1}{q-1}
+q^{k-1}\left[kq+(q-1)\left(kr+\frac{k(k+1)}2\right)\right].
\]
All output-length layers are exactly as follows:
\[
|B_{k,\delta}(x)|=
\begin{cases}
1+\sum_{j=0}^{r-1}{\bf1}_{\{x_j\ne x_{j+k}\}},&\delta=-k,\\
q^{k+\delta-1}\bigl(q+r(q-1)\bigr),&-k<\delta\le0,\\
q^{k-1}\bigl(q+(r+\delta)(q-1)\bigr),&0<\delta\le k.
\end{cases}
\]
Indices on letters here start at zero; empty sums vanish. Thus
\[
|E_k(x)|=A_{q,n,k}+1+\sum_{j=0}^{r-1}{\bf1}_{\{x_j\ne x_{j+k}\}}.
\]
For a uniformly random center \(X\in\Sigma_q^n\), the complete finite-length distribution is
\[
|E_k(X)|\ \overset{d}{=}\ A_{q,n,k}+1+\mathrm{Bin}\left(r,\frac{q-1}{q}\right).
\]
In particular, exactly \(q^k\binom rj(q-1)^j\) centers have ball size \(A_{q,n,k}+1+j\), for \(0\le j\le r\). The exact mean is \(A_{q,n,k}+1+r(q-1)/q\), and the exact variance is \(r(q-1)/q^2\). Exactly \(q^k\) centers attain the minimum (those with period dividing \(k\)); exactly \(q^k(q-1)^r\) attain the maximum. At fixed \(q,k\), the centered, variance-normalized ball size converges to a standard Gaussian as \(n\to\infty\).

## Assumptions and scope
The input is a word of length \(n\ge k\ge1\) on any finite alphabet \(\Sigma_q\) with \(q\ge2\). One edit has both removed and inserted substring lengths at most \(k\), including zero, and **inserts at the same position** as the removal. Every possible received word is counted only once, even if multiple edit descriptions produce it. Unlike unrestricted deletion-followed-by-insertion balls, the inserted block may not move independently. No field structure on the alphabet is used. All formulas are exact for every admissible finite parameter, including \(n=k\), when the binomial random variable is degenerate. The Gaussian statement requires \(n-k\to\infty\) with \(q\) fixed.

## Proof
**1. Maximal-window reduction.** Fix a received-length difference \(\delta=i-d\). Any edit with \(d<d_{\max}=\min\{k,k-\delta\}\) can be expressed as a single replacement removing \(d_{\max}\) input letters and inserting \(d_{\max}+\delta\) letters: enlarge the removed block to a containing interval of length \(d_{\max}\) (possible because \(n\ge k\)), and insert the unchanged extra letters on the appropriate sides of the old replacement. The word produced is unchanged. Hence the entire \(\delta\) layer equals the ball for this maximal pair. For \(\delta=-k\), the maximal pair is \((k,0)\). For \(-k<\delta\le0\), it is \((k,k+\delta)\). For \(0<\delta\le k\), it is \((k-\delta,k)\).

**2. Fixed-pair replacement count with nonempty inserted block.** Fix \(0\le d\le n\) and \(i\ge1\). Let \(W_j\) be the set of words obtained by deleting \(d\) symbols at input position \(j\) and inserting any \(i\)-word there, for \(0\le j\le n-d\). The final window \(j=n-d\) has \(q^i\) outputs. For \(j<n-d\), an output at window \(j\) can be reproduced at a later window if and only if its first inserted symbol equals \(x_j\). The forward implication follows because every later window preserves the prefix through symbol \(x_j\). Conversely, if the first inserted symbol is \(x_j\), shift the window to \(j+1\) and shift the inserted block by one position, appending \(x_{j+d}\) at its end. Therefore window \(j\) contributes precisely \((q-1)q^{i-1}\) outputs whose **rightmost** possible window is \(j\). This gives exactly
\[
\left|\bigcup_{j=0}^{n-d}W_j\right|=q^i+(n-d)(q-1)q^{i-1}
=q^{i-1}\bigl(q+(n-d)(q-1)\bigr).
\]
All these outputs are distinct within their specified rightmost-window class, and the classes are disjoint. Apply this count to the maximal pairs from step 1 to obtain every layer except \(\delta=-k\).

**3. The sole varying layer.** Deleting a \(k\)-block at positions \(j\) and \(j+1\) yields the same word precisely when \(x_j=x_{j+k}\). More generally, the deletion outputs at positions \(a<b\) agree if and only if \(x_j=x_{j+k}\) for every \(a\le j<b\): compare the intervening portions of the two output words coordinate by coordinate. Thus the \(r+1\) ordered deletion windows form equivalence classes consisting of consecutive runs of equal deletion outputs, and their number is \(1+\sum_{j=0}^{r-1}{\bf1}_{\{x_j\ne x_{j+k}\}}\). This classical burst-deletion-run identity was established in earlier work and is used here as an ingredient, not claimed as new.

**4. Aggregation and full distribution.** Received lengths are disjoint. Summing the \(k\) fixed positive-insertion layers with \(\delta\le0\), the \(k\) layers with \(\delta>0\), and the pure-deletion layer gives \(A_{q,n,k}+1+\sum\mathbf1\) exactly as displayed. The graph on symbol positions with edges \((j,j+k)\), \(0\le j<r\), is a disjoint union of \(k\) paths, one for each residue class modulo \(k\). Choose the symbol at each path root in \(q\) ways. For each edge, an equality indicator allows one child symbol, while an inequality allows exactly \(q-1\) child symbols. Every selection of edge equality/inequality values therefore has exactly \(q^k(q-1)^j\) realizing centers when \(j\) edges differ. Choosing which \(j\) of the \(r\) edges differ yields the exact histogram. Uniform input makes the edge differences independent Bernoulli variables with parameter \((q-1)/q\), proving the binomial law, moments, extremizers, and the ordinary binomial central limit theorem.

## Verification
The standalone Python 3 program `substring_ball_verify.py` constructs every edit directly, collects received words into sets separately at each output length, and compares all shell sizes to the theorem. It further checks the **full population histogram** against \(q^k\binom rj(q-1)^j\). Exhaustive tests cover \(44\) parameter triples with \(q\in\{2,3,4\}\), \(k\in\{1,2,3\}\), \(n\in[k,k+4]\), restricted to \(q^n\le10000\). A total of \(17{,}413\) distinct centers were enumerated. The captured program output ends in `VERIFY_OK`; the proof itself, rather than those finite tests, establishes the unrestricted theorem.

## Relationship to prior work
Ye and Ge [1] introduced the same \(k\)-substring-edit notation and studied asymptotically efficient error-correcting constructions, their Section II discussing code-size bounds. The present claim instead determines every received-length layer and the **entire random-center spectrum of ball volumes**, without asserting new correcting-code constructions or a sharper redundancy bound. Lu and Zhang [2] studied **fixed** binary \((t,s)\)-bursts, established that their output balls have center-independent size for \(s\ge1\), and used this for packing bounds. That fixed-pair invariance is a known ingredient, not the claimed novelty. Xi, Sun, and Ge [3, Sec. II-C] restated the known burst-deletion count \(1+\#\{x_j\ne x_{j+k}\}\); their central investigation concerns a different ball, with deletion and insertion blocks at **independently chosen positions**. Their known deletion identity is explicitly reused in step 3. The distinct contribution here is the maximal-window identity for a *union of all* allowed edit lengths, its complete length-resolved formulas, and the exact binomial population law; none is asserted to improve the older fixed-pair facts.

## Limitations
The result concerns a single localized edit at the same site and counts **distinct outputs**. It does not determine optimal correcting-code sizes, multiple-edit balls, per-output inverse-list sizes, or independently located delete-and-insert errors. The novelty comparison is limited to the inspected primary literature and indexed mathematical research records; a differently named or unindexed equivalent result remains possible. The central fixed-burst and pure-deletion ingredients are pre-existing, and their individual formulas must not be presented independently as new.

## References
[1] Z. Ye and G. Ge, *Substring Edit Correcting Codes and Optimal Single Burst-Deletion Correcting Codes*, arXiv:2610.05696 (first submitted 2026-10-05), https://arxiv.org/abs/2610.05696.

[2] Z. Lu and Y. Zhang, *t-Deletion-s-Insertion-Burst Correcting Codes*, arXiv:2201.10259, version 2 (2022), https://arxiv.org/html/2201.10259v2.

[3] Y. Xi, Y. Sun, and G. Ge, *On the Fixed-Length-Burst Levenshtein Ball with Unit Radius*, arXiv:2506.07817 (2025), especially Lemma 2.3 and the definition allowing independently located operations, https://arxiv.org/html/2506.07817.
