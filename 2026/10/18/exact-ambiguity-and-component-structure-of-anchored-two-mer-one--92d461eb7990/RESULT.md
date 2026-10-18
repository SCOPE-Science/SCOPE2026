# Exact ambiguity and component structure of anchored two-mer one-read deletion

## Finding
Fix an alphabet \(\Sigma\) of size \(q\ge2\), an integer \(n\ge1\), and arbitrary fixed two-symbol left and right adapters \(u=(u_0,a)\), \(v=(b,v_1)\). For an input \(x\in\Sigma^n\), transmit the consecutive ordered overlapping two-symbol reads of \(uxv\); delete exactly one read other than the two adapter reads. Two distinct inputs are **confusable** if some received vectors agree. The following statements describe the complete channel.

**Component theorem.** Put \(z=axb\) and let \(\operatorname{red}(z)\) be the word obtained by collapsing each maximal constant run to one symbol. Two input words belong to the same connected component of the confusability graph if and only if their reduced padded words agree. More precisely, fix a reduced word \(c_0c_1\cdots c_k\), with \(c_0=a\), \(c_k=b\), and \(c_i\ne c_{i+1}\). Its component is the graph on all positive integer vectors \((r_0,\ldots,r_k)\) with \(\sum r_i=n+2\). Two vectors are adjacent exactly when one is obtained from the other by transferring one unit from one coordinate to another. The component has
\[
\binom{n+1}{k}\quad\text{vertices and}\quad \binom{k+1}{2}\binom nk\quad\text{edges}.
\]
The number of components with \(k\) transitions is
\[
W_k(a,b)=(J-I)^k_{ab}=
\begin{cases}
\displaystyle\frac{(q-1)^k+(q-1)(-1)^k}{q},& a=b,\\[3pt]
\displaystyle\frac{(q-1)^k-(-1)^k}{q},& a\ne b,
\end{cases}
\]
where \(J\) is the all-ones \(q\)-by-\(q\) matrix and \(I\) is the identity. Here \(0\le k\le n+1\); terms with \(W_k=0\) contribute nothing.

**Exact total-edge law.** The number \(E_{q,n}(a,b)\) of unordered confusable input pairs is
\[
E_{q,n}(a,b)=\sum_{k=0}^{n+1}W_k(a,b)\binom{k+1}{2}\binom nk.
\]
For \(n\ge3\), it simplifies to the adapter-independent expression
\[
\boxed{ E_{q,n}(a,b)=\frac{n(q-1)q^{n-3}}{2}\bigl((n-1)(q-1)+2q\bigr). }
\]
At \(n=1\), the edge count is \(0\) for \(a=b\) and \(1\) otherwise; at \(n=2\), it is \(3(q-1)\) for \(a=b\) and \(3q-4\) otherwise.

**Complete inverse-ambiguity law.** A received read vector is *consistent* if the final symbol of each two-symbol read equals the initial symbol of the next read. Every inconsistent received vector has exactly one possible input. The number of consistent vectors with precisely \(r\) possible inputs is
\[
\boxed{N_r^{\mathrm{cons}}=\binom n{r-1} W_{r-1}(a,b),\qquad 1\le r\le n+1.}
\]
There are exactly \((n+1)(q-1)q^{n-1}\) inconsistent received vectors, each with one possible input. Thus the number of all distinct received vectors is
\[
\boxed{q^{n-1}\bigl[1+(n+1)(q-1)\bigr].}
\]
The inverse-list histogram counts each received vector once, not once per position producing it.

## Assumptions and scope
The alphabet is any fixed labeled set with \(q\ge2\). The transmitted source has exactly \(n\ge1\) editable symbols. Each adapter has length two, is known at the decoder, and is not deleted. The channel deletes exactly one of the \(n+1\) interior two-symbol reads from the \(n+3\) reads of \(uxv\); it introduces no other errors. The graph is simple, undirected, and has one vertex for each source word, not each read vector. In the binomial expressions \(\binom nk=0\) for \(k>n\). The boundary symbols \(u_0\) and \(v_1\) may be arbitrary, including equal to \(a\) or \(b\).

## Proof
**1. Every received vector falls into two exactly described types.** Index the positions of \(z=axb\) by \(0,\ldots,n+1\), and call the full two-mer reads \(p_0=(u_0,z_0)\), \(p_i=(z_{i-1},z_i)\) for \(1\le i\le n+1\), and \(p_{n+2}=(z_{n+1},v_1)\). If \(p_i\) is removed, the only possibly inconsistent consecutive retained reads are \(p_{i-1}\) and \(p_{i+1}\). Their suffix and prefix are \(z_{i-1}\) and \(z_i\), respectively. If these differ, their location in the received vector identifies the deleted read index \(i\); the missing read is uniquely \((z_{i-1},z_i)\). This reconstructs the entire original read vector and hence the unique source word. An inconsistent output can never have a second parent.

If instead \(z_{i-1}=z_i\), the deleted read is a constant pair and every retained adjacency is consistent. The reads uniquely spell a string that differs from \(uxv\) by deleting one symbol from a maximal constant run of \(z\) of length at least two. Removing the unchanged two outer adapter symbols gives a length-\(n+1\) word \(y\) with endpoints \(a,b\). Conversely, for any such \(y\), inserting one additional copy of the symbol in any of its maximal constant runs gives a distinct admissible word \(z\) of length \(n+2\) with the same retained read vector after a suitable constant-read deletion. No other parent is possible. Therefore every consistent output has precisely \(\#\operatorname{red}(y)\) parents, one for each run.

**2. Graph structure.** Two distinct words are confusable only through a consistent output, since an inconsistent output has a unique parent. Two parents of a consistent output arise by expanding one run of the same shorter word \(y\), so their reduced words agree and their run-length vectors differ by moving one unit between two coordinates. Conversely, any two positive run-length vectors related by one such move both shorten, by one run-symbol deletion each, to their componentwise minimum vector; the latter still has all coordinates positive and specifies a common consistent output. This proves the asserted exact adjacency criterion. The positive compositions of \(n+2\) into \(k+1\) parts are connected under unit transfers: repeatedly transfer surplus units into the first part. Their number is \(\binom{n+1}{k}\).

A composition has degree \(k\) times its number of parts at least two, since each such donor may transfer one unit to any of the other \(k\) parts. For each particular donor coordinate, exactly \(\binom nk\) positive compositions have that coordinate at least two. Summing degrees over the \(k+1\) coordinates and halving gives \(\binom{k+1}{2}\binom nk\) edges, including the zero-edge cases.

There are \((J-I)^k_{ab}\) reduced symbol itineraries with exactly \(k\) transitions from \(a\) to \(b\), because each transition changes the letter. The eigenvalues of \(J-I\) are \(q-1\) on constants and \(-1\) on their orthogonal complement, giving the displayed \(W_k\).

**3. Total edges.** Summing component edges gives the first expression for \(E_{q,n}(a,b)\). Since \(\binom nk=0\) when \(k=n+1\), this is the \((a,b)\) entry of
\[
\frac12\sum_{k=0}^{n}k(k+1)\binom nk(J-I)^k
=\frac{n(n-1)}2(J-I)^2J^{n-2}+n(J-I)J^{n-1}.
\]
The identity follows by differentiating \((I+\lambda(J-I))^n\) twice and once, or by the binomial identity for \(k(k+1)\). For \(n\ge3\), \(J^{n-2}=q^{n-3}J\), \((J-I)J=(q-1)J\), and therefore the whole matrix is the displayed scalar multiple of \(J\). This proves adapter independence and the closed formula. Directly evaluating the finite sum at \(n=1,2\) yields the two exceptions.

**4. Output histogram.** By Step 1, a consistent output is equivalent to a word \(y\) of length \(n+1\) with fixed endpoints \(a,b\). If its reduced itinerary has \(r\) runs, the run lengths form a positive composition of \(n+1\) into \(r\) parts, with \(\binom n{r-1}\) choices. There are \(W_{r-1}(a,b)\) possible itineraries. Step 1 shows the inverse-list size equals \(r\), proving the histogram. There are \(q^{n-1}\) such consistent vectors in total.

An inconsistent output is uniquely associated to the input and the location of its nonconstant deleted two-mer, because the gap position is observable. Summing nonconstant internal reads over all \(q^n\) inputs counts these outputs. Each of the \(n+1\) internal adjacent-symbol pairs of \(z\) differs in exactly \((q-1)q^{n-1}\) source words (also when the pair meets one fixed endpoint). Hence the inconsistent-output count is \((n+1)(q-1)q^{n-1}\). Adding the consistent count completes the proof.

## Verification
`CHECK.py` independently builds complete readout sets from the physical overlapping-read definition and groups their distinct parents; it does not use the proof's generated adjacency or histogram when obtaining those sets. For every ordered pair of boundary symbols, it compares the brute-force confusability edges against independently generated unit-transfer edges, compares every inverse-list histogram against the closed counting formulas, and verifies the total-edge and output counts. The executed checks cover \(2\le q\le5\), with \(1\le n\le9\) when \(q=2\), \(1\le n\le6\) when \(q=3\), \(1\le n\le5\) when \(q=4\), and \(1\le n\le4\) when \(q=5\), a total of 270 distinct parameter-and-adapter combinations. `CHECK.out` is the recorded output. The all-length result rests on the combinatorial proof, not the finite checks.

## Relationship to prior work
Xie and Chen (2026, Section II) introduce the anchored adversarial nanopore readout model and analyze consistency completion, redundancy bounds and code constructions rather than the complete one-deletion confusability graph. Ye and Ge (2026, Lemma II.1 and Theorem III.1) analyze single-read deletions using periodic-pattern shortening and give efficient correcting codes. Their structural observation that a consistent single-deletion completion shortens a constant run is an important precursor.

Hanania and Yaakobi (2025, Lemma 1) identify an equivalence between two-symbol labeling-code correction and a derivative-domain zero-deletion code. Thus **the reduction to a zero-deletion channel is not new**. What is determined here is the full unconditioned graph decomposition into positive-composition transfer graphs, its exact edge enumerator—including the nonobvious boundary-independent closed form at every \(n\ge3\)—and the complete inverse-list multiplicity law. Their subsequent Theorems 3–4 bound code cardinalities via zero-run statistics; they do not state these graph and readout-count formulas.

Chee and Vu (2020) previously investigated deletion-correcting codes for symbol-pair reads, including the binary case. Their paper is a plausible further source of equivalent formulations; only its abstract and later accounts were available for comparison, so its full details are an unresolved literature-access risk. A separately indexed reconstruction graph whose edges mean *two common ordinary one-deletion descendants* is a different graph and its edge formula does not imply the present one-read two-mer enumeration.

## Limitations
This is a channel-specific exact classification: one deleted ordered two-symbol read, fixed length-two adapters, known ordered read sequence, and no substitutions, duplications or multiple deletions. It does not establish optimal code cardinality or decoding complexity for a general error budget. The zero-deletion reduction and single-deletion run-shortening premises have predecessors; the claimed distinct contribution is the complete enumerated graph and inverse ambiguity statistics. An unindexed older zero-deletion graph enumeration, especially in the inaccessible 2020 article, could subsume part of this result. Independent validation has not been performed.

## References
1. H. Xie and Z. Chen, “First-order optimal codes for an adversarial nanopore channel,” arXiv:2601.21236 (first public January 29, 2026), Section II. https://arxiv.org/abs/2601.21236
2. Z. Ye and G. Ge, “Deletion-Correcting Codes for the \(\ell\)-Symbol Read Channel,” arXiv:2606.26434 (first public June 24, 2026), Sections II and III-A. https://arxiv.org/abs/2606.26434
3. D. Hanania and E. Yaakobi, “Error-Correcting Codes for Labeled DNA Sequences,” arXiv:2511.01280 (first public as arXiv version November 3, 2025; a conference version appeared in June 2025), Section III-A. https://arxiv.org/abs/2511.01280
4. Y. M. Chee and V. K. Vu, “Codes Correcting Synchronization Errors for Symbol-Pair Read Channels,” IEEE ISIT 2020, pp. 746–750, DOI:10.1109/ISIT44484.2020.9174064.
