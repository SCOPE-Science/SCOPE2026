# Scientific review: sharp rare-event law for equitable wild numbers

## Correctness — PASS

The asserted probability and expectation bounds follow from four checked ingredients: (i) the established two-colour identity \(W=\kappa(G_{\rm red})+\kappa(G_{\rm blue})-2\); (ii) the exact without-replacement isolation probabilities \((N-m)_{n-1}/(N)_{n-1}\) and \((m)_{n-1}/(N)_{n-1}\); (iii) the uniform cut-event inequality \(\Pr(\text{no edge across a prescribed cut})\le e2^{-k(n-k)}\), yielding \(O(n^2 4^{-n})\) for all small nontrivial components; and (iv) the uniform logarithmic falling-factorial expansion producing \(e^{-1}\). The two event-class inclusions controlling \(W\ge2\) and \(W=1\) are explicit. The parameter boundary \(n\ge4\), the treatment of odd edge counts, the component conventions and the meaning of the asymptotic error are all specified. The standard-library verifier independently checked all \(359423\) balanced labelled red-edge selections for \(n=4,5,6,7\), and the exact rational isolation identity held in all four cases. These finite checks are not used to infer the theorem.

## Originality — PASS, with residual priority risk

Dawkins–Nappo–Tong–Zimbizi (arXiv:2610.22142, Sections 2 and 3.2.1) introduce the precise problem and establish \(\mathbb E W\to0\), but not the sharp \(4/e\) constant, explicit \(p_n\), or the probability hierarchy distinguishing one wild edge from at least two. The classic Bender–Canfield–McKay fixed-edge connected-graph enumeration (1990, Theorem 1 and Corollary 3) was compared: its displayed multiplicative asymptotic for the connectivity probability does not supply an asymptotic equivalent for an exponentially small *failure* probability. A large fixed-edge-graph literature remains relevant; an uninspected theorem providing sharp exponentially small disconnection probabilities might imply part of this finding. In addition, the related 1992 paper was checked at abstract level only. Consequently no claim of comprehensive historical priority or independent validation is made.

## Mathematical value — PASS

The motivating recent work left an explicit random-equitable problem with only a vanishing limit. This theorem determines the leading rare-event rate, the nontrivial conditioning factor \(e^{-1}\) relative to independent colour assignments, a uniform exponentially smaller error in the exact finite-population singleton term, and the structural fact that nonzero wild numbers are asymptotically almost always one. These invariants quantify failure frequency and typical repair cost for random balanced two-channel complete networks. They are not merely an exact rewrite of the previously known vanishing bound.

## Limitations and comparison

The result is confined to uniformly random globally equitable two-colourings of simple complete graphs. It does not concern per-vertex equitable degrees, proper edge-colourings, arbitrary host graphs or larger palettes. Historical-priority uncertainty concerns any sharper dense \(G(n,m)\) connectivity asymptotics in the classical literature; the proof here is supplied independently and the claim avoids presenting fixed-edge connectivity as an original field-wide principle.

Self-review: passed. Independent audit: not yet performed.
