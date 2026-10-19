# Exact phase recovery and predictive information in the stationary random dimer shift

## Finding

Let \((W_j)_{j\in\mathbb Z}\) be the stationary unbiased random-orientation close-packed dimer process of Baake and van Enter. The latent pairing phase \(\Phi\) is an independent fair choice of the two alternating tilings of \(\mathbb Z\) by adjacent pairs; within each pair, assign \((+1,-1)\) or \((-1,+1)\) independently and equiprobably. Put \(B_n=(W_0,\ldots,W_{n-1})\), \(H_n=H(B_n)\) in bits, and \(h_2(p)=-p\log_2p-(1-p)\log_2(1-p)\).

**Theorem (complete finite-window phase and information law).** For every integer \(m\ge1\), the numbers of positive-probability length-\(n\) words are
\[
 |\operatorname{supp}B_{2m}|=3\cdot2^m-2,\qquad
 |\operatorname{supp}B_{2m+1}|=2^{m+2}-2.
\]
The odd formula also holds for \(m=0\). The optimal Bayesian error probability, with the fair prior, for guessing the true pairing phase from any length-\(n\) contiguous word is
\[
 \boxed{R_n=2^{-\lfloor n/2\rfloor-1}\quad(n\ge1).}
\]
The ambiguity event is **exactly** the event that the observed word alternates sign at every adjacent position. On that event the posterior probability of the phase pairing \((0,1),(2,3),\ldots\) is \(2/3\) for even length and \(1/2\) for odd length; outside it, the phase is recovered with certainty. The ambiguity-event probabilities are
\[
 \Pr(B_{2m}\text{ alternates})=3\cdot 2^{-m-1},\qquad
 \Pr(B_{2m+1}\text{ alternates})=2^{-m}.
\]
The full Shannon block entropies satisfy
\[
 \boxed{H_{2m}=m+\frac32-3\cdot 2^{-m-1}h_2(1/3)\quad(m\ge1),}
\]
\[
 \boxed{H_{2m+1}=m+2-2^{-m}\quad(m\ge0).}
\]
Consequently the entropy rate is exactly \(1/2\) bit per site, and the excess entropy, equivalently the mutual information between the infinite past and future, is exactly
\[
 \boxed{\lim_{n\to\infty}\big(H_n-n/2\big)=
 \lim_{n\to\infty}I(W_{-n},\ldots,W_{-1};W_0,\ldots,W_{n-1})=\frac32\text{ bits}.}
\]
In particular \(I(B_n;W_n,\ldots,W_{2n-1})=2H_n-H_{2n}\), giving an explicit finite-horizon predictive-information law from the displayed formulas. The first equal-adjacent-sign observation recovers the pairing phase without error; the number \(N\) of symbols needed for this event obeys \(\mathbb E N=9/2\).

## Assumptions and scope

The original two-sided process is defined by first drawing \(\Phi\) uniformly from \(\{0,1\}\). Under phase \(0\), pairs are \((2k,2k+1)\); under phase \(1\), pairs are \((2k-1,2k)\), for every \(k\in\mathbb Z\). Different pairs are independent, and either orientation has probability \(1/2\). The one-site shift exchanges phases, so this mixture is stationary. The theorem concerns the *unbiased* stationary measure, not arbitrary nonstationary weights or noisy observations. It concerns almost-sure phase inference: the two perfectly alternating bi-infinite sequences, on which pairing is not intrinsically distinguishable, have measure zero. Logs in entropy statements are base two.

## Proof

**1. Exact phase likelihoods.** Write \(L_0(w)=\Pr(B_n=w\mid\Phi=0)\) and \(L_1(w)=\Pr(B_n=w\mid\Phi=1)\). For \(n=2m\), phase \(0\) covers exactly \(m\) complete pairs and so gives likelihood \(2^{-m}\) on the \(2^m\) words with all internal even-start edges oppositely signed. Phase \(1\) meets \(m-1\) complete pairs and two boundary half-pairs; its likelihood is \(2^{-(m+1)}\) on \(2^{m+1}\) words with all internal odd-start edges oppositely signed. For \(n=2m+1\), each phase meets \(m\) complete and one half pair and has likelihood \(2^{-(m+1)}\) on \(2^{m+1}\) compatible words.

**2. The exact overlap.** The compatibility sets for the two phases intersect exactly at the two globally alternating sign words. Indeed, the even-start edges and the odd-start edges together cover every adjacent edge, so simultaneously respecting both phase constraints forces opposite adjacent signs throughout. The two alternating words conversely respect both. Inclusion–exclusion immediately gives the support cardinalities in the theorem.

**3. Bayesian decision and stopping time.** An observation containing any equal neighboring signs belongs to exactly one compatibility set and therefore reveals \(\Phi\) without error. On an alternating word of even length the phase likelihoods are in ratio \(2:1\); on one of odd length they coincide. With equal phase priors, the optimal error is
\[
 R_n=\sum_{w\in\{-1,1\}^n}\min\{L_0(w)/2,L_1(w)/2\}.
\]
Only two words contribute, each with the smaller half-weight \(2^{-m-2}\) when \(n=2m\) or \(n=2m+1\). Thus \(R_{2m}=R_{2m+1}=2^{-m-1}\), including \(m=0\) for the odd case. Adding the two mixture probabilities of alternating words yields the displayed ambiguity probabilities.

Let \(N\) be the first prefix length for which a pair of adjacent observations is equal. Then \(N\ge2\), \(\Pr(N>1)=1\), and for \(n\ge2\), \(\Pr(N>n)=\Pr(B_n\text{ alternates})\). Hence the tail-sum formula and two geometric series give
\[
 \mathbb EN=1+1+\sum_{m\ge1}3\cdot2^{-m-1}+\sum_{m\ge1}2^{-m}
 =2+\frac32+1=\frac92.
\]
The decreasing tails also prove \(N<\infty\) almost surely.

**4. Entropy.** Conditional on the phase, every compatible word has constant probability, so
\[
 H(B_{2m}\mid\Phi)=m+\tfrac12,\qquad
 H(B_{2m+1}\mid\Phi)=m+1.
\]
Since \(H(\Phi)=1\), the chain rule gives
\[
 H(B_n)=1+H(B_n\mid\Phi)-H(\Phi\mid B_n).
\]
The conditional phase entropy is zero off the alternating event. Its posterior entropy on that event is \(h_2(1/3)\) for even lengths, and \(1\) bit for odd lengths. Multiplication by the exact event probabilities yields both stated formulas. Dividing by \(n\) gives the entropy rate \(1/2\). For contiguous adjacent blocks of length \(n\), stationarity gives the identity \(I=2H_n-H_{2n}\); substituting the two explicit entropy formulas and passing to the limit gives \(3/2\) bits. The same value follows from \(\lim(H_n-n/2)\). These are exact infinite-limit deductions from formulas proved for every integer \(n\), not extrapolations from finite experiments.

## Verification

The accompanying standalone `verify.py` independently enumerates all words of lengths \(1\) through \(12\) with rational phase-conditioned cylinder probabilities. It checks unit mass, exact support sizes, Bayes risks, alternating masses, and numerical evaluation of the closed Shannon entropy formulas. Run it with `python3 verify.py`. No external dependencies or network access are needed. Its finite checks corroborate but do not replace the all-length combinatorial argument above.

## Relationship to prior work

Baake and van Enter [1, Sections 3–5] introduced exactly this stationary random-orientation dimer process and proved the diffraction/dynamical-spectrum contrast, including recovery of the hidden period-two eigenphase from an infinite observation sequence. Their spectral and factor statements, and their model, are prior results. The present theorem concerns different observables: the finite-window likelihood overlap, its **optimal** phase decision error, the exact complete Shannon block entropy sequence, and its \(3/2\)-bit infinite-past/future information limit. None of these evaluated finite-word information formulas is stated in the inspected full original paper. General one-dependent-process results [2] address classes of processes and factor structure but no identified full-text statement supplies the explicit formulas for this dimer measure. The excess-entropy and synchronization framework of Crutchfield and Feldman [3] supplies the standard information-theoretic interpretation, but their inspected article neither analyzes this dimer model nor states its evaluated phase likelihood or entropy constants. General entropy identities are standard and are used rather than claimed as original.

## Limitations

The result is specific to unbiased random pair orientation and equal prior probability of the two pairing phases. The original hidden period-two eigenphase and its almost-sure infinite-sequence recoverability are not new. The quantitative formulas follow from elementary but exact overlap counting and may be implicit in more general computational-mechanics literature not located by the searches; priority has not been independently certified. There is no claim about the noisy-observation problem, biased pair probabilities, general dimer tilings, higher-dimensional lattice models, or independent audit.

## References

[1] M. Baake and A. van Enter, *Close-packed dimers on the line: diffraction versus dynamical spectrum*, arXiv:1011.1628 (first posted 2010-11-07); Journal of Statistical Physics 143 (2011), 88–101, DOI: 10.1007/s10955-011-0163-5. Full open-access paper: https://link.springer.com/content/pdf/10.1007/s10955-011-0163-5.pdf.

[2] J. Aaronson, D. Gilat, M. Keane, and V. de Valk, *An algebraic construction of a class of one-dependent processes*, Annals of Probability 17 (1989), 128–143, DOI: 10.1214/aop/1176991499. Only bibliographic information and abstract were accessible for this comparison.

[3] J. P. Crutchfield and D. P. Feldman, *Regularities unseen, randomness observed: levels of entropy convergence*, arXiv:cond-mat/0102181 (2001); Chaos 13 (2003), 25–54, DOI: 10.1063/1.1530990.
