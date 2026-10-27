# Sharp entropy loss for interior-one holes in arbitrary gap shifts

## Finding

For every \(S\subseteq\mathbb N_0\) with \(0\in S\) and \(S\cap\mathbb N\ne\varnothing\), finite or infinite, the hole \(w_k=0 1^k0\), \(k\ge2\), has an exact pressure root and a uniform sharp first-order entropy-loss formula. With \(P_S(t)=\sum_{s\in S,\,s>0}t^{s+1}\), let \(q\) solve \(q+P_S(q)=1\), and let \(q_k\) solve

\[
P_S(q_k)\left(\frac{1}{1-q_k}-q_k^{k-1}\right)=1.
\]

Both roots exist uniquely in \((0,1)\), with \(q<q_k<1\). The exact entropies and sharp loss are

\[
h(X_S)=-\log q,\qquad h(Y_{S,k})=-\log q_k,
\]
\[
h(X_S)-h(Y_{S,k})=\frac{(1-q)^2}{q^2(1+P'_S(q))}q^k+O_S(kq^{2k}).
\]

Under the stationary maximal-entropy renewal measure \(\mu_S\), the cylinder mass equals the displayed leading term **exactly**:

\[
\mu_S([0 1^k 0])=\frac{(1-q)^2}{q^2(1+P'_S(q))}q^k,
\qquad \frac{h(X_S)-h(Y_{S,k})}{\mu_S([0 1^k 0])}=1+O_S(kq^k).
\]

This includes arbitrary nonsofic sets of allowed gaps; it makes no eventual-periodicity, tail-frequency or finite-type assumption.

## Assumptions and scope

The two-sided \(S\)-gap shift \(X_S\subseteq\{0,1\}^{\mathbb Z}\) is the closure of bi-infinite concatenations of return words \(10^s\) with \(s\in S\). A word is admissible when every finite sequence between two consecutive ones has a zero-run length in \(S\). For \(k\ge2\), \(Y_{S,k}\) consists of those configurations in \(X_S\) avoiding the contiguous word \(0 1^k0\). The notation \([w]\) denotes the cylinder at coordinates from \(0\) to \(|w|-1\). The implicit constants may depend on \(S\) but not on \(k\). Derivatives of \(P_S\) are ordinary derivatives on \((0,1)\), where all series converge absolutely. Because \(0\) and some positive gap are allowed, the entropy is positive and the renewal mean finite.

## Proof

**1. Regeneration and the hole.** Label each successive pair of ones by the intervening zero-run length \(s\in S\). Call a gap positive when \(s>0\) and zero when \(s=0\). A contiguous word \(0 1^k0\) occurs precisely when two consecutive positive gaps have exactly \(k-1\) zero gaps between them. In a configuration with infinitely many positive gaps in both directions, cut immediately before the one starting each positive gap. The resulting unique regenerative blocks have form \(10^s1^j\), with \(s\in S\cap\mathbb N\) and \(j\in\mathbb N_0\setminus\{k-1\}\). The block has length \(s+1+j\). Its generating function is

\[
C_k(t)=\sum_{s\in S,\,s>0}\sum_{j\ge0,\,j\ne k-1}t^{s+1+j}
=P_S(t)\left(\frac1{1-t}-t^{k-1}\right).
\]

This code is uniquely decipherable because each block begins with a one followed by a nonempty zero run. Finite words with two or more such markers are a concatenation of complete blocks plus two boundary fragments. For a fixed word length \(n\), each boundary fragment is of form \(1^a0^b1^c\) truncated at one or both ends and has at most polynomially many possibilities in \(n\). Words with at most one positive-gap marker also have polynomial complexity. Hence the word-count exponential growth of the full perturbed shift equals that of the renewal concatenations. The latter has growth radius at the unique positive root \(C_k(t)=1\); this follows directly by summing the nonnegative formal geometric series \(1/(1-C_k(t))\) and using positive aperiodic block lengths. Aperiodicity holds because the admissible \(j\)'s include consecutive integers, whatever \(k\ge2\). Consequently \(h(Y_{S,k})=-\log q_k\).

**2. Location of the roots.** In the unperturbed code all \(j\ge0\) are allowed, giving \(C_\infty(t)=P_S(t)/(1-t)\). Its root \(q\) satisfies \(P_S(q)=1-q\), equivalently \(\sum_{s\in S}q^{s+1}=1\), the usual gap-shift entropy equation. Both generating functions are continuous and strictly increasing for \(0<t<1\), vanish at zero and tend to infinity at one. Since \(C_k(q)=1-(1-q)q^{k-1}<1\), the perturbed root satisfies \(q_k>q\). Both lie below one.

**3. Sharp perturbation.** Write \(G(t)=P_S(t)/(1-t)\). The defining equation gives

\[
G(q_k)-G(q)=P_S(q_k)q_k^{k-1},\qquad
G'(q)=\frac{1+P'_S(q)}{1-q}>0.
\]

Fix any \(r\) with \(q<r<1\). Since \(G(r)>1\) and \(P_S(r)r^{k-1}\to0\), eventually \(q<q_k<r\). The mean-value theorem first gives \(q_k-q=O_S(r^{k-1})\), hence \(k(q_k-q)\to0\). Therefore \(q_k^{k-1}=q^{k-1}(1+O_S(k(q_k-q)))\). Applying the mean-value theorem a second time yields \(q_k-q=O_S(q^{k-1})\), and Taylor expansion now yields

\[
q_k-q=\frac{(1-q)^2}{1+P'_S(q)}q^{k-1}+O_S(kq^{2k-2}).
\]

Finally \(h(X_S)-h(Y_{S,k})=\log(q_k/q)\). Replacing the logarithm by its first-order Taylor expansion gives the stated coefficient and \(O_S(kq^{2k})\) remainder, since powers of the fixed \(q\) can be absorbed into the implicit constant.

**4. Cylinder mass.** Put \(p_s=q^{s+1}\) for \(s\in S\). They sum to one. A stationary renewal process obtained by concatenating independent \(10^s\) with probabilities \(p_s\) has mean renewal spacing

\[
M=\sum_{s\in S}(s+1)p_s=q(1+P'_S(q)).
\]

Its entropy per symbol equals \((-\sum_{s\in S}p_s\log p_s)/M=-\log q\); hence it is a maximal-entropy invariant measure of \(X_S\). The occurrence of \(0 1^k0\) begins at the last zero of a positive gap precisely when the next \(k-1\) gaps have length zero and the following gap is positive. Independence of successive gaps and stationary renewal intensity \(1/M\) therefore give

\[
\mu_S([0 1^k0])=\frac{P_S(q)^2q^{k-1}}M
=\frac{(1-q)^2}{q^2(1+P'_S(q))}q^k.
\]

Dividing the entropy expansion by this strictly positive expression gives the claimed relative error.

## Verification

The accompanying `verify.py` independently constructs finite-type higher-block adjacency matrices for five finite allowed-gap sets and four holes \(k=2,3,4,5\). It compares their Perron spectral radii with \(1/q_k\). It also checks the sharp leading term for three large values of \(k\) for each set. All 35 tests passed (`VERIFY_OK`). Finite computations do not establish the universal result, which follows from the regenerative and Taylor arguments above. Execution requires Python 3 and NumPy.

## Relationship to prior work

Cheriyath's *A note on the perturbations of subshifts* (2025), Theorem 1.3 and Section 4, explicitly leaves words beginning and ending in zero, with internal ones, unresolved for general \(S\)-gap shifts. Its Section 4.1 treats special modular gap sets. The present result addresses the structured family \(0 1^k0\), not arbitrary words of the form \(0u0\). Dillon's \(\mathcal S\)-graph entropy theorem supplies a general weighted-graph method that already implies many exact renewal-root calculations; the new assertion here is the **sharp all-gap-set perturbation asymptotic and exact cylinder-mass normalization**, not a claim that renewal-root equations were unknown. Prior work on SFT holes and finite-state Markov measures encompasses finite-type examples but does not itself assert this uniformly for unrestricted nonsofic gap sets.

## Limitations

The hole shape is fixed to \(0 1^k0\) with \(k\ge2\). No result is asserted for general \(0u0\), for sets lacking the zero gap, or for arbitrary multiword holes. The root formula follows classical weighted-renewal methods; the assessed distinction is the explicit sharp coefficient across all allowed-gap sets. Existing broad escape-rate theory may contain a different formulation implying the asymptotic; its full historical priority has not been independently audited. Spectral-radius numerics are finite checks only. No external independent review has occurred.

## References

1. H. Cheriyath, *A note on the perturbations of subshifts*, arXiv:2506.20750v1 (25 June 2025), Introduction and Section 4, especially Theorem 1.3 and Section 4.1. https://arxiv.org/html/2506.20750v1
2. T. Dillon, *Dynamics and entropy of \(\mathcal S\)-graph shifts*, arXiv:2010.06031 (2020), Theorem 1.2 and Section 4. https://arxiv.org/abs/2010.06031
3. N. Agarwal, H. Cheriyath and S. N. Tikekar, *On escape rate for subshift with Markov measure*, arXiv:2401.05118 (2024), Introduction and Sections 3–4. https://arxiv.org/abs/2401.05118
4. D. A. Lind, *Perturbations of Shifts of Finite Type*, SIAM J. Discrete Math. 2 (1989), 350–365. https://doi.org/10.1137/0402031
