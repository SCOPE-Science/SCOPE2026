# Logarithmic Shannon block entropy for the Brik sequence

## Finding
Let \(B_1=101\) and, for each integer \(j\geq1\), let \(B_{j+1}\) be \(B_j\) followed by the suffix of \(B_j\) obtained by removing its first \(j\) symbols. Let \(b\) be the infinite word having every \(B_j\) as a prefix. For a finite binary word \(u\), let \(\mu(u)\) be its limiting frequency among contiguous factors of \(b\). These frequencies exist and define a shift-invariant probability measure \(\mu\). Put
\[
 H_\mu(t)=-\sum_{u\in\{0,1\}^t}\mu(u)\log_2\mu(u),
\]
where a zero summand is interpreted as zero. **For every integer \(t\geq2\)**,
\[
 \boxed{H_\mu(t)\leq\log_2(t+2)+2\log_2\!\bigl(\log_2(t+2)+2\bigr)+7.}
\]
Consequently \(h_\mu=\lim_{t\to\infty}H_\mu(t)/t=0\), while the support of \(\mu\) is the entire golden-mean shift (binary sequences without adjacent zeros), whose topological entropy is \(\log_2((1+\sqrt5)/2)>0\). The new assertion is the **quantitative entropy bound** and its metric-versus-topological consequence, not the previously established existence and positivity of factor frequencies.

## Assumptions and scope
All indices of words are one-based. An occurrence of \(u\) of length \(d\) in a finite word means a start position at which all \(d\) letters lie in that word; overlaps count. Frequencies \(\mu(u)\) are limits over ordinary initial prefixes of every length, not merely selected substitution stages. The entropy is Shannon entropy in bits of the length-\(t\) block distribution. No ergodicity, maximality, independence, or formula for individual cylinder probabilities is claimed. The assertion covers every finite block length, and the entropy estimate is uniform in that length.

## Proof
**1. Lengths and limiting frequencies.** Set \(\ell_j=|B_j|\). Direct induction gives \(\ell_j=2^{j-1}+j+1\). For a word \(u\) of length \(d\), let \(T_j(u)\) be the number of its occurrences in \(B_j\), for stages with \(\ell_j\geq d\). The second portion of \(B_{j+1}\) is a suffix of \(B_j\). Thus it contributes all occurrences that start beyond position \(j\); only at most \(j\) existing starts are lost. New occurrences crossing the joining boundary number at most \(d-1\). Hence
\[
 T_{j+1}(u)=2T_j(u)-A_j+J_j,\qquad 0\leq A_j\leq j,\quad 0\leq J_j\leq d-1.
\]
The sequence \(T_j(u)/2^{j-1}\) is Cauchy, since consecutive differences have absolute value at most \((j+d)/2^j\). Since \(\ell_j/2^{j-1}\to1\), the ratios \(T_j(u)/\ell_j\) converge to a number \(\mu(u)\geq0\).

For clarity, this is also a limit along **all** prefix lengths. Let \(C_u(N)\) count occurrences wholly contained in the first \(N\) letters of \(b\), and let \(E_u(N)=C_u(N)-\mu(u)N\). For the unique stage \(j\) satisfying \(\ell_j\leq N<\ell_{j+1}\), write \(N=\ell_j+s\), where \(0\leq s\leq\ell_j-j\). Removing or adding at most \(2(d-1)\) boundary starts gives
\[
 C_u(N)=T_j(u)+C_u(j+s)-C_u(j)+O(d).
\]
We already know \(E_u(\ell_j)=o(\ell_j)\). The quantity \(\rho=\limsup_{N\to\infty}|E_u(N)|/N\) is finite. In the displayed recurrence, the term \(E_u(j)/N\) tends to zero, and
\[
 \frac{j+s}{\ell_j+s}\leq\frac{\ell_j}{2\ell_j-j}\longrightarrow\frac12.
\]
It follows that \(\rho\leq\rho/2\), so \(\rho=0\). Limits of all cylinder frequencies therefore exist; consistency of overlapping block counts and compactness give the shift-invariant Borel probability \(\mu\).

The full-support statement can be checked independently of the entropy argument. Shallit [1, Theorems 3 and 7] proves recurrence of \(b\) and shows that its factors are exactly the binary words avoiding `00`. If \(u\) occurs arbitrarily far into \(b\), choose an occurrence starting at \(p\), and the smallest \(j\) with \(p+d-1\leq\ell_j\). Taking \(p\) sufficiently large makes \(p\) enormously larger than \(j\). As long as the stage index stays below \(p\), each descendant of that occurrence remains beyond the deleted prefix and therefore appears in both halves at the next stage. For any fixed positive integer \(r\) with \(j+r<p\), this produces at least \(2^r\) occurrences in \(B_{j+r}\). Choose \(r\) of order \(\log_2(j+2)\) so that \(2^r>j+r+1\). The lower half of the occurrence recurrence above then yields
\[
 \mu(u)\geq\frac{T_{j+r}(u)-(j+r+1)}{2^{j+r-1}}>0.
\]
Thus every permissible cylinder has positive measure. This existence/full-support fact also appeared in an earlier frequency analysis and is included here only to make the entropy statement self-contained.

**2. A periodic superword containing every stage as a subsequence.** Fix an integer \(k\geq1\) and write \(U=B_k\), of length \(\ell_k\). The recursion implies inductively that for every \(n\geq k\), the word \(B_n\) is a scattered subsequence of
\[
 V_{n,k}=U^{2^{n-k}}.
\]
Indeed, each new stage concatenates a full copy and a prefix-deleted copy of its predecessor. The number of deleted symbols in such an embedding is exactly
\[
 D_{n,k}=2^{n-k}\ell_k-\ell_n=2^{n-k}(k+1)-(n+1),
\]
so
\[
 \lim_{n\to\infty}\frac{D_{n,k}}{\ell_n}=q_k:=\frac{k+1}{2^{k-1}}.
\]
No Hamming approximation or alignment at fixed output positions is asserted; this is an exact **subsequence embedding**.

**3. Cost of describing a typical block.** Fix integers \(k\geq1\) and \(t\geq2\). Use the embedding above, and choose a uniformly random start \(s\) among all \(\ell_n-t+1\) length-\(t\) windows of \(B_n\). Let \(e_i\) be the increasing index in \(V_{n,k}\) of the \(i\)-th retained symbol. Let
\[
 Z_s=(e_{s+t-1}-e_s+1)-t
\]
count deleted source positions **between** the first and last symbols of the window. Each deleted source symbol belongs to the source span of at most \(t-1\) output windows, hence
\[
 \mathbb E Z_s\leq\frac{(t-1)D_{n,k}}{\ell_n-t+1}.
\]
Given the phase \(e_s\bmod\ell_k\), the nonnegative integer \(Z_s=z\), and the subset of \(z\) deleted positions in the source interval of length \(t+z\), the observed length-\(t\) block is determined, since \(V_{n,k}\) is periodic with period \(\ell_k\). There are at most \(\ell_k\) phases and \(\binom{t+z}{z}\) masks. Writing \(H_n(t)\) for the Shannon entropy of the empirical length-\(t\) block distribution in \(B_n\), the entropy chain rule gives
\[
 H_n(t)\leq\log_2\ell_k+H(Z_s)+\mathbb E\log_2\binom{t+Z_s}{Z_s}.
\]
For a nonnegative integer random variable of mean \(m\), comparison with the geometric distribution of the same mean gives
\[
 H(Z_s)\leq G(m):=(m+1)\log_2(m+1)-m\log_2m.
\]
The function \(d\mapsto\log_2\binom{t+d}{d}\) has decreasing discrete increments \(\log_2(1+t/(d+1))\). Its concave interpolation is bounded by the concave function
\[
 F_t(m):=(t+m)h_2\!\left(\frac{m}{t+m}\right),
 \qquad h_2(x)=-x\log_2x-(1-x)\log_2(1-x).
\]
Jensen's inequality therefore bounds the expected logarithmic mask count by \(F_t(m)\). Both \(G\) and \(F_t\) are increasing. Taking \(n\to\infty\), using the established convergence of each length-\(t\) empirical distribution and the deleted-position mean estimate, proves the **finite-scale bound valid for every choice of \(k\)**:
\[
 H_\mu(t)\leq\log_2\ell_k+G((t-1)q_k)+F_t((t-1)q_k).
\]
This is a bound on actual Shannon entropy; it does not replace the distribution by the uniform law on its exponentially many possible factors.

**4. Explicit logarithmic estimate.** Put \(L=\log_2(t+2)\), so \(L\geq2\), and select
\[
 k=\left\lceil L+2\log_2(L+2)+3\right\rceil.
\]
Elementary inequalities give \(k+1\leq4(L+2)\),
\[
 4(t+2)(L+2)^2\leq2^{k-1}<8(t+2)(L+2)^2,
\]
and therefore \(\ell_k\leq9(t+2)(L+2)^2\) and \(m=(t-1)q_k\leq1/(L+2)\leq1/4\). In particular \(G(m)<1\). Furthermore, using \(\log_2(1+x)\leq x\log_2e\),
\[
 F_t(m)\leq m\log_2\!\bigl(e(1+t/m)\bigr)
 \leq\frac{L+\log_2(L+2)+\log_2 e}{L+2}<2.
\]
The preceding finite-scale bound now yields
\[
 H_\mu(t)< L+2\log_2(L+2)+\log_2 9+3
 <L+2\log_2(L+2)+7,
\]
as claimed. Finally, \(H_\mu(t)/t\to0\). By [1, Corollary 8], the language has \(F_{t+2}\) factors of length \(t\), and hence topological entropy \(\log_2((1+\sqrt5)/2)\). This completes the proof.

## Verification
The standalone `check_entropy.py` reconstructs stages through \(B_{15}\), creates explicit embeddings into repeated shorter stages, tests equality of the retained symbols, verifies the window-deletion-count inequality for several window lengths, and checks the numerical estimates used to choose \(k\) over more than one thousand values. Its associated `check_output.txt` is reproducible with `python check_entropy.py`. The finite calculations test the identities but **do not** certify the infinite convergence, the entropy inequality for all lengths, or novelty; these follow respectively from the proofs and the literature comparison above.

## Relationship to prior work
Shallit's original May 8, 2026 work [1] established the unusual combination of a full golden-mean factor language, recurrence without uniform recurrence, and a well-defined symbol density. A prior frequency analysis (opaque record `8508728d-2547-41f9-9c6b-a88eb78cb63e`) established the existence and positivity of every factor frequency and genericity of the resulting measure, but **made no Shannon block-entropy assertion**. These properties are recalled, not counted as new. In contrast, a full-support invariant measure on the golden-mean shift can have positive entropy (for example its Parry measure), so the earlier statements do not imply the present bound. Standard zero-entropy facts for some rank-one systems may give qualitative analogues; the explicit logarithmic-scale estimate in this specific, heavily overlapping prefix-deletion construction is the substantive new assertion.

## Limitations
The upper bound is not claimed optimal, and no matching asymptotic lower bound is established. The proof does not show the measure is ergodic or uniquely invariant, and does not bound the **topological** factor complexity by a polynomial. Historical-priority risk remains for an unindexed equivalent bound in rank-one or symbolic coding literature. A qualitative entropy-zero theorem in a more general class would not by itself subsume the stated quantitative block-length estimate.

## References
[1] Jeffrey Shallit, *Brik's sequence: a strange recursion*, arXiv:2605.07542v1, first publicly submitted 2026-05-08; full text at https://arxiv.org/abs/2605.07542 . Theorems 3 and 7 and Corollary 8 give the recurrence and factor-language inputs.

[2] Earlier factor-frequency analysis, record `8508728d-2547-41f9-9c6b-a88eb78cb63e` (background deduplication reference, not a source of the entropy result).
