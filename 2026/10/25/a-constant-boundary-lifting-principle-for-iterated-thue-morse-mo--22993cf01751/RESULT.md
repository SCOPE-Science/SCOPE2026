# A constant-boundary lifting principle for iterated Thue–Morse morphisms

## Finding

**Marked-boundary lifting theorem.** Let \(v\) be any finite binary word, with positions indexed from one, and let \(B\subseteq\{1,\ldots,|v|-1\}\) be a set of cuts. Suppose:

1. The adjacent ordered pairs \(v[b]v[b+1]\), for \(b\in B\), include each of \(00,01,10,11\).
2. Every distinct factor \(x\) of \(v\) with \(|x|\ge2\) has **some** occurrence \(v[i..j]=x\) and **some** \(b\in B\) satisfying \(i\le b<b+1\le j\). Thus the factor crosses both endpoints of a marked cut; merely hitting one marked position is not enough.

Write \(\mu(0)=01\), \(\mu(1)=10\), and \(H=2^k\). Then, for **every integer** \(k\ge0\), the scaled position set
\[
\Gamma_k=\{Hb:b\in B\}
\]
is a string attractor of \(\mu^k(v)\). In particular,
\[
\gamma(\mu^k(v))\le |B|\qquad(k\ge0).
\]

This yields finite, scale-independent, explicitly checkable sufficient conditions for a bounded attractor throughout an infinite family of morphic images. The conclusion applies to arbitrary binary seeds satisfying the two hypotheses, not solely to prefixes of one fixed infinite word.

## Assumptions and scope

A string attractor of a finite word \(w\) is a set of positions \(\Gamma\) such that every nonempty factor of \(w\) has at least one occurrence whose interval contains an element of \(\Gamma\). For a cut \(b\), **crossing** requires both positions \(b\) and \(b+1\) to lie in the occurrence. All positions and intervals are inclusive and one-based. The theorem holds for every finite binary seed \(v\), every qualifying set of marked cuts \(B\), and every nonnegative integer \(k\). There is no primitivity, aperiodicity, or prefix-of-fixed-point assumption. It asserts a uniform *upper bound*; no equality or characterization of all minimum attractors is claimed.

## Proof

**1. Universal middle-pair property.** Put \(U_k=\mu^k(0)\) and \(V_k=\mu^k(1)\), each of length \(H=2^k\). We prove by induction that, for every \(k\ge0\), every factor \(x\) of either \(U_k\) or \(V_k\) of length at least two has an occurrence crossing the *middle cut* between the two length-\(H\) blocks in \(\mu^k(pq)=\mu^k(p)\mu^k(q)\), for at least one ordered pair \(pq\in\{00,01,10,11\}\). Here \(x\) is allowed to be a factor of either block, and the pair \(pq\) can depend on \(x\).

At \(k=0\) each block has length one, so the assertion is empty. Assume it for \(k\), and consider a length-at-least-two factor \(x\) of \(\mu^{k+1}(a)\). Since \(\mu^{k+1}(a)=\mu^k(a)\mu^k(1-a)\), either \(x\) crosses this join or \(x\) is contained entirely in one of the two \(k\)-blocks. In the first case, use precisely the ordered \(k\)-block pair \(a(1-a)\) that it crosses. In the second case, the inductive hypothesis supplies an occurrence of \(x\) straddling the join in some \(\mu^k(p)\mu^k(q)\). In either case \(x\) has an occurrence at the join of two \(k\)-blocks of *some* ordered type \(pq\).

Now \(\mu^{k+1}(c)\mu^{k+1}(d)\) consists of four successive \(k\)-blocks \(c,(1-c),d,(1-d)\) after applying \(\mu^k\). The ordered pair of blocks at its central join is \((1-c,d)\). As \(c,d\) range independently over \(\{0,1\}\), these central pairs range over all four possible \(pq\). Therefore any occurrence straddling a \(k\)-block join can be copied to the central join between two \((k+1)\)-blocks with the same within-block offsets. This completes the induction.

**2. Factors spanning multiple inflated letters.** Partition \(\mu^k(v)\) into consecutive length-\(H\) blocks \(\mu^k(v[1]),\ldots,\mu^k(v[|v|])\). Let \(x\) be a factor that intersects at least two such blocks. Let \(y\) be the *shortest contiguous seed-block factor* containing this particular occurrence; thus \(|y|\ge2\), and the occurrence of \(x\) meets both its first and last blocks. By hypothesis 2, there is another occurrence of \(y\) in \(v\) that crosses a marked cut \(b\in B\). Copy the occurrence of \(x\) to the corresponding offsets inside the inflated copy \(\mu^k(y)\). Since \(x\) meets the first and last blocks, its copied occurrence spans **every internal block boundary** of \(y\), including the marked one at positions \(Hb,Hb+1\). It therefore intersects the selected position \(Hb\in\Gamma_k\).

**3. Factors lying within one inflated letter.** Let \(x\) have length at least two and an occurrence entirely contained in one length-\(H\) block. Part 1 produces an occurrence of \(x\) straddling the central join of \(\mu^k(pq)\) for some ordered pair \(pq\). By hypothesis 1, the seed \(v\) has a marked cut \(b\in B\) whose adjacent pair is exactly \(pq\). Hence \(\mu^k(v)\) contains the corresponding two inflated blocks with central join at \(Hb\), yielding an occurrence of \(x\) attracted by \(Hb\).

**4. Single letters.** The first symbol of \(\mu^k(a)\) equals \(a\); its last symbol equals \(a\) when \(k\) is even and \(1-a\) when \(k\) is odd. Hypothesis 1 includes marked cuts with left letters both \(0\) and \(1\). Thus among the selected positions \(Hb\), which are last symbols of inflated left letters, there are both a zero and a one, irrespective of parity of \(k\). Every single-letter factor is attracted. Parts 2–4 exhaust all nonempty factors, completing the proof.

## Verification

The self-contained \(verify.py\) constructs every factor and every occurrence directly. It checks the complete strict marked-cut condition on the fourteen-letter seed \(v=01101001100101\) with cuts \(B=\{3,6,8,11\}\). The marked pairs in order are \(10,00,11,01\). The numbers of distinct factors of lengths 2 through 14 are respectively \(4,6,9,10,9,8,7,6,5,4,3,2,1\), all crossing a marked cut in at least one occurrence.

As further direct finite checks, the checker verifies the scaled attractor for \(\mu^k(v)\) at \(k=0,1,2,3,4\), and for the separate seed \(00110\) with all its four cuts at \(k=0,1,2,3\). These computations are consistency checks only. The induction in the proof establishes the conclusion for every \(k\) and every qualifying seed; finite checks alone would not.

## Relationship to prior work

Faro–Marino–Pavone (2026) give a centered-occurrence construction and complete optimum classification for the *canonical* finite Thue–Morse words; their sixteen-factor coverage certificate motivated treating **both endpoints** of a selected boundary as a reusable primitive. Banbara et al. (2026, extended preprint) give a 720-state finite automaton encoding all four-position attractors of **prefixes of the Thue–Morse fixed point**, and a classification for complete dyadic blocks. Their automaton covers concrete examples that happen to be such prefixes; those examples are not asserted as new. Neither source states a uniform lifting theorem for **arbitrary independent binary seeds** and their iterated images, nor does an automaton restricted to one fixed point logically classify all independent seeds. Standard morphic-block arguments are related, and equivalent statements in less visible literature remain possible.

## Limitations

The seed condition is sufficient, not necessary; the theorem is not a classification of all attractor-bearing seeds. The requirement that every adjacent pair type be represented at marked cuts is used to handle factors wholly inside a single inflated letter; weakening it is not proved. The bound \(|B|\) need not equal the minimum attractor size. This result makes no claim to replace prior classifications of canonical Thue–Morse prefixes or to establish independent validation. An exact general lifting statement may exist under different terminology; historical novelty is limited to the literature inspected.

## References

1. Simone Faro, Francesco Pio Marino and Arianna Pavone, *Smallest String Attractors and Minimal Coverage Certificates of Thue–Morse Words* (first public 2026-10-07), arXiv:2610.10950, especially Sections 3–5.
2. Mutsunori Banbara et al., *The Smallest String Attractors of Fibonacci, Period-Doubling, and Thue–Morse Words*, arXiv:2602.16152, extended version, especially Section 5 and Appendix A.
3. Luke Schaeffer and Jeffrey Shallit, *String Attractors for Automatic Sequences*, on attractors of prefixes of fixed automatic sequences (background, not used for the proof).
