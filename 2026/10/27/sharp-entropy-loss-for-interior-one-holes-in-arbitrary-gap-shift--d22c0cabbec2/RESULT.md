# Sharp entropy loss for interior-one holes in arbitrary gap shifts

## Finding

Let \(S\subseteq\mathbb N_0\) contain 0 and at least one positive integer. The two-sided \(S\)-gap shift \(X_S\) is the closure of bi-infinite concatenations of the words \(10^s\), \(s\in S\). Let \(Y_{S,k}\) be its subshift avoiding \(01^k0\), for \(k\ge2\). Put \(P(t)=\sum_{s\in S,\,s>0}t^{s+1}\), and let \(q\in(0,1)\) solve \(q+P(q)=1\). Then the loss in topological entropy per symbol satisfies
\[
h(X_S)-h(Y_{S,k})=\frac{(1-q)^2}{q^2(1+P'(q))}q^k+O_S(kq^{2k}).
\]
The leading term is exactly the cylinder mass \(\mu_S([01^k0])\) under the stationary maximal-entropy renewal measure of \(X_S\). In particular the ratio of entropy loss to that mass is \(1+O_S(kq^k)\). These conclusions do not require a finite or sofic presentation; the constants may depend on \(S\) and not on \(k\).

## Exact roots and their prior coverage

Use the closure definition of \(X_S\). The constraint on complete gaps alone is not a sufficient criterion for arbitrary finite words: if \(S\) is finite with maximum \(M\), even a word without ones cannot contain a zero run of length \(M+1\). Initial and terminal partial runs must extend into a concatenation of allowed gaps.

The exact entropies are \(-\log q\) and \(-\log q_k\), respectively, where \(q_k\) is the unique solution in \((0,1)\) of
\[
P(q_k)\left(\frac1{1-q_k}-q_k^{k-1}\right)=1.
\]
This fixed-hole root specializes Dillon's \(\mathcal S\)-graph entropy theorem [1, Theorem 1.1 and §4]. Take a two-vertex directed graph with arcs \(0\to1\) and \(1\to0\). The allowed zero-run lengths are \(S\cap\mathbb N\); in the perturbed shift the allowed one-run lengths are \(\mathbb N\setminus\{k\}\), and in the unperturbed shift they are \(\mathbb N\). Every complete run in a finite word meeting both sides of the run must have one of these lengths. Conversely, the partial zero runs at the ends of a word in \(Y_{S,k}\) can be completed to some allowed positive gap, as follows from membership in \(X_S\), and the partial one runs can always be completed to a length different from \(k\). This extends any such finite word to a bi-infinite concatenation of legal alternating runs, also when the word consists of only zeros or only ones. Hence the alternating-run closure is exactly the required subshift. In the generating matrix the two off-diagonal entries are the allowed length series for zero runs and one runs; its spectral radius is the square root of their product. For the perturbed shift the product is
\[
C_k(t)=\left(\sum_{s\in S,\,s>0} t^s\right)\left(\sum_{a\ge1,\,a\ne k} t^a\right)=P(t)\left(\frac1{1-t}-t^{k-1}\right).
\]
For the unperturbed shift it is \(G(t)=P(t)/(1-t)\), giving the equation for \(q\). The functions are positive-coefficient power series, strictly increasing from zero and tending to infinity as \(t\uparrow1\) (there is at least one permitted positive zero-run length and infinitely many one-run lengths). Also \(C_k(q)=1-(1-q)q^{k-1}<1\), so \(q_k>q\). The fixed-hole entropy equation and its renewal representation are starting points for the perturbation estimate, not new general root theorems.

## Sharp perturbation

The defining equations give
\[
G(q_k)-G(q)=P(q_k)q_k^{k-1},\qquad G'(q)=\frac{1+P'(q)}{1-q}>0.
\]
Fix \(r\) with \(q<r<1\). Since \(G(r)>1\) and \(P(r)r^{k-1}\to0\), eventually \(q_k<r\). On the compact interval \([q,r]\), \(G'\) is bounded below by a positive constant and the power series and their derivatives converge normally. By the mean-value theorem \(\delta_k=q_k-q=O_S(r^{k-1})\), so \(k\delta_k\to0\). Thus \(q_k^{k-1}=q^{k-1}(1+O_S(k\delta_k))\), and a second application of the root equation gives \(\delta_k=O_S(q^{k-1})\). Taylor expansion of \(G\) and \(P\) then yields
\[
\delta_k=\frac{(1-q)^2}{1+P'(q)}q^{k-1}+O_S(kq^{2k-2}).
\]
Expanding \(\log(q_k/q)\) gives the asserted entropy loss, with fixed inverse powers of \(q\) absorbed by the constant.

## Cylinder normalization

Under the stationary renewal process let successive gaps be independent at the renewals, with probabilities \(p_s=q^{s+1}\), \(s\in S\). These sum to 1. The mean spacing is \(M=\sum_s (s+1)p_s=q(1+P'(q))<\infty\). The gaps are identifiable from the symbol sequence at each one, and for the stationary process the entropy per symbol is the entropy per gap divided by the mean spacing. Here it equals \(-\sum_s p_s\log(p_s)/M=-\log q\), making the process a maximal-entropy measure. The occurrence of \(01^k0\) at a given site must start at the last zero of a positive gap, followed by \(k-1\) zero gaps and then a positive gap. Each qualifying gap contributes once to the cylinder frequency, so the renewal intensity \(1/M\) and independence give
\[
\mu_S([01^k0])=\frac{P(q)^2q^{k-1}}{M}=\frac{(1-q)^2}{q^2(1+P'(q))}q^k.
\]
The mass is positive, and division of the entropy expansion gives the claimed relative error.

## Relationship to prior work

Cheriyath [2, Theorem 1.3 and §4.1] excludes words \(0u0\) with an interior one in the general result and treats an exception for modular allowed-gap sets. The fixed-hole equation here follows from the general graph method [1]. The general positive-cylinder avoidance result [3, Proposition 7.2] gives a quantitative lower bound on the entropy gap, not its sharp linear leading term for this varying family. Local escape-rate results for nested good neighborhoods do not directly apply to the nonnested cylinders \([01^k0]\); finite-state Markov-hole results do not directly yield the arbitrary nonsofic case. The claim is specifically the sharp entropy comparison and its exact cylinder normalization for this hole family, not a result about all gaps lacking 0, arbitrary zero-ended holes or general escape rates.

The supplied finite-state numerical checker corroborates spectral-radius and asymptotic examples for finite \(S\). It does not certify the nonsofic range; the graph and analytic arguments above handle that range.

## References

1. T. Dillon, *Dynamics and entropy of \(\mathcal S\)-graph shifts*, [arXiv:2010.06031](https://arxiv.org/abs/2010.06031), Theorem 1.1 and §4.
2. H. Cheriyath, *A note on the perturbations of subshifts*, [arXiv:2506.20750v1](https://arxiv.org/html/2506.20750v1), Theorem 1.3 and §4.1.
3. Haydarov, Kadyrov, Makhmudov and Mamayusupov, *Effective intrinsic ergodicity for renewal-type potentials on S-gap shifts*, [arXiv:2606.17031](https://arxiv.org/abs/2606.17031), Theorem 1.1 and Proposition 7.2.
