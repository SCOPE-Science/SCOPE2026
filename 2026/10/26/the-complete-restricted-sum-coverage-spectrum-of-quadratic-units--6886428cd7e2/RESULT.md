# The complete restricted-sum coverage spectrum of quadratic units modulo prime squares

## Finding
For each odd prime \(p\), write
\[
Q_p=\{u^2\bmod p^2: p\nmid u\},\qquad N=|Q_p|=p(p-1)/2.
\]
For \(0\le k\le N\), let \(\Sigma_k(Q_p)\subseteq\mathbb Z/p^2\mathbb Z\) be the set of all sums of \(k\) **pairwise distinct** members of \(Q_p\). A cardinality is *universal* if \(\Sigma_k(Q_p)=\mathbb Z/p^2\mathbb Z\). The complete universal-cardinality spectrum is:

* \(p=3\): empty;
* \(p=5\): exactly \(\{4,6\}\); moreover \(\Sigma_5(Q_5)\) omits exactly \(0,10,15\) modulo \(25\);
* \(p\ge7\): all \(3\le k\le N-3\), with \(k=2,N-2\) additionally universal exactly when \(p\equiv1\pmod4\). No other \(k\) is universal.

Thus the intermediate-cardinality coverage threshold is exactly \(3\) for all \(p\ge7\), and the middle cardinality at \(p=5\) is a genuine gap between two universal cardinalities.

## Assumptions and scope
All primes are odd; the ambient additive group is the residue ring \(\mathbb Z/p^2\mathbb Z\). The phrase quadratic residue means a **unit square**, excluding nonunits. Distinctness refers to residues modulo \(p^2\), not to their square roots. The statement addresses **every** target residue and **every** cardinality from \(0\) through \(N\).

## Proof
**1. Fibers of quadratic units.** Set \(h=(p-1)/2\) and let \(H\subset\mathbb F_p^\times\) be the nonzero squares. For each \(r\in H\), its \(p\) lifts \(r+pt\), \(t\in\mathbb F_p\), are all unit squares modulo \(p^2\). Indeed, any lift of a nonzero square \(r\) has a square root by the elementary Hensel lift, because \(2u\not\equiv0\pmod p\). Hence \(Q_p\) is a disjoint union of \(h\) full fibers, each of size \(p\). Label lifts by \(t\in\mathbb F_p\). A *layer* contains exactly one element of each fiber with a common label \(t\), giving \(p\) disjoint layers of size \(h\).

**2. Coverage for \(p\ge7\) and \(3\le k\le N/2\).** Thus \(h\ge3\). Write \(k=qh+r\), where \(q=\lfloor(k-3)/h\rfloor\) and \(3\le r\le h+2\). Choose integers \(1\le t_1,t_2,t_3\le h-1\) with \(t_1+t_2+t_3=r\); this is possible since \(3\le r\le h+2\le3(h-1)\). We select \(q\) complete layers and \(t_i\) elements from each of three additional distinct layers. The number of used layers is \(q+3\le p-1\), since \(k\le N/2=ph/2\) and \(p\ge7\).

For a subset \(A\subseteq\mathbb F_p\), denote by \(\Sigma_t(A)\) its distinct-\(t\)-term sumset. The Dias da Silva--Hamidoune restricted-sum theorem gives
\[
|\Sigma_t(H)|\ge\min\{p,t(h-t)+1\}\ge h\quad(1\le t\le h-1).
\]
The Cauchy--Davenport theorem therefore yields
\[
\Sigma_{t_1}(H)+\Sigma_{t_2}(H)+\Sigma_{t_3}(H)=\mathbb F_p,
\]
because the cardinality is at least \(\min\{p,3h-2\}=p\). The complete layers contribute a fixed residue, and the three partially filled layers can attain **any** reduction of the sum modulo \(p\).

Fix one such \(k\)-set with reduction \(b\pmod p\). At least one residue fiber contains \(c\) selected elements, with \(1\le c\le q+3\le p-1\). Translate **all selected** elements of this fiber by \(pu\), for an arbitrary \(u\in\mathbb F_p\), keeping the other selected elements unchanged. This preserves distinctness (translation permutes the fiber) and changes the sum by \(cpu\pmod{p^2}\). Since \(c\not\equiv0\pmod p\), these sums attain every lift of \(b\) modulo \(p^2\). Hence \(\Sigma_k(Q_p)=\mathbb Z/p^2\mathbb Z\).

The complement map \(S\mapsto Q_p\setminus S\) sends sums \(b\) of \(k\) elements bijectively to sums \(T-b\) of \(N-k\) elements, where \(T=\sum_{x\in Q_p}x\). Therefore \(k\) is universal if and only if \(N-k\) is universal. We obtain all \(3\le k\le N-3\).

**3. The two-element boundary.** For \(p\equiv3\pmod4\), a sum of two unit squares cannot be divisible by \(p\), because \(-1\) is not a quadratic residue modulo \(p\). Thus \(k=2\) is not universal. For \(p\equiv1\pmod4\) and \(p\ge13\), every \(t\in\mathbb F_p\) is a sum of two members of \(H\). If \(t\ne0\), character orthogonality gives
\[
|\{(a,b)\in H^2:a+b=t\}|=\frac{p-3-2\chi(t)}4\ge2,
\]
where \(\chi\) is the quadratic character. For \(t=0\), take \(a\in H\) and \(b=-a\in H\). Each chosen pair has lifts of their prescribed reductions that add to any specified target \(B\pmod{p^2}\), and two distinct lifts can always be chosen even when the reductions agree (there are \(p\ge5\) possible choices for the first lift, at most one causing equality). Thus \(k=2\) covers every target, and by complementation so does \(k=N-2\).

Since \(N<p^2\), neither \(k=1\) nor \(k=N-1\) can be universal. Cardinalities \(k=0,N\) each produce one sum and are not universal.

**4. Small primes.** For \(p=3\), the three quadratic units all reduce to \(1\pmod3\), so every fixed cardinality has only one possible reduction modulo \(3\), and none is universal. For \(p=5\), the two residue fibers are those over \(1\) and \(4\), each containing five elements. A \(k\)-set choosing \(j\) from the first fiber reduces in sum to \(2j-k\pmod5\), where \(\max(0,k-5)\le j\le\min(5,k)\). For \(k=4\), the five choices \(j=0,1,2,3,4\) give every residue class, and the translated-fiber argument supplies every lift. Complementation yields \(k=6\). For \(k=5\), choices \(j=1,2,3,4\) supply all four nonzero residue classes modulo \(5\), but to obtain reduction \(0\) one needs \(j=0\) or \(j=5\). These are the *entire* individual fibers, whose fixed sums are respectively \(20\) and \(5\pmod{25}\). Thus exactly \(0,10,15\) are missing. For \(k\le3\), reductions \(2j-k\) range over at most four classes and cannot cover \(\mathbb F_5\). The remaining cases follow by complementation. This completes the classification.

## Verification
The accompanying portable Python program uses exact cyclic bit masks to compute, simultaneously for every cardinality, all attainable sums of distinct quadratic units. It checks every target and every cardinality for \(p=3,5,7,11,13,17,19,23\), and confirms the three missing five-element targets at \(p=5\). Running it prints `VERIFY_OK`. The finite check is diagnostic; the infinite-prime classification rests on the proof above.

## Relationship to prior work
The September 26, 2025 work of Xu and Wang investigates additive representations using a primitive root and a power residue in prime-power residue rings. The present theorem instead asks for the complete cardinality-by-cardinality restricted-sum coverage of the unit-square set, with all summands square residues and pairwise distinct. Ding and Zhou's 2019 work concerns subset sums of power values over Galois rings, including sufficient conditions for coverage; the precise relation to its unavailable full text remains a substantive priority for independent literature checking. The present result gives a sharp all-prime, all-cardinality classification and explicitly identifies the exceptional middle-cardinality failure modulo \(25\), rather than a large-parameter sufficient condition. The restricted-sum lower bound of Dias da Silva and Hamidoune and Cauchy--Davenport are used as established input theorems, not claimed as new.

## Limitations
The theorem is specific to unit squares modulo *prime squares*. It does not classify higher-power residue classes, nonunit squares, or arbitrary Galois rings. The proof uses standard restricted-addition theorems; no independent audit has been performed. Full texts of two highly related earlier Galois-ring subset-sum papers and the 2025 prime-power representation paper were not obtainable here, so possible prior implicit coverage remains an originality risk. Unavailable texts are not asserted to be noncovering.

## References
1. Z. Xu and J. Wang, *Elements of Z_q^* represented as sum of two special elements*, Indian Journal of Pure and Applied Mathematics, first public September 26, 2025, DOI: 10.1007/s13226-025-00871-w.
2. Y. Ding and H. Zhou, *Subset sums over Galois rings*, Journal of Number Theory 205 (2019), 148–169, DOI: 10.1016/j.jnt.2019.05.004.
3. Y. Ding and H. Zhou, *Subset sums over Galois rings. II*, Journal of Number Theory 252 (2023), 118–136, DOI: 10.1016/j.jnt.2023.05.003.
4. J. A. Dias da Silva and Y. O. Hamidoune, *Cyclic spaces for Grassmann derivatives and additive theory*, Bulletin of the London Mathematical Society 26 (1994), 140–146.
5. A. L. Cauchy (1813) and H. Davenport (1935), the classical Cauchy--Davenport sumset inequality.
