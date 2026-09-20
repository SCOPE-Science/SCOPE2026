# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The proof was checked along three independent interfaces.

First, the uniform lower envelope uses the exact primorial-support extremality already proved by Fatehizadeh: on the interval \(p_j\#\le n<p_{j+1}\#\), one has \(n/\varphi(n)\le\prod_{p\le p_j}p/(p-1)\). The de la Vallée Poussin error for \(\vartheta\) and the corresponding Mertens product error identify \(p_j\) with \(\log n\) to relative error \(e^{-c\sqrt{\log\log n}}\). Combining this with the two-term prime-number theorem gives the stated uniform lower envelope for \(\varphi(n)/\pi(n)\). The inequality \(A(n)\le\pi(n)\) transfers that envelope to \(\varphi(n)/A(n)\).

Second, primorials give matching witnesses. For \(P(x)=\prod_{p\le x}p\), Mertens' product and \(\vartheta(x)\sim x\) yield \(\varphi(P(x))/\pi(P(x))=e^{-\gamma}x/\log x\) with the same zero-free-region-scale relative error. Replacing \(\pi(P(x))\) by \(A(P(x))=\pi(P(x))-\pi(x)\) changes the ratio by an exponentially smaller amount. Perturbing the inverse point \(Y(h)\) multiplicatively by a constant times \(e^{-c\sqrt{\log h}}\) therefore brackets the last failure from both sides.

Third, the indexing and inversion were stress-tested. The equivalence \(B(n)>kA(n)\iff\varphi(n)>(k+1)A(n)\) requires the shift \(h=k+1\), while \(N_k\) uses \(h=k\). The relevant Lambert branch is \(W_{-1}\), not \(W_0\), because the threshold has \(Y(h)\to\infty\). Adding one to the last failure to obtain the least eventual threshold is negligible on the logarithmic scale. Expanding \(-W_{-1}\) gives the displayed \(\log k\), \(\log\log k\), constant, and \(1/\log k\) terms. No contradictory boundary case or sign error was found.

The proof is analytic; no numerical experiment is used as a substitute for a general argument.

## Originality — PASS, to the best of our knowledge

Fatehizadeh's arXiv:2609.13852v1 was inspected in full. It proves the classical liminf scale, the structural inequality \(M_k\le N_{k+1}\), six exact \(N_k\) values, five exact \(M_k\) values, and Conjecture 3.5 asserting \(M_k=N_{k+1}\) for all \(k\). Searches within the full text found no Lambert-W inversion, no asymptotic for \(N_k\) or \(M_k\) as \(k\to\infty\), and no logarithmic localization of the two threshold sequences.

The older fixed-level literature cited by the source was checked at the level relevant here. Moser's and Sanna's results concern the level \(k=1\); Birch--Singmaster's 1984 article gives an elementary eventual inequality; OEIS A080289 records finite record-low data for \(\varphi(n)/\pi(n)\). None of the located sources states the asymptotic threshold law, the Lambert-W formula, or the exponentially sharp comparison of \(\log M_k\) with \(\log N_{k+1}\).

External searches included exact and synonymous forms involving \(\varphi(n)>k\pi(n)\), eventual thresholds, record lows of \(\varphi/\pi\), \(N_k\), Lambert \(W\), and the scale \(e^\gamma k\log k\). No prior coverage was located. No inaccessible paper was identified whose title, abstract, or citation context specifically suggests the same \(k\to\infty\) threshold asymptotics. The main residual risk is unindexed contemporaneous work following the very recent motivating preprint.

No novelty is claimed for the prime number theorem, Mertens' product formula, zero-free-region error terms, primorial extremality in isolation, or Lambert-W asymptotics. The originality claim concerns their synthesis into an asymptotic theorem for these newly defined exact threshold sequences and the resulting near-equality of the shifted thresholds on the logarithmic scale.

## Value — PASS

The source paper turns the comparison of prime and nonprime totatives into exact threshold sequences and leaves a global equality conjecture. The present result determines the growth of both sequences, including several explicit asymptotic terms, and proves that the two conjecturally equal thresholds are already indistinguishable on the logarithmic scale up to an error smaller than every fixed inverse power of \(\log k\). This gives a quantitative large-parameter counterpart to the finite exact calculations and isolates the scale on which any future counterexample to the exact equality would have to live.

The result does not settle the exact equality conjecture and does not classify the precise last failures; those are substantive remaining problems.
